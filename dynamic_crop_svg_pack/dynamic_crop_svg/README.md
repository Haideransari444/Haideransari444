# Dynamic Crop Fields SVG

A reusable animated SVG for a farm themed GitHub profile or web page.

## Files

- `crop-fields-dynamic.svg`: the animated SVG scene.
- `crop_svg_controller.js`: browser helper that converts values into SVG CSS variables.
- `preview.html`: local preview with sliders.
- `generate_svg.py`: static SVG generator for GitHub README usage.

## Values you can plug in

```js
applyCropTheme(svgElement, {
  timeOfDay: 18.3,       // 0 to 24
  cropHealth: 0.86,     // 0 to 1
  seasonProgress: 0.35, // 0 spring, .5 summer, .75 autumn, 1 winter
  wind: 0.45,           // 0 to 1
  walkingSpeed: 0.55    // 0 to 1
});
```

## GitHub README note

GitHub does not allow JavaScript inside README markdown. For GitHub, use `generate_svg.py` through a GitHub Action and commit the generated SVG on a schedule.

Example local command:

```bash
python generate_svg.py --time 18.2 --health 0.9 --season 0.4 --wind 0.55 --walk 0.7 --out generated-crop-fields.svg
```

Then in README:

```md
<img src="./generated-crop-fields.svg" width="100%" alt="Dynamic animated crop fields" />
```

## Browser app usage

Inline the SVG in your page, then call the controller:

```js
import { applyCropTheme } from './crop_svg_controller.js';

const svg = document.querySelector('#farmScene');
applyCropTheme(svg, {
  timeOfDay: new Date().getHours() + new Date().getMinutes() / 60,
  cropHealth: 0.86,
  seasonProgress: 0.35,
  wind: 0.45,
  walkingSpeed: 0.55
});
```
