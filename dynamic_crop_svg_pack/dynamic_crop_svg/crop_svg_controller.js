/**
 * Crop SVG controller
 * Values are normalized so you can plug real app data into the scene.
 * timeOfDay: 0 to 24
 * cropHealth: 0 to 1
 * seasonProgress: 0 spring, .5 summer, .75 autumn, 1 winter
 * wind: 0 to 1
 * walkingSpeed: 0 slow, 1 fast
 */

export function cropTheme(values = {}) {
  const timeOfDay = clamp(values.timeOfDay ?? currentHour(), 0, 24);
  const cropHealth = clamp(values.cropHealth ?? 0.86, 0, 1);
  const seasonProgress = clamp(values.seasonProgress ?? 0.35, 0, 1);
  const wind = clamp(values.wind ?? 0.45, 0, 1);
  const walkingSpeed = clamp(values.walkingSpeed ?? 0.55, 0, 1);

  const daylight = sunStrength(timeOfDay);
  const warmEdge = sunriseSunsetStrength(timeOfDay);
  const night = 1 - daylight;

  const season = seasonPalette(seasonProgress, cropHealth);
  const sky = skyPalette(timeOfDay, daylight, warmEdge, night);

  const sunX = lerp(170, 1030, timeOfDay / 24);
  const sunY = 240 - Math.sin((timeOfDay / 24) * Math.PI) * 180;

  return {
    "--sky-top": sky.top,
    "--sky-mid": sky.mid,
    "--sky-bottom": sky.bottom,
    "--sun-x": `${Math.round(sunX)}px`,
    "--sun-y": `${Math.round(sunY)}px`,
    "--sun-size": `${Math.round(42 + daylight * 28 + warmEdge * 12)}px`,
    "--sun-color": sky.sun,
    "--sun-glow": sky.glow,
    "--horizon": mix("#132417", "#44613b", daylight),
    "--crop-back": season.back,
    "--crop-mid": season.mid,
    "--crop-front": season.front,
    "--crop-highlight": season.highlight,
    "--soil": mix("#23150d", "#5b351e", daylight),
    "--shadow": mix("#030609", "#1a2416", daylight),
    "--haze-opacity": String(round(0.06 + warmEdge * 0.3 + daylight * 0.08)),
    "--star-opacity": String(round(night * 0.75)),
    "--moon-opacity": String(round(night * 0.8)),
    "--sun-opacity": String(round(Math.max(daylight, warmEdge * 0.85))),
    "--wind-speed": `${round(5.8 - wind * 4.4)}s`,
    "--walk-speed": `${round(11 - walkingSpeed * 7.5)}s`,
    "--blade-sway": `${round(1.2 + wind * 6.5)}deg`,
    "--field-saturation": String(round(0.62 + cropHealth * 0.55))
  };
}

export function applyCropTheme(svgElement, values = {}) {
  const theme = cropTheme(values);
  for (const [key, value] of Object.entries(theme)) {
    svgElement.style.setProperty(key, value);
  }
  return theme;
}

function currentHour() {
  const d = new Date();
  return d.getHours() + d.getMinutes() / 60;
}

function sunStrength(hour) {
  if (hour < 5.5 || hour > 19.3) return 0;
  const t = (hour - 5.5) / (19.3 - 5.5);
  return Math.pow(Math.sin(Math.PI * t), 0.72);
}

function sunriseSunsetStrength(hour) {
  const sunrise = Math.exp(-Math.pow((hour - 6.3) / 1.55, 2));
  const sunset = Math.exp(-Math.pow((hour - 18.2) / 1.65, 2));
  return clamp(Math.max(sunrise, sunset), 0, 1);
}

function skyPalette(hour, daylight, warmEdge, night) {
  const noon = Math.exp(-Math.pow((hour - 12.4) / 5.1, 2));
  const dawnDusk = warmEdge;

  const top = mix(mix("#071021", "#3568a8", daylight), "#5f416d", dawnDusk * 0.55);
  const mid = mix(mix("#101d3b", "#79b7e8", daylight), "#f08f54", dawnDusk);
  const bottom = mix(mix("#182340", "#d8f2ff", daylight), "#ffd08a", dawnDusk);

  const sun = mix(mix("#f2f5ff", "#ffe082", daylight), "#ffb15e", dawnDusk);
  const glow = mix(mix("#7e8bb8", "#ffe59a", daylight), "#ff6f3c", dawnDusk);

  return { top, mid, bottom, sun, glow, noon, night };
}

function seasonPalette(progress, health) {
  const spring = ["#4f7d2b", "#78a63d", "#2f6327", "#d9e76d"];
  const summer = ["#78963a", "#a6a845", "#496b29", "#eadf64"];
  const autumn = ["#8d6d2f", "#b17d35", "#5d3c21", "#f0b14a"];
  const winter = ["#53654c", "#64745d", "#334035", "#cfd9c7"];

  let a;
  let b;
  let t;
  if (progress < 0.45) {
    a = spring; b = summer; t = progress / 0.45;
  } else if (progress < 0.78) {
    a = summer; b = autumn; t = (progress - 0.45) / 0.33;
  } else {
    a = autumn; b = winter; t = (progress - 0.78) / 0.22;
  }

  const dull = 1 - health;
  return {
    back: mix(mix(a[0], b[0], t), "#5d563f", dull * 0.5),
    mid: mix(mix(a[1], b[1], t), "#756648", dull * 0.45),
    front: mix(mix(a[2], b[2], t), "#3a3329", dull * 0.6),
    highlight: mix(mix(a[3], b[3], t), "#9b8b62", dull * 0.5)
  };
}

function clamp(v, min, max) {
  return Math.max(min, Math.min(max, v));
}

function lerp(a, b, t) {
  return a + (b - a) * t;
}

function round(n) {
  return Math.round(n * 1000) / 1000;
}

function mix(hexA, hexB, t) {
  t = clamp(t, 0, 1);
  const a = hexToRgb(hexA);
  const b = hexToRgb(hexB);
  return rgbToHex({
    r: Math.round(lerp(a.r, b.r, t)),
    g: Math.round(lerp(a.g, b.g, t)),
    b: Math.round(lerp(a.b, b.b, t))
  });
}

function hexToRgb(hex) {
  const clean = hex.replace("#", "");
  return {
    r: parseInt(clean.slice(0, 2), 16),
    g: parseInt(clean.slice(2, 4), 16),
    b: parseInt(clean.slice(4, 6), 16)
  };
}

function rgbToHex({ r, g, b }) {
  return `#${[r, g, b].map(v => v.toString(16).padStart(2, "0")).join("")}`;
}
