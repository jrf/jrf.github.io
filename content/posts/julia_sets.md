---
title: "Julia Sets Explorer"
date: 2025-06-01T10:00:00-06:00
categories: [fractals, complex-analysis]
math: true
---

The Julia set for a complex number $c$ is the boundary between points that escape to infinity and those that remain bounded under iteration of:

$$z_{n+1} = z_n^2 + c$$

Each value of $c$ produces a different fractal. Connected Julia sets correspond to points inside the Mandelbrot set; disconnected "dust" fractals come from points outside.

**Controls:** Click the Mandelbrot set (left) to choose $c$. Drag to pan, scroll to zoom the Julia set.

<div id="julia-container" style="display: flex; gap: 16px; flex-wrap: wrap; margin: 20px 0;">
  <div style="flex: 1; min-width: 280px;">
    <div style="font-weight: bold; margin-bottom: 6px;">Mandelbrot Set</div>
    <canvas id="mandelbrot" width="400" height="400" style="border: 1px solid #333; cursor: crosshair; width: 100%; height: auto;"></canvas>
    <div id="c-value" style="font-family: monospace; font-size: 12px; margin-top: 5px;">c = -0.7 + 0.27i</div>
  </div>
  <div style="flex: 1; min-width: 280px;">
    <div style="font-weight: bold; margin-bottom: 6px;">Julia Set</div>
    <canvas id="julia" width="400" height="400" style="border: 1px solid #333; cursor: grab; width: 100%; height: auto;"></canvas>
  </div>
</div>

<script>
(function() {
  const vsSource = `#version 300 es
    in vec2 a_pos;
    void main() { gl_Position = vec4(a_pos, 0, 1); }`;

  const fsJulia = `#version 300 es
    precision highp float;
    uniform vec2 u_resolution;
    uniform vec2 u_center;
    uniform float u_zoom;
    uniform vec2 u_c;
    out vec4 fragColor;

    vec3 palette(float t) {
      return 0.5 + 0.5 * cos(6.28318 * (t + vec3(0.0, 0.1, 0.2)));
    }

    void main() {
      vec2 uv = (gl_FragCoord.xy - u_resolution * 0.5) / min(u_resolution.x, u_resolution.y);
      vec2 z = uv / u_zoom + u_center;

      float i;
      for(i = 0.0; i < 256.0; i++) {
        if(dot(z, z) > 4.0) break;
        z = vec2(z.x*z.x - z.y*z.y, 2.0*z.x*z.y) + u_c;
      }

      if(i >= 256.0) {
        fragColor = vec4(0, 0, 0, 1);
      } else {
        float smooth_i = i - log2(log2(dot(z,z))) + 4.0;
        fragColor = vec4(palette(smooth_i * 0.02), 1);
      }
    }`;

  const fsMandelbrot = `#version 300 es
    precision highp float;
    uniform vec2 u_resolution;
    uniform vec2 u_c;
    out vec4 fragColor;

    void main() {
      vec2 uv = (gl_FragCoord.xy - u_resolution * 0.5) / min(u_resolution.x, u_resolution.y);
      vec2 c = uv * 2.5 - vec2(0.5, 0.0);
      vec2 z = vec2(0);

      float i;
      for(i = 0.0; i < 128.0; i++) {
        if(dot(z, z) > 4.0) break;
        z = vec2(z.x*z.x - z.y*z.y, 2.0*z.x*z.y) + c;
      }

      vec3 col;
      if(i >= 128.0) {
        // Inside the set - subtle dark blue
        col = vec3(0.05, 0.08, 0.15);
      } else {
        // Outside - color by iteration count
        // High i = many iterations before escape = near the boundary
        float t = i / 128.0;
        vec3 outer = vec3(0.02, 0.03, 0.08);  // Far from set (escaped quickly)
        vec3 edge = vec3(0.3, 0.5, 0.85);     // Near boundary - bright blue glow
        col = mix(outer, edge, pow(t, 0.6));  // pow < 1 widens the glow
      }

      // Draw marker for current c
      vec2 cPos = (u_c + vec2(0.5, 0.0)) / 2.5;
      vec2 pixelC = (cPos + 0.5) * u_resolution;
      if(length(gl_FragCoord.xy - pixelC) < 4.0) {
        col = vec3(1, 0.3, 0.3);
      }

      fragColor = vec4(col, 1);
    }`;

  function createShader(gl, type, source) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      console.error(gl.getShaderInfoLog(shader));
      return null;
    }
    return shader;
  }

  function createProgram(gl, vs, fs) {
    const program = gl.createProgram();
    gl.attachShader(program, vs);
    gl.attachShader(program, fs);
    gl.linkProgram(program);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
      console.error(gl.getProgramInfoLog(program));
      return null;
    }
    return program;
  }

  function setupGL(canvas, fsSource) {
    const gl = canvas.getContext('webgl2');
    if (!gl) { console.error('WebGL2 not supported'); return null; }

    const vs = createShader(gl, gl.VERTEX_SHADER, vsSource);
    const fs = createShader(gl, gl.FRAGMENT_SHADER, fsSource);
    const program = createProgram(gl, vs, fs);

    const posBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, posBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, 1,1]), gl.STATIC_DRAW);

    const posLoc = gl.getAttribLocation(program, 'a_pos');
    gl.enableVertexAttribArray(posLoc);
    gl.vertexAttribPointer(posLoc, 2, gl.FLOAT, false, 0, 0);

    return { gl, program };
  }

  const juliaCanvas = document.getElementById('julia');
  const mandelbrotCanvas = document.getElementById('mandelbrot');
  const cValueEl = document.getElementById('c-value');

  const julia = setupGL(juliaCanvas, fsJulia);
  const mandelbrot = setupGL(mandelbrotCanvas, fsMandelbrot);

  if (!julia || !mandelbrot) return;

  let c = [-0.7, 0.27];
  let center = [0, 0];
  let zoom = 0.35;
  let dragging = false;
  let lastMouse = [0, 0];

  // Expose setC globally for the preset buttons
  window.setC = function(re, im) {
    c = [re, im];
    center = [0, 0];
    zoom = 0.35;
    cValueEl.textContent = `c = ${c[0].toFixed(3)} ${c[1] >= 0 ? '+' : '-'} ${Math.abs(c[1]).toFixed(3)}i`;
    render();
  };

  function renderJulia() {
    const { gl, program } = julia;
    gl.viewport(0, 0, juliaCanvas.width, juliaCanvas.height);
    gl.useProgram(program);
    gl.uniform2f(gl.getUniformLocation(program, 'u_resolution'), juliaCanvas.width, juliaCanvas.height);
    gl.uniform2f(gl.getUniformLocation(program, 'u_center'), center[0], center[1]);
    gl.uniform1f(gl.getUniformLocation(program, 'u_zoom'), zoom);
    gl.uniform2f(gl.getUniformLocation(program, 'u_c'), c[0], c[1]);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
  }

  function renderMandelbrot() {
    const { gl, program } = mandelbrot;
    gl.viewport(0, 0, mandelbrotCanvas.width, mandelbrotCanvas.height);
    gl.useProgram(program);
    gl.uniform2f(gl.getUniformLocation(program, 'u_resolution'), mandelbrotCanvas.width, mandelbrotCanvas.height);
    gl.uniform2f(gl.getUniformLocation(program, 'u_c'), c[0], c[1]);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
  }

  function render() {
    renderJulia();
    renderMandelbrot();
  }

  function updateC(x, y) {
    const rect = mandelbrotCanvas.getBoundingClientRect();
    const px = (x - rect.left) / rect.width;
    const py = 1 - (y - rect.top) / rect.height;
    c[0] = (px - 0.5) * 2.5 * 2 - 0.5;
    c[1] = (py - 0.5) * 2.5 * 2;
    cValueEl.textContent = `c = ${c[0].toFixed(3)} ${c[1] >= 0 ? '+' : '-'} ${Math.abs(c[1]).toFixed(3)}i`;
    center = [0, 0];
    zoom = 0.35;
    render();
  }

  mandelbrotCanvas.addEventListener('click', e => updateC(e.clientX, e.clientY));
  mandelbrotCanvas.addEventListener('mousemove', e => {
    if (e.buttons === 1) updateC(e.clientX, e.clientY);
  });

  juliaCanvas.addEventListener('mousedown', e => {
    dragging = true;
    lastMouse = [e.clientX, e.clientY];
    juliaCanvas.style.cursor = 'grabbing';
  });

  window.addEventListener('mouseup', () => {
    dragging = false;
    juliaCanvas.style.cursor = 'grab';
  });

  juliaCanvas.addEventListener('mousemove', e => {
    if (!dragging) return;
    const dx = (e.clientX - lastMouse[0]) / juliaCanvas.width / zoom;
    const dy = (e.clientY - lastMouse[1]) / juliaCanvas.height / zoom;
    center[0] -= dx * 2;
    center[1] += dy * 2;
    lastMouse = [e.clientX, e.clientY];
    render();
  });

  juliaCanvas.addEventListener('wheel', e => {
    e.preventDefault();
    const factor = e.deltaY > 0 ? 0.9 : 1.1;
    zoom *= factor;
    render();
  }, { passive: false });

  // Handle touch for mobile
  juliaCanvas.addEventListener('touchstart', e => {
    if (e.touches.length === 1) {
      dragging = true;
      lastMouse = [e.touches[0].clientX, e.touches[0].clientY];
    }
  });

  juliaCanvas.addEventListener('touchmove', e => {
    if (!dragging || e.touches.length !== 1) return;
    e.preventDefault();
    const dx = (e.touches[0].clientX - lastMouse[0]) / juliaCanvas.width / zoom;
    const dy = (e.touches[0].clientY - lastMouse[1]) / juliaCanvas.height / zoom;
    center[0] -= dx * 2;
    center[1] += dy * 2;
    lastMouse = [e.touches[0].clientX, e.touches[0].clientY];
    render();
  }, { passive: false });

  juliaCanvas.addEventListener('touchend', () => { dragging = false; });

  render();
})();
</script>

The coloring uses smooth iteration count to avoid banding:

$$\text{smooth}_i = i - \log_2(\log_2|z_n|)$$

Try these interesting values:

<div style="display: flex; flex-wrap: wrap; gap: 8px; margin: 15px 0;">
  <button onclick="setC(0, 1)" style="padding: 6px 12px; cursor: pointer; border: 1px solid #555; background: #222; color: #eee; border-radius: 4px;">Dendrite (c = i)</button>
  <button onclick="setC(-0.391, -0.587)" style="padding: 6px 12px; cursor: pointer; border: 1px solid #555; background: #222; color: #eee; border-radius: 4px;">Siegel disk</button>
  <button onclick="setC(-0.123, 0.745)" style="padding: 6px 12px; cursor: pointer; border: 1px solid #555; background: #222; color: #eee; border-radius: 4px;">Rabbit</button>
  <button onclick="setC(-0.75, 0)" style="padding: 6px 12px; cursor: pointer; border: 1px solid #555; background: #222; color: #eee; border-radius: 4px;">San Marco</button>
  <button onclick="setC(-0.8, 0.156)" style="padding: 6px 12px; cursor: pointer; border: 1px solid #555; background: #222; color: #eee; border-radius: 4px;">Spiral</button>
  <button onclick="setC(0.285, 0.01)" style="padding: 6px 12px; cursor: pointer; border: 1px solid #555; background: #222; color: #eee; border-radius: 4px;">Galaxies</button>
</div>

[Code](/code/julia_sets/)
