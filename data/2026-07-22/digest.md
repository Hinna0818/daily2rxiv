# daily2rxiv Digest - 2026-07-22

共收录 65 篇论文。

## arxiv

### 1. [Hadamard 流形上的 1-Lipschitz 神经网络](https://arxiv.org/abs/2607.19335v1)
- Original title: 1-Lipschitz Neural Networks on Hadamard Manifolds
- Authors: Davide Murari, Marta Ghirardelli, Ben Adcock, Elena Celledoni, Brynjulf Owren et al.
- Meta: 2026-07-21 | math.NA
- 中文摘要: 控制神经网络的 Lipschitz 常数是提高鲁棒性和稳定性的标准方法。大多数现有的约束策略都是为欧几里得空间设计的。在这项工作中，我们构建并分析了 Hadamard 流形上的一类 1-Lipschitz 神经网络。我们的层是梯度下降类型、$1$-Lipschitz 和准$α$-严格非膨胀的。该架构的核心构建模块是 Busemann 函数，我们利用 Busemann 梯度流的特性来设计 $1$-Lipschitz 几何保留层。我们提供双曲流形和对称正定（SPD）矩阵流形的显式构造和示例。我们在两个数值实验中测试了所提出的架构：庞加莱盘上的鲁棒分类和掩模威沙特协方差重建。
- Abstract: Controlling the Lipschitz constant of a neural network is a standard way to promote robustness and stability. Most existing constraining strategies are designed for Euclidean spaces. In this work, we construct and analyze a class of 1-Lipschitz neural networks on Hadamard manifolds. Our layers are of gradient-descent type, $1$-Lipschitz, and quasi-$α$-firmly nonexpansive. The core building blocks of the proposed arc...
- Summary (fallback): 机器翻译摘要显示：控制神经网络的 Lipschitz 常数是提高鲁棒性和稳定性的标准方法。大多数现有的约束策略都是为欧几里得空间设计的。在这项工作中，我们构建并分析了 Hadamard 流形上的一类 1-Lipschitz 神经网络。我们的层是梯度下降类型、$1$-Lipschitz 和准$α$-严格非膨胀的。该架构的核心构建模块是 Busemann 函数，我们利用 Busemann 梯度流的特性来设计 $1$-Lipschitz 几何保留层。我们提供双曲流形和对称正定（SPD）矩阵流形的显式构造和示例。我们在两个数值实验中测试了所提出的架构：庞加莱盘上的鲁棒分类和掩模威沙特协方差重建。
- Keywords: lipschitz, neural, networks, manifolds, proposed

### 2. [简单二元决策的分布式多类分类的基本限制](https://arxiv.org/abs/2607.19334v1)
- Original title: Fundamental limits of distributed multiclass classification from simple binary decisions
- Authors: Ioannis Papageorgiou, Srinivas Nomula, Ayalvadi Ganesh, Sidharth Jaggi, Parimal Parag
- Meta: 2026-07-21 | stat.ML
- 中文摘要: 我们考虑从 $O(\log K)$ 简单二元分类器的组合构建 $K$ 类分类器的问题——这是以分布式方式构建复杂分类器的自然范例，每个代理执行相对简单的任务。我们研究了当相应的二元分类器是超平面时这种分类器的基本性能限制。对于程式化的高斯设置，其中 $K$ 类中心是 $\mathbb R^d$ 中的独立高斯点，并且观察结果被高斯噪声破坏，我们在多个解码和维度机制中得出了明确的性能界限。广泛的模拟实验为所提出的理论结果提供了强有力的实证验证。
- Abstract: We consider the problem of constructing a $K$-class classifier from the combination of $O(\log K)$ simple binary classifiers -- this is a natural paradigm to construct a sophisticated classifier in a distributed manner with each agent performing a relatively straightforward task. We study the fundamental performance limits of such a classifier when the corresponding binary classifiers are hyperplanes. For a stylized...
- Summary (fallback): 机器翻译摘要显示：我们考虑从 $O(\log K)$ 简单二元分类器的组合构建 $K$ 类分类器的问题——这是以分布式方式构建复杂分类器的自然范例，每个代理执行相对简单的任务。我们研究了当相应的二元分类器是超平面时这种分类器的基本性能限制。对于程式化的高斯设置，其中 $K$ 类中心是 $\mathbb R^d$ 中的独立高斯点，并且观察结果被高斯噪声破坏，我们在多个解码和维度机制中得出了明确的性能界限。广泛的模拟实验为所提出的理论结果提供了强有力的实证验证。
- Keywords: binary, classifier, gaussian, fundamental, limits

### 3. [通过 DDIM 针对线性逆问题可证明的基于扩散的后验采样](https://arxiv.org/abs/2607.19333v1)
- Original title: Provable diffusion-based posterior sampling for linear inverse problems via DDIM
- Authors: Yuchen Jiao, Na Li, Changxiao Cai, Yuxin Chen, Gen Li
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 基于扩散的方法在解决逆问题方面取得了显着的经验成功。然而，许多现有的后采样器要么缺乏严格的理论保证，要么会产生大量的计算开销。我们提出了一种简单而有效的算法，称为 \pddim，用于通过 DDIM 型采样器解决具有扩散先验的线性逆问题。我们的方法只需要对标准 DDIM 更新进行轻量级的、坐标式的修改，同时明确地合并测量模型。关键思想是沿着测量算子的每个奇异方向分别执行后验采样：对于每个方向，当观测信噪比（SNR）低于相应的扩散SNR时，采样器遵循学习的扩散先验，否则切换到基于校准的测量的预测器。
- Abstract: Diffusion-based methods have achieved remarkable empirical success in solving inverse problems. However, many existing posterior samplers either lack rigorous theoretical guarantees or incur substantial computational overhead. We propose a simple and efficient algorithm, called \pddim, for solving linear inverse problems with diffusion priors via a DDIM-type sampler. Our method requires only lightweight, coordinate-...
- Summary (fallback): 机器翻译摘要显示：基于扩散的方法在解决逆问题方面取得了显着的经验成功。然而，许多现有的后采样器要么缺乏严格的理论保证，要么会产生大量的计算开销。我们提出了一种简单而有效的算法，称为 \pddim，用于通过 DDIM 型采样器解决具有扩散先验的线性逆问题。我们的方法只需要对标准 DDIM 更新进行轻量级的、坐标式的修改，同时明确地合并测量模型。关键思想是沿着测量算子的每个奇异方向分别执行后验采样：对于每个方向，当观测信噪比（SNR）低于相应的扩散SNR时，采样器遵循学习的扩散先验，否则切换到基于校准的测量的预测器。
- Keywords: posterior, inverse, problems, sampler, diffusion-based

### 4. [ROMS-IMLE：竞争性单步生成建模的极简方法](https://arxiv.org/abs/2607.19332v1)
- Original title: ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling
- Authors: Chirag Vashist, Ke Li
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 生成模型经历了很多代的演变，从 VAE/GAN 到扩散/流匹配。一路走来，基础技术变得更加复杂，并且关于驱动强大经验表现的各种信念已经占据主导地位。由于扩散模型和流匹配的成功，更常见的信念之一是通过许多小的变换逐渐将噪声分布转换为数据分布的重要性。我们询问这是否真的有必要，并采取极简主义的方法来设计有竞争力的生成模型。我们从最基本的要素开始，即训练目标和模型。我们有目的地让两者变得简单。
- Abstract: Generative models have undergone many generations of evolution, from VAEs/GANs to diffusion/flow matching. Along the way, the underlying techniques have become more complicated and various beliefs about what drives strong empirical performance have taken hold. Due to the success of diffusion models and flow matching, one of the more common beliefs is the importance of transforming the noise distribution to the data...
- Summary (fallback): 机器翻译摘要显示：生成模型经历了很多代的演变，从 VAE/GAN 到扩散/流匹配。一路走来，基础技术变得更加复杂，并且关于驱动强大经验表现的各种信念已经占据主导地位。由于扩散模型和流匹配的成功，更常见的信念之一是通过许多小的变换逐渐将噪声分布转换为数据分布的重要性。我们询问这是否真的有必要，并采取极简主义的方法来设计有竞争力的生成模型。我们从最基本的要素开始，即训练目标和模型。我们有目的地让两者变得简单。
- Keywords: generative, model, training, minimalist, approach

### 5. [ISO：RLVR 原生优化堆栈](https://arxiv.org/abs/2607.19331v1)
- Original title: ISO: An RLVR-Native Optimization Stack
- Authors: Hanqing Zhu, Wenyan Cong, Zhizhou Sha, Sagnik Mukherjee, Xinyuan Song et al.
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 具有可验证奖励的强化学习（RLVR）正在迅速提高语言模型的推理能力，但将奖励反馈转换为权重空间更新的优化层仍然知之甚少。基于我们之前的分析（Zhu et al., 2025），我们通过模型权重的奇异结构来研究这个缺失层，并识别谱继承：RLVR 可以重用基础模型的权重谱，同时通过相关输入和输出奇异帧的变化来获取新的行为。我们将谱继承操作为等谱优化 (ISO)，这是一种 RLVR 原生的固定谱优化框架，具有互补的离线和在线实例化。
- Abstract: Reinforcement learning with verifiable rewards (RLVR) is rapidly advancing the reasoning capabilities of language models, yet the optimization layer that converts reward feedback into weight-space updates remains poorly understood. Building on our prior analysis (Zhu et al., 2025), we study this missing layer through the singular structure of model weights and identify spectral inheritance: RLVR can reuse the base m...
- Summary (fallback): 机器翻译摘要显示：具有可验证奖励的强化学习（RLVR）正在迅速提高语言模型的推理能力，但将奖励反馈转换为权重空间更新的优化层仍然知之甚少。基于我们之前的分析（Zhu et al., 2025），我们通过模型权重的奇异结构来研究这个缺失层，并识别谱继承：RLVR 可以重用基础模型的权重谱，同时通过相关输入和输出奇异帧的变化来获取新的行为。我们将谱继承操作为等谱优化 (ISO)，这是一种 RLVR 原生的固定谱优化框架，具有互补的离线和在线实例化。
- Keywords: optimization, training, steps, rlvr, layer

### 6. [ResearchArena：评估自动化人工智能研发中的破坏和监控](https://arxiv.org/abs/2607.19321v1)
- Original title: ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D
- Authors: Lena Libon, Ben Rank, Jehyeok Yeon, David Schmotz, Jeremy Qin et al.
- Meta: 2026-07-21 | cs.AI
- 中文摘要: 随着人工智能代理开始自动化人工智能研发，我们需要方法来评估其输出是否可以安全部署，即使代理本身可能不可信。人工智能控制提供了一种这样的方法：它不是信任代理，而是将其视为潜在的对手，并在部署之前使用监视器来检测秘密破坏。我们使用 ResearchArena 评估自动化 AI 研发的 AI 控制，该框架涵盖四个长期任务：训练后安全、训练后功能、CUDA 内核优化和推理服务器优化。由于人工智能研发中的可交付成果是一个将要部署和运行的工件，因此我们将每个主要任务与两种隐藏的副任务配对：一个是破坏提交的模型、适配器、内核或服务器本身的嵌入式副任务，以及一个独立的副任务，它在沙箱中采取隐蔽的超出范围的操作，同时保持工件诚实。
- Abstract: As AI agents begin to automate AI R&D, we need ways to assess whether their outputs are safe to deploy, even when the agents themselves may be untrusted. AI control offers one such approach: rather than trusting the agent, it treats it as a potential adversary and uses a monitor to detect covert sabotage before deployment. We evaluate AI control for automated AI R&D with ResearchArena, a framework spanning four long...
- Summary (fallback): 机器翻译摘要显示：随着人工智能代理开始自动化人工智能研发，我们需要方法来评估其输出是否可以安全部署，即使代理本身可能不可信。人工智能控制提供了一种这样的方法：它不是信任代理，而是将其视为潜在的对手，并在部署之前使用监视器来检测秘密破坏。我们使用 ResearchArena 评估自动化 AI 研发的 AI 控制，该框架涵盖四个长期任务：训练后安全、训练后功能、CUDA 内核优化和推理服务器优化。由于人工智能研发中的可交付成果是一个将要部署和运行的工件，因此我们将每个主要任务与两种隐藏的副任务配对：一个是破坏提交的模型、适配器、内核或服务器本身的嵌入式副任务，以及一个独立的副任务，它在沙箱中采取隐蔽的超出范围的操作，同时保持工件诚实。
- Keywords: sabotage, artifact, monitor, task, researcharena

### 7. [SoK：通过红队实现变分量子本征解算器的对抗鲁棒性](https://arxiv.org/abs/2607.19318v1)
- Original title: SoK: Adversarial Robustness of the Variational Quantum Eigensolver via Red-Teaming
- Authors: Ahmed Azaz Humdoon, Cheng Chu, Lei Jiang, Qian Lou, Mengxin Zheng
- Meta: 2026-07-21 | quant-ph
- 中文摘要: 变分量子本征求解器 (VQE) 是一种用于在近期量子硬件上估计分子基态能量的领先算法，其应用涵盖量子化学、材料科学和药物发现。随着 VQE 工作负载越来越多地通过基于云的“VQE 即服务”管道进行部署，它们会暴露给攻击者，例如受损的服务组件、恶意共同租户或转译堆栈中的内部人员，其中任何一个都可能在结果到达用户之前破坏结果。已经提出了一系列针对变分量子电路的攻击，但每种攻击都是单独研究的：一些针对具有基于精度的度量的量子分类器，另一些针对具有能量误差度量的变分量子算法。缺乏通用的评估设置使得它们的相对严重性难以比较，并且导致 VQE 的安全性难以表征。
- Abstract: The Variational Quantum Eigensolver (VQE) is a leading algorithm for estimating molecular ground-state energies on near-term quantum hardware, with applications spanning quantum chemistry, materials science, and drug discovery. As VQE workloads are increasingly deployed through cloud-based ``VQE-as-a-service'' pipelines, they become exposed to adversaries such as compromised service components, malicious co-tenants,...
- Summary (fallback): 机器翻译摘要显示：变分量子本征求解器 (VQE) 是一种用于在近期量子硬件上估计分子基态能量的领先算法，其应用涵盖量子化学、材料科学和药物发现。随着 VQE 工作负载越来越多地通过基于云的“VQE 即服务”管道进行部署，它们会暴露给攻击者，例如受损的服务组件、恶意共同租户或转译堆栈中的内部人员，其中任何一个都可能在结果到达用户之前破坏结果。已经提出了一系列针对变分量子电路的攻击，但每种攻击都是单独研究的：一些针对具有基于精度的度量的量子分类器，另一些针对具有能量误差度量的变分量子算法。缺乏通用的评估设置使得它们的相对严重性难以比较，并且导致 VQE 的安全性难以表征。
- Keywords: quantum, variational, attacks, backdoor, eigensolver

### 8. [CircuitKIT：用于机制解释的电路发现、评估和应用工具包](https://arxiv.org/abs/2607.19317v1)
- Original title: CircuitKIT : Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability
- Authors: Pratinav Seth, Hem Gosalia, Aditya Kasliwal, Vinay Kumar Sankarapu
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 电路分析不仅可以支持模型解释，还可以支持下游干预，例如修剪、编辑、引导和选择性微调。然而，目前进行此类分析需要将发现、评估和干预的单独实现拼接在一起，以及手动编写许多发现方法所需的对比提示。这种碎片化使得方法难以比较，并限制了它们在规范任务之外的应用。我们引入了 CircuitKIT，这是一个可获取源代码的库，它通过类型化、可序列化的表示形式连接电路分析工作流程。 CircuitKIT 提供了一套发现算法、用于将结构化数据映射到发现任务的声明式接口、补充电路诊断和下游应用模块。
- Abstract: Circuit analysis can support not only model explanation but also downstream interventions such as pruning, editing, steering, and selective fine-tuning. However, conducting such analyses currently requires stitching together separate implementations for discovery, evaluation, and intervention, as well as hand-authoring the contrastive prompts required by many discovery methods. This fragmentation makes methods diffi...
- Summary (fallback): 机器翻译摘要显示：电路分析不仅可以支持模型解释，还可以支持下游干预，例如修剪、编辑、引导和选择性微调。然而，目前进行此类分析需要将发现、评估和干预的单独实现拼接在一起，以及手动编写许多发现方法所需的对比提示。这种碎片化使得方法难以比较，并限制了它们在规范任务之外的应用。我们引入了 CircuitKIT，这是一个可获取源代码的库，它通过类型化、可序列化的表示形式连接电路分析工作流程。 CircuitKIT 提供了一套发现算法、用于将结构化数据映射到发现任务的声明式接口、补充电路诊断和下游应用模块。
- Keywords: discovery, circuitkit, circuit, application, evaluation

### 9. [偏心率约束的 CNN 训练揭示了视野周围的自适应信息编码](https://arxiv.org/abs/2607.19316v1)
- Original title: Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field
- Authors: Dylan M. Diaz, Margaret M. Henderson
- Meta: 2026-07-21 | q-bio.NC | DOI: 10.32470/0416gfsq
- 中文摘要: 在灵长类视觉系统中，中心偏好的皮质群体具有较高的空间分辨率并重叠面部和单词选择区域，而外围偏好的群体具有较低的空间分辨率和重叠的场景选择区域。这种“偏心偏差”可能反映了不同的任务相关性：中央视觉可以更好地支持面部识别和阅读等细粒度任务，而外围视觉可以更好地支持场景理解。为了测试依赖偏心率的编码是否可以从自然体验中产生，我们使用了来自视觉体验数据集（VEDB）的以自我为中心的视频和眼动追踪数据。我们使用对比学习 (SimCLR) 在经过修改的框架上训练 ResNet-18 模型，以隔离不同的偏心率（仅注视条件的中央凹作物、仅外围作物以及应用 NeuroFovea 变换的仅外围作物）。
- Abstract: In the primate visual system, center-preferring cortical populations have higher spatial resolution and overlap face- and word-selective regions while periphery-preferring populations have lower spatial resolution and overlap scene-selective regions. This "eccentricity bias" may reflect differential task-relevance: central vision may better support fine-grained tasks like face recognition and reading, while peripher...
- Summary (fallback): 机器翻译摘要显示：在灵长类视觉系统中，中心偏好的皮质群体具有较高的空间分辨率并重叠面部和单词选择区域，而外围偏好的群体具有较低的空间分辨率和重叠的场景选择区域。这种“偏心偏差”可能反映了不同的任务相关性：中央视觉可以更好地支持面部识别和阅读等细粒度任务，而外围视觉可以更好地支持场景理解。为了测试依赖偏心率的编码是否可以从自然体验中产生，我们使用了来自视觉体验数据集（VEDB）的以自我为中心的视频和眼动追踪数据。我们使用对比学习 (SimCLR) 在经过修改的框架上训练 ResNet-18 模型，以隔离不同的偏心率（仅注视条件的中央凹作物、仅外围作物以及应用 NeuroFovea 变换的仅外围作物）。
- Keywords: models, visual, periphery-only, regions, better

### 10. [Off-Context GRPO：学习使用特权信息推理难题](https://arxiv.org/abs/2607.19313v1)
- Original title: Off-Context GRPO: Learning to Reason on Hard Problems using Privileged Information
- Authors: Priyank Agrawal, Ankur Samanta, Shervin Ghasemlou, Jalaj Bhandari, Kavosh Asadi et al.
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 具有可验证奖励的强化学习 (RLVR) 改进了大型语言模型中的推理。然而，典型的 RLVR 方法无法解决难题：当模型无法生成任何正确的解决方案时，它会接收 \textit{zero} 学习信号。在训练期间提供特权指导（例如解决方案前缀）可以通过引导模型转向{具有非零奖励的正确解决方案}来帮助克服这种学习悬崖。
- Abstract: Reinforcement learning with verifiable rewards (RLVR) improves reasoning in large language models. Yet, typical RLVR approaches fail on difficult problems: when a model cannot generate any correct solutions, it receives \textit{zero} learning signal. Providing privileged guidance during training, such as solution prefixes, can help overcome this learning cliff by steering the model towards {correct solutions with no...
- Summary (fallback): 机器翻译摘要显示：具有可验证奖励的强化学习 (RLVR) 改进了大型语言模型中的推理。然而，典型的 RLVR 方法无法解决难题：当模型无法生成任何正确的解决方案时，它会接收 \textit{zero} 学习信号。在训练期间提供特权指导（例如解决方案前缀）可以通过引导模型转向{具有非零奖励的正确解决方案}来帮助克服这种学习悬崖。
- Keywords: grpo, learning, off-context, privileged, guidance

### 11. [从噪声轨迹数据中检测停留点 \[实验论文\]](https://arxiv.org/abs/2607.19312v1)
- Original title: Staypoint Detection from Noisy Trajectory Data \[Experiment Paper\]
- Authors: Lance Kennedy, Hossein Amiri, Yueyang Liu, Riyang Bao, Hanqi Chen et al.
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 从原始轨迹数据中检测停留点是众多空间计算应用的基础。此过程将地理位置的原始数字序列转换为语义上有意义的位置，例如家庭、工作场所或餐馆。尽管停留点检测对于语义轨迹分析很重要，但它缺乏标准基准，并且现有算法从未经过系统评估。这种差距仍然存在，因为没有公开可用的数据集提供原始的个人轨迹和地面真实停留点注释。
- Abstract: Detecting staypoints from raw trajectory data is fundamental to numerous spatial computing applications. This process transforms raw numeric sequences of geolocations into semantically meaningful locations, such as homes, workplaces, or restaurants. Despite its importance for semantic trajectory analysis, staypoint detection lacks standard benchmarks, and existing algorithms have never been systematically evaluated....
- Summary (fallback): 机器翻译摘要显示：从原始轨迹数据中检测停留点是众多空间计算应用的基础。此过程将地理位置的原始数字序列转换为语义上有意义的位置，例如家庭、工作场所或餐馆。尽管停留点检测对于语义轨迹分析很重要，但它缺乏标准基准，并且现有算法从未经过系统评估。这种差距仍然存在，因为没有公开可用的数据集提供原始的个人轨迹和地面真实停留点注释。
- Keywords: staypoint, detection, trajectory, existing, datasets

### 12. [黎曼深度学习：模块、网络和几何](https://arxiv.org/abs/2607.19305v1)
- Original title: Riemannian Deep Learning:Modules, Networks, and Geometries
- Authors: Chen Ziheng
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 基于流形值表示的深度神经网络引起了越来越多的兴趣，但许多基本组件仍然与特定流形相关，依赖于欧几里得近似，或者需要昂贵且数值脆弱的几何运算。本论文从三个互补的角度开发了黎曼深度学习的统一框架：可重用的神经模块、流形特定的网络架构和底层几何的设计。它将批量归一化从欧几里德空间和单个流形推广到广泛的李群和陀螺群，并将多项式逻辑回归从欧几里德空间扩展到 SPD 流形，然后扩展到一般黎曼流形。
- Abstract: Deep neural networks on manifold-valued representations have attracted growing interest, but many basic components remain tied to specific manifolds, rely on Euclidean approximations, or require costly and numerically fragile geometric operations. This thesis develops a unified framework for Riemannian deep learning from three complementary perspectives: reusable neural modules, manifold-specific network architectur...
- Summary (fallback): 机器翻译摘要显示：基于流形值表示的深度神经网络引起了越来越多的兴趣，但许多基本组件仍然与特定流形相关，依赖于欧几里得近似，或者需要昂贵且数值脆弱的几何运算。本论文从三个互补的角度开发了黎曼深度学习的统一框架：可重用的神经模块、流形特定的网络架构和底层几何的设计。它将批量归一化从欧几里德空间和单个流形推广到广泛的李群和陀螺群，并将多项式逻辑回归从欧几里德空间扩展到 SPD 流形，然后扩展到一般黎曼流形。
- Keywords: manifolds, riemannian, learning, geometries, deep

### 13. [浅层循环解码器网络的实时最优控制](https://arxiv.org/abs/2607.19302v1)
- Original title: Real-time optimal control with shallow recurrent decoder networks
- Authors: Matteo Tomasetto, Francesco Braghin, J. Nathan Kutz, Andrea Manzoni
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 跨多种场景实时控制动力系统对于实现自适应控制策略、确保稳定性和效率至关重要。然而，为了根据不同的场景定制控制动作，传统的最优控制问题通常需要多个系统模拟，由于底层时空动力学的高维性，这通常对计算要求很高。在这项工作中，我们利用基于浅循环解码器网络的降阶建模（SHRED-ROM）来合成用于高维和参数动态的实时闭环控制器，仅依赖于有限的状态传感器读数。在专家演示者给出的一些最佳示例上训练模型后，SHRED-ROM 在新场景中通过有效的分布式控制操作来模仿专家行为，从而减轻维数灾难。
- Abstract: Controlling dynamical systems in real-time across multiple scenarios is critical to enabling adaptive control strategies, ensuring stability and efficiency. However, to tailor control actions in response to varying scenarios, traditional optimal control problems typically require several system simulations, which are often computationally demanding due to the high-dimensionality of the underlying spatio-temporal dyn...
- Summary (fallback): 机器翻译摘要显示：跨多种场景实时控制动力系统对于实现自适应控制策略、确保稳定性和效率至关重要。然而，为了根据不同的场景定制控制动作，传统的最优控制问题通常需要多个系统模拟，由于底层时空动力学的高维性，这通常对计算要求很高。在这项工作中，我们利用基于浅循环解码器网络的降阶建模（SHRED-ROM）来合成用于高维和参数动态的实时闭环控制器，仅依赖于有限的状态传感器读数。在专家演示者给出的一些最佳示例上训练模型后，SHRED-ROM 在新场景中通过有效的分布式控制操作来模仿专家行为，从而减轻维数灾难。
- Keywords: control, optimal, real-time, scenarios, sensor

### 14. [用于预测燃气轮机燃烧室稀薄井喷的强化学习增强液体燃料反应堆网络模型](https://arxiv.org/abs/2607.19281v1)
- Original title: A Reinforcement-Learning-Augmented Liquid-Fueled Reactor Network Model for Predicting Lean Blowout in Gas Turbine Combustors
- Authors: Philip John, Eloghosa Ikponmwoba, Pinaki Pal, Opeoluwa Owoyele
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 本研究引入了强化学习 (RL) 框架，用于生成最佳液体燃料反应堆，以改善燃气轮机燃烧室的稀薄井喷 (LBO) 预测。确定簇边界的现有方法依赖于手动启发式或输入空间中基于距离的度量。相比之下，所提出的方法是面向目标的，明确地考虑了集群形成期间的目标指标（例如，LBO 预测精度）。该框架采用多阶段聚类-分类策略：初始聚类步骤（例如，$k$-表示聚类）生成一大组同质微聚类，然后由行动者批评家 RL 代理将它们合并到最佳反应器区域中。
- Abstract: This study introduces a reinforcement learning (RL) framework for generating optimal liquid-fueled reactors to improve lean blowout (LBO) predictions in gas turbine combustors. Existing approaches for determining cluster boundaries rely on manual heuristics or distance-based metrics in the input space. In contrast, the proposed method is goal-oriented, explicitly accounting for the target metric (e.g., LBO predictio...
- Summary (fallback): 机器翻译摘要显示：本研究引入了强化学习 (RL) 框架，用于生成最佳液体燃料反应堆，以改善燃气轮机燃烧室的稀薄井喷 (LBO) 预测。确定簇边界的现有方法依赖于手动启发式或输入空间中基于距离的度量。相比之下，所提出的方法是面向目标的，明确地考虑了集群形成期间的目标指标（例如，LBO 预测精度）。该框架采用多阶段聚类-分类策略：初始聚类步骤（例如，$k$-表示聚类）生成一大组同质微聚类，然后由行动者批评家 RL 代理将它们合并到最佳反应器区域中。
- Keywords: framework, liquid-fueled, reactor, model, lean

### 15. [基于外翻的机器人可以在脊柱蛛网膜下腔内安全进入、转向和内窥镜成像](https://arxiv.org/abs/2607.19274v1)
- Original title: Eversion-based robots can enable safe access,steering and endoscopic imaging within the spinal subarachnoid space
- Authors: Zicong Wu, Panagiotis Kalozoumis, S. M. Hadi Sadati, Aminul I. Ahmed, Jonathan Shapey et al.
- Meta: 2026-07-21 | cs.RO
- 中文摘要: 脊柱蛛网膜下腔内的安全导航受到其狭窄、柔顺且脆弱的解剖结构的限制。传统的导管和连续体机器人依赖于近端推动，沿组织装置界面产生摩擦和剪切，限制了远端的可控性并增加了神经损伤的风险。在这里，我们提出了一个直径 2 毫米的外翻生长机器人平台，该平台能够在人类脊柱蛛网膜下腔内实现摩擦力最小化的伸展和转向，并通过计算模型、模型实验和完整的人类尸体研究进行验证。该机器人集成了一个微型内窥镜，用于实时鞘内可视化，并通过压力驱动尖端外翻来前进，将运动定位到远端，同时最大限度地减少部署主体的平移滑动。
- Abstract: Safe navigation within the spinal subarachnoid space is constrained by its narrow, compliant, and delicate anatomy. Conventional catheters and continuum robots rely on proximal pushing, generating friction and shear along the tissue device interface that limit distal controllability and increase the risk of neural injury. Here, we present a 2 mm diameter eversion-growing robotic platform that enables friction minimi...
- Summary (fallback): 机器翻译摘要显示：脊柱蛛网膜下腔内的安全导航受到其狭窄、柔顺且脆弱的解剖结构的限制。传统的导管和连续体机器人依赖于近端推动，沿组织装置界面产生摩擦和剪切，限制了远端的可控性并增加了神经损伤的风险。在这里，我们提出了一个直径 2 毫米的外翻生长机器人平台，该平台能够在人类脊柱蛛网膜下腔内实现摩擦力最小化的伸展和转向，并通过计算模型、模型实验和完整的人类尸体研究进行验证。该机器人集成了一个微型内窥镜，用于实时鞘内可视化，并通过压力驱动尖端外翻来前进，将运动定位到远端，同时最大限度地减少部署主体的平移滑动。
- Keywords: spinal, human, within, subarachnoid, space

### 16. [基于 GNN 的模型中空间可转移性的引导式网络无关特征初始化](https://arxiv.org/abs/2607.19270v1)
- Original title: GUIDED Network-Agnostic Feature Initialization for Spatial Transferability in GNN-based Models
- Authors: Alessandro Scalese, Santhanakrishnan Narayanan, Constantinos Antoniou
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 交通分配问题是交通规划中一个基本但计算成本较高的组成部分。虽然图神经网络已经成为快速、数据驱动的替代品，但它们的实际部署受到空间泛化差距的严重限制。标准模型依赖于转换特征初始化，将出行需求与固定网络拓扑联系起来，从而阻止无缝转移到新的城市环境。为了克服这种结构限制，本研究提出了一种与网络无关的初始化层，称为几何无约束归纳需求嵌入（GUIDED）。通过将出行需求作为辅助虚拟链路上的标量属性而不是特定的节点特征注入，该模块化框架标准化了输入空间，无论网络规模如何。
- Abstract: The Traffic Assignment Problem is a fundamental but computationally expensive component of transportation planning. While Graph Neural Networks have emerged as fast, data-driven surrogates, their practical deployment is severely constrained by a spatial generalization gap. Standard models rely on transductive feature initializations that tie travel demand to fixed network topologies, preventing seamless transfer to...
- Summary (fallback): 机器翻译摘要显示：交通分配问题是交通规划中一个基本但计算成本较高的组成部分。虽然图神经网络已经成为快速、数据驱动的替代品，但它们的实际部署受到空间泛化差距的严重限制。标准模型依赖于转换特征初始化，将出行需求与固定网络拓扑联系起来，从而阻止无缝转移到新的城市环境。为了克服这种结构限制，本研究提出了一种与网络无关的初始化层，称为几何无约束归纳需求嵌入（GUIDED）。通过将出行需求作为辅助虚拟链路上的标量属性而不是特定的节点特征注入，该模块化框架标准化了输入空间，无论网络规模如何。
- Keywords: initialization, spatial, demand, network, guided

### 17. [肺动脉、小动脉、毛细血管、小静脉和静脉的多尺度血流动力学模型](https://arxiv.org/abs/2607.19269v1)
- Original title: Multiscale hemodynamics model for the pulmonary arteries, arterioles, capillaries, venules and veins
- Authors: Michelle A Bartolo, Mansoor A Haider, Nicholas A Hill, Mette S Olufsen
- Meta: 2026-07-21 | q-bio.TO
- 中文摘要: 这项研究提出了第一个包含完整肺循环的脉动血流动力学数学模型，明确地将大动脉、小动脉、毛细血管、小静脉和大静脉联系起来。为了克服先前模型排除显式毛细血管动力学的局限性，我们将肺动脉和静脉的一维结构化树模型与动态毛细血管片模型结合起来。这种方法建立了一种递归方法，用于将毛细血管片耦合到结构化树，以梯状结构连接小动脉和小静脉。为了评估纳入这种毛细血管结构的影响，我们比较了健康对照受试者和肺动脉高压（PH）患者的模拟血流动力学。
- Abstract: This study presents the first mathematical model of pulsatile hemodynamics that encompasses the complete pulmonary circulation, explicitly linking the large arteries, arterioles, capillaries, venules, and large veins. To overcome the limitations of previous models that exclude explicit capillary dynamics, we incorporate a one-dimensional structured-tree model of the pulmonary arteries and veins with a dynamic capill...
- Summary (fallback): 机器翻译摘要显示：这项研究提出了第一个包含完整肺循环的脉动血流动力学数学模型，明确地将大动脉、小动脉、毛细血管、小静脉和大静脉联系起来。为了克服先前模型排除显式毛细血管动力学的局限性，我们将肺动脉和静脉的一维结构化树模型与动态毛细血管片模型结合起来。这种方法建立了一种递归方法，用于将毛细血管片耦合到结构化树，以梯状结构连接小动脉和小静脉。为了评估纳入这种毛细血管结构的影响，我们比较了健康对照受试者和肺动脉高压（PH）患者的模拟血流动力学。
- Keywords: capillary, model, pulmonary, capillaries, hemodynamics

### 18. [他们会验证。他们就是不采取行动。权限框架和洗钱代码如何将可信代理 CI/CD 管道变成攻击面](https://arxiv.org/abs/2607.19267v1)
- Original title: They'll Verify. They Just Won't Act. How Authority Framing and Laundered Code Turn a Trusted Agentic CI/CD Pipeline Into an Attack Surface
- Authors: Yohann Sidot
- Meta: 2026-07-21 | cs.CR
- 中文摘要: 我们研究了一个五代理 CI/CD 管道（分类 -> 开发人员 -> 安全扫描 -> 审查 -> 批准/部署），该管道由三个提供商的五个不同的生产 LLM 构建，位于影子模式下的 LLM 防火墙后面。单个不受信任的输入（请求“使用遥测”功能的外部问题）要求提供将进程秘密 (dict(os.environ)) 泄露到攻击者 URL 的代码，并被洗白为可观察性。
- Abstract: We study a five-agent CI/CD pipeline (triage -> developer -> security-scan -> review -> approve/deploy), built from five distinct production LLMs across three providers, behind an LLM firewall in shadow mode. A single untrusted input - an external issue requesting a "usage-telemetry" feature - asks for code that exfiltrates process secrets (dict(os.environ)) to an attacker URL, laundered as observability. Across a p...
- Summary (fallback): 机器翻译摘要显示：我们研究了一个五代理 CI/CD 管道（分类 -> 开发人员 -> 安全扫描 -> 审查 -> 批准/部署），该管道由三个提供商的五个不同的生产 LLM 构建，位于影子模式下的 LLM 防火墙后面。单个不受信任的输入（请求“使用遥测”功能的外部问题）要求提供将进程秘密 (dict(os.environ)) 泄露到攻击者 URL 的代码，并被洗白为可观察性。
- Keywords: laundered, code, they, pipeline, across

### 19. [实现可审计的欺诈检测：结合图形特征、模型解释和代理案例调查](https://arxiv.org/abs/2607.19266v1)
- Original title: Toward Auditable Fraud Detection: Combining Graph Features, Model Explanations, and Agentic Case Investigation
- Authors: Rahil Sharma
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 欺诈检测系统必须随着交易量的增加而扩展，同时保持可解释和可审查。我们研究了 PaySim 数据集上的分层管道，该管道结合了梯度增强分类器、图派生结构特征、基于自动编码器的异常信号、TreeSHAP 解释以及应用于分类器评分不确定情况的有界 LLM 调查代理。在进行任何模型比较之前，我们会识别并删除模拟器特定的平衡快捷方式，否则会夸大基线性能。进行此校正后，图形特征和异常信号都不会提高整个测试集的平均精度。然而，两者都在获得中间基线分数的案例子集中对欺诈进行了更好的排名。
- Abstract: Fraud detection systems must scale with rising transaction volume while remaining explainable and reviewable. We study a layered pipeline on the PaySim dataset that combines a gradient-boosted classifier, graph-derived structural features, an autoencoder-based anomaly signal, TreeSHAP explanations, and a bounded LLM investigation agent applied to cases the classifier scores uncertainly. Before any model comparison,...
- Summary (fallback): 机器翻译摘要显示：欺诈检测系统必须随着交易量的增加而扩展，同时保持可解释和可审查。我们研究了 PaySim 数据集上的分层管道，该管道结合了梯度增强分类器、图派生结构特征、基于自动编码器的异常信号、TreeSHAP 解释以及应用于分类器评分不确定情况的有界 LLM 调查代理。在进行任何模型比较之前，我们会识别并删除模拟器特定的平衡快捷方式，否则会夸大基线性能。进行此校正后，图形特征和异常信号都不会提高整个测试集的平均精度。然而，两者都在获得中间基线分数的案例子集中对欺诈进行了更好的排名。
- Keywords: fraud, agent, features, investigation, classifier

### 20. [BioSecBench-Surveillance：病原体基因组监测中 AI 代理的可验证基准](https://arxiv.org/abs/2607.19262v1)
- Original title: BioSecBench-Surveillance: A Verifiable Benchmark for AI Agents in Pathogen Genomic Surveillance
- Authors: Harmon Bhasin, Kevin Flyangolts, Dianzhuo Wang, Evan Seeyave, Arjun Banerjee et al.
- Meta: 2026-07-21 | cs.AI
- 中文摘要: 随着病原体基因组监测规模的扩大，瓶颈正在从数据生成转向分析。我们推出了 BioSecBench-Surveillance，这是一个包含 100 项评估的可验证基准，测试 AI 代理是否可以从原始测序数据和监控上下文中推断出正确的分析流程。每次评估仅向代理提供人类分析师将拥有的数据和上下文，然后确定性地对其结构化答案进行评分。这些任务涵盖七个类别，从分类学分类到基因工程检测，涉及不同的样本类型和测序技术。在 16 个模型背带对的 3,962 次可分级尝试中，最强的配置仅通过了大约一半。
- Abstract: As pathogen genomic surveillance scales, the bottleneck is shifting from data generation to analysis. We present BioSecBench-Surveillance, a verifiable benchmark of 100 evaluations testing whether AI agents can infer the right analysis pipeline from raw sequencing data and surveillance context. Each evaluation gives an agent only the data and context a human analyst would have, then grades its structured answer dete...
- Summary (fallback): 机器翻译摘要显示：随着病原体基因组监测规模的扩大，瓶颈正在从数据生成转向分析。我们推出了 BioSecBench-Surveillance，这是一个包含 100 项评估的可验证基准，测试 AI 代理是否可以从原始测序数据和监控上下文中推断出正确的分析流程。每次评估仅向代理提供人类分析师将拥有的数据和上下文，然后确定性地对其结构化答案进行评分。这些任务涵盖七个类别，从分类学分类到基因工程检测，涉及不同的样本类型和测序技术。在 16 个模型背带对的 3,962 次可分级尝试中，最强的配置仅通过了大约一半。
- Keywords: percent, agents, surveillance, confidence, interval

### 21. [财务报表欺诈检测的基准概括：稳健的评估和新颖的任务](https://arxiv.org/abs/2607.19259v1)
- Original title: Benchmarking Generalization in Financial Statement Fraud Detection: robust evaluation and novel tasks
- Authors: Guy Stephane Waffo Dzuyo, Gaël Guibon, Christophe Cerisara, Luis Belmar-Letelier
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 财务报表欺诈检测 (FSFD) 对于市场诚信至关重要，但面临着日益复杂的方案和财务报告中未充分利用的文本数据的挑战。现有的方法通常依赖于随机数据分割，导致过于乐观的绩效估计，无法反映对新公司或未来时期的现实世界的概括。为了用最先进的技术解决这个反复出现的问题，我们提出了一个强大的 FSFD 框架，利用大型语言模型 (LLM) 来集成财务报告中的结构化财务数据和非结构化文本信息。我们通过称为公司隔离 FSFD (CI-FSFD) 的新颖且具有挑战性的基准任务提供更现实的评估。我们构建并公开了一个综合的美国公司数据集，其中结合了财务报表、MD&A 文本摘要和欺诈标签。
- Abstract: Financial statement fraud detection (FSFD) is crucial for market integrity but faces challenges from increasingly sophisticated schemes and under-utilized textual data in financial reports. Existing methods often rely on random data splits, leading to overoptimistic performance estimates that do not reflect real-world generalization to new companies or future periods. To address this recurring problem with the state...
- Summary (fallback): 机器翻译摘要显示：财务报表欺诈检测 (FSFD) 对于市场诚信至关重要，但面临着日益复杂的方案和财务报告中未充分利用的文本数据的挑战。现有的方法通常依赖于随机数据分割，导致过于乐观的绩效估计，无法反映对新公司或未来时期的现实世界的概括。为了用最先进的技术解决这个反复出现的问题，我们提出了一个强大的 FSFD 框架，利用大型语言模型 (LLM) 来集成财务报告中的结构化财务数据和非结构化文本信息。我们通过称为公司隔离 FSFD (CI-FSFD) 的新颖且具有挑战性的基准任务提供更现实的评估。我们构建并公开了一个综合的美国公司数据集，其中结合了财务报表、MD&A 文本摘要和欺诈标签。
- Keywords: financial, fraud, detection, robust, evaluation

### 22. [用于超临界燃烧中真实流体热力学性质神经预测的热力学信息输入重新参数化](https://arxiv.org/abs/2607.19241v1)
- Original title: Thermodynamics-Informed Input Reparameterization for Neural Prediction of Real-Fluid Thermodynamic Properties in Supercritical Combustion
- Authors: Haoze Zhang, Han Li, Ke Xiao, Yangchen Xu, Runze Mao et al.
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 真实流体热力学性质评估是超临界燃烧模拟中的主要计算成本。在基于焓的压力修正公式中，闭包通过焓-温度反演和重复的真实流体状态方程评估，从求解器状态 (h,p,Y) 评估温度 T、密度 $ρ$ 和压缩系数 $ψ$。神经网络代理提供固定成本推理，但从 (h,p,Y) 到 $(T,ρ,ψ)$ 的直接映射必须捕获焓-温度关系和非理想状态方程响应，从而导致复杂的回归问题。这项工作引入了一种基于热力学的输入重新参数化策略，称为目标对齐输入重新参数化（TAIR）。
- Abstract: Real-fluid thermodynamic property evaluation is a major computational cost in supercritical combustion simulations. In the enthalpy-based pressure-correction formulation, the closure evaluates temperature T, density $ρ$, and compressibility coefficient $ψ$ from the solver state (h,p,Y) through enthalpy-temperature inversion and repeated real-fluid equation-of-state evaluations. Neural-network surrogates offer fixed-...
- Summary (fallback): 机器翻译摘要显示：真实流体热力学性质评估是超临界燃烧模拟中的主要计算成本。在基于焓的压力修正公式中，闭包通过焓-温度反演和重复的真实流体状态方程评估，从求解器状态 (h,p,Y) 评估温度 T、密度 $ρ$ 和压缩系数 $ψ$。神经网络代理提供固定成本推理，但从 (h,p,Y) 到 $(T,ρ,ψ)$ 的直接映射必须捕获焓-温度关系和非理想状态方程响应，从而导致复杂的回归问题。这项工作引入了一种基于热力学的输入重新参数化策略，称为目标对齐输入重新参数化（TAIR）。
- Keywords: input, real-fluid, thermodynamic, reparameterization, supercritical

### 23. [DBMol：通过结构预测模型设计高亲和力、目标特异性小分子](https://arxiv.org/abs/2607.19237v1)
- Original title: DBMol: Design of High-Affinity, Target-Specific Small Molecules through Structure Prediction Models
- Authors: Yiming Qin, Kai Yi, Miruna Cretu, Sjors H. W. Scheres, Pietro Liò et al.
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 设计与特定蛋白质口袋高亲和力结合的小分子配体是药物发现的基本目标，因为小分子构成了已批准治疗的主要部分。结构预测方面的最新突破（例如 AlphaFold-3 和 Boltz-2）能够实现准确的生物分子相互作用预测，并有望成为下游任务（包括结合亲和力预测）的基础模型。我们建议利用这些模型并引入 DBMol，这是一种用于从头小分子设计的新结构预测引导框架。 DBMol 制定了交替的优化和投影过程。在优化阶段，DBMol 从初始分子开始，使用基于梯度的优化来改善口袋特异性相互作用，并使用结构预测模型预测结合亲和力。
- Abstract: Designing small molecule ligands that bind with high affinity to specific protein pockets is a fundamental goal in drug discovery, as small molecules constitute a major fraction of approved therapeutics. Recent breakthroughs in structure prediction, such as AlphaFold-3 and Boltz-2, enable accurate biomolecular interaction prediction and show promise as foundation models for downstream tasks, including binding affini...
- Summary (fallback): 机器翻译摘要显示：设计与特定蛋白质口袋高亲和力结合的小分子配体是药物发现的基本目标，因为小分子构成了已批准治疗的主要部分。结构预测方面的最新突破（例如 AlphaFold-3 和 Boltz-2）能够实现准确的生物分子相互作用预测，并有望成为下游任务（包括结合亲和力预测）的基础模型。我们建议利用这些模型并引入 DBMol，这是一种用于从头小分子设计的新结构预测引导框架。 DBMol 制定了交替的优化和投影过程。在优化阶段，DBMol 从初始分子开始，使用基于梯度的优化来改善口袋特异性相互作用，并使用结构预测模型预测结合亲和力。
- Keywords: dbmol, prediction, molecules, structure, affinity

### 24. [具有随机卷积特征的上下文时间序列分类](https://arxiv.org/abs/2607.19234v1)
- Original title: In-Context Time Series Classification with Random Convolutional Features
- Authors: Joscha Cüppers, Jilles Vreeken
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 时间序列分类是医疗信号分析、工业监控和基于传感器的活动识别等领域的核心，其中类别信息表现为局部形状、特定频率、时间变化或复杂的跨通道交互。随机卷积变换有效地将这些序列映射到固定维度的表格特征，但传统上与简单的线性分类器配对。我们研究预训练的表格基础模型是否可以更有效地利用这些丰富的表示。我们提出了 MASHT，这是一种将 MultiRocket 和 Hydra 功能与上下文表格基础模型的强大功能相结合的管道。通过利用预训练的表格基础模型，我们的方法完全绕过特定于任务的模型训练，只需要特征提取和直接推理。
- Abstract: Time series classification is central to domains like medical signal analysis, industrial monitoring, and sensor-based activity recognition, where class information manifests as localized shapes, specific frequencies, temporal shifts, or complex cross-channel interactions. Random convolutional transforms efficiently map these sequences to fixed-dimensional tabular features but are traditionally paired with simple li...
- Summary (fallback): 机器翻译摘要显示：时间序列分类是医疗信号分析、工业监控和基于传感器的活动识别等领域的核心，其中类别信息表现为局部形状、特定频率、时间变化或复杂的跨通道交互。随机卷积变换有效地将这些序列映射到固定维度的表格特征，但传统上与简单的线性分类器配对。我们研究预训练的表格基础模型是否可以更有效地利用这些丰富的表示。我们提出了 MASHT，这是一种将 MultiRocket 和 Hydra 功能与上下文表格基础模型的强大功能相结合的管道。通过利用预训练的表格基础模型，我们的方法完全绕过特定于任务的模型训练，只需要特征提取和直接推理。
- Keywords: tabular, time, series, classification, features

### 25. [S3：分层强化学习中通过约束粗动态的不确定性实现稳定的子目标选择](https://arxiv.org/abs/2607.19232v1)
- Original title: S3: Stable Subgoal Selection by Constraining Uncertainty of Coarse Dynamics in Hierarchical Reinforcement Learning
- Authors: Kshitij Kumar Srivastava, Kshitij Jerath
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 分层强化学习（HRL）旨在将战略规划与原始执行分开。它在解决长期和复杂的任务方面取得了广泛的成功，而平面强化学习算法在这些任务上存在学习困难。然而，虽然HRL中的低层智能体受益于密集的反馈和丰富的尝试机会，但高层智能体从环境中接收到稀疏的、延迟的反馈，其性能取决于低层的执行能力。在本文中，我们研究了是否可以通过为高级智能体提供动态感知的内在动机来更有策略地执行子目标选择。
- Abstract: Hierarchical Reinforcement Learning (HRL) intends to separate strategic planning from primitive execution. It has been widely successful in solving long-horizon and complex tasks, where flat-RL algorithms have difficulty in learning. However, while the low-level agent in HRL benefits from dense feedback and abundant trial opportunities, the high-level agent receives sparse, delayed feedback from the environment and...
- Summary (fallback): 机器翻译摘要显示：分层强化学习（HRL）旨在将战略规划与原始执行分开。它在解决长期和复杂的任务方面取得了广泛的成功，而平面强化学习算法在这些任务上存在学习困难。然而，虽然HRL中的低层智能体受益于密集的反馈和丰富的尝试机会，但高层智能体从环境中接收到稀疏的、延迟的反馈，其性能取决于低层的执行能力。在本文中，我们研究了是否可以通过为高级智能体提供动态感知的内在动机来更有策略地执行子目标选择。
- Keywords: dynamics, learning, agent, high-level, subgoal

### 26. [推理的代价：神经机器翻译强化学习的成本与质量权衡](https://arxiv.org/abs/2607.19226v1)
- Original title: The Price of Reasoning: Cost-Quality Tradeoffs in Reinforcement Learning for Neural Machine Translation
- Authors: Michael Jungo, Aixiu An
- Meta: 2026-07-21 | cs.CL | DOI: 10.1145/3820755.3833407
- 中文摘要: 具有可验证奖励的强化学习 (RLVR) 已被确立为大型语言模型 (LLM) 后期训练的可行范例，包括神经机器翻译 (NMT) 等下游任务。最新研究表明，由于 RLVR 具有诱导推理能力，RLVR 可能成为翻译法律文档的首选训练方法，但这引发了一个问题：它是否真的归因于推理，或更普遍地归因于训练范式。我们研究了在训练和推理过程中将模型的推理轨迹包含在生成的响应中的重要性，方法是系统地从其中一个阶段中省略它。我们的实验表明，包括推理，特别是在推理过程中，对整体翻译质量具有积极影响。
- Abstract: Reinforcement learning with verifiable rewards (RLVR) has been established as a viable paradigm for the post-training of Large Language Models (LLMs), including downstream tasks, such as Neural Machine Translation (NMT). With the latest research indicating that RLVR could be the preferred training method for translating legal documents due to the induced reasoning capabilities, it raises the question whether it is r...
- Summary (fallback): 机器翻译摘要显示：具有可验证奖励的强化学习 (RLVR) 已被确立为大型语言模型 (LLM) 后期训练的可行范例，包括神经机器翻译 (NMT) 等下游任务。最新研究表明，由于 RLVR 具有诱导推理能力，RLVR 可能成为翻译法律文档的首选训练方法，但这引发了一个问题：它是否真的归因于推理，或更普遍地归因于训练范式。我们研究了在训练和推理过程中将模型的推理轨迹包含在生成的响应中的重要性，方法是系统地从其中一个阶段中省略它。我们的实验表明，包括推理，特别是在推理过程中，对整体翻译质量具有积极影响。
- Keywords: reasoning, translation, including, training, cost-quality

### 27. [AdaFlash：通过策略蒸馏扩散起草器进行自适应推测解码](https://arxiv.org/abs/2607.19223v1)
- Original title: AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters
- Authors: Yu-Yang Qian, Hao-Cong Wu, Chen Chen, Jiacheng Sun, Zhenhua Dong et al.
- Meta: 2026-07-21 | cs.LG
- 中文摘要: 推测解码（其中轻量级草稿模型首先生成草稿序列，然后由目标模型并行验证）已成为加速大型语言模型推理的流行范例。 DFlash 等最近的工作通过利用扩散起草器进一步提高了起草效率，其并行降噪机制可以在单次前向传递中生成草稿。在这项工作中，我们发现了扩散起草者的一个中心陷阱：双向注意力是一把双刃剑。一方面赋予模型并行生成和全局上下文建模能力；另一方面，这种固有的全局依赖性在域级别和令牌级别上引入了高方差：不同域之间的接受率波动很大，并且草稿令牌质量在不同令牌位置上也存在差异。
- Abstract: Speculative decoding, in which a lightweight draft model first generates a draft sequence that is then verified in parallel by the target model, has become a prevalent paradigm for accelerating large language model inference. Recent work such as DFlash further boosts drafting efficiency by leveraging diffusion drafters, whose parallel denoising mechanism enables draft generation in a single forward pass. In this wor...
- Summary (fallback): 机器翻译摘要显示：推测解码（其中轻量级草稿模型首先生成草稿序列，然后由目标模型并行验证）已成为加速大型语言模型推理的流行范例。 DFlash 等最近的工作通过利用扩散起草器进一步提高了起草效率，其并行降噪机制可以在单次前向传递中生成草稿。在这项工作中，我们发现了扩散起草者的一个中心陷阱：双向注意力是一把双刃剑。一方面赋予模型并行生成和全局上下文建模能力；另一方面，这种固有的全局依赖性在域级别和令牌级别上引入了高方差：不同域之间的接受率波动很大，并且草稿令牌质量在不同令牌位置上也存在差异。
- Keywords: model, diffusion, drafters, draft, adaflash

### 28. [计算机教育中团队解决问题练习的评估](https://arxiv.org/abs/2607.19209v1)
- Original title: Assessment in Team Problem-Solving Exercises in Computing Education
- Authors: Valdemar Švábenský, Jan Vykopal, Sukrit Leelaluk, Pavel Čeleda, Fumiya Okubo et al.
- Meta: 2026-07-21 | cs.CY
- 中文摘要: 这篇从研究到实践的完整论文介绍了评估学生团队桌面练习（TTX）的方法。 TTX 使学习者团队能够为工作场所任务做好准备并练习危机响应，例如解决网络安全事件。虽然评估对于确定团队实现学习目标的程度至关重要，但 TTX 的复杂性和开放性往往会导致反馈延迟或不完整。 TTX学习平台可以记录团队的行动和沟通；然而，利用这些数据来评估绩效的探索尚未充分。为了解决这一差距，我们使用来自两个国家 81 名参与者的原始数据集比较了两种 TTX 后团队评估方法——聚类和大型语言模型 (LLM)。我们根据标准化评分标准根据教师分配的分数评估了这些方法。
- Abstract: This full paper in the research-to-practice track presents methods for assessing student teams in tabletop exercises (TTXs). TTXs enable learner teams to prepare for workplace tasks and practice crisis responses, such as resolving cybersecurity incidents. While assessment is essential for determining how well teams achieve learning objectives, the complex, open-ended nature of TTXs often leads to delayed or incomple...
- Summary (fallback): 机器翻译摘要显示：这篇从研究到实践的完整论文介绍了评估学生团队桌面练习（TTX）的方法。 TTX 使学习者团队能够为工作场所任务做好准备并练习危机响应，例如解决网络安全事件。虽然评估对于确定团队实现学习目标的程度至关重要，但 TTX 的复杂性和开放性往往会导致反馈延迟或不完整。 TTX学习平台可以记录团队的行动和沟通；然而，利用这些数据来评估绩效的探索尚未充分。为了解决这一差距，我们使用来自两个国家 81 名参与者的原始数据集比较了两种 TTX 后团队评估方法——聚类和大型语言模型 (LLM)。我们根据标准化评分标准根据教师分配的分数评估了这些方法。
- Keywords: teams, methods, assessment, ttxs, learning

### 29. [关于贝叶斯预测推理的一些警示故事](https://arxiv.org/abs/2607.19206v1)
- Original title: Some cautionary tales about Bayesian predictive inference
- Authors: Emanuela Dreassi, Fabrizio Leisen, Luca Pratelli, Pietro Rigo
- Meta: 2026-07-21 | math.ST
- 中文摘要: 讨论了贝叶斯预测推理中经常出现的两个误解。第一个涉及数据生成机制，而第二个则高估了渐近可交换性所发挥的作用。通过例子强调了这种误解的一些后果。
- Abstract: Two misunderstandings, frequently arising in Bayesian predictive inference, are discussed. The first deals with the data generating mechanism, while the second consists in overestimating the role played by asymptotic exchangeability. Some consequences of such misunderstandings are highlighted through examples.
- Summary (fallback): 机器翻译摘要显示：讨论了贝叶斯预测推理中经常出现的两个误解。第一个涉及数据生成机制，而第二个则高估了渐近可交换性所发挥的作用。通过例子强调了这种误解的一些后果。
- Keywords: some, bayesian, predictive, inference, misunderstandings

### 30. [进化熵决定了格陵兰鲨的寿命](https://arxiv.org/abs/2607.19203v1)
- Original title: Evolutionary Entropy Shapes Lifespan of the Greenland Shar
- Authors: Jorge Buescu, Saber N. Elaidy, Henrique M. Oliveira
- Meta: 2026-07-21 | q-bio.PE
- 中文摘要: 格陵兰鲨 (\emph{Somniosus microcephalus}) 是已知最长寿的脊椎动物之一，雌性成熟期估计约为 156 岁，最大年龄接近四个世纪。我们应用年龄结构人群的进化熵理论来研究哪些生殖窗口与这种极端的人口特征相兼容。利用开放群体种群的同质性和临界阈值定理，我们得出了世代时间、生殖分位数和熵最大化生殖终点的人口统计情景。临界阈值出现在 $q_c\approx0.9763$ 处，处于接近统一的持久性状态。寿命校准场景跨越了有限极大值和渐近熵状态的边界。
- Abstract: The Greenland shark (\emph{Somniosus microcephalus}) is among the longest-lived vertebrates known, with female maturity estimated at approximately 156 years and maximum ages approaching four centuries. We apply the theory of evolutionary entropy for age-structured populations to investigate which reproductive windows are compatible with such an extreme demographic profile. Using the homogeneity and critical-threshol...
- Summary (fallback): 机器翻译摘要显示：格陵兰鲨 (\emph{Somniosus microcephalus}) 是已知最长寿的脊椎动物之一，雌性成熟期估计约为 156 岁，最大年龄接近四个世纪。我们应用年龄结构人群的进化熵理论来研究哪些生殖窗口与这种极端的人口特征相兼容。利用开放群体种群的同质性和临界阈值定理，我们得出了世代时间、生殖分位数和熵最大化生殖终点的人口统计情景。临界阈值出现在 $q_c\approx0.9763$ 处，处于接近统一的持久性状态。寿命校准场景跨越了有限极大值和渐近熵状态的边界。
- Keywords: reproductive, entropy, evolutionary, greenland, centuries

## biorxiv

### 1. [人类肠道微生物组中表达的孤儿基因、虚假孤儿基因和保守基因的鉴定和分类](https://www.biorxiv.org/content/10.64898/2026.01.16.699869v2)
- Original title: Identification and Classification of Expressed Orphan Genes, Spurious Orphan Genes, and Conserved Genes in the Human Gut Microbiome
- Authors: Chen, C., Vakirlis, N., Holmer, R., de Ridder, D., Kupczok, A.
- Meta: 2026-07-22 | genomics | DOI: 10.64898/2026.01.16.699869
- 中文摘要: 孤儿基因——物种外缺乏可检测同源物的基因——广泛存在于微生物基因组中，被认为有助于微生物的适应和分子创新。然而，并非所有预测的孤儿基因都可以代表新的功能编码序列。假阳性孤儿基因，也称为虚假孤儿基因，可能是由基因预测错误引起的。我们推断缺乏可检测表达的孤儿基因更有可能是假的。为了测试这一点，我们将人类肠道微生物组的大规模宏转录组分析与机器学习相结合，以区分表达的孤儿基因和虚假基因，并将它们与多个物种中发现的保守基因进行比较。
- Abstract: Orphan genes - genes lacking detectable homologs outside a species - are widespread in microbial genomes and are thought to contribute to their adaptation and molecular innovation. However, not all predicted orphan genes may represent novel functional coding sequences. False positive orphan genes, also called spurious orphan genes, can arise from gene prediction errors. We reason that orphan genes lacking detectable...
- Summary (fallback): 机器翻译摘要显示：孤儿基因——物种外缺乏可检测同源物的基因——广泛存在于微生物基因组中，被认为有助于微生物的适应和分子创新。然而，并非所有预测的孤儿基因都可以代表新的功能编码序列。假阳性孤儿基因，也称为虚假孤儿基因，可能是由基因预测错误引起的。我们推断缺乏可检测表达的孤儿基因更有可能是假的。为了测试这一点，我们将人类肠道微生物组的大规模宏转录组分析与机器学习相结合，以区分表达的孤儿基因和虚假基因，并将它们与多个物种中发现的保守基因进行比较。
- Keywords: genes, orphan, spurious, expressed, conserved

### 2. [拟南芥基因组内容快速分化的遗传控制](https://www.biorxiv.org/content/10.1101/2025.06.11.659220v3)
- Original title: The genetic control of rapid genome content divergence in Arabidopsis thaliana
- Authors: Fiscus, C. J., Koenig, D.
- Meta: 2026-07-22 | genomics | DOI: 10.1101/2025.06.11.659220
- 中文摘要: 真核生物的基因组进化主要由重复序列的动态驱动，这些重复序列在拷贝数和序列组成方面差异很大。重复进化的速率在物种之间和物种内部有所不同，并且可能受到遗传和环境的调节。为了揭示影响基因组内容进化速率的因素，我们使用基于 K-mer 的新型方法分析了 1,142 个重新测序的拟南芥基因组，以表征基因组内容变异并识别重复丰度差异背后的高变区。接下来，我们将重复丰度视为数量性状，并对 400 多个重复家族进行全基因组关联分析，以确定拷贝数变异的遗传基础。
- Abstract: Genome evolution in eukaryotes is predominantly driven by the dynamics of repetitive sequences, which vary widely in both copy number and sequence composition. Rates of repeat evolution differ between and within species and are likely modulated by both genetics and environment. To uncover factors shaping the rate of genome content evolution, we analyzed 1,142 resequenced Arabidopsis thaliana genomes using a novel K-...
- Summary (fallback): 机器翻译摘要显示：真核生物的基因组进化主要由重复序列的动态驱动，这些重复序列在拷贝数和序列组成方面差异很大。重复进化的速率在物种之间和物种内部有所不同，并且可能受到遗传和环境的调节。为了揭示影响基因组内容进化速率的因素，我们使用基于 K-mer 的新型方法分析了 1,142 个重新测序的拟南芥基因组，以表征基因组内容变异并识别重复丰度差异背后的高变区。接下来，我们将重复丰度视为数量性状，并对 400 多个重复家族进行全基因组关联分析，以确定拷贝数变异的遗传基础。
- Keywords: genome, repeat, content, evolution, genetic

### 3. [人类线粒体接触位点和嵴组织系统 (MICOS) 子组件的综合结构测定](https://www.biorxiv.org/content/10.64898/2026.07.19.739404v1)
- Original title: Integrative structure determination of a human mitochondrial contact site and cristae organizing system (MICOS) sub-assembly
- Authors: Jindal, M., Mahato, R., Das, S., Guha, A., Majila, K. et al.
- Meta: 2026-07-22 | bioinformatics | DOI: 10.64898/2026.07.19.739404
- 中文摘要: 线粒体接触位点和嵴组织系统 (MICOS) 复合体是存在于嵴连接处的线粒体内膜 (IMM) 组件。它负责调节嵴的形成和重塑。然而，其结构尚不清楚。我们应用贝叶斯综合结构测定来表征包含 Mic60、Mic19、Mic10 和 Mic13 的 MICOS 复合物的结构，将 AlphaFold 预测与来自交联质谱、生化测定、电子断层扫描、同源建模和序列比对的数据相结合。该整合结构揭示了 Mic10N,C、Mic60LBS1,LBS2、mitofilin 和 Mic13central,C 之间新颖的相互界面，并经过实验验证。一些可能致病的错义突变也定位于这些新的界面，突出了它们的重要性。
- Abstract: The Mitochondrial contact site and Cristae Organizing System (MICOS) complex is an inner mitochondrial membrane (IMM) assembly present at the cristae junction. It is responsible for regulating cristae formation and remodeling. However, its structure is not known. We applied Bayesian integrative structure determination to characterize the structure of the Mic60, Mic19, Mic10, and Mic13-containing MICOS complex combin...
- Summary (fallback): 机器翻译摘要显示：线粒体接触位点和嵴组织系统 (MICOS) 复合体是存在于嵴连接处的线粒体内膜 (IMM) 组件。它负责调节嵴的形成和重塑。然而，其结构尚不清楚。我们应用贝叶斯综合结构测定来表征包含 Mic60、Mic19、Mic10 和 Mic13 的 MICOS 复合物的结构，将 AlphaFold 预测与来自交联质谱、生化测定、电子断层扫描、同源建模和序列比对的数据相结合。该整合结构揭示了 Mic10N,C、Mic60LBS1,LBS2、mitofilin 和 Mic13central,C 之间新颖的相互界面，并经过实验验证。一些可能致病的错义突变也定位于这些新的界面，突出了它们的重要性。
- Keywords: structure, micos, integrative, cristae, mitochondrial

### 4. [基于深度学习的分割的超分辨率成像，用于详细描述庞贝病骨骼肌线粒体排列的特征](https://www.biorxiv.org/content/10.64898/2026.07.21.739567v1)
- Original title: Super-resolution imaging with deep learning-based segmentation for detailed characterization of mitochondrial arrangement in Pompe disease skeletal muscle
- Authors: HASSANI, I., Deniaud, J., Thorin, C., Fiore, T., Dubreil, L. et al.
- Meta: 2026-07-22 | pathology | DOI: 10.64898/2026.07.21.739567
- 中文摘要: 庞贝氏病（II 型糖原贮积病）是一种常染色体隐性遗传性溶酶体贮积病，其特征是溶酶体内进行性糖原积累。它导致它们的增大、自噬体的积聚和自噬流的缺陷。在病理生理学特征中，线粒体异常长期以来被认为是溶酶体功能障碍的继发后果。通常，它们在电子显微镜下被描述，揭示了晶体内含物、嵴丢失、线粒体肿胀和充满糖原的结构。然而，骨骼肌中线粒体和溶酶体之间的空间组织和相互作用仍然知之甚少，这些改变相对于肌肉代谢特征的进展也是如此。
- Abstract: Pompe disease (glycogen storage disease type II) is an autosomal recessive lysosomal storage disorder characterized by progressive glycogen accumulation within lysosomes. It leads to their enlargement, autophagosome build-up and defective autophagic flux. Among the pathophysiological features, mitochondrial abnormalities have long been regarded as secondary consequences of lysosomal dysfunction. Typically, they have...
- Summary (fallback): 机器翻译摘要显示：庞贝氏病（II 型糖原贮积病）是一种常染色体隐性遗传性溶酶体贮积病，其特征是溶酶体内进行性糖原积累。它导致它们的增大、自噬体的积聚和自噬流的缺陷。在病理生理学特征中，线粒体异常长期以来被认为是溶酶体功能障碍的继发后果。通常，它们在电子显微镜下被描述，揭示了晶体内含物、嵴丢失、线粒体肿胀和充满糖原的结构。然而，骨骼肌中线粒体和溶酶体之间的空间组织和相互作用仍然知之甚少，这些改变相对于肌肉代谢特征的进展也是如此。
- Keywords: disease, muscle, mitochondrial, lysosomal, pompe

### 5. [癫痫相关基因的表达模式作为 PTE 和 SE 模型中常见的病理特征以及通过计算机方法进行可能的治疗](https://www.biorxiv.org/content/10.64898/2026.04.23.720518v2)
- Original title: Expression Pattern of Epilepsy Associated Genes as a Common Pathological Signature in PTE and SE models and possible therapeutics via an in-silico approach
- Authors: Tyagi, J., Kumari, S., Prakash, C., Saran, S., Biswal, B. et al.
- Meta: 2026-07-22 | neuroscience | DOI: 10.64898/2026.04.23.720518
- 中文摘要: 从最初的脑损伤到慢性癫痫的转变仍然是临床神经科学的一个关键挑战，通常涉及难以通过单基因分析捕获的复杂分子变化。本研究调查了两种不同病因模型中基因组不稳定性收敛途径的存在：铁诱导的 (FeCl3) 创伤后癫痫 (PTE) 和锂-毛果芸香碱诱导的 (LiCl-Pilo) 癫痫持续状态 (SE)。通过将电生理学 (EEG)、γ-振荡频谱分析、多单位活动 (MUA) 记录与行为评估莫里斯水迷宫 (MWM) 和旷场测试 (OFT) 相结合，我们验证并建立了这两种模型的慢性过度兴奋性和相关的认知情绪共病。
- Abstract: The transition from an initial brain insult to chronic epilepsy remains a critical challenge in clinical neuroscience, often involving complex molecular shifts that are difficult to capture through single-gene analysis. This study investigated the existence of a convergent pathway of genomic instability across two distinct etiological models: iron-induced (FeCl3) post-traumatic epilepsy (PTE) and lithium-pilocarpine...
- Summary (fallback): 机器翻译摘要显示：从最初的脑损伤到慢性癫痫的转变仍然是临床神经科学的一个关键挑战，通常涉及难以通过单基因分析捕获的复杂分子变化。本研究调查了两种不同病因模型中基因组不稳定性收敛途径的存在：铁诱导的 (FeCl3) 创伤后癫痫 (PTE) 和锂-毛果芸香碱诱导的 (LiCl-Pilo) 癫痫持续状态 (SE)。通过将电生理学 (EEG)、γ-振荡频谱分析、多单位活动 (MUA) 记录与行为评估莫里斯水迷宫 (MWM) 和旷场测试 (OFT) 相结合，我们验证并建立了这两种模型的慢性过度兴奋性和相关的认知情绪共病。
- Keywords: genes, models, epilepsy, analysis, associated

### 6. [土壤食物网中的顶级捕食者提高了碳循环效率](https://www.biorxiv.org/content/10.64898/2026.07.20.739503v1)
- Original title: Top predators in soil food webs increase carbon cycling efficiency
- Authors: Lejoly, J. D. M., van Hoof, E., Wang, Y., Favre, V., Quist, C. et al.
- Meta: 2026-07-22 | ecology | DOI: 10.64898/2026.07.20.739503
- 中文摘要: 土壤微生物被认为是凋落物分解和土壤碳形成的核心。微生物的活动和丰度由食微生物动物控制，而微生物本身又被顶级捕食者捕食。然而，很少有人研究顶级捕食者在碳循环中的作用，特别是在以食菌动物为主的食物网中。在这里，我们测试了由微生物、食微生物动物（以食菌动物为主的线虫群落）和顶级捕食者（以线虫为食的螨虫）组成的营养级联如何影响碳循环以及相关的微生物库和过程。我们发现，我们的模型顶级捕食者降低了食真菌线虫的丰度，并对微生物组的组成产生级联效应，特别是增加了革兰氏阳性细菌的生物量，从而促进了细菌能量通道。
- Abstract: Soil microbes are considered central in litter decomposition and soil carbon formation. Microbial activity and abundance are controlled by microbivores, which are themselves preyed upon by top predators. However, the role of top predators in carbon cycling is rarely studied, especially in bacterivore-dominated food webs. Here we tested how trophic cascades, consisting of microbes, microbivores (bacterivore-dominated...
- Summary (fallback): 机器翻译摘要显示：土壤微生物被认为是凋落物分解和土壤碳形成的核心。微生物的活动和丰度由食微生物动物控制，而微生物本身又被顶级捕食者捕食。然而，很少有人研究顶级捕食者在碳循环中的作用，特别是在以食菌动物为主的食物网中。在这里，我们测试了由微生物、食微生物动物（以食菌动物为主的线虫群落）和顶级捕食者（以线虫为食的螨虫）组成的营养级联如何影响碳循环以及相关的微生物库和过程。我们发现，我们的模型顶级捕食者降低了食真菌线虫的丰度，并对微生物组的组成产生级联效应，特别是增加了革兰氏阳性细菌的生物量，从而促进了细菌能量通道。
- Keywords: carbon, cycling, predators, soil, trophic

### 7. [IGFBP5/IGF1、THPO 和 P38 MAPK 信号传导的靶向调节是可推广用于线粒体呼吸链疾病和骨肉瘤的有效治疗策略](https://www.biorxiv.org/content/10.64898/2026.07.20.739625v1)
- Original title: Targeted modulation of IGFBP5/IGF1, THPO, and P38 MAPK signaling are potent therapeutic strategies generalizable for mitochondrial respiratory chain disease and osteosarcoma
- Authors: Keith, K., Peng, M., Remes, C., Miranda, V., Wachowski, N. et al.
- Meta: 2026-07-22 | genetics | DOI: 10.64898/2026.07.20.739625
- 中文摘要: 原发性线粒体疾病 (PMD) 的疾病缓解疗法有限，目前仅适用于 400 多种离散基因疾病中的 3 种。环己酰亚胺 (CHX) 是一种全球胞质翻译抑制剂，我们之前报道过它可以挽救 PMD 临床前模型，尽管其毒性阻碍了临床开发。为了确定 CHX 对 PMD 治疗有益的特定介质，在半乳糖中生长的复合物 I 缺陷和遗传性疾病成纤维细胞系模型中进行了基于 SOMAscan 的蛋白质组学研究。与健康对照细胞相比，在 PMD 细胞中经 CHX 处理后发现，血小板生成素 (THPO) 和胰岛素样生长因子结合蛋白 5 (IGFBP5) 是仅有的两种差异调节蛋白，以及 ERK/MAPK 通路失调。
- Abstract: Primary mitochondrial diseases (PMD) have limited disease-modifying therapies currently applicable to only 3 of over 400 discrete gene disorders. Cycloheximide (CHX) is a global cytosolic translation inhibitor we previously reported to rescue PMD preclinical models, although its toxicity precluded clinical development. To identify specific mediators underlying CHX treatment benefit in PMD, SOMAscan-based proteomics...
- Summary (fallback): 机器翻译摘要显示：原发性线粒体疾病 (PMD) 的疾病缓解疗法有限，目前仅适用于 400 多种离散基因疾病中的 3 种。环己酰亚胺 (CHX) 是一种全球胞质翻译抑制剂，我们之前报道过它可以挽救 PMD 临床前模型，尽管其毒性阻碍了临床开发。为了确定 CHX 对 PMD 治疗有益的特定介质，在半乳糖中生长的复合物 I 缺陷和遗传性疾病成纤维细胞系模型中进行了基于 SOMAscan 的蛋白质组学研究。与健康对照细胞相比，在 PMD 细胞中经 CHX 处理后发现，血小板生成素 (THPO) 和胰岛素样生长因子结合蛋白 5 (IGFBP5) 是仅有的两种差异调节蛋白，以及 ERK/MAPK 通路失调。
- Keywords: thpo, inhibition, igf1, mapk, therapeutic

### 8. [HPRC2：几乎完全覆盖常见遗传变异的人类全基因组参考](https://www.biorxiv.org/content/10.64898/2026.07.21.739710v1)
- Original title: HPRC2: A human pangenome reference with near-complete coverage of common genetic variation
- Authors: Lucas, J. K., Hebbar, P., Liao, W.-W., Macias-Velasco, J. F., Novak, A. M. et al.
- Meta: 2026-07-22 | genomics | DOI: 10.64898/2026.07.21.739710
- 中文摘要: 全基因组参考通过整合群体中存在的变异，克服了任何个体参考基因组的固有局限性。我们推出了人类泛基因组参考联盟 (HPRC) 第 2 版 (HPRC2)，这是一种公开可用的第二阶段泛基因组，其基因组数量比 HPRC 第 1 版 (HPRC1) 的基因组数量增加了约五倍，并且在基因组完整性、连续性和准确性方面有了可测量的改进。 HPRC2 使用优先考虑常见变异覆盖率的原则性算法来选择样本，提供了 460 个单倍型，这些单倍型总共捕获了 All of Us Research Program v8 队列中观察到的超过 99% 的常见变异。
- Abstract: A pangenome reference overcomes the inherent limitation of any individual reference genome by integrating the variation present in a population. We present the Human Pangenome Reference Consortium's (HPRC) Release 2 (HPRC2), an openly available, second phase pangenome that is an approximately fivefold expansion in genome number over HPRC Release 1 (HPRC1) and measurable improvement in genome completeness, contiguity...
- Summary (fallback): 机器翻译摘要显示：全基因组参考通过整合群体中存在的变异，克服了任何个体参考基因组的固有局限性。我们推出了人类泛基因组参考联盟 (HPRC) 第 2 版 (HPRC2)，这是一种公开可用的第二阶段泛基因组，其基因组数量比 HPRC 第 1 版 (HPRC1) 的基因组数量增加了约五倍，并且在基因组完整性、连续性和准确性方面有了可测量的改进。 HPRC2 使用优先考虑常见变异覆盖率的原则性算法来选择样本，提供了 460 个单倍型，这些单倍型总共捕获了 All of Us Research Program v8 队列中观察到的超过 99% 的常见变异。
- Keywords: pangenome, reference, genome, variation, hprc2

### 9. [细菌土臭素生物合成被划分在双组分蛋白质壳内](https://www.biorxiv.org/content/10.64898/2026.07.21.739788v1)
- Original title: Bacterial Geosmin Biosynthesis is Compartmentalized Inside a Two-Component Protein Shell
- Authors: Fazal, A., Dutcher, C. A., Andreas, M. P., Giessen, T. W.
- Meta: 2026-07-22 | biochemistry | DOI: 10.64898/2026.07.21.739788
- 中文摘要: 萜类化合物是在生命的三个领域中普遍存在的、结构多样的天然产物。最常见和最深入研究的萜类化合物之一是挥发性的岩质化合物土臭素，它产生土壤的泥土气味，而人类可以接受的浓度低至万亿分之几。对细菌土臭素合酶 (GeoA) 编码基因簇的生物信息分析表明，许多基因簇与编码家族 2B 封装蛋白壳蛋白的基因共定位。在这里，我们重点研究了模型粘杆菌 Myxococcus xanthus 的封装蛋白编码土臭素基因簇，并表明这两种壳蛋白形成了双组分家族 2B 封装蛋白，其中 GeoA 作为内化货物。
- Abstract: Terpenoids are ubiquitous, structurally diverse natural products found across the three domains of life. One of the most commonly observed and well-studied terpenoids is the volatile, petrichoric compound geosmin, responsible for the earthy smell of soil to which humans are receptive down to a few parts per trillion. Bioinformatic analysis of bacterial geosmin synthase (GeoA)-encoding gene clusters reveals that many...
- Summary (fallback): 机器翻译摘要显示：萜类化合物是在生命的三个领域中普遍存在的、结构多样的天然产物。最常见和最深入研究的萜类化合物之一是挥发性的岩质化合物土臭素，它产生土壤的泥土气味，而人类可以接受的浓度低至万亿分之几。对细菌土臭素合酶 (GeoA) 编码基因簇的生物信息分析表明，许多基因簇与编码家族 2B 封装蛋白壳蛋白的基因共定位。在这里，我们重点研究了模型粘杆菌 Myxococcus xanthus 的封装蛋白编码土臭素基因簇，并表明这两种壳蛋白形成了双组分家族 2B 封装蛋白，其中 GeoA 作为内化货物。
- Keywords: cargo, geosmin, shell, geoa, family

### 10. [AI 驱动的纳米结合剂设计，针对 TSLPR 异二聚体接口，抑制 2 型炎症信号传导](https://www.biorxiv.org/content/10.64898/2026.07.20.739581v1)
- Original title: AI-Driven Design of Nanobinders Targeting the TSLPR Heterodimer Interface to Suppress Type 2 Inflammatory Signaling
- Authors: Ahn, W.-C., Son, M.-J., Kim, J.-R., Go, S.-R., Kang, J.-E. et al.
- Meta: 2026-07-22 | biochemistry | DOI: 10.64898/2026.07.20.739581
- 中文摘要: 胸腺基质淋巴细胞生成素 (TSLP) 信号传导异常是 2 型炎症性疾病的核心驱动因素，但唯一获批的 TSLP 靶向疗法是 150 kDa 单克隆抗体，其体积庞大，限制组织渗透并妨碍吸入递送。在这里，我们报告了一种人工智能驱动的框架，用于设计超紧凑的从头纳米结合剂，通过空间破坏 TSLPR-IL-7R 异二聚体的组装来抑制 TSLP 信号传导。我们比较了两种结构引导策略，即纯粹从头生成螺旋束和将天然结合基序模拟界面移植到设计的支架上。尽管两者都产生纳摩尔结合物，但只有天然细胞因子几何形状的正位模拟才能阻断受体异二聚化，这表明功能拮抗作用是由精确的表位几何形状而不是单独的亲和力控制的。
- Abstract: Aberrant thymic stromal lymphopoietin (TSLP) signaling is a central driver of type 2 inflammatory diseases, yet the only approved TSLP-targeted therapy is a 150 kDa monoclonal antibody whose bulky format limits tissue penetration and precludes inhaled delivery. Here, we report an AI-driven framework for designing ultra-compact de novo nanobinders that suppress TSLP signaling by sterically disrupting assembly of the...
- Summary (fallback): 机器翻译摘要显示：胸腺基质淋巴细胞生成素 (TSLP) 信号传导异常是 2 型炎症性疾病的核心驱动因素，但唯一获批的 TSLP 靶向疗法是 150 kDa 单克隆抗体，其体积庞大，限制组织渗透并妨碍吸入递送。在这里，我们报告了一种人工智能驱动的框架，用于设计超紧凑的从头纳米结合剂，通过空间破坏 TSLPR-IL-7R 异二聚体的组装来抑制 TSLP 信号传导。我们比较了两种结构引导策略，即纯粹从头生成螺旋束和将天然结合基序模拟界面移植到设计的支架上。尽管两者都产生纳摩尔结合物，但只有天然细胞因子几何形状的正位模拟才能阻断受体异二聚化，这表明功能拮抗作用是由精确的表位几何形状而不是单独的亲和力控制的。
- Keywords: type, signaling, ai-driven, nanobinders, heterodimer

### 11. [用于同时进行短读长和长读病毒基因组监测的有源矩阵数字微流控平台](https://www.biorxiv.org/content/10.64898/2026.07.21.739725v1)
- Original title: An active-matrix digital microfluidic platform for simultaneous short- and long-read viral genomic surveillance
- Authors: BINGBING, Z., FANG, Z., LIU, Q., JI, J., HU, S. et al.
- Meta: 2026-07-22 | bioengineering | DOI: 10.64898/2026.07.21.739725
- 中文摘要: 病毒病原体的爆发频率和地理分布不断扩大，使得加强基因组监测成为全球公共卫生的迫切需求。结合二代测序（NGS）和三代测序（TGS）的并行文库制备可以显着提高基因组监测的覆盖范围和分辨率，是加强监测的关键策略。在这里，我们开发了一个完整的样本到结果系统，将可编程有源矩阵数字微流控 (AM-DMF) 芯片与生物信息学分析管道集成在一起。与公共卫生实验室使用的传统手动方案相比，我们的系统减少了72%的试剂消耗，缩短了45%的文库制备时间，并将批间变异系数（CV）降低了20%。
- Abstract: The outbreak frequency and geographic distribution of viral pathogens are continuously expanding, making enhanced genomic surveillance an urgent global public health need. Parallel library preparation combining next-generation sequencing (NGS) and third-generation sequencing (TGS) can substantially improve the coverage and resolution of genomic surveillance, representing a key strategy for strengthening surveillance...
- Summary (fallback): 机器翻译摘要显示：病毒病原体的爆发频率和地理分布不断扩大，使得加强基因组监测成为全球公共卫生的迫切需求。结合二代测序（NGS）和三代测序（TGS）的并行文库制备可以显着提高基因组监测的覆盖范围和分辨率，是加强监测的关键策略。在这里，我们开发了一个完整的样本到结果系统，将可编程有源矩阵数字微流控 (AM-DMF) 芯片与生物信息学分析管道集成在一起。与公共卫生实验室使用的传统手动方案相比，我们的系统减少了72%的试剂消耗，缩短了45%的文库制备时间，并将批间变异系数（CV）降低了20%。
- Keywords: surveillance, genomic, system, viral, active-matrix

### 12. [用于肝细胞优先 mRNA 递送的 TLS11a 修饰的可电离脂质纳米颗粒平台和多级验证的 CRISPR LDLR 敲除 HepG2 模型](https://www.biorxiv.org/content/10.64898/2026.07.21.739738v1)
- Original title: A TLS11a-decorated ionizable lipid nanoparticle platform and a multilevel-validated CRISPR LDLR-knockout HepG2 model for hepatocyte-preferential mRNA delivery
- Authors: Hussain, I., Kholaif, N., Alsultan, R., Eltahir, R., Alajlan, H. et al.
- Meta: 2026-07-22 | bioengineering | DOI: 10.64898/2026.07.21.739738
- 中文摘要: 可电离脂质纳米粒子 (LNP) 广泛用于将 CRISPR/Cas9 有效负载递送至肝细胞，但传统的肝脏摄取受到载脂蛋白 E 吸附和随后的低密度脂蛋白受体 (LDLR) 介导的内化的强烈影响。这种依赖性可能会限制 LDLR 缺陷环境中的特异性并降低疗效。在这里，我们设计了一个适体功能化的 LNP 平台，通过不依赖 LDLR 的途径实现肝细胞选择性基因组编辑，并使用基因定义的 LDLR 敲除 HepG2 模型验证其性能。使用硫醇-马来酰亚胺化学方法，将 Cas9 mRNA 和 LDLR 靶向引导 RNA 共封装的可电离 LNP 表面装饰有肝细胞癌靶向 TLS11a 适体。
- Abstract: Ionizable lipid nanoparticles (LNPs) are widely used for delivery of CRISPR/Cas9 payloads to hepatocytes, but conventional hepatic uptake is strongly influenced by adsorption of apolipoprotein E and subsequent low-density lipoprotein receptor (LDLR)-mediated internalization. This dependence may limit specificity and reduce efficacy in LDLR-deficient settings. Here, we designed an aptamer-functionalized LNP platform...
- Summary (fallback): 机器翻译摘要显示：可电离脂质纳米粒子 (LNP) 广泛用于将 CRISPR/Cas9 有效负载递送至肝细胞，但传统的肝脏摄取受到载脂蛋白 E 吸附和随后的低密度脂蛋白受体 (LDLR) 介导的内化的强烈影响。这种依赖性可能会限制 LDLR 缺陷环境中的特异性并降低疗效。在这里，我们设计了一个适体功能化的 LNP 平台，通过不依赖 LDLR 的途径实现肝细胞选择性基因组编辑，并使用基因定义的 LDLR 敲除 HepG2 模型验证其性能。使用硫醇-马来酰亚胺化学方法，将 Cas9 mRNA 和 LDLR 靶向引导 RNA 共封装的可电离 LNP 表面装饰有肝细胞癌靶向 TLS11a 适体。
- Keywords: delivery, hepg2, mrna, uptake, ionizable

### 13. [IL-32 是 MASLD 向 HCC 转变期间锁定在非典型 NF-κB 炎症环中的应激反应性节点](https://www.biorxiv.org/content/10.64898/2026.07.21.739717v1)
- Original title: IL-32 is a stress-responsive node locked in a noncanonical NF-κB inflammatory loop during MASLD to HCC transition
- Authors: Zhao, L. N., Kaldis, P., Andersen, J.
- Meta: 2026-07-22 | cancer biology | DOI: 10.64898/2026.07.21.739717
- 中文摘要: 背景：白介素 32 (IL-32) 在肝脏疾病中呈现出长期存在的悖论，在肝细胞癌 (HCC) 中表达显着升高，但对肝脂肪变性具有保护作用。典型受体或明确的分泌途径的缺乏使其生物学功能变得模糊。本研究旨在通过描述肝癌发生过程中控制 IL-32 活性的调节机制来解决这一悖论。方法：我们分析了两个内部前瞻性队列，包括 MASLD 队列和 MASLD 相关 HCC 队列，整合了匹配的转录组学和代谢组学数据。靶向脂质组学和多组学分析与单细胞和空间转录组学相结合。使用功能测定和基因扰动模型验证了主要发现。
- Abstract: Background: Interleukin-32 (IL-32) presents a long-standing paradox in liver disease, with markedly elevated expression in hepatocellular carcinoma (HCC) yet a protective role against hepatic steatosis. The absence of a canonical receptor or defined secretory pathway has obscured its biological function. This study aimed to resolve this paradox by delineating the regulatory mechanisms that govern IL-32 activity duri...
- Summary (fallback): 机器翻译摘要显示：背景：白介素 32 (IL-32) 在肝脏疾病中呈现出长期存在的悖论，在肝细胞癌 (HCC) 中表达显着升高，但对肝脂肪变性具有保护作用。典型受体或明确的分泌途径的缺乏使其生物学功能变得模糊。本研究旨在通过描述肝癌发生过程中控制 IL-32 活性的调节机制来解决这一悖论。方法：我们分析了两个内部前瞻性队列，包括 MASLD 队列和 MASLD 相关 HCC 队列，整合了匹配的转录组学和代谢组学数据。靶向脂质组学和多组学分析与单细胞和空间转录组学相结合。使用功能测定和基因扰动模型验证了主要发现。
- Keywords: il-32, inflammatory, during, kappa, paradox

### 14. [碳氮代谢基因E1OGDH1影响玉米根系结构和氮素可塑性](https://www.biorxiv.org/content/10.64898/2026.07.21.739812v1)
- Original title: The carbon-nitrogen metabolism gene E1OGDH1 influences maize root system architecture and nitrogen plasticity
- Authors: Cho, M., Liu, Z., Luebbert, C., Ziegler, G., Thiruppathi, D. et al.
- Meta: 2026-07-22 | plant biology | DOI: 10.64898/2026.07.21.739812
- 中文摘要: 合成氮肥极大地提高了作物产量，但施用的大部分氮肥却从农业生态系统中流失，造成环境污染和更高的经济成本。了解根系结构 (RSA) 如何控制土壤氮捕获可以提高氮吸收效率 (NUpE)。尽管根性状很少成为明确的育种目标，但对地上氮积累变化的选择也可能形成了 RSA 的差异。伊利诺伊州蛋白质菌株重组近交群体源自一个多世纪以来对种子蛋白质浓度的不同选择，为剖析 RSA 变异提供了强大的资源。
- Abstract: Synthetic nitrogen fertilizers have greatly increased crop yields, yet much of the applied nitrogen is lost from agroecosystems and contributes to environmental pollution and higher economic costs. Improving nitrogen uptake efficiency (NUpE) benefits from understanding how root system architecture (RSA) governs soil nitrogen capture. Although root traits have seldom been explicit breeding targets, selection for vari...
- Summary (fallback): 机器翻译摘要显示：合成氮肥极大地提高了作物产量，但施用的大部分氮肥却从农业生态系统中流失，造成环境污染和更高的经济成本。了解根系结构 (RSA) 如何控制土壤氮捕获可以提高氮吸收效率 (NUpE)。尽管根性状很少成为明确的育种目标，但对地上氮积累变化的选择也可能形成了 RSA 的差异。伊利诺伊州蛋白质菌株重组近交群体源自一个多世纪以来对种子蛋白质浓度的不同选择，为剖析 RSA 变异提供了强大的资源。
- Keywords: nitrogen, root, e1ogdh1, metabolism, carbon-nitrogen

### 15. [CRISPR-Cas9 诱导四倍体马铃薯中 BEL5 的敲除：通过重复从头再生优化方法及其对块茎的影响](https://www.biorxiv.org/content/10.64898/2026.07.21.739726v1)
- Original title: CRISPR-Cas9 Induced Knockout of BEL5 in Tetraploid Potato: Optimized Methodology via Repeated de novo Regeneration and Impact on Tuberization
- Authors: Zounkova, A., Chirivi, D., Pribylova, A., Martignago, D., Myslivcova, J. et al.
- Meta: 2026-07-22 | plant biology | DOI: 10.64898/2026.07.21.739726
- 中文摘要: CRISPR-Cas9 已成为植物靶向基因组编辑的强大工具；然而，由于其无性繁殖和复杂的高度杂合基因组，其在四倍体马铃薯（Solanum tuberosum ssp. tuberosum）中的应用仍然具有挑战性。特定基因型的全基因组序列数据的可用性对于确保完全敲除靶基因的所有等位基因同时最大限度地减少脱靶突变至关重要。在这项研究中，我们利用四倍体马铃薯品种 Desiree 报道了 CRISPR-Cas9 介导的 BEL5 基因的完全敲除，该基因编码转录因子，被称为驱动块茎形成的关键调节因子之一。我们采用农杆菌介导的转化，并证明重复的从头再生可以通过促进新突变的出现来提高编辑效率。
- Abstract: CRISPR-Cas9 has emerged as a powerful tool for targeted genome editing in plants; however, its application in tetraploid potato (Solanum tuberosum ssp. tuberosum) remains challenging due to its vegetative propagation and complex highly heterozygous genome. Availability of whole-genome sequence data for the specific genotype is crucial to ensure complete knockout of all alleles of target genes while minimizing off-ta...
- Summary (fallback): 机器翻译摘要显示：CRISPR-Cas9 已成为植物靶向基因组编辑的强大工具；然而，由于其无性繁殖和复杂的高度杂合基因组，其在四倍体马铃薯（Solanum tuberosum ssp. tuberosum）中的应用仍然具有挑战性。特定基因型的全基因组序列数据的可用性对于确保完全敲除靶基因的所有等位基因同时最大限度地减少脱靶突变至关重要。在这项研究中，我们利用四倍体马铃薯品种 Desiree 报道了 CRISPR-Cas9 介导的 BEL5 基因的完全敲除，该基因编码转录因子，被称为驱动块茎形成的关键调节因子之一。我们采用农杆菌介导的转化，并证明重复的从头再生可以通过促进新突变的出现来提高编辑效率。
- Keywords: bel5, potato, knockout, tuber, crispr-cas9

### 16. [工程恶臭假单胞菌中的七个突变解锁了严格的合成甲基营养](https://www.biorxiv.org/content/10.64898/2026.07.20.739708v1)
- Original title: Seven mutations unlock strict synthetic methylotrophy in engineered Pseudomonas putida
- Authors: Puiggene, O., Fricano, M., Rossi, R., Jansen, L. F. M., Ozdemir, E. et al.
- Meta: 2026-07-22 | synthetic biology | DOI: 10.64898/2026.07.20.739708
- 中文摘要: 甲醇是一种用于可持续生物生产的还原性、可溶性单碳 (C1) 原料，但将这种潜力转化为强劲的微生物生长仍然很困难。几种合成 C1 同化途径依赖于自催化循环，其运行需要氧化还原平衡、有毒中间体、底物再生和宿主调节的协调控制。在这里，我们在土壤细菌恶臭假单胞菌中实施了丝氨酸-苏氨酸循环（STC），并使用生长耦合选择和适应性实验室进化（ALE）从混合营养型C1掺入过渡到严格的甲基营养型。进化后的菌株在大气 CO2 下以甲醇作为唯一的碳和能源生长，倍增时间约为 100 倍。 40小时。
- Abstract: Methanol is a reduced, soluble one-carbon (C1) feedstock for sustainable bioproduction, but converting this potential into robust microbial growth remains difficult. Several synthetic C1 assimilation routes depend on autocatalytic cycles, whose operation requires coordinated control of redox balance, toxic intermediates, substrate regeneration, and host regulation. Here, we implemented the serine-threonine cycle (ST...
- Summary (fallback): 机器翻译摘要显示：甲醇是一种用于可持续生物生产的还原性、可溶性单碳 (C1) 原料，但将这种潜力转化为强劲的微生物生长仍然很困难。几种合成 C1 同化途径依赖于自催化循环，其运行需要氧化还原平衡、有毒中间体、底物再生和宿主调节的协调控制。在这里，我们在土壤细菌恶臭假单胞菌中实施了丝氨酸-苏氨酸循环（STC），并使用生长耦合选择和适应性实验室进化（ALE）从混合营养型C1掺入过渡到严格的甲基营养型。进化后的菌株在大气 CO2 下以甲醇作为唯一的碳和能源生长，倍增时间约为 100 倍。 40小时。
- Keywords: strict, synthetic, methylotrophy, putida, methanol

### 17. [通过共同组装丝状和液态 DNA 相来编程合成区室的内部结构](https://www.biorxiv.org/content/10.64898/2026.07.20.739699v1)
- Original title: Programming the Internal Architecture of Synthetic Compartments by Coassembling Filamentous and Liquid DNA Phases
- Authors: Dizani, M., Perlstein, B., McGrory, D., Afrose, S. P., Agarwal, S. et al.
- Meta: 2026-07-22 | synthetic biology | DOI: 10.64898/2026.07.20.739699
- 中文摘要: 活细胞依靠细丝和凝聚物作为其内部的关键组织者。使用可编程组件在合成室内共同开发这些结构原语是朝着构建功能性合成细胞、复合生物材料和合成组织迈出的一步。在这里，我们证明 DNA 纳米管和 DNA 凝聚物可以在细胞大小的隔室中共同组装，包括油包水滴和巨型单层囊泡 (GUV)。这两种纳米结构按预期形成，产生一种被不同形态的纳米管包围的单一冷凝物，这些纳米管的形态取决于 DNA 和盐浓度以及隔室大小。
- Abstract: Living cells rely on filaments and condensates as key organizers of their interior. Developing these structural primitives together inside synthetic compartments using programmable components is a step toward building functional synthetic cells, composite biomaterials, and synthetic tissues. Here, we demonstrate that DNA nanotubes and DNA condensates can be co-assembled within cell-sized compartments, including wate...
- Summary (fallback): 机器翻译摘要显示：活细胞依靠细丝和凝聚物作为其内部的关键组织者。使用可编程组件在合成室内共同开发这些结构原语是朝着构建功能性合成细胞、复合生物材料和合成组织迈出的一步。在这里，我们证明 DNA 纳米管和 DNA 凝聚物可以在细胞大小的隔室中共同组装，包括油包水滴和巨型单层囊泡 (GUV)。这两种纳米结构按预期形成，产生一种被不同形态的纳米管包围的单一冷凝物，这些纳米管的形态取决于 DNA 和盐浓度以及隔室大小。
- Keywords: synthetic, compartments, condensates, cells, filaments

### 18. [临床高危和首发精神病中的纵向白质轨迹：多中心 PSYSCAN 研究的结果](https://www.biorxiv.org/content/10.64898/2026.07.20.739516v1)
- Original title: Longitudinal White Matter Trajectories in Clinical High Risk and First-Episode Psychosis: Findings from the Multi-Centre PSYSCAN Study
- Authors: Bolte, L., Gifford, G., Serpa, M., Cottaar, M., Dazzan, P. et al.
- Meta: 2026-07-22 | neuroscience | DOI: 10.64898/2026.07.20.739516
- 中文摘要: 精神病与多个白质束中扩散衍生的分数各向异性（FA）的变化有关，但大多数证据都是横截面的。纵向研究结果不一致，白质随时间变化的临床相关性仍不清楚。为了解决这一差距，我们在一项大型多中心扩散张量成像研究中研究了早期精神病中的纵向白质变化及其临床相关性。在 18 个地点，407 名参与者（健康对照：n = 97，59.8% 男性，平均年龄 23.9 岁；临床高风险精神病：n = 158，53.5% 男性，平均年龄 23.0 岁；首发精神病：n = 152，71.1% 男性，平均年龄 25.1 岁）在 12 个月内最多三个时间点进行扫描。 FA 在扣带束、上纵束、额枕下束和全脑水平进行评估。
- Abstract: Psychosis has been linked to changes in diffusion-derived fractional anisotropy (FA) across multiple white matter tracts, yet most evidence is cross-sectional. Longitudinal findings are inconsistent, and the clinical relevance of white matter changes over time remains unclear. To address this gap, we investigated longitudinal white matter changes and their clinical correlates in early psychosis in a large, multi-cen...
- Summary (fallback): 机器翻译摘要显示：精神病与多个白质束中扩散衍生的分数各向异性（FA）的变化有关，但大多数证据都是横截面的。纵向研究结果不一致，白质随时间变化的临床相关性仍不清楚。为了解决这一差距，我们在一项大型多中心扩散张量成像研究中研究了早期精神病中的纵向白质变化及其临床相关性。在 18 个地点，407 名参与者（健康对照：n = 97，59.8% 男性，平均年龄 23.9 岁；临床高风险精神病：n = 158，53.5% 男性，平均年龄 23.0 岁；首发精神病：n = 152，71.1% 男性，平均年龄 25.1 岁）在 12 个月内最多三个时间点进行扫描。 FA 在扣带束、上纵束、额枕下束和全脑水平进行评估。
- Keywords: psychosis, longitudinal, white, matter, clinical

### 19. [语言结构和概率以高伽玛功率联合编码](https://www.biorxiv.org/content/10.64898/2026.07.21.739808v1)
- Original title: Linguistic structure and probability are jointly encoded in high gamma power
- Authors: Slaats, S., Hervais-Adelman, A.
- Meta: 2026-07-22 | neuroscience | DOI: 10.64898/2026.07.21.739808
- 中文摘要: 在语音理解过程中，大脑会根据感觉输入动态地推断出越来越抽象的表示的层次结构。推理层次中的一个重要步骤是组合单词以形成短语和句子。这个过程主要是由语言输入中的统计模式驱动的，还是由将单词组合成层次表示的机制驱动的，这是一个备受争议的话题，随着大型语言模型的出现，这个话题又重新变得重要起来。这项研究调查了颅内记录的局部皮质活动（高伽马功率；70-150 Hz）是否受到词汇概率和句法结构的共同调节；以及词汇概率是否影响句法结构的推理。
- Abstract: During speech comprehension, the brain dynamically infers a hierarchy of increasingly abstract representations from the sensory input. An important step in the inferential hierarchy is the combination of words to form phrases and sentences. Whether this process is driven primarily by statistical patterns in the linguistic input, or by a mechanism that combines words into hierarchical representations, is a subject of...
- Summary (fallback): 机器翻译摘要显示：在语音理解过程中，大脑会根据感觉输入动态地推断出越来越抽象的表示的层次结构。推理层次中的一个重要步骤是组合单词以形成短语和句子。这个过程主要是由语言输入中的统计模式驱动的，还是由将单词组合成层次表示的机制驱动的，这是一个备受争议的话题，随着大型语言模型的出现，这个话题又重新变得重要起来。这项研究调查了颅内记录的局部皮质活动（高伽马功率；70-150 Hz）是否受到词汇概率和句法结构的共同调节；以及词汇概率是否影响句法结构的推理。
- Keywords: lexical, structure, probability, syntactic, jointly

### 20. [从死后组织重建皮质的发育历史](https://www.biorxiv.org/content/10.64898/2026.07.21.739857v1)
- Original title: Reconstructing the developmental history of the cortex from postmortem tissue
- Authors: Murakami, T. C., Heintz, N.
- Meta: 2026-07-22 | neuroscience | DOI: 10.64898/2026.07.21.739857
- 中文摘要: 人脑的单细胞分辨率图谱对于理解细胞水平表型与疾病之间的联系至关重要。组织透明化和介观成像促进了细胞群的全器官量化，并有望推动神经系统疾病病理缺陷的识别。然而，由于皮质折叠模式和异质细胞分布的巨大变异性，人类脑组织的细观比较仍然具有挑战性。在这里，我们提出了对皮质的“回顾性”分析，该分析从组织的静态快照中重建神经干细胞的增殖历史，为跨样本比较提供了一个发育基础的坐标系。
- Abstract: Single-cell-resolution mapping of the human brain is central to understanding the link between cellular-level phenotypes and disease. Tissue clearing and mesoscale imaging have facilitated organ-wide quantification of cell populations and are expected to drive the identification of pathological deficits in neurological disorders. However, mesoscopic comparison of human brain tissue remains challenging because of lar...
- Summary (fallback): 机器翻译摘要显示：人脑的单细胞分辨率图谱对于理解细胞水平表型与疾病之间的联系至关重要。组织透明化和介观成像促进了细胞群的全器官量化，并有望推动神经系统疾病病理缺陷的识别。然而，由于皮质折叠模式和异质细胞分布的巨大变异性，人类脑组织的细观比较仍然具有挑战性。在这里，我们提出了对皮质的“回顾性”分析，该分析从组织的静态快照中重建神经干细胞的增殖历史，为跨样本比较提供了一个发育基础的坐标系。
- Keywords: cell, analysis, tissue, cortical, folding

### 21. [颗粒体蛋白前体单倍体不足重塑脑微血管和神经血管单元](https://www.biorxiv.org/content/10.64898/2026.07.20.738719v1)
- Original title: Progranulin haploinsufficiency remodels the cerebral microvasculature and neurovascular unit
- Authors: Chakraborty, S., Weick, M., Franciosa, S. A., Tabrizi, Z., Swinehart, C. et al.
- Meta: 2026-07-22 | neuroscience | DOI: 10.64898/2026.07.20.738719
- 中文摘要: 颗粒体蛋白前体（PGRN）缺乏是额颞叶痴呆（FTD）的一个主要遗传原因，但其对脑血管功能的影响仍未得到充分研究。在这里，我们发现 PGRN 缺乏有助于脑微血管灌注并诱导神经血管单元内的改变。体内双光子成像显示毛细血管停滞增加和脑血流量 (CBF) 减少，部分原因是白细胞-毛细血管相互作用增加和内皮 ICAM-1 表达升高。分离的脑微血管的转录组学分析表明，免疫和细胞外基质途径的协调上调，同时抑制血管生成和应激反应程序，表明内皮细胞激活。
- Abstract: Progranulin (PGRN) deficiency is a major genetic cause of frontotemporal dementia (FTD), yet its impact on cerebrovascular function remains understudied. Here, we show that PGRN deficiency contributes to cerebral microvascular perfusion and induces alterations within the neurovascular unit. In vivo two-photon imaging revealed increased capillary stalling and reductions in cerebral blood flow (CBF), driven in part by...
- Summary (fallback): 机器翻译摘要显示：颗粒体蛋白前体（PGRN）缺乏是额颞叶痴呆（FTD）的一个主要遗传原因，但其对脑血管功能的影响仍未得到充分研究。在这里，我们发现 PGRN 缺乏有助于脑微血管灌注并诱导神经血管单元内的改变。体内双光子成像显示毛细血管停滞增加和脑血流量 (CBF) 减少，部分原因是白细胞-毛细血管相互作用增加和内皮 ICAM-1 表达升高。分离的脑微血管的转录组学分析表明，免疫和细胞外基质途径的协调上调，同时抑制血管生成和应激反应程序，表明内皮细胞激活。
- Keywords: cerebral, progranulin, endothelial, neurovascular, unit

### 22. [APOE4 通过阻止神经元蛋白质组动力学破坏中心法则](https://www.biorxiv.org/content/10.64898/2026.07.15.738801v1)
- Original title: APOE4 disrupts the central dogma by arresting neuronal proteome dynamics
- Authors: Krogsaeter, E. K., McKetney, J., Lishi Li, L., Liu, I., Richards, A. L. et al.
- Meta: 2026-07-22 | neuroscience | DOI: 10.64898/2026.07.15.738801
- 中文摘要: 载脂蛋白 E4 (APOE4) 是晚发性阿尔茨海默病最强的遗传风险因素，并通过不完全了解的机制促进神经元功能障碍。在这里，我们整合了同基因 APOE3 和 APOE4 人类 iPSC 衍生神经元的转录组、翻译组和蛋白质组分析，发现 APOE4 从根本上损害神经元蛋白质组更新。尽管转录变化不大，但 APOE4 破坏了核糖体占据，改变了翻译动力学，并从转录水平解偶联了蛋白质丰度。全蛋白质组周转测量揭示了蛋白质半衰期的全球延长和长寿命蛋白质的广泛积累。功能蛋白质组学分析表明，同时存在的溶酶体和蛋白酶体损伤与蛋白酶体活性降低以及 APOE 与神经元蛋白酶体的关联增加相关。
- Abstract: Apolipoprotein E4 (APOE4) is the strongest genetic risk factor for late-onset Alzheimer's disease and promotes neuronal dysfunction through incompletely understood mechanisms. Here, we integrated transcriptomic, translatomic, and proteomic profiling of isogenic APOE3 and APOE4 human iPSC-derived neurons and found that APOE4 fundamentally impairs neuronal proteome renewal. Although transcriptional changes were modest...
- Summary (fallback): 机器翻译摘要显示：载脂蛋白 E4 (APOE4) 是晚发性阿尔茨海默病最强的遗传风险因素，并通过不完全了解的机制促进神经元功能障碍。在这里，我们整合了同基因 APOE3 和 APOE4 人类 iPSC 衍生神经元的转录组、翻译组和蛋白质组分析，发现 APOE4 从根本上损害神经元蛋白质组更新。尽管转录变化不大，但 APOE4 破坏了核糖体占据，改变了翻译动力学，并从转录水平解偶联了蛋白质丰度。全蛋白质组周转测量揭示了蛋白质半衰期的全球延长和长寿命蛋白质的广泛积累。功能蛋白质组学分析表明，同时存在的溶酶体和蛋白酶体损伤与蛋白酶体活性降低以及 APOE 与神经元蛋白酶体的关联增加相关。
- Keywords: apoe4, neuronal, proteome, protein, central

### 23. [浦肯野神经元中微管蛋白酪氨酸化的丧失不会导致其退化](https://www.biorxiv.org/content/10.64898/2026.07.21.739800v1)
- Original title: Loss of Tubulin Tyrosination in Purkinje Neurons Does Not Cause Their Degeneration
- Authors: Chakraborty, S., Paulcan, S., Janke, C., Magiera, M. M.
- Meta: 2026-07-22 | neuroscience | DOI: 10.64898/2026.07.21.739800
- 中文摘要: 微管蛋白的翻译后修饰 (PTM) 已被建议形成微管蛋白代码来协调微管功能。虽然在分子水平上 PTM 被证明以特定靶点的方式发挥作用，但一个突出的问题是它们控制细胞和生理功能的选择性。例如，一些微管蛋白 PTM 与神经变性有关，这表明无论哪个 PTM 失调都可能足以引起微管扰动并导致神经元死亡。在这里，我们测试酪氨酸化的扰动是否会导致浦肯野神经元的变性，类似于 PTM 多谷氨酰化异常积累时发生的情况。
- Abstract: Posttranslational modifications (PTMs) of tubulin have been suggested to form a tubulin code to coordinate microtubule functions. While at the molecular level PTMs were demonstrated to act in a target-specific manner, an outstanding question is the selectivity with which they control cellular and physiological functions. For instance, several tubulin PTMs have been linked to neurodegeneration, suggesting that whiche...
- Summary (fallback): 机器翻译摘要显示：微管蛋白的翻译后修饰 (PTM) 已被建议形成微管蛋白代码来协调微管功能。虽然在分子水平上 PTM 被证明以特定靶点的方式发挥作用，但一个突出的问题是它们控制细胞和生理功能的选择性。例如，一些微管蛋白 PTM 与神经变性有关，这表明无论哪个 PTM 失调都可能足以引起微管扰动并导致神经元死亡。在这里，我们测试酪氨酸化的扰动是否会导致浦肯野神经元的变性，类似于 PTM 多谷氨酰化异常积累时发生的情况。
- Keywords: tubulin, ptms, purkinje, neurons, cause

### 24. [测试全局神经元工作空间理论和综合信息论的时空预测](https://www.biorxiv.org/content/10.64898/2026.07.16.738188v1)
- Original title: Testing the Spatiotemporal Predictions of Global Neuronal Workspace Theory and Integrated Information Theory
- Authors: Bandara, K. H., Rowe, E., Garrido, M.
- Meta: 2026-07-22 | neuroscience | DOI: 10.64898/2026.07.16.738188
- 中文摘要: 意识感知背后的神经机制仍然存在争议，全局神经元工作空间理论（GNWT）和整合信息理论（IIT）对意识处理的时空动态提供了不同的预测。 Cogitate Consortium (2025) 最近进行了大规模对抗性合作，在 GNWT 和 IIT 之间进行仲裁；然而，他们的一些分析得出了不同的结果。由于最初的研究依赖于功能连接，因此无法评估直接测试这些理论的机械主张所需的定向神经影响。在这里，我们使用动态因果模型 (DCM) 重新检查了 Cogitate Consortium MEG 数据集 (N = 100)，以测试每种理论在与任务无关的面部感知期间预测的有效连接配置文件。
- Abstract: The neural mechanisms underlying conscious perception remain contested, with global neuronal workspace theory (GNWT) and integrated information theory (IIT) offering divergent predictions about the spatiotemporal dynamics of conscious processing. The Cogitate Consortium (2025) recently conducted a large-scale adversarial collaboration to arbitrate between GNWT and IIT; however, some of their analyses yielded mixed f...
- Summary (fallback): 机器翻译摘要显示：意识感知背后的神经机制仍然存在争议，全局神经元工作空间理论（GNWT）和整合信息理论（IIT）对意识处理的时空动态提供了不同的预测。 Cogitate Consortium (2025) 最近进行了大规模对抗性合作，在 GNWT 和 IIT 之间进行仲裁；然而，他们的一些分析得出了不同的结果。由于最初的研究依赖于功能连接，因此无法评估直接测试这些理论的机械主张所需的定向神经影响。在这里，我们使用动态因果模型 (DCM) 重新检查了 Cogitate Consortium MEG 数据集 (N = 100)，以测试每种理论在与任务无关的面部感知期间预测的有效连接配置文件。
- Keywords: theory, connectivity, testing, predictions, gnwt

### 25. [I型和II型干扰素对女性生殖道沙眼衣原体感染的调节](https://www.biorxiv.org/content/10.64898/2026.07.17.739123v1)
- Original title: Regulation of Chlamydia trachomatis infection in the female genital tract by type I and type II interferons
- Authors: He, R., Wu, Y., Abdelsalam, A., Wang, Y., Fan, H. et al.
- Meta: 2026-07-22 | immunology | DOI: 10.64898/2026.07.17.739123
- 中文摘要: 阴道内接种沙眼衣原体后，缺乏 I 型干扰素受体 IFNaR1 (IFNaR1-/-) 的小鼠在第 3 天和第 5 天显着增加了活衣原体的产量，但在第 7 天时将其降至野生型小鼠的水平，而缺乏 II 型干扰素受体 IFNgR1 (IFNgR1-/-) 的小鼠则显着增加了活衣原体产量第 5 天，这种增加在感染过程的剩余时间内持续存在。这些观察结果揭示了 I 型和 II 型干扰素在调节女性生殖道沙眼衣原体感染方面的时间分工。有趣的是，到第 6 周，缺乏 IFNaR1 和 IFNgR1 的小鼠表现出更高的死亡率，并且比 IFNgR1-/- 小鼠排出更多的衣原体生物体，这表明 IFNaR1 对于晚期沙眼衣原体的抑制仍然至关重要。
- Abstract: Following an intravaginal inoculation with Chlamydia trachomatis, mice deficient in type I interferon receptor IFNaR1 (IFNaR1-/-) significantly increased the yield of live chlamydiae on days 3 & 5 but reduced it to the level of wild-type mice by day 7, while mice deficient in type II interferon receptor IFNgR1 (IFNgR1-/-) significantly increased the chlamydial yield by day 5 and the increase persisted throughout the...
- Summary (fallback): 机器翻译摘要显示：阴道内接种沙眼衣原体后，缺乏 I 型干扰素受体 IFNaR1 (IFNaR1-/-) 的小鼠在第 3 天和第 5 天显着增加了活衣原体的产量，但在第 7 天时将其降至野生型小鼠的水平，而缺乏 II 型干扰素受体 IFNgR1 (IFNgR1-/-) 的小鼠则显着增加了活衣原体产量第 5 天，这种增加在感染过程的剩余时间内持续存在。这些观察结果揭示了 I 型和 II 型干扰素在调节女性生殖道沙眼衣原体感染方面的时间分工。有趣的是，到第 6 周，缺乏 IFNaR1 和 IFNgR1 的小鼠表现出更高的死亡率，并且比 IFNgR1-/- 小鼠排出更多的衣原体生物体，这表明 IFNaR1 对于晚期沙眼衣原体的抑制仍然至关重要。
- Keywords: type, trachomatis, infection, mice, interferon

### 26. [基苏木菌落的多位点表型表征，用于比较测试中心之间的杀虫剂敏感性](https://www.biorxiv.org/content/10.64898/2026.07.21.739746v1)
- Original title: Multi-site phenotypic characterisation of Kisumu colonies for comparison of insecticide susceptibility between testing centres
- Authors: Harvey, G. F., Praulins, G., Akoupou, S., Amlalo, G. K., Anthony, S. et al.
- Meta: 2026-07-22 | zoology | DOI: 10.64898/2026.07.21.739746
- 中文摘要: 杀虫剂和基于杀虫剂的病媒控制工具的测试依赖于生物测定的使用，通过生物测定，昆虫被暴露并测量死亡率或另一个相关的昆虫学终点。为了能够跨时间和空间比较产品之间的结果，使用了标准实验室菌株。在涉及杀虫剂抗性群体的研究中，通常使用杀虫剂敏感菌株作为比较物。 “Kisumu”是一种历史悠久、广泛使用的冈比亚按蚊杀虫剂敏感菌株。在这项研究中，不同国家的 16 个设施将其 3-5 天龄的基苏木群体暴露于四种杀虫剂（氯菊酯、高效氯氰菊酯、滴滴涕和甲基嘧啶磷）中，在 WHO 管试验中以不同浓度进行评估，以评估敏感性。
- Abstract: Testing of insecticides and insecticide-based vector control tools relies on the use of bioassays whereby insects are exposed and mortality, or another relevant entomological endpoint, is measured. To be able to compare results between products and across time and space standard laboratory strains are used. Insecticide-susceptible strains are often used as comparators in studies involving insecticide-resistant popul...
- Summary (fallback): 机器翻译摘要显示：杀虫剂和基于杀虫剂的病媒控制工具的测试依赖于生物测定的使用，通过生物测定，昆虫被暴露并测量死亡率或另一个相关的昆虫学终点。为了能够跨时间和空间比较产品之间的结果，使用了标准实验室菌株。在涉及杀虫剂抗性群体的研究中，通常使用杀虫剂敏感菌株作为比较物。 “Kisumu”是一种历史悠久、广泛使用的冈比亚按蚊杀虫剂敏感菌株。在这项研究中，不同国家的 16 个设施将其 3-5 天龄的基苏木群体暴露于四种杀虫剂（氯菊酯、高效氯氰菊酯、滴滴涕和甲基嘧啶磷）中，在 WHO 管试验中以不同浓度进行评估，以评估敏感性。
- Keywords: colonies, testing, kisumu, results, strains

### 27. [进化限制限制了雪貂对牛源 H5N1 流感病毒的额外哺乳动物适应性](https://www.biorxiv.org/content/10.64898/2026.07.20.739655v1)
- Original title: Evolutionary constraints limit additional mammalian adaptation of bovine-derived H5N1 influenza viruses in ferrets
- Authors: Machkovech, H. M., Wei, W., Gu, C., Guan, L., Biswas, A. et al.
- Meta: 2026-07-22 | microbiology | DOI: 10.64898/2026.07.20.739655
- 中文摘要: 美国奶牛中 2.3.4.4b 分支 H5N1 病毒的爆发引发了人们的担忧，即农业哺乳动物之间的持续传播可能会促进病毒适应有效的人类传播。然而，人们对控制这种适应的进化动力学仍然知之甚少。在这里，我们研究了两种牛源性 H5N1 B3.13 基因型病毒在雪貂中感染和空气传播过程中的进化，基于其强大复制和低效空气传播的先前特征。在宿主体内，病毒遗传多样性有限，病毒容易发生遗传漂变和弱纯化选择。当传播发生时，其特点是存在严格的瓶颈，导致病毒遗传多样性急剧下降。我们没有发现哺乳动物在感染或传播过程中适应的证据。
- Abstract: The outbreak of clade 2.3.4.4b H5N1 viruses among U.S. dairy cattle has raised concerns that sustained circulation among agricultural mammals could facilitate viral adaptation toward efficient human transmission. However, the evolutionary dynamics governing such adaptation remain poorly understood. Here we investigated the evolution of two bovine-derived H5N1 B3.13 genotype viruses during infection and airborne tran...
- Summary (fallback): 机器翻译摘要显示：美国奶牛中 2.3.4.4b 分支 H5N1 病毒的爆发引发了人们的担忧，即农业哺乳动物之间的持续传播可能会促进病毒适应有效的人类传播。然而，人们对控制这种适应的进化动力学仍然知之甚少。在这里，我们研究了两种牛源性 H5N1 B3.13 基因型病毒在雪貂中感染和空气传播过程中的进化，基于其强大复制和低效空气传播的先前特征。在宿主体内，病毒遗传多样性有限，病毒容易发生遗传漂变和弱纯化选择。当传播发生时，其特点是存在严格的瓶颈，导致病毒遗传多样性急剧下降。我们没有发现哺乳动物在感染或传播过程中适应的证据。
- Keywords: transmission, viruses, evolutionary, mammalian, adaptation

### 28. [单分子纳米孔镊子分析完整和“无茎”酵母 RNA 聚合酶 II 的转录延伸](https://www.biorxiv.org/content/10.64898/2026.07.20.739707v1)
- Original title: Single-molecule nanopore-tweezers analysis of transcription elongation by intact and "stalk-less" yeast RNA polymerase II
- Authors: Yang, S., Chen, M., Craig, J. M., Laszlo, A. H., Gundlach, J. H. et al.
- Meta: 2026-07-22 | molecular biology | DOI: 10.64898/2026.07.20.739707
- 中文摘要: 单分子皮米分辨率纳米孔镊子 (SPRNT) 能够通过序列配准、亚核苷酸空间分辨率、亚毫秒时间分辨率以及施加协助或反对易位的力的能力来监测核酸轨道上核酸运动蛋白的易位。最近，我们利用SPRNT分析了大肠杆菌RNA聚合酶单分子在转录延伸过程中相对于DNA模板链的易位，并直接检测到了大肠杆菌yrbL共有暂停元件处的序列依赖性暂停和“半易位状态”的形成。
- Abstract: Single-molecule picometer-resolution nanopore tweezers (SPRNT) enables monitoring of translocation of a nucleic-acid motor protein on a nucleic-acid track with sequence registration, sub-nucleotide spatial resolution, sub-millisecond temporal resolution, and the ability to apply forces that assist or oppose translocation. Recently, we used SPRNT to analyze the translocation of single molecules of Escherichia coli RN...
- Summary (fallback): 机器翻译摘要显示：单分子皮米分辨率纳米孔镊子 (SPRNT) 能够通过序列配准、亚核苷酸空间分辨率、亚毫秒时间分辨率以及施加协助或反对易位的力的能力来监测核酸轨道上核酸运动蛋白的易位。最近，我们利用SPRNT分析了大肠杆菌RNA聚合酶单分子在转录延伸过程中相对于DNA模板链的易位，并直接检测到了大肠杆菌yrbL共有暂停元件处的序列依赖性暂停和“半易位状态”的形成。
- Keywords: translocation, intact, stalk-less, resolution, coli

### 29. [SpatialJEPA：受 JEPA 启发的图形上下文蒸馏，用于空间感知多组学集成](https://www.biorxiv.org/content/10.64898/2026.07.21.739810v1)
- Original title: SpatialJEPA: JEPA-inspired graph-context distillation for spatially aware multiomics integration
- Authors: Mann-Krzisnik, D., Li, Y.
- Meta: 2026-07-22 | molecular biology | DOI: 10.64898/2026.07.21.739810
- 中文摘要: 用于整合空间基因组学模式的计算框架将基于细胞的表示学习扩展到分子层，但许多配对的 RNA-ATAC 数据集是分离的并且缺乏空间坐标。我们介绍 SpatialJEPA，这是一个受 JEPA 启发的师生框架，用于将空间上下文从空间多组学数据转移到非空间多组学数据。与补丁或特征屏蔽目标相反，SpatialJEPA 在学生训练期间通过用仅自我的身份图替换教师的空间邻域图来屏蔽空间上下文，使空间样本对学生来说显得分离。学生从图上下文限制的视图中学习匹配教师嵌入，因此可以在推理时应用于分离的 RNA-ATAC 数据。
- Abstract: Computational frameworks for integrating spatial genomics modalities extend cell-based representation learning across molecular layers, but many paired RNA-ATAC datasets are dissociated and lack spatial coordinates. We introduce SpatialJEPA, a JEPA-inspired teacher-student framework for transferring spatial context from spatial multiomics data to non-spatial multiome data. In contrast to patch- or feature-masking ob...
- Summary (fallback): 机器翻译摘要显示：用于整合空间基因组学模式的计算框架将基于细胞的表示学习扩展到分子层，但许多配对的 RNA-ATAC 数据集是分离的并且缺乏空间坐标。我们介绍 SpatialJEPA，这是一个受 JEPA 启发的师生框架，用于将空间上下文从空间多组学数据转移到非空间多组学数据。与补丁或特征屏蔽目标相反，SpatialJEPA 在学生训练期间通过用仅自我的身份图替换教师的空间邻域图来屏蔽空间上下文，使空间样本对学生来说显得分离。学生从图上下文限制的视图中学习匹配教师嵌入，因此可以在推理时应用于分离的 RNA-ATAC 数据。
- Keywords: spatial, spatialjepa, multiomics, dissociated, student

### 30. [复制耦合搜索在 DNA 错配修复中为链切口定位 MutH](https://www.biorxiv.org/content/10.64898/2026.07.21.739762v1)
- Original title: Replication-coupled search positions MutH for strand incision in DNA mismatch repair
- Authors: Moores, A. N., Banaz, N., Makamure, T., Uphoff, S.
- Meta: 2026-07-22 | molecular biology | DOI: 10.64898/2026.07.21.739762
- 中文摘要: DNA 错配修复 (MMR) 通过纠正复制错误来保障基因组稳定性，但其组成部分如何作为活细胞中的有效途径进行协调仍不清楚。在大肠杆菌中，MutS 和 MutL 检测到错配，并且必须快速激活 MutH 以在远处的 GATC 位点切割新生 DNA 链。在这里，我们使用活细胞单分子追踪来解决 MMR 蛋白在体内的目标搜索动态。我们发现 MutH 在半甲基化 GATC 位点结合 DNA，与错配识别无关，且无需 MutS 或 MutL。 DNA 复制叉附近从快速扩散模式转变为慢速搜索模式，促进了 MutH 的自主招募。该指导允许 MutH 在复制叉之后暂时占据潜在的切口位点，等待 MutS-MutL 的激活。
- Abstract: DNA mismatch repair (MMR) safeguards genome stability by correcting replication errors, yet how its components coordinate as an efficient pathway in living cells remains unclear. In Escherichia coli, MutS and MutL detect mismatches and must rapidly activate MutH to incise the nascent DNA strand at distantly located GATC sites. Here, we used live-cell single-molecule tracking to resolve the target-search dynamics of...
- Summary (fallback): 机器翻译摘要显示：DNA 错配修复 (MMR) 通过纠正复制错误来保障基因组稳定性，但其组成部分如何作为活细胞中的有效途径进行协调仍不清楚。在大肠杆菌中，MutS 和 MutL 检测到错配，并且必须快速激活 MutH 以在远处的 GATC 位点切割新生 DNA 链。在这里，我们使用活细胞单分子追踪来解决 MMR 蛋白在体内的目标搜索动态。我们发现 MutH 在半甲基化 GATC 位点结合 DNA，与错配识别无关，且无需 MutS 或 MutL。 DNA 复制叉附近从快速扩散模式转变为慢速搜索模式，促进了 MutH 的自主招募。该指导允许 MutH 在复制叉之后暂时占据潜在的切口位点，等待 MutS-MutL 的激活。
- Keywords: muth, replication, mismatch, repair, sites

## medrxiv

### 1. [serocalculator，一个 R 包，用于根据横截面血清学数据估计血清发生率](https://www.medrxiv.org/content/10.1101/2025.06.04.25328941v4)
- Original title: serocalculator, an R package for estimating seroincidence from cross-sectional serological data
- Authors: Lai, K. W., Orwa, C., Seidman, J. C., Garrett, D. O., Saha, S. K. et al.
- Meta: 2026-07-22 | epidemiology | DOI: 10.1101/2025.06.04.25328941
- 中文摘要: 动机：血清发病率（人群中新感染率）是了解病原体传播动态和为公共卫生行动提供信息的关键指标，特别是当临床监测对于人群水平发病率估计不可行或不可靠时。实现：血清计算器是一个开源 R 包，它使用基于可能性的框架，结合建模的抗体衰减、生物变异性和测量噪声，根据横截面血清学数据估计泊松感染过程下的血清发生率。一般功能：该软件包支持使用单个或多个生物标志物进行整体和分层血清发生率估计。
- Abstract: Motivation: Seroincidence----the rate of new infections in a population--is a key measure for understanding pathogen transmission dynamics and informing public health action, particularly when clinical surveillance is not feasible or reliable for population-level incidence estimation. Implementation: serocalculator is an open-source R package that uses a likelihood-based framework incorporating modeled antibody deca...
- Summary (fallback): 机器翻译摘要显示：动机：血清发病率（人群中新感染率）是了解病原体传播动态和为公共卫生行动提供信息的关键指标，特别是当临床监测对于人群水平发病率估计不可行或不可靠时。实现：血清计算器是一个开源 R 包，它使用基于可能性的框架，结合建模的抗体衰减、生物变异性和测量噪声，根据横截面血清学数据估计泊松感染过程下的血清发生率。一般功能：该软件包支持使用单个或多个生物标志物进行整体和分层血清发生率估计。
- Keywords: serocalculator, package, seroincidence, cross-sectional, antibody

### 2. [肌肉稳定性缺陷与足球运动员的肌肉骨骼疾病密切相关：自适应力比优于传统力量参数——一项带有初步随访的横断面研究](https://www.medrxiv.org/content/10.64898/2026.07.07.26357205v2)
- Original title: Muscle stability deficits are strongly associated with musculoskeletal complaints in football (soccer) players: Adaptive Force ratio outperforms conventional strength parameters--a cross-sectional study with preliminary follow-up
- Authors: Schaefer, L. V., Bittmann, F. N., Ulrich, J., Prill, R., Becker, R.
- Meta: 2026-07-22 | sports medicine | DOI: 10.64898/2026.07.07.26357205
- 中文摘要: 目的鉴于足球运动中的高损伤负担以及基于力量的筛查的局限性，需要采取新的方法。适应性力（AF）——比推/拉力量更接近容易受伤的动作——提供了一种替代方案。这项研究研究了足球运动员基于 AF 的肌肉稳定性与肌肉骨骼疾病之间的关联，并比较了 AF 衍生的力量参数和传统力量参数的判别能力，并辅以初步的前瞻性随访。方法测量了 23 名男性足球运动员五个双侧肌肉群（膝关节伸肌/屈肌；髋屈肌/内收肌/外展肌）的 AF 和最大自主等长收缩 (MVIC)。
- Abstract: ObjectiveGiven the high injury burden in football and the documented limitations of strength-based screening, novel approaches are warranted. Adaptive Force (AF)--being closer to injury-prone movements than pushing/pulling strength--offers an alternative. This study examined the association between AF-based muscle stability and musculoskeletal complaints in football players and compared AF-derived and conventional s...
- Summary (fallback): 机器翻译摘要显示：目的鉴于足球运动中的高损伤负担以及基于力量的筛查的局限性，需要采取新的方法。适应性力（AF）——比推/拉力量更接近容易受伤的动作——提供了一种替代方案。这项研究研究了足球运动员基于 AF 的肌肉稳定性与肌肉骨骼疾病之间的关联，并比较了 AF 衍生的力量参数和传统力量参数的判别能力，并辅以初步的前瞻性随访。方法测量了 23 名男性足球运动员五个双侧肌肉群（膝关节伸肌/屈肌；髋屈肌/内收肌/外展肌）的 AF 和最大自主等长收缩 (MVIC)。
- Keywords: complaints, players, strength, muscle, football

### 3. [索马鲁肽改变人类胚胎-子宫内膜界面](https://www.medrxiv.org/content/10.64898/2026.03.03.26347354v2)
- Original title: Semaglutide alters the human embryo-endometrium interface
- Authors: Apostolov, A., Pathare, A. D. S., Lavogina, D., Zhao, C., Kask, K. et al.
- Meta: 2026-07-22 | obstetrics and gynecology | DOI: 10.64898/2026.03.03.26347354
- 中文摘要: 索马鲁肽 (SE) 是一种具有降血糖和减肥作用的胰高血糖素样肽 1 受体激动剂 (GLP-1RA)，其使用量迅速增加，特别是在育龄妇女中。虽然临床前研究表明通过下丘脑-垂体-卵巢轴对卵巢功能有益，但其对子宫内膜-胚胎界面的影响仍不清楚。在这里，我们发现 GLP-1R 在人子宫内膜中动态表达，仅限于上皮细胞，并在月经周期的分泌中期显着上调。 SE 激活细胞内 cAMP 信号传导并增强上皮代谢，推动氧化磷酸化的转变。
- Abstract: The use of semaglutide (SE), a glucagon-like peptide-1 receptor agonist (GLP-1RA) with glucose-lowering and weight-loss effects, has risen rapidly, particularly among women of reproductive age. While preclinical studies suggest benefits for ovarian function via the hypothalamic-pituitary-ovarian axis, its impact on the endometrial-embryo interface remains unclear. Here, we show that GLP-1R is dynamically expressed i...
- Summary (fallback): 机器翻译摘要显示：索马鲁肽 (SE) 是一种具有降血糖和减肥作用的胰高血糖素样肽 1 受体激动剂 (GLP-1RA)，其使用量迅速增加，特别是在育龄妇女中。虽然临床前研究表明通过下丘脑-垂体-卵巢轴对卵巢功能有益，但其对子宫内膜-胚胎界面的影响仍不清楚。在这里，我们发现 GLP-1R 在人子宫内膜中动态表达，仅限于上皮细胞，并在月经周期的分泌中期显着上调。 SE 激活细胞内 cAMP 信号传导并增强上皮代谢，推动氧化磷酸化的转变。
- Keywords: human, glp-1r, epithelial, priming, stromal

### 4. [健康框架消息及其对夏令时态度的影响](https://www.medrxiv.org/content/10.1101/2025.10.11.25337370v2)
- Original title: Health-Framed Messaging and Its Impact on Attitudes Toward Daylight Saving Time
- Authors: Weger, M., von Hippel, C., Gachon, F., Weger, B. D.
- Meta: 2026-07-22 | health policy | DOI: 10.1101/2025.10.11.25337370
- 中文摘要: 目的 本研究旨在调查澳大利亚公众对夏令时 (DST) 的态度及其对健康的影响，其中州级夏令时采用情况的差异提供了一个独特的环境，可以测试暴露于夏令时相关的健康风险信息是否会影响这些态度，以及个体差异如何调节这种影响。方法 在一项预先注册的随机在线实验中，澳大利亚成年人 (n = 499) 被分配接收有关夏令时的中立信息或强调夏令时负面健康后果的与夏令时相关的健康风险信息。评估了参与者对夏令时的态度、政策偏好、感知的健康后果、预先存在的健康意识和可信度认知，并随后收集了社会人口特征。使用微型慕尼黑 ChronoType 问卷对 ChronoType 进行评估。
- Abstract: Objectives This study aimed to examine public attitudes toward daylight saving time (DST) and its perceived health consequences in Australia, where state-level variation in DST adoption provides a unique setting to test whether the exposure to DST-related health risk information influences these attitudes and how individual differences moderate this effect. Methods In a preregistered, randomized online experiment, A...
- Summary (fallback): 机器翻译摘要显示：目的 本研究旨在调查澳大利亚公众对夏令时 (DST) 的态度及其对健康的影响，其中州级夏令时采用情况的差异提供了一个独特的环境，可以测试暴露于夏令时相关的健康风险信息是否会影响这些态度，以及个体差异如何调节这种影响。方法 在一项预先注册的随机在线实验中，澳大利亚成年人 (n = 499) 被分配接收有关夏令时的中立信息或强调夏令时负面健康后果的与夏令时相关的健康风险信息。评估了参与者对夏令时的态度、政策偏好、感知的健康后果、预先存在的健康意识和可信度认知，并随后收集了社会人口特征。使用微型慕尼黑 ChronoType 问卷对 ChronoType 进行评估。
- Keywords: health, messaging, consequences, attitudes, toward

### 5. [评估模型复杂性在虚拟临床试验结果中的作用](https://www.medrxiv.org/content/10.64898/2025.12.22.25342808v3)
- Original title: Assessing the Role of Model Complexity in Virtual Clinical Trial Outcomes
- Authors: Gevertz, J. L., Wares, J. R.
- Meta: 2026-07-22 | pharmacology and therapeutics | DOI: 10.64898/2025.12.22.25342808
- 中文摘要: 虚拟临床试验 (VCT) 为改善药物开发流程带来了巨大希望，但其预测可靠性在很大程度上取决于人们对设计决策的了解仍知之甚少。本研究探讨了模型复杂性如何影响 VCT 结果，以及先验参数分布和虚拟患者纳入标准的选择如何影响这些结果。以小鼠肿瘤的溶瘤病毒疗法治疗作为案例研究，我们比较了在不同参数先验（均匀分布和正态分布）和两种纳入方法（接受或拒绝和接受或扰动）下复杂性不断增加的三种数学模型的相对层次结构。我们的结果表明，最简单的模型产生的合理群体不足以跨越可行的轨迹空间，可能会丢失关键的患者间异质性。
- Abstract: Virtual clinical trials (VCTs) hold significant promise for improving the drug development process, yet their predictive reliability depends critically on design decisions that remain poorly understood. This study examines how model complexity influences VCT outcomes, as well as how the choice of prior parameter distributions and virtual patient inclusion criteria affects those outcomes. Using oncolytic virotherapy...
- Summary (fallback): 机器翻译摘要显示：虚拟临床试验 (VCT) 为改善药物开发流程带来了巨大希望，但其预测可靠性在很大程度上取决于人们对设计决策的了解仍知之甚少。本研究探讨了模型复杂性如何影响 VCT 结果，以及先验参数分布和虚拟患者纳入标准的选择如何影响这些结果。以小鼠肿瘤的溶瘤病毒疗法治疗作为案例研究，我们比较了在不同参数先验（均匀分布和正态分布）和两种纳入方法（接受或拒绝和接受或扰动）下复杂性不断增加的三种数学模型的相对层次结构。我们的结果表明，最简单的模型产生的合理群体不足以跨越可行的轨迹空间，可能会丢失关键的患者间异质性。
- Keywords: complexity, model, prior, inclusion, virtual
