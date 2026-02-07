---
title: "julia_sets.glsl"
---

```glsl
#version 300 es
precision highp float;

uniform vec2 u_resolution;
uniform vec2 u_center;
uniform float u_zoom;
uniform vec2 u_c;

out vec4 fragColor;

vec3 palette(float t) {
    // Attempt at a continuous, smooth coloring. For each color channel,
    // the expression is: 0.5 + 0.5 * cos(2π * (t + offset))
    return 0.5 + 0.5 * cos(6.28318 * (t + vec3(0.0, 0.1, 0.2)));
}

void main() {
    // Map fragment coordinates to complex plane
    vec2 uv = (gl_FragCoord.xy - u_resolution * 0.5) / min(u_resolution.x, u_resolution.y);
    vec2 z = uv / u_zoom + u_center;

    // Iterate z = z^2 + c
    float i;
    for(i = 0.0; i < 256.0; i++) {
        if(dot(z, z) > 4.0) break;  // |z|^2 > 4 means escape
        z = vec2(z.x*z.x - z.y*z.y, 2.0*z.x*z.y) + u_c;
    }

    if(i >= 256.0) {
        // Point is in the Julia set (didn't escape)
        fragColor = vec4(0, 0, 0, 1);
    } else {
        // Smooth iteration count to avoid color banding
        // smooth_i = i - log2(log2(|z|^2)) + 4
        float smooth_i = i - log2(log2(dot(z, z))) + 4.0;
        fragColor = vec4(palette(smooth_i * 0.02), 1);
    }
}
```

## Mandelbrot Picker

```glsl
#version 300 es
precision highp float;

uniform vec2 u_resolution;
uniform vec2 u_c;  // Current c value to mark

out vec4 fragColor;

void main() {
    vec2 uv = (gl_FragCoord.xy - u_resolution * 0.5) / min(u_resolution.x, u_resolution.y);

    // Mandelbrot uses c as the varying parameter, z starts at 0
    vec2 c = uv * 2.5 - vec2(0.5, 0.0);  // Shift to show main cardioid
    vec2 z = vec2(0);

    float i;
    for(i = 0.0; i < 128.0; i++) {
        if(dot(z, z) > 4.0) break;
        z = vec2(z.x*z.x - z.y*z.y, 2.0*z.x*z.y) + c;
    }

    vec3 col;
    if(i >= 128.0) {
        col = vec3(0.1, 0.1, 0.15);  // Inside the set
    } else {
        col = vec3(0.2, 0.3, 0.4) * (i / 128.0);  // Outside
    }

    // Draw red marker for current c value
    vec2 cPos = (u_c + vec2(0.5, 0.0)) / 2.5;
    vec2 pixelC = (cPos + 0.5) * u_resolution;
    if(length(gl_FragCoord.xy - pixelC) < 4.0) {
        col = vec3(1, 0.3, 0.3);
    }

    fragColor = vec4(col, 1);
}
```
