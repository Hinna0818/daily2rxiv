# daily2rxiv Digest - 2026-07-20

共收录 82 篇论文。

## arxiv

### 1. [PagedWeight：高效的 MoE LLM 服务，具有动态质量感知权重量化](https://arxiv.org/abs/2607.16184v1)
- Original title: PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization
- Authors: Yuchen Yang, Yifan Zhao, Anisha Dasgupta, Sasa Misailovic
- Meta: 2026-07-17 | cs.LG
- 中文摘要: Mixture-of-Experts (MoE) 是一类流行的大型语言模型 (LLM)，提供高效率和准确性。然而，在 KV 缓存密集型服务场景中，MoE 经常表现出模型权重的 GPU 内存需求与不断增长的 KV 缓存之间的紧张关系。我们提出了 PagedWeight，一种用于 MoE LLM 服务的新颖管理方法，可在运行时动态量化 MoE 模型的权重，并平衡专家权重精度与 KV 缓存大小。 PagedWeight 公开并有效地处理模型任务准确性、内存消耗和吞吐量/延迟之间的复杂权衡。在多个内存敏感的 MoE 服务场景中，PagedWeight 改进了多个现有量化基线的质量与内存权衡。
- Abstract: Mixture-of-Experts (MoE) is a popular class of large language models (LLMs), offering high efficiency and accuracy. However, in KV-cache-intensive serving scenarios, MoEs often exhibit a tension between the GPU memory requirements of the model weights and the growing KV cache. We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model's weights at runtime and balances...
- Summary (fallback): 机器翻译摘要显示：Mixture-of-Experts (MoE) 是一类流行的大型语言模型 (LLM)，提供高效率和准确性。然而，在 KV 缓存密集型服务场景中，MoE 经常表现出模型权重的 GPU 内存需求与不断增长的 KV 缓存之间的紧张关系。我们提出了 PagedWeight，一种用于 MoE LLM 服务的新颖管理方法，可在运行时动态量化 MoE 模型的权重，并平衡专家权重精度与 KV 缓存大小。 PagedWeight 公开并有效地处理模型任务准确性、内存消耗和吞吐量/延迟之间的复杂权衡。在多个内存敏感的 MoE 服务场景中，PagedWeight 改进了多个现有量化基线的质量与内存权衡。
- Keywords: pagedweight, serving, memory, quantization, accuracy

### 2. [基于平衡的可微分连续变量热力学计算的蓝图](https://arxiv.org/abs/2607.16183v1)
- Original title: A Blueprint for Equilibrium-Based Differentiable Continuous-Variable Thermodynamic Computing
- Authors: Owen Lockwood, Jérémy Béjanin, Joost Bus, Christopher Chamberland, Patrick Huembeli et al.
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 为了解决机器学习工作负载不断增长的能源和延迟需求，我们引入了一个节能且快速的热力学计算堆栈的蓝图，该堆栈利用物理硬件中的随机模拟过程。在这项工作中，我们专注于基于能量的热力学计算，其中随机过程由具有可调能量势的朗之万动力学很好地描述。在物理硬件中实现这种潜力使我们能够从基本的参数化基于能量的模型中生成和采样。我们演示了如何使用概率图模型框架构建和训练基于这些硬件本机基于能量的模型的流行机器学习模型。我们根据理论考虑和数值研究分析了这种热力学范式中不同模型的运行时间和能耗。
- Abstract: To address the escalating energy and latency demands of machine-learning workloads, we introduce a blueprint for an energy-efficient and fast thermodynamic computing stack that leverages stochastic analog processes in physical hardware. In this work, we focus on energy-based thermodynamic computing where the stochastic process is well described by Langevin dynamics with tunable energy potentials. The implementation...
- Summary (fallback): 机器翻译摘要显示：为了解决机器学习工作负载不断增长的能源和延迟需求，我们引入了一个节能且快速的热力学计算堆栈的蓝图，该堆栈利用物理硬件中的随机模拟过程。在这项工作中，我们专注于基于能量的热力学计算，其中随机过程由具有可调能量势的朗之万动力学很好地描述。在物理硬件中实现这种潜力使我们能够从基本的参数化基于能量的模型中生成和采样。我们演示了如何使用概率图模型框架构建和训练基于这些硬件本机基于能量的模型的流行机器学习模型。我们根据理论考虑和数值研究分析了这种热力学范式中不同模型的运行时间和能耗。
- Keywords: thermodynamic, models, hardware, computing, energy

### 3. [通过拉普拉斯最优传输进行集群感知匹配](https://arxiv.org/abs/2607.16178v1)
- Original title: Cluster-Aware Matching via Laplacian Optimal Transport
- Authors: Gabriel Samberg, YoonHaeng Hur, Yuehaw Khoo, Nir Sharon
- Meta: 2026-07-17 | stat.ML
- 中文摘要: 在许多匹配应用中，要匹配的点云不仅仅是非结构化的点集，而是来自具有内在簇结构的分布的样本。在这种情况下，由于各个点在相干区域内通常是可互换的，因此找到稳健的区域到区域对齐比建立精确的点到点对应关系更可取。为此，我们提出了一种基于拉普拉斯最优传输（LapOT）的聚类感知匹配的新方法。关键思想是使用由点云相似图构造的二次拉普拉斯项来规范最优传输问题，这鼓励最优耦合以尊重两个点集的簇结构。
- Abstract: In many applications of matching, the point clouds to be matched are not merely unstructured sets of points but rather samples from distributions with an intrinsic cluster structure. In such cases, as individual points are often interchangeable within a coherent region, finding a robust region-to-region alignment is more desirable than establishing a precise point-to-point correspondence. To this end, we propose a n...
- Summary (fallback): 机器翻译摘要显示：在许多匹配应用中，要匹配的点云不仅仅是非结构化的点集，而是来自具有内在簇结构的分布的样本。在这种情况下，由于各个点在相干区域内通常是可互换的，因此找到稳健的区域到区域对齐比建立精确的点到点对应关系更可取。为此，我们提出了一种基于拉普拉斯最优传输（LapOT）的聚类感知匹配的新方法。关键思想是使用由点云相似图构造的二次拉普拉斯项来规范最优传输问题，这鼓励最优耦合以尊重两个点集的簇结构。
- Keywords: point, cluster-aware, matching, optimal, laplacian

### 4. [用于动态系统实时最优控制的物理增强强化学习](https://arxiv.org/abs/2607.16177v1)
- Original title: Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems
- Authors: Matteo Tomasetto, Nicolò Botteghi, Gabriele Bruni, Andrea Manzoni
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 强化学习（RL）最近已成为非线性和复杂动力系统的一种有前途的反馈控制策略。然而，强化学习算法样本效率低下，需要与环境进行大量交互才能合成最优控制策略。因此，由于高维空间中的探索-利用困境所带来的维数灾难，强化学习的应用通常仅限于稀疏传感器和执行器。在这项工作中，我们将强化学习和传统动力系统最优控制与一种新颖的物理增强强化学习（PEARL）范式结合起来，该范式专为高维和参数动力系统的控制而设计，利用了它们动力学的差异性。
- Abstract: Reinforcement learning (RL) has recently emerged as a promising feedback control strategy for nonlinear and complex dynamical systems. However, RL algorithms are sample inefficient and require a large number of interaction with the environment to synthesize optimal control strategies. Consequently, applications of RL are typically limited to sparse sensors and actuators due to the curse of dimensionality entailed by...
- Summary (fallback): 机器翻译摘要显示：强化学习（RL）最近已成为非线性和复杂动力系统的一种有前途的反馈控制策略。然而，强化学习算法样本效率低下，需要与环境进行大量交互才能合成最优控制策略。因此，由于高维空间中的探索-利用困境所带来的维数灾难，强化学习的应用通常仅限于稀疏传感器和执行器。在这项工作中，我们将强化学习和传统动力系统最优控制与一种新颖的物理增强强化学习（PEARL）范式结合起来，该范式专为高维和参数动力系统的控制而设计，利用了它们动力学的差异性。
- Keywords: control, learning, dynamical, systems, reinforcement

### 5. [Muon何时有助于代理强化学习？](https://arxiv.org/abs/2607.16169v1)
- Original title: When Does Muon Help Agentic Reinforcement Learning?
- Authors: Kai Ruan, Jinghao Lin, Zihe Huang, Ziqi Zhou, Qianshan Wei et al.
- Meta: 2026-07-17 | cs.LG
- 中文摘要: Muon 在大规模预训练方面与 AdamW 具有竞争力，但其对于强化学习（RL）训练后的价值仍不清楚。我们通过使用 Qwen2.5-0.5B-Instruct 在 ALFWorld 上与 AdamW 进行匹配单种子比较来研究稀疏奖励代理强化学习中的普通 Muon。在组中组策略优化 (GiGPO) 下，仅将 Muon 应用于隐藏权重矩阵可将最终窗口验证成功率从 0.290 提高到 0.546 (+88%)；高速率 AdamW 控件不会保留更新后的成功。效果取决于优势估计器和学习率。在 3e-5 时，Muon 将 GRPO 从 0.161 提高到 0.268，而 GraphGPO 的后期窗口差距缩小到接近饱和。在 1e-5 时，GraphGPO Muon 达到 0.901，将标准化验证 AUC 从 0.399 提高到 0.556，并且在 30 次更新和 60 次更新之前分别达到 0.5 和 0.75 成功。
- Abstract: Muon is competitive with AdamW in large-scale pre-training, but its value for reinforcement-learning (RL) post-training remains unclear. We study vanilla Muon in sparse-reward agentic RL through matched single-seed comparisons with AdamW on ALFWorld using Qwen2.5-0.5B-Instruct. Under Group-in-Group Policy Optimization (GiGPO), applying Muon only to hidden weight matrices raises final-window validation success from 0...
- Summary (fallback): 机器翻译摘要显示：Muon 在大规模预训练方面与 AdamW 具有竞争力，但其对于强化学习（RL）训练后的价值仍不清楚。我们通过使用 Qwen2.5-0.5B-Instruct 在 ALFWorld 上与 AdamW 进行匹配单种子比较来研究稀疏奖励代理强化学习中的普通 Muon。在组中组策略优化 (GiGPO) 下，仅将 Muon 应用于隐藏权重矩阵可将最终窗口验证成功率从 0.290 提高到 0.546 (+88%)；高速率 AdamW 控件不会保留更新后的成功。效果取决于优势估计器和学习率。在 3e-5 时，Muon 将 GRPO 从 0.161 提高到 0.268，而 GraphGPO 的后期窗口差距缩小到接近饱和。在 1e-5 时，GraphGPO Muon 达到 0.901，将标准化验证 AUC 从 0.399 提...
- Keywords: muon, agentic, learning, adamw, validation

### 6. [用于自适应住宅短期负荷预测的行为条件神经过程](https://arxiv.org/abs/2607.16168v1)
- Original title: Behaviour-Conditioned Neural Processes for Adaptive Residential Short-Term Load Forecasting
- Authors: Ramin Soleimani, Andrea Visentin, Dirk Pesch
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 住宅短期负荷预测（STLF）具有挑战性，因为家庭需求是异质的、随时间变化的，并且由不同的行为习惯决定。这项工作研究了推断的行为结构是否可以嵌入基于神经过程的概率模型的预测机制中，而不是仅用作上下文条件住宅 STLF 的外部分组信号。我们提出了一个以行为为条件的注意力神经过程框架，将每个负载曲线视为预测任务。行为结构由从可用上下文推断的离散潜在变量表示，并用于行为条件解码器调节，而连续潜在变量捕获跨异构配置文件的共享功能不确定性。
- Abstract: Residential short-term load forecasting (STLF) is challenging because household demand is heterogeneous, temporally variable, and shaped by diverse behavioural routines. This work investigates whether inferred behavioural structure can be embedded within the forecasting mechanism of a Neural Process-based probabilistic model, rather than used only as an external grouping signal, for context-conditioned residential S...
- Summary (fallback): 机器翻译摘要显示：住宅短期负荷预测（STLF）具有挑战性，因为家庭需求是异质的、随时间变化的，并且由不同的行为习惯决定。这项工作研究了推断的行为结构是否可以嵌入基于神经过程的概率模型的预测机制中，而不是仅用作上下文条件住宅 STLF 的外部分组信号。我们提出了一个以行为为条件的注意力神经过程框架，将每个负载曲线视为预测任务。行为结构由从可用上下文推断的离散潜在变量表示，并用于行为条件解码器调节，而连续潜在变量捕获跨异构配置文件的共享功能不确定性。
- Keywords: forecasting, heterogeneous, variable, behavioural, context

### 7. [积极观察者的考试](https://arxiv.org/abs/2607.16165v1)
- Original title: An Exam for Active Observers
- Authors: Jiarui Zhang, Muzi Tao, Shangshang Wang, Ollie Liu, Xuezhe Ma et al.
- Meta: 2026-07-17 | cs.CV
- 中文摘要: 人类视觉是一个闭环：视线不断地被中间假设而不是单个快照重定向。数十年的心理物理学和认知科学认为，这种主动观察对于许多任务来说都是必不可少的。当今的多模态大语言模型（MLLM）是否进行主动观察是一个实证问题，当前的视觉语言基准无法回答。我们推出了 ActiveVision，这是一个可以衡量 MLLM 主动观察的基准，包含 3 个类别的 17 项任务。任务旨在强制重复的视觉感知，而不是单一的静态描述。
- Abstract: Human vision is a closed loop: gaze is continuously redirected by intermediate hypotheses rather than a single snapshot. Decades of psychophysics and cognitive science have argued that this active observation is essential for a wide range of tasks. Whether today's multimodal large language models (MLLMs) exercise active observation is an empirical question that current vision-language benchmarks do not answer. We in...
- Summary (fallback): 机器翻译摘要显示：人类视觉是一个闭环：视线不断地被中间假设而不是单个快照重定向。数十年的心理物理学和认知科学认为，这种主动观察对于许多任务来说都是必不可少的。当今的多模态大语言模型（MLLM）是否进行主动观察是一个实证问题，当前的视觉语言基准无法回答。我们推出了 ActiveVision，这是一个可以衡量 MLLM 主动观察的基准，包含 3 个类别的 17 项任务。任务旨在强制重复的视觉感知，而不是单一的静态描述。
- Keywords: active, observation, tasks, mllms, models

### 8. [PRISA：用于交叉口安全评估的主动基础设施 LiDAR 框架](https://arxiv.org/abs/2607.16156v1)
- Original title: PRISA: Proactive Infrastructure LiDAR Framework for Intersection Safety Assessment
- Authors: Tam Bang, Hussam Abubakr, Emiliano de la Garza Villarreal, Truc Phuong Nguyen, Austin Harris et al.
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 城市十字路口是道路网络中最危险的地点之一，对车辆和行人和骑自行车者等弱势道路使用者 (VRU) 构成重大风险。多代理交互的复杂性要求连续、实时的监控系统能够在冲突升级为崩溃之前预测冲突。我们推出 PRISA，这是一种模块化基础设施 LiDAR 框架，利用隐私保护、低光鲁棒性路边传感器进行长期交通观察和边缘实时风险检测。该框架包括两个核心组件：传感和感知层以及即插即用的风险评估模块。后者自动从累积的感知输出中整理特定地点的训练数据，以训练轨迹预测模型，而无需手动注释。
- Abstract: Urban intersections are among the most hazardous locations in road networks, posing significant risks to vehicles and vulnerable road users (VRUs) such as pedestrians and cyclists. The complexity of multi-agent interactions demands continuous, real-time monitoring systems capable of anticipating conflicts before they escalate into crashes. We present PRISA, a modular infrastructure LiDAR framework leveraging privacy...
- Summary (fallback): 机器翻译摘要显示：城市十字路口是道路网络中最危险的地点之一，对车辆和行人和骑自行车者等弱势道路使用者 (VRU) 构成重大风险。多代理交互的复杂性要求连续、实时的监控系统能够在冲突升级为崩溃之前预测冲突。我们推出 PRISA，这是一种模块化基础设施 LiDAR 框架，利用隐私保护、低光鲁棒性路边传感器进行长期交通观察和边缘实时风险检测。该框架包括两个核心组件：传感和感知层以及即插即用的风险评估模块。后者自动从累积的感知输出中整理特定地点的训练数据，以训练轨迹预测模型，而无需手动注释。
- Keywords: prisa, framework, intersection, safety, assessment

### 9. [使用黎曼流匹配从大型强子对撞机数据中学习标准模型结构](https://arxiv.org/abs/2607.16144v1)
- Original title: Learning Standard Model structure from LHC data with Riemannian flow matching
- Authors: Midori Kato, Kevin A. Urquía-Calderón, Inar Timiryasov, Oleg Ruchayskiy
- Meta: 2026-07-17 | hep-ph
- 中文摘要: 在这项工作中，我们证明了基于单一变压器的生成模型可以捕获跨越 5 个十年不变质量的标准模型结构，从亚 GeV 体系到 TeV 连续体，这是任何一个蒙特卡罗样本都无法覆盖的范围。为了实现这一目标，我们设计了 \textsc{ShellFlow}，这是一个黎曼条件流匹配模型，根据记录的事件组成，在其壳流形上生成每个粒子。它唯一的物理先验是壳内条件和不变质量公式。该模型在 ATLAS Open Data 13~TeV 版本中的 $\sim 10^{9}$ real $pp$ 碰撞事件上进行训练，除此之外没有任何其他信息。
- Abstract: In this work we demonstrate that a single transformer-based generative model can capture Standard Model structure spanning five decades of invariant mass, from the sub-GeV regime to the TeV continuum, a range that no single Monte Carlo sample covers. To achieve this we design \textsc{ShellFlow}, a Riemannian conditional flow matching model that, given the recorded event composition, generates each particle on its on...
- Summary (fallback): 机器翻译摘要显示：在这项工作中，我们证明了基于单一变压器的生成模型可以捕获跨越 5 个十年不变质量的标准模型结构，从亚 GeV 体系到 TeV 连续体，这是任何一个蒙特卡罗样本都无法覆盖的范围。为了实现这一目标，我们设计了 \textsc{ShellFlow}，这是一个黎曼条件流匹配模型，根据记录的事件组成，在其壳流形上生成每个粒子。它唯一的物理先验是壳内条件和不变质量公式。该模型在 ATLAS Open Data 13~TeV 版本中的 $\sim 10^{9}$ real $pp$ 碰撞事件上进行训练，除此之外没有任何其他信息。
- Keywords: model, standard, single, structure, riemannian

### 10. [改进改进的内核 PLS](https://arxiv.org/abs/2607.16138v1)
- Original title: Improving Improved Kernel PLS
- Authors: Ole-Christian Galbo Engstrøm
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 改进的核偏最小二乘 (IKPLS) 算法 1 和 2 是最快的 PLS 校准算法之一。本文重点介绍两个共享步骤，即 $\mathbf{X}$ 旋转 $\mathbf{R}$ 的计算和 $\mathbf{Y}$ 载荷 $\mathbf{Q}$ 的计算，并加速这两个步骤。对于 $\mathbf{R}$，逐项累加被直接评估策略所取代，该策略需要相同数量的乘法，但在现代硬件上可以更好地并行化。
- Abstract: Improved Kernel Partial Least Squares (IKPLS) algorithms 1 and 2 are among the fastest PLS calibration algorithms. This article focuses on two shared steps, the computation of the $\mathbf{X}$ rotations, $\mathbf{R}$, and the $\mathbf{Y}$ loadings, $\mathbf{Q}$, and accelerates both. For $\mathbf{R}$, term-by-term accumulation is replaced by a direct evaluation strategy that requires the same number of multiplicatio...
- Summary (fallback): 机器翻译摘要显示：改进的核偏最小二乘 (IKPLS) 算法 1 和 2 是最快的 PLS 校准算法之一。本文重点介绍两个共享步骤，即 $\mathbf{X}$ 旋转 $\mathbf{R}$ 的计算和 $\mathbf{Y}$ 载荷 $\mathbf{Q}$ 的计算，并加速这两个步骤。对于 $\mathbf{R}$，逐项累加被直接评估策略所取代，该策略需要相同数量的乘法，但在现代硬件上可以更好地并行化。
- Keywords: mathbf, ikpls, algorithms, both, same

### 11. [多代理系统何时有用？信息瓶颈视角](https://arxiv.org/abs/2607.16133v1)
- Original title: When Do Multi-Agent Systems Help? An Information Bottleneck Perspective
- Authors: Wendi Yu, Lianhao Zhou, Xiangjue Dong, Sai Sudarshan Barath, Declan Staunton et al.
- Meta: 2026-07-17 | cs.LG
- 中文摘要: LLM 支持的多智能体系统 (MAS) 已成为复杂任务的有前途的范例。然而，它们相对于单代理系统 (SAS) 的优势仍不清楚，不同设置下的性能变化不一致。在这里，我们提供信息瓶颈视角来阐明 MAS 和 SAS 之间的差异。具体来说，我们的主要观察结果是 SAS 在一个共享上下文中累积其完整推理轨迹，而 MAS 使用通过有界中继消息连接的隔离本地上下文。我们表明，在无限中继带宽下，任何 SAS 都可以通过传输完整上行上下文的 MAS 进行模拟。因此，MAS 的重要优势出现在有界中继下，其中压缩引入了一个基本的权衡：减少冗余上下文可以提高效率，但也可能导致任务相关信息的丢失。
- Abstract: LLM powered multi-agent systems (MAS) have emerged as a promising paradigm for complex tasks. However, their advantages over single-agent systems (SAS) remain unclear, with performance varying inconsistently across settings. Here, we provide an information bottleneck perspective on elucidating the differences between MAS and SAS. Specifically, our key observation is that a SAS accumulates its full reasoning trace in...
- Summary (fallback): 机器翻译摘要显示：LLM 支持的多智能体系统 (MAS) 已成为复杂任务的有前途的范例。然而，它们相对于单代理系统 (SAS) 的优势仍不清楚，不同设置下的性能变化不一致。在这里，我们提供信息瓶颈视角来阐明 MAS 和 SAS 之间的差异。具体来说，我们的主要观察结果是 SAS 在一个共享上下文中累积其完整推理轨迹，而 MAS 使用通过有界中继消息连接的隔离本地上下文。我们表明，在无限中继带宽下，任何 SAS 都可以通过传输完整上行上下文的 MAS 进行模拟。因此，MAS 的重要优势出现在有界中继下，其中压缩引入了一个基本的权衡：减少冗余上下文可以提高效率，但也可能导致任务相关信息的丢失。
- Keywords: information, when, context, multi-agent, systems

### 12. [CRAFT：对规则进行聚类以诊断法学硕士能力薄弱并生成有针对性的微调数据](https://arxiv.org/abs/2607.16122v1)
- Original title: CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted Fine-Tuning Data
- Authors: Vipul Gupta, Zihao Wang, Razvan-Gabriel Dumitru, MohammadHossein Rezaei, Aakash Sabharwal et al.
- Meta: 2026-07-17 | cs.AI
- 中文摘要: 评估不应只是衡量模型当前的性能。他们应该告诉我们下一次模型迭代需要修复什么，并提供一种生成有针对性的后训练数据的方法。大多数评估流程都会识别薄弱的示例、主题或类别，但它们隐含了潜在的能力失败：它们只说明模型在哪里失败，而不是原因。我们引入了 CRAFT，一种将任何基于评估数据集的评估数据集转换为针对弱能力的模型特定诊断的方法。 CRAFT 将每个评分标准视为能力探测：它从每个提示标题对中提取能力描述，将这些描述聚集到分层能力树中，在每个节点对目标模型进行评分，并以每个故障最明显的粒度跨树级别动态选择低性能节点。
- Abstract: Evaluations should do more than measure a models current performance. They should tell us what to fix for the next model iteration and provide a way to generate targeted post training data. Most evaluation pipelines identify weak examples, topics, or categories, but they leave the underlying capability failure implicit: they say where a model fails, not why. We introduce CRAFT, a method that converts any rubric base...
- Summary (fallback): 机器翻译摘要显示：评估不应只是衡量模型当前的性能。他们应该告诉我们下一次模型迭代需要修复什么，并提供一种生成有针对性的后训练数据的方法。大多数评估流程都会识别薄弱的示例、主题或类别，但它们隐含了潜在的能力失败：它们只说明模型在哪里失败，而不是原因。我们引入了 CRAFT，一种将任何基于评估数据集的评估数据集转换为针对弱能力的模型特定诊断的方法。 CRAFT 将每个评分标准视为能力探测：它从每个提示标题对中提取能力描述，将这些描述聚集到分层能力树中，在每个节点对目标模型进行评分，并以每个故障最明显的粒度跨树级别动态选择低性能节点。
- Keywords: craft, models, model, weak, capability

### 13. [诚实的仲裁问题：代理基础设施的认知拜占庭容错](https://arxiv.org/abs/2607.16109v1)
- Original title: The Honest Quorum Problem: Epistemic Byzantine Fault Tolerance for Agentic Infrastructure
- Authors: Jun He, Deying Yu
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 状态机复制 (SMR) 和拜占庭容错 (BFT) 共识保证了协议的一致性，尽管任意、串通的错误参与者数量有限。然而，这些保证依赖于该集合之外的参与者正确执行协议的转换语义。代理验证器暴露了较弱的边界：经过身份验证的、响应式的、明确的且符合协议的推理参与者仍可能由于推理错误而认可语义上无效的转换。我们将这种故障模式称为认知错误，并将这种集体现象称为诚实群体问题（其中“诚实”意味着符合协议，但语义上不正确）。这样的法定人数可以满足普通检查，同时形成无效转换的证书。因此，协议本身并不能保证语义有效性或执行安全性。
- Abstract: State machine replication (SMR) and Byzantine fault-tolerant (BFT) consensus guarantee agreement despite a bounded number of arbitrary, colluding faulty participants. However, these guarantees rely on participants outside this set correctly executing the protocol's transition semantics. Agentic validators expose a weaker boundary: an authenticated, responsive, non-equivocating, and protocol-compliant reasoning parti...
- Summary (fallback): 机器翻译摘要显示：状态机复制 (SMR) 和拜占庭容错 (BFT) 共识保证了协议的一致性，尽管任意、串通的错误参与者数量有限。然而，这些保证依赖于该集合之外的参与者正确执行协议的转换语义。代理验证器暴露了较弱的边界：经过身份验证的、响应式的、明确的且符合协议的推理参与者仍可能由于推理错误而认可语义上无效的转换。我们将这种故障模式称为认知错误，并将这种集体现象称为诚实群体问题（其中“诚实”意味着符合协议，但语义上不正确）。这样的法定人数可以满足普通检查，同时形成无效转换的证书。因此，协议本身并不能保证语义有效性或执行安全性。
- Keywords: byzantine, fault, epistemic, agentic, invalid

### 14. [自相关存在下在线变点检测的有效似然比检验](https://arxiv.org/abs/2607.16106v1)
- Original title: An Efficient Likelihood Ratio Test for Online Changepoint Detection in the Presence of Autocorrelation
- Authors: Yuntang Fan, Paul Fearnhead, Idris A. Eckley, Gaetano Romano
- Meta: 2026-07-17 | stat.ME
- 中文摘要: 近年来，变化点检测方法取得了长足的发展，在线算法能够近乎实时地识别流数据中的结构变化。然而，大多数现有方法都是在 IID 观测假设下设计的，这使得它们在应用于表现出时间依赖性的数据时容易受到更多误报或更长的检测延迟的影响，而时间依赖性是许多现实世界数据流的共同特征。在本文中，我们将广义似然比 (GLR) 统计扩展到 $p$ 阶的自回归过程，并采用焦点算法来开发计算高效的在线变化检测器。由此产生的 AR($p$) 聚焦算法每次迭代的平均计算成本为 $\mathcal{O}(\log n)$，使其适合高频数据流。
- Abstract: Changepoint detection methods have seen considerable development in recent years, with online algorithms capable of identifying structural changes in streaming data in near real time. However, the majority of existing methods are designed under the assumption of IID observations, rendering them susceptible to either more false positives or longer detection delays when applied to data exhibiting temporal dependence,...
- Summary (fallback): 机器翻译摘要显示：近年来，变化点检测方法取得了长足的发展，在线算法能够近乎实时地识别流数据中的结构变化。然而，大多数现有方法都是在 IID 观测假设下设计的，这使得它们在应用于表现出时间依赖性的数据时容易受到更多误报或更长的检测延迟的影响，而时间依赖性是许多现实世界数据流的共同特征。在本文中，我们将广义似然比 (GLR) 统计扩展到 $p$ 阶的自回归过程，并采用焦点算法来开发计算高效的在线变化检测器。由此产生的 AR($p$) 聚焦算法每次迭代的平均计算成本为 $\mathcal{O}(\log n)$，使其适合高频数据流。
- Keywords: detection, online, focus, efficient, changepoint

### 15. [从训练前到训练后理解推理](https://arxiv.org/abs/2607.16097v1)
- Original title: Understanding Reasoning from Pretraining to Post-Training
- Authors: Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum et al.
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 强化学习 (RL) 已成为改进复杂推理任务的大型语言模型 (LLM) 的核心，但 RL 后训练在很大程度上是与之前的预训练分开研究的。因此，两个基本问题仍然悬而未决：(1) 预训练选择（模型大小、数据）如何影响 RL 计算的回报，以及 (2) RL 实际上对模型做了什么？这些问题在标准法学硕士环境中很难研究：预训练语料库庞大且不受控制，因此很难将行为归因于预训练与强化学习，而且跨两个阶段的系统计算扫描成本高昂。为了应对这些挑战，我们使用国际象棋作为受控测试平台来研究整个训练前到训练后流程的推理。
- Abstract: Reinforcement learning (RL) has become central to improving large language models (LLMs) on complex reasoning tasks, yet RL post-training is largely studied in isolation from the pretraining that precedes it. As a result, two basic questions remain open: (1) how do pretraining choices (model size, data) shape the returns to RL compute, and (2) what does RL actually do to the model? These questions are difficult to s...
- Summary (fallback): 机器翻译摘要显示：强化学习 (RL) 已成为改进复杂推理任务的大型语言模型 (LLM) 的核心，但 RL 后训练在很大程度上是与之前的预训练分开研究的。因此，两个基本问题仍然悬而未决：(1) 预训练选择（模型大小、数据）如何影响 RL 计算的回报，以及 (2) RL 实际上对模型做了什么？这些问题在标准法学硕士环境中很难研究：预训练语料库庞大且不受控制，因此很难将行为归因于预训练与强化学习，而且跨两个阶段的系统计算扫描成本高昂。为了应对这些挑战，我们使用国际象棋作为受控测试平台来研究整个训练前到训练后流程的推理。
- Keywords: pretraining, reasoning, chess, language, model

### 16. [经验空间分布函数及其相关空间深度估计量的维数不变均匀一致性](https://arxiv.org/abs/2607.16092v1)
- Original title: Dimension-invariant uniform consistency of the empirical spatial distribution function and its associated spatial depth estimator
- Authors: Felix Gnettner, Hyemin Yeon, Piotr Kokoszka
- Meta: 2026-07-17 | math.ST
- 中文摘要: 我们提供了一个证明，证明 $\mathbb R^d$ 中的经验空间分布估计器以及相应的空间深度插件估计器是一致的 $L^1$ 一致的。一致性率仅取决于样本大小 $n$，而不取决于维度 $d$ 或任何调整或正则化参数。这是一个罕见的财产。本说明的结果源自与 ChatGPT 5.4 Pro 的对话，这是我们自己早期对其数学推理功能进行的一些实验的一部分。
- Abstract: We provide a proof that the empirical spatial distribution estimator in $\mathbb R^d$ as well as the corresponding plug-in estimator of the spatial depth are uniformly $L^1$-consistent. The consistency rate only depends on the sample size $n$, not on the dimension $d$ or any tuning or regularization parameters. This is a rare property. The result of this note originates from a conversation with ChatGPT 5.4 Pro as pa...
- Summary (fallback): 机器翻译摘要显示：我们提供了一个证明，证明 $\mathbb R^d$ 中的经验空间分布估计器以及相应的空间深度插件估计器是一致的 $L^1$ 一致的。一致性率仅取决于样本大小 $n$，而不取决于维度 $d$ 或任何调整或正则化参数。这是一个罕见的财产。本说明的结果源自与 ChatGPT 5.4 Pro 的对话，这是我们自己早期对其数学推理功能进行的一些实验的一部分。
- Keywords: spatial, estimator, consistency, empirical, distribution

### 17. [DADiff：扩散驱动的强化学习跨域策略适应](https://arxiv.org/abs/2607.16090v1)
- Original title: DADiff: Diffusion-Driven Cross-Domain Policy Adaptation for Reinforcement Learning
- Authors: Hanyang Chen, Anirudh Satheesh, Longchao Da, Hua Wei
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 由于源域和目标域之间的动态不匹配，跨域转移策略对强化学习提出了重大挑战。在本文中，我们考虑在线动态适应的设置，其中策略在具有足够数据的源域中进行训练，而仅允许与目标域进行有限的交互。有一些现有的工作通过采用域分类器、价值引导的数据过滤或表示学习来解决动态不匹配问题。相反，我们从生成建模的角度研究领域适应问题。具体来说，我们引入了 DADiff，一个基于扩散的框架，它利用下一个状态的生成过程中源域和目标域生成轨迹之间的差异来估计动态失配。
- Abstract: Transferring policies across domains poses a vital challenge in reinforcement learning, due to the dynamics mismatch between the source and target domains. In this paper, we consider the setting of online dynamics adaptation, where policies are trained in the source domain with sufficient data, while only limited interactions with the target domain are allowed. There are a few existing works that address the dynamic...
- Summary (fallback): 机器翻译摘要显示：由于源域和目标域之间的动态不匹配，跨域转移策略对强化学习提出了重大挑战。在本文中，我们考虑在线动态适应的设置，其中策略在具有足够数据的源域中进行训练，而仅允许与目标域进行有限的交互。有一些现有的工作通过采用域分类器、价值引导的数据过滤或表示学习来解决动态不匹配问题。相反，我们从生成建模的角度研究领域适应问题。具体来说，我们引入了 DADiff，一个基于扩散的框架，它利用下一个状态的生成过程中源域和目标域生成轨迹之间的差异来估计动态失配。
- Keywords: domain, dynamics, mismatch, target, policy

### 18. [AlphaFold2 的神经光谱揭示了编码的蛋白质构象景观](https://arxiv.org/abs/2607.16087v1)
- Original title: Neural spectroscopy of AlphaFold2 reveals encoded protein conformational landscapes
- Authors: Kaustav Mehta
- Meta: 2026-07-17 | cs.LG
- 中文摘要: AlphaFold2 的 9300 万个参数是由蛋白质数据库中编码的蛋白质结构的进化记录和序列比对形成的，传统上仅将其视为将序列转换为结构的机器。我们认为它们也是一个可以直接分析的科学对象：可以探测和表征的蛋白质构象组织的学习编码。通过使用高斯卷积平滑 Evoformer 的权重张量并缩放结果，我们表明训练后的模型会产生物理结构化的构象景观。在扰动下，泛素的天然接触打破了数十年折叠实验所建立的顺序。对于 KaiB 来说，五个独立训练的模型一致认为替代折叠在扰动下无法恢复。
- Abstract: AlphaFold2's 93 million parameters, shaped by the evolutionary record of protein structure encoded in the Protein Data Bank and in sequence alignments, are conventionally treated only as machinery for converting sequence to structure. We propose they are also a scientific object that can be analyzed directly: a learned encoding of protein conformational organization that can be probed and characterized. By smoothing...
- Summary (fallback): 机器翻译摘要显示：AlphaFold2 的 9300 万个参数是由蛋白质数据库中编码的蛋白质结构的进化记录和序列比对形成的，传统上仅将其视为将序列转换为结构的机器。我们认为它们也是一个可以直接分析的科学对象：可以探测和表征的蛋白质构象组织的学习编码。通过使用高斯卷积平滑 Evoformer 的权重张量并缩放结果，我们表明训练后的模型会产生物理结构化的构象景观。在扰动下，泛素的天然接触打破了数十年折叠实验所建立的顺序。对于 KaiB 来说，五个独立训练的模型一致认为替代折叠在扰动下无法恢复。
- Keywords: protein, conformational, alphafold2, landscapes, under

### 19. [针对始发地到目的地飞行问题的 MPC 策略的选择学习校准](https://arxiv.org/abs/2607.16084v1)
- Original title: Pick-to-Learn Calibration of an MPC Policy for an Origin-to-Destination Flight Problem
- Authors: Marco C. Campi, Simone Garatti
- Meta: 2026-07-17 | eess.SY
- 中文摘要: 本文阐述了应用于模型预测控制策略校准的“挑选学习”方法。虽然围绕特定示例进行开发，但该演示文稿旨在强调一种具有广泛适用性的方法。该示例涉及一架飞机在存在不确定的侧风和应避免的低连接区域的情况下从出发点飞往目的地点。 MPC 策略由两个超参数参数化，这两个超参数是由 P2L 过程从数据中选择的。从 400 个风力实现的数据集（也称为场景）开始，P2L 识别出仅包含两个信息丰富的场景的最终压缩集。
- Abstract: This paper illustrates the Pick-to-Learn methodology applied to the calibration of a Model Predictive Control policy. While developed around a specific example, the presentation is meant to highlight a methodology of broad applicability. The example concerns an aircraft traveling from an origin point to a destination point in the presence of uncertain crosswinds and a low-connectivity zone that should be avoided. Th...
- Summary (fallback): 机器翻译摘要显示：本文阐述了应用于模型预测控制策略校准的“挑选学习”方法。虽然围绕特定示例进行开发，但该演示文稿旨在强调一种具有广泛适用性的方法。该示例涉及一架飞机在存在不确定的侧风和应避免的低连接区域的情况下从出发点飞往目的地点。 MPC 策略由两个超参数参数化，这两个超参数是由 P2L 过程从数据中选择的。从 400 个风力实现的数据集（也称为场景）开始，P2L 识别出仅包含两个信息丰富的场景的最终压缩集。
- Keywords: policy, low-connectivity, zone, scenarios, pick-to-learn

### 20. [基于物理的深时空超局域雷达临近预报，采用多变量 U-Net 进行高分辨率降水预报](https://arxiv.org/abs/2607.16080v1)
- Original title: Physics-Based Deep Spatiotemporal Hyperlocal Radar Nowcasting with a Multi-Variable U-Net for High-Resolution Precipitation Forecasting
- Authors: Akshay Sunil, Muhammed Rashid, Raja Sekhar Sivaraju, Sushma Nair, Subimal Ghosh
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 近期 10​​-90 分钟的降水预报对于城市地区的洪水管理和实时决策非常重要。传统的短程预报与高分辨率数值天气预报需要频繁的数据同化、模型初始化和旋转，从而引入计算延迟。机器学习提供了一种替代方案，通过直接从高频观测中学习风暴演化并在训练后快速生成预测。这对于印度孟买尤其重要，那里的季风对流、陆海相互作用和局部强降雨使得短期预测变得困难。在这里，我们开发了一个紧凑的仅雷达临近预报框架，该框架在编码器-解码器 U-Net 中结合了多仰角反射率、多普勒径向速度和径向速度梯度代理特征。
- Abstract: Precipitation nowcasting over the immediate 10-90 min period is important for flood management and real-time decision-making in urban regions. Conventional short-range forecasting with high-resolution numerical weather prediction requires frequent data assimilation, model initialization, and spin-up, introducing computational latency. Machine learning provides an alternative by learning storm evolution directly from...
- Summary (fallback): 机器翻译摘要显示：近期 10​​-90 分钟的降水预报对于城市地区的洪水管理和实时决策非常重要。传统的短程预报与高分辨率数值天气预报需要频繁的数据同化、模型初始化和旋转，从而引入计算延迟。机器学习提供了一种替代方案，通过直接从高频观测中学习风暴演化并在训练后快速生成预测。这对于印度孟买尤其重要，那里的季风对流、陆海相互作用和局部强降雨使得短期预测变得困难。在这里，我们开发了一个紧凑的仅雷达临近预报框架，该框架在编码器-解码器 U-Net 中结合了多仰角反射率、多普勒径向速度和径向速度梯度代理特征。
- Keywords: model, radar, nowcasting, lead, u-net

### 21. [光学相干断层扫描中跨域视网膜层分割的空间归一化](https://arxiv.org/abs/2607.16065v1)
- Original title: Spatial Normalization for Cross-Domain Retinal Layer Segmentation in Optical Coherence Tomography
- Authors: Iker Moran-Cavero, Monica Hernandez, Elvira Mayordomo, Naiara Artiaga, Beatriz Pardiñas et al.
- Meta: 2026-07-17 | cs.CV
- 中文摘要: 光学相干断层扫描 (OCT) 中的视网膜层分割是提取视网膜结构定量生物标志物的基本步骤。事实上，人们对神经退行性疾病背景下的 OCT 分析越来越感兴趣。然而，由于散斑噪声、阴影伪影、相邻层之间的低对比度、受试者之间的解剖变异性以及不同采集协议和临床人群引起的域变化，分割仍然具有挑战性。尽管深度学习方法取得了显着的性能，但它们在异构数据集上的鲁棒性和泛化性仍然有限。在这项工作中，我们研究了空间归一化作为预处理策略的作用，以减轻几何域移位并提高视网膜层分割的一致性。
- Abstract: Retinal layer segmentation in Optical Coherence Tomography (OCT) is a fundamental step for extracting quantitative biomarkers of retinal structure. Indeed, there is a growing interest in the analysis of OCTs in the context of neurodegenerative diseases. However, segmentation remains challenging due to speckle noise, shadowing artifacts, low contrast between adjacent layers, anatomical variability across subjects, an...
- Summary (fallback): 机器翻译摘要显示：光学相干断层扫描 (OCT) 中的视网膜层分割是提取视网膜结构定量生物标志物的基本步骤。事实上，人们对神经退行性疾病背景下的 OCT 分析越来越感兴趣。然而，由于散斑噪声、阴影伪影、相邻层之间的低对比度、受试者之间的解剖变异性以及不同采集协议和临床人群引起的域变化，分割仍然具有挑战性。尽管深度学习方法取得了显着的性能，但它们在异构数据集上的鲁棒性和泛化性仍然有限。在这项工作中，我们研究了空间归一化作为预处理策略的作用，以减轻几何域移位并提高视网膜层分割的一致性。
- Keywords: segmentation, retinal, normalization, level, spatial

### 22. [当模型合并对手联合多任务强化学习时：任务向量几何分析](https://arxiv.org/abs/2607.16062v1)
- Original title: When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis
- Authors: S. Aaron McClendon
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 模型合并被推广为联合多任务训练的替代品，但在强化学习设置中，这种替代本质上从未根据其声称要替代的基线进行测试：方法精确地合并独立发布的代理，因为联合模型不可用。我们建立缺失的比较。使用 LOOP 在 AppWorld 代理基准上训练难度 1 和难度 2 Qwen3-8B 专家，我们将它们合并（TIES、RAM+），并将结果与​​相同数据上联合训练的模型进行比较。在完成任务目标时，合并与联合强化学习相匹配——并且每个合并变体在统计上是无法区分的。
- Abstract: Model merging is promoted as a substitute for joint multi-task training, yet in the reinforcement-learning setting this substitution is essentially never tested against the baseline it claims to replace: methods merge independently released agents precisely because a joint model is unavailable. We build the missing comparison. Training difficulty-1 and difficulty-2 Qwen3-8B specialists on the AppWorld agent benchmar...
- Summary (fallback): 机器翻译摘要显示：模型合并被推广为联合多任务训练的替代品，但在强化学习设置中，这种替代本质上从未根据其声称要替代的基线进行测试：方法精确地合并独立发布的代理，因为联合模型不可用。我们建立缺失的比较。使用 LOOP 在 AppWorld 代理基准上训练难度 1 和难度 2 Qwen3-8B 专家，我们将它们合并（TIES、RAM+），并将结果与​​相同数据上联合训练的模型进行比较。在完成任务目标时，合并与联合强化学习相匹配——并且每个合并变体在统计上是无法区分的。
- Keywords: model, merging, joint, merge, training

### 23. [基因调控网络推理的深度概率模型](https://arxiv.org/abs/2607.16053v1)
- Original title: Deep and Probabilistic Models for Gene Regulatory Network Inference
- Authors: Claudia Skok Gibbs
- Meta: 2026-07-17 | stat.ML
- 中文摘要: 基因调控网络（GRN）将转录因子（TF）蛋白与其靶基因连接起来，但在实际和方法学限制下，从全基因组数据重建这些网络仍然具有挑战性。许多方法将建模假设与特定的推理过程结合起来，并依赖于启发式模型选择，而评估则受到不完整的参考网络和缺乏不确定性的点估计输出的限制。 GRN 重建还依赖于限制 TF-基因相互作用的先验知识，但可用的先验知识通常依赖于分析，并且难以跨物种和特征较少的系统转移。在本文中，我们开发了两个互补的框架来解决这些限制。
- Abstract: Gene regulatory networks (GRNs) link transcription factor (TF) proteins to their target genes, yet reconstructing these networks from genome-wide data remains challenging under practical and methodological constraints. Many methods couple modeling assumptions to a specific inference procedure and rely on heuristic model selection, while evaluation is constrained by incomplete reference networks and point-estimate ou...
- Summary (fallback): 机器翻译摘要显示：基因调控网络（GRN）将转录因子（TF）蛋白与其靶基因连接起来，但在实际和方法学限制下，从全基因组数据重建这些网络仍然具有挑战性。许多方法将建模假设与特定的推理过程结合起来，并依赖于启发式模型选择，而评估则受到不完整的参考网络和缺乏不确定性的点估计输出的限制。 GRN 重建还依赖于限制 TF-基因相互作用的先验知识，但可用的先验知识通常依赖于分析，并且难以跨物种和特征较少的系统转移。在本文中，我们开发了两个互补的框架来解决这些限制。
- Keywords: inference, probabilistic, gene, regulatory, networks

### 24. [DELUGE：通过基础模型嵌入的可解释条件实现大陆规模的每日洪涝灾害预测](https://arxiv.org/abs/2607.16050v1)
- Original title: DELUGE: Towards Continental-Scale Daily Pluvial Flood Damage Prediction via Interpretable Conditioning on Foundation Model Embeddings
- Authors: Yuya Kawakami, Daniel Cayan, Dongyu Liu, Kwan-Liu Ma, Tom Corringham
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 雨洪（降雨驱动的）洪水占美国国家洪水保险计划 (NFIP) 索赔的 45%，并且比河流和沿海洪水更难预测，现有方法仅限于粗分辨率、区域域或基于计算密集型过程的模型，不适合日常大陆规模使用。我们提出了 DELUGE，这是一种多模态深度学习框架，用于在约 1 公里分辨率和全国范围内进行每日雨洪灾害损失预测，并根据空间和时间校正的 NFIP 索赔（2017-2022）进行训练，并围绕灾害风险的危害、暴露和脆弱性组成部分进行构建。我们没有对美国本土 (CONUS) 进行全面覆盖，而是对索赔最高的前 100 个 75 公里单元进行建模，这些单元分布在全国范围内，约占雨洪索赔总额的 81%。
- Abstract: Pluvial (rainfall-driven) flooding accounts for 45% of National Flood Insurance Program (NFIP) claims in the United States and is harder to predict than its riverine and coastal counterparts, with existing approaches limited to coarse resolution, regional domains, or computationally intensive process-based models unsuitable for daily continental-scale use. We present DELUGE, a multimodal deep learning framework for...
- Summary (fallback): 机器翻译摘要显示：雨洪（降雨驱动的）洪水占美国国家洪水保险计划 (NFIP) 索赔的 45%，并且比河流和沿海洪水更难预测，现有方法仅限于粗分辨率、区域域或基于计算密集型过程的模型，不适合日常大陆规模使用。我们提出了 DELUGE，这是一种多模态深度学习框架，用于在约 1 公里分辨率和全国范围内进行每日雨洪灾害损失预测，并根据空间和时间校正的 NFIP 索赔（2017-2022）进行训练，并围绕灾害风险的危害、暴露和脆弱性组成部分进行构建。我们没有对美国本土 (CONUS) 进行全面覆盖，而是对索赔最高的前 100 个 75 公里单元进行建模，这些单元分布在全国范围内，约占雨洪索赔总额的 81%。
- Keywords: deluge, pluvial, flood, claims, daily

### 25. [SciForge：用于科学发现的 AI 原生多模式工作台](https://arxiv.org/abs/2607.16038v1)
- Original title: SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery
- Authors: SciForge Team, Zhangyang Gao, Minghao Fang, Yifei Liu, Hanhui Yang et al.
- Meta: 2026-07-17 | cs.AI
- 中文摘要: 科学工作越来越多地跨越异构工件——论文、代码、数据集、科学文件格式、模型输出、图表、手稿和团队决策——但通用人工智能助手很少将这些对象保存为连贯的、可审计的研究状态。我们推出了 SciForge，一个多模式研究原生 AI 工作台，它保留了图形界面供人类判断，同时搜索、解析、模型路由、工作流执行、绘图、写作和演示文稿生成作为模块化代理可访问的服务运行。
- Abstract: Scientific work increasingly spans heterogeneous artifacts -- papers, code, datasets, scientific file formats, model outputs, figures, manuscripts, and team decisions -- yet general-purpose AI assistants rarely preserve these objects as a coherent, auditable research state. We present SciForge, a multimodal research-native AI workbench that reserves the graphical interface for human judgment while search, parsing, m...
- Summary (fallback): 机器翻译摘要显示：科学工作越来越多地跨越异构工件——论文、代码、数据集、科学文件格式、模型输出、图表、手稿和团队决策——但通用人工智能助手很少将这些对象保存为连贯的、可审计的研究状态。我们推出了 SciForge，一个多模式研究原生 AI 工作台，它保留了图形界面供人类判断，同时搜索、解析、模型路由、工作流执行、绘图、写作和演示文稿生成作为模块化代理可访问的服务运行。
- Keywords: scientific, sciforge, research, emph, textbf

### 26. [在 1.5 T MR 直线加速器上进行快速非门控五维心脏 MRI，用于 MRI 引导放射治疗](https://arxiv.org/abs/2607.16033v1)
- Original title: Fast ungated five-dimensional cardiac MRI on a 1.5 T MR-linac for MRI-guided radiotherapy
- Authors: M. L. Terpstra, T. E. Olausson, M. M. N. Aubert, C. Beijst, A. Sbrizzi et al.
- Meta: 2026-07-17 | physics.med-ph
- 中文摘要: 背景：室性心动过速患者的立体定向心律失常放射消融（STAR）目前受到复杂的心肺运动的限制。当前的 5D-MRI 运动模型需要较长的采集和重建时间，限制了临床可行性。目的：开发一种快速、非门控 5D-MRI 重建方法，用于个性化运动表征，以支持 MRI 引导的 STAR 治疗。方法：我们提出了一种基于 CMR-MOTUS 框架的快速、非门控 5D-MRI 重建方法。该方法使用具有联合优化框架的 3D 笛卡尔采集来重建运动校正参考图像和低阶变形矢量场 (DVF)。通过利用低阶结构，我们在优化过程中明确地解开呼吸和心脏运动。
- Abstract: Background: Stereotactic arrhythmia radio-ablation (STAR) for patients with ventricular tachycardia is currently limited by complex cardiorespiratory motion. Current 5D-MRI motion models require long acquisition and reconstruction times, limiting clinical viability. Objective: To develop a fast, ungated 5D-MRI reconstruction method for personalized motion characterization to support MRI-guided STAR treatments. Metho...
- Summary (fallback): 机器翻译摘要显示：背景：室性心动过速患者的立体定向心律失常放射消融（STAR）目前受到复杂的心肺运动的限制。当前的 5D-MRI 运动模型需要较长的采集和重建时间，限制了临床可行性。目的：开发一种快速、非门控 5D-MRI 重建方法，用于个性化运动表征，以支持 MRI 引导的 STAR 治疗。方法：我们提出了一种基于 CMR-MOTUS 框架的快速、非门控 5D-MRI 重建方法。该方法使用具有联合优化框架的 3D 笛卡尔采集来重建运动校正参考图像和低阶变形矢量场 (DVF)。通过利用低阶结构，我们在优化过程中明确地解开呼吸和心脏运动。
- Keywords: motion, d-mri, reconstruction, method, fast

### 27. [使用表格基础模型重新审视数据驱动的动态安全评估](https://arxiv.org/abs/2607.16031v1)
- Original title: Revisiting data-driven dynamic security assessment with a tabular foundation model
- Authors: Olayiwola Arowolo, Maosheng Yang, Jochen Cremer
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 数据驱动的故障前动态安全评估 (DSA) 使用机器学习快速评估电力系统中可信意外事件的动态风险。现有方法面临两个限制。首先，它们需要一个大型标记数据库进行训练，并为可能很长的可信意外事件列表中的每个意外事件训练、调整和维护一个单独的模型。其次，经过训练的模型对于看不见的突发事件的泛化能力很差。这项工作通过使用表格基础模型（TFM）解决了这些限制，该模型通过上下文学习来评估稳定性，无需重新训练或超参数优化。单个 TFM 可以同时评估许多意外事件，从而无需每个分类器使用一个模型。
- Abstract: Data-driven pre-fault dynamic security assessment (DSA) rapidly evaluates the dynamic risk of credible contingencies on a power system using machine learning. Existing approaches face two limitations. First, they require a large labelled database for training, with a separate model trained, tuned, and maintained for each contingency in a potentially long list of credible contingencies. Second, the trained models gen...
- Summary (fallback): 机器翻译摘要显示：数据驱动的故障前动态安全评估 (DSA) 使用机器学习快速评估电力系统中可信意外事件的动态风险。现有方法面临两个限制。首先，它们需要一个大型标记数据库进行训练，并为可能很长的可信意外事件列表中的每个意外事件训练、调整和维护一个单独的模型。其次，经过训练的模型对于看不见的突发事件的泛化能力很差。这项工作通过使用表格基础模型（TFM）解决了这些限制，该模型通过上下文学习来评估稳定性，无需重新训练或超参数优化。单个 TFM 可以同时评估许多意外事件，从而无需每个分类器使用一个模型。
- Keywords: model, contingencies, labelled, dynamic, foundation

### 28. [利用量子费舍尔信息重新思考量子持续学习](https://arxiv.org/abs/2607.16030v1)
- Original title: Rethinking Quantum Continual Learning with Quantum Fisher Information
- Authors: Yu-Chao Hsu, Yu-Cheng Lin, Tai-Yue Li, Nan-Yow Chen, En-Jui Kuo
- Meta: 2026-07-17 | quant-ph
- 中文摘要: 量子持续学习的目的是在连续任务上训练量子模型，而不会丢失之前学到的知识。然而，变分量子分类器（VQC）在非平稳任务分布下很容易出现灾难性遗忘。我们提出了量子弹性权重合并（QEWC），这是一种基于量子费希尔信息（QFI）的正则化方法，用于减轻遗忘。与基于经典 Fisher 信息 (CFI) 的传统弹性权重合并不同，QEWC 使用 QFI 来量化参数化量子态的内在敏感性，后者通过测量相关的输出统计来测量参数重要性。这给出了信息几何视图，其中重要参数通过量子态流形的局部响应来识别。
- Abstract: Quantum continual learning aims to train quantum models on sequential tasks without losing previously learned knowledge. However, variational quantum classifiers (VQCs) are prone to catastrophic forgetting under nonstationary task distributions. We propose quantum elastic weight consolidation (QEWC), a quantum Fisher information (QFI)-informed regularization method for mitigating forgetting. Unlike conventional elas...
- Summary (fallback): 机器翻译摘要显示：量子持续学习的目的是在连续任务上训练量子模型，而不会丢失之前学到的知识。然而，变分量子分类器（VQC）在非平稳任务分布下很容易出现灾难性遗忘。我们提出了量子弹性权重合并（QEWC），这是一种基于量子费希尔信息（QFI）的正则化方法，用于减轻遗忘。与基于经典 Fisher 信息 (CFI) 的传统弹性权重合并不同，QEWC 使用 QFI 来量化参数化量子态的内在敏感性，后者通过测量相关的输出统计来测量参数重要性。这给出了信息几何视图，其中重要参数通过量子态流形的局部响应来识别。
- Keywords: quantum, qewc, tasks, forgetting, continual

### 29. [CLaC@FinMMEval 2026 任务 3：用于主动交易的情感增强深度强化学习——Alpha 奖励方法](https://arxiv.org/abs/2607.16028v1)
- Original title: CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach
- Authors: Andrei Neagu, Eeham Khan, Leila Kosseim
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 本文介绍了我们用于 CLEF 2026 FinMMEval 实验室任务 3 的系统，该系统需要使用新闻和历史市场数据对比特币 (BTC) 和特斯拉 (TSLA) 进行每日多头、持平或空头交易决策。我们将该问题表述为离散动作马尔可夫决策过程，并比较了四种深度强化学习算法：策略梯度 (PG)、近端策略优化 (PPO)、深度 Q 学习 (DQL) 和深度确定性策略梯度 (DDPG)。代理使用 LLaMA 3.2 1B 生成的技术指标、周期日历编码和每日新闻情绪评分。为了减少过度拟合并使训练与超越买入并持有的目标保持一致，我们引入了基于超额市场回报的阿尔法奖励，并随机化剧集开始日期。
- Abstract: This paper presents our system for Task 3 of the CLEF 2026 FinMMEval Lab, which requires daily long, flat, or short trading decisions for Bitcoin (BTC) and Tesla (TSLA) using news and historical market data. We formulate the problem as a discrete-action Markov Decision Process and compare four deep reinforcement learning algorithms: Policy Gradient (PG), Proximal Policy Optimization (PPO), Deep Q-Learning (DQL), and...
- Summary (fallback): 机器翻译摘要显示：本文介绍了我们用于 CLEF 2026 FinMMEval 实验室任务 3 的系统，该系统需要使用新闻和历史市场数据对比特币 (BTC) 和特斯拉 (TSLA) 进行每日多头、持平或空头交易决策。我们将该问题表述为离散动作马尔可夫决策过程，并比较了四种深度强化学习算法：策略梯度 (PG)、近端策略优化 (PPO)、深度 Q 学习 (DQL) 和深度确定性策略梯度 (DDPG)。代理使用 LLaMA 3.2 1B 生成的技术指标、周期日历编码和每日新闻情绪评分。为了减少过度拟合并使训练与超越买入并持有的目标保持一致，我们引入了基于超额市场回报的阿尔法奖励，并随机化剧集开始日期。
- Keywords: deep, ddpg, task, policy, buy-and-hold

### 30. [受限赫布学习支持结构约束下的高效表征分配](https://arxiv.org/abs/2607.16027v1)
- Original title: Constrained Hebbian Learning Supports Efficient Representational Allocation under Structural Constraints
- Authors: Patrick Inoue, Florian Röhrbein, Andreas Knoblauch
- Meta: 2026-07-17 | cs.LG
- 中文摘要: 简介：生物系统面临解剖和代谢限制，包括昂贵的突触维护和有限的连接。这些约束有利于将行为相关信息压缩为低冗余模式的神经代码。我们测试了兴奋性竞争性赫布规则是否可以在这种约束下支持突触资源分配，以及所得到的表示是否比参考学习规则占据更有利的成本绩效制度。方法：使用源自变分信息瓶颈的基于互信息的度量来量化表征成本。实验使用来自三个视听基准（AVE、Kinetics-Sounds、VGGSound100）的固定视听嵌入来隔离下游关联可塑性。
- Abstract: Introduction: Biological systems face anatomical and metabolic constraints, including costly synaptic maintenance and limited connectivity. These constraints favor neural codes that compress behaviorally relevant information into low-redundancy patterns. We test whether an excitatory competitive Hebbian rule can support synaptic resource allocation under such constraints and whether the resulting representations occ...
- Summary (fallback): 机器翻译摘要显示：简介：生物系统面临解剖和代谢限制，包括昂贵的突触维护和有限的连接。这些约束有利于将行为相关信息压缩为低冗余模式的神经代码。我们测试了兴奋性竞争性赫布规则是否可以在这种约束下支持突触资源分配，以及所得到的表示是否比参考学习规则占据更有利的成本绩效制度。方法：使用源自变分信息瓶颈的基于互信息的度量来量化表征成本。实验使用来自三个视听基准（AVE、Kinetics-Sounds、VGGSound100）的固定视听嵌入来隔离下游关联可塑性。
- Keywords: hebbian, learning, constraints, information, representational

## biorxiv

### 1. [迁移增量的时间顺序在 MYO10 耗尽和胶原蛋白暴露下具有定向记忆](https://www.biorxiv.org/content/10.64898/2026.07.16.739021v1)
- Original title: Temporal ordering of migration increments carries directional memory under MYO10 depletion and collagen exposure
- Authors: Dutta, S.
- Meta: 2026-07-20 | biophysics | DOI: 10.64898/2026.07.16.739021
- 中文摘要: 细胞迁移通常用速度、均方位移或单个持续时间来概括，尽管这些描述符丢弃了连续位移增量的顺序。在一项结合了 MYO10 消耗和胶原蛋白暴露的公开二乘二阶乘实验中，我们使用等视场和等重复推理重新分析了 117 个视场的 48,134 条轨迹。两种扰动都会抑制运动性，但它们的组合会在方向持久性中产生积极的缓冲相互作用。保留每个轨迹的增量、长度、净位移和静态极性的分析零序表明，大多数可再现的相互作用取决于串行顺序。
- Abstract: Cell migration is commonly summarized by speed, mean-squared displacement, or a single persistence time, although these descriptors discard the order of successive displacement increments. We reanalyzed 48,134 trajectories from 117 fields of view in a public two-by-two factorial experiment combining MYO10 depletion and collagen exposure, using equal-field and equal-repeat inference. Both perturbations suppressed mot...
- Summary (fallback): 机器翻译摘要显示：细胞迁移通常用速度、均方位移或单个持续时间来概括，尽管这些描述符丢弃了连续位移增量的顺序。在一项结合了 MYO10 消耗和胶原蛋白暴露的公开二乘二阶乘实验中，我们使用等视场和等重复推理重新分析了 117 个视场的 48,134 条轨迹。两种扰动都会抑制运动性，但它们的组合会在方向持久性中产生积极的缓冲相互作用。保留每个轨迹的增量、长度、净位移和静态极性的分析零序表明，大多数可再现的相互作用取决于串行顺序。
- Keywords: positive, increments, directional, displacement, interaction

### 2. [R-Ras 在黑色素瘤的单通路抑制下协调 ERK5 和 ERK1/2 的相互激活](https://www.biorxiv.org/content/10.64898/2026.07.17.737152v1)
- Original title: R-Ras coordinates reciprocal activation of ERK5 and ERK1/2 under single pathway inhibition in melanoma
- Authors: Tusa, I., Mazzei, C., Papini, D., Menconi, A., Sfragano, Y. et al.
- Meta: 2026-07-20 | cancer biology | DOI: 10.64898/2026.07.17.737152
- 中文摘要: 恶性黑色素瘤是一种侵袭性癌症，由异常的丝裂原激活蛋白激酶 (MAPK) 信号传导驱动。尽管 BRAF 和 MEK1/2 抑制剂改善了 BRAF 突变患者的预后，但经常出现耐药性。临床前水平积累的证据已经确定，在 Ras-RAF-MEK1/2-ERK1/2 通路抑制后维持不同类型癌症生长的机制中，MEK5/ERK5 通路的激活是存在的。另一方面，缺乏关于 ERK5 抑制对黑色素瘤中 RAF-MEK1/2-ERK1/2 通路影响的信息。在这里，我们报告 ERK5 的遗传和药理学抑制会导致 BRAFV600E 突变的黑色素瘤细胞中 MEK1/2-ERK1/2 级联的过度激活。
- Abstract: Malignant melanoma is an aggressive cancer driven by aberrant Mitogen Activated Protein Kinase (MAPK) signaling. Although BRAF and MEK1/2 inhibitors improved the outcome in patients with BRAF mutations, resistance frequently arises. Accumulating evidence at the preclinical level has identified the activation of the MEK5/ERK5 pathway among the mechanisms sustaining the growth in different types of cancer upon Ras-RAF...
- Summary (fallback): 机器翻译摘要显示：恶性黑色素瘤是一种侵袭性癌症，由异常的丝裂原激活蛋白激酶 (MAPK) 信号传导驱动。尽管 BRAF 和 MEK1/2 抑制剂改善了 BRAF 突变患者的预后，但经常出现耐药性。临床前水平积累的证据已经确定，在 Ras-RAF-MEK1/2-ERK1/2 通路抑制后维持不同类型癌症生长的机制中，MEK5/ERK5 通路的激活是存在的。另一方面，缺乏关于 ERK5 抑制对黑色素瘤中 RAF-MEK1/2-ERK1/2 通路影响的信息。在这里，我们报告 ERK5 的遗传和药理学抑制会导致 BRAFV600E 突变的黑色素瘤细胞中 MEK1/2-ERK1/2 级联的过度激活。
- Keywords: erk5, erk1, r-ras, inhibition, melanoma

### 3. [谁资助开放数据共享？生物医学出版物中数据可用性声明的分析](https://www.biorxiv.org/content/10.64898/2026.07.17.739022v1)
- Original title: Who Funds Open Data Sharing? Analysis of data availability statements in biomedical publications
- Authors: Lawrimore, J., Li, C., Moraczewski, D., Poline, J.-B., Thomas, A.
- Meta: 2026-07-20 | scientific communication and education | DOI: 10.64898/2026.07.17.739022
- 中文摘要: 研究资助者、期刊和机构越来越多地要求开放数据共享，但大规模的合规性衡量仍然具有挑战性。我们使用双源管道分析了 2024 年 1 月至 2025 年 6 月期间发表的 784,262 篇开放获取生物医学研究文章：基于 PDF 的文本提取 (MinerU)，其中 PDF 可用，否则使用 PMC XML，然后对数据共享语句进行算法检测 (oddpub v7.2.3)，并通过来自 OpenAlex 的资助者、期刊和机构元数据进行丰富。该语料库包括 256,660 篇包含 PDF 的文章 (32.7%) 和 527,602 篇仅包含 XML 的文章 (67.3%)。我们发现，与资助者相关的文章（在元数据中至少识别出一位资助者的文章）的总体开放数据率为 8.7%，上升至 11.7%。
- Abstract: Open data sharing is increasingly mandated by research funders, journals, and institutions, yet large-scale compliance measurement remains challenging. We analyzed 784,262 open access biomedical research articles published between January 2024 and June 2025 using a dual-source pipeline: PDF-based text extraction (MinerU) where PDFs were available and PMC XML otherwise, followed by algorithmic detection of data shari...
- Summary (fallback): 机器翻译摘要显示：研究资助者、期刊和机构越来越多地要求开放数据共享，但大规模的合规性衡量仍然具有挑战性。我们使用双源管道分析了 2024 年 1 月至 2025 年 6 月期间发表的 784,262 篇开放获取生物医学研究文章：基于 PDF 的文本提取 (MinerU)，其中 PDF 可用，否则使用 PMC XML，然后对数据共享语句进行算法检测 (oddpub v7.2.3)，并通过来自 OpenAlex 的资助者、期刊和机构元数据进行丰富。该语料库包括 256,660 篇包含 PDF 的文章 (32.7%) 和 527,602 篇仅包含 XML 的文章 (67.3%)。我们发现，与资助者相关的文章（在元数据中至少识别出一位资助者的文章）的总体开放数据率为 8.7%，上升至 11.7%。
- Keywords: open, sharing, articles, rates, statements

### 4. [产前大麻暴露影响人类胎儿神经发育：综合多组学研究](https://www.biorxiv.org/content/10.64898/2026.07.15.738779v1)
- Original title: Prenatal cannabis exposure affects human fetal neurodevelopment: anintegrated multi-omics study
- Authors: Kahlert, G., Chen, X., Bammler, T. K., MacDonald, J. W., Benson, L. S. et al.
- Meta: 2026-07-20 | neuroscience | DOI: 10.64898/2026.07.15.738779
- 中文摘要: 产前大麻的使用呈上升趋势，观察性研究表明，这种使用会导致后代神经发育缺陷。由于观察性研究可能会受到未解释因素的干扰，因此我们在分子水平上研究了产前大麻使用对神经发育的影响。我们采用综合多组学方法，结合转录组学和全局蛋白质组学，对妊娠早期（T1）和中期（T2）人类胎儿大脑进行研究，无论是否有记录的母亲大麻暴露和滥用药物。产前大麻暴露对女性 T1 胎儿大脑产生最小的分子影响，但对男性 T2 胎儿大脑产生明显的系统级破坏。
- Abstract: Prenatal cannabis use is on the rise, and observational studies suggest that such use results in neurodevelopmental deficits in the offspring. Because observational studies can be confounded by unaccounted factors, we studied the neurodevelopmental consequences, at the molecular level, of prenatal cannabis use. We applied an integrated multi-omics approach, combining transcriptomics and global proteomics, tofirst tr...
- Summary (fallback): 机器翻译摘要显示：产前大麻的使用呈上升趋势，观察性研究表明，这种使用会导致后代神经发育缺陷。由于观察性研究可能会受到未解释因素的干扰，因此我们在分子水平上研究了产前大麻使用对神经发育的影响。我们采用综合多组学方法，结合转录组学和全局蛋白质组学，对妊娠早期（T1）和中期（T2）人类胎儿大脑进行研究，无论是否有记录的母亲大麻暴露和滥用药物。产前大麻暴露对女性 T1 胎儿大脑产生最小的分子影响，但对男性 T2 胎儿大脑产生明显的系统级破坏。
- Keywords: cannabis, prenatal, fetal, neurodevelopmental, molecular

### 5. [Cranifera cranifera (Chitwood, 1932) Kloss, 1960 来自圈养 Blaptica dubia Serville, 1838 蟑螂的形态基因组描述](https://www.biorxiv.org/content/10.64898/2026.07.17.739199v1)
- Original title: Morphogenomic description of Cranifera cranifera (Chitwood, 1932) Kloss, 1960 from captive Blaptica dubia Serville, 1838 cockroach
- Authors: Morffe, J., Guiglielmoni, N., Wassey, N., Gueddach, K., Schuster, A. et al.
- Meta: 2026-07-20 | zoology | DOI: 10.64898/2026.07.17.739199
- 中文摘要: 线虫总科的线虫存在于各种节肢动物的消化系统中，以宿主微生物组为食。它们有时被认为是自由生活的小杆藻和寄生螺旋藻之间的生态中间形式，而在系统发育上它们嵌套在后者内。除了有关雄性形态的新形态学数据外，该手稿还首次使用长读长测序方法组装了造口龟科物种 Cranifera cranifera 的核基因组，使造口造口鱼总科总共获得了三个核基因组。这里展示的 C. cranifera 核基因组组装体长 246 Mb，由 7563 个重叠群组成，N50 为 43 kb，包含 94% 的 BUSCO nematoda_odb12 基因。
- Abstract: Nematodes of the superfamily Thelastomatoidea are found in the digestive system of various arthropods, feeding on their host microbiome. They are sometimes considered to be ecologically intermediate forms between free-living rhabditids and parasitic Spirurina, while phylogenetically they are nested within the latter. In addition to new morphological data on the male morphology, this manuscript presents the first nuc...
- Summary (fallback): 机器翻译摘要显示：线虫总科的线虫存在于各种节肢动物的消化系统中，以宿主微生物组为食。它们有时被认为是自由生活的小杆藻和寄生螺旋藻之间的生态中间形式，而在系统发育上它们嵌套在后者内。除了有关雄性形态的新形态学数据外，该手稿还首次使用长读长测序方法组装了造口龟科物种 Cranifera cranifera 的核基因组，使造口造口鱼总科总共获得了三个核基因组。这里展示的 C. cranifera 核基因组组装体长 246 Mb，由 7563 个重叠群组成，N50 为 43 kb，包含 94% 的 BUSCO nematoda_odb12 基因。
- Keywords: cranifera, nuclear, genome, assembly, long

### 6. [应激源身份塑造人类血浆蛋白质组和代谢反应](https://www.biorxiv.org/content/10.64898/2026.07.17.739102v1)
- Original title: Stressor identity shapes plasma proteomic and metabolic responses in humans
- Authors: Ebert, T.
- Meta: 2026-07-20 | molecular biology | DOI: 10.64898/2026.07.17.739102
- 中文摘要: 急性压力会引发快速的生理适应，但不同的压力模式如何塑造人类循环分子景观仍不清楚。我们对三种范式进行了纵向深层血浆蛋白质组学和靶向代谢组学研究：心理压力、受控身体压力以及蹦极引起的心理-身体综合压力。尽管下丘脑-垂体-肾上腺轴被强烈激活，但心理压力引起了最小的血浆蛋白质组和代谢变化，而身体压力则引发了快速、协调的蛋白质组重塑，并伴有应激源特异性代谢适应。联合应激引发了最强烈和最持久的蛋白质组反应，定义了跨应激模式的分级分子特征。
- Abstract: Acute stress triggers rapid physiological adaptations, yet how distinct stress modalities shape the human circulating molecular landscape remains unclear. We performed longitudinal deep plasma proteomics and targeted metabolomics across three paradigms: psychological stress, controlled physical stress, and combined psychological-physical stress induced by bungee jumping. Despite robust hypothalamic-pituitary-adrenal...
- Summary (fallback): 机器翻译摘要显示：急性压力会引发快速的生理适应，但不同的压力模式如何塑造人类循环分子景观仍不清楚。我们对三种范式进行了纵向深层血浆蛋白质组学和靶向代谢组学研究：心理压力、受控身体压力以及蹦极引起的心理-身体综合压力。尽管下丘脑-垂体-肾上腺轴被强烈激活，但心理压力引起了最小的血浆蛋白质组和代谢变化，而身体压力则引发了快速、协调的蛋白质组重塑，并伴有应激源特异性代谢适应。联合应激引发了最强烈和最持久的蛋白质组反应，定义了跨应激模式的分级分子特征。
- Keywords: stress, plasma, proteomic, metabolic, molecular

### 7. [MBD2-NuRD 复合物内 GATAD2A-CHD4 相互作用的结构引导靶向导致成人红细胞中高水平的 HbF](https://www.biorxiv.org/content/10.64898/2026.07.17.739209v1)
- Original title: Structure-guided targeting of the GATAD2A-CHD4 interaction within the MBD2-NuRD complex results in high levels of HbF in adult erythroid cells
- Authors: Shang, S., Goswami, S. G., Li, T., Wang, H., Travis, C. et al.
- Meta: 2026-07-20 | molecular biology | DOI: 10.64898/2026.07.17.739209
- 中文摘要: 胎儿血红蛋白 (HbF) 的表达在成人红细胞中在出生后被沉默。充分增加 HbF 的表达已被证明可以克服镰状细胞病和 β 地中海贫血的病理生理后遗症。由于 HbF 沉默需要 MBD2a-NuRD 染色质重塑复合物，因此本研究旨在探索破坏该复合物的潜在治疗方法。 AlphaFold 3 和最近的晶体结构被用来预测连接 NuRD 的组蛋白脱乙酰酶核心子复合物 (HDCC) 中的 GATAD2A 和 CHD4 ATPase 的关键相互作用域，CHD4 ATPase 已被证明是胎儿伽马珠蛋白 (HBG) 基因沉默所必需的。两个预测的关键结构域，即 GATAD2A 的 CR2 螺旋结构域和 CHD4 的 C 末端结构域 1 和 2（C1b 和 C2ab），均通过体外生物物理学研究进行了验证。
- Abstract: Fetal hemoglobin (HbF) expression is silenced postnatally in adult erythroid cells. Sufficiently increased expression of HbF has been shown to overcome the pathophysiologic sequelae of both sickle cell disease and beta-thalassemia. As the MBD2a-NuRD chromatin remodeling complex is required for silencing of HbF, the present studies were aimed at exploring a potential therapeutic approach for disrupting this complex....
- Summary (fallback): 机器翻译摘要显示：胎儿血红蛋白 (HbF) 的表达在成人红细胞中在出生后被沉默。充分增加 HbF 的表达已被证明可以克服镰状细胞病和 β 地中海贫血的病理生理后遗症。由于 HbF 沉默需要 MBD2a-NuRD 染色质重塑复合物，因此本研究旨在探索破坏该复合物的潜在治疗方法。 AlphaFold 3 和最近的晶体结构被用来预测连接 NuRD 的组蛋白脱乙酰酶核心子复合物 (HDCC) 中的 GATAD2A 和 CHD4 ATPase 的关键相互作用域，CHD4 ATPase 已被证明是胎儿伽马珠蛋白 (HBG) 基因沉默所必需的。两个预测的关键结构域，即 GATAD2A 的 CR2 螺旋结构域和 CHD4 的 C 末端结构域 1 和 2（C1b 和 C2ab），均通过体外生物物理学研究进行了验证。
- Keywords: cells, gatad2a, erythroid, domains, chd4

### 8. [N-钙粘蛋白定向顺序随着心肌细胞粘附连接处的机械负载而降低](https://www.biorxiv.org/content/10.64898/2026.07.17.739172v1)
- Original title: N-cadherin orientational order decreases with mechanical load at cardiomyocyte adherens junctions
- Authors: Tran, Y. T. B., Dean, W. F., Han, Y., Karpov, K. I., Ainslie, C. M. et al.
- Meta: 2026-07-20 | cell biology | DOI: 10.64898/2026.07.17.739172
- 中文摘要: 粘附连接在物理上连接相邻细胞，并围绕经典钙粘蛋白（连接肌动蛋白细胞骨架的同亲性跨膜蛋白）构建。经典的钙粘蛋白可以在体外组织成有序阵列，但它们在细胞中是否这样做仍有待确定。在这里，我们使用荧光偏振显微镜来证明经典钙粘蛋白 N-钙粘蛋白在心肌细胞细胞-细胞连接处是定向有序的。尽管桥粒钙粘蛋白桥粒糖蛋白 2 在不同连接类型上的排序相似，但 N-钙粘蛋白的顺序在空间上是异质的。当有组织的肌原纤维终止于高负荷、富含纽蛋白的轴向连接处时，秩序最低；而在低负荷、缺乏纽蛋白的横向连接处，秩序最高。顺序和机械负载之间的这种反比关系表明强大的钙粘蛋白介导的粘附不需要胞外域顺序。
- Abstract: Adherens junctions physically connect neighboring cells and are built around classical cadherins, homophilic transmembrane proteins that link to the actin cytoskeleton. Classical cadherins can organize into ordered arrays in vitro, but whether they do so in cells remains to be established. Here, we use fluorescence polarization microscopy to show that the classical cadherin N-cadherin is orientationally ordered at c...
- Summary (fallback): 机器翻译摘要显示：粘附连接在物理上连接相邻细胞，并围绕经典钙粘蛋白（连接肌动蛋白细胞骨架的同亲性跨膜蛋白）构建。经典的钙粘蛋白可以在体外组织成有序阵列，但它们在细胞中是否这样做仍有待确定。在这里，我们使用荧光偏振显微镜来证明经典钙粘蛋白 N-钙粘蛋白在心肌细胞细胞-细胞连接处是定向有序的。尽管桥粒钙粘蛋白桥粒糖蛋白 2 在不同连接类型上的排序相似，但 N-钙粘蛋白的顺序在空间上是异质的。当有组织的肌原纤维终止于高负荷、富含纽蛋白的轴向连接处时，秩序最低；而在低负荷、缺乏纽蛋白的横向连接处，秩序最高。顺序和机械负载之间的这种反比关系表明强大的钙粘蛋白介导的粘附不需要胞外域顺序。
- Keywords: order, junctions, classical, ordered, n-cadherin

### 9. [双键几何形状决定脂肪酸代谢命运和铁死亡敏感性](https://www.biorxiv.org/content/10.64898/2026.07.17.739092v1)
- Original title: Double-bond geometry determines fatty acid metabolic fate and ferroptosis sensitivity
- Authors: Harris, C. A., Kato, S., Otoki, Y., Martin Perez, E., Boone, D. et al.
- Meta: 2026-07-20 | cell biology | DOI: 10.64898/2026.07.17.739092
- 中文摘要: 铁死亡是由氧化损伤的膜磷脂的积累驱动的，使得膜脂成分成为细胞死亡敏感性的核心决定因素。虽然脂肪酸链长度和不饱和度是铁死亡的公认调节因子，但脂肪酸立体化学是否有助于铁死亡的易感性大多尚未被探索。在这里，我们系统地筛选了结构多样的脂肪酸调节铁死亡的能力，并意外地发现反式不饱和脂肪酸是有效的敏化剂。与顺式亚油酸相比，反式多不饱和脂肪酸（PUFA）亚油酸更强烈地增强脂质过氧化并促进铁死亡易感磷脂种类的积累。
- Abstract: Ferroptosis is driven by the accumulation of oxidatively damaged membrane phospholipids, making membrane lipid composition a central determinant of cell death sensitivity. While fatty acid chain length and degree of unsaturation are well-established regulators of ferroptosis, whether fatty acid stereochemistry contributes to ferroptosis susceptibility is mostly unexplored. Here, we systematically screened structural...
- Summary (fallback): 机器翻译摘要显示：铁死亡是由氧化损伤的膜磷脂的积累驱动的，使得膜脂成分成为细胞死亡敏感性的核心决定因素。虽然脂肪酸链长度和不饱和度是铁死亡的公认调节因子，但脂肪酸立体化学是否有助于铁死亡的易感性大多尚未被探索。在这里，我们系统地筛选了结构多样的脂肪酸调节铁死亡的能力，并意外地发现反式不饱和脂肪酸是有效的敏化剂。与顺式亚油酸相比，反式多不饱和脂肪酸（PUFA）亚油酸更强烈地增强脂质过氧化并促进铁死亡易感磷脂种类的积累。
- Keywords: acid, fatty, ferroptosis, metabolic, membrane

### 10. [早期 CYP26A1/CRYAA 祖细胞神经胶质结构域标记了人类视网膜发育过程中的假定黄斑区域](https://www.biorxiv.org/content/10.64898/2026.07.17.738962v1)
- Original title: An early CYP26A1/CRYAA progenitor-glial domain marks the presumptive macular region during human retinal development
- Authors: Yang, Q., Docampo-Seara, A., Powner, M. B., Chung, G. H., Ribeiro-Bravo, I. et al.
- Meta: 2026-07-20 | developmental biology | DOI: 10.64898/2026.07.17.738962
- 中文摘要: 人类黄斑是中央视力所必需的高敏锐度视网膜区域，在发育早期就出现了，但其区域特化的细胞基础仍未完全解决。基于最近在假定黄斑中发现 CYP26A1 介导的视黄酸 (RA) 抑制的研究，我们定义了从受孕后第 7 周 (pcw) 起人类颞部视网膜中的 CRYAA 阳性祖细胞神经胶质区室。单细胞 RNA 测序、免疫组织化学和空间形态测量表明，该区室与区域神经胶质细胞成熟有关，并随后对应于专门的黄斑 M&uumlller 神经胶质细胞群，而不是简单地反映统一的全视网膜发育时间。空间映射显示，随着周围视网膜的扩张，CYP26A1 阳性区域仍然被界定。
- Abstract: The human macula, a high-acuity retinal region essential for central vision, emerges early in development, but the cellular basis of its regional specialisation remains incompletely resolved. Building on recent studies that identified CYP26A1-mediated retinoic acid (RA) suppression in the presumptive macula, we define a CRYAA-positive progenitor-glial compartment in the temporal human retina from post-conception wee...
- Summary (fallback): 机器翻译摘要显示：人类黄斑是中央视力所必需的高敏锐度视网膜区域，在发育早期就出现了，但其区域特化的细胞基础仍未完全解决。基于最近在假定黄斑中发现 CYP26A1 介导的视黄酸 (RA) 抑制的研究，我们定义了从受孕后第 7 周 (pcw) 起人类颞部视网膜中的 CRYAA 阳性祖细胞神经胶质区室。单细胞 RNA 测序、免疫组织化学和空间形态测量表明，该区室与区域神经胶质细胞成熟有关，并随后对应于专门的黄斑 M&uumlller 神经胶质细胞群，而不是简单地反映统一的全视网膜发育时间。空间映射显示，随着周围视网膜的扩张，CYP26A1 阳性区域仍然被界定。
- Keywords: macular, early, human, cyp26a1, progenitor-glial

### 11. [夜间授粉服务作为热带生物多样性热点地区木瓜生产的生态安全网](https://www.biorxiv.org/content/10.64898/2026.07.17.739175v1)
- Original title: Nocturnal pollination services as an ecological safety net for papaya production in a tropical biodiversity hotspot
- Authors: Otieno, M., Peters, M. K., Plesser, S. M., Zhang, J., Steffan-Dewenter, I.
- Meta: 2026-07-20 | ecology | DOI: 10.64898/2026.07.17.739175
- 中文摘要: 授粉对于热带农业至关重要，但以蜜蜂为中心的观点往往忽视了夜间活动的昆虫在授粉服务中的关键作用。我们评估了肯尼亚泰塔山（全球重要的生物多样性热点地区）自给农场的昼间和夜间授粉媒介对木瓜产量的相对贡献。我们将花卉访客观察与五种实验处理结合起来：开放授粉、仅风授粉（封闭）、手工授粉以及仅白天和仅夜间服务的时间排除。我们的结果揭示了昼间蜜蜂和​​夜间天蛾（天蛾科）之间完整的时间生态位划分。我们发现，昼夜授粉者和夜间授粉者提供附加服务，而不是冗余服务，对木瓜坐果和重量的贡献程度相似。
- Abstract: Pollination is of key importance for tropical agriculture, yet a bee-centred perspective often overlooks the critical role of nocturnal insects in pollination services. We evaluated the relative contributions of diurnal and nocturnal pollinators to papaya yields on subsistence farms in the Taita Hills, Kenya, a globally important biodiversity hotspot. We combined flower visitor observations with five experimental tr...
- Summary (fallback): 机器翻译摘要显示：授粉对于热带农业至关重要，但以蜜蜂为中心的观点往往忽视了夜间活动的昆虫在授粉服务中的关键作用。我们评估了肯尼亚泰塔山（全球重要的生物多样性热点地区）自给农场的昼间和夜间授粉媒介对木瓜产量的相对贡献。我们将花卉访客观察与五种实验处理结合起来：开放授粉、仅风授粉（封闭）、手工授粉以及仅白天和仅夜间服务的时间排除。我们的结果揭示了昼间蜜蜂和​​夜间天蛾（天蛾科）之间完整的时间生态位划分。我们发现，昼夜授粉者和夜间授粉者提供附加服务，而不是冗余服务，对木瓜坐果和重量的贡献程度相似。
- Keywords: nocturnal, pollination, services, papaya, diurnal

### 12. [评估 DNA 元条形码以表征多面性中捕食者小黑背鸥 (Larus fuscus) 的饮食多样性和觅食策略](https://www.biorxiv.org/content/10.64898/2026.07.17.738687v1)
- Original title: Evaluating DNA metabarcoding to characterise diet diversity and foraging strategies in a generalist mesopredator, the lesser black-backed gull (Larus fuscus)
- Authors: Risely, A., Carss, D. N., How, E. F., Donato, B. J., Frayling, T. D. et al.
- Meta: 2026-07-20 | ecology | DOI: 10.64898/2026.07.17.738687
- 中文摘要: 1）有关个体和种群水平饮食成分的信息对于了解资源利用和可用性至关重要，这会影响个体健康以及捕食者和猎物的种群动态。 DNA饮食元条形码为饮食分析提供了一种强大的分子方法，但其应用可能受到方法学偏差的限制，特别是在饮食高度多样化的通才物种中。 2) 在这里，我们评估了小黑背鸥 (Larus fuscus) 饮食分析中 DNA 元条形码的性能，小黑背鸥是一种高度通才的中掠食者，在过去的半个世纪里，其种群对自然和人为食物资源的变化表现出了复杂的反应。
- Abstract: 1) Information on diet composition at both individual and population levels is fundamental to understanding resource use and availability, which influence individual fitness and the population dynamics of both predators and their prey. DNA diet metabarcoding offers a powerful molecular approach to diet analysis, but its application can be limited by methodological biases, particularly in generalist species with high...
- Summary (fallback): 机器翻译摘要显示：1）有关个体和种群水平饮食成分的信息对于了解资源利用和可用性至关重要，这会影响个体健康以及捕食者和猎物的种群动态。 DNA饮食元条形码为饮食分析提供了一种强大的分子方法，但其应用可能受到方法学偏差的限制，特别是在饮食高度多样化的通才物种中。 2) 在这里，我们评估了小黑背鸥 (Larus fuscus) 饮食分析中 DNA 元条形码的性能，小黑背鸥是一种高度通才的中掠食者，在过去的半个世纪里，其种群对自然和人为食物资源的变化表现出了复杂的反应。
- Keywords: metabarcoding, diet, species, highly, samples

### 13. [白蜡树腐烂洞中无脊椎动物群落多样性和结构的地方和生物地理决定因素](https://www.biorxiv.org/content/10.64898/2026.07.17.739164v1)
- Original title: Local and biogeographical determinants of the diversity and structure of invertebrate communities in rot holes of ash, Fraxinus excelsior
- Authors: Dawson, W. G., Jones, H., Cuff, J. P., Shepherd, M. J., Boddy, L.
- Meta: 2026-07-20 | ecology | DOI: 10.64898/2026.07.17.739164
- 中文摘要: 1. 老树是生物多样性的热点，提供了一系列的微生境，包括树洞或树干上的腐洞，它们支持包括受威胁物种在内的多种无脊椎动物的生存。每个腐洞都是一个独特的微观世界，具有可变的生物和非生物特征，使其能够被许多无脊椎动物类群利用。 2. 以往大多数描述腐洞无脊椎动物群落及其结构因素的研究都集中在狭窄的无脊椎动物类群上，许多寄主树种仍未被探索。由于白蜡顶枯病的蔓延，欧洲白蜡（Fraxinus excelsior L.）是欧洲最受威胁的落叶树种之一，但人们对这些损失对栖息在白蜡中的无脊椎动物群落的潜在影响知之甚少。 3.
- Abstract: 1. Veteran trees are biodiversity hotspots, providing a range of microhabitats, including tree hollows or rot holes in trunks, which support a large diversity of invertebrates including threatened species. Each rot hole is a unique microcosm, with variable biotic and abiotic characteristics enabling their use by many invertebrate taxa. 2. Most previous studies describing the invertebrate communities of rot holes and...
- Summary (fallback): 机器翻译摘要显示：1. 老树是生物多样性的热点，提供了一系列的微生境，包括树洞或树干上的腐洞，它们支持包括受威胁物种在内的多种无脊椎动物的生存。每个腐洞都是一个独特的微观世界，具有可变的生物和非生物特征，使其能够被许多无脊椎动物类群利用。 2. 以往大多数描述腐洞无脊椎动物群落及其结构因素的研究都集中在狭窄的无脊椎动物类群上，许多寄主树种仍未被探索。由于白蜡顶枯病的蔓延，欧洲白蜡（Fraxinus excelsior L.）是欧洲最受威胁的落叶树种之一，但人们对这些损失对栖息在白蜡中的无脊椎动物群落的潜在影响知之甚少。 3.
- Keywords: invertebrate, communities, holes, diversity, range

### 14. [植物性和传统面包屑虾的质构分析和消费者感官评价](https://www.biorxiv.org/content/10.64898/2026.07.17.739214v1)
- Original title: Texture Profile Analysis and Consumer Sensory Evaluation of Plant-Based and Conventional Breaded Shrimp
- Authors: Koosis, A. O., Kuhl, E.
- Meta: 2026-07-20 | bioengineering | DOI: 10.64898/2026.07.17.739214
- 中文摘要: 植物性海鲜替代品可以减轻对海洋生态系统的压力，但植物性产品和传统产品之间的质地差异限制了消费者的采用。本研究比较了植物基虾和传统面包屑虾的质地特性和消费者接受度，以评估仪器质地差异是否可以预测感官差异。对四种面包屑虾产品进行了质地概况分析 (TPA)（每个产品 n = 14--15 个重复），消费者感官评估 (n = 107) 使用受试者内平衡设计来评估享乐评级、恰到好处的属性、检查所有适用的描述符和购买意图。 TPA 显示，植物基虾的硬度（14.9 +/- 1.0 N 与 9.6 +/- 2.8 N）、硬度（592 +/- 40 kPa 与 382 +/- 113 kPa）和咀嚼性（10.5 +/- 0.8 N 与 9.6 +/- 2.8 N）显着更高。
- Abstract: Plant-based seafood alternatives could reduce pressure on marine ecosystems, yet texture gaps between plant-based and conventional products limit consumer adoption. This study compared the textural properties and consumer acceptance of plant-based and conventional breaded shrimp to evaluate whether instrumental texture differences predict sensory differences. Texture Profile Analysis (TPA) was performed on four brea...
- Summary (fallback): 机器翻译摘要显示：植物性海鲜替代品可以减轻对海洋生态系统的压力，但植物性产品和传统产品之间的质地差异限制了消费者的采用。本研究比较了植物基虾和传统面包屑虾的质地特性和消费者接受度，以评估仪器质地差异是否可以预测感官差异。对四种面包屑虾产品进行了质地概况分析 (TPA)（每个产品 n = 14--15 个重复），消费者感官评估 (n = 107) 使用受试者内平衡设计来评估享乐评级、恰到好处的属性、检查所有适用的描述符和购买意图。 TPA 显示，植物基虾的硬度（14.9 +/- 1.0 N 与 9.6 +/- 2.8 N）、硬度（592 +/- 40 kPa 与 382 +/- 113 kPa）和咀嚼性（10.5 +/- 0.8 N 与 9.6 +/- 2.8 N）显着更高。
- Keywords: shrimp, consumer, plant-based, breaded, texture

### 15. [机械负载骨活体双光子成像的实时轴向运动补偿](https://www.biorxiv.org/content/10.64898/2026.07.17.739194v1)
- Original title: Real-Time Axial Motion Compensation for Intravital Two-Photon Imaging of Mechanically Loaded Bone
- Authors: Bratcher, S., Mora-Antoinette, M., Lewis, K. J.
- Meta: 2026-07-20 | bioengineering | DOI: 10.64898/2026.07.17.739194
- 中文摘要: 运动伪影对经历生理运动或机械负荷的组织的活体成像提出了重大挑战。由于 z 轴移动而导致的图像强度模糊或人为变化会降低数据的再现性和可靠性。现有的采集后方法可以部分补偿运动，但它们增加了实验复杂性，并且不太适合用于机械加载的骨骼。因此，我们开发了一种通过同步物镜与执行器的运动来实时校正骨骼机械加载过程中的轴向运动的新方法。通过将致动器压电电机的位置与物镜压电电机的位置联系起来，并通过电位计进行用户精确的减小，从而实现同步。
- Abstract: Motion artifacts present a major challenge for intravital imaging of tissues undergoing physiological movement or mechanical loading. Blurring or artificial changes in image intensity due to shifting on the z-axis reduce data reproducibility and reliability. Existing post-acquisition approaches can partially compensate for motion, but they increase experimental complexity and are not well suited for use in mechanica...
- Summary (fallback): 机器翻译摘要显示：运动伪影对经历生理运动或机械负荷的组织的活体成像提出了重大挑战。由于 z 轴移动而导致的图像强度模糊或人为变化会降低数据的再现性和可靠性。现有的采集后方法可以部分补偿运动，但它们增加了实验复杂性，并且不太适合用于机械加载的骨骼。因此，我们开发了一种通过同步物镜与执行器的运动来实时校正骨骼机械加载过程中的轴向运动的新方法。通过将致动器压电电机的位置与物镜压电电机的位置联系起来，并通过电位计进行用户精确的减小，从而实现同步。
- Keywords: motion, bone, axial, imaging, mechanically

### 16. [细菌curli蛋白CsgA的单分子研究揭示了结构动态单体结构](https://www.biorxiv.org/content/10.1101/2025.09.08.674806v5)
- Original title: Single molecule studies of the bacterial curli protein CsgA reveal a structurally dynamic monomeric structure
- Authors: Foster, D. A. N., Dee, D. R.
- Meta: 2026-07-20 | biophysics | DOI: 10.1101/2025.09.08.674806
- 中文摘要: E. coli curli 是一种关键的生物膜支架和抗菌靶标，主要由蛋白质 CsgA 组装而成，并在受调节的功能性淀粉样蛋白组装途径中受到许多其他伴侣的引导。 CsgA 非常容易聚集，这会干扰对其结构和淀粉样蛋白形成机制的高分辨率研究。整体研究表明 CsgA 本质上是无序的，而结构预测显示是一个折叠良好的 {β}-螺线管。在这里，使用光镊单分子力谱来定义单个 CsgA 分子的构象动力学。 CsgA单体表现出与完全折叠、部分折叠和折叠但无序构象一致的去折叠/重折叠，表明CsgA存在于与无序状态平衡的亚稳态折叠状态。
- Abstract: E. coli curli, a critical biofilm scaffold and antimicrobial target, is assembled mainly from the protein CsgA guided by many other chaperones in a regulated functional amyloid assembly pathway. CsgA is highly aggregation prone, confounding high-resolution studies of its structure and amyloid formation mechanism. Ensemble studies show CsgA is intrinsically disordered, while structure predictions show a well-folded {...
- Summary (fallback): 机器翻译摘要显示：E. coli curli 是一种关键的生物膜支架和抗菌靶标，主要由蛋白质 CsgA 组装而成，并在受调节的功能性淀粉样蛋白组装途径中受到许多其他伴侣的引导。 CsgA 非常容易聚集，这会干扰对其结构和淀粉样蛋白形成机制的高分辨率研究。整体研究表明 CsgA 本质上是无序的，而结构预测显示是一个折叠良好的 {β}-螺线管。在这里，使用光镊单分子力谱来定义单个 CsgA 分子的构象动力学。 CsgA单体表现出与完全折叠、部分折叠和折叠但无序构象一致的去折叠/重折叠，表明CsgA存在于与无序状态平衡的亚稳态折叠状态。
- Keywords: csga, studies, amyloid, folded, curli

### 17. [脓蛋白通过影响基于肌动蛋白的突起形成来促进 3D 胶原凝胶中乳腺癌细胞的侵袭](https://www.biorxiv.org/content/10.64898/2026.07.17.739166v1)
- Original title: Septins promote breast cancer cell invasion in 3D collagen gels by influencing actin-based protrusion formation
- Authors: van der Net, A., Beslmueller, K., van Vliet, N., Tavasso, M., Beerens, M. et al.
- Meta: 2026-07-20 | cancer biology | DOI: 10.64898/2026.07.17.739166
- 中文摘要: 脓蛋白是细胞骨架蛋白，通过与细胞膜和细胞骨架的相互作用促进细胞迁移和细胞分裂等重要的细胞过程。脓毒蛋白的高表达与乳腺癌恶性肿瘤相关并促进细胞侵袭，但脓毒蛋白相互作用的分子复杂性使得剖析潜在的分子机制具有挑战性。在这里，我们使用条件敲除方法来消除转移性三阴性乳腺癌细胞系 Hs578T 中的 SEPT7，并检查了 septin 在乳腺癌细胞 3D 基质侵袭中的作用。我们通过球体测定表明，SEPT7 缺失会强烈损害乳腺癌细胞侵入胶原凝胶。
- Abstract: Septins are cytoskeletal proteins that contribute to essential cellular processes such as cell migration and cell division through interactions with the cell membrane and the cytoskeleton. High expression of septins is correlated with breast cancer malignancy and promotes cell invasion, but the molecular complexity of septins interactions has made it challenging to dissect the underlying molecular mechanisms. Here,...
- Summary (fallback): 机器翻译摘要显示：脓蛋白是细胞骨架蛋白，通过与细胞膜和细胞骨架的相互作用促进细胞迁移和细胞分裂等重要的细胞过程。脓毒蛋白的高表达与乳腺癌恶性肿瘤相关并促进细胞侵袭，但脓毒蛋白相互作用的分子复杂性使得剖析潜在的分子机制具有挑战性。在这里，我们使用条件敲除方法来消除转移性三阴性乳腺癌细胞系 Hs578T 中的 SEPT7，并检查了 septin 在乳腺癌细胞 3D 基质侵袭中的作用。我们通过球体测定表明，SEPT7 缺失会强烈损害乳腺癌细胞侵入胶原凝胶。
- Keywords: cell, breast, cancer, septins, invasion

### 18. [可逆的染色质重塑使 Prosopis cineraria 在反复出现的极端高温下得以生存。](https://www.biorxiv.org/content/10.64898/2026.07.17.734425v1)
- Original title: Reversible chromatin remodeling enables Prosopis cineraria survival under recurrent heat extremes.
- Authors: Dubay, B., Muthukumar, R., Purayil, F. T., Sundararaja Moorthy, D. K., Shah, I. et al.
- Meta: 2026-07-20 | plant biology | DOI: 10.64898/2026.07.17.734425
- 中文摘要: 气候变暖正在加剧季节性炎热和干旱，引发了关于长寿沙漠植物如何在反复出现的极端情况下维持生理功能的紧迫问题。在 Prosopis cineraria（一种本土阿拉伯沙漠豆科树）中，我们在六个时间点使用季节性 Hi-C、转录组、组蛋白标记和 DNA 甲基化分析来揭示潜在机制。我们发现，在高温期间，染色质边界选择性减弱，候选拓扑结构域合并，激活富含 H3K4me3 和 H3K27ac 的热保护基因簇。在凉爽的季节，免疫和发育基因调控与开花相结合，这与将繁殖远离致命高温的对冲策略相一致。
- Abstract: Climate warming is intensifying seasonal heat and drought, raising urgent questions about how long-lived desert plants sustain physiological function across recurrent extremes. In Prosopis cineraria, a native Arabian desert legume tree, we used seasonal Hi-C, transcriptomic, histone-mark, and DNA-methylation profiling at six time points to uncover the underlying mechanisms. We found that during peak heat, chromatin...
- Summary (fallback): 机器翻译摘要显示：气候变暖正在加剧季节性炎热和干旱，引发了关于长寿沙漠植物如何在反复出现的极端情况下维持生理功能的紧迫问题。在 Prosopis cineraria（一种本土阿拉伯沙漠豆科树）中，我们在六个时间点使用季节性 Hi-C、转录组、组蛋白标记和 DNA 甲基化分析来揭示潜在机制。我们发现，在高温期间，染色质边界选择性减弱，候选拓扑结构域合并，激活富含 H3K4me3 和 H3K27ac 的热保护基因簇。在凉爽的季节，免疫和发育基因调控与开花相结合，这与将繁殖远离致命高温的对冲策略相一致。
- Keywords: heat, seasonal, chromatin, desert, reversible

### 19. [Alarmone ((p)ppGpp) 信号调节拟南芥核基因表达以塑造植物免疫结果的平衡](https://www.biorxiv.org/content/10.64898/2026.07.17.739251v1)
- Original title: Alarmone ((p)ppGpp) signalling tunes Arabidopsis thaliana nuclear gene expression to shape the balance of plant immune outcomes
- Authors: Aballay, F. E., Leon Sanchez, I. J., Rodriguez, F. S., Benelli, C., Salaberry, P. J. et al.
- Meta: 2026-07-20 | plant biology | DOI: 10.64898/2026.07.17.739251
- 中文摘要: RSH 酶（RelA/SpoT 同系物）在质体中合成 ppGpp（四磷酸/五磷酸鸟苷），调节细胞器功能。更重要的是，ppGpp 是否充当免疫输出的简单变阻器或决定植物部署哪种防御模式仍知之甚少。使用高（RSH3OX）或无效（rshq）ppGpp水平的拟南芥品系，我们发现ppGpp控制水杨酸（SA）和茉莉酸（JA）代谢中的核编码防御基因，包括RSH3OX中的激素失活酶和rshq中的MeSA-to-SA转换基因。相反，病原体感染诱导 ppGpp 合酶 RSH2 和 RSH3，诱导先于防御基因激活，并需要 SA 生物合成和功能性 III 型分泌系统。 RSH3OX 植物对丁香假单胞菌 pv. 高度敏感。
- Abstract: RSH enzymes (RelA/SpoT homologs) synthesize ppGpp (guanosine tetra-/pentaphosphate) in plastids, regulating organelle function. More importantly, whether ppGpp acts as a simple rheostat on immune output or determines which mode of defence a plant deploys remains poorly understood. Using Arabidopsis thaliana lines with high (RSH3OX) or null (rshq) ppGpp levels, we show that ppGpp controls nuclear-encoded defence gene...
- Summary (fallback): 机器翻译摘要显示：RSH 酶（RelA/SpoT 同系物）在质体中合成 ppGpp（四磷酸/五磷酸鸟苷），调节细胞器功能。更重要的是，ppGpp 是否充当免疫输出的简单变阻器或决定植物部署哪种防御模式仍知之甚少。使用高（RSH3OX）或无效（rshq）ppGpp水平的拟南芥品系，我们发现ppGpp控制水杨酸（SA）和茉莉酸（JA）代谢中的核编码防御基因，包括RSH3OX中的激素失活酶和rshq中的MeSA-to-SA转换基因。相反，病原体感染诱导 ppGpp 合酶 RSH2 和 RSH3，诱导先于防御基因激活，并需要 SA 生物合成和功能性 III 型分泌系统。 RSH3OX 植物对丁香假单胞菌 pv. 高度敏感。
- Keywords: ppgpp, defence, rsh3ox, immune, rshq

### 20. [613 项研究中多元宇宙风格分析的采用和实施](https://www.biorxiv.org/content/10.64898/2026.07.15.738584v1)
- Original title: Uptake and Implementation of Multiverse-style Analyses Across 613 Studies
- Authors: Nepomuceno, A., Ghosal, A., Sandoval Lentisco, A., Ioannidis, J. P. A.
- Meta: 2026-07-20 | scientific communication and education | DOI: 10.64898/2026.07.15.738584
- 中文摘要: 实证结论可能取决于研究人员在分析数据时做出的许多个人选择。多元宇宙风格的分析通过计算一组规范而不是单个规范的结果来解决这个问题，但目前尚不清楚它们的使用范围和实施方式。我们在 Web of Science 核心合集（2026 年 5 月）中搜索了引用六篇关于多元宇宙风格方法不同变体的基础论文的文章，并将每篇引用文章分类为实现此类方法或仅讨论它们。对于实现，我们记录了所使用的框架、规范的数量、四个决策节点（测量、数据处理、建模和估计）中的哪一个是不同的，以及其他方面，例如如何可视化和解释结果。
- Abstract: Empirical conclusions can depend on the many individual choices researchers make when analyzing data. Multiverse-style analyses address this by computing results across a set of specifications rather than a single one, but it is unclear how widely they are being used and how they are being implemented. We searched the Web of Science Core Collection (May 2026) for articles citing six foundational papers on different...
- Summary (fallback): 机器翻译摘要显示：实证结论可能取决于研究人员在分析数据时做出的许多个人选择。多元宇宙风格的分析通过计算一组规范而不是单个规范的结果来解决这个问题，但目前尚不清楚它们的使用范围和实施方式。我们在 Web of Science 核心合集（2026 年 5 月）中搜索了引用六篇关于多元宇宙风格方法不同变体的基础论文的文章，并将每篇引用文章分类为实现此类方法或仅讨论它们。对于实现，我们记录了所使用的框架、规范的数量、四个决策节点（测量、数据处理、建模和估计）中的哪一个是不同的，以及其他方面，例如如何可视化和解释结果。
- Keywords: multiverse-style, analyses, specifications, across, articles

### 21. [NeuroFlow：用于小鼠大脑图谱注册和量化的集成跨平台工作流程](https://www.biorxiv.org/content/10.64898/2026.07.15.737186v1)
- Original title: NeuroFlow: An Integrated, Cross-Platform Workflow for Mouse Brain Atlas Registration and Quantification
- Authors: Rao, A., Oo, H. Z., Tao, C., Zhang, G.-W.
- Meta: 2026-07-20 | neuroscience | DOI: 10.64898/2026.07.15.737186
- 中文摘要: 将组织学切片注册到参考图谱对于解剖定位和基于区域的定量分析至关重要。尽管已建立的工作流程功能强大，但图像准备、配准、量化和可视化通常依赖于多个软件包，其中一些软件包需要特定于平台的安装或本地配置的编程环境。在这里，我们介绍 NeuroFlow，一种基于浏览器的工作流程，用于对小鼠大脑组织学进行定量分析。 NeuroFlow 将图像配准、信号检测、量化和可视化集成在一个界面中，并且可以跨主要操作系统运行，无需安装额外的软件。它支持仿射和非线性对齐，以及参考图集的实时倾斜重新切片。
- Abstract: Registration of histological sections to a reference atlas is essential for anatomical localization and region-based quantitative analysis. Although established workflows are powerful, image preparation, registration, quantification, and visualization often rely on multiple software packages, some of which require platform-specific installation or locally configured programming environments. Here, we present NeuroFl...
- Summary (fallback): 机器翻译摘要显示：将组织学切片注册到参考图谱对于解剖定位和基于区域的定量分析至关重要。尽管已建立的工作流程功能强大，但图像准备、配准、量化和可视化通常依赖于多个软件包，其中一些软件包需要特定于平台的安装或本地配置的编程环境。在这里，我们介绍 NeuroFlow，一种基于浏览器的工作流程，用于对小鼠大脑组织学进行定量分析。 NeuroFlow 将图像配准、信号检测、量化和可视化集成在一个界面中，并且可以跨主要操作系统运行，无需安装额外的软件。它支持仿射和非线性对齐，以及参考图集的实时倾斜重新切片。
- Keywords: neuroflow, registration, atlas, quantification, installation

### 22. [从肉类基质中自动分离 DNA 的分析验证，用于基于 PCR 的高质量食品认证](https://www.biorxiv.org/content/10.64898/2026.07.17.739293v1)
- Original title: Analytical Validation of Automated DNA Isolation from Meat Matrices for High-Quality PCR-Based Food Authentication
- Authors: Dewi, Y. K., Chudori, Y. N.
- Meta: 2026-07-20 | molecular biology | DOI: 10.64898/2026.07.17.739293
- 中文摘要: 可靠的 DNA 分离是基于 PCR 的食品认证的关键先决条件，特别是对于复杂基质可能会影响 DNA 质量和扩增效率的肉类产品。本研究旨在分析验证使用 Qiagen QIAcube Connect 与 DNeasy Mericon Food Kit 结合从肉类基质中自动提取 DNA 的方法。验证参数包括 DNA 浓度、总产量、纯度、完整性以及使用针对猪细胞色素 b 基因的实时 PCR 评估 PCR 抑制剂。该方法产生的平均 DNA 浓度为 219.5 ng/μL，平均产量为 21,519.7 ng，超出了预定的验收标准。琼脂糖凝胶电泳证实 DNA 片段大小大于目标扩增子，表明适合 PCR 分析。
- Abstract: Reliable DNA isolation is a critical prerequisite for PCR based food authentication, particularly for meat products where complex matrices may compromise DNA quality and amplification efficiency. This study aimed to analytically validate an automated DNA extraction method from meat matrices using Qiagen QIAcube Connect in combination with the DNeasy Mericon Food Kit. Validation parameters included DNA concentration,...
- Summary (fallback): 机器翻译摘要显示：可靠的 DNA 分离是基于 PCR 的食品认证的关键先决条件，特别是对于复杂基质可能会影响 DNA 质量和扩增效率的肉类产品。本研究旨在分析验证使用 Qiagen QIAcube Connect 与 DNeasy Mericon Food Kit 结合从肉类基质中自动提取 DNA 的方法。验证参数包括 DNA 浓度、总产量、纯度、完整性以及使用针对猪细胞色素 b 基因的实时 PCR 评估 PCR 抑制剂。该方法产生的平均 DNA 浓度为 219.5 ng/μL，平均产量为 21,519.7 ng，超出了预定的验收标准。琼脂糖凝胶电泳证实 DNA 片段大小大于目标扩增子，表明适合 PCR 分析。
- Keywords: meat, food, automated, matrices, authentication

### 23. [ORC 通过本质上无序的区域与异染色质蛋白 1 结合是异染色质结构和功能所必需的](https://www.biorxiv.org/content/10.64898/2026.07.17.738698v1)
- Original title: ORC binding to Heterochromatin Protein 1 through intrinsically disordered regions is required for heterochromatin structure and function
- Authors: Luo, Y., Rajshekar, S., Kumar, H., Berger, J. M., Karpen, G. et al.
- Meta: 2026-07-20 | molecular biology | DOI: 10.64898/2026.07.17.738698
- 中文摘要: 起源识别复合体 (ORC) 因在真核细胞中启动 DNA 复制而闻名，但越来越多的证据表明 ORC 具有多种功能。在这里，我们表明，黑腹果蝇中两种主要核成分（异染色质和核仁）的组织和功能取决于 Orc1 和异染色质蛋白 1a (HP1a) 之间的多价相互作用。具体来说，结合需要 Orc1 本质无序区域 (IDR) 中的两个短基序（R1 和 R2），以及位于 HP1a N 端和 C 端区域的两个基序（HGM 和 CTE）。这四个基序的配对促进 ORC-HP1 相互作用，这也需要 HP1 二聚化。
- Abstract: The Origin Recognition Complex (ORC) is known for initiating DNA replication in eukaryotic cells, but increasing evidence suggests that ORC has multiple functions. Here we show that the organization and function of two major nuclear components, heterochromatin and the nucleolus, depend on multivalent interactions between Orc1 and Heterochromatin Protein 1a (HP1a) in Drosophila melanogaster. Specifically, binding req...
- Summary (fallback): 机器翻译摘要显示：起源识别复合体 (ORC) 因在真核细胞中启动 DNA 复制而闻名，但越来越多的证据表明 ORC 具有多种功能。在这里，我们表明，黑腹果蝇中两种主要核成分（异染色质和核仁）的组织和功能取决于 Orc1 和异染色质蛋白 1a (HP1a) 之间的多价相互作用。具体来说，结合需要 Orc1 本质无序区域 (IDR) 中的两个短基序（R1 和 R2），以及位于 HP1a N 端和 C 端区域的两个基序（HGM 和 CTE）。这四个基序的配对促进 ORC-HP1 相互作用，这也需要 HP1 二聚化。
- Keywords: heterochromatin, interactions, motifs, regions, binding

### 24. [系统级蛋白质组学分析识别神经元发育过程中 KIFBP 的驱动蛋白靶点](https://www.biorxiv.org/content/10.64898/2026.07.17.739260v1)
- Original title: A systems-level proteomic analysis identifies kinesin targets of KIFBP during neuronal development
- Authors: Paschall, S.-C., Blasius, T. L., Missman, A., Rodriguez, P., Cianfrocco, M. A. et al.
- Meta: 2026-07-20 | cell biology | DOI: 10.64898/2026.07.17.739260
- 中文摘要: 驱动蛋白是在神经元发育和维持过程中组织和重塑细胞骨架所必需的分子运动蛋白。一个关键的调节因子是驱动蛋白家族结合蛋白（KIFBP），它通过阻断运动-微管相互作用来抑制驱动蛋白的子集。 KIFBP 的纯合突变会导致 Goldberg-Shprintzen 综合征 (GOSHS)，这是一种以智力障碍、小头畸形和轴突神经病为特征的神经发育障碍。尽管 KIFBP 缺失与神经突长度缩短和微管解体有关，但这些表型背后的特定驱动蛋白仍不清楚。在这里，我们使用 CRISPR-Cas9 生成的 KIFBP 敲除 Neuro-2a 细胞系来证明 KIFBP 是神经突延伸所必需的，并使用诱导型 GFP-KIFBP 来定义神经元分化过程中的 KIFBP 相互作用组。
- Abstract: Kinesins are molecular motor proteins essential for organizing and remodeling the cytoskeleton during neuronal development and maintenance. One key regulator is kinesin family binding protein (KIFBP), which inhibits a subset of kinesins by blocking motor-microtubule interactions. Homozygous mutations in KIFBP cause Goldberg-Shprintzen Syndrome (GOSHS), a neurodevelopmental disorder characterized by intellectual disa...
- Summary (fallback): 机器翻译摘要显示：驱动蛋白是在神经元发育和维持过程中组织和重塑细胞骨架所必需的分子运动蛋白。一个关键的调节因子是驱动蛋白家族结合蛋白（KIFBP），它通过阻断运动-微管相互作用来抑制驱动蛋白的子集。 KIFBP 的纯合突变会导致 Goldberg-Shprintzen 综合征 (GOSHS)，这是一种以智力障碍、小头畸形和轴突神经病为特征的神经发育障碍。尽管 KIFBP 缺失与神经突长度缩短和微管解体有关，但这些表型背后的特定驱动蛋白仍不清楚。在这里，我们使用 CRISPR-Cas9 生成的 KIFBP 敲除 Neuro-2a 细胞系来证明 KIFBP 是神经突延伸所必需的，并使用诱导型 GFP-KIFBP 来定义神经元分化过程中的 KIFBP 相互作用组。
- Keywords: kifbp, kinesins, neuronal, kinesin, during

### 25. [SGEF 通过调节连接稳定性、集体迁移和细胞外基质重塑来协调上皮形态发生](https://www.biorxiv.org/content/10.64898/2026.07.17.739205v1)
- Original title: SGEF coordinates epithelial morphogenesis by regulating junction stability, collective migration, and extracellular matrix remodeling
- Authors: Lovejoy, M., Rabino, A. F., Gonzalez-Blotta, L., Gangasani, V., Durham, S. M. et al.
- Meta: 2026-07-20 | cell biology | DOI: 10.64898/2026.07.17.739205
- 中文摘要: 极化上皮对于器官功能至关重要，上皮极性的破坏是包括癌症在内的许多疾病的标志。我们之前表明，RhoG 特异性鸟嘌呤核苷酸交换因子 SGEF 与 Scribble 极性复合物相互作用，调节 2D 单层中的上皮连接组装。然而，它在 3D 上皮形态发生和管腔形成中的作用仍然未知。在这里，我们将定量形态分析与长期活细胞成像相结合，研究 SGEF 在 MDCK 囊肿发育过程中的作用。 SGEF KD 破坏了正常的管腔生成，产生具有多个塌陷管腔的增大囊肿，同时 E-钙粘蛋白、{β}-连环蛋白和 ZO-1 表达减少。 SGEF 的缺失也改变了肌动球蛋白网络的分布。
- Abstract: Polarized epithelia are essential for organ function, and disruption of epithelial polarity is a hallmark of many diseases, including cancer. We previously showed that the RhoG-specific guanine nucleotide exchange factor SGEF interacts with the Scribble polarity complex to regulate epithelial junction assembly in 2D monolayers. However, its role in epithelial morphogenesis and lumen formation in 3D remains unknown....
- Summary (fallback): 机器翻译摘要显示：极化上皮对于器官功能至关重要，上皮极性的破坏是包括癌症在内的许多疾病的标志。我们之前表明，RhoG 特异性鸟嘌呤核苷酸交换因子 SGEF 与 Scribble 极性复合物相互作用，调节 2D 单层中的上皮连接组装。然而，它在 3D 上皮形态发生和管腔形成中的作用仍然未知。在这里，我们将定量形态分析与长期活细胞成像相结合，研究 SGEF 在 MDCK 囊肿发育过程中的作用。 SGEF KD 破坏了正常的管腔生成，产生具有多个塌陷管腔的增大囊肿，同时 E-钙粘蛋白、{β}-连环蛋白和 ZO-1 表达减少。 SGEF 的缺失也改变了肌动球蛋白网络的分布。
- Keywords: sgef, epithelial, junction, lumen, cyst

### 26. [桑葚树互补可恢复异种相容 SALL1 缺失羊的胎儿肾脏](https://www.biorxiv.org/content/10.64898/2026.07.17.739226v1)
- Original title: Morula complementation restores fetal kidneys in xenocompatible SALL1 null sheep
- Authors: Appleby, S. J., Fermin, L. M., Delaney, S., Wei, J., Meng, F. et al.
- Meta: 2026-07-20 | cell biology | DOI: 10.64898/2026.07.17.739226
- 中文摘要: 为了满足全球器官短缺的问题，人们进行了广泛的基因组改造，使家畜组织“人性化”，用于异种移植。然而，残留的免疫排斥仍然是一个问题，促使人们探索使用动物作为生长人体器官的宿主的替代方法。这需要基因组编辑来禁用宿主中的器官发生，并用合适的供体细胞进行胚胎互补，以填补嵌合动物中空的器官生态位。猪是这种方法研究的主要牲畜物种。在这里，我们使用家羊作为供体来源的肾脏形成的宿主。 Spalt 样转录因子 1 (SALL1) 被靶向缺乏异种抗原 CMAH 和 GGTA1 的雄性成纤维细胞，使用锌指簇 (ZFC) 2 内的一个 gRNA 或两个 gRNA 来去除所有 ZF 结构域。
- Abstract: To meet the global shortage of organs, extensive genome modifications have been performed to "humanize" livestock tissues for xenotransplantation. However, residual immune rejection remains a problem, prompting alternative approaches that explore the use of animals as hosts for growing human organs. This requires genome editing to disable organogenesis in the host and embryo complementation with suitable donor cells...
- Summary (fallback): 机器翻译摘要显示：为了满足全球器官短缺的问题，人们进行了广泛的基因组改造，使家畜组织“人性化”，用于异种移植。然而，残留的免疫排斥仍然是一个问题，促使人们探索使用动物作为生长人体器官的宿主的替代方法。这需要基因组编辑来禁用宿主中的器官发生，并用合适的供体细胞进行胚胎互补，以填补嵌合动物中空的器官生态位。猪是这种方法研究的主要牲畜物种。在这里，我们使用家羊作为供体来源的肾脏形成的宿主。 Spalt 样转录因子 1 (SALL1) 被靶向缺乏异种抗原 CMAH 和 GGTA1 的雄性成纤维细胞，使用锌指簇 (ZFC) 2 内的一个 gRNA 或两个 gRNA 来去除所有 ZF 结构域。
- Keywords: complementation, sall1, sheep, hosts, morula

### 27. [红狐（Vulpes vulpes）的死亡率和年存活率。](https://www.biorxiv.org/content/10.64898/2026.07.18.739295v1)
- Original title: Mortality causes and annual survival rates of red foxes (Vulpes vulpes).
- Authors: Willebrand, T., Odden, M., Walton, Z., Samelius, G., Ostbye, K. et al.
- Meta: 2026-07-20 | ecology | DOI: 10.64898/2026.07.18.739295
- 中文摘要: 对佩戴 GPS 项圈的动物进行个体跟踪后得出的死亡率和存活率估计提供了可靠的人口统计数据，但对于红狐 Vulpes vulpes 来说，这样的估计很少见。我们使用了 2011 年至 2019 年间在瑞典中部和挪威的纬度梯度上追踪的 126 只戴着 GPS 项圈的红狐的数据，利用 Cox 比例风险模型的 Andersen-Gill 扩展来量化死亡原因并估计每年的生存概率。狩猎是主要的死亡原因（63%），其次是车辆碰撞（14%）、压力或营养不良（11%）、疥疮（9%）和捕食（3%）。成虫的年生存率为 0.58，亚成虫的年生存率为 0.32。亚成体的风险大约是成体的两倍，雄性的风险相对于雌性更高，死亡风险在秋季和初冬最高。
- Abstract: Mortality causes and survival rate estimates from individual follow-ups of GPS-collared animals provide reliable demographic data, but such estimates are rare for red foxes Vulpes vulpes. We used data from 126 GPS-collared red foxes tracked between 2011 and 2019 across a latitudinal gradient in central Sweden and Norway to quantify mortality causes and estimate annual survival probabilities using the Andersen-Gill e...
- Summary (fallback): 机器翻译摘要显示：对佩戴 GPS 项圈的动物进行个体跟踪后得出的死亡率和存活率估计提供了可靠的人口统计数据，但对于红狐 Vulpes vulpes 来说，这样的估计很少见。我们使用了 2011 年至 2019 年间在瑞典中部和挪威的纬度梯度上追踪的 126 只戴着 GPS 项圈的红狐的数据，利用 Cox 比例风险模型的 Andersen-Gill 扩展来量化死亡原因并估计每年的生存概率。狩猎是主要的死亡原因（63%），其次是车辆碰撞（14%）、压力或营养不良（11%）、疥疮（9%）和捕食（3%）。成虫的年生存率为 0.58，亚成虫的年生存率为 0.32。亚成体的风险大约是成体的两倍，雄性的风险相对于雌性更高，死亡风险在秋季和初冬最高。
- Keywords: mortality, foxes, survival, vulpes, estimates

### 28. [使用天然质谱法阐明肠沙门氏菌 FraB 脱糖酶的半位点反应机制](https://www.biorxiv.org/content/10.64898/2026.07.17.739170v1)
- Original title: Elucidating the half-site reactivity mechanism of Salmonella enterica FraB deglycase using native mass spectrometry
- Authors: Gao, Y., Law, J. D., Gopalan, V., Wysocki, V. H.
- Meta: 2026-07-20 | biochemistry | DOI: 10.64898/2026.07.17.739170
- 中文摘要: 亚基间通讯和变构调节是寡聚酶功能的核心，但这些特征仍然难以表征。传统的动力学和结构方法通常产生整体平均值或静态快照，因此很难揭示寡聚酶多位点催化所必需的动态跨亚基合作。在这里，我们研究了沙门氏菌 FraB（一种同型二聚体去糖酶和潜在的药物靶标），展示了结合天然质谱 (nMS)、表面诱导解离 (SID) 和动力学研究的综合方法的价值，以深入了解催化中间体和亚基间通讯。
- Abstract: Inter-subunit communication and allosteric regulation are central to the function of oligomeric enzymes, yet these features remain difficult to characterize. Conventional kinetic and structural methods typically yield ensemble averages or static snapshots, thus making it difficult to uncover the dynamic cross-subunit cooperation obligatory for multi-site catalysis by oligomeric enzymes. Here, we investigate Salmonel...
- Summary (fallback): 机器翻译摘要显示：亚基间通讯和变构调节是寡聚酶功能的核心，但这些特征仍然难以表征。传统的动力学和结构方法通常产生整体平均值或静态快照，因此很难揭示寡聚酶多位点催化所必需的动态跨亚基合作。在这里，我们研究了沙门氏菌 FraB（一种同型二聚体去糖酶和潜在的药物靶标），展示了结合天然质谱 (nMS)、表面诱导解离 (SID) 和动力学研究的综合方法的价值，以深入了解催化中间体和亚基间通讯。
- Keywords: active, frab, inter-subunit, communication, oligomeric

### 29. [通过基于氟磷酸盐活性的蛋白质分析对克氏锥虫丝氨酸组进行功能定位](https://www.biorxiv.org/content/10.64898/2026.07.18.739127v1)
- Original title: Functional Mapping of the Trypanosoma cruzi Serinome by Fluorophosphonate Activity-Based Protein Profiling
- Authors: Isern, J. A., Mediavilla, M. G., Porta, E. O. J., Merli, M. L., Ballari, M. S. et al.
- Meta: 2026-07-20 | biochemistry | DOI: 10.64898/2026.07.18.739127
- 中文摘要: 丝氨酸水解酶 (SH) 是真核生物中最大的酶超家族之一，但它们在克氏锥虫（恰加斯病的病原体）中的作用在很大程度上仍然未知。在这里，我们通过使用一组细胞可渗透的氟膦酸盐（FP）-炔探针将基因组信息计算机模拟与基于全细胞活性的蛋白质分析（ABPP）相结合，报告了克氏锥虫上鞭毛体丝氨酸组的基于活性的化学蛋白质组图谱。全细胞标记后进行无标记定量蛋白质组学 (LFQ-MS)，鉴定出 37 种富集的 SH 样蛋白，其中 35 种具有保守或部分保守的催化三联体/二联体特征，涵盖脂肪酶、肽酶、酯酶和先前未表征的水解酶。这 35 个 SH 约占催化位点管理后保留的 56 个预测 S​​H 的 63%。
- Abstract: Serine hydrolases (SHs) constitute one of the largest enzyme superfamilies in eukaryotes, yet their roles in Trypanosoma cruzi, the causative agent of Chagas disease, remain largely uncharacterized. Here, we report an activity-based chemoproteomic map of the T. cruzi epimastigote serinome by combining genome-informed in silico curation with whole-cell activity-based protein profiling (ABPP) using a panel of cell-per...
- Summary (fallback): 机器翻译摘要显示：丝氨酸水解酶 (SH) 是真核生物中最大的酶超家族之一，但它们在克氏锥虫（恰加斯病的病原体）中的作用在很大程度上仍然未知。在这里，我们通过使用一组细胞可渗透的氟膦酸盐（FP）-炔探针将基因组信息计算机模拟与基于全细胞活性的蛋白质分析（ABPP）相结合，报告了克氏锥虫上鞭毛体丝氨酸组的基于活性的化学蛋白质组图谱。全细胞标记后进行无标记定量蛋白质组学 (LFQ-MS)，鉴定出 37 种富集的 SH 样蛋白，其中 35 种具有保守或部分保守的催化三联体/二联体特征，涵盖脂肪酶、肽酶、酯酶和先前未表征的水解酶。这 35 个 SH 约占催化位点管理后保留的 56 个预测 S​​H 的 63%。
- Keywords: functional, cruzi, activity-based, including, trypanosoma

### 30. [UniFlow：通过可扩展的归一化流统一蛋白质构象系综生成和机器学习力场](https://www.biorxiv.org/content/10.64898/2026.07.17.739266v1)
- Original title: UniFlow: Unifying protein conformational ensemble generation and machine-learned force fields with a scalable normalizing Flow
- Authors: Liu, Y., Chen, M., Lin, G.
- Meta: 2026-07-20 | biochemistry | DOI: 10.64898/2026.07.17.739266
- 中文摘要: 分子动力学（MD）为平衡蛋白质构象能量景观建模提供了一种原则性方法，但其计算成本限制了长时间尺度和更大蛋白质系统的获取。最近，生成蛋白质集成模型和机器学习的粗粒度力场已成为加速构象采样的补充方法。然而，尽管对相同的基础均衡分布进行建模，但它们通常是单独开发的。我们推出了 UniFlow，这是第一个可扩展的生成模型，它将蛋白质集成生成和机器学习的粗粒度力场统一在一个框架内进行分子动力学模拟。 UniFlow 采用内坐标归一化流，支持高效的 i.i.d.采样、精确似然评估以及可微能量和力计算。
- Abstract: Molecular dynamics (MD) provides a principled method for modeling equilibrium protein conformational energy landscapes, but its computational cost limits access to long timescales and larger protein systems. Recently, generative protein ensemble models and machine-learned coarse-grained force fields have emerged as complementary approaches for accelerating conformational sampling. However, they are typically develop...
- Summary (fallback): 机器翻译摘要显示：分子动力学（MD）为平衡蛋白质构象能量景观建模提供了一种原则性方法，但其计算成本限制了长时间尺度和更大蛋白质系统的获取。最近，生成蛋白质集成模型和机器学习的粗粒度力场已成为加速构象采样的补充方法。然而，尽管对相同的基础均衡分布进行建模，但它们通常是单独开发的。我们推出了 UniFlow，这是第一个可扩展的生成模型，它将蛋白质集成生成和机器学习的粗粒度力场统一在一个框架内进行分子动力学模拟。 UniFlow 采用内坐标归一化流，支持高效的 i.i.d.采样、精确似然评估以及可微能量和力计算。
- Keywords: protein, uniflow, ensemble, force, molecular

## medrxiv

### 1. [暴露组学和心血管疾病：机器学习方法的范围审查](https://www.medrxiv.org/content/10.1101/2024.07.19.24310695v4)
- Original title: Exposomics and Cardiovascular Diseases: A Scoping Review of Machine Learning Approaches
- Authors: Argyri, K. D., Gallos, I. K., Amditis, A., Dionysiou, D. D.
- Meta: 2026-07-20 | health informatics | DOI: 10.1101/2024.07.19.24310695
- 中文摘要: 心血管疾病已被确定为世界第一杀手，每年导致超过2000万人死亡。这一事实，加上人们日益认识到暴露组学危险因素对心血管疾病的影响，促使科学界利用机器学习策略作为传统统计流行病学研究的补充方法，这些研究受到暴露组学数据高度异质性和动态性的挑战。这项工作的主要目标是确定关键的相关文献，并概述暴露组学数据的机器学习应用领域的研究广度，重点是心血管疾病。其次，我们的目标是确定共同的限制和未来需要解决的有意义的指令。
- Abstract: Cardiovascular disease has been established as the world's number one killer, causing over 20 million deaths per year. This fact, along with the growing awareness of the impact of exposomic risk factors on cardiovascular diseases, has led the scientific community to leverage machine learning strategies as a complementary approach to traditional statistical epidemiological studies that are challenged by the highly he...
- Summary (fallback): 机器翻译摘要显示：心血管疾病已被确定为世界第一杀手，每年导致超过2000万人死亡。这一事实，加上人们日益认识到暴露组学危险因素对心血管疾病的影响，促使科学界利用机器学习策略作为传统统计流行病学研究的补充方法，这些研究受到暴露组学数据高度异质性和动态性的挑战。这项工作的主要目标是确定关键的相关文献，并概述暴露组学数据的机器学习应用领域的研究广度，重点是心血管疾病。其次，我们的目标是确定共同的限制和未来需要解决的有意义的指令。
- Keywords: cardiovascular, exposomics, diseases, machine, learning

### 2. [模拟合成健康记录以评估疫苗功效的因果推理方法](https://www.medrxiv.org/content/10.64898/2026.07.17.26358308v2)
- Original title: Simulation of synthetic health records for assessment of causal inference methods for vaccine efficacy
- Authors: Velasco Pardo, V., Daines, L., Katikireddi, S. V., Ritchie, L., Robertson, C. et al.
- Meta: 2026-07-20 | infectious diseases | DOI: 10.64898/2026.07.17.26358308
- 中文摘要: 背景 在 COVID-19 大流行期间，公共卫生机构使用近乎实时的观察数据来回答有关疫苗有效性的问题。然而，传统的观察方法不允许从临床数据中得出有关反事实场景的结论。反事实是在替代干预措施下可能发生的结果，可用于正式评估公共卫生干预措施对健康结果的因果影响，同时考虑混杂的影响。理想情况下，个体患者数据用于开发反事实。在治理和隐私限制禁止访问敏感个人数据的情况下，低保真合成数据可能有助于推进方法开发。
- Abstract: Background During the COVID-19 pandemic, public health agencies used near real-time observational data to answer questions regarding vaccine effectiveness. However, traditional observational methods do not allow conclusions regarding counterfactual scenarios to be drawn from clinical data. Counterfactuals, which are outcomes that would have occurred under alternative interventions, can be used to formally assess the...
- Summary (fallback): 机器翻译摘要显示：背景 在 COVID-19 大流行期间，公共卫生机构使用近乎实时的观察数据来回答有关疫苗有效性的问题。然而，传统的观察方法不允许从临床数据中得出有关反事实场景的结论。反事实是在替代干预措施下可能发生的结果，可用于正式评估公共卫生干预措施对健康结果的因果影响，同时考虑混杂的影响。理想情况下，个体患者数据用于开发反事实。在治理和隐私限制禁止访问敏感个人数据的情况下，低保真合成数据可能有助于推进方法开发。
- Keywords: synthetic, confounding, causal, scenarios, health

### 3. [基于小波分解的人体心电图基因组分析](https://www.medrxiv.org/content/10.64898/2026.05.20.26353725v4)
- Original title: Wavelet Decomposition-Based Genomic Analysis of the Human Electrocardiogram
- Authors: Zainana, S., Lauer, L. P., Kiiskinen, T., Tibshirani, R. j., Hastie, T. et al.
- Meta: 2026-07-20 | cardiovascular medicine | DOI: 10.64898/2026.05.20.26353725
- 中文摘要: 心电图 (ECG) 对心脏在多个时间尺度上的电活动进行编码，但标准临床分析将这种丰富的信号分解为少数标量测量值，从而丢弃了大部分波形结构。在这种减少过程中丢失的频率信号是否携带与心血管疾病风险相关的遗传生物信息仍不清楚。在这里，我们使用跨 12 导联和 7 个分解级别的 Daubechies-6 小波分析，将 47,052 名英国白人生物银行参与者的静息 12 导联心电图分解为 84 个特定频率的能量特征，并对每个特征进行独立的全基因组关联分析。
- Abstract: The electrocardiogram (ECG) encodes the electrical activity of the heart across multiple timescales, yet standard clinical analysis collapses this rich signal into a handful of scalar measurements that discard most of the waveform's structure. Whether the frequency signals lost in this reduction carry heritable biological information relevant to cardiovascular disease risk remains unclear. Here we decompose resting...
- Summary (fallback): 机器翻译摘要显示：心电图 (ECG) 对心脏在多个时间尺度上的电活动进行编码，但标准临床分析将这种丰富的信号分解为少数标量测量值，从而丢弃了大部分波形结构。在这种减少过程中丢失的频率信号是否携带与心血管疾病风险相关的遗传生物信息仍不清楚。在这里，我们使用跨 12 导联和 7 个分解级别的 Daubechies-6 小波分析，将 47,052 名英国白人生物银行参与者的静息 12 导联心电图分解为 84 个特定频率的能量特征，并对每个特征进行独立的全基因组关联分析。
- Keywords: genetic, analysis, electrocardiogram, cardiovascular, loci

### 4. [危重儿童经常接受已制定但未使用的药物基因组学指南的药物治疗：综合电子病历和外显子组测序研究的可行发现](https://www.medrxiv.org/content/10.64898/2026.07.16.26358240v1)
- Original title: Critically Ill Children Frequently Receive Medications with Established but Unused Pharmacogenomic Guidelines: Actionable Findings from an Integrated Electronic Medical Record and Exome Sequencing Study
- Authors: Lynch, N., Elefant, N., Revah-Politi, A., Geneslaw, A. S., Beckett, J. et al.
- Meta: 2026-07-20 | genetic and genomic medicine | DOI: 10.64898/2026.07.16.26358240
- 中文摘要: 重要性 药物基因组学 (PGx) 指南可以提高药物疗效并降低毒性，但其在儿科重症监护病房 (PICU) 中的应用在很大程度上仍未得到探索。目的 确定 PICU 中已制定的 PGx 指南使用药物的频率，并评估外显子组测序捕获这些药物的 PGx 表型的能力。设计整合电子病历和外显子组测序数据的回顾性队列研究。设置纽约长老会摩根士丹利儿童医院，一所单中心三级护理儿童医院。参与者 共有 4,939 名儿童入住 PICU（2020 年至 2024 年），192 名儿童入住 PICU 并接受外显子组测序用于研究目的（2015 年至 2023 年）。暴露 需要入住 PICU 的危重疾病。
- Abstract: Importance Pharmacogenomic (PGx) guidelines can improve medication efficacy and reduce toxicity, but their application in pediatric intensive care units (PICUs) remains largely unexplored. Objective To determine the frequency of medications with established PGx guidelines administered in the PICU and assess the capacity of exome sequencing to capture PGx phenotypes for these medications. Design Retrospective cohort...
- Summary (fallback): 机器翻译摘要显示：重要性 药物基因组学 (PGx) 指南可以提高药物疗效并降低毒性，但其在儿科重症监护病房 (PICU) 中的应用在很大程度上仍未得到探索。目的 确定 PICU 中已制定的 PGx 指南使用药物的频率，并评估外显子组测序捕获这些药物的 PGx 表型的能力。设计整合电子病历和外显子组测序数据的回顾性队列研究。设置纽约长老会摩根士丹利儿童医院，一所单中心三级护理儿童医院。参与者 共有 4,939 名儿童入住 PICU（2020 年至 2024 年），192 名儿童入住 PICU 并接受外显子组测序用于研究目的（2015 年至 2023 年）。暴露 需要入住 PICU 的危重疾病。
- Keywords: children, medications, exome, sequencing, guidelines

### 5. [双丝 3D 打印具有嵌入式植入物和可调金属伪影强度的患者特异性 CT 模型](https://www.medrxiv.org/content/10.64898/2026.07.17.26358319v1)
- Original title: Dual-Filament 3D Printing of Patient-Specific CT Phantoms with Embedded Implants and Tunable Metal-Artifact Intensity
- Authors: Pasyar, P., Mei, K., Im, J. Y., Roshkovan, L., Geagan, M. et al.
- Meta: 2026-07-20 | radiology and imaging | DOI: 10.64898/2026.07.17.26358319
- 中文摘要: 摘要背景：矫形螺钉、假肢和牙科硬件等金属植入物会产生束硬化、光子饥饿和条纹伪影，从而降低计算机断层扫描 (CT) 图像质量，而为减轻这些伪影而开发的金属伪影减少 (MAR) 方法需要客观、可重复的基准测试。目的：CT 中 MAR 算法的客观评估因缺乏同时提供解剖学真实背景、已知几何形状的嵌入式植入物以及可控的地面真实参考伪影强度的体模而受到阻碍。我们提出了一种双丝、体素级三维 (3D) 打印方法，可以满足这些要求，并在具有嵌入式矫形脊柱螺钉的临床代表性颈椎病例上展示其功能。
- Abstract: ABSTRACT Background: Metallic implants such as orthopedic screws, prostheses, and dental hardware produce beam-hardening, photon-starvation, and streak artifacts that degrade computed tomography (CT) image quality, and the metal artifact reduction (MAR) methods developed to mitigate them require objective, reproducible benchmarking. Purpose: Objective evaluation of MAR algorithms in CT is hindered by the absence of...
- Summary (fallback): 机器翻译摘要显示：摘要背景：矫形螺钉、假肢和牙科硬件等金属植入物会产生束硬化、光子饥饿和条纹伪影，从而降低计算机断层扫描 (CT) 图像质量，而为减轻这些伪影而开发的金属伪影减少 (MAR) 方法需要客观、可重复的基准测试。目的：CT 中 MAR 算法的客观评估因缺乏同时提供解剖学真实背景、已知几何形状的嵌入式植入物以及可控的地面真实参考伪影强度的体模而受到阻碍。我们提出了一种双丝、体素级三维 (3D) 打印方法，可以满足这些要求，并在具有嵌入式矫形脊柱螺钉的临床代表性颈椎病例上展示其功能。
- Keywords: implants, phantoms, embedded, method, dual-filament

### 6. [关于使用结构 MRI 检测阿尔茨海默病，持续的错误分类告诉我们什么？](https://www.medrxiv.org/content/10.64898/2026.07.17.26358326v1)
- Original title: What Do Persistent Misclassifications Tell Us About Alzheimer's Disease Detection using Structural MRI?
- Authors: Stark, D., Shin, H., Muenster, N., Federmann, L., Ritter, K. et al.
- Meta: 2026-07-20 | neurology | DOI: 10.64898/2026.07.17.26358326
- 中文摘要: 应用于结构 MRI (sMRI) 的深度学习分类器在检测阿尔茨海默病 (AD) 方面取得了高性能，但对其失效模式的系统研究仍然有限。在这项研究中，我们训练了两种深度学习架构，使用 ADNI 数据集中的 sMRI 数据对认知正常 (CN) 参与者进行 AD 分类，并检查模型和训练配置中是否存在错误分类。我们确定了在 100 个模型实例中持续被错误分类的受试者亚组，并发现这些受试者与正确分类的 AD 病例相比表现出明显不同的萎缩亚型分布，其中海马保留亚型和最小萎缩亚型显着丰富。
- Abstract: Deep learning classifiers applied to structural MRI (sMRI) have achieved high performance in detecting Alzheimer's Disease (AD), yet systematic investigation of their failure modes remains limited. In this study, we trained two deep learning architectures to classify AD from cognitively normal (CN) participants using sMRI data from the ADNI dataset, and examined whether misclassifications persist across models and t...
- Summary (fallback): 机器翻译摘要显示：应用于结构 MRI (sMRI) 的深度学习分类器在检测阿尔茨海默病 (AD) 方面取得了高性能，但对其失效模式的系统研究仍然有限。在这项研究中，我们训练了两种深度学习架构，使用 ADNI 数据集中的 sMRI 数据对认知正常 (CN) 参与者进行 AD 分类，并检查模型和训练配置中是否存在错误分类。我们确定了在 100 个模型实例中持续被错误分类的受试者亚组，并发现这些受试者与正确分类的 AD 病例相比表现出明显不同的萎缩亚型分布，其中海马保留亚型和最小萎缩亚型显着丰富。
- Keywords: disease, persistent, whether, subjects, misclassifications

### 7. [Hume Pod 生物阻抗分析仪用于身体成分评估的有效性和重测可靠性](https://www.medrxiv.org/content/10.64898/2026.07.17.26358337v1)
- Original title: Validity and Test-Retest Reliability of the Hume Pod Bioimpedance Analyzer for Body Composition Assessment
- Authors: Tinsley, G. M., Velasquez, C. M., Florez, C. M., Way, A. E., Sullivan, M. H. et al.
- Meta: 2026-07-20 | nutrition | DOI: 10.64898/2026.07.17.26358337
- 中文摘要: 消费级生物电阻抗分析仪已广泛用于身体成分评估，但其准确性在不同设备上存在很大差异。 Hume Pod 是一种流行的消费级分析仪，号称高度准确，但缺乏独立验证。本研究的目的是评估 Hume Pod 相对于四室 (4C) 模型和双能 X 射线吸收测定法 (DXA) 的可靠性和有效性。 67 名成年人（42 名女性，25 名男性；年龄 37.2 +/- 13.5 岁，体重指数：24.6 +/- 4.9 kg/m2，体脂百分比 [BF%]：26.4 +/- 10.2%）完成了重复的 Hume Pod 评估以及 DXA 和 4C 评估。使用测量技术误差（TEM）和组内相关系数（ICC）来评估可靠性。
- Abstract: Consumer-grade bioelectrical impedance analyzers have become widely used for body composition assessment, yet their accuracy varies considerably across devices. The Hume Pod is a popular consumer-grade analyzer marketed as being highly accurate, but independent validation is lacking. The purpose of this study was to evaluate the reliability and validity of the Hume Pod relative to both a four-compartment (4C) model...
- Summary (fallback): 机器翻译摘要显示：消费级生物电阻抗分析仪已广泛用于身体成分评估，但其准确性在不同设备上存在很大差异。 Hume Pod 是一种流行的消费级分析仪，号称高度准确，但缺乏独立验证。本研究的目的是评估 Hume Pod 相对于四室 (4C) 模型和双能 X 射线吸收测定法 (DXA) 的可靠性和有效性。 67 名成年人（42 名女性，25 名男性；年龄 37.2 +/- 13.5 岁，体重指数：24.6 +/- 4.9 kg/m2，体脂百分比 [BF%]：26.4 +/- 10.2%）完成了重复的 Hume Pod 评估以及 DXA 和 4C 评估。使用测量技术误差（TEM）和组内相关系数（ICC）来评估可靠性。
- Keywords: hume, body, reliability, validity, composition

### 8. [免疫组织定义了乳腺癌的适应性免疫能力和临床结果](https://www.medrxiv.org/content/10.64898/2026.07.17.26358324v1)
- Original title: Immune organization defines adaptive immune competence and clinical outcome in breast cancer
- Authors: Sanfeliu, E., Segui, E., Martinez-Romero, A., Albarran-Fernandez, V., Pascual, T. et al.
- Meta: 2026-07-20 | oncology | DOI: 10.64898/2026.07.17.26358324
- 中文摘要: 肿瘤浸润淋巴细胞（TIL）广泛用于评估乳腺癌的抗肿瘤免疫，但可能无法反映适应性免疫反应的功能能力。我们表明，由三级淋巴结构（TLS）和协调的体液和细胞免疫程序反映的免疫组织代表了淋巴细胞丰度之外的肿瘤免疫的独特维度。通过整合多个乳腺癌队列的组织学、转录组学、空间和免疫受体谱分析，我们发现免疫组织与更大的免疫库多样性、治疗诱导的克隆选择的证据以及改善的临床结果相关，而与免疫浸润无关。免疫组织的转录组测量在外部队列中保留了独立的预后价值，而免疫浸润的测量则没有。
- Abstract: Tumor-infiltrating lymphocytes (TILs) are widely used to assess antitumor immunity in breast cancer but may not reflect the functional competence of adaptive immune responses. We show that immune organization, reflected by tertiary lymphoid structures (TLS) and coordinated humoral and cellular immune programs, represents a distinct dimension of tumor immunity beyond lymphocyte abundance. By integrating histologic, t...
- Summary (fallback): 机器翻译摘要显示：肿瘤浸润淋巴细胞（TIL）广泛用于评估乳腺癌的抗肿瘤免疫，但可能无法反映适应性免疫反应的功能能力。我们表明，由三级淋巴结构（TLS）和协调的体液和细胞免疫程序反映的免疫组织代表了淋巴细胞丰度之外的肿瘤免疫的独特维度。通过整合多个乳腺癌队列的组织学、转录组学、空间和免疫受体谱分析，我们发现免疫组织与更大的免疫库多样性、治疗诱导的克隆选择的证据以及改善的临床结果相关，而与免疫浸润无关。免疫组织的转录组测量在外部队列中保留了独立的预后价值，而免疫浸润的测量则没有。
- Keywords: immune, organization, breast, cancer, adaptive

### 9. [行为准备度而非人口统计数据预测了可穿戴设备在多元化跨国人群中的采用和数字医疗整合：一项针对卡塔尔 3,004 名成年人的横断面研究](https://www.medrxiv.org/content/10.64898/2026.07.17.26358328v1)
- Original title: Behavioural readiness, not demographics, predicts wearable adoption and digital medicine integration in a diverse multinational population: a cross-sectional study of 3,004 adults in Qatar
- Authors: Zaghloul, H., Arabi, B., Al-Ani, M., Abdullah, A., El-Masri, R. et al.
- Meta: 2026-07-20 | health informatics | DOI: 10.64898/2026.07.17.26358328
- 中文摘要: 西方环境之外的不同人群在行为上是否准备好将可穿戴设备衍生的数据整合到临床护理中仍然知之甚少。这项研究探讨了卡塔尔庞大且高度多样化的跨国人口中可穿戴设备采用和数字健康数据共享准备情况的社会技术决定因素，卡塔尔是一个快速数字化的健康生态系统，拥有先进的电子医疗基础设施。我们对卡塔尔 3,004 名成年人进行了一项基于社区的横断面调查，评估可穿戴设备的使用情况、行为参与度以及将可穿戴设备生成的数据集成到医疗保健工作流程中的意愿。多变量逻辑回归确定了可穿戴设备采用的独立预测因素。可穿戴设备的使用率为 34.1%。
- Abstract: Whether diverse populations outside Western settings are behaviourally ready to integrate wearable-derived data into clinical care remains poorly understood. This study examines sociotechnical determinants of wearable adoption and digital health data-sharing readiness in a large, highly diverse multinational population in Qatar, a rapidly digitising health ecosystem with advanced eHealth infrastructure. We conducted...
- Summary (fallback): 机器翻译摘要显示：西方环境之外的不同人群在行为上是否准备好将可穿戴设备衍生的数据整合到临床护理中仍然知之甚少。这项研究探讨了卡塔尔庞大且高度多样化的跨国人口中可穿戴设备采用和数字健康数据共享准备情况的社会技术决定因素，卡塔尔是一个快速数字化的健康生态系统，拥有先进的电子医疗基础设施。我们对卡塔尔 3,004 名成年人进行了一项基于社区的横断面调查，评估可穿戴设备的使用情况、行为参与度以及将可穿戴设备生成的数据集成到医疗保健工作流程中的意愿。多变量逻辑回归确定了可穿戴设备采用的独立预测因素。可穿戴设备的使用率为 34.1%。
- Keywords: wearable, digital, adoption, behavioural, health

### 10. [巴门达地区医院新近接受护理的艾滋病毒感染者的死亡率和相关因素：一项回顾性队列研究](https://www.medrxiv.org/content/10.64898/2026.07.17.26358304v1)
- Original title: Mortality and associated factors among people living with HIV newly initiated into care at Bamenda Regional Hospital: A Retrospective Cohort Study
- Authors: Ajamah, F., Zefack, J. T., Mengnjo, L. T., Yongwa, O., Ashu, M. A. et al.
- Meta: 2026-07-20 | hiv aids | DOI: 10.64898/2026.07.17.26358304
- 中文摘要: 简介 据报道，在全球和非洲，艾滋病毒死亡率多年来有所下降。 2023年喀麦隆全国死亡率为1.7%，存在地区差异和漏报情况。我们评估了 2021 年 1 月至 2023 年 12 月在巴门达地区医院 (BRH) 开始接受艾滋病毒护理的艾滋病毒感染者 (PLHIV) 的死亡率和相关因素。 方法 2024 年 6 月至 2024 年 12 月在巴门达地区医院 (BRH) 进行了一项回顾性队列研究。使用非概率连续抽样技术，纳入了 331 名新开始接受 ART 的参与者。使用问卷从医疗记录中收集数据，并使用 R 软件版本 4.3.1 进行分析。多变量 Cox 回归模型包含显示统计显着性的变量，并评估其与死亡率的关系，同时调整潜在的混杂因素。
- Abstract: Introduction Globally and in Africa, HIV mortality is reported to have decreased over the years. Cameroon's national mortality rate was 1.7% in 2023, and there exist regional disparities and underreporting. We assessed the mortality and associated factors among People Living with HIV(PLHIV) initiated into HIV care from January 2021 to December 2023 at the Bamenda regional hospital (BRH) Methods A retrospective cohor...
- Summary (fallback): 机器翻译摘要显示：简介 据报道，在全球和非洲，艾滋病毒死亡率多年来有所下降。 2023年喀麦隆全国死亡率为1.7%，存在地区差异和漏报情况。我们评估了 2021 年 1 月至 2023 年 12 月在巴门达地区医院 (BRH) 开始接受艾滋病毒护理的艾滋病毒感染者 (PLHIV) 的死亡率和相关因素。 方法 2024 年 6 月至 2024 年 12 月在巴门达地区医院 (BRH) 进行了一项回顾性队列研究。使用非概率连续抽样技术，纳入了 331 名新开始接受 ART 的参与者。使用问卷从医疗记录中收集数据，并使用 R 软件版本 4.3.1 进行分析。多变量 Cox 回归模型包含显示统计显着性的变量，并评估其与死亡率的关系，同时调整潜在的混杂因素。
- Keywords: mortality, opportunistic, associated, initiated, regional

### 11. [亚组分类准确性对检测金黄色葡萄球菌菌血症异质性治疗效果的影响：模拟研究](https://www.medrxiv.org/content/10.64898/2026.07.17.26357924v1)
- Original title: Impact of subgroup classification accuracy on detecting heterogeneous treatment effects in Staphylococcus aureus bacteraemia: A simulation study
- Authors: Hamilton, F. W., Ong, S. Y., Swets, M., Russell, C. D., Underwood, J.
- Meta: 2026-07-20 | infectious diseases | DOI: 10.64898/2026.07.17.26357924
- 中文摘要: 背景 金黄色葡萄球菌菌血症 (SAB) 具有临床异质性。最近通过对患者亚组的分析，使用常规临床变量确定了潜在的异质治疗效果 (HTE)。然而，将患者错误分类到这些组中的影响尚不清楚，改善 HTE 检测的实际策略仍不确定。方法 我们使用 SAB 中选定的随机试验和观察性研究的已发表数据进行了模拟研究。我们评估了 HTE 事后分析中不同分类准确度 (70%-100%) 对 i) 功效、ii) I 类错误和 iii) 偏差的影响。然后，我们评估了两种提高性能的策略：富集设计，其中只有预测属于目标亚组的患者被随机化，以及使用序数结果而不是二元结果。
- Abstract: Background Staphylococcus aureus bacteraemia (SAB) is clinically heterogeneous. Potential heterogeneous treatment effects (HTE) have recently been identified through analysis of patient subgroups, identified using routine clinical variables.However, the impact of misclassifying patients into these groups is unclear, and practical strategies to improve HTE detection remain uncertain. Methods We performed a simulation...
- Summary (fallback): 机器翻译摘要显示：背景 金黄色葡萄球菌菌血症 (SAB) 具有临床异质性。最近通过对患者亚组的分析，使用常规临床变量确定了潜在的异质治疗效果 (HTE)。然而，将患者错误分类到这些组中的影响尚不清楚，改善 HTE 检测的实际策略仍不确定。方法 我们使用 SAB 中选定的随机试验和观察性研究的已发表数据进行了模拟研究。我们评估了 HTE 事后分析中不同分类准确度 (70%-100%) 对 i) 功效、ii) I 类错误和 iii) 偏差的影响。然后，我们评估了两种提高性能的策略：富集设计，其中只有预测属于目标亚组的患者被随机化，以及使用序数结果而不是二元结果。
- Keywords: subgroup, classification, heterogeneous, treatment, power

### 12. [机器学习模型可提高血培养检测的针对性](https://www.medrxiv.org/content/10.64898/2026.07.17.26358320v1)
- Original title: Machine learning models to improve targeting of blood culture testing
- Authors: Forrest-Hammond, R. W., Gupta, R., McVean, G., Noursadeghi, M., O'Grady, J. et al.
- Meta: 2026-07-20 | infectious diseases | DOI: 10.64898/2026.07.17.26358320
- 中文摘要: 背景 血流感染是死亡的主要原因，但主要检测方法血培养的阳性率较低 (<10%)，且检测时间为 24 - 48 小时。许多是从感染风险较低的患者身上采集的，而一些血液感染诊断较晚或完全被漏诊。我们的目标是开发和外部验证机器学习模型，以提高血培养测试的针对性。方法 在这项回顾性队列研究中，我们使用了 2016 年 1 月 1 日至 2025 年 3 月 17 日期间从大型多站点 NHS 信托基金（牛津大学医院；牛津​​郡感染研究数据库）培养物收集中常规收集的临床和实验室数据。所有取自成人和儿童的血培养物均包括在内。
- Abstract: Background Bloodstream infections are a major cause of mortality, yet the primary testing method, blood cultures, have low positivity (<10%) and turnaround times of 24 - 48 hours. Many are taken from patients at low risk of infection, while some bloodstream infections are diagnosed late or missed entirely. We aimed to develop and externally validate machine learning models to improve targeting of blood culture testi...
- Summary (fallback): 机器翻译摘要显示：背景 血流感染是死亡的主要原因，但主要检测方法血培养的阳性率较低 (<10%)，且检测时间为 24 - 48 小时。许多是从感染风险较低的患者身上采集的，而一些血液感染诊断较晚或完全被漏诊。我们的目标是开发和外部验证机器学习模型，以提高血培养测试的针对性。方法 在这项回顾性队列研究中，我们使用了 2016 年 1 月 1 日至 2025 年 3 月 17 日期间从大型多站点 NHS 信托基金（牛津大学医院；牛津​​郡感染研究数据库）培养物收集中常规收集的临床和实验室数据。所有取自成人和儿童的血培养物均包括在内。
- Keywords: blood, culture, cultures, testing, machine

### 13. [冠心病的性别和种族差异：基于英国的三种族队列分析](https://www.medrxiv.org/content/10.64898/2026.07.17.26357977v1)
- Original title: Sex and ethnicity differences in coronary heart disease: A UK-based tri-ethnic cohort analysis
- Authors: Smeeth, D., Eastwood, S. V., Wong, A., Hughes, A. D., Chaturvedi, N.
- Meta: 2026-07-20 | cardiovascular medicine | DOI: 10.64898/2026.07.17.26357977
- 中文摘要: 背景和目的：少数民族冠心病（CHD）风险的性别差异常常被忽视。在这里，我们的目的是探讨先心病结局的性别与种族差异以及危险因素的影响。方法：在英国索撒尔和布伦特重访 (SABRE) 队列中，确定了欧洲人、南亚和非洲/非洲加勒比第一代移民的冠心病事件。在基线（1988-91）评估心血管危险因素。 Cox 比例风险模型量化了 CHD 发病率和危险因素贡献的群体差异。人群归因分数（PAF）描述了风险因素对群体差异的贡献。结果：在 4,754 名参与者中进行了 40.8 年的随访，其中发生了 1,710 起先心病事件。
- Abstract: Background and aims: Sex differences in ethnic minority risk of coronary heart disease (CHD) are often overlooked. Here we aim to explore sex-by-ethnicity differences in CHD outcomes and the contribution of risk factors. Methods: Incident CHD events were identified for Europeans, and South Asian and African/African Caribbean first generation migrants in the UK-based Southall and Brent Revisited (SABRE) cohort. Cardi...
- Summary (fallback): 机器翻译摘要显示：背景和目的：少数民族冠心病（CHD）风险的性别差异常常被忽视。在这里，我们的目的是探讨先心病结局的性别与种族差异以及危险因素的影响。方法：在英国索撒尔和布伦特重访 (SABRE) 队列中，确定了欧洲人、南亚和非洲/非洲加勒比第一代移民的冠心病事件。在基线（1988-91）评估心血管危险因素。 Cox 比例风险模型量化了 CHD 发病率和危险因素贡献的群体差异。人群归因分数（PAF）描述了风险因素对群体差异的贡献。结果：在 4,754 名参与者中进行了 40.8 年的随访，其中发生了 1,710 起先心病事件。
- Keywords: risk, differences, south, contribution, asian

### 14. [儿科血培养中菌血症与污染物决策规则的外部验证](https://www.medrxiv.org/content/10.64898/2026.07.17.26358300v1)
- Original title: External validation of a decision rule for bacteremia vs contaminants in pediatric blood cultures
- Authors: DAmours-Gravel, M., Charvet, A., Ibanez Miguel, C., Rouxel, N., Fontaine, C. et al.
- Meta: 2026-07-20 | emergency medicine | DOI: 10.64898/2026.07.17.26358300
- 中文摘要: 背景：儿科急诊科（PED）中一半的阳性血培养物代表污染物，导致不必要的住院、抗生素暴露和重复就诊。 CHU Sainte-Justine 制定的临床决策规则显示区分菌血症和污染物的灵敏度为 99%，特异性为 60%，但尚未经过外部验证。我们试图在一个独立的儿科队列中验证这一规则。方法：这项回顾性诊断研究从 2015 年 1 月到 2025 年 5 月在瑞士的一家三级 PED 进行，使用了 16 岁以下患者的阳性血培养。四个预测因子（成对或链状革兰氏阴性菌或革兰氏阳性球菌；阳性时间<17小时；留置装置；疑似骨关节感染）将每个病例分为低、中或高风险。
- Abstract: BACKGROUND: Half of positive blood cultures in pediatric emergency departments (PEDs) represent contaminants, driving unnecessary hospitalization, antibiotic exposure, and repeat visits. A clinical decision rule derived at CHU Sainte-Justine showed 99% sensitivity and 60% specificity for distinguishing bacteremia from contaminants but had not been externally validated. We sought to validate this rule in an independe...
- Summary (fallback): 机器翻译摘要显示：背景：儿科急诊科（PED）中一半的阳性血培养物代表污染物，导致不必要的住院、抗生素暴露和重复就诊。 CHU Sainte-Justine 制定的临床决策规则显示区分菌血症和污染物的灵敏度为 99%，特异性为 60%，但尚未经过外部验证。我们试图在一个独立的儿科队列中验证这一规则。方法：这项回顾性诊断研究从 2015 年 1 月到 2025 年 5 月在瑞士的一家三级 PED 进行，使用了 16 岁以下患者的阳性血培养。四个预测因子（成对或链状革兰氏阴性菌或革兰氏阳性球菌；阳性时间<17小时；留置装置；疑似骨关节感染）将每个病例分为低、中或高风险。
- Keywords: rule, bacteremia, contaminants, pediatric, validation

### 15. [唐氏综合症患者的死亡：美国医疗补助和医疗保险登记成人的死亡率统计数据和新的预测因素。](https://www.medrxiv.org/content/10.64898/2026.07.17.26358090v1)
- Original title: Death in People with Down syndrome: Mortality statistics and novel predictors in US Medicaid and Medicare enrolled adults.
- Authors: Tewolde, S., Rosellini, A. J., Michals, A., Skotko, B. G., Fortea, J. et al.
- Meta: 2026-07-20 | epidemiology | DOI: 10.64898/2026.07.17.26358090
- 中文摘要: 与普通人群以及患有其他智力和发育障碍的同龄人相比，唐氏综合症患者的特定年龄死亡率更高。虽然很大一部分死亡归因于阿尔茨海默病，但许多人在诊断出阿尔茨海默病之前就已死亡，还有一些人活到老年，但在没有患阿尔茨海默病的情况下死去。我们的目标是使用 11 年的医疗补助和医疗保险数据来描述与唐氏综合症成人死亡相关的特征和因素，并使用机器学习来确定哪些情况最能预测整个人群的死亡并按年龄分层。我们使用医疗保险和医疗补助系统中心使用 ICD 9 和 10 代码报告的死亡健康状况日期来确定死亡。我们使用了带有风险集抽样的病例对照设计，以通过控制来模拟阿尔茨海默病的发病时间分布。
- Abstract: People with Down syndrome have higher age-specific mortality rates compared to the general population as well as peers with other intellectual and developmental disabilities. While a large proportion of mortality is attributable to Alzheimers disease, many die prior to Alzheimers diagnosis and some live to old ages, dying without Alzheimers. Our objectives were to use 11 years of Medicaid and Medicare data to descri...
- Summary (fallback): 机器翻译摘要显示：与普通人群以及患有其他智力和发育障碍的同龄人相比，唐氏综合症患者的特定年龄死亡率更高。虽然很大一部分死亡归因于阿尔茨海默病，但许多人在诊断出阿尔茨海默病之前就已死亡，还有一些人活到老年，但在没有患阿尔茨海默病的情况下死去。我们的目标是使用 11 年的医疗补助和医疗保险数据来描述与唐氏综合症成人死亡相关的特征和因素，并使用机器学习来确定哪些情况最能预测整个人群的死亡并按年龄分层。我们使用医疗保险和医疗补助系统中心使用 ICD 9 和 10 代码报告的死亡健康状况日期来确定死亡。我们使用了带有风险集抽样的病例对照设计，以通过控制来模拟阿尔茨海默病的发病时间分布。
- Keywords: death, down, syndrome, mortality, alzheimers

### 16. [通过肯塔基州注射器残留物分析确定掺杂物和多物质使用研究重点](https://www.medrxiv.org/content/10.64898/2026.07.17.26358092v1)
- Original title: Characterizing Adulterant and Polysubstance Use Research Priorities through Syringe Residue Analysis in Kentucky
- Authors: McNealy, K. R., Tolbert, P. T., Ward, M., Byczek, K., Harpe, K. et al.
- Meta: 2026-07-20 | epidemiology | DOI: 10.64898/2026.07.17.26358092
- 中文摘要: 多物质的使用正在增加，并与服药过量率升高和治疗挑战增加有关，而街头毒品供应中掺假物（例如甲苯噻嗪）的检测增加进一步加剧了这种情况。减低危害团体提供无菌注射器以换取用过的注射器，创造了一个独特的机会来表征普遍的多物质组合并为转化和临床前研究提供信息我们使用气相色谱质谱法 (GC-MS) 分析了从肯塔基州杰斐逊县的几个减低危害组织（2025 年 1 月至 12 月）获得的旧注射器 (N = 3,168) 的残留物中是否存在物质。我们将化合物分类为掺假物（例如苯海拉明 [DPH]/苯海拉明）、合成副产品/前体（例如 4-ANPP）和消遣性毒品（例如冰毒）。
- Abstract: Polysubstance use is rising and linked to heightened overdose rates and increased treatment challenges, further exacerbated by increasing detection of adulterants (e.g., xylazine) in the street drug supply. Harm reduction groups provide sterile syringes in exchange for used ones, creating a unique opportunity to characterize prevalent polysubstance combinations and inform translational and preclinical research We an...
- Summary (fallback): 机器翻译摘要显示：多物质的使用正在增加，并与服药过量率升高和治疗挑战增加有关，而街头毒品供应中掺假物（例如甲苯噻嗪）的检测增加进一步加剧了这种情况。减低危害团体提供无菌注射器以换取用过的注射器，创造了一个独特的机会来表征普遍的多物质组合并为转化和临床前研究提供信息我们使用气相色谱质谱法 (GC-MS) 分析了从肯塔基州杰斐逊县的几个减低危害组织（2025 年 1 月至 12 月）获得的旧注射器 (N = 3,168) 的残留物中是否存在物质。我们将化合物分类为掺假物（例如苯海拉明 [DPH]/苯海拉明）、合成副产品/前体（例如 4-ANPP）和消遣性毒品（例如冰毒）。
- Keywords: fentanyl, polysubstance, lidocaine, meth, heroin

### 17. [祖先校准的多基因风险评分可预测近期创伤幸存者的 PTSD 轨迹并与社区资源互动](https://www.medrxiv.org/content/10.64898/2026.07.17.26358149v1)
- Original title: Ancestry-Calibrated Polygenic Risk Scores Predict PTSD Trajectories in Recent Trauma Survivors and Interact with Neighborhood Resources
- Authors: Webb, E. K., Jajoo, A., Balakundi, V., Sendi, M. S. E., Koenen, K. C. et al.
- Meta: 2026-07-20 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.17.26358149
- 中文摘要: 目的：创伤后应激障碍 (PTSD) 的多基因风险评分 (PRS) 通常解释的方差较小。 PRS 量表和方差中与祖先相关的差异限制了跨组比较。鉴于社会环境暴露在不同种族群体中分布不均，这一方法论挑战进一步使基因环境（GxE）分析变得复杂。我们在迄今为止最大的创伤幸存者纵向研究中构建了 PTSD 的祖先校准多基因风险评分 (AC-PRS)，并调查了 GxE 相互作用。方法：最近的创伤幸存者 (N=1,801) 提供了一份血液样本用于基因分型。先前从创伤后 2 周、8 周、3 个月和 6 个月的 DSM-5 (PCL-5) 分数 PTSD 检查表中确定了 6 个 PTSD 轨迹。
- Abstract: Objective: Polygenic risk scores (PRS) for posttraumatic stress disorder (PTSD) often account for a low amount of variance. Ancestry-related differences in PRS scale and variance limit cross-group comparisons. This methodological challenge further complicates gene-by-environment (GxE) analyses, given that socioenvironmental exposures are inequitably distributed across ethnoracial groups. We constructed an ancestry-c...
- Summary (fallback): 机器翻译摘要显示：目的：创伤后应激障碍 (PTSD) 的多基因风险评分 (PRS) 通常解释的方差较小。 PRS 量表和方差中与祖先相关的差异限制了跨组比较。鉴于社会环境暴露在不同种族群体中分布不均，这一方法论挑战进一步使基因环境（GxE）分析变得复杂。我们在迄今为止最大的创伤幸存者纵向研究中构建了 PTSD 的祖先校准多基因风险评分 (AC-PRS)，并调查了 GxE 相互作用。方法：最近的创伤幸存者 (N=1,801) 提供了一份血液样本用于基因分型。先前从创伤后 2 周、8 周、3 个月和 6 个月的 DSM-5 (PCL-5) 分数 PTSD 检查表中确定了 6 个 PTSD 轨迹。
- Keywords: ptsd, ac-prs, scores, risk, trajectories

### 18. [制定创伤性脑损伤 (TBI) 数字健康全球框架：临床医生对在 TBI 护理途径中使用数字技术的看法](https://www.medrxiv.org/content/10.64898/2026.07.17.26358327v1)
- Original title: Developing a Global Framework for Digital Health in Traumatic Brain Injury (TBI): Clinician Perspectives of the Use of Digital Technologies in the TBI Care Pathway
- Authors: Mantle, O., Smith, B. G., Whiffin, C., Hobbs, L., Penmetcha, V. et al.
- Meta: 2026-07-20 | public and global health | DOI: 10.64898/2026.07.17.26358327
- 中文摘要: 背景 创伤性脑损伤 (TBI) 每年影响全球 6900 万人，但护理仍然分散在复杂、多专业的途径和环境中。数字医疗技术提供了弥合护理差距的潜力，特别是在资源有限的环境中，但现有框架未能充分解决 TBI 护理途径的复杂性或护理发生的多样化全球背景。方法 通过国家健康与护理研究所获得性脑和脊柱损伤全球健康研究小组 (NIHR ABSI) 合作中心、社交媒体和社会通讯，对国际上招募的执业神经外科医生进行了一项横断面定性研究，使用批判性现实主义主题分析。
- Abstract: Background Traumatic brain injury (TBI) affects 69 million individuals globally each year, yet care remains fragmented across complex, multi-specialty pathways and settings. Digital health technologies offer potential to bridge care gaps, particularly in resource-limited settings, yet existing frameworks do not adequately address the complexities of the TBI care pathway or the diverse global contexts in which care o...
- Summary (fallback): 机器翻译摘要显示：背景 创伤性脑损伤 (TBI) 每年影响全球 6900 万人，但护理仍然分散在复杂、多专业的途径和环境中。数字医疗技术提供了弥合护理差距的潜力，特别是在资源有限的环境中，但现有框架未能充分解决 TBI 护理途径的复杂性或护理发生的多样化全球背景。方法 通过国家健康与护理研究所获得性脑和脊柱损伤全球健康研究小组 (NIHR ABSI) 合作中心、社交媒体和社会通讯，对国际上招募的执业神经外科医生进行了一项横断面定性研究，使用批判性现实主义主题分析。
- Keywords: care, digital, health, technology, global

### 19. [斯威士兰艾滋病毒感染者与艾滋病毒阴性成年人的高血压相关心血管疾病预计负担](https://www.medrxiv.org/content/10.64898/2026.07.17.26358301v1)
- Original title: Projected burden of hypertension-associated cardiovascular disease in people living with HIV versus HIV-negative adults in Eswatini
- Authors: Milali, M. P., Citron, D. T., Bhamidipati, K., Yamamoto, N., Osei-Ntansah, A. et al.
- Meta: 2026-07-20 | public and global health | DOI: 10.64898/2026.07.17.26358301
- 中文摘要: 背景 在实现联合国艾滋病规划署 95-95-95 目标后，斯威士兰面临着日益沉重的非传染性疾病负担，这些疾病是发病率和死亡率的主要原因。随着生存率的提高和代谢风险（包括与多替拉韦 (DTG) 相关的风险）的增加，艾滋病毒感染者 (PLHIV) 中与高血压相关的心血管疾病 (CVD) 呈上升趋势。我们预测了 2045 年 PLHIV 和 HIV 阴性成人 (PLWHIV) 的 CVD 负担，以便为 HIV-CVD 综合规划提供信息。方法 EMOD-HIV 是一种针对斯威士兰流行病进行校准的基于主体的模型，可生成 HIV 流行轨迹。这些与年龄标准化的全球 CVD 疾病负担估计和发布的相对风险 (RR) 相结合，以产生 HIV 分层的 CVD 预测。
- Abstract: Background Having achieved the UNAIDS 95-95-95 targets, Eswatini faces a growing burden of non-communicable diseases which are major contributors to morbidity and mortality. Hypertension-associated cardiovascular disease (CVD) is rising among people living with HIV (PLHIV) as survival improves and metabolic risks - including those linked to dolutegravir (DTG) - increase. We projected CVD burden among PLHIV and HIV-n...
- Summary (fallback): 机器翻译摘要显示：背景 在实现联合国艾滋病规划署 95-95-95 目标后，斯威士兰面临着日益沉重的非传染性疾病负担，这些疾病是发病率和死亡率的主要原因。随着生存率的提高和代谢风险（包括与多替拉韦 (DTG) 相关的风险）的增加，艾滋病毒感染者 (PLHIV) 中与高血压相关的心血管疾病 (CVD) 呈上升趋势。我们预测了 2045 年 PLHIV 和 HIV 阴性成人 (PLWHIV) 的 CVD 负担，以便为 HIV-CVD 综合规划提供信息。方法 EMOD-HIV 是一种针对斯威士兰流行病进行校准的基于主体的模型，可生成 HIV 流行轨迹。这些与年龄标准化的全球 CVD 疾病负担估计和发布的相对风险 (RR) 相结合，以产生 HIV 分层的 CVD 预测。
- Keywords: mortality, burden, versus, plhiv, through

### 20. [2000-2025年撒哈拉以南非洲36个国家地区生育率小区域估算](https://www.medrxiv.org/content/10.64898/2026.07.17.26358322v1)
- Original title: Small-area estimation of district-level fertility in 36 countries in sub-Saharan Africa 2000-2025
- Authors: Stevens, O., Imai-Eaton, J. W.
- Meta: 2026-07-20 | public and global health | DOI: 10.64898/2026.07.17.26358322
- 中文摘要: 简介：撒哈拉以南非洲 (SSA) 的政策制定者和项目规划者需要地区一级的生育率估算，以指导地方一级的决策。现有的地区一级生育率估算方法使用较高行政级别的年龄结构或总生育率随时间变化的趋势，这阻碍了生育率估算中地区一级异质性的体现。方法：我们从 194 个具有全国代表性的家庭调查中提取了按五年年龄组、单一历年和地区分层的出生人数和人年观察数据。我们构建了一个时空贝叶斯分层模型，该模型协调点数据和面数据并调整非抽样偏差，以估计 2000 年至 2025 年间 36 个国家的特定年龄 (ASFR) 和总生育率 (TFR)。
- Abstract: Introduction: District-level estimates of fertility are required by policymakers and programme planners in sub-Saharan Africa (SSA) to guide decision making at the local level. Existing approaches to produce fertility estimates at the district level use age-structures or total fertility trends over time from higher administrative levels which prevents representation of district-level heterogeneity in fertility estim...
- Summary (fallback): 机器翻译摘要显示：简介：撒哈拉以南非洲 (SSA) 的政策制定者和项目规划者需要地区一级的生育率估算，以指导地方一级的决策。现有的地区一级生育率估算方法使用较高行政级别的年龄结构或总生育率随时间变化的趋势，这阻碍了生育率估算中地区一级异质性的体现。方法：我们从 194 个具有全国代表性的家庭调查中提取了按五年年龄组、单一历年和地区分层的出生人数和人年观察数据。我们构建了一个时空贝叶斯分层模型，该模型协调点数据和面数据并调整非抽样偏差，以估计 2000 年至 2025 年间 36 个国家的特定年龄 (ASFR) 和总生育率 (TFR)。
- Keywords: fertility, countries, district-level, estimates, total

### 21. [动脉粥样硬化性脑血管疾病 STA-MCA 搭桥术后生物性别与临床结果的关系](https://www.medrxiv.org/content/10.64898/2026.07.17.26358368v1)
- Original title: Association of biological sex with clinical outcomes following STA-MCA bypass in atherosclerotic cerebrovascular disease
- Authors: Iqbal, M. A., Alsolivany, J., Ferdowssian, K., Mertens, R., Sprünken, E. D. et al.
- Meta: 2026-07-20 | surgery | DOI: 10.64898/2026.07.17.26358368
- 中文摘要: 背景：脑血管疾病的性别差异是急性卒中护理和血管干预结果的既定决定因素，但脑血管搭桥手术的证据仍然有限。本研究探讨了动脉粥样硬化性脑血管疾病 (ACVD) 患者的生物性别是否与颞浅动脉至大脑中动脉 (STA-MCA) 搭桥术后的结果相关。方法：我们回顾性筛选了接受颅外颅内 (EC-IC) 搭桥术的成人（2012 年至 2025 年），并纳入了接受 STA-MCA 搭桥术治疗并进行随访的 ACVD 患者。主要结果是最近一次随访时的改良Rankin量表（mRS），使用比例优势回归进行分析。针对年龄、术前 mRS 和血管合并症进行调整的多变量模型。在一个亚组中分析脑血管储备能力（CVRC）。
- Abstract: Background: Sex differences in cerebrovascular disease are established determinants of outcome in acute stroke care and vascular interventions, but evidence in cerebrovascular bypass surgery remains limited. This study examined whether biological sex was associated with outcome after superficial temporal artery to middle cerebral artery (STA-MCA) bypass in patients with atherosclerotic cerebrovascular disease (ACVD)...
- Summary (fallback): 机器翻译摘要显示：背景：脑血管疾病的性别差异是急性卒中护理和血管干预结果的既定决定因素，但脑血管搭桥手术的证据仍然有限。本研究探讨了动脉粥样硬化性脑血管疾病 (ACVD) 患者的生物性别是否与颞浅动脉至大脑中动脉 (STA-MCA) 搭桥术后的结果相关。方法：我们回顾性筛选了接受颅外颅内 (EC-IC) 搭桥术的成人（2012 年至 2025 年），并纳入了接受 STA-MCA 搭桥术治疗并进行随访的 ACVD 患者。主要结果是最近一次随访时的改良Rankin量表（mRS），使用比例优势回归进行分析。针对年龄、术前 mRS 和血管合并症进行调整的多变量模型。在一个亚组中分析脑血管储备能力（CVRC）。
- Keywords: outcome, bypass, cerebrovascular, disease, sta-mca

### 22. [对精准健康研究参与的看法：认知访谈研究](https://www.medrxiv.org/content/10.64898/2026.03.30.26349735v2)
- Original title: Perceptions of precision health research participation: a cognitive interview study
- Authors: Werner, R. J., Karim, S. T., Cunningham, M. A., Moultrie, L. H., Goodwine, M. L. et al.
- Meta: 2026-07-20 | health systems and quality improvement | DOI: 10.64898/2026.03.30.26349735
- 中文摘要: 摘要 背景 精准研究参与 (PECAN) 研究旨在探索影响精准健康研究参与认知的因素 - 定义为整合遗传、行为和环境决定因素以定制个性化疾病预防和治疗的研究 - 重点关注南卡罗来纳州的不同社区。目标是确定影响参与精准健康研究的因素，并为减少受健康差异影响较大的人群之间的障碍提供策略。方法 为了确保 PECAN 研究调查工具的文化可及性和可理解性，研究人员使用有目的的抽样策略进行了定性认知访谈研究。
- Abstract: Abstract Background The Precision rEsearCh pArticipatioN (PECAN) study aims to explore factors that influence perceptions of precision health research participation - defined as research integrating genetic, behavioral, and environmental determinants to tailor individualized disease prevention and treatment - focusing on diverse communities in South Carolina. The objective is to identify factors influencing particip...
- Summary (fallback): 机器翻译摘要显示：摘要 背景 精准研究参与 (PECAN) 研究旨在探索影响精准健康研究参与认知的因素 - 定义为整合遗传、行为和环境决定因素以定制个性化疾病预防和治疗的研究 - 重点关注南卡罗来纳州的不同社区。目标是确定影响参与精准健康研究的因素，并为减少受健康差异影响较大的人群之间的障碍提供策略。方法 为了确保 PECAN 研究调查工具的文化可及性和可理解性，研究人员使用有目的的抽样策略进行了定性认知访谈研究。
- Keywords: survey, research, cognitive, precision, health
