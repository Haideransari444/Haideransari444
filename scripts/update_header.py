from pathlib import Path
from shutil import copyfile
from datetime import datetime
from zoneinfo import ZoneInfo

ASSETS = Path("assets")
LIVE = ASSETS / "farm-header-live.png"

now = datetime.now(ZoneInfo("Asia/Karachi"))
hour = now.hour

if 5 <= hour < 9:
    src = ASSETS / "header-dawn.png"
    mode = "dawn"
elif 9 <= hour < 17:
    src = ASSETS / "header-day.png"
    mode = "day"
elif 17 <= hour < 20:
    src = ASSETS / "header-dusk.png"
    mode = "dusk"
else:
    src = ASSETS / "header-night.png"
    mode = "night"

if not src.exists():
    raise FileNotFoundError(f"Missing source header: {src}")

copyfile(src, LIVE)
print(f"Updated {LIVE} using {src} for mode={mode}, Karachi time={now.isoformat()}")
