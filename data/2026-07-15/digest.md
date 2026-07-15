# daily2rxiv Digest - 2026-07-15

共收录 68 篇论文。

## arxiv

### 1. [视频传播模型中的序列性差距](https://arxiv.org/abs/2607.13031v1)
- Original title: The Seriality Gap in Video Diffusion Models
- Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai
- Meta: 2026-07-14 | cs.LG
- 中文摘要: 当一个球击中另一个球，然后击中另一个球时，视频模型应该预测每次弹跳的后果。在多球硬球动力学的受控实验中，我们发现，即使提供更多的降噪步骤，标准双向视频扩散的性能也会随着因果链的延长而降低。在长度匹配的单球控制中，不存在球与球的相互作用，退化很大程度上消失，隔离相关事件结构而不是视频长度作为原因。在干预研究中，增加有效串行计算的方法极大地提高了性能，包括自回归/分块生成和架构深度。我们将这种模式识别为串行差距：需要不断增长的串行计算的任务与视频扩散模型之间的不匹配，而视频扩散模型的去噪循环不提供可扩展的串行计算...
- Abstract: When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent, the degradation l...
- Summary (fallback): 机器翻译摘要显示：当一个球击中另一个球，然后击中另一个球时，视频模型应该预测每次弹跳的后果。在多球硬球动力学的受控实验中，我们发现，即使提供更多的降噪步骤，标准双向视频扩散的性能也会随着因果链的延长而降低。在长度匹配的单球控制中，不存在球与球的相互作用，退化很大程度上消失，隔离相关事件结构而不是视频长度作为原因。在干预研究中，增加有效串行计算的方法极大地提高了性能，包括自回归/分块生成和架构深度。我们将这种模式识别为串行差距：需要不断增长的串行计算的任务与视频扩散模型之间的不匹配，而视频扩散模型的去噪循环不提供可扩展的串行计算...
- Keywords: video, serial, diffusion, models, denoising

### 2. [TerraZero：大规模零演示自我游戏的程序驾驶模拟](https://arxiv.org/abs/2607.13028v1)
- Original title: TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale
- Authors: Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee et al.
- Meta: 2026-07-14 | cs.LG
- 中文摘要: 训练强大的自动驾驶代理需要一个模拟器，该模拟器必须足够快以进行大规模强化学习，足够真实以在现实世界地图结构中提供基础行为，并且足够多样化以涵盖记录数据很少包含的安全关键长尾。我们推出 TerraZero，一个程序化驾驶模拟器和自玩训练堆栈。可配置的 C 引擎通过零复制路径在 CPU 上运行模拟并在 GPU 上运行策略推理，在单个服务器级 GPU 上维持每秒 130 万个代理步骤，远快于现有的对象级模拟器，同时保持保真度较轻的单代理系统省略：异构代理、多个动态模型和完整的流量规则实施。
- Abstract: Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and poli...
- Summary (fallback): 机器翻译摘要显示：训练强大的自动驾驶代理需要一个模拟器，该模拟器必须足够快以进行大规模强化学习，足够真实以在现实世界地图结构中提供基础行为，并且足够多样化以涵盖记录数据很少包含的安全关键长尾。我们推出 TerraZero，一个程序化驾驶模拟器和自玩训练堆栈。可配置的 C 引擎通过零复制路径在 CPU 上运行模拟并在 GPU 上运行策略推理，在单个服务器级 GPU 上维持每秒 130 万个代理步骤，远快于现有的对象级模拟器，同时保持保真度较轻的单代理系统省略：异构代理、多个动态模型和完整的流量规则实施。
- Keywords: driving, terrazero, self-play, agents, policy

### 3. [通过流量匹配实现统计稳态湍流的捷径](https://arxiv.org/abs/2607.13022v1)
- Original title: A Shortcut to Statistically Steady-State Turbulence with Flow Matching
- Authors: Gianluca Galletti, Gerald Gutenbrunner, William Hornsby, Lorenzo Zanisi, Naomi Carey et al.
- Meta: 2026-07-14 | physics.plasm-ph
- 中文摘要: 许多非线性物理系统表现出一个初始瞬态阶段，其中扰动在非线性相互作用导致统计稳态之前增长。虽然这种饱和状态是人们最感兴趣的，但直接数值模拟必须在达到它之前解决完整的瞬态动力学，从而产生大量的计算成本。在计算流体动力学中，大涡模拟等降阶方法通过对小规模动力学进行建模来降低计算成本，从而实现湍流的易于处理的近似。相比之下，对于回旋动力学等系统，通常无法获得相对有效的完整动力学闭包，并且仍然需要高保真度模拟。这些系统的现有替代建模方法是自回归的，因此它们会遭受累积误差的影响。
- Abstract: Many nonlinear physical systems exhibit an initial transient phase in which perturbations grow before nonlinear interactions lead to a statistically steady state. While this saturated regime is of primary interest, direct numerical simulations must resolve the full transient dynamics before reaching it, incurring significant computational cost. In Computational Fluid Dynamics, reduced-order approaches such as Large...
- Summary (fallback): 机器翻译摘要显示：许多非线性物理系统表现出一个初始瞬态阶段，其中扰动在非线性相互作用导致统计稳态之前增长。虽然这种饱和状态是人们最感兴趣的，但直接数值模拟必须在达到它之前解决完整的瞬态动力学，从而产生大量的计算成本。在计算流体动力学中，大涡模拟等降阶方法通过对小规模动力学进行建模来降低计算成本，从而实现湍流的易于处理的近似。相比之下，对于回旋动力学等系统，通常无法获得相对有效的完整动力学闭包，并且仍然需要高保真度模拟。这些系统的现有替代建模方法是自回归的，因此它们会遭受累积误差的影响。
- Keywords: dynamics, systems, transient, phase, saturated

### 4. [DermDepth：面向皮肤病学的单目公制 3D 重建模型](https://arxiv.org/abs/2607.13010v1)
- Original title: DermDepth: Toward Monocular Metric Scale 3D Reconstruction Models for Dermatology
- Authors: Héctor Carrión, Narges Norouzi
- Meta: 2026-07-14 | cs.CV
- 中文摘要: 皮肤病学实践通常涉及测量和跟踪病变大小、形态和纹理，作为伤口或皮肤癌筛查、监测和诊断的关键组成部分。为了完成这项任务，从业者经常使用常用的现成相机传感器对皮肤表面进行成像。这导致了对 2D 方法的大量研究关注，而这些目标自然受益于 3D 信息。在本文中，我们证明了在皮肤镜和宏观情况下都可以实现密集的单目 3D 重建、公制尺度测量和丰富的表面法线纹理估计，而无需额外的硬件或多次捕获。我们推出了 DermDepth（皮肤科领域第一个单视图公制尺度 3D 模型）和 D-Synth（第一个具有像素完美 3D 信息的合成皮肤镜数据集）。
- Abstract: Dermatological practice routinely involves measuring and tracking lesion size, morphology and texture, as critical components of wound or skin cancer screening, monitoring and diagnosis. To accomplish this task, practitioners often image the skin surface with commonly available off-the-shelf camera sensors. This has led to an overwhelming research focus on 2D methods while these objectives naturally benefit from 3D...
- Summary (fallback): 机器翻译摘要显示：皮肤病学实践通常涉及测量和跟踪病变大小、形态和纹理，作为伤口或皮肤癌筛查、监测和诊断的关键组成部分。为了完成这项任务，从业者经常使用常用的现成相机传感器对皮肤表面进行成像。这导致了对 2D 方法的大量研究关注，而这些目标自然受益于 3D 信息。在本文中，我们证明了在皮肤镜和宏观情况下都可以实现密集的单目 3D 重建、公制尺度测量和丰富的表面法线纹理估计，而无需额外的硬件或多次捕获。我们推出了 DermDepth（皮肤科领域第一个单视图公制尺度 3D 模型）和 D-Synth（第一个具有像素完美 3D 信息的合成皮肤镜数据集）。
- Keywords: dermdepth, metric, scale, texture, dermoscopic

### 5. [频谱还不够：当上下文有助于时间序列预测时](https://arxiv.org/abs/2607.13006v1)
- Original title: The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting
- Authors: Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban
- Meta: 2026-07-14 | cs.LG
- 中文摘要: 越来越多的指数系列对一系列指标的可预测性进行评分。从业者越来越多地将这些分数视为回答一个不同的问题：\emph{添加上下文}、更长的回顾、检索插件或预训练模型是否会有帮助。这些不是同一个问题。上下文的值是操作点的属性，而不是系列的属性。从功率谱构建的任何指数在相位随机化下都是不变的，而检索和基础模型提供的超二阶值则不然，因为相位随机化序列是渐近高斯分布的。我们将其表述为不可能的结果，并将其与通过构造固定频谱和边际的代理对隔离。
- Abstract: A growing family of indices scores how predictable a series is from its spectrum. Practitioners increasingly read these scores as answering a different question: whether \emph{adding context}, a longer lookback, a retrieval plug-in, or a pretrained model, will help. These are not the same question. The value of context is a property of the operating point, not of the series. Any index built from the power spectrum i...
- Summary (fallback): 机器翻译摘要显示：越来越多的指数系列对一系列指标的可预测性进行评分。从业者越来越多地将这些分数视为回答一个不同的问题：\emph{添加上下文}、更长的回顾、检索插件或预训练模型是否会有帮助。这些不是同一个问题。上下文的值是操作点的属性，而不是系列的属性。从功率谱构建的任何指数在相位随机化下都是不变的，而检索和基础模型提供的超二阶值则不然，因为相位随机化序列是渐近高斯分布的。我们将其表述为不可能的结果，并将其与通过构造固定频谱和边际的代理对隔离。
- Keywords: value, spectrum, context, series, retrieval

### 6. [生成模型的水印取证：信息论的视角](https://arxiv.org/abs/2607.13003v1)
- Original title: Watermark Forensics for Generative Models: An Information-Theoretic Perspective
- Authors: Xiaoyu Li, Zheng Gao, Xiaoyan Feng, Jiaojiao Jiang, Yulei Sui et al.
- Meta: 2026-07-14 | cs.CR
- 中文摘要: 生成模型输出中的水印通常仅询问文本是否是机器制作的。相同的标记可以做更多的事情：将其归因于生成它的用户，提取隐藏的有效负载，或者本地化编辑后幸存的部分。这些形成了一个取证阶梯，我们询问样本长度 $n$ 中每个梯级的成本是多少。一个对象组织答案。令 $S$ 为标记携带的秘密（用户的身份或有效负载），并让信息配置文件 $ν(t)=I(S;X_t\mid X_{<t})$ 记录第 $t$ 个令牌在给定先前令牌的情况下揭示了多少关于 $S$ 的内容。它的总质量用于支付归因和提取；如何传播质量来支付本地化费用；单独的检测不是通过信息来支付的，而是通过存在来支付的，即从标记分布到未标记分布的距离。
- Abstract: A watermark in a generative model's output is usually asked only whether a text is machine-made. The same mark can do more: attribute it to the user who produced it, extract a hidden payload, or localize the part that survives editing. These form a forensic ladder, and we ask what each rung costs in the sample length $n$. One object organizes the answers. Let $S$ be the secret the mark carries (a user's identity or...
- Summary (fallback): 机器翻译摘要显示：生成模型输出中的水印通常仅询问文本是否是机器制作的。相同的标记可以做更多的事情：将其归因于生成它的用户，提取隐藏的有效负载，或者本地化编辑后幸存的部分。这些形成了一个取证阶梯，我们询问样本长度 $n$ 中每个梯级的成本是多少。一个对象组织答案。令 $S$ 为标记携带的秘密（用户的身份或有效负载），并让信息配置文件 $ν(t)=I(S;X_t\mid X_{<t})$ 记录第 $t$ 个令牌在给定先前令牌的情况下揭示了多少关于 $S$ 的内容。它的总质量用于支付归因和提取；如何传播质量来支付本地化费用；单独的检测不是通过信息来支付的，而是通过存在来支付的，即从标记分布到未标记分布的距离。
- Keywords: text, mark, user, payload, costs

### 7. [在治疗因素之间是否存在合理的统计相互作用的析因临床试验。方法论文献的历史回顾](https://arxiv.org/abs/2607.12991v1)
- Original title: Factorial clinical trials in the presence and absence of plausible statistical interactions between treatment factors. A historical review of the methodological literature
- Authors: Rebecca E. A. Walwyn, Pritaporn Kingkaew, Alan A. Montgomery, Alexandra Wright-Hughes, Steven G. Gilmour
- Meta: 2026-07-14 | stat.ME
- 中文摘要: 当两个或多个治疗因素之间的统计相互作用无法预期时，以及当预期存在统计相互作用时，都可以进行析因试验。如果没有交互作用，k-in-1 析因试验用与一次平行组试验相同的单元数回答 k 个单因素问题。有关 k-in-1 析因试验的文献主导了英国试验者对析因试验的理解。然而，析因实验起源于实验设计领域，可以稳健地估计相互作用。这些文献中看似相互矛盾的指导给试验者带来了困惑和误解。我们将这些文献放在一起，以澄清用于推荐在存在和不存在相互作用的情况下使用析因试验的论点。我们概述了激励人心的例子。
- Abstract: Factorial trials can be conducted when statistical interactions between two or more treatment factors are not anticipated, but also when they are. A k-in-1 factorial trial answers k single-factor questions with the same number of units as one parallel-group trial if there are no interactions. Literature on k-in-1 factorial trials has dominated trialists understanding of factorial trials in the UK. However, factorial...
- Summary (fallback): 机器翻译摘要显示：当两个或多个治疗因素之间的统计相互作用无法预期时，以及当预期存在统计相互作用时，都可以进行析因试验。如果没有交互作用，k-in-1 析因试验用与一次平行组试验相同的单元数回答 k 个单因素问题。有关 k-in-1 析因试验的文献主导了英国试验者对析因试验的理解。然而，析因实验起源于实验设计领域，可以稳健地估计相互作用。这些文献中看似相互矛盾的指导给试验者带来了困惑和误解。我们将这些文献放在一起，以澄清用于推荐在存在和不存在相互作用的情况下使用析因试验的论点。我们概述了激励人心的例子。
- Keywords: factorial, trials, interactions, treatment, trialists

### 8. [用于隐式数据同化的集成控制流过滤](https://arxiv.org/abs/2607.12975v1)
- Original title: Ensemble Controlled-Flow Filtering for Implicit Data Assimilation
- Authors: Zhuoyuan Li, Yue Zhao, Ming Li
- Meta: 2026-07-14 | stat.ML
- 中文摘要: 数据同化根据模型预测和传入观测来估计动力系统的状态。然而，许多观察机制是多对一的、隐式的、非平滑的或只能通过模拟访问的，并且不需要提供现有集合滤波器所需的残差结构或似然指导。我们引入隐式数据同化，其中分析定律被定义为预测分布的能量倾斜。然后，我们提出了集成控制流滤波器（EnCF），它通过随机控制流实现这种更新，并通过终端能量梯度的伴随匹配来学习依赖于观察的控制。对于模拟器定义的观测，EnCF-LF 从样本中学习替代条件能量并应用相同的受控流求解器。
- Abstract: Data assimilation estimates the state of a dynamical system from model forecasts and incoming observations. Many observation mechanisms, however, are many-to-one, implicit, non-smooth, or accessible only through simulation, and need not provide the residual structures or likelihood guidance required by existing ensemble filters. We introduce implicit data assimilation, in which the analysis law is defined as an ener...
- Summary (fallback): 机器翻译摘要显示：数据同化根据模型预测和传入观测来估计动力系统的状态。然而，许多观察机制是多对一的、隐式的、非平滑的或只能通过模拟访问的，并且不需要提供现有集合滤波器所需的残差结构或似然指导。我们引入隐式数据同化，其中分析定律被定义为预测分布的能量倾斜。然后，我们提出了集成控制流滤波器（EnCF），它通过随机控制流实现这种更新，并通过终端能量梯度的伴随匹配来学习依赖于观察的控制。对于模拟器定义的观测，EnCF-LF 从样本中学习替代条件能量并应用相同的受控流求解器。
- Keywords: implicit, ensemble, controlled-flow, assimilation, observations

### 9. [形式，而非内容？通过冻结小代码模型中的提示和权重对学习错误条件自我修复进行预注册、安慰剂控制的评估](https://arxiv.org/abs/2607.12962v1)
- Original title: Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models
- Authors: Mehmet Iscan
- Meta: 2026-07-14 | cs.SE
- 中文摘要: 冻结的小代码 LLM 是在本地部署的，但在自我修复文献中，在没有安慰剂对照的情况下，仍然可以测量在尝试失败后指导重试的信息。我们将失败的程序视为猜想，将执行反例视为与预言机相关的反驳，并引入 PoPE（波普尔安慰剂控制评估）：一种用于衡量伪造 LLM 生成代码的证据是否可以由同一模型操作使用的方法。在 PoPE 中，错误内容与特定通道的安慰剂配对，这些安慰剂保留预先声明的支架，同时消除任务相关内容或打乱任务错误分配。冻结的小代码模型（0.5-1.5B）通过提示通道和权重通道（小数据适配器训练）根据预先注册的规则进行评估，每个臂单元对有四代。
- Abstract: Frozen small code LLMs are deployed locally, yet the information guiding a retry after a failed attempt is still measured without placebo controls in the self-repair literature. We treat a failed program as a conjecture and an execution counterexample as an oracle-relative refutation, and introduce PoPE (Popperian Placebo-controlled Evaluation): a methodology for measuring whether evidence that falsifies LLM-generat...
- Summary (fallback): 机器翻译摘要显示：冻结的小代码 LLM 是在本地部署的，但在自我修复文献中，在没有安慰剂对照的情况下，仍然可以测量在尝试失败后指导重试的信息。我们将失败的程序视为猜想，将执行反例视为与预言机相关的反驳，并引入 PoPE（波普尔安慰剂控制评估）：一种用于衡量伪造 LLM 生成代码的证据是否可以由同一模型操作使用的方法。在 PoPE 中，错误内容与特定通道的安慰剂配对，这些安慰剂保留预先声明的支架，同时消除任务相关内容或打乱任务错误分配。冻结的小代码模型（0.5-1.5B）通过提示通道和权重通道（小数据适配器训练）根据预先注册的规则进行评估，每个臂单元对有四代。
- Keywords: code, channel, content, placebo-controlled, frozen

### 10. [NWP 预测误差下光伏发电预测深度学习模型的稳健性：时空和物理可解释的分析](https://arxiv.org/abs/2607.12954v1)
- Original title: Robustness of Deep Learning Models for PV Power Forecasting under NWP Forecast Errors: A Spatiotemporal and Physically Interpretable Analysis
- Authors: Dandan Chen, Yan Zhao, Xuepeng Chen
- Meta: 2026-07-14 | physics.ao-ph
- 中文摘要: 人工智能预测模型的工程应用不仅需要较高的名义精度，还需要在不确定输入下的可预测行为。在光伏 (PV) 预报中，这一要求尤其具有挑战性，因为数值天气预报 (NWP) 误差具有时间相关性、状态依赖性以及跨变量的物理耦合性。然而，现有的评估通常依赖于完美的预测假设或不反映这些特征的简单扰动。本研究提出了一种基于仿真的物理约束鲁棒性评估框架，使用虚拟光伏发电作为受控响应变量，以将输入不确定性的传播与电站级别的混杂因素隔离开来。
- Abstract: Engineering use of AI forecasting models requires not only high nominal accuracy but also predictable behavior under uncertain inputs. In photovoltaic (PV) forecasting, this requirement is especially challenging because numerical weather prediction (NWP) errors are temporally correlated, state dependent, and physically coupled across variables. Existing evaluations, however, often rely on perfect forecast assumption...
- Summary (fallback): 机器翻译摘要显示：人工智能预测模型的工程应用不仅需要较高的名义精度，还需要在不确定输入下的可预测行为。在光伏 (PV) 预报中，这一要求尤其具有挑战性，因为数值天气预报 (NWP) 误差具有时间相关性、状态依赖性以及跨变量的物理耦合性。然而，现有的评估通常依赖于完美的预测假设或不反映这些特征的简单扰动。本研究提出了一种基于仿真的物理约束鲁棒性评估框架，使用虚拟光伏发电作为受控响应变量，以将输入不确定性的传播与电站级别的混杂因素隔离开来。
- Keywords: under, robustness, models, forecasting, forecast

### 11. [电池异质性和筛选不确定性下再利用锂离子电池组的优化组装](https://arxiv.org/abs/2607.12951v1)
- Original title: Optimal Assembly of Repurposed Lithium-Ion Battery Packs under Cell Heterogeneity and Screening Uncertainty
- Authors: Hassan Zahid Butt, Xingpeng Li
- Meta: 2026-07-14 | eess.SY
- 中文摘要: 退役电动汽车电池供应的不断增长为二次使用固定式储能提供了机会，但由于容量、直流内阻 (DCIR) 和自放电的巨大变化，将异构退役电池组装成可靠的电池组具有挑战性。本文提出了一种用于二次电池的电池到电池组组装的稳健优化框架。拓扑筛选阶段首先确定满足逆变器和能量要求的最小单元串并联配置，从而减少后续分配问题的维数。对于每个候选拓扑，混合整数线性程序选择电池并沿串联串分配它们，将功率、电压和能量要求作为硬约束，同时最小化 DCIR 分布、容量分布和自放电不平衡的归一化加权和。
- Abstract: The growing supply of retired electric vehicle batteries presents an opportunity for second-life stationary energy storage, but assembling heterogeneous retired cells into reliable packs is challenging due to substantial variation in capacity, DC internal resistance (DCIR), and self-discharge. This paper proposes a robust optimization framework for cell-to-pack assembly of second-life batteries. A topology-screening...
- Summary (fallback): 机器翻译摘要显示：退役电动汽车电池供应的不断增长为二次使用固定式储能提供了机会，但由于容量、直流内阻 (DCIR) 和自放电的巨大变化，将异构退役电池组装成可靠的电池组具有挑战性。本文提出了一种用于二次电池的电池到电池组组装的稳健优化框架。拓扑筛选阶段首先确定满足逆变器和能量要求的最小单元串并联配置，从而减少后续分配问题的维数。对于每个候选拓扑，混合整数线性程序选择电池并沿串联串分配它们，将功率、电压和能量要求作为硬约束，同时最小化 DCIR 分布、容量分布和自放电不平衡的归一化加权和。
- Keywords: requirements, assembly, under, uncertainty, second-life

### 12. [一维无导数随机凸优化的 Sharp 优化算法](https://arxiv.org/abs/2607.12938v1)
- Original title: Sharp Optimal Algorithm for Derivative-Free Stochastic Convex Optimization in One Dimension
- Authors: Alexandra Carpentier, Chloé Rouyer, Alexandre Tsybakov, Arya Akhavan
- Meta: 2026-07-14 | math.OC
- 中文摘要: 随机凸优化是一个经典问题，在一阶反馈下具有易于理解的保证。相反，对于带有噪声函数评估的零阶优化，即使在一维情况下，已知上限和 $Ω(1/\sqrt{T})$ 下限之间仍然存在对数间隙。在这项工作中，我们研究使用具有亚高斯噪声的零阶预言机最小化凸函数 $f : [0,1] \to [0,1]$ 的问题。我们提出了一种计算高效的算法，可实现最佳 $O(1/\sqrt{T})$ 收敛速度，与下限相匹配。结果缩小了一个维度上的现有差距，在这种情况下提供了第一个大幅利率保证。
- Abstract: Stochastic convex optimization is a classical problem with well-understood guarantees under first-order feedback. In contrast, for zero-order optimization with noisy function evaluations, a logarithmic gap has persisted between known upper bounds and the $Ω(1/\sqrt{T})$ lower bound, even in the one-dimensional case. In this work, we study the problem of minimizing a convex function $f : [0,1] \to [0,1]$ using a zero...
- Summary (fallback): 机器翻译摘要显示：随机凸优化是一个经典问题，在一阶反馈下具有易于理解的保证。相反，对于带有噪声函数评估的零阶优化，即使在一维情况下，已知上限和 $Ω(1/\sqrt{T})$ 下限之间仍然存在对数间隙。在这项工作中，我们研究使用具有亚高斯噪声的零阶预言机最小化凸函数 $f : [0,1] \to [0,1]$ 的问题。我们提出了一种计算高效的算法，可实现最佳 $O(1/\sqrt{T})$ 收敛速度，与下限相匹配。结果缩小了一个维度上的现有差距，在这种情况下提供了第一个大幅利率保证。
- Keywords: convex, optimization, sharp, optimal, algorithm

### 13. [用于数字乳腺断层合成的精确且校准的扩散重建](https://arxiv.org/abs/2607.12937v1)
- Original title: Exact and Calibrated Diffusion Reconstruction for Digital Breast Tomosynthesis
- Authors: Imade Bouftini
- Meta: 2026-07-14 | eess.IV
- 中文摘要: 有限角度数字乳腺断层合成 (DBT) 通过窄弧上的一些低剂量投影重建体积。在具有代表性的九视图 $25^{\circ}$ 协议中，超过 98% 的图像空间是未测量的，因此学习到的先验必须提供缺失楔形中的结构。条件扩散先验在这里实现了很强的感知质量，但留下了三个临床障碍：不精确的数据一致性、非局部幻觉和未校准的不确定性。我们通过将条件扩散采样器的每步近端更新替换为数据一致集上的精确欧几里得投影来精确地执行测量，该投影是通过具有一次性 Gram 矩阵 $AA^{\top}$ 分解的 $m$ 维对偶系统计算的。此投影每步花费 4.5 毫秒（加速 $248\times$），并将数据残差驱动到双精度下限 ($2.4\times10^{-13}$)。
- Abstract: Limited-angle digital breast tomosynthesis (DBT) reconstructs a volume from a few low-dose projections over a narrow arc. At a representative nine-view, $25^{\circ}$ protocol more than 98% of image space is unmeasured, so a learned prior must supply structure in the missing wedge. Conditional diffusion priors achieve strong perceptual quality here but leave three clinical obstacles: inexact data consistency, unlocal...
- Summary (fallback): 机器翻译摘要显示：有限角度数字乳腺断层合成 (DBT) 通过窄弧上的一些低剂量投影重建体积。在具有代表性的九视图 $25^{\circ}$ 协议中，超过 98% 的图像空间是未测量的，因此学习到的先验必须提供缺失楔形中的结构。条件扩散先验在这里实现了很强的感知质量，但留下了三个临床障碍：不精确的数据一致性、非局部幻觉和未校准的不确定性。我们通过将条件扩散采样器的每步近端更新替换为数据一致集上的精确欧几里得投影来精确地执行测量，该投影是通过具有一次性 Gram 矩阵 $AA^{\top}$ 分解的 $m$ 维对偶系统计算的。此投影每步花费 4.5 毫秒（加速 $248\times$），并将数据残差驱动到双精度下限 ($2.4\times10^{-13}$)。
- Keywords: step, error, diffusion, breast, proximal

### 14. [迭代活动图的最佳光刺激选择](https://arxiv.org/abs/2607.12930v1)
- Original title: Optimal photostimulation selection for iterative activity maps
- Authors: Jacob J. Morra, Kaitlyn E. Fouke, Owen Traubert, Eva A. Naumann
- Meta: 2026-07-14 | q-bio.NC
- 中文摘要: 全光学双光子全息光遗传学通过在对群体活动进行成像的同时刺激特定的神经元或神经元群来实现因果电路映射。然而，由于组合复杂性、组织加热、光损伤和实验时间，详尽的连接映射在实验上仍然令人望而却步。我们提出了 OPhELIA（迭代活动图的最佳光刺激选择），这是一个贝叶斯框架，用于在有限的试验预算下选择信息扰动。 OPhELIA 将 Beta-Bernoulli 连接推理与基于模糊性的获取启发式方法以及从刺激前神经活动中获得的学习先验相结合，增强了主动学习和压缩感知。在独立模拟和体内斑马鱼幼虫视觉运动实验中，具有主动学习功能的 OPhELIA 提高了详尽功能连接组的试验效率近似。
- Abstract: All-optical two-photon holographic optogenetics enables causal circuit mapping by stimulating defined neurons or ensembles while imaging population activity. Yet exhaustive connectivity mapping remains experimentally prohibitive because of combinatorial complexity, tissue heating, photodamage, and experimental time. We present OPhELIA (Optimal Photostimulation sElection for Iterative Activity maps), a Bayesian frame...
- Summary (fallback): 机器翻译摘要显示：全光学双光子全息光遗传学通过在对群体活动进行成像的同时刺激特定的神经元或神经元群来实现因果电路映射。然而，由于组合复杂性、组织加热、光损伤和实验时间，详尽的连接映射在实验上仍然令人望而却步。我们提出了 OPhELIA（迭代活动图的最佳光刺激选择），这是一个贝叶斯框架，用于在有限的试验预算下选择信息扰动。 OPhELIA 将 Beta-Bernoulli 连接推理与基于模糊性的获取启发式方法以及从刺激前神经活动中获得的学习先验相结合，增强了主动学习和压缩感知。在独立模拟和体内斑马鱼幼虫视觉运动实验中，具有主动学习功能的 OPhELIA 提高了详尽功能连接组的试验效率近似。
- Keywords: ophelia, activity, exhaustive, optimal, photostimulation

### 15. [有效的顺序校准，误差范围为 $O(T^{2/3-ε})$](https://arxiv.org/abs/2607.12928v1)
- Original title: Efficient Sequential Calibration with $O(T^{2/3-ε})$ Error Bound
- Authors: Zihan Zhang
- Meta: 2026-07-14 | cs.LG
- 中文摘要: 我们研究在线二进制顺序校准问题。 \citet{dagan2024writing} 最近的突破克服了经典的 \(T^{2/3}\) 校准误差障碍。在此结果的基础上，我们提出了一种有效的随机预测器，对于某些常数 \(\varepsilon>0\) ，它实现了预期的校准误差 \(O(T^{2/3-\varepsilon})\)。我们的预测器将 \textsc{SPR-Calibration} 程序 \citep{dagan2024writing} 与外部 Blackwell 式校正层结合起来。 \textsc{SPR-Calibration} 过程控制相对于条件均值估计的代理序列的校准，而校正层控制当这些代理用于近似真实结果时产生的额外误差。
- Abstract: We study the online binary sequential calibration problem. A recent breakthrough by \citet{dagan2024breaking} overcomes the classical \(T^{2/3}\) barrier for calibration error. Building on this result, we present an efficient randomized forecaster that achieves an expected calibration error \(O(T^{2/3-\varepsilon})\) for some constant \(\varepsilon>0\). Our forecaster combines the \textsc{SPR-Calibration} procedure...
- Summary (fallback): 机器翻译摘要显示：我们研究在线二进制顺序校准问题。 \citet{dagan2024writing} 最近的突破克服了经典的 \(T^{2/3}\) 校准误差障碍。在此结果的基础上，我们提出了一种有效的随机预测器，对于某些常数 \(\varepsilon>0\) ，它实现了预期的校准误差 \(O(T^{2/3-\varepsilon})\)。我们的预测器将 \textsc{SPR-Calibration} 程序 \citep{dagan2024writing} 与外部 Blackwell 式校正层结合起来。 \textsc{SPR-Calibration} 过程控制相对于条件均值估计的代理序列的校准，而校正层控制当这些代理用于近似真实结果时产生的额外误差。
- Keywords: calibration, error, textsc, spr-calibration, dagan2024breaking

### 16. [LatentFlow：调节随机过程的通用框架](https://arxiv.org/abs/2607.12922v1)
- Original title: LatentFlow: A General Framework for Conditioning Stochastic Processes
- Authors: Louis Sharrock, Lachlan Astfalck, Henry Moss
- Meta: 2026-07-14 | stat.ML
- 中文摘要: 一般来说，随机过程模型的模拟比条件要容易得多。非线性观测、非高斯似然、黑盒信息和全局约束都会引发棘手的条件定律，需要定制的、特定于模型的构造。我们引入 LatentFlow，这是一个用于调节随机过程的单一框架，无需学习神经近似，也无需训练。我们的出发点是将随机过程写为易于处理的潜在创新的确定性图像，$f_0 = T_{\vartheta}(xi_0)$，其中$xi_0$从简单的参考分布中采样。这将过程级调节减少为潜在空间推理：通过 $T_{\vartheta}$ 将似然性拉回，用易于处理的引导概率流对生成的潜在规律进行采样，然后向前推动样本。
- Abstract: Stochastic-process models are, as a rule, far easier to simulate than to condition. Non-linear observations, non-Gaussian likelihoods, black-box information, and global constraints all induce intractable conditional laws, requiring bespoke, model-specific constructions. We introduce LatentFlow, a single framework for conditioning stochastic processes, with no learned neural approximations and no training. Our starti...
- Summary (fallback): 机器翻译摘要显示：一般来说，随机过程模型的模拟比条件要容易得多。非线性观测、非高斯似然、黑盒信息和全局约束都会引发棘手的条件定律，需要定制的、特定于模型的构造。我们引入 LatentFlow，这是一个用于调节随机过程的单一框架，无需学习神经近似，也无需训练。我们的出发点是将随机过程写为易于处理的潜在创新的确定性图像，$f_0 = T_{\vartheta}(xi_0)$，其中$xi_0$从简单的参考分布中采样。这将过程级调节减少为潜在空间推理：通过 $T_{\vartheta}$ 将似然性拉回，用易于处理的引导概率流对生成的潜在规律进行采样，然后向前推动样本。
- Keywords: stochastic, conditioning, processes, latentflow, single

### 17. [论系统发育网络的树网络可区分性和完全可识别性](https://arxiv.org/abs/2607.12919v1)
- Original title: On Tree-Network Distinguishability and Full Identifiability of Phylogenetic Networks
- Authors: Jari Brits, Niels Holtgrefe, Leo van Iersel, Samuel Martin
- Meta: 2026-07-14 | q-bio.PE
- 中文摘要: 系统发育网络将系统发育树概括为进化历史，其中包括重组、水平基因转移和杂交等网状事件。在核苷酸取代的马尔可夫模型下，系统发育网络决定叶模式的分布。在这里，我们研究 Jukes-Cantor (JC)、Kimura 2 参数 (K2P) 和 Kimura 3 参数 (K3P) 模型下该分布的网络拓扑的可识别性。我们的第一个结果是，1 级系统发生网络（模重定向三角形）的半定向网络参数在所有三个模型下，在生物学上合理的参数空间上是完全可识别的，其中替代率是概率性的，并且混合参数是非平凡的（即不是 0 或 1）。
- Abstract: Phylogenetic networks generalize phylogenetic trees to evolutionary histories that include reticulate events such as recombination, horizontal gene transfer, and hybridization. Under a Markov model of nucleotide substitution, a phylogenetic network determines a distribution of leaf-patterns. Here, we study the identifiability of the network topology from this distribution under the Jukes-Cantor (JC), Kimura 2-parame...
- Summary (fallback): 机器翻译摘要显示：系统发育网络将系统发育树概括为进化历史，其中包括重组、水平基因转移和杂交等网状事件。在核苷酸取代的马尔可夫模型下，系统发育网络决定叶模式的分布。在这里，我们研究 Jukes-Cantor (JC)、Kimura 2 参数 (K2P) 和 Kimura 3 参数 (K3P) 模型下该分布的网络拓扑的可识别性。我们的第一个结果是，1 级系统发生网络（模重定向三角形）的半定向网络参数在所有三个模型下，在生物学上合理的参数空间上是完全可识别的，其中替代率是概率性的，并且混合参数是非平凡的（即不是 0 或 1）。
- Keywords: phylogenetic, network, parameter, identifiability, under

### 18. [用于灵活且几何最佳嵌入和更快收敛的对比折叠损失](https://arxiv.org/abs/2607.12916v1)
- Original title: Contrastive-Collapsed Loss for Flexible and Geometrically Optimal Embeddings and Faster Convergence
- Authors: Blanca Cano-Camarero, Ángela Fernández-Pascual, José R. Dorronsoro
- Meta: 2026-07-14 | cs.LG
- 中文摘要: 在这项工作中，我们引入了 CoCo，一种旨在学习标准化和结构良好的表示的损失函数。所提出的损失鼓励类内崩溃和类间对比，同时为神经网络保留足够的灵活性，以在类之间具有大角距的情况下近似几何最佳嵌入。我们提供了关于点回归和交叉熵等相关目标定位 CoCo 的理论分析，表明新提出的损失受益于更接近最优配置的初始化、更多信息梯度以及对类表示崩溃的更强激励。
- Abstract: In this work, we introduce CoCo, a loss function aimed at learning normalized and well-structured representations. The proposed loss encourages intra-class collapse and inter-class contrast while preserving sufficient flexibility for neural networks to approximate geometrically optimal embeddings with large angular separation between classes. We provide a theoretical analysis positioning CoCo with respect to related...
- Summary (fallback): 机器翻译摘要显示：在这项工作中，我们引入了 CoCo，一种旨在学习标准化和结构良好的表示的损失函数。所提出的损失鼓励类内崩溃和类间对比，同时为神经网络保留足够的灵活性，以在类之间具有大角距的情况下近似几何最佳嵌入。我们提供了关于点回归和交叉熵等相关目标定位 CoCo 的理论分析，表明新提出的损失受益于更接近最优配置的初始化、更多信息梯度以及对类表示崩溃的更强激励。
- Keywords: loss, coco, optimal, geometrically, embeddings

### 19. [Open-KNEAD：通过代理分解进行基于知识的营养估算](https://arxiv.org/abs/2607.12911v1)
- Original title: Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition
- Authors: Bruce Coburn, Jingbo Yue, Jinge Ma, Siddeshwar Raghavan, Gautham Vinod et al.
- Meta: 2026-07-14 | cs.CV
- 中文摘要: 多模态大语言模型（MLLM）越来越多地用于根据膳食图像进行饮食评估，其中检索增强基础被证明可以提高营养估计。然而，我们发现这个前提对于当前的 MLLM 来说不再成立。现代 MLLM 的直接估计现在可以匹配或超过完整的检索流程。这就提出了一个问题：如果检索不再改善总体估计，它是否仍然可以提供临床医生重视的两件事：准确的部分和可追溯的逐项记录？我们在追求这一目标的同时保留了对临床采用重要的内容：最小的用户负担（单个、未注释的膳食图像）、可解释性（可审计的记录）和隐私（本地托管的推理）。我们推出了 Open-KNEAD，这是一种基于知识的膳食营养估计代理框架，无需培训且可在本地部署。
- Abstract: Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates. However, we find this premise no longer holds for current MLLMs. A modern MLLM's direct estimate now matches or surpasses the full retrieval pipeline. This raises a question: if retrieval no longer improves the overall estimate, can it s...
- Summary (fallback): 机器翻译摘要显示：多模态大语言模型（MLLM）越来越多地用于根据膳食图像进行饮食评估，其中检索增强基础被证明可以提高营养估计。然而，我们发现这个前提对于当前的 MLLM 来说不再成立。现代 MLLM 的直接估计现在可以匹配或超过完整的检索流程。这就提出了一个问题：如果检索不再改善总体估计，它是否仍然可以提供临床医生重视的两件事：准确的部分和可追溯的逐项记录？我们在追求这一目标的同时保留了对临床采用重要的内容：最小的用户负担（单个、未注释的膳食图像）、可解释性（可审计的记录）和隐私（本地托管的推理）。我们推出了 Open-KNEAD，这是一种基于知识的膳食营养估计代理框架，无需培训且可在本地部署。
- Keywords: open-knead, meal, estimates, nutrition, estimation

### 20. [低功耗边缘平台基于视觉的实时跌倒检测](https://arxiv.org/abs/2607.12909v1)
- Original title: Real-time fall detection based on vision for low-power edge platforms
- Authors: Wenjun Xia, Zhicheng Peng, Haopeng Li, Zhengdi Zhang
- Meta: 2026-07-14 | q-bio.NC
- 中文摘要: 跌倒检测对于养老、智能监控至关重要；然而，流行的基于视觉的方法主要将其框架为静态姿势分类或离散时间模式匹配，从根本上忽视了人类支持系统的不稳定性动态。本文提出了一种基于物理的跌倒检测框架，该框架将跌倒重新定义为耦合动态系统中的稳定性损失事件。我们引入了一种新颖的双 LTC 架构，包括质心 (CoM) 子系统和支撑基 (BoS) 子系统，两者都实例化为液体时间常数 (LTC) 神经网络，通过自适应时间常数连续模拟惯性轨迹演化和地面接触调整、下落运动的物理可解释性。
- Abstract: Falling detection is vital for elderly care and intelligent surveillance; however, prevailing vision-based approaches predominantly frame it as static pose classification or discrete temporal pattern matching, fundamentally overlooking the instability dynamics of the human support system. This paper proposes a physics-informed falling detection framework that recasts falling as a stability-loss event in a coupled dy...
- Summary (fallback): 机器翻译摘要显示：跌倒检测对于养老、智能监控至关重要；然而，流行的基于视觉的方法主要将其框架为静态姿势分类或离散时间模式匹配，从根本上忽视了人类支持系统的不稳定性动态。本文提出了一种基于物理的跌倒检测框架，该框架将跌倒重新定义为耦合动态系统中的稳定性损失事件。我们引入了一种新颖的双 LTC 架构，包括质心 (CoM) 子系统和支撑基 (BoS) 子系统，两者都实例化为液体时间常数 (LTC) 神经网络，通过自适应时间常数连续模拟惯性轨迹演化和地面接触调整、下落运动的物理可解释性。
- Keywords: falling, detection, physical, stability, real-time

### 21. [随机哈密顿量蒙特卡罗的加速混合时间](https://arxiv.org/abs/2607.12902v1)
- Original title: Accelerated Mixing Time of Randomized Hamiltonian Monte Carlo
- Authors: Siddharth Mitra, Vishwak Srinivasan, Xiuyuan Wang, Andre Wibisono
- Meta: 2026-07-14 | stat.ML
- 中文摘要: 我们展示了随机哈密顿蒙特卡罗 (RHMC) 算法为从对数凹概率分布中采样提供了加速混合时间保证。 RHMC 通过重复模拟一些随机积分时间的连续时间哈密顿动力学，并在每次模拟之间将速度重置为独立的高斯随机变量来进行。我们证明，当目标分布为对数凹且满足 $α$-Talagrand 不等式时（例如，如果目标分布为 $α$-强对数凹），如果我们使用平均值为 $θ(α^{-1/2})$ 的三角分布或指数分布的随机积分时间，则 RHMC 在 KL 散度中以指数方式快速收敛，并且在 KL 散度中达到误差 $\varepsilon$ 的总积分时间缩放为 $O(α^{-1/2} \log(\varepsilon^{-1}))$。
- Abstract: We show the Randomized Hamiltonian Monte Carlo (RHMC) algorithm has accelerated mixing time guarantees for sampling from log-concave probability distributions. RHMC proceeds by repeatedly simulating the continuous-time Hamiltonian dynamics for some random integration times, and resetting the velocity to be an independent Gaussian random variable between each simulation. We show that when the target distribution is l...
- Summary (fallback): 机器翻译摘要显示：我们展示了随机哈密顿蒙特卡罗 (RHMC) 算法为从对数凹概率分布中采样提供了加速混合时间保证。 RHMC 通过重复模拟一些随机积分时间的连续时间哈密顿动力学，并在每次模拟之间将速度重置为独立的高斯随机变量来进行。我们证明，当目标分布为对数凹且满足 $α$-Talagrand 不等式时（例如，如果目标分布为 $α$-强对数凹），如果我们使用平均值为 $θ(α^{-1/2})$ 的三角分布或指数分布的随机积分时间，则 RHMC 在 KL 散度中以指数方式快速收敛，并且在 KL 散度中达到误差 $\varepsilon$ 的总积分时间缩放为 $O(α^{-1/2} \log(\varepsilon^{-1}))$。
- Keywords: time, hamiltonian, integration, distribution, log-concave

### 22. [UniMedSeg：多范式 2D/3D 医学图像分割的统一上下文学习](https://arxiv.org/abs/2607.12896v1)
- Original title: UniMedSeg: Unified In-Context Learning for Multi-Paradigm 2D/3D Medical Image Segmentation
- Authors: Yunzhou Li, Jiesi Hu, Yanwu Yang, Hanyang Peng, Chenfei Ye et al.
- Meta: 2026-07-14 | cs.CV
- 中文摘要: 医学图像分割基础模型有望在不同的临床场景中推广，但现有的通用方法仍然因即时范式和空间维度而支离破碎。视觉上下文学习、交互式分割和语言引导分割通常由特定范例模型处理，而 2D 和 3D 图像也分别建模。这种隔离防止异构注释和数据被单个可扩展模型共同吸收，并限制跨范式知识转移。
- Abstract: Medical image segmentation foundation models are expected to generalize across diverse clinical scenarios, yet existing universal methods remain fragmented by prompt paradigms and spatial dimensions. Visual in-context learning, interactive segmentation, and language-guided segmentation are typically handled by paradigm-specific models, while 2D and 3D images are also modeled separately. Such isolation prevents heter...
- Summary (fallback): 机器翻译摘要显示：医学图像分割基础模型有望在不同的临床场景中推广，但现有的通用方法仍然因即时范式和空间维度而支离破碎。视觉上下文学习、交互式分割和语言引导分割通常由特定范例模型处理，而 2D 和 3D 图像也分别建模。这种隔离防止异构注释和数据被单个可扩展模型共同吸收，并限制跨范式知识转移。
- Keywords: segmentation, unimedseg, in-context, visual, medical

### 23. [基于能量的物理通知的簇张拉整体结构找形](https://arxiv.org/abs/2607.12888v1)
- Original title: Energy-Based Physics-Informed Form Finding for Clustered Tensegrity Structures
- Authors: Jing Qin, Muhao Chen
- Meta: 2026-07-14 | cs.LG
- 中文摘要: 张拉整体找形和物理性质预测是结构力学中的基本反问题，旨在确定平衡配置和内力分布。由于几何形状和力之间的耦合产生的强非线性、确保结构稳定性的需要以及边界条件和对称性等约束的强制执行，这些问题具有挑战性。此外，传统方法通常缺乏对噪声和异常值的鲁棒性。本文提出了一种基于能量的学习框架，用于集群张拉整体形状查找和物理属性预测。
- Abstract: Tensegrity form-finding and physical property prediction are fundamental inverse problems in structural mechanics, which aim to determine equilibrium configurations and internal force distributions. These problems are challenging due to strong nonlinearity arising from the coupling between geometry and forces, the need to ensure structural stability, and the enforcement of constraints such as boundary conditions and...
- Summary (fallback): 机器翻译摘要显示：张拉整体找形和物理性质预测是结构力学中的基本反问题，旨在确定平衡配置和内力分布。由于几何形状和力之间的耦合产生的强非线性、确保结构稳定性的需要以及边界条件和对称性等约束的强制执行，这些问题具有挑战性。此外，传统方法通常缺乏对噪声和异常值的鲁棒性。本文提出了一种基于能量的学习框架，用于集群张拉整体形状查找和物理属性预测。
- Keywords: physical, tensegrity, prediction, energy-based, form

### 24. [用于自主、免微调临床症状检测的多代理系统：开发和验证研究](https://arxiv.org/abs/2607.12886v1)
- Original title: A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study
- Authors: Cameron Cagan, Pedram Fard, Jiazi Tian, Jingya Cheng, Shawn N. Murphy et al.
- Meta: 2026-07-14 | cs.AI
- 中文摘要: 临床记录包含许多需要护理患者的体征和症状，但这些信息很少到达结构化领域。现有的提取方法要么依赖于产生误报的上下文不敏感规则，要么依赖于需要大量微调的监督模型。我们推出了 Pythia，这是一个多代理系统，可以自主编写和优化临床概念的提取提示，无需手动提示工程或微调。 Pythia 在本地托管的开放权重模型上运行，保留本地基础设施的临床记录，并使用开发集的敏感性和特异性来选择提示。我们将 Pythia 与包含来自代表 387 名患者的 400 份临床记录的 72 种体征和症状的精选词典进行了比较。每个概念的开发集 (n=300) 和验证集 (n=100) 独立划分。
- Abstract: Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensitive rules that generate false positives or on supervised models that require substantial fine-tuning. We present Pythia, a multi-agent system that autonomously writes and optimizes extraction prompts for clinical concep...
- Summary (fallback): 机器翻译摘要显示：临床记录包含许多需要护理患者的体征和症状，但这些信息很少到达结构化领域。现有的提取方法要么依赖于产生误报的上下文不敏感规则，要么依赖于需要大量微调的监督模型。我们推出了 Pythia，这是一个多代理系统，可以自主编写和优化临床概念的提取提示，无需手动提示工程或微调。 Pythia 在本地托管的开放权重模型上运行，保留本地基础设施的临床记录，并使用开发集的敏感性和特异性来选择提示。我们将 Pythia 与包含来自代表 387 名患者的 400 份临床记录的 72 种体征和症状的精选词典进行了比较。每个概念的开发集 (n=300) 和验证集 (n=100) 独立划分。
- Keywords: clinical, development, pythia, sensitivity, validation

### 25. [用于与 Agentic AI 兼容的深度学习的度量引导合成图像数据渲染](https://arxiv.org/abs/2607.12874v1)
- Original title: Metric-Guided Synthetic Image Data Rendering for Deep Learning compatible with Agentic AI
- Authors: Martina Radoynova, Samuel Pantze, Trina De, Ulrik Günther, Artur Yakimovich
- Meta: 2026-07-14 | cs.CV
- 中文摘要: 用于科学应用的深度学习计算机视觉需要以费力、昂贵且容易出错的过程收集和注释大型数据集。通过 3D 建模和渲染生成合成数据可以简化此过程，并通过以编程方式生成注释来提高注释的准确性。然而，在视觉上最小化真实图像和合成图像之间的域差距是主观的，并且缺乏系统的定量指导。我们推出 GraNatPy，一个 Python 包，其中包含指导渲染场景改进的指标。我们表明，渲染数据集的真实感、多样性和大小的可量化增加与场景视觉感知的改善和对象检测模型更高的零样本性能相关。
- Abstract: Deep learning computer vision for scientific applications requires collecting and annotating large datasets in a laborious, expensive and error-prone process. Synthetic data generation through 3D modelling and rendering may simplify this process and increase the accuracy of annotations by generating them programmatically. However, minimising the domain gap between real and synthetic images visually is subjective and...
- Summary (fallback): 机器翻译摘要显示：用于科学应用的深度学习计算机视觉需要以费力、昂贵且容易出错的过程收集和注释大型数据集。通过 3D 建模和渲染生成合成数据可以简化此过程，并通过以编程方式生成注释来提高注释的准确性。然而，在视觉上最小化真实图像和合成图像之间的域差距是主观的，并且缺乏系统的定量指导。我们推出 GraNatPy，一个 Python 包，其中包含指导渲染场景改进的指标。我们表明，渲染数据集的真实感、多样性和大小的可量化增加与场景视觉感知的改善和对象检测模型更高的零样本性能相关。
- Keywords: synthetic, rendering, deep, learning, agentic

### 26. [Deep4ge：用于故障检测和诊断的 DNN 训练轨迹](https://arxiv.org/abs/2607.12868v1)
- Original title: Deep4ge: DNN Training Trajectories for Fault Detection and Diagnosis
- Authors: Sigma Jahan
- Meta: 2026-07-14 | cs.SE
- 中文摘要: 深度学习系统经常会由于微妙的实施错误而导致训练行为的改变而失败。最近的工作研究了如何根据训练时期观察到的变化来检测和诊断此类故障。然而，软件工程社区仍然缺乏每个时期训练运行的公共数据集，其中包含记录的故障历史记录、特征提取详细信息以及对故障检测和诊断任务的明确重用支持。我们推出 Deep4ge，这是一个受控基准测试，包含 14,227 次训练运行，这些训练运行是从 Stack Overflow 收集的 59 个经过改编的 TensorFlow/Keras 深度神经网络 (DNN) 程序生成的。我们使用 27 个源代码转换生成了错误变体，这些转换引入了七个类别的已知错误。该数据集包含 9,845 次错误运行和 4,382 次正确基线运行。
- Abstract: Deep learning systems often fail due to subtle implementation faults that alter training behavior. Recent work has studied how to detect and diagnose such failures from changes observed across training epochs. However, the software engineering community still lacks a public dataset of per-epoch training runs with documented fault history, feature extraction details, and clear reuse support for fault detection and di...
- Summary (fallback): 机器翻译摘要显示：深度学习系统经常会由于微妙的实施错误而导致训练行为的改变而失败。最近的工作研究了如何根据训练时期观察到的变化来检测和诊断此类故障。然而，软件工程社区仍然缺乏每个时期训练运行的公共数据集，其中包含记录的故障历史记录、特征提取详细信息以及对故障检测和诊断任务的明确重用支持。我们推出 Deep4ge，这是一个受控基准测试，包含 14,227 次训练运行，这些训练运行是从 Stack Overflow 收集的 59 个经过改编的 TensorFlow/Keras 深度神经网络 (DNN) 程序生成的。我们使用 27 个源代码转换生成了错误变体，这些转换引入了七个类别的已知错误。该数据集包含 9,845 次错误运行和 4,382 次正确基线运行。
- Keywords: training, fault, runs, deep4ge, detection

### 27. [有害突变能否在确定性群体浪潮中冲浪？](https://arxiv.org/abs/2607.12864v1)
- Original title: Can deleterious mutations surf deterministic population waves?
- Authors: Joao Luiz de Oliveira Madeira, Marcel Ortgiese, Sarah Penington
- Meta: 2026-07-14 | math.AP
- 中文摘要: 在空间结构的种群中，罕见的中性突变可以在范围扩张过程中传播到大片区域，这种现象被称为基因冲浪。有害突变是否也能传播仍知之甚少。为了解决这个问题，我们研究了空间穆勒棘轮的确定性版本，由反应扩散方程的无限系统给出，描述了无性种群遭受突变、迁移和密度依赖性繁殖和死亡的影响。在确定偏微分方程系统适定后，我们分析了群体中有害突变的分布。在单稳态条件下，我们得出携带给定数量突变的个体密度与无突变个体密度之间比率的定量界限。
- Abstract: In spatially structured populations, rare neutral mutations can spread through large regions during a range expansion, a phenomenon known as gene surfing. Whether deleterious mutations can also surf remains poorly understood. To address this question, we study a deterministic version of the spatial Muller's ratchet, given by an infinite system of reaction-diffusion equations describing an asexual population subject...
- Summary (fallback): 机器翻译摘要显示：在空间结构的种群中，罕见的中性突变可以在范围扩张过程中传播到大片区域，这种现象被称为基因冲浪。有害突变是否也能传播仍知之甚少。为了解决这个问题，我们研究了空间穆勒棘轮的确定性版本，由反应扩散方程的无限系统给出，描述了无性种群遭受突变、迁移和密度依赖性繁殖和死亡的影响。在确定偏微分方程系统适定后，我们分析了群体中有害突变的分布。在单稳态条件下，我们得出携带给定数量突变的个体密度与无突变个体密度之间比率的定量界限。
- Keywords: mutations, deleterious, population, surf, deterministic

### 28. [变压器注意力头中的偏差定位和修复](https://arxiv.org/abs/2607.12863v1)
- Original title: Toward Localizing and Repairing Bias in Transformer Attention Heads
- Authors: Sigma Jahan
- Meta: 2026-07-14 | cs.SE
- 中文摘要: Transformer 语言模型越来越多地用作软件组件，但有偏差的输出仍然难以在模型内部进行本地化和修复。现有的公平性测试和修复方法主要在输入输出或再训练层面上运行，而最近的研究表明，与偏见相关的行为可以集中在一小部分注意力集中。本文研究是否可以通过有针对性的推理时间干预来定位和修复注意力头。我们引入了 ROBIN，一种白盒头级公平性调试方法，它使用对公平性探针的敏感性对注意力头进行排名，并从选定的头输出中删除一个小的偏差子空间。在一项四模型试点研究中，ROBIN 减少了所有模型中测得的 WinoBias 差距，同时比全头归零更好地保持了语言建模质量。
- Abstract: Transformer language models are increasingly used as software components, yet biased outputs remain difficult to localize and repair inside the model. Existing fairness testing and repair methods largely operate at the input-output or retraining level, while recent work suggests that bias-related behavior can concentrate in a small set of attention heads. This paper studies whether attention heads can be localized a...
- Summary (fallback): 机器翻译摘要显示：Transformer 语言模型越来越多地用作软件组件，但有偏差的输出仍然难以在模型内部进行本地化和修复。现有的公平性测试和修复方法主要在输入输出或再训练层面上运行，而最近的研究表明，与偏见相关的行为可以集中在一小部分注意力集中。本文研究是否可以通过有针对性的推理时间干预来定位和修复注意力头。我们引入了 ROBIN，一种白盒头级公平性调试方法，它使用对公平性探针的敏感性对注意力头进行排名，并从选定的头输出中删除一个小的偏差子空间。在一项四模型试点研究中，ROBIN 减少了所有模型中测得的 WinoBias 差距，同时比全头归零更好地保持了语言建模质量。
- Keywords: heads, attention, bias, repair, fairness

### 29. [基于验证器的热能存储控制推理模型强化微调](https://arxiv.org/abs/2607.12856v1)
- Original title: Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control
- Authors: Takumi Shioda, Kohei Terashima, Tatsuo Nagai
- Meta: 2026-07-14 | cs.LG
- 中文摘要: 建筑物预计会根据电网状况改变冷却负荷。热能存储（TES）可以实现这种转变，但要妥善安排它需要在存​​储限制下提前几个小时进行规划。模型预测控制 (MPC) 和强化学习很难跨建筑物扩展。相反，本研究通过具有可验​​证奖励的强化学习（RLVR）来采用开放权重推理模型。我们将精确的离线动态编程（DP）动作值转换为每个候选动作的密集奖励。仅使用 30 个训练提示，强化微调 (RFT) 将模型训练为上层调度程序，根据基于文本的状态和预测输出每小时的热泵设定点。评估使用特意简单的办公楼 TES 基准，其中精确的 DP 易于处理并且最佳值已知。
- Abstract: Buildings are expected to shift cooling loads in response to grid conditions. Thermal energy storage (TES) enables this shift, but scheduling it well requires planning hours ahead under storage constraints. Model predictive control (MPC) and reinforcement learning are difficult to scale across buildings. This study instead adapts an open-weight reasoning model through reinforcement learning with verifiable rewards (...
- Summary (fallback): 机器翻译摘要显示：建筑物预计会根据电网状况改变冷却负荷。热能存储（TES）可以实现这种转变，但要妥善安排它需要在存​​储限制下提前几个小时进行规划。模型预测控制 (MPC) 和强化学习很难跨建筑物扩展。相反，本研究通过具有可验​​证奖励的强化学习（RLVR）来采用开放权重推理模型。我们将精确的离线动态编程（DP）动作值转换为每个候选动作的密集奖励。仅使用 30 个训练提示，强化微调 (RFT) 将模型训练为上层调度程序，根据基于文本的状态和预测输出每小时的热泵设定点。评估使用特意简单的办公楼 TES 基准，其中精确的 DP 易于处理并且最佳值已知。
- Keywords: reinforcement, reasoning, storage, model, energy

### 30. [使用热驱动超顺磁体进行可重复储层计算：控制温度灵敏度](https://arxiv.org/abs/2607.12840v1)
- Original title: Reproducible Reservoir Computing with Thermally Driven Superparamagnets: Controlling Temperature Sensitivity
- Authors: Zhengfei Chen, Alex Welbourne, Matthew O. A. Ellis, Dan A. Allwood, Eleni Vasilaki et al.
- Meta: 2026-07-14 | cs.ET
- 中文摘要: 非常规计算系统必须在现实环境条件下表现出强大的性能，才能实现实际部署。我们最近提出了由应变感应磁电耦合驱动的超顺磁性纳米点系综作为超低能耗储层计算基板的令人兴奋的候选者。然而，由于它们的动态受热激活效应控制，这些系统本质上对环境温度波动敏感，导致在训练期间使用的温度范围之外运行时任务性能下降。在本文中，我们模拟了温度变化如何影响此类超顺磁系综的磁化动力学，并量化了这如何影响任务性能。
- Abstract: Unconventional computing systems must demonstrate robust performance under real-world environmental conditions to enable practical deployments. We have recently proposed superparamagnetic nanodot ensembles driven by strain-induced magnetoelectric coupling as exciting candidates for use as ultra-low energy consumption reservoir computing substrates. However, because their dynamics are governed by thermal activation e...
- Summary (fallback): 机器翻译摘要显示：非常规计算系统必须在现实环境条件下表现出强大的性能，才能实现实际部署。我们最近提出了由应变感应磁电耦合驱动的超顺磁性纳米点系综作为超低能耗储层计算基板的令人兴奋的候选者。然而，由于它们的动态受热激活效应控制，这些系统本质上对环境温度波动敏感，导致在训练期间使用的温度范围之外运行时任务性能下降。在本文中，我们模拟了温度变化如何影响此类超顺磁系综的磁化动力学，并量化了这如何影响任务性能。
- Keywords: performance, temperature, reservoir, computing, task

## biorxiv

### 1. [皮层下结构的偏侧性预测自发的大脑动力学](https://www.biorxiv.org/content/10.64898/2026.07.13.738145v1)
- Original title: Laterality of subcortical structures predicts spontaneous brain dynamics
- Authors: Ghafari, T., Quinn, A. J., Jensen, O.
- Meta: 2026-07-15 | neuroscience | DOI: 10.64898/2026.07.13.738145
- 中文摘要: 皮质下结构在通过分布式皮质-皮质下网络塑造皮质计算方面发挥着关键作用，但尚不清楚皮质下解剖结构的个体差异是否反映在静息态皮质振荡中。我们分析了剑桥衰老和神经科学中心 (CamCAN) 队列中 533 名健康成年人的静息态脑磁图 (MEG) 和结构 MRI，以测试皮层下体积的半球不对称是否预示着皮层振荡功率的不对称。计算皮质下体积和同源 MEG 传感器对的振荡功率的侧化指数。基于聚类的排列测试揭示了皮层下解剖结构和皮层活动之间的频率特异性关联。
- Abstract: Subcortical structures play a key role in shaping cortical computation through distributed cortico-subcortical networks, yet it remains unclear whether individual differences in subcortical anatomy are reflected in resting-state cortical oscillations. We analysed resting-state magnetoencephalography (MEG) and structural MRI from 533 healthy adults in the Cambridge Centre for Ageing and Neuroscience (CamCAN) cohort t...
- Summary (fallback): 机器翻译摘要显示：皮质下结构在通过分布式皮质-皮质下网络塑造皮质计算方面发挥着关键作用，但尚不清楚皮质下解剖结构的个体差异是否反映在静息态皮质振荡中。我们分析了剑桥衰老和神经科学中心 (CamCAN) 队列中 533 名健康成年人的静息态脑磁图 (MEG) 和结构 MRI，以测试皮层下体积的半球不对称是否预示着皮层振荡功率的不对称。计算皮质下体积和同源 MEG 传感器对的振荡功率的侧化指数。基于聚类的排列测试揭示了皮层下解剖结构和皮层活动之间的频率特异性关联。
- Keywords: subcortical, cortical, lateralisation, associated, structures

### 2. [解码和表征语义信息的颅内表示](https://www.biorxiv.org/content/10.64898/2026.07.13.738249v1)
- Original title: Decoding and Characterizing the Intracranial Representation of Semantic Information
- Authors: Smith, C., Inchyna, S., Barrentine, B., Nelson, M. J.
- Meta: 2026-07-15 | neuroscience | DOI: 10.64898/2026.07.13.738249
- 中文摘要: 脑机接口（BCI）通过解码与语音产生相关的运动和发音信号，取得了令人印象深刻的性能。然而，对于是否可以从人类皮层活动中解码更高级别的语义表示，人们知之甚少。展示语义解码将促进我们对语言组织的理解以及依赖概念而非纯粹发音信息的脑机接口的开发。我们记录了接受立体定向脑电图（sEEG）的患者在执行需要语义处理的语言任务时的颅内神经活动，以进行临床癫痫监测。从局部场势中提取高伽马功率，并​​用于生成用于监督机器学习分类的试验级特征。使用交叉验证评估分类性能。
- Abstract: Brain-computer interfaces (BCIs) have achieved impressive performance by decoding motor and articulatory signals associated with speech production. However, considerably less is known about whether higher-level semantic representations can be decoded from human cortical activity. Demonstrating semantic decoding would advance both our understanding of language organization and the development of BCIs that rely on con...
- Summary (fallback): 机器翻译摘要显示：脑机接口（BCI）通过解码与语音产生相关的运动和发音信号，取得了令人印象深刻的性能。然而，对于是否可以从人类皮层活动中解码更高级别的语义表示，人们知之甚少。展示语义解码将促进我们对语言组织的理解以及依赖概念而非纯粹发音信息的脑机接口的开发。我们记录了接受立体定向脑电图（sEEG）的患者在执行需要语义处理的语言任务时的颅内神经活动，以进行临床癫痫监测。从局部场势中提取高伽马功率，并​​用于生成用于监督机器学习分类的试验级特征。使用交叉验证评估分类性能。
- Keywords: semantic, information, decoding, language, intracranial

### 3. [宿主感染选择导致细菌社交作弊的 sRNA 变体](https://www.biorxiv.org/content/10.64898/2025.12.19.695336v3)
- Original title: Host infection selects for sRNA variants that drive bacterial social cheating
- Authors: Dubois, Q., Brual, T., Sprenger, M., Utzinger, V., Mercier, R. et al.
- Meta: 2026-07-15 | microbiology | DOI: 10.64898/2025.12.19.695336
- 中文摘要: 调节性小 RNA (sRNA) 中的单核苷酸突变代表了细菌感染期间社交欺骗的一种很大程度上尚未探索的途径。在这里，我们发现 arcZ 在植物病原体 Dickeya solani 中编码保守的 Hfq 依赖性 sRNA，在马铃薯块茎感染期间经历反复的单核苷酸突变。五个不同的 arcZ 等位基因定义了一系列分级的 ArcZ 功能损伤，其中抗真菌和蛋白酶活性逐渐降低，而毒力仅在等位基因的子集中受到损害。所有五种变体仅在与野生型 arcZ1 细胞共感染期间获得适应性优势。当变异很罕见时，这种优势最为明显，并且随着作弊者频率的增加而下降，最终与细菌总生产力的降低、社会作弊的典型特征和公地悲剧相关。
- Abstract: Single-nucleotide mutations in regulatory small RNAs (sRNAs) represent a largely unexplored route to social cheating during bacterial infection. Here we show that arcZ, encoding a conserved Hfq-dependent sRNA in the plant pathogen Dickeya solani, undergoes recurrent single-nucleotide mutations during potato tuber infection. Five distinct arcZ alleles define a graded series of ArcZ functional impairment in which anti...
- Summary (fallback): 机器翻译摘要显示：调节性小 RNA (sRNA) 中的单核苷酸突变代表了细菌感染期间社交欺骗的一种很大程度上尚未探索的途径。在这里，我们发现 arcZ 在植物病原体 Dickeya solani 中编码保守的 Hfq 依赖性 sRNA，在马铃薯块茎感染期间经历反复的单核苷酸突变。五个不同的 arcZ 等位基因定义了一系列分级的 ArcZ 功能损伤，其中抗真菌和蛋白酶活性逐渐降低，而毒力仅在等位基因的子集中受到损害。所有五种变体仅在与野生型 arcZ1 细胞共感染期间获得适应性优势。当变异很罕见时，这种优势最为明显，并且随着作弊者频率的增加而下降，最终与细菌总生产力的降低、社会作弊的典型特征和公地悲剧相关。
- Keywords: infection, variants, during, arcz, social

### 4. [分子动力学模拟表明抗生素对镜像细菌靶标的亲和力降低](https://www.biorxiv.org/content/10.64898/2026.07.14.738450v1)
- Original title: Molecular dynamics simulations demonstrate reduced antibiotic affinity to mirror bacterial targets
- Authors: Fady, P.-E., Ciccone, J.
- Meta: 2026-07-15 | molecular biology | DOI: 10.64898/2026.07.14.738450
- 中文摘要: 镜像生命是由非天然手性生物大分子组成的自我复制生物体，它构成了未来的威胁，并可能产生全球性后果。因此，专家们一致认为不应该创建它。然而，对于现有的医疗对策在镜像细菌产生后的有效性如何方面存在一些分歧。在这里，我们利用包括对接和分子动力学在内的计算化学方法来确定现有抗生素对天然和镜像细菌蛋白靶标的可能结合功效。我们发现大多数现有抗生素无法结合镜像细菌蛋白靶标，这与它们的天然手性靶标不同。这表明当前医疗对策的结合发生了改变，这可能会影响镜像细菌的抗菌活性（如果镜像细菌被创造出来）。
- Abstract: Mirror life, self-replicating organisms composed of non-natural-chirality biomacromolecules, presents a future threat with potentially global consequences. Consequently, there is strong agreement among experts that it should not be created. However, there is some disagreement over how effective existing medical countermeasures might prove against mirror bacteria in the event that they were created. Here, we leverage...
- Summary (fallback): 机器翻译摘要显示：镜像生命是由非天然手性生物大分子组成的自我复制生物体，它构成了未来的威胁，并可能产生全球性后果。因此，专家们一致认为不应该创建它。然而，对于现有的医疗对策在镜像细菌产生后的有效性如何方面存在一些分歧。在这里，我们利用包括对接和分子动力学在内的计算化学方法来确定现有抗生素对天然和镜像细菌蛋白靶标的可能结合功效。我们发现大多数现有抗生素无法结合镜像细菌蛋白靶标，这与它们的天然手性靶标不同。这表明当前医疗对策的结合发生了改变，这可能会影响镜像细菌的抗菌活性（如果镜像细菌被创造出来）。
- Keywords: mirror, targets, bacterial, created, existing

### 5. [SF3B3 / SF3B5 形成 U2 snRNP 的后生动物特异性转录模块，以独立剪接的方式协调 Pol II 延伸](https://www.biorxiv.org/content/10.64898/2026.07.14.737342v1)
- Original title: SF3B3 / SF3B5 form a metazoan specific transcription module of the U2 snRNP that coordinates Pol II elongation in a splicing independent manner
- Authors: Vassiliadis, D., Balic, J. J., Braniff, O., Gillespie, A., Rothnie, W. et al.
- Meta: 2026-07-15 | molecular biology | DOI: 10.64898/2026.07.14.737342
- 中文摘要: 共转录剪接是真核基因表达的保守特征。然而，确定这个过程的功能性质一直很困难。在这里，使用高通量 CRISPR/Cas9 筛选，我们令人惊讶地发现，U2 snRNP 复合物的第三大亚基 SF3B3 是 RNA Pol II 暂停释放和持续合成能力的主要调节因子。值得注意的是，SF3B3 的缺失会极大地扰乱转录，但 U2 snRNP 组装和 RNA 剪接不受影响。从机制上讲，SF3B3 与 PAF1c 和 Integrator 复合物一起协调转录激酶 (CDK9/12/13) 的染色质占据，以调节 Pol II。 SF3B3 的结构/功能分析表明，其无序尾部表型中的后生动物特异性 18aa 序列复制了其损失并介导 SF3B5 的物理关联和稳定性。
- Abstract: Co-transcriptional splicing is a conserved feature of eukaryotic gene expression. However, establishing the functional nature of this process has been difficult. Here using high throughput CRISPR/Cas9 screens we surprisingly find that SF3B3, the third largest subunit of the U2 snRNP complex, is a major regulator of RNA Pol II pause release and processivity. Remarkably, the absence of SF3B3 dramatically perturbs tran...
- Summary (fallback): 机器翻译摘要显示：共转录剪接是真核基因表达的保守特征。然而，确定这个过程的功能性质一直很困难。在这里，使用高通量 CRISPR/Cas9 筛选，我们令人惊讶地发现，U2 snRNP 复合物的第三大亚基 SF3B3 是 RNA Pol II 暂停释放和持续合成能力的主要调节因子。值得注意的是，SF3B3 的缺失会极大地扰乱转录，但 U2 snRNP 组装和 RNA 剪接不受影响。从机制上讲，SF3B3 与 PAF1c 和 Integrator 复合物一起协调转录激酶 (CDK9/12/13) 的染色质占据，以调节 Pol II。 SF3B3 的结构/功能分析表明，其无序尾部表型中的后生动物特异性 18aa 序列复制了其损失并介导 SF3B5 的物理关联和稳定性。
- Keywords: sf3b3, snrnp, sf3b5, splicing, metazoan

### 6. [超越气候干旱指数：量化森林水分压力的水力方法](https://www.biorxiv.org/content/10.64898/2026.07.13.738371v1)
- Original title: Beyond climatic drought indices : an hydraulic approach to quantifying forest water stress
- Authors: Cochard, H.
- Meta: 2026-07-15 | plant biology | DOI: 10.64898/2026.07.13.738371
- 中文摘要: 本文介绍了一种基于植物水力建模方法而不是经典气候干旱指数的新森林压力指数 (ISF)。与 scPDSI 或 SPEI 等其他指数不同，ISF 是以机械 SurEau 模型模拟的木质部栓塞动力学为基础的。目标是更好地将气候异常与树木的生理功能和死亡风险联系起来。 ISF 使用局部适应的表型来定义，其特征在于参考水力功能阈值下的最佳 P50 值。使用多个气候数据集在欧洲和法国进行模拟。该指数对于模型参数化选择和关于植物功能性状的假设是稳健的。结果显示出很强的时空一致性以及与 SPEI 和 scPDSI 的显着相关性。然而，ISF 更强烈地强调极端干旱年份，并表现出更偏态的分布......
- Abstract: The article introduces a new Forest Stress Index (ISF) based on a plant hydraulic modelling approach rather than classical climatic drought indices. Unlike other index like scPDSI or SPEI, ISF is grounded in xylem embolism dynamics simulated with the mechanistic SurEau model. The goal is to better link climatic anomalies to tree physiological functioning and mortality risk. ISF is defined using a locally adapted ide...
- Summary (fallback): 机器翻译摘要显示：本文介绍了一种基于植物水力建模方法而不是经典气候干旱指数的新森林压力指数 (ISF)。与 scPDSI 或 SPEI 等其他指数不同，ISF 是以机械 SurEau 模型模拟的木质部栓塞动力学为基础的。目标是更好地将气候异常与树木的生理功能和死亡风险联系起来。 ISF 使用局部适应的表型来定义，其特征在于参考水力功能阈值下的最佳 P50 值。使用多个气候数据集在欧洲和法国进行模拟。该指数对于模型参数化选择和关于植物功能性状的假设是稳健的。结果显示出很强的时空一致性以及与 SPEI 和 scPDSI 的显着相关性。然而，ISF 更强烈地强调极端干旱年份，并表现出更偏态的分布......
- Keywords: drought, hydraulic, climatic, forest, stress

### 7. [蛋白质组学中隐藏的结构偏差：超声诱导的本质无序区域的选择性断裂](https://www.biorxiv.org/content/10.64898/2026.07.14.738389v1)
- Original title: Hidden Structural Bias in Proteomics: Sonication-induced Selective Fragmentation of Intrinsically Disordered Regions
- Authors: Narita, M., Yamakawa, T., Nishimura, R., Iwasaki, M.
- Meta: 2026-07-15 | cell biology | DOI: 10.64898/2026.07.14.738389
- 中文摘要: 超声处理是蛋白质组样品制备的一项基本技术，主要用于蛋白质溶解和基因组 DNA 剪切。尽管 DNA 的机械剪切已得到充分表征，但其对蛋白质结构完整性的意外影响仍然是高通量分析工作流程中的一个重要“盲点”。在这项研究中，我们通过将凝胶分级分离 (PEPPI-MS) 与序列水平组成分析和生物信息学图谱相结合，系统地研究了超声处理诱导的蛋白质断裂。我们的结果表明，超声处理不会显着改变整体蛋白质组鉴定或膜蛋白的回收；然而，它会引起广泛且非随机的蛋白质碎片。
- Abstract: Sonication is a fundamental technique in proteome sample preparation, primarily used for protein solubilization and shearing of genomic DNA. Although the mechanical shearing of DNA is well-characterized, its unintended impact on protein structural integrity remains a significant ''blind spot'' in high-throughput analytical workflows. In this study, we systematically investigated sonication-induced protein fragmentat...
- Summary (fallback): 机器翻译摘要显示：超声处理是蛋白质组样品制备的一项基本技术，主要用于蛋白质溶解和基因组 DNA 剪切。尽管 DNA 的机械剪切已得到充分表征，但其对蛋白质结构完整性的意外影响仍然是高通量分析工作流程中的一个重要“盲点”。在这项研究中，我们通过将凝胶分级分离 (PEPPI-MS) 与序列水平组成分析和生物信息学图谱相结合，系统地研究了超声处理诱导的蛋白质断裂。我们的结果表明，超声处理不会显着改变整体蛋白质组鉴定或膜蛋白的回收；然而，它会引起广泛且非随机的蛋白质碎片。
- Keywords: structural, sonication, protein, proteins, fragmentation

### 8. [坏死性凋亡信号传导改变角质形成细胞的命运，促进分化和减缓伤口愈合](https://www.biorxiv.org/content/10.64898/2026.07.13.738083v1)
- Original title: Necroptotic Signalling Diverts Keratinocyte Fate to Promote Differentiation and Slow Wound Healing
- Authors: Anderton, H., He, Y., Silke, N., Lynch-Godrei, A., Gu, L. H. et al.
- Meta: 2026-07-15 | cell biology | DOI: 10.64898/2026.07.13.738083
- 中文摘要: 坏死性凋亡最为人所知的是一种由 RIPK3 和 MLKL 介导的溶解性促炎性细胞死亡途径。有效的伤口修复需要炎症的快速消退，持续的坏死性凋亡活动只会加剧组织损伤，延迟愈合。然而，受损的皮肤为坏死性凋亡信号提供了一个富含触发因素的环境，这是一个尚未解决的明显悖论。通过对多个伤口模型进行基因消融和药物抑制，我们发现抑制坏死性凋亡可加速伤口闭合，揭示坏死性凋亡信号通常会抑制修复。令人惊讶的是，我们发现野生型角质形成细胞中的 MLKL 激活诱导分化和膜修复而不是细胞裂解。这种适应性的、非致命性的坏死性凋亡信号传导模式保留了屏障的完整性，但减缓了上皮细胞的再形成。
- Abstract: Necroptosis is best known as a lytic, proinflammatory cell-death pathway mediated by RIPK3 and MLKL. Effective wound repair requires the rapid resolution of inflammation, and ongoing necroptotic activity would only exacerbate tissue damage, delaying healing. However, damaged skin presents a trigger-rich environment for necroptotic signalling, an apparent paradox that remains unresolved. Using genetic ablation and ph...
- Summary (fallback): 机器翻译摘要显示：坏死性凋亡最为人所知的是一种由 RIPK3 和 MLKL 介导的溶解性促炎性细胞死亡途径。有效的伤口修复需要炎症的快速消退，持续的坏死性凋亡活动只会加剧组织损伤，延迟愈合。然而，受损的皮肤为坏死性凋亡信号提供了一个富含触发因素的环境，这是一个尚未解决的明显悖论。通过对多个伤口模型进行基因消融和药物抑制，我们发现抑制坏死性凋亡可加速伤口闭合，揭示坏死性凋亡信号通常会抑制修复。令人惊讶的是，我们发现野生型角质形成细胞中的 MLKL 激活诱导分化和膜修复而不是细胞裂解。这种适应性的、非致命性的坏死性凋亡信号传导模式保留了屏障的完整性，但减缓了上皮细胞的再形成。
- Keywords: necroptotic, signalling, wound, repair, necroptosis

### 9. [蝾螈的再生揭示了脊椎动物基因组中保守的休眠顺式调控语法](https://www.biorxiv.org/content/10.64898/2026.07.13.738357v1)
- Original title: Axolotl regeneration reveals a dormant cis-regulatory grammar conserved across vertebrate genomes
- Authors: Fujiwara, T., Nakanishi, K., Suzuki, T., Shimizu, H.
- Meta: 2026-07-15 | systems biology | DOI: 10.64898/2026.07.13.738357
- 中文摘要: 大多数哺乳动物缺乏在受伤后再生复杂组织的能力，而其他脊椎动物（例如蝾螈）在一生中都能重建完整的四肢，但这种显着差异背后的调节机制仍然难以捉摸。在这里，我们定义了驱动蝾螈肢体再生的核心顺式调控基序语法，并证明该语法在人类和小鼠基因组中再生基因直系同源物的同线邻域内是保守的，尽管在成年哺乳动物组织中被表观遗传封闭。
- Abstract: Unlike most mammals, which lack the capacity to regenerate complex tissues following injury, other vertebrates such as the axolotl rebuild complete limbs throughout life, yet the regulatory mechanisms underlying this striking difference have remained elusive. Here, we define the core cis-regulatory motif grammar driving axolotl limb regeneration and demonstrate that this grammar is conserved within the syntenic neig...
- Summary (fallback): 机器翻译摘要显示：大多数哺乳动物缺乏在受伤后再生复杂组织的能力，而其他脊椎动物（例如蝾螈）在一生中都能重建完整的四肢，但这种显着差异背后的调节机制仍然难以捉摸。在这里，我们定义了驱动蝾螈肢体再生的核心顺式调控基序语法，并证明该语法在人类和小鼠基因组中再生基因直系同源物的同线邻域内是保守的，尽管在成年哺乳动物组织中被表观遗传封闭。
- Keywords: grammar, axolotl, regenerative, regeneration, dormant

### 10. [支持多命运细胞决策的基因调控网络](https://www.biorxiv.org/content/10.64898/2026.07.13.738161v1)
- Original title: Gene Regulatory Networks that support Multi-Fate Cellular Decisions
- Authors: BV, H., Adigwe, S., Jolly, M. K., Gedeon, T.
- Meta: 2026-07-15 | systems biology | DOI: 10.64898/2026.07.13.738161
- 中文摘要: 细胞命运决定是由基因调控网络（GRN）驱动的。虽然相互抑制切换开关有效地模拟了二元命运决策，但具有两个以上节点的完全连接的抑制网络无法捕获多命运决策，因为“单一高状态”的流行率较低，其中只有一个主调节器被高度表达。本研究的目标是找到支持所有单一高状态的网络结构。我们发现，在单调布尔（MB）模型集中实现所有单一高状态的最高可能流行率的唯一网络是完全断开的。由于生物网络通常需要连接性，我们研究支持等势的网络结构，其中所有单一高状态在 MB 模型中具有相同的流行度。
- Abstract: Cell fate decisions are driven by gene regulatory networks (GRNs). While the mutually inhibitory toggle switch effectively models binary fate decisions, fully connected inhibitory networks with more than two nodes fail to capture multi-fate decisions due to the low prevalence of ``single high states", where only a single master regulator is highly expressed. The goal of this study is to find network structures that...
- Summary (fallback): 机器翻译摘要显示：细胞命运决定是由基因调控网络（GRN）驱动的。虽然相互抑制切换开关有效地模拟了二元命运决策，但具有两个以上节点的完全连接的抑制网络无法捕获多命运决策，因为“单一高状态”的流行率较低，其中只有一个主调节器被高度表达。本研究的目标是找到支持所有单一高状态的网络结构。我们发现，在单调布尔（MB）模型集中实现所有单一高状态的最高可能流行率的唯一网络是完全断开的。由于生物网络通常需要连接性，我们研究支持等势的网络结构，其中所有单一高状态在 MB 模型中具有相同的流行度。
- Keywords: networks, single, support, high, states

### 11. [撤回：花粉饮食和甾醇供应对通才独居蜂幼虫发育的影响不同](https://www.biorxiv.org/content/10.1101/2025.04.21.649687v2)
- Original title: WITHDRAWN: Pollen Diet and Sterol Provisioning Differentially Affected Larval Development in a Generalist Solitary Bee
- Authors: Martel, C., Kreidt, J., Furse, S., Jennifer Scott, J., Griffiths-Lee, J. et al.
- Meta: 2026-07-15 | developmental biology | DOI: 10.1101/2025.04.21.649687
- 中文摘要: 作者已撤回他们的手稿，因为其中一位列出的作者在提交之前未提供对作者身份和提交的批准。因此，作者不希望该工作被引用作为该项目的参考。如有疑问，请联系通讯作者。
- Abstract: The authors have withdrawn their manuscript because one of the listed authors had not provided approval of the authorship and submission prior to submission. Therefore, the authors do not wish this work to be cited as reference for the project. If you have any questions, please contact the corresponding author.
- Summary (fallback): 机器翻译摘要显示：作者已撤回他们的手稿，因为其中一位列出的作者在提交之前未提供对作者身份和提交的批准。因此，作者不希望该工作被引用作为该项目的参考。如有疑问，请联系通讯作者。
- Keywords: authors, withdrawn, submission, pollen, diet

### 12. [从海岸线植被到胚胎沙丘：高度城市化海岸的自然固沙](https://www.biorxiv.org/content/10.64898/2026.07.14.738448v1)
- Original title: From strandline vegetation to embryo dunes: natural sand retention along a heavily urbanized coast
- Authors: Taelman, C., Provoost, S., Batsleer, F., Bonte, D., Van Uytvanck, J.
- Meta: 2026-07-15 | ecology | DOI: 10.64898/2026.07.14.738448
- 中文摘要: 1. 城市化海岸沿线的沙滩越来越多地通过海滩营养和硬基础设施进行管理，但这些干预措施往往限制自然沙丘的形成过程。沿着比利时海岸，大部分海滩-沙丘界面都与堤坝、长廊和密集的娱乐场所接壤，岸线植被可能提供了一种被忽视的固沙和启动沙丘胚胎发育的机制。 2. 我们评估了四种先锋沙丘植物物种（Cakile maritima、Calamagrostis arenararia、Elymus farctus 和 Salsola kali）在比利时海岸沿线建立、发展植被覆盖和促进沙子积累的潜力。
- Abstract: 1. Sandy beaches along urbanized coasts are increasingly managed through beach nourishment and hard infrastructure, yet these interventions often constrain natural dune-building processes. Along the Belgian coast, where much of the beach-dune interface is bordered by dikes, promenades and intensive recreation, strandline vegetation may provide an overlooked mechanism for retaining sand and initiating embryo dune dev...
- Summary (fallback): 机器翻译摘要显示：1. 城市化海岸沿线的沙滩越来越多地通过海滩营养和硬基础设施进行管理，但这些干预措施往往限制自然沙丘的形成过程。沿着比利时海岸，大部分海滩-沙丘界面都与堤坝、长廊和密集的娱乐场所接壤，岸线植被可能提供了一种被忽视的固沙和启动沙丘胚胎发育的机制。 2. 我们评估了四种先锋沙丘植物物种（Cakile maritima、Calamagrostis arenararia、Elymus farctus 和 Salsola kali）在比利时海岸沿线建立、发展植被覆盖和促进沙子积累的潜力。
- Keywords: vegetation, sand, cover, strandline, along

### 13. [死亡预言的编年史：加纳萨库莫泻湖的生态崩溃](https://www.biorxiv.org/content/10.64898/2026.07.14.738434v1)
- Original title: Chronicle of a Death Foretold: The Ecological Collapse of Sakumo Lagoon, Ghana
- Authors: Akwetey, M. F. A., Lamptey, E., Abrokwah, S., Aheto, D. W., Mensah, P. K. et al.
- Meta: 2026-07-15 | ecology | DOI: 10.64898/2026.07.14.738434
- 中文摘要: 萨库莫泻湖是加纳的一个小型（1平方公里）半开放沿海泻湖，位于阿克拉和特马市之间。泻湖及其周围的湿地于 1992 年被指定为拉姆萨尔湿地，主要是因为它是 66 种本地鸟类和候鸟的避难所。 1971 年，人们对泻湖的生态及其主要鱼类（特别是黑颊罗非鱼（Sarotherodon melanotheron））的生物学进行了彻底研究，当时泻湖是一个多样化的、主要是咸水的生态系统，支持着传统且管理良好的渔业。 2016年至2017年，另一项研究发现泻湖大部分被漂浮植被和塑料垃圾覆盖。最终，在 2024 年，目视调查发现，漂浮的植被几乎完全被陆地植物所取代，连接泻湖和公海的涵洞前只有几平方米的垃圾散布的水域。
- Abstract: Sakumo Lagoon, a small (1 km2) semi-open coastal lagoon in Ghana, lies between the cities of Accra and Tema. The lagoon and its surrounding wetland were designated a Ramsar Site in 1992, mainly because it served as a refuge for 66 local and migratory bird species. Its ecology, and the biology of its major fish species, notably the blackchin tilapia (Sarotherodon melanotheron) were thoroughly studied in 1971, when th...
- Summary (fallback): 机器翻译摘要显示：萨库莫泻湖是加纳的一个小型（1平方公里）半开放沿海泻湖，位于阿克拉和特马市之间。泻湖及其周围的湿地于 1992 年被指定为拉姆萨尔湿地，主要是因为它是 66 种本地鸟类和候鸟的避难所。 1971 年，人们对泻湖的生态及其主要鱼类（特别是黑颊罗非鱼（Sarotherodon melanotheron））的生物学进行了彻底研究，当时泻湖是一个多样化的、主要是咸水的生态系统，支持着传统且管理良好的渔业。 2016年至2017年，另一项研究发现泻湖大部分被漂浮植被和塑料垃圾覆盖。最终，在 2024 年，目视调查发现，漂浮的植被几乎完全被陆地植物所取代，连接泻湖和公海的涵洞前只有几平方米的垃圾散布的水域。
- Keywords: lagoon, sakumo, ghana, ramsar, site

### 14. [物种分布模型在发生数据污染时失效：校准误差集中在河流网络源头](https://www.biorxiv.org/content/10.64898/2026.07.14.738364v1)
- Original title: Where species distribution models fail under occurrence-data contamination: calibration error concentrates at stream-network headwaters
- Authors: Miok, K., Laza, A. V., Skrlj, B., Robnik-Sikonja, M., Parvulescu, L.
- Meta: 2026-07-15 | ecology | DOI: 10.64898/2026.07.14.738364
- 中文摘要: 物种分布模型 (SDM) 越来越多地为淡水系统的保护和生物安全决策提供信息，其中不确定性估计的可靠性与其点预测一样重要。集成SDM从跨重复方差中得出预测区间，但只有当重复数据不一致时，这种方差才会捕获系统误差，当训练数据受到低准确度记录污染时（公民科学数据集中的常态），这种假设就会失败。这种故障在空间上是均匀的还是集中在某个范围的可识别部分尚不清楚。
- Abstract: Species distribution models (SDMs) increasingly inform conservation and biosecurity decisions in freshwater systems, where the reliability of its uncertainty estimates matters as much as its point predictions. Ensemble SDMs derive prediction intervals from across-replicate variance, but this variance captures systematic error only when replicates disagree about it, an assumption that fails when training data are con...
- Summary (fallback): 机器翻译摘要显示：物种分布模型 (SDM) 越来越多地为淡水系统的保护和生物安全决策提供信息，其中不确定性估计的可靠性与其点预测一样重要。集成SDM从跨重复方差中得出预测区间，但只有当重复数据不一致时，这种方差才会捕获系统误差，当训练数据受到低准确度记录污染时（公民科学数据集中的常态），这种假设就会失败。这种故障在空间上是均匀的还是集中在某个范围的可识别部分尚不清楚。
- Keywords: where, calibration, headwaters, species, ensemble

### 15. [学习的地标关联支持能见度降低下的在线视觉控制](https://www.biorxiv.org/content/10.64898/2026.07.13.738310v1)
- Original title: Learned landmark associations support online visual control under degraded visibility
- Authors: Roessling, G., Fajen, B.
- Meta: 2026-07-15 | animal behavior and cognition | DOI: 10.64898/2026.07.13.738310
- 中文摘要: 人类和其他动物经常在至少部分熟悉的环境中行动，其中空间布局的各个方面都是已知的。尽管已知此类知识可以支持导航和空间认知，但其在在线控制行动中的作用仍不清楚。我们调查了驾驶员是否使用道路布局知识来指导高能见度和低能见度下的转向，如果是的话，研究这些知识的形式。在两次模拟驾驶实验（总计 N = 90）中，参与者反复驾驶包含有雾和无雾路段的蜿蜒道路。反复经历相同道路的驾驶员比遇到新道路的驾驶员表现出更稳定的转向和车道定位，但前提是能见度降低。这些优势伴随着在评估道路几何知识的后测试中的卓越表现。
- Abstract: Humans and other animals often act in environments that are at least partly familiar, where aspects of the spatial layout are known. Although such knowledge is known to support navigation and spatial cognition, its role in the online control of action remains unclear. We investigated whether drivers use knowledge of road layout to guide steering in high and low visibility and, if so, the form of such knowledge. In t...
- Summary (fallback): 机器翻译摘要显示：人类和其他动物经常在至少部分熟悉的环境中行动，其中空间布局的各个方面都是已知的。尽管已知此类知识可以支持导航和空间认知，但其在在线控制行动中的作用仍不清楚。我们调查了驾驶员是否使用道路布局知识来指导高能见度和低能见度下的转向，如果是的话，研究这些知识的形式。在两次模拟驾驶实验（总计 N = 90）中，参与者反复驾驶包含有雾和无雾路段的蜿蜒道路。反复经历相同道路的驾驶员比遇到新道路的驾驶员表现出更稳定的转向和车道定位，但前提是能见度降低。这些优势伴随着在评估道路几何知识的后测试中的卓越表现。
- Keywords: knowledge, road, associations, control, visibility

### 16. [CRBN 的共价重塑创建了与 NTAQ1 的非规范新底物界面](https://www.biorxiv.org/content/10.64898/2026.07.14.738385v1)
- Original title: Covalent remodeling of CRBN creates a non-canonical neosubstrate interface with NTAQ1
- Authors: de la Pena, A. H., Cruite, J. T., Che, J., Matyskiela, M. E., Chamberlain, P. P. et al.
- Meta: 2026-07-15 | biochemistry | DOI: 10.64898/2026.07.14.738385
- 中文摘要: 分子胶降解剂 EM12-FS 共价修饰 cereblon (CRBN) His353，从而能够选择性地将新底物 NTAQ1 招募到 CRL4CRBN 泛素连接酶中。我们确定了 NTAQ1-EM12-FS-CRBN-DDB1 复合物的冷冻电镜结构，揭示了通过共价重塑 CRBN 传感器环路创建的非规范新基质界面。咪唑化重新定位 His353，以消除阻碍 NTAQ1 与可逆 IMiD 结合的空间冲突，并且通过硫酸化 His353 和 NTAQ1 Phe126 之间独特的 T 形 C-H/{pi} 相互作用来稳定工程界面。生化和突变分析定义了三元复合物形成和泛素化的决定因素。
- Abstract: Molecular glue degrader EM12-FS covalently modifies cereblon (CRBN) His353, enabling selective recruitment of the neosubstrate NTAQ1 to the CRL4CRBN ubiquitin ligase. We determined the cryo-EM structure of the NTAQ1-EM12-FS-CRBN-DDB1 complex, revealing a non-canonical neosubstrate interface created by covalent remodeling of the CRBN sensor loop. Imidazylation repositions His353 to eliminate the steric clash that pre...
- Summary (fallback): 机器翻译摘要显示：分子胶降解剂 EM12-FS 共价修饰 cereblon (CRBN) His353，从而能够选择性地将新底物 NTAQ1 招募到 CRL4CRBN 泛素连接酶中。我们确定了 NTAQ1-EM12-FS-CRBN-DDB1 复合物的冷冻电镜结构，揭示了通过共价重塑 CRBN 传感器环路创建的非规范新基质界面。咪唑化重新定位 His353，以消除阻碍 NTAQ1 与可逆 IMiD 结合的空间冲突，并且通过硫酸化 His353 和 NTAQ1 Phe126 之间独特的 T 形 C-H/{pi} 相互作用来稳定工程界面。生化和突变分析定义了三元复合物形成和泛素化的决定因素。
- Keywords: crbn, ntaq1, covalent, neosubstrate, interface

### 17. [TSC 复合物 GAP 活性的分子基础](https://www.biorxiv.org/content/10.64898/2026.07.14.738392v1)
- Original title: Molecular basis of TSC complex GAP activity
- Authors: Titze, S., Ruettermann, M., Nellist, M., Kuemmel, D.
- Meta: 2026-07-15 | biochemistry | DOI: 10.64898/2026.07.14.738392
- 中文摘要: 结节性硬化症复合物 (TSC) 蛋白复合物 (TSCC) 充当小 GTP 酶 Rheb 的 GTP 酶激活蛋白 (GAP)，以限制 mTORC1（雷帕霉素复合物 1 的机械靶标）活性和细胞生长。我们报道了 TSCC 和 Rheb 的催化过渡态复合物的结构。细胞中的功能需要两个含有天冬酰胺-拇指 GAP 结构域的 TSC2 亚基与两个辅助 TSC1 亚基的组装。催化需要 TSC2 的天冬酰胺拇指残基和 Rheb 中在多个相互作用位点结合 TSC2 的保守残基。令人惊讶的是，只有一个 TSC2 GAP 结构域具有催化能力并与 Rheb 相互作用。这是通过 TSC1 的不对称结合实现的，它能够激活 TSC2 亚基之一的结构变化，并将第二个 TSC2 副本锁定在非活性构象中。
- Abstract: The tuberous sclerosis complex (TSC) protein complex (TSCC) acts as the GTPase activating protein (GAP) for the small GTPase Rheb, to limit mTORC1 (mechanistic target of rapamycin complex 1) activity and cellular growth. We report the structure of the catalytic transition state complex of TSCC and Rheb. Assembly of two TSC2 subunits containing asparagine-thumb GAP domains with two accessory TSC1 subunits is required...
- Summary (fallback): 机器翻译摘要显示：结节性硬化症复合物 (TSC) 蛋白复合物 (TSCC) 充当小 GTP 酶 Rheb 的 GTP 酶激活蛋白 (GAP)，以限制 mTORC1（雷帕霉素复合物 1 的机械靶标）活性和细胞生长。我们报道了 TSCC 和 Rheb 的催化过渡态复合物的结构。细胞中的功能需要两个含有天冬酰胺-拇指 GAP 结构域的 TSC2 亚基与两个辅助 TSC1 亚基的组装。催化需要 TSC2 的天冬酰胺拇指残基和 Rheb 中在多个相互作用位点结合 TSC2 的保守残基。令人惊讶的是，只有一个 TSC2 GAP 结构域具有催化能力并与 Rheb 相互作用。这是通过 TSC1 的不对称结合实现的，它能够激活 TSC2 亚基之一的结构变化，并将第二个 TSC2 副本锁定在非活性构象中。
- Keywords: tsc2, complex, rheb, tscc, subunits

### 18. [整合血管和肥大软骨微组织来制造用于软骨内骨组织工程的放大移植物](https://www.biorxiv.org/content/10.64898/2026.07.13.738124v1)
- Original title: Integrating vascular and hypertrophic cartilage microtissues to fabricatescaled-up grafts for endochondral bone tissue engineering
- Authors: Kronemberger, G. S., Burdis, R., Correia, C., Baptista, L., Kelly, D. J.
- Meta: 2026-07-15 | bioengineering | DOI: 10.64898/2026.07.13.738124
- 中文摘要: 大骨缺损的修复仍然是一个重大的临床挑战，部分原因是血管化不足和移植材料整合不良。组织工程策略概括了软骨内骨化的发育过程，即软骨模板重塑为骨骼，在大骨缺损愈合的临床前模型中显示出巨大的潜力。然而，成功地将这些方法扩展到临床相关的尺寸将需要制定策略来支持移植物在体内植入后的快速血管化。在这里，首先通过将源自人类间充质干细胞/基质细胞 (MSC) 的肥大软骨微组织整合到涂有纳米羟基磷灰石 (nanoHA) 的骨传导性 3D 打印聚己内酯 (PCL) 框架内来制造机械加固模板。
- Abstract: The repair of large bone defects remains a major clinical challenge, in part due to inadequate vascularization and poor integration of graft materials. Tissue engineering strategies that recapitulate the developmental process of endochondral ossification, whereby a cartilage template remodels into bone, have shown significant potential in pre-clinical models of large bone defect healing. However, successfully scalin...
- Summary (fallback): 机器翻译摘要显示：大骨缺损的修复仍然是一个重大的临床挑战，部分原因是血管化不足和移植材料整合不良。组织工程策略概括了软骨内骨化的发育过程，即软骨模板重塑为骨骼，在大骨缺损愈合的临床前模型中显示出巨大的潜力。然而，成功地将这些方法扩展到临床相关的尺寸将需要制定策略来支持移植物在体内植入后的快速血管化。在这里，首先通过将源自人类间充质干细胞/基质细胞 (MSC) 的肥大软骨微组织整合到涂有纳米羟基磷灰石 (nanoHA) 的骨传导性 3D 打印聚己内酯 (PCL) 框架内来制造机械加固模板。
- Keywords: cartilage, bone, hypertrophic, microtissues, endochondral

### 19. [通过交互式自适应处理的基于纳米气泡的超声定位显微镜](https://www.biorxiv.org/content/10.64898/2026.07.14.738435v1)
- Original title: Nanobubble-Based Ultrasound Localization Microscopy through Interactive Adaptive Processing
- Authors: Ilovitsh, T., Shapiro, G., Gershman, Y., Bismuth, M.
- Meta: 2026-07-15 | bioengineering | DOI: 10.64898/2026.07.14.738435
- 中文摘要: 这项研究提出了使用亚微米纳米气泡（NB）作为超声定位显微镜（ULM）的造影剂，这是一种超分辨率成像技术，可以可视化超出声学衍射极限的微血管结构和流动。虽然 ULM 传统上依赖于微米级的微泡 (MB)，但 NB 尺寸的减小和循环时间的延长使其成为基于定位的成像的有吸引力的候选者。然而，它们较弱的声学响应给可靠检测和跟踪带来了重大挑战。为了应对这一挑战，我们开发了 ULM Master GUI，这是一个用于优化整个 ULM 处理流程的交互式框架。
- Abstract: This study presents the use of sub-micron nanobubbles (NBs) as contrast agents for ultrasound localization microscopy (ULM), a super-resolution imaging technique that visualizes microvascular structure and flow beyond the acoustic diffraction limit. While ULM has traditionally relied on micron-sized microbubbles (MBs), the reduced dimensions and prolonged circulation times of NBs make them attractive candidates for...
- Summary (fallback): 机器翻译摘要显示：这项研究提出了使用亚微米纳米气泡（NB）作为超声定位显微镜（ULM）的造影剂，这是一种超分辨率成像技术，可以可视化超出声学衍射极限的微血管结构和流动。虽然 ULM 传统上依赖于微米级的微泡 (MB)，但 NB 尺寸的减小和循环时间的延长使其成为基于定位的成像的有吸引力的候选者。然而，它们较弱的声学响应给可靠检测和跟踪带来了重大挑战。为了应对这一挑战，我们开发了 ULM Master GUI，这是一个用于优化整个 ULM 处理流程的交互式框架。
- Keywords: flow, acoustic, ultrasound, localization, microscopy

### 20. [结核分枝杆菌多表位疫苗的计算设计](https://www.biorxiv.org/content/10.64898/2026.07.09.737463v1)
- Original title: Computational design of a multi-epitope vaccine against M. tuberculosis
- Authors: Buhari, A., Okutu, P., Oyeleke, U. A., Sivakumar, A., Hameed, S. A.
- Meta: 2026-07-15 | bioinformatics | DOI: 10.64898/2026.07.09.737463
- 中文摘要: 背景：结核病仍然是全球主要的传染病杀手，卡介苗提供的成人保护不一致，而不断增加的耐药菌株需要新的疫苗策略。我们报告了第一个同时针对三种先前未开发的结核分枝杆菌毒力蛋白的多表位疫苗构建体； EccB3、MycP 和聚酮合酶共同控制营养获取、ESX 分泌完整性和先天免疫逃避。方法：使用反向疫苗学流程，预测 B 细胞、CTL 和 HTL 表位，过滤过敏性、毒性和 IFN-{gamma} 诱导，然后组装成 823 个残基的嵌合构建体，其中包含 β-防御素和 PADRE 佐剂以及 AAY/GPGPG 连接子，覆盖约 90% 的全球 HLA 多样性。
- Abstract: Background: Tuberculosis remains a leading global infectious killer, with BCG offering inconsistent adult protection and rising drug-resistant strains demanding novel vaccine strategies. We report the first multi-epitope vaccine construct simultaneously targeting three previously unexplored Mycobacterium tuberculosis virulence proteins; EccB3, MycP, and polyketide synthase which collectively govern nutrient acquisit...
- Summary (fallback): 机器翻译摘要显示：背景：结核病仍然是全球主要的传染病杀手，卡介苗提供的成人保护不一致，而不断增加的耐药菌株需要新的疫苗策略。我们报告了第一个同时针对三种先前未开发的结核分枝杆菌毒力蛋白的多表位疫苗构建体； EccB3、MycP 和聚酮合酶共同控制营养获取、ESX 分泌完整性和先天免疫逃避。方法：使用反向疫苗学流程，预测 B 细胞、CTL 和 HTL 表位，过滤过敏性、毒性和 IFN-{gamma} 诱导，然后组装成 823 个残基的嵌合构建体，其中包含 β-防御素和 PADRE 佐剂以及 AAY/GPGPG 连接子，覆盖约 90% 的全球 HLA 多样性。
- Keywords: construct, vaccine, tuberculosis, immune, multi-epitope

### 21. [综合计算毒理学通过暴露转录组学、单细胞空间映射和标记感知虚拟扰动揭示了牛皮癣中 PFOS 和 PFHxS 相关的炎症角质形成细胞生态位](https://www.biorxiv.org/content/10.64898/2026.07.09.737426v1)
- Original title: Integrative computational toxicology reveals PFOS and PFHxS associated inflammatory keratinocyte niches in psoriasis through exposure transcriptomics, single-cell spatial mapping and token-aware virtual perturbation
- Authors: Ma, J., Yu, Q.
- Meta: 2026-07-15 | bioinformatics | DOI: 10.64898/2026.07.09.737426
- 中文摘要: 全氟烷基物质和多氟烷基物质 (PFAS) 是持久性毒物，具有免疫、代谢和上皮效应，但其与炎症性皮肤病的相关性仍不清楚。我们开发了一个计算毒理学框架来测试全氟烷基磺酸盐程序，特别是全氟辛烷磺酸（PFOS）和全氟己磺酸（PFHxS）是否与银屑病相关的角质形成细胞炎症一致。暴露转录组源自 GSE236956，其中人胚胎干细胞衍生的上皮谱系模型暴露于 10 M PFAS 8-16 天。使用描述符、Tanimoto 相似性、毒理学证据、不良结果途径 (AOP) 类关键事件、暴露差异表达基因负担和跨读支持对六种 PFAS 进行优先排序。
- Abstract: Per- and polyfluoroalkyl substances (PFAS) are persistent toxicants with immunological, metabolic and epithelial effects, but their relevance to inflammatory skin disease remains unclear. We developed a computational toxicology framework to test whether perfluoroalkyl sulfonate programs, especially perfluorooctanesulfonic acid (PFOS) and perfluorohexanesulfonic acid (PFHxS), converge with psoriasis-associated kerati...
- Summary (fallback): 机器翻译摘要显示：全氟烷基物质和多氟烷基物质 (PFAS) 是持久性毒物，具有免疫、代谢和上皮效应，但其与炎症性皮肤病的相关性仍不清楚。我们开发了一个计算毒理学框架来测试全氟烷基磺酸盐程序，特别是全氟辛烷磺酸（PFOS）和全氟己磺酸（PFHxS）是否与银屑病相关的角质形成细胞炎症一致。暴露转录组源自 GSE236956，其中人胚胎干细胞衍生的上皮谱系模型暴露于 10 M PFAS 8-16 天。使用描述符、Tanimoto 相似性、毒理学证据、不良结果途径 (AOP) 类关键事件、暴露差异表达基因负担和跨读支持对六种 PFAS 进行优先排序。
- Keywords: inflammatory, pfhxs, keratinocyte, pfos, psoriasis

### 22. [可重复设计：Romics Processor，一个用于多组学和空间组学分析的 FAIR 生态系统](https://www.biorxiv.org/content/10.64898/2026.07.09.737600v1)
- Original title: Reproducible-by-design: Romics Processor, a FAIR ecosystem for multi-omics and spatial-omics analysis
- Authors: Gorman, B. L., Bhotika, H., Jehrio, M., Purkerson, J. M., Carlin, F. et al.
- Meta: 2026-07-15 | bioinformatics | DOI: 10.64898/2026.07.09.737600
- 中文摘要: 多组学和空间组学技术的使用呈爆炸式增长，产生越来越复杂的数据集。现有的生物信息学工具正在迅速发展，但未能完全执行公平原则，使得该领域容易受到计算再现性问题不断升级的影响。在这里，我们介绍了一种以组学数据处理包 RomicsProcessor 为代表的可重复设计范例。其核心是“Romics_object”，它是一个独立的数字工件，封装了从原始数据到完全处理状态的完整数据历史记录，捕获转换步骤和所需依赖关系的详细信息。这种架构确保计算工作流程完全可移植且可重复。
- Abstract: Multi-omics and spatial-omics technologies are exploding in use, producing increasingly complex datasets. Existing bioinformatics tools are developing rapidly but fail to fully enforce the FAIR principles, leaving the field vulnerable to escalating issues in computational reproducibility. Here, we introduce a reproducible-by-design paradigm represented in an omics data processing package, RomicsProcessor. At its cor...
- Summary (fallback): 机器翻译摘要显示：多组学和空间组学技术的使用呈爆炸式增长，产生越来越复杂的数据集。现有的生物信息学工具正在迅速发展，但未能完全执行公平原则，使得该领域容易受到计算再现性问题不断升级的影响。在这里，我们介绍了一种以组学数据处理包 RomicsProcessor 为代表的可重复设计范例。其核心是“Romics_object”，它是一个独立的数字工件，封装了从原始数据到完全处理状态的完整数据历史记录，捕获转换步骤和所需依赖关系的详细信息。这种架构确保计算工作流程完全可移植且可重复。
- Keywords: fair, multi-omics, fully, computational, reproducible-by-design

### 23. [CD4+ T 细胞 Perturb-seq 中的可靠性加权目标优先级：通用性理论分解](https://www.biorxiv.org/content/10.64898/2026.07.13.738312v1)
- Original title: Reliability-weighted target prioritization in CD4+ T-cell Perturb-seq: a generalizability-theory decomposition
- Authors: Cheng, C.
- Meta: 2026-07-15 | bioinformatics | DOI: 10.64898/2026.07.13.738312
- 中文摘要: 基因组规模的扰动序列筛选根据扰动转录效应的强度来优先考虑候选目标。效应强度没有回答先前的测量问题：读数可靠吗？从单个引导、单个供体或少量细胞的伪大量估计的大效应不需要在复制中存活，并且为了确定目标优先级，每个错误引导都需要进行验证实验。我们将每个扰动效应视为交叉目标 x 引导 x 捐助者 x 条件设计中的测量，并应用概括性理论（Cronbach 等，1972；Brennan，2001）将效应的可靠部分与特定方面的特质分开。指导者和捐赠者作为随机方面进入；条件作为固定方面进入并在其级别内进行分析。
- Abstract: Genome-scale Perturb-seq screens prioritize candidate targets by the strength of a perturbation's transcriptional effect. Effect strength does not answer a prior measurement question: is the readout dependable? A large effect estimated from a single guide, a single donor, or a pseudobulk of few cells need not survive replication, and for target prioritization each false lead costs a validation experiment. We treat e...
- Summary (fallback): 机器翻译摘要显示：基因组规模的扰动序列筛选根据扰动转录效应的强度来优先考虑候选目标。效应强度没有回答先前的测量问题：读数可靠吗？从单个引导、单个供体或少量细胞的伪大量估计的大效应不需要在复制中存活，并且为了确定目标优先级，每个错误引导都需要进行验证实验。我们将每个扰动效应视为交叉目标 x 引导 x 捐助者 x 条件设计中的测量，并应用概括性理论（Cronbach 等，1972；Brennan，2001）将效应的可靠部分与特定方面的特质分开。指导者和捐赠者作为随机方面进入；条件作为固定方面进入并在其级别内进行分析。
- Keywords: effect, target, dependable, each, guides

### 24. [WNT11 通过灭活 RAC1 抑制肿瘤发生和侵袭](https://www.biorxiv.org/content/10.64898/2026.07.13.738348v1)
- Original title: WNT11 suppresses tumor initiation and invasion by inactivating RAC1
- Authors: Karthikeyan, S., Casey, P., Wang, M.
- Meta: 2026-07-15 | cancer biology | DOI: 10.64898/2026.07.13.738348
- 中文摘要: WNT11 是一种非经典 WNT 配体，在发育和组织结构中发挥明确的作用；然而，它在癌症中的作用仍然不明确。在这里，我们将 WNT11 描述为人类上皮癌模型中癌症干性、侵袭和体内肿瘤形成的背景依赖性抑制因子。我们发现 WNT11 上调可降低干性促进基因的表达，抑制上皮间质转化，并抑制球体形成和肿瘤生长。相反，WNT11 的下调会增强癌细胞的这些侵袭性恶性特性。从机制上讲，我们发现 WNT11 抑制 RAC1 GTPase 激活的能力对于其入侵和自我更新的调节至关重要。在对 WNT11 无反应的细胞中，WNT11 和 RAC1 活性之间的连接被断开。
- Abstract: WNT11, a non-canonical WNT ligand, plays well-defined roles in development and tissue architecture; however, its function in cancer remains ambiguous. Here, we characterize WNT11 as a context-dependent suppressor of cancer stemness, invasion, and in vivo tumor formation in human epithelial cancer models. We show that WNT11 upregulation reduces the expression of stemness-promoting genes, suppresses epithelial-to-mese...
- Summary (fallback): 机器翻译摘要显示：WNT11 是一种非经典 WNT 配体，在发育和组织结构中发挥明确的作用；然而，它在癌症中的作用仍然不明确。在这里，我们将 WNT11 描述为人类上皮癌模型中癌症干性、侵袭和体内肿瘤形成的背景依赖性抑制因子。我们发现 WNT11 上调可降低干性促进基因的表达，抑制上皮间质转化，并抑制球体形成和肿瘤生长。相反，WNT11 的下调会增强癌细胞的这些侵袭性恶性特性。从机制上讲，我们发现 WNT11 抑制 RAC1 GTPase 激活的能力对于其入侵和自我更新的调节至关重要。在对 WNT11 无反应的细胞中，WNT11 和 RAC1 活性之间的连接被断开。
- Keywords: wnt11, rac1, cancer, tumor, cells

### 25. [磷酸化 YB-1 通过小细胞外囊泡的核易位导致三阴性乳腺癌的恶性表型](https://www.biorxiv.org/content/10.64898/2026.07.14.738446v1)
- Original title: Nuclear translocation of phosphorylated YB-1 via small extracellular vesicles contributes to the malignant phenotype of triple negative breast cancer
- Authors: Santos, M., Kim, Y., Feng, Z., Biebighauser, T., Lorico, A. et al.
- Meta: 2026-07-15 | cancer biology | DOI: 10.64898/2026.07.14.738446
- 中文摘要: 尽管诊断和治疗不断取得进展，但乳腺癌（BC）仍然是一个主要的健康问题。三阴性（雌激素受体-/孕激素受体-/HER2-）乳腺癌（TNBC）因其高转移潜力和对化疗的耐药性而成为最具侵袭性的亚型。 Y 盒结合蛋白 1 (YB-1) 转录因子是一种存在于细胞质和细胞核中的蛋白质，是 TNBC 恶性肿瘤的驱动因素，因为它会刺激癌症干细胞表型并扰乱细胞周期进程。在这里，我们假设含有 YB-1 的 sEV 将 YB-1 递送到受体癌细胞的核区室，并在转移过程的激活中发挥重要作用。我们发现 MDA 和 4T1 细胞的 sEV 中 YB-1 选择性富集，通过 d-STORM，所有 sEV 中约 65% 和 50% 的 YB-1 呈阳性。
- Abstract: Despite continuous progress in diagnosis and therapy, breast carcinoma (BC) remains a major health problem. Triple-negative (Estrogen Receptor-/Progesterone Receptor-/HER2-) breast cancer (TNBC) is the most aggressive subtype due to its high metastatic potential and resistance to chemotherapy. The Y-box binding protein 1 (YB-1) transcription factor, a protein present in both cytoplasm and nucleus, is a driver of TNB...
- Summary (fallback): 机器翻译摘要显示：尽管诊断和治疗不断取得进展，但乳腺癌（BC）仍然是一个主要的健康问题。三阴性（雌激素受体-/孕激素受体-/HER2-）乳腺癌（TNBC）因其高转移潜力和对化疗的耐药性而成为最具侵袭性的亚型。 Y 盒结合蛋白 1 (YB-1) 转录因子是一种存在于细胞质和细胞核中的蛋白质，是 TNBC 恶性肿瘤的驱动因素，因为它会刺激癌症干细胞表型并扰乱细胞周期进程。在这里，我们假设含有 YB-1 的 sEV 将 YB-1 递送到受体癌细胞的核区室，并在转移过程的激活中发挥重要作用。我们发现 MDA 和 4T1 细胞的 sEV 中 YB-1 选择性富集，通过 d-STORM，所有 sEV 中约 65% 和 50% 的 YB-1 呈阳性。
- Keywords: yb-1, nuclear, cancer, translocation, sevs

### 26. [精神疲劳会损害骑行耐力表现和努力感，但不会损害肌肉激活](https://www.biorxiv.org/content/10.64898/2026.03.19.712281v4)
- Original title: Mental fatigue impairs cycling endurance performance and perception of effort, but not muscle activation
- Authors: Souron, R., Sarcher, A., Lacourpaille, L., Boulahouche, I., Richier, C. et al.
- Meta: 2026-07-15 | physiology | DOI: 10.64898/2026.03.19.712281
- 中文摘要: 长时间从事认知要求高的任务会引起精神疲劳，并损害耐力表现。这种表现下降背后的神经心理生理机制尚不清楚，有人认为精神疲劳可能会扰乱运动命令，从而扰乱肌肉激活。我们旨在通过一项重复交叉设计研究来检验这一假设，其中 18 名参与者完成了两次实验，其中包括在 80% 峰值功率输出下进行任务时间故障循环测试。每个循环任务之前都有 1 小时的延长 Stroop 任务（Stroop 条件）或中性控制任务（控制条件）。使用以“一点也不疲劳”和“极度疲劳”为锚定的视觉模拟量表来评估精神疲劳。
- Abstract: Mental fatigue is induced by prolonged engagement in cognitively demanding tasks and impairs endurance performance. The neuropsychophysiological mechanisms underlying this decreased performance remain unclear, with suggestion that mental fatigue may disrupt motor command and consequently muscle activation. We aimed to test this hypothesis in a repeated cross-over design study in which 18 participants completed two e...
- Summary (fallback): 机器翻译摘要显示：长时间从事认知要求高的任务会引起精神疲劳，并损害耐力表现。这种表现下降背后的神经心理生理机制尚不清楚，有人认为精神疲劳可能会扰乱运动命令，从而扰乱肌肉激活。我们旨在通过一项重复交叉设计研究来检验这一假设，其中 18 名参与者完成了两次实验，其中包括在 80% 峰值功率输出下进行任务时间故障循环测试。每个循环任务之前都有 1 小时的延长 Stroop 任务（Stroop 条件）或中性控制任务（控制条件）。使用以“一点也不疲劳”和“极度疲劳”为锚定的视觉模拟量表来评估精神疲劳。
- Keywords: mental, fatigue, stroop, control, cycling

### 27. [EC1 体通过配子坑的形成控制精子细胞的接收。](https://www.biorxiv.org/content/10.64898/2026.07.14.738444v1)
- Original title: EC1 body controls sperm cell reception via gamete pit formation.
- Authors: Susaki, D., Oshirabe, H., Nagahara, S., Goto, Y., Oi, T. et al.
- Meta: 2026-07-15 | plant biology | DOI: 10.64898/2026.07.14.738444
- 中文摘要: 开花植物双受精的显着效率取决于将不动的精子细胞精确输送到两个雌配子。尽管精子细胞从花粉管中快速释放，但它们如何准确地定向到受精部位仍然未知。在这里，我们确定了一种短暂的细胞外结构，称为配子坑，它在花粉管排出后立即在卵细胞-中央细胞（EC-CC）界面处形成，并作为精子细胞的着陆位点。配子坑的形成是通过 EC-CC 界面的局部解离来实现的，由指定为 EC1 体的细胞外蛋白质组装体介导。这些结构含有富含 EGG CELL 1 (EC1) 肽的细胞外沉积物，包括淀粉样蛋白样组件。
- Abstract: The remarkable efficiency of double fertilization in flowering plants depends on the precise delivery of immotile sperm cells to two female gametes. Although sperm cells are rapidly released from the pollen tube, how they are accurately directed to their fertilization site has remained unknown. Here we identify a transient extracellular structure, termed the gamete pit, that forms at the egg cell-central cell (EC-CC...
- Summary (fallback): 机器翻译摘要显示：开花植物双受精的显着效率取决于将不动的精子细胞精确输送到两个雌配子。尽管精子细胞从花粉管中快速释放，但它们如何准确地定向到受精部位仍然未知。在这里，我们确定了一种短暂的细胞外结构，称为配子坑，它在花粉管排出后立即在卵细胞-中央细胞（EC-CC）界面处形成，并作为精子细胞的着陆位点。配子坑的形成是通过 EC-CC 界面的局部解离来实现的，由指定为 EC1 体的细胞外蛋白质组装体介导。这些结构含有富含 EGG CELL 1 (EC1) 肽的细胞外沉积物，包括淀粉样蛋白样组件。
- Keywords: gamete, sperm, cell, extracellular, formation

### 28. [对番茄 MAGIC 群体的多性状评估确定了氮利用效率 (NUE) 提高的有前途的品系](https://www.biorxiv.org/content/10.64898/2026.07.14.738388v1)
- Original title: Multi-trait evaluation of a tomato MAGIC population identifies promising lines with improved nitrogen use efficiency (NUE)
- Authors: Baraja-Fonseca, V., Gil-Villar, D., Bancic, J., Renau-Morata, B., Salud Justamante, M. et al.
- Meta: 2026-07-15 | plant biology | DOI: 10.64898/2026.07.14.738388
- 中文摘要: 氮利用效率 (NUE) 是番茄 (Solanum lycopersicum L.) 在氮投入减少的情况下维持产量的关键育种目标。在这里，我们利用最近开发的番茄多亲先进世代间杂交（ToMAGIC）群体来识别在氮利用率降低的情况下具有优异性能的品系。八个创始人和 118 个 ToMAGIC 品系的核心子集用 10,684 个 SNP 标记进行了表征，并在总计 1,576 株植物的实验中在最佳（opN，15 mM）和次优（subN，8 mM）氮供应下进行了评估，在 61 个表型变量中生成了 48,068 个数据点。在两种氮处理下，ToMAGIC品系在大多数性状上都表现出越行分离，证实了该群体作为未开发变异库的价值。
- Abstract: Nitrogen-use efficiency (NUE) is a pivotal breeding target in tomato (Solanum lycopersicum L.) to sustain production under reduced N inputs. Here, we leveraged a recently developed tomato multi-parent advanced generation inter-cross (ToMAGIC) population to identify lines with superior performance under reduced N availability. The eight founders and a core subset of 118 ToMAGIC lines were characterized with 10,684 SN...
- Summary (fallback): 机器翻译摘要显示：氮利用效率 (NUE) 是番茄 (Solanum lycopersicum L.) 在氮投入减少的情况下维持产量的关键育种目标。在这里，我们利用最近开发的番茄多亲先进世代间杂交（ToMAGIC）群体来识别在氮利用率降低的情况下具有优异性能的品系。八个创始人和 118 个 ToMAGIC 品系的核心子集用 10,684 个 SNP 标记进行了表征，并在总计 1,576 株植物的实验中在最佳（opN，15 mM）和次优（subN，8 mM）氮供应下进行了评估，在 61 个表型变量中生成了 48,068 个数据点。在两种氮处理下，ToMAGIC品系在大多数性状上都表现出越行分离，证实了该群体作为未开发变异库的价值。
- Keywords: lines, under, tomagic, traits, tomato

### 29. [反复出现的雌雄同体和性别偏向的 ABCDE 基因表达揭示了有梗橡树谱系中潜在的花可塑性 (Q.robur s.l.)](https://www.biorxiv.org/content/10.64898/2026.07.14.738412v1)
- Original title: Recurrent Hermaphroditism and Sex-Biased ABCDE Gene Expression Reveal Latent Floral Plasticity in the Pedunculate Oak Lineage (Q.robur s.l.)
- Authors: Afonso, H. R., Macedo, M., Azevedo, H., Vila-Vicosa, C., Costa, M. M. R.
- Meta: 2026-07-15 | plant biology | DOI: 10.64898/2026.07.14.738412
- 中文摘要: 背景与目的：单性花的发育依赖于花器官特性和性别决定的紧密协调。栎属通常被认为是严格雌雄同株的，在同一棵树上具有完全分离的雄花和雌花。然而，一些关于该属非典型开花的报告对这一规范观点提出了挑战，表明橡树的开花可能比传统假设的更加灵活。在这项工作中，研究了栎树花发育的动态，以将对比鲜明的花形态与不同的分子谱关联起来。方法：对几个个体和数年的 Q. orocantabrica 树的开花物候进行了密切监测，并对雄花、雌花和非典型花进行了详细的花形态分析。
- Abstract: Background and Aims: The development of unisexual flowers relies on the tight coordination of flower organ identity and sex determination. The genus Quercus is typically considered strictly monoecious, bearing fully segregated male and female flowers within the same individual tree. However, several reports of atypical flowering across the genus challenge this canonical view, suggesting that flowering in oaks may be...
- Summary (fallback): 机器翻译摘要显示：背景与目的：单性花的发育依赖于花器官特性和性别决定的紧密协调。栎属通常被认为是严格雌雄同株的，在同一棵树上具有完全分离的雄花和雌花。然而，一些关于该属非典型开花的报告对这一规范观点提出了挑战，表明橡树的开花可能比传统假设的更加灵活。在这项工作中，研究了栎树花发育的动态，以将对比鲜明的花形态与不同的分子谱关联起来。方法：对几个个体和数年的 Q. orocantabrica 树的开花物候进行了密切监测，并对雄花、雌花和非典型花进行了详细的花形态分析。
- Keywords: gene, expression, floral, flowers, flowering

### 30. [与双相情感障碍中躁狂到抑郁和抑郁到躁狂转变相关的转录组特征：使用诱导小胶质细胞样（iMG）细胞的病例报告](https://www.biorxiv.org/content/10.64898/2026.07.12.735946v1)
- Original title: Transcriptomic signatures associated with mania-to-depression and depression-to-mania transitions in bipolar disorder: a case report using induced microglia-like (iMG) cells
- Authors: Inamine, S., Kyuragi, S., Ohgidani, M., Kimura, T., Inoue, I. et al.
- Meta: 2026-07-15 | neuroscience | DOI: 10.64898/2026.07.12.735946
- 中文摘要: 简介 双相情感障碍 (BD) 的特点是反复发作的躁狂和抑郁。尽管进行了大量研究，但这些情绪波动背后的病理生理学仍然难以捉摸。新出现的证据表明神经炎症和小胶质细胞激活在 BD 的病理生理学中具有潜在作用。方法 我们采用逆翻译方法，从一名 BD 患者的外周血单核细胞中直接生成诱导型小胶质细胞样 (iMG) 细胞，并在抑郁、躁狂和随后的抑郁阶段重复取样。在每个时间点对 iMG 细胞进行 RNA 测序，以确定与情绪状态转变相关的差异表达基因。
- Abstract: Introduction Bipolar disorder (BD) is characterized by recurring episodes of mania and depression. Despite extensive research, the pathophysiology underlying these mood swings remains elusive. Emerging evidence indicates a potential role for neuroinflammation and microglial activation in the pathophysiology of BD. Methods We employed a reverse-translational approach to generate directly induced microglia-like (iMG)...
- Summary (fallback): 机器翻译摘要显示：简介 双相情感障碍 (BD) 的特点是反复发作的躁狂和抑郁。尽管进行了大量研究，但这些情绪波动背后的病理生理学仍然难以捉摸。新出现的证据表明神经炎症和小胶质细胞激活在 BD 的病理生理学中具有潜在作用。方法 我们采用逆翻译方法，从一名 BD 患者的外周血单核细胞中直接生成诱导型小胶质细胞样 (iMG) 细胞，并在抑郁、躁狂和随后的抑郁阶段重复取样。在每个时间点对 iMG 细胞进行 RNA 测序，以确定与情绪状态转变相关的差异表达基因。
- Keywords: genes, mood, gene, depression-to-mania, transitions

## medrxiv

### 1. [麻疹疫苗接种后不提供加强白喉-破伤风-百日咳 (DTP) 疫苗接种和儿童生存的随机试验：一项失败的试验](https://www.medrxiv.org/content/10.1101/2025.10.29.25339081v2)
- Original title: Randomised trial of not providing booster diphtheria-tetanus-pertussis (DTP) vaccination after measles vaccination and child survival: A failed trial
- Authors: Agergaard, J., Nielsen, S., Benn, C. S., Aaby, P.
- Meta: 2026-07-15 | epidemiology | DOI: 10.1101/2025.10.29.25339081
- 中文摘要: 摘要 背景 在低收入环境中，世卫组织建议在 18 个月大时注射加强剂量的 DTP (DTP4) 和 OPV (OPV4)。先前的研究发现 MV 后的 DTP 与较高的女性死亡率相关。我们在几内亚比绍进行了一项随机试验 (RCT)，其中 18 个月大的儿童被随机分配接受 DTP4+OPV4 与仅接受 OPV4 治疗，以评估总体和按性别对生存和住院治疗的影响。方法 试验于2005-2012年进行。儿童被随机分组​​并从 18 个月到 4 岁进行随访。通过主要儿科病房的监测系统记录住院情况，通过研究区域的人口监测系统以及每年对研究参与者的家访发现死亡情况。在 Cox 比例风险模型中对数据进行分析，以年龄为基础时间尺度。
- Abstract: ABSTRACT Background In low-income settings, WHO recommended a booster-dose of DTP (DTP4) and OPV (OPV4) at 18 months of age. Previous studies found DTP after MV to be associated with higher female mortality. We conducted a randomised trial (RCTs) in Guinea-Bissau, in which children from 18 months of age were randomised to receive DTP4+OPV4 vs OPV4-only to assess the impact on survival and hospitalisations, overall a...
- Summary (fallback): 机器翻译摘要显示：摘要 背景 在低收入环境中，世卫组织建议在 18 个月大时注射加强剂量的 DTP (DTP4) 和 OPV (OPV4)。先前的研究发现 MV 后的 DTP 与较高的女性死亡率相关。我们在几内亚比绍进行了一项随机试验 (RCT)，其中 18 个月大的儿童被随机分配接受 DTP4+OPV4 与仅接受 OPV4 治疗，以评估总体和按性别对生存和住院治疗的影响。方法 试验于2005-2012年进行。儿童被随机分组​​并从 18 个月到 4 岁进行随访。通过主要儿科病房的监测系统记录住院情况，通过研究区域的人口监测系统以及每年对研究参与者的家访发现死亡情况。在 Cox 比例风险模型中对数据进行分析，以年龄为基础时间尺度。
- Keywords: trial, dtp4, opv4, randomised, mortality

### 2. [肠道微生物群与内化精神病理学之间共享的宿主遗传结构](https://www.medrxiv.org/content/10.64898/2026.05.31.26354553v2)
- Original title: Shared host-genetic architecture between gut microbiota and internalizing psychopathology
- Authors: Velez-Pardo, P., Solano, R. J., Quinchia-Figueroa, A. M., Montoya Monsalve, R., Moratto-Vasquez, N. S.
- Meta: 2026-07-15 | psychiatry and clinical psychology | DOI: 10.64898/2026.05.31.26354553
- 中文摘要: 肠道微生物组成是否与精神疾病存在因果关系，或者仅仅与之相关，仍然悬而未决。使用遗传变异作为自然工具（孟德尔随机化，MR），我们使用最大的可用全基因组关联研究，测试了 211 个肠道微生物类群对 9 种精神病学和精神病理学相关表型的遗传预测影响。在 1,898 项有效测试中，7 个分类单元结果关联通过了错误发现率校正（FDR < 0.05），并且全部属于内化谱（抑郁、神经质和失眠），而不是双相情感障碍或精神分裂症；它们包括 Mollicutes/Tenericutes 分支与抑郁症的保护性关联（β = -0.073，p = 1.5e-6）和 Butyrivibrio 与神经质的保护性关联，以及 Betaproteobacteria 与神经质的有害关联。
- Abstract: Whether gut microbial composition is causally linked to mental illness, or merely correlated with it, remains unresolved. Using genetic variants as natural instruments (Mendelian randomization, MR), we tested the genetically predicted effects of 211 gut microbial taxa on nine psychiatric and psychopathology-related phenotypes, using the largest available genome-wide association studies. Across 1,898 valid tests, sev...
- Summary (fallback): 机器翻译摘要显示：肠道微生物组成是否与精神疾病存在因果关系，或者仅仅与之相关，仍然悬而未决。使用遗传变异作为自然工具（孟德尔随机化，MR），我们使用最大的可用全基因组关联研究，测试了 211 个肠道微生物类群对 9 种精神病学和精神病理学相关表型的遗传预测影响。在 1,898 项有效测试中，7 个分类单元结果关联通过了错误发现率校正（FDR < 0.05），并且全部属于内化谱（抑郁、神经质和失眠），而不是双相情感障碍或精神分裂症；它们包括 Mollicutes/Tenericutes 分支与抑郁症的保护性关联（β = -0.073，p = 1.5e-6）和 Butyrivibrio 与神经质的保护性关联，以及 Betaproteobacteria 与神经质的有害关联。
- Keywords: internalizing, causal, psychopathology, microbial, taxa

### 3. [源自欧洲的冠状动脉疾病多基因评分过度标记了越南和东南亚人群的遗传风险：1000 个基因组的多评分分析](https://www.medrxiv.org/content/10.64898/2026.07.10.26357796v1)
- Original title: European-derived coronary artery disease polygenic scores over-flag genetic risk in Vietnamese and Southeast Asian populations: a multi-score analysis in 1000 Genomes
- Authors: Hoang, Q. P., Le, T. X., Doan, D. D.
- Meta: 2026-07-15 | genetic and genomic medicine | DOI: 10.64898/2026.07.10.26357796
- 中文摘要: 背景。冠状动脉疾病 (CAD) 的多基因评分 (PRS) 几乎完全来自欧洲血统数据。当分数与风险阈值一起使用时，它们对包括越南人在内的东南亚人群的可移植性在很大程度上是未知的，并且在临床上具有重要意义。方法。我们评估了来自 1000 名基因组计划的 2,504 名个体的 PGS 目录中的四个独立的欧洲衍生 CAD 评分（PGS000058、PGS000349、PGS002809、PGS004198；70 - 5,723 个变体），重点关注越南 Kinh (KHV) 和 Dai (CDX) 样本。使用 PLINK2 计算每个人的分数并进行标准化。我们评估了 (i) 跨血统分布（校准）和 (ii) 临床相关结果：当应用欧洲前 20% 阈值（如果完全校准，则为 20%）时，每个人群标记为高遗传风险的比例。结果。
- Abstract: Background. Polygenic scores (PRS) for coronary artery disease (CAD) are derived almost entirely from European-ancestry data. Their portability to Southeast Asian populations, including the Vietnamese, is largely uncharacterised and clinically consequential when scores are used with risk thresholds. Methods. We evaluated four independent European-derived CAD scores from the PGS Catalog (PGS000058, PGS000349, PGS0028...
- Summary (fallback): 机器翻译摘要显示：背景。冠状动脉疾病 (CAD) 的多基因评分 (PRS) 几乎完全来自欧洲血统数据。当分数与风险阈值一起使用时，它们对包括越南人在内的东南亚人群的可移植性在很大程度上是未知的，并且在临床上具有重要意义。方法。我们评估了来自 1000 名基因组计划的 2,504 名个体的 PGS 目录中的四个独立的欧洲衍生 CAD 评分（PGS000058、PGS000349、PGS002809、PGS004198；70 - 5,723 个变体），重点关注越南 Kinh (KHV) 和 Dai (CDX) 样本。使用 PLINK2 计算每个人的分数并进行标准化。我们评估了 (i) 跨血统分布（校准）和 (ii) 临床相关结果：当应用欧洲前 20% 阈值（如果完全校准，则为 20%）时，每个人群标记为高遗传风险的比例。结果。
- Keywords: scores, vietnamese, risk, southeast, european

### 4. [超越强度：时间面部动作单元动态的跨数据集一致性作为抑郁症的可转移标记](https://www.medrxiv.org/content/10.64898/2026.07.12.26357331v2)
- Original title: Beyond Intensity: Cross-Dataset Consistency of Temporal Facial Action-Unit Dynamics as Transferable Markers of Depression
- Authors: Jeong, I., Jang, M., Kim, J.-w., Kim, H., Park, S. et al.
- Meta: 2026-07-15 | health informatics | DOI: 10.64898/2026.07.12.26357331
- 中文摘要: 面部行为是抑郁症状分析中广泛研究的客观信号，但大多数系统都是在单个数据集中进行训练和评估的，因此不清楚学习到的表征是否反映了抑郁症或数据集特定的伪影。之前的工作也很大程度上依赖于总体强度统计数据和小样本。我们通过询问哪些面部动作单元（AU）特征跨数据集转移来重新构建问题，而不是最大化数据集内的歧视。在由 2,608 名参与者组成的韩国队列中使用时间分辨的 AU 动态，其中包括 265 名具有 PHQ-9 定义的抑郁症状的参与者，在快乐和不快乐的情绪引发条件下记录，询问哪些 AU 特征在数据集中转移，而不是哪些最大化数据集内的歧视。
- Abstract: Facial behavior is a widely studied objective signal for depressive-symptom analysis, yet most systems are trained and evaluated within a single dataset, leaving it unclear whether the learned representations reflect depression or dataset-specific artifacts. Prior work has also relied largely on aggregate intensity statistics and on small samples. We reframe the problem by asking which facial action unit (AU) featur...
- Summary (fallback): 机器翻译摘要显示：面部行为是抑郁症状分析中广泛研究的客观信号，但大多数系统都是在单个数据集中进行训练和评估的，因此不清楚学习到的表征是否反映了抑郁症或数据集特定的伪影。之前的工作也很大程度上依赖于总体强度统计数据和小样本。我们通过询问哪些面部动作单元（AU）特征跨数据集转移来重新构建问题，而不是最大化数据集内的歧视。在由 2,608 名参与者组成的韩国队列中使用时间分辨的 AU 动态，其中包括 265 名具有 PHQ-9 定义的抑郁症状的参与者，在快乐和不快乐的情绪引发条件下记录，询问哪些 AU 特征在数据集中转移，而不是哪些最大化数据集内的歧视。
- Keywords: which, features, intensity, temporal, facial

### 5. [德克萨斯州乳腺 X 光检查的普及、城市化和晚期乳腺癌负担：贝叶斯空间分析](https://www.medrxiv.org/content/10.64898/2026.07.11.26357817v1)
- Original title: Mammography Access, Urbanicity, and Late-Stage Breast Cancer Burden Across Texas: A Bayesian Spatial Analysis
- Authors: Gao, J., Zhang, Y., Tian, J., Ferguson, G. M., Griffin, B. C. et al.
- Meta: 2026-07-15 | health policy | DOI: 10.64898/2026.07.11.26357817
- 中文摘要: 背景 在获得预防性医疗服务方面的地理差异仍然是美国乳腺癌不平等的一个重要因素。乳房X光检查在早期发现和提高生存率方面发挥着关键作用；然而，筛查基础设施和医疗保健可及性在许多地区仍然分布不均，特别是在德克萨斯州等社会经济多元化的大州。了解乳房X光检查的获取、城市化、社会经济脆弱性和晚期乳腺癌负担之间的空间关系对于制定有针对性的地理公共卫生干预措施非常重要。
- Abstract: Background Geographic disparities in access to preventive healthcare services remain an important contributor to breast cancer inequities in the United States. Mammography screening plays a critical role in early detection and improved survival; however, screening infrastructure and healthcare accessibility remain unevenly distributed across many regions, particularly within large and socioeconomically diverse state...
- Summary (fallback): 机器翻译摘要显示：背景 在获得预防性医疗服务方面的地理差异仍然是美国乳腺癌不平等的一个重要因素。乳房X光检查在早期发现和提高生存率方面发挥着关键作用；然而，筛查基础设施和医疗保健可及性在许多地区仍然分布不均，特别是在德克萨斯州等社会经济多元化的大州。了解乳房X光检查的获取、城市化、社会经济脆弱性和晚期乳腺癌负担之间的空间关系对于制定有针对性的地理公共卫生干预措施非常重要。
- Keywords: cancer, burden, spatial, breast, mammography

### 6. [乙酸是一种纤维衍生的肠道代谢物，可降低更年期早期女性的心血管疾病风险](https://www.medrxiv.org/content/10.64898/2026.02.10.26346040v2)
- Original title: Acetate, a fibre-derived gut metabolite, is associated with reduced cardiovascular disease risk in females with early menopause
- Authors: Yang, C., BioBank Japan Project,, Namba, S., Matsuda, K., Okada, Y. et al.
- Meta: 2026-07-15 | cardiovascular medicine | DOI: 10.64898/2026.02.10.26346040
- 中文摘要: 背景和目的：雌激素缺乏和睾酮过多会显着增加女性心血管疾病的风险。膳食纤维及其微生物副产物短链脂肪酸具有心脏保护作用。我们的目的是研究血浆醋酸盐（最丰富的短链脂肪酸）是否与性激素谱改变的女性心血管结局的改善相关。方法：这项队列研究纳入了来自英国生物银行和日本生物银行的 105,563 名女性参与者，并进行了长达 10 年的随访。主要结局是与早期绝经（雌激素不足的替代）和血浆游离睾酮相关的主要不良心血管事件（MACE）。蛋白质组学分析探索了潜在的分子途径。结果：在英国生物银行中，较高的血浆醋酸盐与较低的 10 年 MACE 发生率相关（HR=0.887，p=0.002）。
- Abstract: Background and Aims: Estrogen deficiency and testosterone excess substantially increase cardiovascular disease risk in females. Dietary fibre and its microbial by-products, short-chain fatty acids, have cardioprotective effects. We aim to investigate whether plasma acetate - the most abundant short-chain fatty acid - is associated with improved cardiovascular outcomes in females with altered sex hormone profiles. Me...
- Summary (fallback): 机器翻译摘要显示：背景和目的：雌激素缺乏和睾酮过多会显着增加女性心血管疾病的风险。膳食纤维及其微生物副产物短链脂肪酸具有心脏保护作用。我们的目的是研究血浆醋酸盐（最丰富的短链脂肪酸）是否与性激素谱改变的女性心血管结局的改善相关。方法：这项队列研究纳入了来自英国生物银行和日本生物银行的 105,563 名女性参与者，并进行了长达 10 年的随访。主要结局是与早期绝经（雌激素不足的替代）和血浆游离睾酮相关的主要不良心血管事件（MACE）。蛋白质组学分析探索了潜在的分子途径。结果：在英国生物银行中，较高的血浆醋酸盐与较低的 10 年 MACE 发生率相关（HR=0.887，p=0.002）。
- Keywords: acetate, early, risk, menopause, mace

### 7. [TAC/SARIFA 在结直肠双癌和三癌中与宿主相关的一致性表明患者特异性代谢重编程](https://www.medrxiv.org/content/10.64898/2026.07.12.26357852v2)
- Original title: Host-related concordance of TAC/SARIFA in colorectal double and triple carcinomas suggests patient-specific metabolic reprogramming
- Authors: Farfan Lopez, F. J., Wiegering, A., Maerkl, B., Waidhauser, J., Krebs, M. et al.
- Meta: 2026-07-15 | pathology | DOI: 10.64898/2026.07.12.26357852
- 中文摘要: 介绍。 TAC/SARIFA 已作为一种新的强大且易于评估的生物标志物被引入包括结直肠癌在内的多种癌症实体中。它的定义是至少五个肿瘤细胞和一个脂肪细胞之间的直接接触，并被认为表明与不良结果相关的代谢重编程。然而，导致 TAC/SARIFA 阳性的机制仍不清楚。为了调查是否存在个体成分，我们对双重和三重癌症进行了一项研究，建立了患者内部设计。方法。我们回顾性分析了来自两个学术医疗中心的 135 例 276 例结直肠癌病例。评估 TAC/SARIFA 状态以及基本组织病理学因素。中位随访时间为 120 个月。结果。任何 TAC/SARIFA 阳性肿瘤的病例显示总生存率显着降低（62 比 10）。
- Abstract: Introduction. TAC/SARIFA has been introduced as a new robust and easy-to-evaluate biomarker in several cancer entities, including colorectal cancer. It is defined by direct contact between at least five tumour cells and one adipocyte and is believed to indicate metabolic reprogramming associated with adverse outcome. However, the mechanism that leads to TAC/SARIFA positivity remains unclear. To investigate whether t...
- Summary (fallback): 机器翻译摘要显示：介绍。 TAC/SARIFA 已作为一种新的强大且易于评估的生物标志物被引入包括结直肠癌在内的多种癌症实体中。它的定义是至少五个肿瘤细胞和一个脂肪细胞之间的直接接触，并被认为表明与不良结果相关的代谢重编程。然而，导致 TAC/SARIFA 阳性的机制仍不清楚。为了调查是否存在个体成分，我们对双重和三重癌症进行了一项研究，建立了患者内部设计。方法。我们回顾性分析了来自两个学术医疗中心的 135 例 276 例结直肠癌病例。评估 TAC/SARIFA 状态以及基本组织病理学因素。中位随访时间为 120 个月。结果。任何 TAC/SARIFA 阳性肿瘤的病例显示总生存率显着降低（62 比 10）。
- Keywords: sarifa, colorectal, cases, double, triple

### 8. [FreqFuseNet：解决薄壁头颈 OAR 分割双频融合中的特征尺度不匹配问题](https://www.medrxiv.org/content/10.64898/2026.07.09.26357642v2)
- Original title: FreqFuseNet: Resolving Feature-Scale Mismatch in Dual-Frequency Fusion for Thin-Wall Head-and-Neck OAR Segmentation
- Authors: Chen, W.-Y., Wan, S.-Y., Lin, G.-Y.
- Meta: 2026-07-15 | radiology and imaging | DOI: 10.64898/2026.07.09.26357642
- 中文摘要: 薄壁危险器官 (OAR)（耳蜗、前庭半规管、内听道、鼓室和中耳）的准确分割在临床上与头颈放射治疗计划相关，但这些小型薄壁结构仍然是自动描绘最具挑战性的目标之一。双频特征融合是边界敏感表示的一个有前途的方向，但在研究的 FP16 FFT-FcaNet 设置下，我们观察到 FFT 和 FcaNet 分支之间大约 863 倍的激活尺度不匹配，导致标称 5% 的残差系数表现为大约 43 倍的主导项。
- Abstract: Accurate segmentation of thin-wall organs-at-risk (OARs)-the cochlea, vestibular semicircular canals, internal auditory canal, tympanic cavity, and middle ear-is clinically relevant for head-and-neck radiotherapy planning, yet these small, thin-wall structures remain among the most challenging targets for automated delineation. Dual-frequency feature fusion is a promising direction for boundary-sensitive representat...
- Summary (fallback): 机器翻译摘要显示：薄壁危险器官 (OAR)（耳蜗、前庭半规管、内听道、鼓室和中耳）的准确分割在临床上与头颈放射治疗计划相关，但这些小型薄壁结构仍然是自动描绘最具挑战性的目标之一。双频特征融合是边界敏感表示的一个有前途的方向，但在研究的 FP16 FFT-FcaNet 设置下，我们观察到 FFT 和 FcaNet 分支之间大约 863 倍的激活尺度不匹配，导致标称 5% 的残差系数表现为大约 43 倍的主导项。
- Keywords: freqfusenet, thin-wall, mismatch, head-and-neck, coefficient
