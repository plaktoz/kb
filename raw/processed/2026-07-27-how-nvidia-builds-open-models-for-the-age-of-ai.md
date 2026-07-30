# How NVIDIA Builds Open Models for the Age of AI

source_url: https://blog.bytebytego.com/p/how-nvidia-builds-open-models-for

---

You probably know NVIDIA sells GPUs. But did you know it is also the largest publisher of open AI models in the world? Its models rank among the most downloaded on Hugging Face, and the lineup goes way beyond chatbots: reasoning models, world models, models for humanoid robots, self-driving cars, even drug discovery, quantum computing, and global forecasting.

This raises two questions. How does a company best known for hardware build so many strong models across so many domains? And why give them away for free, when those same models run on the GPUs NVIDIA sells?

To understand both, ByteByteGo spoke with Bryan Catanzaro, VP of Applied Deep Learning Research at NVIDIA. He walked through how his team builds the company's open models, the reasoning behind their architecture, and why NVIDIA open-sources so much of it.

## NVIDIA's Open Model Ecosystem

NVIDIA's open models sit at two ends of AI. At one end are models that work with symbols, the language, code, and reasoning that lives on a screen. At the other are models that work in the physical world, where robots and autonomous vehicles (AVs) have to perceive their surroundings and act. Most of the lineup falls somewhere along that line.

### 1. Reasoning models

Reasoning models are large language models that are trained to produce intermediate tokens before the final answer. This is what lets them think through tasks such as math and coding. Most frontier models you see these days are powered by a reasoning model — Claude Opus, GLM-5.2, Kimi K2.7.

NVIDIA's reasoning model family is called Nemotron. The first Nemotron model was introduced in 2023. In 2024, NVIDIA released the next generation with 340 billion parameters, followed by a faster hybrid design in 2025. The current generation, Nemotron 3, arrived across late 2025 and 2026 in three sizes: a small Nano model for fast, simple tasks, a mid-size Super model for harder planning and reasoning, and a large Ultra model for complex tasks that need the heaviest reasoning.

### 2. Physical AI

Language models are great at predicting the next token, but they do not understand the physical world. They cannot tell you how a shirt sleeve folds, or what a glass of water looks like the moment it tips over. A robot or a self-driving car needs that kind of understanding, but it cannot get it from text.

That is what a world model provides. Instead of predicting the next word, it understands the world and can predict the next state given the current state of the world and an action. It can generate realistic, physically plausible video, reason about motion and cause and effect, and produce the action data a robot needs to learn.

World models are extremely useful because you can use them to create training data for situations that are slow, expensive, or dangerous to capture in the real world.

NVIDIA's CEO, Jensen Huang, has called this "the ChatGPT moment for physical AI." NVIDIA's frontier open model for physical AI is Cosmos, launched at CES in January 2025 and unified in 2026 into a single omni-model, Cosmos 3, that can generate a scene, reason about it, and predict what comes next. Cosmos 3 also introduces world action models, which turn the pretrained video backbones directly into robot policies. There is also a 4-billion-parameter Edge version small enough to run on the robot and control it in real time.

#### From World Models to Robot Policies

A world model can predict the next scene, but a robot has to act. It has to turn what its cameras see into how its motors move, in real time, on tasks nobody scripted in advance.

That is the job of a robot foundation model, often called a vision-language-action model. The inputs to these models are usually camera images and instructions, and the model produces the movement.

NVIDIA's open foundation model line for humanoid robots is Isaac GR00T. NVIDIA unveiled the project in 2024, released the first open humanoid foundation model, GR00T N1, in early 2025, and has since iterated to GR00T 1.7.

GR00T models use Cosmos as a reasoning backbone, giving robots a shared foundation for perception, reasoning, and locomanipulation: the ability to move while manipulating objects. This enables more human-like decision-making and helps robots break complex actions into structured, step-by-step plans that developers can specialize for specific tasks. The 1.7 release also includes a production-friendly commercial license, allowing developers to deploy the model in real-world applications.

### 3. Healthcare, autonomous vehicles, quantum, and more specialized applications

The lineup keeps going. Alpamayo is an open model family for reasoning-based self-driving. Like GR00T, it uses Cosmos as its reasoning backbone, so the same physical-AI foundation that powers robots also lets a car work through road situations it was never trained on. It also exposes the chain of cause and effect behind each decision, which developers can inspect and build on. BioNeMo brings open models to biology and drug discovery, and the BioNeMo Agent Toolkit lets developers build autonomous agents for life sciences work. Ising gives quantum computer builders, operators, and developers the AI tools needed to scale devices to fault tolerance. Earth-2 is a family of open models, libraries, and frameworks that makes professional-grade weather and climate AI available to anyone. On top of these, NVIDIA offers open models for production use: safety models that filter unsafe content, speech models for voice, and vision models for images.

## How the Models Are Built to Be Frontier and Fast

It is often a challenge to build a model that is both fast and capable. Capable models are usually larger, which makes them slower to train and to answer questions. NVIDIA's answer is to chase the frontier and speed at the same time. Bryan put it this way: "the fastest model is the smartest model."

A faster model can be trained on more data in the same amount of time. It can be post-trained across more environments. Once deployed, it can think for longer on a hard problem at the same cost. So speed translates into capability and compounds at every stage.

### 1. The hybrid architecture

Most well-known models are built almost entirely on the Transformer's attention mechanism. Attention lets every token in the input look at every other token, which is powerful for capturing relationships but expensive. The cost grows with the square of the input length, so doubling the input roughly quadruples the work. The model has to keep every earlier token in memory as it runs. On very long inputs, that gets slow and costly.

The other main class is the state space model, and Mamba is its best-known example. Instead of comparing every token with every other one, a Mamba layer reads the sequence once and compresses everything it has seen into a fixed-size memory. That makes it cheap: the cost grows linearly with length, and the memory stays constant no matter how long the input. The tradeoff is that a fixed-size memory cannot keep every detail, so Mamba is weaker at recalling one exact fact buried far back.

Mamba layers are efficient while attention layers are more effective. Combining them gives the best of both worlds. A hybrid architecture swaps most of the attention layers in the Transformer with Mamba layers and keeps a few blocks with full attention.

NVIDIA's models rely on the same hybrid pattern. Most of the layers are Mamba, which keeps long inputs cheap to process and is what makes a million-token context window practical rather than just theoretical. A few attention layers are placed in between to restore the pinpoint recall that Mamba gives up, so the model can still retrieve exact details from anywhere in the context.

On top of the hybrid design, the models also use mixture-of-experts, or MoE, layers. An MoE layer consists of many small expert layers and routes each token to only a few of them. So instead of running every parameter on every token, the model activates only a small subset of its parameters. That allows a large total capacity at a low per-token cost, which keeps the model fast.

The way Bryan describes it, Mamba builds a global view of the whole sequence. Attention can always go back and find an exact fact. Put together, they are smarter than either one alone. NVIDIA published this hybrid result in 2024, and other labs, including the teams behind Qwen and Kimi, have since moved in the same direction.

### 2. Co-designing the GPU and the model

The second choice is where NVIDIA's two businesses meet. Its larger models are pretrained in a 4-bit number format called NVFP4, meaning most of the math during training uses just four bits per value. Fewer bits means less memory and less data to move, so the math runs faster and on less power.

Note that four bits is very little precision. Most teams train in higher precision and only shrink the model afterward, which loses accuracy. NVIDIA trained in 4 bits from the first step because it knew its next GPU generation, Blackwell, was being built with fast 4-bit hardware. The model and the chip were designed for each other.

The VP described the mindset behind it: Moore's law is no longer giving easy gains every generation, so progress has to come from designing the model and the hardware together. The team only attempted 4-bit pretraining because it believed the result was possible.

### 3. Post-training: learning from experience

With those efficiency choices in place, post-training is where the model gains its capability.

The post-training recipe itself is what most other teams converged to. It starts with supervised fine-tuning, where the model learns from curated examples of good answers and picks up the format and behavior expected of it. Then it switches to reinforcement learning, where the model practices on real tasks and is rewarded for reaching the right outcome. Instead of learning from examples, it learns from its own attempts.

Scaling up this reinforcement learning stage has been shown to improve a model's capability significantly. Here NVIDIA's efficiency focus pays off again. Because its models are cheaper to run, it can scale RL at a lower cost, letting the model practice across many environments in parallel and learn from over a million rollouts.

This is where the VP placed the real bottleneck for better models: not data or compute, but the diversity of these training environments. The more varied the situations a model practices in, the more capable it becomes, because that is where it gains real problem-solving experience.

## One Unified Foundation

Building strong models in one domain is hard. Building them across language, video, robotics, vehicles, and biology needs huge engineering and compute resources. NVIDIA's approach is to identify a reusable foundation, build it once, and reuse it across different efforts.

The VP traced this back to CUDA, the software layer that made NVIDIA's GPUs programmable. The "U" stands for Unified, and he called it the most important letter. The idea is to build one foundation and run everything on top of it, rather than maintaining many separate stacks.

The same instinct shapes the models. The hybrid architecture is not rebuilt for each model. The same backbone scales across all three Nemotron sizes. Whole components cross between efforts too. Cosmos Reason, the model built to reason about the physical world, was reused as the reasoning core inside NVIDIA's Isaac GR00T foundation model, so the robotics team did not have to build that part from scratch. The alternative, ten parallel efforts each reinventing the same pieces, would spread people and compute too thin. According to Bryan, NVIDIA tries to be as lazy as possible, because that is how it gets the most out of limited resources.

The other reason the team is so productive and iterates quickly is cultural. NVIDIA is mostly not top-down; it is a company of volunteers, where teams choose what to work on, and unification happens through invitation rather than control. The culture of collaboration is that if teams work with each other and get more done, they will get more resources than if they each go alone. When everyone shares that belief, a small group can produce a lot.

## Open is More Than Just Releasing Weights

You may have heard a lot about open models. Several AI labs released capable models. You can download the weights and use them. But that is not truly an open model. This is where NVIDIA's approach really separates it from the other labs. As Bryan puts it, Nemotron is not just a model. It is also the data, the tools, the training recipes, and the ideas published in the papers. The finished weights are just the last step.

In practice that means NVIDIA publishes the training datasets, the post-training datasets, the reinforcement learning environments, and the recipes needed to reproduce the work. A team can not only run the model, but also see how it was built and train their own version.

The same is true for robotics and self-driving cars, where developers can use open source simulation and learning frameworks, datasets to train and evaluate the model performance before deployment.

Releasing data at this scale is unusual. It is a scary thing for a company to do. NVIDIA does it anyway, and even shares clever building blocks like synthetic "persona" data that is statistically realistic but fully private, so a model can learn about the world without memorizing real people.

You can see this in what the community has done with it. NVIDIA's open data and models have spawned a large set of community fine-tunes and derivatives. One of its robotics datasets became one of the most-downloaded datasets on Hugging Face. Many variants of its Nemotron models have millions of downloads each, and the Nemotron family recently crossed 100M in total. You cannot build like that from the weights alone.

## Why a Chip Company Gives It All Away

You may think releasing open models sounds great. But why would a company that sells GPUs give away the AI that runs on them?

Bryan shared two reasons. The first is that NVIDIA needs to understand AI deeply to build the right hardware for it. To design future chips, you have to know where AI is going. The best way to really know is to build models yourself and put them in front of real users. A model kept private is easy to fool yourself about, so releasing it openly keeps the work honest and keeps NVIDIA's researchers connected to the wider community they learn from. With open models being such a hot topic, the real value is in enabling developers to post-train these models themselves at a fraction of the cost.

The second reason is about the business. NVIDIA grows whenever AI grows. Its goal is to support the ecosystem, not to compete with the companies building on top of it. Every team that adopts open models and builds its own AI can become a future customer for compute. So the company would rather hand the ecosystem the models and let the world's demand for AI pull its business forward.

There is also a side benefit: safety. Open technology tends to be safer because more people can inspect it and find problems, the way the open internet is hardened by everyone who uses it.

## What NVIDIA Has Learned Shipping Open Models

Shipping this many models in public teaches lessons that closed labs never face. Bryan shared several valuable lessons.

**1. The program matters more than any single release.** In a field moving this fast, every model is obsolete before it ships. So no single release is the point. What earns trust is a steady, sustained program. When the community believes a model line is here to stay, it pays attention to each new release instead of treating it as a one-off.

**2. Make it easy for developers.** A clean launch is the result of getting a hundred small things right, from licensing to documentation to ready-to-run examples. Listening to community feedback and smoothing that first-run experience is what turns a download into lasting use.

**3. Pick a license the community trusts.** NVIDIA moved away from its own homegrown licenses to OpenMDW, a community license from the Linux Foundation built specifically for open AI. Using a shared, purpose-built license removes friction and signals that the models are meant to be used freely.

## What's Next

The direction from here is to open even earlier. Rather than build a model privately and post it when it is done, NVIDIA wants to bring collaborators in sooner, since it plans to open everything anyway. The aim is to let partners shape the models while they are still being built. To make this happen, NVIDIA formed the Nemotron and Cosmos Coalitions.

What stands out most is the conviction that this is a long-term commitment, not a phase. The VP pointed to CUDA, which took more than a decade before the rest of the world understood why it mattered. NVIDIA stuck with it, and it became the foundation of the company.

He expects open models to follow the same path. As he put it, this is not a science project, and it is not charity. It is how NVIDIA moves itself forward into the future.
