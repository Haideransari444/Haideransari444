from __future__ import annotations

import argparse
import datetime as dt
import math
import pathlib
import re
from dataclasses import dataclass

ROOT = pathlib.Path(__file__).resolve().parent
TEMPLATE = ROOT / "crop-fields-dynamic.svg"

@dataclass
class Values:
    time_of_day: float
    crop_health: float = 0.86
    season_progress: float = 0.35
    wind: float = 0.45
    walking_speed: float = 0.55


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.replace("#", "")
    return int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#" + "".join(f"{clamp(int(v), 0, 255):02x}" for v in rgb)


def mix(a: str, b: str, t: float) -> str:
    t = clamp(t, 0, 1)
    ar, ag, ab = hex_to_rgb(a)
    br, bg, bb = hex_to_rgb(b)
    return rgb_to_hex((round(lerp(ar, br, t)), round(lerp(ag, bg, t)), round(lerp(ab, bb, t))))


def sun_strength(hour: float) -> float:
    if hour < 5.5 or hour > 19.3:
        return 0.0
    t = (hour - 5.5) / (19.3 - 5.5)
    return math.sin(math.pi * t) ** 0.72


def sunrise_sunset_strength(hour: float) -> float:
    sunrise = math.exp(-((hour - 6.3) / 1.55) ** 2)
    sunset = math.exp(-((hour - 18.2) / 1.65) ** 2)
    return clamp(max(sunrise, sunset), 0, 1)


def season_palette(progress: float, health: float) -> dict[str, str]:
    spring = ["#4f7d2b", "#78a63d", "#2f6327", "#d9e76d"]
    summer = ["#78963a", "#a6a845", "#496b29", "#eadf64"]
    autumn = ["#8d6d2f", "#b17d35", "#5d3c21", "#f0b14a"]
    winter = ["#53654c", "#64745d", "#334035", "#cfd9c7"]

    if progress < 0.45:
        a, b, t = spring, summer, progress / 0.45
    elif progress < 0.78:
        a, b, t = summer, autumn, (progress - 0.45) / 0.33
    else:
        a, b, t = autumn, winter, (progress - 0.78) / 0.22

    dull = 1 - health
    return {
        "--crop-back": mix(mix(a[0], b[0], t), "#5d563f", dull * 0.5),
        "--crop-mid": mix(mix(a[1], b[1], t), "#756648", dull * 0.45),
        "--crop-front": mix(mix(a[2], b[2], t), "#3a3329", dull * 0.6),
        "--crop-highlight": mix(mix(a[3], b[3], t), "#9b8b62", dull * 0.5),
    }


def theme(values: Values) -> dict[str, str]:
    h = clamp(values.time_of_day, 0, 24)
    health = clamp(values.crop_health, 0, 1)
    season = clamp(values.season_progress, 0, 1)
    wind = clamp(values.wind, 0, 1)
    walk = clamp(values.walking_speed, 0, 1)

    daylight = sun_strength(h)
    warm = sunrise_sunset_strength(h)
    night = 1 - daylight

    top = mix(mix("#071021", "#3568a8", daylight), "#5f416d", warm * 0.55)
    mid = mix(mix("#101d3b", "#79b7e8", daylight), "#f08f54", warm)
    bottom = mix(mix("#182340", "#d8f2ff", daylight), "#ffd08a", warm)
    sun = mix(mix("#f2f5ff", "#ffe082", daylight), "#ffb15e", warm)
    glow = mix(mix("#7e8bb8", "#ffe59a", daylight), "#ff6f3c", warm)

    sun_x = lerp(170, 1030, h / 24)
    sun_y = 240 - math.sin((h / 24) * math.pi) * 180

    return {
        "--sky-top": top,
        "--sky-mid": mid,
        "--sky-bottom": bottom,
        "--sun-x": f"{round(sun_x)}px",
        "--sun-y": f"{round(sun_y)}px",
        "--sun-size": f"{round(42 + daylight * 28 + warm * 12)}px",
        "--sun-color": sun,
        "--sun-glow": glow,
        "--horizon": mix("#132417", "#44613b", daylight),
        "--soil": mix("#23150d", "#5b351e", daylight),
        "--shadow": mix("#030609", "#1a2416", daylight),
        "--haze-opacity": f"{0.06 + warm * 0.3 + daylight * 0.08:.3f}",
        "--star-opacity": f"{night * 0.75:.3f}",
        "--moon-opacity": f"{night * 0.8:.3f}",
        "--sun-opacity": f"{max(daylight, warm * 0.85):.3f}",
        "--wind-speed": f"{5.8 - wind * 4.4:.3f}s",
        "--walk-speed": f"{11 - walk * 7.5:.3f}s",
        "--blade-sway": f"{1.2 + wind * 6.5:.3f}deg",
        "--field-saturation": f"{0.62 + health * 0.55:.3f}",
        **season_palette(season, health),
    }


def render(values: Values, out: pathlib.Path) -> None:
    svg = TEMPLATE.read_text(encoding="utf-8")
    values_map = theme(values)
    for key, value in values_map.items():
        svg = re.sub(rf"{re.escape(key)}:[^;]+;", f"{key}:{value};", svg)
    out.write_text(svg, encoding="utf-8")


def current_hour() -> float:
    now = dt.datetime.now()
    return now.hour + now.minute / 60


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a themed dynamic crop fields SVG.")
    parser.add_argument("--time", type=float, default=current_hour(), help="Time of day from 0 to 24.")
    parser.add_argument("--health", type=float, default=0.86, help="Crop health from 0 to 1.")
    parser.add_argument("--season", type=float, default=0.35, help="Season progress from 0 to 1.")
    parser.add_argument("--wind", type=float, default=0.45, help="Wind from 0 to 1.")
    parser.add_argument("--walk", type=float, default=0.55, help="Walking speed from 0 to 1.")
    parser.add_argument("--out", type=pathlib.Path, default=ROOT / "generated-crop-fields.svg")
    args = parser.parse_args()

    render(
        Values(
            time_of_day=args.time,
            crop_health=args.health,
            season_progress=args.season,
            wind=args.wind,
            walking_speed=args.walk,
        ),
        args.out,
    )
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
