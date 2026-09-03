---
source_url: https://www.worldlabs.ai/blog/atlas
author: World Labs Team
date: 2026-09-01
---

# Atlas: A World Model for Spatial Intelligence

World Labs introduced **Atlas**, a next-generation omni world model pretrained natively on text, images, video, and 3D data. It is described as "a multimodal autoregressive diffusion transformer" where all inputs form a shared spatial context.

## Key Capabilities

**Camera-Controlled Generation**
Atlas accepts one or more reference images and generates new views at any specified camera position, producing up to 1 minute of video at 1440p. It uses precise camera geometry as a native input rather than text instructions.

**Spatial Context**
Like an LLM building a token context, Atlas grounds each image at a 3D position in space. This allows, for example, placing two unrelated images and having Atlas generate a coherent world between them — imagining doorways, hallways, and transitions.

**Spatial Reconstruction**
Atlas reconstructs real-world scenes from as few as one to several images, outputting novel views, point clouds, or 3D Gaussian splats. It reportedly "outperforms state-of-the-art results by models specially trained only for 3D reconstruction."

**Space-Time Simulation**
With footage from as few as three cell-phone cameras, Atlas can freeze time and reframe shots. It also supports Real-to-Sim robotics workflows, generating RGB and depth sensor data for simulated robot navigation and manipulation.

**Image Generation**
Atlas generates images and 360° panoramas from text or image prompts across diverse visual styles.

## Architecture

Four core properties work together:
- **Multimodal** — processes text, images, camera poses, and depth maps
- **Autoregressive** — generates outputs sequentially, conditioned on prior context
- **Diffusion** — uses rectified flow / denoising for high-quality continuous outputs
- **Transformer** — standard matrix-multiply backbone suited to modern hardware

## Benchmarks

- On camera-controlled generation, human raters preferred Atlas over competing video models, with preference rates ranging from 75% (vs. MiniMax H3) up to 94% (vs. Seedance 2.5).
- On 3D reconstruction (sparse-view pointmap error), Atlas scored a mean AbsRel of **25.3**, outperforming the next-best result of 28.7 across seven benchmark datasets.

## Scaling

The team reports that training a series of models at increasing compute levels consistently "unlocked new model capabilities," and expects this trend to continue.

Atlas is entering early access with select partners and will power future versions of Marble and other World Labs products.
