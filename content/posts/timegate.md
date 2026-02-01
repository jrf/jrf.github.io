---
title: "Replicating the Chrono Trigger Time Gate in GLSL"
date: 2025-05-30T09:29:00-06:00
categories: [chronotrigger, glsl]
math: true
---

<div style="display: flex; justify-content: space-around;">
    <img src="/videos/timegate.gif" alt="Chrono Trigger Time Gate Replica" style="width: 48%;" />
    <img src="/img/timegate.png" alt="Chrono Trigger Time Gate" style="width: 48%;" />
</div>

The time gates in Chrono Trigger have a distinctive swirling blue portal effect. This shader recreates that look using layered sine waves, procedural hash noise for texture, and a spiral distortion centered slightly off-axis. The color gradient shifts from deep blue at the edges through cyan to near-white at the peaks, with a soft vignette that fades the portal into darkness at the rim.

The effect pixelates the output to 6x6 blocks for a retro SNES feel.

[Code](/code/timegate/)
