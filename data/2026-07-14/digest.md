# daily2rxiv Digest - 2026-07-14

共收录 61 篇论文。

## arxiv

### 1. [PHINN-EEG：梦态脑电图的拓扑时间序列分析——用于梦内容分类和拓扑条件神经信号合成的动态贝蒂曲线](https://arxiv.org/abs/2607.09662v1)
- Original title: PHINN-EEG: Topological Time-Series Analysis of Dream-State EEG -- Dynamic Betti Curves for Dream Content Classification and Topology-Conditioned Neural Signal Synthesis
- Authors: Ren Takahashi, Emre Yusuf, Jayabrata Bhaduri
- Meta: 2026-07-10 | q-bio.NC
- 中文摘要: 当前基于脑电图 (EEG) 的梦境检测依赖于功率谱密度 (PSD) 和统计矩特征，在 DREAM 数据库上实现了约 0.70 的接收器操作特性曲线 (AUC) 下的最先进面积（Wong 等人，2025，自然通讯）。我们介绍 PHINN-EEG（脑电图持久同源启发神经网络），这是第一个用于梦境心理分析的拓扑时间序列框架。在多通道预觉醒脑电图时期上使用滑动窗口 Takens 延迟嵌入和 Vietoris-Rips 过滤，我们提取了动态 Betti 曲线，该曲线表征了神经活动的几何结构，而不仅仅是其能量。
- Abstract: Current electroencephalography (EEG)-based dream detection relies on power spectral density (PSD) and statistical moment features, achieving a state-of-the-art area under the receiver operating characteristic curve (AUC) of approximately 0.70 on the DREAM database (Wong et al., 2025, Nature Communications). We introduce PHINN-EEG (Persistent Homology Inspired Neural Network for EEG), the first topological time-serie...
- Summary (fallback): 机器翻译摘要显示：当前基于脑电图 (EEG) 的梦境检测依赖于功率谱密度 (PSD) 和统计矩特征，在 DREAM 数据库上实现了约 0.70 的接收器操作特性曲线 (AUC) 下的最先进面积（Wong 等人，2025，自然通讯）。我们介绍 PHINN-EEG（脑电图持久同源启发神经网络），这是第一个用于梦境心理分析的拓扑时间序列框架。在多通道预觉醒脑电图时期上使用滑动窗口 Takens 延迟嵌入和 Vietoris-Rips 过滤，我们提取了动态 Betti 曲线，该曲线表征了神经活动的几何结构，而不仅仅是其能量。
- Keywords: dream, topological, neural, betti, topology-conditioned

### 2. [有向无环图上的深度高斯过程](https://arxiv.org/abs/2607.09645v1)
- Original title: Deep Gaussian Processes on Directed Acyclic Graphs
- Authors: Federico L. Perlino, Oliver Hamelijnck, Adam M. Johansen, Theodoros Damoulas
- Meta: 2026-07-10 | stat.ML
- 中文摘要: 许多现实世界的过程可以表示为沿有向无环图 (DAG) 的函数组合。在因果建模中，这些对应于潜在的机制；在工程中，达到多个保真度级别；在基因调控网络中，转录因子。这些函数在 DAG 中被部分观察到，具有噪声和异构采样测量，给重建、不确定性传播和推理带来了重大挑战。为了应对这些挑战，我们将先验置于函数之上，自然而然地得到了 DAG 之上的深度高斯过程。我们从理论上研究了它们的先验崩溃行为，以及图拓扑和中间观察对信息保存的影响。
- Abstract: Many real-world processes can be represented as compositions of functions along a directed acyclic graph (DAG). In causal modelling, these correspond to the underlying mechanisms; in engineering, to multiple fidelity levels; and in gene-regulatory networks, to transcription factors. These functions are partially observed across the DAG, with noisy and heterogeneously sampled measurements, posing significant challeng...
- Summary (fallback): 机器翻译摘要显示：许多现实世界的过程可以表示为沿有向无环图 (DAG) 的函数组合。在因果建模中，这些对应于潜在的机制；在工程中，达到多个保真度级别；在基因调控网络中，转录因子。这些函数在 DAG 中被部分观察到，具有噪声和异构采样测量，给重建、不确定性传播和推理带来了重大挑战。为了应对这些挑战，我们将先验置于函数之上，自然而然地得到了 DAG 之上的深度高斯过程。我们从理论上研究了它们的先验崩溃行为，以及图拓扑和中间观察对信息保存的影响。
- Keywords: processes, functions, graph, deep, gaussian

### 3. [语义 Pareto-DQN：用于金融异常检测的多目标强化学习框架](https://arxiv.org/abs/2607.09641v1)
- Original title: Semantic Pareto-DQN: A Multi-Objective Reinforcement Learning Framework for Financial Anomaly Detection
- Authors: Cláudio Lúcio do Val Lopes, Lucca Machado da Silva
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 金融异常检测遭受极端的类别不平衡，导致传统的单目标算法表现出“欺诈崩溃”，默认为多数类别，并且无法平衡异常拦截与客户摩擦。为了在不扭曲数据重采样的情况下克服这个问题，我们提出了语义 Pareto-DQN，一种多目标强化学习框架。我们的方法将异构交易特征合成为有凝聚力的自然语言叙述，由大型语言模型编码，从而产生强大的、尺度不变的状态表示。该代理优化了矢量奖励，明确地解耦了财务效率、操作摩擦和语义发现。通过映射连续的帕累托前沿，系统可以动态地导航遗漏异常与误报的不对称成本。
- Abstract: Financial anomaly detection suffers from extreme class imbalance, causing traditional single-objective algorithms to exhibit ``fraud collapse'', defaulting to the majority class and failing to balance anomaly interdiction with customer friction. To overcome this without distortive data resampling, we propose the Semantic Pareto-DQN, a multi-objective reinforcement learning framework. Our approach synthesizes heterog...
- Summary (fallback): 机器翻译摘要显示：金融异常检测遭受极端的类别不平衡，导致传统的单目标算法表现出“欺诈崩溃”，默认为多数类别，并且无法平衡异常拦截与客户摩擦。为了在不扭曲数据重采样的情况下克服这个问题，我们提出了语义 Pareto-DQN，一种多目标强化学习框架。我们的方法将异构交易特征合成为有凝聚力的自然语言叙述，由大型语言模型编码，从而产生强大的、尺度不变的状态表示。该代理优化了矢量奖励，明确地解耦了财务效率、操作摩擦和语义发现。通过映射连续的帕累托前沿，系统可以动态地导航遗漏异常与误报的不对称成本。
- Keywords: semantic, financial, anomaly, pareto-dqn, friction

### 4. [前端设计 EDA 法学硕士：挑战与机遇](https://arxiv.org/abs/2607.09616v1)
- Original title: LLM for EDA in Front-End Design: Challenges and Opportunities
- Authors: Kangwei Xu, Bing Li, Ulf Schlichtmann
- Meta: 2026-07-10 | cs.ET
- 中文摘要: 随着芯片复杂性的增加和上市时间压力的加大，前端设计已成为芯片开发的关键瓶颈。最近，大型语言模型（LLM）在电子设计自动化（EDA）领域显示出巨大的潜力。除了规范理解之外，LLM 还显示出作为硬件描述语言 (HDL) 生成、测试平台构建和设计空间探索的统一智能接口的潜力。以 OpenClaw 等开创性系统为代表的代理人工智能的兴起，为下一代 EDA 提供了战略路线图。本文从这个角度讨论了EDA从本地化协助到自主代理执行的演变。
- Abstract: As chip complexity increases and time-to-market pressures grow, front-end design has become a critical bottleneck in chip development. Recently, Large Language Models (LLMs) have shown great potential in Electronic Design Automation (EDA). Beyond specification understanding, LLMs show the potential to serve as a unified intelligent interface for hardware description language (HDL) generation, testbench construction,...
- Summary (fallback): 机器翻译摘要显示：随着芯片复杂性的增加和上市时间压力的加大，前端设计已成为芯片开发的关键瓶颈。最近，大型语言模型（LLM）在电子设计自动化（EDA）领域显示出巨大的潜力。除了规范理解之外，LLM 还显示出作为硬件描述语言 (HDL) 生成、测试平台构建和设计空间探索的统一智能接口的潜力。以 OpenClaw 等开创性系统为代表的代理人工智能的兴起，为下一代 EDA 提供了战略路线图。本文从这个角度讨论了EDA从本地化协助到自主代理执行的演变。
- Keywords: design, front-end, llms, generation, agentic

### 5. [Inunda：用于高分辨率洪水淹没建模的 GPU 原生、支持代理、可微分求解器](https://arxiv.org/abs/2607.09614v1)
- Original title: Inunda: A GPU-Native, Agent-enabled, Differentiable Solver for High-Resolution Flood Inundation Modeling
- Authors: Zhi Li
- Meta: 2026-07-10 | physics.geo-ph
- 中文摘要: 使用传统的水力求解器以高分辨率和跨大域来预测洪水的去向和深度，其计算成本仍然很高，而纯数据驱动的替代方案速度很快，但缺乏物理保证，并且在训练活动之外的泛化能力很差。我们提出了 Inunda，一种 GPU 原生洪水淹没模型，可求解二维浅水方程。 Inunda 使用大规模保守局部惯性方案，并在单个 GPU 上在几分钟内运行数百万个单元上的多日事件。由于每个算子都是自动梯度兼容的，因此求解器可以通过构造进行微分：可以通过完整模拟的反向模式自动微分，根据量具观测值通过梯度下降来估计模型参数。我们通过三个案例研究展示了 Inunda。
- Abstract: Predicting where floodwater goes and how deep it gets, at high resolution and across large domains, remains computationally expensive with conventional hydraulic solvers, while purely data-driven surrogates are fast but lack physical guarantees and generalize poorly beyond their training events. We present Inunda, a GPU-native flood inundation model that solves the two-dimensional shallow water equations. Inunda use...
- Summary (fallback): 机器翻译摘要显示：使用传统的水力求解器以高分辨率和跨大域来预测洪水的去向和深度，其计算成本仍然很高，而纯数据驱动的替代方案速度很快，但缺乏物理保证，并且在训练活动之外的泛化能力很差。我们提出了 Inunda，一种 GPU 原生洪水淹没模型，可求解二维浅水方程。 Inunda 使用大规模保守局部惯性方案，并在单个 GPU 上在几分钟内运行数百万个单元上的多日事件。由于每个算子都是自动梯度兼容的，因此求解器可以通过构造进行微分：可以通过完整模拟的反向模式自动微分，根据量具观测值通过梯度下降来估计模型参数。我们通过三个案例研究展示了 Inunda。
- Keywords: inunda, flood, differentiable, model, gpu-native

### 6. [具有分布数据特征选择的动态 Frechet 回归](https://arxiv.org/abs/2607.09613v1)
- Original title: Dynamic Frechet Regression with Feature Selection for Distributional Data
- Authors: Kiran Adhikari, Amrutha Dinesh, Mathew Kuttolamadom, Ying Lin
- Meta: 2026-07-10 | stat.ME
- 中文摘要: 许多科学和工程应用程序生成的响应不是标量或向量，而是统计对象，其形式随着时间、深度等有序索引而演变。概率分布是一个突出的例子，它捕获了低维统计无法概括的可变性和不确定性。当顺序观察此类响应时，所得的动态分布轨迹对回归提出了重大挑战，特别是在将标量预测变量与指数内变异性和跨指数演化相关联时。我们提出了动态 Fréchet 回归（DFR），这是一个用于对分布值响应的指数相关轨迹进行建模的框架。 DFR 通过引入索引感知加权机制来扩展全局 Fréchet 回归。
- Abstract: Many scientific and engineering applications generate responses that are not scalars or vectors, but statistical objects whose form evolves over an ordered index such as time, depth. Probability distributions are a prominent example, capturing variability and uncertainty that cannot be summarized by low-dimensional statistics. When such responses are observed sequentially, the resulting dynamic distributional trajec...
- Summary (fallback): 机器翻译摘要显示：许多科学和工程应用程序生成的响应不是标量或向量，而是统计对象，其形式随着时间、深度等有序索引而演变。概率分布是一个突出的例子，它捕获了低维统计无法概括的可变性和不确定性。当顺序观察此类响应时，所得的动态分布轨迹对回归提出了重大挑战，特别是在将标量预测变量与指数内变异性和跨指数演化相关联时。我们提出了动态 Fréchet 回归（DFR），这是一个用于对分布值响应的指数相关轨迹进行建模的框架。 DFR 通过引入索引感知加权机制来扩展全局 Fréchet 回归。
- Keywords: regression, distributional, dynamic, feature, responses

### 7. [通过变量投影表征多快照尖峰反卷积的凸盆](https://arxiv.org/abs/2607.09593v1)
- Original title: Characterization of the basin of convexity for multi-snapshot spike deconvolution via variable projection
- Authors: Meghna Kalra, Maxime Ferreira Da Costa, Kiryung Lee
- Meta: 2026-07-10 | stat.ML
- 中文摘要: 我们研究多快照尖峰反卷积问题，其目标是使用跨多个快照的已知点扩散函数（PSF）从噪声卷积中恢复稀疏脉冲的位置。我们采用可变投影公式来消除封闭形式的振幅，将任务简化为仅针对尖峰位置的非凸最小二乘问题，我们将其称为尖峰反卷积的可变投影公式（VarProSD）。我们根据关键 PSF 属性（包括功率谱密度和平滑度）对 VarProSD 物镜的凸盆进行了明确的表征，揭示了采样带宽和尖峰分离如何影响局部几何形状。
- Abstract: We study the problem of multi-snapshot spike deconvolution, where the goal is to recover the locations of sparse impulses from their noisy convolution with a known point spread function (PSF) across multiple snapshots. We adopt a variable-projection formulation that eliminates the amplitudes in closed form, reducing the task to a nonconvex least-squares problem over the spike locations alone, which we refer to as th...
- Summary (fallback): 机器翻译摘要显示：我们研究多快照尖峰反卷积问题，其目标是使用跨多个快照的已知点扩散函数（PSF）从噪声卷积中恢复稀疏脉冲的位置。我们采用可变投影公式来消除封闭形式的振幅，将任务简化为仅针对尖峰位置的非凸最小二乘问题，我们将其称为尖峰反卷积的可变投影公式（VarProSD）。我们根据关键 PSF 属性（包括功率谱密度和平滑度）对 VarProSD 物镜的凸盆进行了明确的表征，揭示了采样带宽和尖峰分离如何影响局部几何形状。
- Keywords: spike, basin, deconvolution, local, characterization

### 8. [用于化学动力学建模的熵约束机器学习和剩余数据增强](https://arxiv.org/abs/2607.09582v1)
- Original title: Entropy-Constrained Machine Learning with Residual Data Augmentation for Modeling Chemical Kinetics
- Authors: Okezzi Ukorigho, Opeoluwa Owoyele
- Meta: 2026-07-10 | physics.flu-dyn
- 中文摘要: 我们提出了一个物理约束的机器学习框架，用于加速湍流反应流的直接数值模拟（DNS）。该模型用从降低的热化学状态预测反应速率的替代项取代了对详细化学源项的直接评估。为了提高物理一致性，通过强制非负熵生成将热力学第二定律纳入训练约束，这将热化学态的演化限制为物理允许的方向，并提高了时间积分期间的稳定性。该方法在与湍流流场相互作用的二维平面贫预混甲烷-空气火焰的 DNS 上进行了演示。该模型以高保真度再现详细的化学结果，同时使计算成本降低了一个数量级以上。
- Abstract: We present a physics-constrained machine learning framework for accelerating the direct numerical simulation (DNS) of turbulent reacting flows. The model replaces the direct evaluation of detailed chemical source terms with a surrogate that predicts reaction rates from a reduced thermochemical state. To improve physical consistency, the second law of thermodynamics is incorporated as a training constraint by enforci...
- Summary (fallback): 机器翻译摘要显示：我们提出了一个物理约束的机器学习框架，用于加速湍流反应流的直接数值模拟（DNS）。该模型用从降低的热化学状态预测反应速率的替代项取代了对详细化学源项的直接评估。为了提高物理一致性，通过强制非负熵生成将热力学第二定律纳入训练约束，这将热化学态的演化限制为物理允许的方向，并提高了时间积分期间的稳定性。该方法在与湍流流场相互作用的二维平面贫预混甲烷-空气火焰的 DNS 上进行了演示。该模型以高保真度再现详细的化学结果，同时使计算成本降低了一个数量级以上。
- Keywords: machine, learning, augmentation, chemical, direct

### 9. [生存预测中表格基础模型的审查感知目标接口](https://arxiv.org/abs/2607.09577v1)
- Original title: A censoring-aware target interface for tabular foundation models in survival prediction
- Authors: Yue Lyu, Steven H. Lin, Xuelin Huang, Ziyi Li
- Meta: 2026-07-10 | stat.ME
- 中文摘要: 从表格患者数据中预测事件发生时间对于预后和生物医学决策支持至关重要，但右删失随访阻止了直接使用普通回归标签。表格基础模型为适度的异构数据集提供了可重用的预测机制，但它们通常假设完全观察到的结果。我们引入了 SurvFM-RMST，这是一种审查感知目标接口框架，可将生存结果转换为限制平均生存时间的折刀伪观察目标，使多个表格主干能够执行特定于水平的 RMST 回归，而无需进行特定于生存的微调。在已知条件 RMST 的受控模拟中，SurvFM-RMST 准确地恢复了受限的无事件时间，并且伪 RMST 目标优于朴素的受限观察时间和仅事件目标。
- Abstract: Time-to-event prediction from tabular patient data is central to prognosis and biomedical decision support, but right-censored follow-up prevents direct use of ordinary regression labels. Tabular foundation models offer reusable prediction machinery for modest heterogeneous datasets, yet they generally assume fully observed outcomes. We introduce SurvFM-RMST, a censoring-aware target-interface framework that convert...
- Summary (fallback): 机器翻译摘要显示：从表格患者数据中预测事件发生时间对于预后和生物医学决策支持至关重要，但右删失随访阻止了直接使用普通回归标签。表格基础模型为适度的异构数据集提供了可重用的预测机制，但它们通常假设完全观察到的结果。我们引入了 SurvFM-RMST，这是一种审查感知目标接口框架，可将生存结果转换为限制平均生存时间的折刀伪观察目标，使多个表格主干能够执行特定于水平的 RMST 回归，而无需进行特定于生存的微调。在已知条件 RMST 的受控模拟中，SurvFM-RMST 准确地恢复了受限的无事件时间，并且伪 RMST 目标优于朴素的受限观察时间和仅事件目标。
- Keywords: tabular, survival, prediction, targets, restricted

### 10. [超越固定表示：开放式人工智能中的词汇和验证者差距](https://arxiv.org/abs/2607.09560v1)
- Original title: Beyond Fixed Representations: The Vocabulary and Verifier Gaps in Open-Ended AI
- Authors: Yuan Cao, Haiqian Yang
- Meta: 2026-07-10 | cs.AI
- 中文摘要: 现代人工智能系统越来越多地因其推理、编码、证明定理、使用工具和长期研究任务的能力而受到评估。这些都是强大的功能，但它们都有一个结构性限制：模型运行的表征框架，包括其概念词汇、它可以搜索的可接受解决方案的空间以及评估成功的标准，通常是预先固定和提供的。本文认为，构建能够进行开放式创新的更强大的智能系统需要额外的操作类别：新的表征基元的创建、稳定和重用，这会改变正在搜索的空间，而不是简单地在其中进行搜索。我们通过两个差距来描述当前人工智能系统与真正开放式智能之间的距离。
- Abstract: Modern AI systems are increasingly being evaluated for their ability to reason, code, prove theorems, use tools, and long-horizon research tasks. These are powerful capabilities, but they share a structural limitation: the representational frame within which the model operates, including its conceptual vocabulary, the space of admissible solutions it can search, and the criteria by which success is evaluated, is typ...
- Summary (fallback): 机器翻译摘要显示：现代人工智能系统越来越多地因其推理、编码、证明定理、使用工具和长期研究任务的能力而受到评估。这些都是强大的功能，但它们都有一个结构性限制：模型运行的表征框架，包括其概念词汇、它可以搜索的可接受解决方案的空间以及评估成功的标准，通常是预先固定和提供的。本文认为，构建能够进行开放式创新的更强大的智能系统需要额外的操作类别：新的表征基元的创建、稳定和重用，这会改变正在搜索的空间，而不是简单地在其中进行搜索。我们通过两个差距来描述当前人工智能系统与真正开放式智能之间的距离。
- Keywords: representational, which, open-ended, fixed, vocabulary

### 11. [高维插值器可能很脆弱：重尾部和高维大偏差](https://arxiv.org/abs/2607.09547v1)
- Original title: High-Dimensional Interpolators Can Be Fragile: Heavy Tails and High-Dimensional Large Deviations
- Authors: Youheng Zhu, Yiping Lu
- Meta: 2026-07-10 | math.ST
- 中文摘要: 高维插值在现代机器学习中很常见，但其尾部风险比其预期预测风险更难理解。现有理论表明，插值模型可以在预期中表现良好，但这种保证并不能确定罕见、严重错误的概率。在运筹学和随机决策应用中，罕见的估计错误可能会产生不成比例的下游影响，因此尾部行为与平均性能一样重要。我们使用大偏差方法研究高维线性插值器的脆弱性。我们关注无岭回归并将其与岭正则化估计器进行比较。我们首先表明，无脊回归的风险可以表现出重尾行为：尽管其预期风险可能仍然得到很好的控制，但其上尾的衰减速度比正则化替代方案的衰减慢得多。
- Abstract: High-dimensional interpolation is common in modern machine learning, but its tail risk is less understood than its expected prediction risk. Existing theory shows that interpolating models can perform well in expectation, yet such guarantees do not determine the probability of rare, severe errors. In operations research and stochastic decision-making applications, rare estimation errors can have disproportionate dow...
- Summary (fallback): 机器翻译摘要显示：高维插值在现代机器学习中很常见，但其尾部风险比其预期预测风险更难理解。现有理论表明，插值模型可以在预期中表现良好，但这种保证并不能确定罕见、严重错误的概率。在运筹学和随机决策应用中，罕见的估计错误可能会产生不成比例的下游影响，因此尾部行为与平均性能一样重要。我们使用大偏差方法研究高维线性插值器的脆弱性。我们关注无岭回归并将其与岭正则化估计器进行比较。我们首先表明，无脊回归的风险可以表现出重尾行为：尽管其预期风险可能仍然得到很好的控制，但其上尾的衰减速度比正则化替代方案的衰减慢得多。
- Keywords: risk, high-dimensional, tail, rare, ridgeless

### 12. [通过变量投影完成图正则化低秩矩阵](https://arxiv.org/abs/2607.09546v1)
- Original title: Graph-Regularized Low-Rank Matrix Completion by Variable Projection
- Authors: Benoît Loucheur, P. -A. Absil, Michel Journée
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 我们通过将图正则化合并到现有的黎曼信任区域矩阵补全（RTRMC）框架中来解决低秩矩阵补全问题。后者使用低秩约束的几何形状将问题重新建模为单个格拉斯曼流形上的无约束优化问题。我们的方法称为图正则化 RTRMC (GR-RTRMC)，利用矩阵的行和列之间的固有关系。通过使用这些关系，我们的目标是提高矩阵补全的准确性和鲁棒性，特别是在基础数据在行或列之间表现出强相关性的情况下。
- Abstract: We address the low-rank matrix completion problem by incorporating graph regularization into the existing Riemannian Trust-Region Matrix Completion (RTRMC) framework. The latter uses the geometry of the low-rank constraint to remodel the problem as an unconstrained optimization problem on a single Grassmann manifold. Our approach, named Graph-Regularized RTRMC (GR-RTRMC), exploits the inherent relationships between...
- Summary (fallback): 机器翻译摘要显示：我们通过将图正则化合并到现有的黎曼信任区域矩阵补全（RTRMC）框架中来解决低秩矩阵补全问题。后者使用低秩约束的几何形状将问题重新建模为单个格拉斯曼流形上的无约束优化问题。我们的方法称为图正则化 RTRMC (GR-RTRMC)，利用矩阵的行和列之间的固有关系。通过使用这些关系，我们的目标是提高矩阵补全的准确性和鲁棒性，特别是在基础数据在行或列之间表现出强相关性的情况下。
- Keywords: matrix, completion, low-rank, problem, graph-regularized

### 13. [计数存在，但未对齐：理解和纠正 VLM 中的计数失败](https://arxiv.org/abs/2607.09544v1)
- Original title: The Count Is There, but Misaligned: Understanding and Correcting Counting Failures in VLMs
- Authors: Ahmed Oumar El-Shangiti, Abzal Nurgazy, Hilal AlQuabeh, Nikolai Rozanov, Kentaro Inui
- Meta: 2026-07-10 | cs.CV
- 中文摘要: 尽管在许多多模式任务上表现出色，但视觉语言模型 (VLM) 仍然难以处理基本的对象计数。我们调查这是否反映了内部知识的缺失或内部表征与语言输出之间的差距。对来自五个计数数据集的四个 VLM 的激活训练简单探针表明，非线性探针可以可靠地检测计数错误，这表明 VLM 经常编码正确的计数，即使它们输出错误的答案。 SVCCA 分析表明，根据真实计数训练的探针和根据模型输出训练的探针占据部分共享的激活子空间，但沿未对齐的方向读取。我们使用因果转向干预进一步验证了我们的发现，证明加强计数识别探针的方向确实可以提高模型计数性能。
- Abstract: Despite strong performance on many multimodal tasks, vision-language models (VLMs) still struggle with basic object counting. We investigate whether this reflects missing internal knowledge or a gap between internal representations and verbalized outputs. Training simple probes on activations from four VLMs across five counting datasets reveals that nonlinear probes can reliably detect counting errors, suggesting th...
- Summary (fallback): 机器翻译摘要显示：尽管在许多多模式任务上表现出色，但视觉语言模型 (VLM) 仍然难以处理基本的对象计数。我们调查这是否反映了内部知识的缺失或内部表征与语言输出之间的差距。对来自五个计数数据集的四个 VLM 的激活训练简单探针表明，非线性探针可以可靠地检测计数错误，这表明 VLM 经常编码正确的计数，即使它们输出错误的答案。 SVCCA 分析表明，根据真实计数训练的探针和根据模型输出训练的探针占据部分共享的激活子空间，但沿未对齐的方向读取。我们使用因果转向干预进一步验证了我们的发现，证明加强计数识别探针的方向确实可以提高模型计数性能。
- Keywords: counting, probes, vlms, internal, model

### 14. [CoCoT-EEG：用于 EEG 解码的对比预训练多尺度卷积变换器](https://arxiv.org/abs/2607.09543v1)
- Original title: CoCoT-EEG: Contrastive-Pretrained Multiscale Convolutional Transformer for EEG Decoding
- Authors: Gabriel Mahuas, Victoria Shevchenko, Ugo Tanielian, Yassir Bendou, Richard Gao
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 自监督预训练基础模型 (FM) 已在非侵入性脑电图 (EEG) 解码应用中显示出早期前景。最近的许多大型模型都集中于对原始脑电图进行标记化，然后进行掩模重建预训练的方法。然而，事实证明，这种方法对于脑电图等数据来说并不是最理想的，因为噪声幅度较高，而且信息仅限于有限的维度，例如窄频带。基于这一见解，我们开发了一种新颖的对比预训练脑电图模型，具有多尺度时间卷积输入层和 Transformer 编码器块 (CoCoT)。 CoCoT 在具有异构电极配置的广泛基准解码任务上匹配或击败了最先进的重建预训练 EEG 模型。
- Abstract: Self-supervised pretrained foundation models (FM) have shown early promise for non-invasive electroencephalogram (EEG) decoding applications. Many recent large-scale models converged on the approach of tokenizing raw EEG followed by masked reconstruction pretraining. However, this recipe has been shown to be suboptimal for data, like EEG, with high noise amplitude and information confined to limited dimensions such...
- Summary (fallback): 机器翻译摘要显示：自监督预训练基础模型 (FM) 已在非侵入性脑电图 (EEG) 解码应用中显示出早期前景。最近的许多大型模型都集中于对原始脑电图进行标记化，然后进行掩模重建预训练的方法。然而，事实证明，这种方法对于脑电图等数据来说并不是最理想的，因为噪声幅度较高，而且信息仅限于有限的维度，例如窄频带。基于这一见解，我们开发了一种新颖的对比预训练脑电图模型，具有多尺度时间卷积输入层和 Transformer 编码器块 (CoCoT)。 CoCoT 在具有异构电极配置的广泛基准解码任务上匹配或击败了最先进的重建预训练 EEG 模型。
- Keywords: models, decoding, pretraining, cocot, contrastive-pretrained

### 15. [GatedLinear：用于时间序列预测的互补线性基的自适应路由](https://arxiv.org/abs/2607.09537v1)
- Original title: GatedLinear: Adaptive Routing of Complementary Linear Bases for Time Series Forecasting
- Authors: Qitai Tan, Ruiwen Gu, Yilin Su, Mo Li, Xu Lin et al.
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 时间序列预测需要模型捕获不同的、通常相互排斥的时间动态，从平滑趋势延续到非平稳漂移和严格的相位对齐递归。虽然最近的深度学习模型提高了准确性，但它们通常通过由固定算法归纳偏差（例如自注意力或光谱过滤）控制的单一计算主干来强制这些不同的模式。这种单一机制方法经常与现实世界序列的深刻异质性作斗争，其中不同的变量和预测范围需要根本不同的预测处理。为了解决这个问题，我们提出了 GatedLinear：一个轻量级框架，将预测框架为互补线性基的自适应路由。
- Abstract: Time series forecasting requires models to capture diverse, often mutually exclusive, temporal dynamics, from smooth trend continuation to nonstationary drift and strict phase-aligned recurrence. While recent deep learning models have improved accuracy, they typically force these diverse patterns through a single computational backbone governed by fixed algorithmic inductive biases (e.g., self-attention or spectral...
- Summary (fallback): 机器翻译摘要显示：时间序列预测需要模型捕获不同的、通常相互排斥的时间动态，从平滑趋势延续到非平稳漂移和严格的相位对齐递归。虽然最近的深度学习模型提高了准确性，但它们通常通过由固定算法归纳偏差（例如自注意力或光谱过滤）控制的单一计算主干来强制这些不同的模式。这种单一机制方法经常与现实世界序列的深刻异质性作斗争，其中不同的变量和预测范围需要根本不同的预测处理。为了解决这个问题，我们提出了 GatedLinear：一个轻量级框架，将预测框架为互补线性基的自适应路由。
- Keywords: routing, gatedlinear, time, series, forecasting

### 16. [深度神经网络中统计上无法检测的后门](https://arxiv.org/abs/2607.09532v1)
- Original title: Statistically Undetectable Backdoors in Deep Neural Networks
- Authors: Andrej Bogdanov, Alon Rosen, Neekon Vafa
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 我们展示了对抗模型训练器如何在一大类深度前馈神经网络中植入后门。这些后门在白盒设置中在统计上是无法检测到的，这意味着即使给出了模型的完整描述（例如所有权重），后门模型和诚实训练的模型在总变异距离上也很接近。后门为每个输入提供基于不变性的对抗性示例，将遥远的输入映射到异常接近的输出。然而，如果没有后门，事实证明不可能（在标准加密假设下）在多项式时间内生成任何此类对抗性示例。我们的理论和初步实证研究结果表明，模型训练者和模型用户之间存在根本的权力不对称。
- Abstract: We show how an adversarial model trainer can plant backdoors in a large class of deep, feedforward neural networks. These backdoors are statistically undetectable in the white-box setting, meaning that the backdoored and honestly trained models are close in total variation distance, even given the full descriptions of the models (e.g., all of the weights). The backdoor provides access to invariance-based adversarial...
- Summary (fallback): 机器翻译摘要显示：我们展示了对抗模型训练器如何在一大类深度前馈神经网络中植入后门。这些后门在白盒设置中在统计上是无法检测到的，这意味着即使给出了模型的完整描述（例如所有权重），后门模型和诚实训练的模型在总变异距离上也很接近。后门为每个输入提供基于不变性的对抗性示例，将遥远的输入映射到异常接近的输出。然而，如果没有后门，事实证明不可能（在标准加密假设下）在多项式时间内生成任何此类对抗性示例。我们的理论和初步实证研究结果表明，模型训练者和模型用户之间存在根本的权力不对称。
- Keywords: backdoors, adversarial, model, statistically, undetectable

### 17. [TSAI-MetaFraud：元界生态系统中金融欺诈交易和行为风险检测的基准数据集](https://arxiv.org/abs/2607.09528v1)
- Original title: TSAI-MetaFraud: A Benchmark Dataset for Financial Fraud Transaction and Behavioral Risk Detection in Metaverse Ecosystems
- Authors: Refat Ishrak Hemel, Ehsan Hallaji, Roozbeh Razavi-Far
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 元宇宙平台的出现创造了虚拟经济，带来了与欺诈、机器人活动和非法金融行为相关的新挑战。尽管人们对可信的元宇宙分析越来越感兴趣，但现有数据集通常单独关注用户行为、身份验证或金融交易，限制了多模式欺诈检测方法的开发和可重复评估。为了解决这一差距，我们推出了 TSAI-MetaFraud，这是一个用于虚拟经济中欺诈分析的多模式、多任务基准数据集。 TSAI-MetaFraud 集成了行为、交易和图形结构信息，同时结合了现实的欺诈和自动化机器人场景。
- Abstract: The emergence of metaverse platforms has created virtual economies that introduce new challenges related to fraud, bot activity, and illicit financial behavior. Despite growing interest in trustworthy metaverse analytics, existing datasets typically focus on user behavior, authentication, or financial transactions in isolation, limiting the development and reproducible evaluation of multimodal fraud detection method...
- Summary (fallback): 机器翻译摘要显示：元宇宙平台的出现创造了虚拟经济，带来了与欺诈、机器人活动和非法金融行为相关的新挑战。尽管人们对可信的元宇宙分析越来越感兴趣，但现有数据集通常单独关注用户行为、身份验证或金融交易，限制了多模式欺诈检测方法的开发和可重复评估。为了解决这一差距，我们推出了 TSAI-MetaFraud，这是一个用于虚拟经济中欺诈分析的多模式、多任务基准数据集。 TSAI-MetaFraud 集成了行为、交易和图形结构信息，同时结合了现实的欺诈和自动化机器人场景。
- Keywords: fraud, tsai-metafraud, benchmark, financial, detection

### 18. [ALICE：向视觉、视觉语言和载玻片专家学习通用病理学基础模型](https://arxiv.org/abs/2607.09526v1)
- Original title: ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts
- Authors: Jiawen Li, Tian Guan, Huijuan Shi, Xitong Ling, Mingxi Fu et al.
- Meta: 2026-07-10 | cs.CV
- 中文摘要: 基础模型正在重塑计算病理学，但它们的能力仍然受到预训练目标、数据源和空间尺度的影响，将互补的专业知识分散到不同的骨干网中。在这里，我们提出了 ALICE，这是一个通过多阶段凝聚蒸馏训练​​的统一基础模型，它依次将八个仅视觉、视觉语言和幻灯片级别的教师模型蒸馏为单个主干的专用模块。 ALICE 经过 24,985,184 个切片级病理图像和 155,604 个高分辨率图像的预训练，并在 21 个任务场景、96 个下游任务和 48 个数据源中进行评估，涵盖感兴趣区域组织分析、视觉语言多模态评估和全幻灯片临床评估。在所有三种评估设置中，ALICE 在任务匹配的病理学基础模型中取得了最佳平均排名。
- Abstract: Foundation models are reshaping computational pathology, yet their capabilities remain shaped by pretraining objectives, data sources, and spatial scales, fragmenting complementary expertise across separate backbones. Here we present ALICE, a unified foundation model trained through multi-stage agglomerative distillation that sequentially distills eight vision-only, vision-language, and slide-level teacher models in...
- Summary (fallback): 机器翻译摘要显示：基础模型正在重塑计算病理学，但它们的能力仍然受到预训练目标、数据源和空间尺度的影响，将互补的专业知识分散到不同的骨干网中。在这里，我们提出了 ALICE，这是一个通过多阶段凝聚蒸馏训练​​的统一基础模型，它依次将八个仅视觉、视觉语言和幻灯片级别的教师模型蒸馏为单个主干的专用模块。 ALICE 经过 24,985,184 个切片级病理图像和 155,604 个高分辨率图像的预训练，并在 21 个任务场景、96 个下游任务和 48 个数据源中进行评估，涵盖感兴趣区域组织分析、视觉语言多模态评估和全幻灯片临床评估。在所有三种评估设置中，ALICE 在任务匹配的病理学基础模型中取得了最佳平均排名。
- Keywords: alice, pathology, foundation, models, model

### 19. [SAGEAgent：多模态生存预测中用于成本感知模态获取的自我进化代理](https://arxiv.org/abs/2607.09521v1)
- Original title: SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction
- Authors: Chongyu Qu, Can Cui, Zhengyi Lu, Junchao Zhu, Tianyuan Yao et al.
- Meta: 2026-07-10 | cs.AI
- 中文摘要: 每个癌症患者真的需要完整的诊断检查才能准确预测生存期吗？在多模式临床肿瘤学中，诊断模式遵循临床规定的负担逐步升级的顺序——从摄入时收集的人口统计数据到需要专门组织分析的基因组分析。当前的多模式生存方法要么假设所有模式都可用，要么被动处理缺失的数据，但没有一个方法主动推理对于沿着这个有序工作流程的给定患者获取下一种模式是否合理。我们将其表述为一个顺序决策问题，并提出了 SAGEAgent（经验引导的顺序获取），这是一种基于 LLM 的自我进化临床代理，可以决定为每位患者获取哪种诊断方式，平衡预测准确性与临床侵入性。
- Abstract: Does every cancer patient truly need a complete diagnostic workup for accurate survival prediction? In multimodal clinical oncology, diagnostic modalities follow a clinically mandated order of escalating burden -- from demographics collected at intake to genomic profiling requiring specialized tissue analysis. Current multimodal survival methods either assume all modalities are available or passively handle missing...
- Summary (fallback): 机器翻译摘要显示：每个癌症患者真的需要完整的诊断检查才能准确预测生存期吗？在多模式临床肿瘤学中，诊断模式遵循临床规定的负担逐步升级的顺序——从摄入时收集的人口统计数据到需要专门组织分析的基因组分析。当前的多模式生存方法要么假设所有模式都可用，要么被动处理缺失的数据，但没有一个方法主动推理对于沿着这个有序工作流程的给定患者获取下一种模式是否合理。我们将其表述为一个顺序决策问题，并提出了 SAGEAgent（经验引导的顺序获取），这是一种基于 LLM 的自我进化临床代理，可以决定为每位患者获取哪种诊断方式，平衡预测准确性与临床侵入性。
- Keywords: diagnostic, sageagent, survival, patient, clinical

### 20. [具有任意参数分布的全局耦合相位振荡器网络的多系综平均场约简方法](https://arxiv.org/abs/2607.09516v1)
- Original title: A multi-ensemble mean-field reduction method for networks of globally coupled phase oscillators with arbitrary parameter distributions
- Authors: Richard Gast, Shotaro Takasu, Helmut Schmidt, Ann Kennedy
- Meta: 2026-07-10 | cond-mat.dis-nn
- 中文摘要: 了解具有异构振荡器频率的耦合相位振荡器系统的动态特性一直是复杂系统理论的长期挑战。虽然 Ott 和 Antonsen 的开创性工作极大地提高了我们对一小部分振荡器频率分布的耦合相位振荡器的理论理解，但我们在这里提出了一种针对任意频率分布的平均场降低方法。我们的方法利用洛伦兹频率分布获得的大幅降维，并将其与数据驱动的多集成方法相结合。
- Abstract: Understanding the dynamical properties of coupled phase oscillator systems with heterogeneous oscillator frequencies has been a long-standing challenge of complex systems theory. While the seminal work of Ott and Antonsen dramatically improved our theoretical understanding of coupled phase oscillators for a small family of oscillator frequency distributions, we here present a mean-field reduction method for arbitrar...
- Summary (fallback): 机器翻译摘要显示：了解具有异构振荡器频率的耦合相位振荡器系统的动态特性一直是复杂系统理论的长期挑战。虽然 Ott 和 Antonsen 的开创性工作极大地提高了我们对一小部分振荡器频率分布的耦合相位振荡器的理论理解，但我们在这里提出了一种针对任意频率分布的平均场降低方法。我们的方法利用洛伦兹频率分布获得的大幅降维，并将其与数据驱动的多集成方法相结合。
- Keywords: distributions, reduction, method, phase, oscillator

### 21. [所有解释都是错误的，但许多解释都是有用的：用大型语言模型探索罗生门解释集](https://arxiv.org/abs/2607.09502v1)
- Original title: All Explanations are Wrong, But Many Are Useful: Exploring the Rashomon Explanation Set with Large Language Models
- Authors: Pan Li
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 解释机器学习模型对于决策和消费者信任变得越来越重要，但人们普遍认为这是有代价的：现有的可解释人工智能（XAI）方法一直面临着准确性与可解释性之间的权衡。我们认为，这种权衡并不是根本性的，而是将解释和预测视为独立目标的产物；当正确耦合时，它们会变得互补，因此配备模型来解释自身可以提高而不是降低其准确性。我们引入了罗生门解释范式，它构建了一组忠实的预测指导解释，而不是单个解释，并证明该集合通常是非空的，并且解释保真度限制了它所指导的模型的性能。
- Abstract: Explaining machine-learning models is increasingly important for decision-making and consumer trust, yet it is widely believed to come at a cost: existing Explainable AI (XAI) methods suffer from a persistent accuracy-explainability trade-off. We argue that this trade-off is not fundamental, but an artifact of treating explanation and prediction as separate objectives; when properly coupled, they become complementar...
- Summary (fallback): 机器翻译摘要显示：解释机器学习模型对于决策和消费者信任变得越来越重要，但人们普遍认为这是有代价的：现有的可解释人工智能（XAI）方法一直面临着准确性与可解释性之间的权衡。我们认为，这种权衡并不是根本性的，而是将解释和预测视为独立目标的产物；当正确耦合时，它们会变得互补，因此配备模型来解释自身可以提高而不是降低其准确性。我们引入了罗生门解释范式，它构建了一组忠实的预测指导解释，而不是单个解释，并证明该集合通常是非空的，并且解释保真度限制了它所指导的模型的性能。
- Keywords: explanation, explanations, models, prediction, rashomon

### 22. [时间序列的终端降维及其应用](https://arxiv.org/abs/2607.09490v1)
- Original title: Terminal Dimension Reduction for Time Series with Applications
- Authors: Alexander Munteanu, Matteo Russo, David Saulpic, Chris Schwiegelshohn
- Meta: 2026-07-10 | cs.DS
- 中文摘要: 终端嵌入已成为降维的强大工具。给定一组点 $P\subset \mathbb{R}^d$，终端嵌入是一个映射 $f:\mathbb{R}^d\rightarrow \mathbb{R}^t$，它在该映射下保留任意一对点 $p\in P$ 和 $q\in \mathbb{R}^d$ 之间的成对距离，直至出现小失真。终端嵌入对于构建 $k$-means 和 $k$-median 核心集特别有效，其目标是找到 $P$ 的典型加权子集 $Ω$，这样对于任何候选解决方案，$Ω$ 上的聚类目标成本近似于 $P$ 上的聚类目标成本，直至小失真。不幸的是，这些技术尚未扩展到更复杂的结构，例如在测量之间的常见直线插值下对时间序列数据进行聚类。
- Abstract: Terminal embeddings have emerged as a powerful tool for dimension reduction. Given a set of points $P\subset \mathbb{R}^d$, a terminal embedding is a mapping $f:\mathbb{R}^d\rightarrow \mathbb{R}^t$ that preserves the pairwise distance between any pair of points $p\in P$ and $q\in \mathbb{R}^d$ up to small distortion under this mapping. Terminal embeddings have been particularly fruitful for constructing $k$-means a...
- Summary (fallback): 机器翻译摘要显示：终端嵌入已成为降维的强大工具。给定一组点 $P\subset \mathbb{R}^d$，终端嵌入是一个映射 $f:\mathbb{R}^d\rightarrow \mathbb{R}^t$，它在该映射下保留任意一对点 $p\in P$ 和 $q\in \mathbb{R}^d$ 之间的成对距离，直至出现小失真。终端嵌入对于构建 $k$-means 和 $k$-median 核心集特别有效，其目标是找到 $P$ 的典型加权子集 $Ω$，这样对于任何候选解决方案，$Ω$ 上的聚类目标成本近似于 $P$ 上的聚类目标成本，直至小失真。不幸的是，这些技术尚未扩展到更复杂的结构，例如在测量之间的常见直线插值下对时间序列数据进行聚类。
- Keywords: terminal, embeddings, mathbb, clustering, dimension

### 23. [禁止神经崩溃：语言模型中的信息层](https://arxiv.org/abs/2607.09487v1)
- Original title: Neural Collapse Is Forbidden: Information Floors in Language Models
- Authors: Bruno Abrahao
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 语言模型表示的类内方差通常被解读为不完全的神经崩溃。我们认为它是分配的信息存储，并且分配遵循规律。单行居中恒等式使一系列单纯形等角紧框架断言无效，包括我们自己早期的断言；在 14 个模型的无量纲方差份额中，宏观类别结构仅携带 4-12% 的表征方差，而标记内上下文则携带 79-91%，在 100 倍参数范围内保持稳定。从理论上讲，令牌级别的权重衰减按类别的类型计数而不是其出现质量的比例对类别进行惩罚，从而将下一个令牌预测减少为不平衡的 K 类问题，其最佳顺序按类型计数对类别规范进行排序。
- Abstract: Within-class variance in language-model representations is commonly read as incomplete neural collapse. We argue it is allocated information storage, and that the allocation obeys a law. A one-line centering identity voids a family of simplex equiangular-tight-frame claims, including our own earlier ones; in dimensionless variance shares across 14 models, macro-category structure carries only 4-12% of representation...
- Summary (fallback): 机器翻译摘要显示：语言模型表示的类内方差通常被解读为不完全的神经崩溃。我们认为它是分配的信息存储，并且分配遵循规律。单行居中恒等式使一系列单纯形等角紧框架断言无效，包括我们自己早期的断言；在 14 个模型的无量纲方差份额中，宏观类别结构仅携带 4-12% 的表征方差，而标记内上下文则携带 79-91%，在 100 倍参数范围内保持稳定。从理论上讲，令牌级别的权重衰减按类别的类型计数而不是其出现质量的比例对类别进行惩罚，从而将下一个令牌预测减少为不平衡的 K 类问题，其最佳顺序按类型计数对类别规范进行排序。
- Keywords: information, variance, across, category, models

### 24. [将语言指导与文本引导医疗分割的主干分离](https://arxiv.org/abs/2607.09481v1)
- Original title: Decoupling Language Guidance from Backbones for Text-Guided Medical Segmentation
- Authors: Yungeng Liu, Xuanzi Fang, Haijin Zeng, Qi Dai, Yongyong Chen
- Meta: 2026-07-10 | cs.CV
- 中文摘要: 文本引导的医学图像分割利用临床语义来改善病变描绘，但许多现有模型将跨模式融合、监督和解码器设计绑定到特定于任务的架构中。这种紧密耦合使得跨异构视觉和文本主干重用语言指导模块变得困难，并且当编码器对发生变化时通常需要重新设计网络。本文提出了 BTHA，一种用于文本引导医学图像分割的主干可转移分层适配器框架。 BTHA 围绕稳定的特征级接口构建：给定多尺度视觉特征和文本表示，它通过形状保留适配器注入语义指导，同时维护解码器端张量契约。
- Abstract: Text-guided medical image segmentation leverages clinical semantics to improve lesion delineation, yet many existing models bind cross-modal fusion, supervision, and decoder design into a task-specific architecture. Such tight coupling makes it difficult to reuse language guidance modules across heterogeneous vision and text backbones, and often requires redesigning the network when the encoder pair changes. This pa...
- Summary (fallback): 机器翻译摘要显示：文本引导的医学图像分割利用临床语义来改善病变描绘，但许多现有模型将跨模式融合、监督和解码器设计绑定到特定于任务的架构中。这种紧密耦合使得跨异构视觉和文本主干重用语言指导模块变得困难，并且当编码器对发生变化时通常需要重新设计网络。本文提出了 BTHA，一种用于文本引导医学图像分割的主干可转移分层适配器框架。 BTHA 围绕稳定的特征级接口构建：给定多尺度视觉特征和文本表示，它通过形状保留适配器注入语义指导，同时维护解码器端张量契约。
- Keywords: guidance, text-guided, language, backbones, medical

### 25. [聚焦点引导动态令牌选择，实现稳健高效的视觉 Transformer](https://arxiv.org/abs/2607.09480v1)
- Original title: Foveation-Guided Dynamic Token Selection for Robust and Efficient Vision Transformers
- Authors: Ibrahim Batuhan Akkaya, Kishaan Jeeveswaran, Bahram Zonooz, Elahe Arani
- Meta: 2026-07-10 | cs.CV
- 中文摘要: 人类视觉系统 (HVS) 采用中心点采样和眼球运动来实现高效感知，从而节省代谢能量和计算资源。从这种鲁棒性和适应性中汲取灵感，我们引入了 Foveated Dynamic Transformer (FDT)，这是一种注视点引导的动态令牌选择架构，它将这些机制集成到视觉转换器框架中。尽管没有针对此类挑战进行过明确的培训，但 FDT 对各种类型的噪声和对抗性攻击表现出强大的恢复能力。这种固有的鲁棒性是通过使用注视点和注视点模块来实现的：注视点模块识别注视点以过滤掉不相关的信息，而注视点模块则生成具有多尺度信息的注视点嵌入。在 50% 的注视预算设置下，FDT 比 DeiT-S 实现了更高的准确度（81.9% vs.
- Abstract: The human visual system (HVS) employs foveated sampling and eye movements to achieve efficient perception, conserving both metabolic energy and computational resources. Drawing inspiration from this robustness and adaptability, we introduce the Foveated Dynamic Transformer (FDT), a foveation-guided dynamic token-selection architecture that integrates these mechanisms into a vision transformer framework. The FDT exhi...
- Summary (fallback): 机器翻译摘要显示：人类视觉系统 (HVS) 采用中心点采样和眼球运动来实现高效感知，从而节省代谢能量和计算资源。从这种鲁棒性和适应性中汲取灵感，我们引入了 Foveated Dynamic Transformer (FDT)，这是一种注视点引导的动态令牌选择架构，它将这些机制集成到视觉转换器框架中。尽管没有针对此类挑战进行过明确的培训，但 FDT 对各种类型的噪声和对抗性攻击表现出强大的恢复能力。这种固有的鲁棒性是通过使用注视点和注视点模块来实现的：注视点模块识别注视点以过滤掉不相关的信息，而注视点模块则生成具有多尺度信息的注视点嵌入。在 50% 的注视预算设置下，FDT 比 DeiT-S 实现了更高的准确度（81.9% vs.
- Keywords: dynamic, foveated, fixation, foveation-guided, efficient

### 26. [使用一阶条件的递归实用程序的深度学习动态规划](https://arxiv.org/abs/2607.09461v1)
- Original title: Deep Learning for Dynamic Programming with Recursive Utility Using First-order Conditions
- Authors: Xianhua Peng, Wu Guo, Songyan Wang, Jianfei Zhu
- Meta: 2026-07-10 | q-fin.CP
- 中文摘要: 本文提出了确定性等效一阶学习（CEFOL）算法，这是一种利用递归效用解决离散时间动态规划问题的深度学习算法。具有递归效用的动态规划具有挑战性，因为非线性确定性等价出现在贝尔曼方程和一阶最优性条件中，但难以评估。通过引入单独的神经网络来表示确定性等价物，CEFOL 能够利用贝尔曼和特定于模型的一阶最优条件。除了确定性等价之外，CEFOL 还使用神经网络来学习价值函数、策略函数和拉格朗日乘子，通过使用模型特定的一阶条件来构造残差以实现最小化。
- Abstract: This paper proposes the certainty-equivalent first-order learning (CEFOL) algorithm, a deep learning algorithm for solving discrete-time dynamic programming problems with recursive utility. Dynamic programming with recursive utility is challenging because nonlinear certainty equivalent appears in the Bellman equation and the first-order optimality conditions but is difficult to evaluate. By introducing a separate ne...
- Summary (fallback): 机器翻译摘要显示：本文提出了确定性等效一阶学习（CEFOL）算法，这是一种利用递归效用解决离散时间动态规划问题的深度学习算法。具有递归效用的动态规划具有挑战性，因为非线性确定性等价出现在贝尔曼方程和一阶最优性条件中，但难以评估。通过引入单独的神经网络来表示确定性等价物，CEFOL 能够利用贝尔曼和特定于模型的一阶最优条件。除了确定性等价之外，CEFOL 还使用神经网络来学习价值函数、策略函数和拉格朗日乘子，通过使用模型特定的一阶条件来构造残差以实现最小化。
- Keywords: first-order, utility, recursive, cefol, dynamic

### 27. [主动拒绝能够可靠地推广通用机器学习原子间势](https://arxiv.org/abs/2607.09456v1)
- Original title: Active rejection enables reliable generalization of universal machine-learning interatomic potentials
- Authors: Mingxiang Luo, Xinnan Mao, Lu Wang, Lei Bai, Feng Ding et al.
- Meta: 2026-07-10 | cs.LG
- 中文摘要: 通用机器学习原子间势 (uMLIP) 连接了量子力学精度和大规模分子动力学，但 r$^2$SCAN 等高精度计算的成本限制了对相对于开放材料空间仍然较小的数据集的训练。强大的平均基准性能也不能保证对每个结构进行可靠的能量-力预测。我们提出了自适应多教师路由（ATR），它将高保真数据构建重新表述为不确定性下的结构决策问题。使用一小组真实的 r$^2$SCAN 标签，ATR 校准多个预训练的 uMLIP 教师，并结合结构描述符、教师身份和教师间分歧来估计每个结构-教师对的可靠性。
- Abstract: Universal machine learning interatomic potentials (uMLIPs) bridge quantum-mechanical accuracy and large-scale molecular dynamics, but the cost of high-accuracy calculations such as r$^2$SCAN limits training to datasets that remain small relative to the open materials space. Strong average benchmark performance also does not guarantee reliable energy--force predictions for every structure. We propose Adaptive Multi-T...
- Summary (fallback): 机器翻译摘要显示：通用机器学习原子间势 (uMLIP) 连接了量子力学精度和大规模分子动力学，但 r$^2$SCAN 等高精度计算的成本限制了对相对于开放材料空间仍然较小的数据集的训练。强大的平均基准性能也不能保证对每个结构进行可靠的能量-力预测。我们提出了自适应多教师路由（ATR），它将高保真数据构建重新表述为不确定性下的结构决策问题。使用一小组真实的 r$^2$SCAN 标签，ATR 校准多个预训练的 uMLIP 教师，并结合结构描述符、教师身份和教师间分歧来估计每个结构-教师对的可靠性。
- Keywords: scan, reliable, umlips, multiple, structures

### 28. [通过测试时提示适应来增强视觉语言模型](https://arxiv.org/abs/2607.09450v1)
- Original title: Robustifying Vision-Language Models via Test-Time Prompt Adaptation
- Authors: Xingyu Zhu, Huanshen Wu, Shuo Wang, Beier Zhu, Jiannan Ge et al.
- Meta: 2026-07-10 | cs.CV
- 中文摘要: CLIP 等预训练视觉语言模型 (VLM) 实现了强大的零样本泛化，但它们的性能在对抗性扰动下急剧下降。现有的测试时间适应方法通常依赖于样本级置信启发法，忽略了数据的内在分布结构。这种以样本为中心的方法限制了鲁棒性，因为它无法区分可信的对抗性错误预测和真正的语义一致性。在这项工作中，我们观察到对抗性扭曲在结构上是脆弱的：虽然整体表示被破坏，但语义完整性通常在增强视图的分布中得以保留。受这一见解的启发，我们提出了 RITA，这是一个鲁棒的测试时间提示适应框架，从样本级别估计转向分布级别对齐。
- Abstract: Pre-trained Vision-Language Models (VLMs) such as CLIP achieve strong zero-shot generalization, but their performance degrades sharply under adversarial perturbations. Existing test-time adaptation methods typically rely on sample-level confidence heuristics, overlooking the intrinsic distributional structure of the data. This sample-centric approach limits robustness, as it fails to distinguish confident adversaria...
- Summary (fallback): 机器翻译摘要显示：CLIP 等预训练视觉语言模型 (VLM) 实现了强大的零样本泛化，但它们的性能在对抗性扰动下急剧下降。现有的测试时间适应方法通常依赖于样本级置信启发法，忽略了数据的内在分布结构。这种以样本为中心的方法限制了鲁棒性，因为它无法区分可信的对抗性错误预测和真正的语义一致性。在这项工作中，我们观察到对抗性扭曲在结构上是脆弱的：虽然整体表示被破坏，但语义完整性通常在增强视图的分布中得以保留。受这一见解的启发，我们提出了 RITA，这是一个鲁棒的测试时间提示适应框架，从样本级别估计转向分布级别对齐。
- Keywords: adversarial, test-time, semantic, rita, vision-language

### 29. [多项式时间内接近最优的节点私有社区估计](https://arxiv.org/abs/2607.09441v1)
- Original title: Near-optimal node-private community estimation in polynomial-time
- Authors: Laurentiu Marchis, Olga Klopp, Po-Ling Loh, Ilias Zadik
- Meta: 2026-07-10 | math.ST
- 中文摘要: 在本文中，我们通过提供高概率多项式时间节点私有算法解决了 Klopp & Zadik (2026) 的一个悬而未决的问题，该算法几乎与他们的指数时间节点私有算法的性能相匹配，用于随机块模型中的精确恢复。我们的结果涉及为惩罚似然函数明确构造的 Lipschitz 代理，以及精心设计的接受-拒绝算法，该算法在多项式时间内从相应的指数机制中采样社区标签。我们严格分析了我们提出的算法的隐私、运行时间和实用性，表明即使社区数量 K 随节点数量 n 对数增长，我们也可以通过隐私参数 epsilon 作为 log(n) 增长来实现精确恢复的极小最大速率，从而匹配此设置的隐私成本的已知下限。
- Abstract: In this paper, we resolve an open question of Klopp & Zadik (2026) by providing a high-probability polynomial-time, node-private algorithm which nearly matches the performance of their exponential-time node-private algorithm for exact recovery in stochastic block models. Our result involves an explicitly constructed Lipschitz surrogate for the penalized likelihood function, as well as a carefully devised accept-reje...
- Summary (fallback): 机器翻译摘要显示：在本文中，我们通过提供高概率多项式时间节点私有算法解决了 Klopp & Zadik (2026) 的一个悬而未决的问题，该算法几乎与他们的指数时间节点私有算法的性能相匹配，用于随机块模型中的精确恢复。我们的结果涉及为惩罚似然函数明确构造的 Lipschitz 代理，以及精心设计的接受-拒绝算法，该算法在多项式时间内从相应的指数机制中采样社区标签。我们严格分析了我们提出的算法的隐私、运行时间和实用性，表明即使社区数量 K 随节点数量 n 对数增长，我们也可以通过隐私参数 epsilon 作为 log(n) 增长来实现精确恢复的极小最大速率，从而匹配此设置的隐私成本的已知下限。
- Keywords: algorithm, node-private, polynomial-time, privacy, community

### 30. [多语言 Visual MCQ 上小型 VLM 的测试时间缩放](https://arxiv.org/abs/2607.09438v1)
- Original title: Test-Time Scaling for Small VLMs on Multilingual Visual MCQ
- Authors: Spiros Baxevanakis, Peng-Jian Yang
- Meta: 2026-07-10 | cs.CL
- 中文摘要: 测试时间缩放（TTS）可靠地改善了大型语言模型的推理，但它是否转移到小型开放视觉语言模型仍不清楚。我们在 EXAMS-V（一种多语言视觉多项选择基准）上对此进行了检查，比较了自我一致性、描述然后推理与 PRM 引导束搜索以及 Qwen2.5-VL-7B-Instruct 和 Qwen3.5-4B 中的两个事后选择器。重要的是 TTS 运行的条件，而不是搜索或验证机制。最大的因素是可解析性：早期的提示格式使许多链能够正确推理，但从未承诺回复信，而标准答案提示和引导修复步骤在很大程度上消除了这一点。更大的解码预算会消除其余部分：将每链代币限制从 1k 提高到 2k 可恢复 3.7 个百分点，而采样更多链（8 至 16 个）仅增加 0.15 个百分点。
- Abstract: Test-time scaling (TTS) reliably improves reasoning in large language models, but whether it transfers to small open vision-language models remains unclear. We examine this on EXAMS-V, a multilingual visual multiple-choice benchmark, comparing self-consistency, describe-then-reason with PRM-guided beam search, and two post-hoc selectors across Qwen2.5-VL-7B-Instruct and Qwen3.5-4B. What matters is the conditions und...
- Summary (fallback): 机器翻译摘要显示：测试时间缩放（TTS）可靠地改善了大型语言模型的推理，但它是否转移到小型开放视觉语言模型仍不清楚。我们在 EXAMS-V（一种多语言视觉多项选择基准）上对此进行了检查，比较了自我一致性、描述然后推理与 PRM 引导束搜索以及 Qwen2.5-VL-7B-Instruct 和 Qwen3.5-4B 中的两个事后选择器。重要的是 TTS 运行的条件，而不是搜索或验证机制。最大的因素是可解析性：早期的提示格式使许多链能够正确推理，但从未承诺回复信，而标准答案提示和引导修复步骤在很大程度上消除了这一点。更大的解码预算会消除其余部分：将每链代币限制从 1k 提高到 2k 可恢复 3.7 个百分点，而采样更多链（8 至 16 个）仅增加 0.15 个百分点。
- Keywords: visual, search, chains, test-time, scaling

## biorxiv

### 1. [星形胶质细胞和内皮细胞 GLUT1 恢复可改善 GLUT1 缺乏综合征中的脑葡萄糖稳态](https://www.biorxiv.org/content/10.64898/2026.03.04.709430v4)
- Original title: Astrocytic and endothelial GLUT1 restoration improves brain glucose homeostasis in GLUT1 deficiency syndrome
- Authors: Tamura, S., Shimbo, H., Aruga, N., Kawaguchi, M., Okado, H. et al.
- Meta: 2026-07-13 | neuroscience | DOI: 10.64898/2026.03.04.709430
- 中文摘要: 葡萄糖转运蛋白 1 缺乏综合征 (GLUT1-DS) 是一种由大脑葡萄糖转运受损引起的严重神经代谢紊乱。由于 GLUT1 传统上被认为主要定位于血脑屏障内皮细胞，因此基因治疗策略主要集中于内皮 GLUT1 的恢复。然而，这种以内皮为中心的模型是否能充分解释疾病的发病机制和治疗拯救仍不清楚。通过对小鼠大脑和人类死后组织的增强检测，我们发现 GLUT1 在星形胶质细胞和内皮细胞中广泛表达，从血管末足延伸到星形胶质细胞胞体和突起。
- Abstract: Glucose transporter 1 deficiency syndrome (GLUT1-DS) is a severe neurometabolic disorder caused by impaired brain glucose transport. Because GLUT1 has been classically viewed as predominantly localized to blood-brain barrier endothelial cells, gene therapy strategies have largely focused on endothelial GLUT1 restoration. However, whether this endothelial-centered model fully explains disease pathogenesis and therape...
- Summary (fallback): 机器翻译摘要显示：葡萄糖转运蛋白 1 缺乏综合征 (GLUT1-DS) 是一种由大脑葡萄糖转运受损引起的严重神经代谢紊乱。由于 GLUT1 传统上被认为主要定位于血脑屏障内皮细胞，因此基因治疗策略主要集中于内皮 GLUT1 的恢复。然而，这种以内皮为中心的模型是否能充分解释疾病的发病机制和治疗拯救仍不清楚。通过对小鼠大脑和人类死后组织的增强检测，我们发现 GLUT1 在星形胶质细胞和内皮细胞中广泛表达，从血管末足延伸到星形胶质细胞胞体和突起。
- Keywords: glut1, endothelial, glucose, restoration, brain

### 2. [鉴定 A/H5N1 禽流感 HLA-A33 限制性 CD8+ T 细胞表位](https://www.biorxiv.org/content/10.64898/2026.06.21.733083v2)
- Original title: Identification of HLA-A33-restricted CD8+ T cell epitopes from avian influenza A/H5N1
- Authors: Muraduzzaman, A. K. M., Illing, P. T., Jenzen, M., Croft, N. P., Williams, S. M. et al.
- Meta: 2026-07-13 | immunology | DOI: 10.64898/2026.06.21.733083
- 中文摘要: A/H5N1 禽流感的快速演变，包括最近在美国爆发的 2.3.4.4b 分支，凸显了其大流行的潜力以及对持久、广泛保护性疫苗的迫切需要。鉴于 CD8+ T 细胞介导交叉毒株免疫的能力，我们研究了地理上不同的 HLA-A33 同种异型（东亚/东南亚的 HLA-A*33:01 和南亚的 HLA-A*33:03）是否对流感免疫肽组有不同的塑造并影响抗病毒免疫。过表达 HLA-A*33:01 或 HLA-A*33:03 的抗原呈递细胞用单一 A/H5N1 抗原转染或用 A/X-31 (H3N2) 感染，作为代表当前季节性流感病毒的对照比较。我们鉴定了仅限于 HLA-A*33:01（57 个来自 A/H5N1；55 个来自 A/X-31）和 HLA-A*33:03（29 个来自 A/H5N1；45 个来自 A/X-31）的新配体。
- Abstract: The rapid evolution of avian influenza A/H5N1, including the recent U.S. clade 2.3.4.4b outbreak, highlights its pandemic potential and the urgent need for durable, broadly protective vaccines. Given the capacity of CD8+ T cells to mediate cross-strain immunity, we investigated whether geographically distinct HLA-A33 allotypes, HLA-A*33:01 in East/Southeast Asia and HLA-A*33:03 in South Asia, differentially shape th...
- Summary (fallback): 机器翻译摘要显示：A/H5N1 禽流感的快速演变，包括最近在美国爆发的 2.3.4.4b 分支，凸显了其大流行的潜力以及对持久、广泛保护性疫苗的迫切需要。鉴于 CD8+ T 细胞介导交叉毒株免疫的能力，我们研究了地理上不同的 HLA-A33 同种异型（东亚/东南亚的 HLA-A*33:01 和南亚的 HLA-A*33:03）是否对流感免疫肽组有不同的塑造并影响抗病毒免疫。过表达 HLA-A*33:01 或 HLA-A*33:03 的抗原呈递细胞用单一 A/H5N1 抗原转染或用 A/X-31 (H3N2) 感染，作为代表当前季节性流感病毒的对照比较。我们鉴定了仅限于 HLA-A*33:01（57 个来自 A/H5N1；55 个来自 A/X-31）和 HLA-A*33:03（29 个来自 A/H5N1；45 个来自 A/X-31...
- Keywords: hla-a, h5n1, influenza, peptides, cell

### 3. [分泌途径的乙酰化依赖性重塑塑造了衰老相关的分泌组](https://www.biorxiv.org/content/10.64898/2026.06.23.733964v3)
- Original title: Acetylation-dependent remodeling of the secretory pathway shapes the senescence-associated secretome
- Authors: Nasrashvili, T., Emini, B., Cirri, E., Rahnis, N., Poempner, N. et al.
- Meta: 2026-07-13 | cell biology | DOI: 10.64898/2026.06.23.733964
- 中文摘要: 细胞衰老的特征是稳定的细胞周期停滞和衰老相关的分泌表型（SASP），这会驱动组织重塑和炎症。 SASP 细胞因子和其他分泌蛋白分泌增加，其背后是分泌途径的大规模重组。虽然衰老的转录调控已被广泛研究，但翻译后修饰 (PTM) 对分泌途径调控的贡献仍知之甚少。在这里，我们将定量蛋白质组学与磷酸化、泛素化和乙酰化的多层 PTM 分析相结合，以研究衰老过程中细胞内运输和分泌的调节方式。
- Abstract: Cellular senescence is characterized by stable cell cycle arrest and the senescence-associated secretory phenotype (SASP), which drives tissue remodeling and inflammation. Underlying SASP with its increased secretion of cytokines and other secreted proteins is a massive reorganization of the secretory pathway. While transcriptional regulation of senescence has been extensively studied, the contribution of post-trans...
- Summary (fallback): 机器翻译摘要显示：细胞衰老的特征是稳定的细胞周期停滞和衰老相关的分泌表型（SASP），这会驱动组织重塑和炎症。 SASP 细胞因子和其他分泌蛋白分泌增加，其背后是分泌途径的大规模重组。虽然衰老的转录调控已被广泛研究，但翻译后修饰 (PTM) 对分泌途径调控的贡献仍知之甚少。在这里，我们将定量蛋白质组学与磷酸化、泛素化和乙酰化的多层 PTM 分析相结合，以研究衰老过程中细胞内运输和分泌的调节方式。
- Keywords: senescence, secretory, senescence-associated, remodeling, pathway

### 4. [雷达数据中空中动物分类的形态类型方法](https://www.biorxiv.org/content/10.64898/2026.03.24.713935v3)
- Original title: The morphotype approach to classification of aerial animals in radar data
- Authors: Werber, Y.
- Meta: 2026-07-13 | ecology | DOI: 10.64898/2026.03.24.713935
- 中文摘要: 雷达航空生态学利用雷达对空中野生动物进行生态推断。虽然生成描述空气生物活动的独特的大规模数据集，但雷达基本上无法将检测结果与特定物种相关联，因此在分类学上受到限制。我描述了一种分析方法，通过将检测到的生物体分为基于形态和运动的空中形态类型来提高垂直雷达数据的分类分辨率。 Birdscan MR1 雷达广泛用于空中野生动物研究和监测，部署在欧洲、近东和美国的数十个地点。通过使用 MR1 目标分类器、机翼扑动频率计算和目标大小估计，我使用以色列胡拉谷研究站的雷达数据证明鸟类分类分辨率提高了近 8 倍。
- Abstract: Radar aeroecology makes ecological inferences about aerial wildlife using radars. While generating unique, large-scale datasets describing airborne biological activity, radars are largely incapable of relating detections to specific species and are thus taxonomically limited. I describe an analytical method to increase taxonomic resolution in vertical looking radar data by dividing detected organisms into morphology...
- Summary (fallback): 机器翻译摘要显示：雷达航空生态学利用雷达对空中野生动物进行生态推断。虽然生成描述空气生物活动的独特的大规模数据集，但雷达基本上无法将检测结果与特定物种相关联，因此在分类学上受到限制。我描述了一种分析方法，通过将检测到的生物体分为基于形态和运动的空中形态类型来提高垂直雷达数据的分类分辨率。 Birdscan MR1 雷达广泛用于空中野生动物研究和监测，部署在欧洲、近东和美国的数十个地点。通过使用 MR1 目标分类器、机翼扑动频率计算和目标大小估计，我使用以色列胡拉谷研究站的雷达数据证明鸟类分类分辨率提高了近 8 倍。
- Keywords: radar, aerial, approach, aeroecology, increase

### 5. [Spermacoceae（茜草科）部落的质体系统发育组学：分类学意义和属的关键](https://www.biorxiv.org/content/10.64898/2026.07.10.737747v1)
- Original title: Plastome phylogenomics of the tribe Spermacoceae (Rubiaceae): taxonomic implications and a key to the genera
- Authors: Nunez Florentin, M., Claypool, K., Huda, N., Green, K., Monzel, G. et al.
- Meta: 2026-07-13 | plant biology | DOI: 10.64898/2026.07.10.737747
- 中文摘要: 受精科（茜草科）部落由约 1,400 种形态多样的物种组成，分布在新热带地区、非洲、亚洲、澳大利亚和太平洋地区。它仍然是该家族中分类学上最棘手的群体之一，两个多世纪以来，其属种限制不断被重新定义。先前基于有限数量的质体和核标记的系统发育研究留下了许多未解决的关系，并提供了新热带谱系的稀疏代表性。在这里，我们基于质体规模数据和新热带类群的扩大采样，提出了该部落的首次系统发育学研究。我们对涵盖所有主要分支的 55 个属的 121 个物种进行了采样，并生成了 123 个新的质体，其中包括首次纳入分子系统发育框架的 25 个物种。
- Abstract: The tribe Spermacoceae (Rubiaceae) comprises a morphologically diverse assemblage of approximately 1,400 species distributed across the Neotropics, Africa, Asia, Australia, and Pacific region. It remains one of the most taxonomically intractable groups in the family, with generic limits repeatedly redefined for more than two centuries. Previous phylogenetic studies based on a limited number of plastid and nuclear ma...
- Summary (fallback): 机器翻译摘要显示：受精科（茜草科）部落由约 1,400 种形态多样的物种组成，分布在新热带地区、非洲、亚洲、澳大利亚和太平洋地区。它仍然是该家族中分类学上最棘手的群体之一，两个多世纪以来，其属种限制不断被重新定义。先前基于有限数量的质体和核标记的系统发育研究留下了许多未解决的关系，并提供了新热带谱系的稀疏代表性。在这里，我们基于质体规模数据和新热带类群的扩大采样，提出了该部落的首次系统发育学研究。我们对涵盖所有主要分支的 55 个属的 121 个物种进行了采样，并生成了 123 个新的质体，其中包括首次纳入分子系统发育框架的 25 个物种。
- Keywords: genera, phylogenetic, tribe, spermacoceae, species

### 6. [高通量气孔表型分析为抗逆小麦提供选择目标](https://www.biorxiv.org/content/10.64898/2026.07.10.737162v1)
- Original title: High-throughput stomatal phenotyping provides selection targets for stress-resilient wheat
- Authors: Mabrouk, M., Russell, N. J., Alegria, E. V., Wang, T.-C., Liang, J.-A. et al.
- Meta: 2026-07-13 | plant biology | DOI: 10.64898/2026.07.10.737162
- 中文摘要: 对气孔性状及其发育可塑性进行表型分析非常耗时，但有可能提高水分利用效率和光合作用，从而设计气候变化下的耐逆作物。在这里，我们开发了一个强大的高通量管道，用于对冬小麦中与大小、变异、最大电导度和空间模式相关的 14 个气孔性状进行表型分析。我们 (1) 分析了在生长室、温室和田间条件下生长的 60 个小麦品种的 25,000 多张图像； (2) 研究光、温度以及水和氮供应减少对气孔性状及其近轴和远轴表面发育可塑性的影响； (3)评价气孔性状的遗传多样性和育种进展。
- Abstract: Phenotyping stomatal traits and their developmental plasticity is time-consuming but holds potential to improve water use efficiency and photosynthesis for designing stress-tolerant crops under climate change. Here, we develop a robust, high-throughput pipeline for phenotyping 14 stomatal traits in winter wheat related to size, variation, maximum conductance, and spatial patterning. We (1) analyze over 25,000 images...
- Summary (fallback): 机器翻译摘要显示：对气孔性状及其发育可塑性进行表型分析非常耗时，但有可能提高水分利用效率和光合作用，从而设计气候变化下的耐逆作物。在这里，我们开发了一个强大的高通量管道，用于对冬小麦中与大小、变异、最大电导度和空间模式相关的 14 个气孔性状进行表型分析。我们 (1) 分析了在生长室、温室和田间条件下生长的 60 个小麦品种的 25,000 多张图像； (2) 研究光、温度以及水和氮供应减少对气孔性状及其近轴和远轴表面发育可塑性的影响； (3)评价气孔性状的遗传多样性和育种进展。
- Keywords: stomatal, traits, conditions, phenotyping, wheat

### 7. [尽管存在遗传变异和营养诱导的表型可塑性，但协调的叶片水力阈值在杨树中保持几乎为零的气孔安全裕度](https://www.biorxiv.org/content/10.64898/2026.07.10.737750v1)
- Original title: Coordinated leaf hydraulic thresholds maintain virtually null stomatal safety margins in poplar despite genetic variation and nutrient-induced phenotypic plasticity
- Authors: CHASSAGNAUD, D., BEZON, L., LE JAN, I., FICHOT, R.
- Meta: 2026-07-13 | plant biology | DOI: 10.64898/2026.07.10.737750
- 中文摘要: 植物对缺水反应的叶片生理阈值序列被认为在功能上是协调的。然而，在种内水平上，跨基因型和环境在多大程度上维持这种协调仍然缺乏记录。我们对经过对照、额外氮或额外钾处理的河岸物种黑杨（DRA-038 与 PG-31）的两种基因型的叶子中气孔关闭、膨压损失和木质部栓塞的序列进行了表征。在控制条件下，使用光学脆弱性方法进行的栓塞测量表明，DRA-038 比 PG-31 更脆弱，这与使用参考 Cavitron 方法对茎进行的测量一致。气孔关闭始终发生在木质部栓塞之前，而一旦木质部栓塞已经达到 50%，通常就会观察到大量叶片的膨压损失。
- Abstract: The sequence of leaf physiological thresholds underlying plant responses to water deficit is thought to be functionally coordinated; yet, to what extent this coordination is maintained across genotypes and environments remains poorly documented at the intraspecific level. We characterized the sequence of stomatal closure, turgor loss and xylem embolism in the leaves of two genotypes of the riparian species Populus n...
- Summary (fallback): 机器翻译摘要显示：植物对缺水反应的叶片生理阈值序列被认为在功能上是协调的。然而，在种内水平上，跨基因型和环境在多大程度上维持这种协调仍然缺乏记录。我们对经过对照、额外氮或额外钾处理的河岸物种黑杨（DRA-038 与 PG-31）的两种基因型的叶子中气孔关闭、膨压损失和木质部栓塞的序列进行了表征。在控制条件下，使用光学脆弱性方法进行的栓塞测量表明，DRA-038 比 PG-31 更脆弱，这与使用参考 Cavitron 方法对茎进行的测量一致。气孔关闭始终发生在木质部栓塞之前，而一旦木质部栓塞已经达到 50%，通常就会观察到大量叶片的膨压损失。
- Keywords: leaf, thresholds, stomatal, genotypes, embolism

### 8. [通过基因删除和芳基醇氧化酶分析在工程细菌中进行空气驱动的醛合成](https://www.biorxiv.org/content/10.64898/2026.07.12.738062v1)
- Original title: Air-driven aldehyde synthesis in engineered bacteria via gene deletion and aryl-alcohol oxidase profiling
- Authors: Dickey, R. M., Bryan, J., Somasundaram, V., Anderson, S. R., Phan, N. et al.
- Meta: 2026-07-13 | synthetic biology | DOI: 10.64898/2026.07.12.738062
- 中文摘要: 用于氧化非天然醇的工程化细菌途径面临三个挑战：烟酰胺依赖性酶与细胞氧化还原代谢耦合，烟酰胺独立的芳基醇氧化酶（AAO）通常在细菌中表达较差，醛产物被宿主酶快速修饰。在这里，我们通过改造保留醛的大肠杆菌来发现和应用可溶性细菌 AAO，从而解决了这些局限性。筛选 51 个候选者发现了一个高表达序列簇，其中含有对多种芳香醇和呋喃基醇具有活性的酶。将性能最佳的 AAO 与醛保留细胞中的设计途径配对，可以从提供的醇开始形成模块化 C-N 和 C-C 键形成级联。
- Abstract: Engineered bacterial routes for oxidation of non-native alcohols face three challenges: Nicotinamide-dependent enzymes are coupled to cellular redox metabolism, nicotinamide-independent aryl-alcohol oxidases (AAOs) usually express poorly in bacteria, and aldehyde products are rapidly modified by host enzymes. Here, we address these limitations by engineering aldehyde-retaining Escherichia coli for discovery and appl...
- Summary (fallback): 机器翻译摘要显示：用于氧化非天然醇的工程化细菌途径面临三个挑战：烟酰胺依赖性酶与细胞氧化还原代谢耦合，烟酰胺独立的芳基醇氧化酶（AAO）通常在细菌中表达较差，醛产物被宿主酶快速修饰。在这里，我们通过改造保留醛的大肠杆菌来发现和应用可溶性细菌 AAO，从而解决了这些局限性。筛选 51 个候选者发现了一个高表达序列簇，其中含有对多种芳香醇和呋喃基醇具有活性的酶。将性能最佳的 AAO 与醛保留细胞中的设计途径配对，可以从提供的醇开始形成模块化 C-N 和 C-C 键形成级联。
- Keywords: alcohols, engineered, bacteria, enzymes, air-driven

### 9. [ARCHIVE：机器引导设计高效开放式 DNA 记录装置，以提高多重细胞历史追踪的分辨率](https://www.biorxiv.org/content/10.64898/2026.07.10.737758v1)
- Original title: ARCHIVE: Machine-Guided Design of an Efficient Open-Ended DNA Recording Device to Increase Resolution of Multiplexed Cell History Tracking
- Authors: Rosenstein, A. H., Garton, M.
- Meta: 2026-07-13 | synthetic biology | DOI: 10.64898/2026.07.10.737758
- 中文摘要: 工程化基于细胞的设备将事件记录到 DNA 中，既可以作为非烧蚀研究工具，也可以在临床上根据细胞历史制定基于基因电路的细胞治疗逻辑。无论是作为理解单细胞水平相互作用的手段，还是重建细胞事件历史的手段，细胞 DNA 记录设备都具有广泛的用途，其中基于主要编辑的方法处于这一努力的最前沿，尤其是 peCHYRON。然而，此类开放式记录工具的分辨率本质上受到编辑插入效率的限制，并且尚无法捕获 RNA 聚合酶 II 转录信号，而这些信号代表了功能定义的内源基因调控架构的很大一部分。
- Abstract: Engineering cell-based devices to record events into DNA has potential both as a non-ablative research tool and in the clinic for enacting gene-circuit-based logic of cell therapies conditional on cell history. Whether as a means of understanding interactions on the single-cell level, or reconstructing histories of cellular events, a cellular DNA recording device has widespread utility, with prime editing-based meth...
- Summary (fallback): 机器翻译摘要显示：工程化基于细胞的设备将事件记录到 DNA 中，既可以作为非烧蚀研究工具，也可以在临床上根据细胞历史制定基于基因电路的细胞治疗逻辑。无论是作为理解单细胞水平相互作用的手段，还是重建细胞事件历史的手段，细胞 DNA 记录设备都具有广泛的用途，其中基于主要编辑的方法处于这一努力的最前沿，尤其是 peCHYRON。然而，此类开放式记录工具的分辨率本质上受到编辑插入效率的限制，并且尚无法捕获 RNA 聚合酶 II 转录信号，而这些信号代表了功能定义的内源基因调控架构的很大一部分。
- Keywords: recording, efficiency, archive, device, resolution

### 10. [在 S-腺苷-L-甲硫氨酸合成酶中设计柔性环，能够生产具有选择性生化和细胞活性的 SAM 核碱基类似物](https://www.biorxiv.org/content/10.64898/2026.07.10.737877v1)
- Original title: Engineering a flexible loop in S-adenosyl-L-methionine synthetase enables production of SAM nucleobase analogues with selective biochemical and cellular activity
- Authors: Hazra, A. B., Kalita, D. B., Bhattacharyya, A., Gupte, V., Venugopal, V. et al.
- Meta: 2026-07-13 | synthetic biology | DOI: 10.64898/2026.07.10.737877
- 中文摘要: S-腺苷-L-蛋氨酸 (SAM) 是所有生命形式中必需的辅助因子，由蛋氨酸腺苷转移酶 (MAT) 从蛋氨酸和 ATP 合成。 SAM 中的腺嘌呤部分似乎没有直接的催化功能，一些 MAT 同系物可以在体外利用天然的三磷酸核苷酸，产生相应的 SAM 核碱基类似物。然而，MAT 酶的核苷酸选择的分子决定因素以及 SAM 中核碱基的细胞意义尚不清楚。在这项研究中，利用结构和生物信息学引导的诱变，我们确定了灵活的活性位点环作为 MAT 中核苷酸特异性的主要决定因素。环突变和环交换将 ATP 选择性大肠杆菌 MAT 转化为接受 GTP、CTP 和 UTP 的变体，从而能够酶促合成和纯化 S-鸟苷基-、S-胞苷-和 S-尿酰基-L-蛋氨酸...
- Abstract: S-adenosyl-L-methionine (SAM), an essential cofactor in all forms of life, is synthesized by the enzyme methionine adenosyltransferase (MAT) from methionine and ATP. The adenine moiety in SAM appears to have no direct function in catalysis, and some MAT homologs can utilize natural nucleotide triphosphates in vitro, producing the corresponding SAM nucleobase analogues. However, the molecular determinants of nucleoti...
- Summary (fallback): 机器翻译摘要显示：S-腺苷-L-蛋氨酸 (SAM) 是所有生命形式中必需的辅助因子，由蛋氨酸腺苷转移酶 (MAT) 从蛋氨酸和 ATP 合成。 SAM 中的腺嘌呤部分似乎没有直接的催化功能，一些 MAT 同系物可以在体外利用天然的三磷酸核苷酸，产生相应的 SAM 核碱基类似物。然而，MAT 酶的核苷酸选择的分子决定因素以及 SAM 中核碱基的细胞意义尚不清楚。在这项研究中，利用结构和生物信息学引导的诱变，我们确定了灵活的活性位点环作为 MAT 中核苷酸特异性的主要决定因素。环突变和环交换将 ATP 选择性大肠杆菌 MAT 转化为接受 GTP、CTP 和 UTP 的变体，从而能够酶促合成和纯化 S-鸟苷基-、S-胞苷-和 S-尿酰基-L-蛋氨酸...
- Keywords: loop, analogues, nucleotide, coli, flexible

### 11. [NPC1 缺陷参与与神经退行性变和细胞衰老特征相关的溶酶体 - 基因组 - 免疫程序](https://www.biorxiv.org/content/10.64898/2026.07.12.738054v1)
- Original title: NPC1 deficiency engages a lysosome - genome - immune program linked to neurodegeneration and cellular aging signatures
- Authors: Abyadeh, M., Zarei, M., Hou, P.-C., Sari, V., Lee, K. et al.
- Meta: 2026-07-13 | molecular biology | DOI: 10.64898/2026.07.12.738054
- 中文摘要: 溶酶体功能障碍是神经变性和衰老的一个突出特征，但溶酶体运输的主要缺陷如何转化为进行性细胞衰退仍知之甚少。 C 型尼曼皮克病 (NPC) 是由 NPC1 依赖性胆固醇输出受损引起的，提供了一个基因定义的模型来解决这个问题。在这里，我们发现 NPC1 缺陷会激活溶酶体、基因组、免疫轴，将胆固醇运输失败与神经变性和细胞衰老标志联系起来。在 Npc1 突变小鼠中，NPC1 缺失引发 DNA 损伤、神经炎症、小胶质细胞和星形胶质细胞激活、浦肯野神经元变性和运动功能障碍。一致的是，鼻咽癌患者来源的成纤维细胞表现出线粒体异常和广泛的 DNA 双链断裂。
- Abstract: Lysosomal dysfunction is a prominent feature of neurodegeneration and aging, yet how primary defects in lysosomal trafficking are converted into progressive cellular decline remains poorly understood. Niemann Pick disease type C (NPC), caused by impaired NPC1 dependent cholesterol export, provides a genetically defined model to address this question. Here, we show that NPC1 deficiency activates a lysosome, genome, i...
- Summary (fallback): 机器翻译摘要显示：溶酶体功能障碍是神经变性和衰老的一个突出特征，但溶酶体运输的主要缺陷如何转化为进行性细胞衰退仍知之甚少。 C 型尼曼皮克病 (NPC) 是由 NPC1 依赖性胆固醇输出受损引起的，提供了一个基因定义的模型来解决这个问题。在这里，我们发现 NPC1 缺陷会激活溶酶体、基因组、免疫轴，将胆固醇运输失败与神经变性和细胞衰老标志联系起来。在 Npc1 突变小鼠中，NPC1 缺失引发 DNA 损伤、神经炎症、小胶质细胞和星形胶质细胞激活、浦肯野神经元变性和运动功能障碍。一致的是，鼻咽癌患者来源的成纤维细胞表现出线粒体异常和广泛的 DNA 双链断裂。
- Keywords: npc1, lysosomal, immune, neurodegeneration, cellular

### 12. [病原体对神经表皮信号传导的破坏会损害溶酶体功能，从而破坏胶原蛋白稳态](https://www.biorxiv.org/content/10.1101/2025.06.28.662087v2)
- Original title: Pathogen Subversion of Neuro-Epidermal Signaling Impairs Lysosomal Function to Disrupt Collagen Homeostasis
- Authors: Li, Q., Liu, Y., Chen, H., Xiao, W., QI, B.
- Meta: 2026-07-13 | cell biology | DOI: 10.1101/2025.06.28.662087
- 中文摘要: 表皮依靠富含胶原蛋白的细胞外基质（ECM）来维持针对病原体的屏障完整性。溶酶体调节角质层胶原蛋白周转，但感染期间神经元信号如何调节表皮溶酶体功能和胶原组织仍不清楚。使用铜绿假单胞菌 PA14-秀丽隐杆线虫感染模型，我们证明病原体诱导的神经元信号传导会破坏表皮溶酶体活性和胶原蛋白重塑。 PA14 感染触发神经元分泌 NSIF-1（神经元分泌免疫因子 1），NSIF-1 易位至表皮并通过抑制转录因子 ELT-3 损害溶酶体酸化、成熟和降解。这种破坏导致胶原蛋白结构紊乱，损害角质层完整性和宿主抵抗力。
- Abstract: The epidermis relies on collagen-rich extracellular matrices (ECMs) to maintain barrier integrity against pathogens. Lysosomes regulate cuticle collagen turnover, yet how neuronal signaling modulates epidermal lysosomal function and collagen organization during infection remains unclear. Using Pseudomonas aeruginosa PA14-Caenorhabditis elegans infection model, we demonstrate that pathogen-induced neuronal signaling...
- Summary (fallback): 机器翻译摘要显示：表皮依靠富含胶原蛋白的细胞外基质（ECM）来维持针对病原体的屏障完整性。溶酶体调节角质层胶原蛋白周转，但感染期间神经元信号如何调节表皮溶酶体功能和胶原组织仍不清楚。使用铜绿假单胞菌 PA14-秀丽隐杆线虫感染模型，我们证明病原体诱导的神经元信号传导会破坏表皮溶酶体活性和胶原蛋白重塑。 PA14 感染触发神经元分泌 NSIF-1（神经元分泌免疫因子 1），NSIF-1 易位至表皮并通过抑制转录因子 ELT-3 损害溶酶体酸化、成熟和降解。这种破坏导致胶原蛋白结构紊乱，损害角质层完整性和宿主抵抗力。
- Keywords: collagen, lysosomal, neuronal, nsif-1, function

### 13. [肌动蛋白调节机制的不对称遗传塑造了早期秀丽隐杆线虫胚胎发生过程中的细胞骨架异质性](https://www.biorxiv.org/content/10.64898/2026.03.22.713200v3)
- Original title: Asymmetric inheritance of actin regulatory machinery shapes cytoskeletal heterogeneity during early Caenorhabditis elegans embryogenesis
- Authors: Mathonnet, G., Benoit, R., Sunher, D., Arbogast, N., Guiot, E. et al.
- Meta: 2026-07-13 | developmental biology | DOI: 10.64898/2026.03.22.713200
- 中文摘要: 每个胚胎都经历着巨大的挑战，才能成功地将负载亲本物质的被动卵母细胞转化为分化卵裂球的极化胚胎。秀丽隐杆线虫的分化是在一个细胞阶段通过细胞极化、不对称或对称分裂的组合启动的。模式尤其是通过每次细胞分裂时发生的分子分离的调节而出现，包括极性蛋白、细胞命运决定因素、转录因子或 mRNA。肌动球蛋白细胞骨架被证明在这些早期分化事件中发挥着至关重要的作用。然而，与其他分子内容相比，肌动蛋白本身如何从第一次不对称分裂开始分离仍然知之甚少。
- Abstract: Each embryo experiences enormous challenges to successfully transform a passive oocyte loaded with parental material into a polarized embryo of differentiated blastomeres. In Caenorhabditis elegans differentiation is initiated at the one cell stage via a combination of cell polarisation, asymmetric or symmetric divisions. Patterns notably emerge via regulated segregation of molecules occurring at each cell division,...
- Summary (fallback): 机器翻译摘要显示：每个胚胎都经历着巨大的挑战，才能成功地将负载亲本物质的被动卵母细胞转化为分化卵裂球的极化胚胎。秀丽隐杆线虫的分化是在一个细胞阶段通过细胞极化、不对称或对称分裂的组合启动的。模式尤其是通过每次细胞分裂时发生的分子分离的调节而出现，包括极性蛋白、细胞命运决定因素、转录因子或 mRNA。肌动球蛋白细胞骨架被证明在这些早期分化事件中发挥着至关重要的作用。然而，与其他分子内容相比，肌动蛋白本身如何从第一次不对称分裂开始分离仍然知之甚少。
- Keywords: cell, actin, asymmetric, early, polymerisation

### 14. [体外受精过程中的超低氧张力可改善小鼠的胚胎和成年结局](https://www.biorxiv.org/content/10.64898/2026.07.10.737757v1)
- Original title: Ultra-low oxygen tension during in vitro fertilization improves embryonic and adult outcomes in mice
- Authors: Hemphill, C. N., Rhon-Calderon, E. A., Savage, A. J., Domingo-Muelas, A., Krapp, C. J. et al.
- Meta: 2026-07-13 | developmental biology | DOI: 10.64898/2026.07.10.737757
- 中文摘要: 胚胎培养是体外受精 (IVF) 过程中的必要步骤，它使发育中的胚胎暴露于体内通常不会经历的改变的环境条件，包括改变的氧 (O2) 张力。重要的是，氧气影响基因表达、新陈代谢和塑造表观遗传景观的酶的活性。尽管有证据表明哺乳动物雌性生殖道部分的 O2 水平低至 2%，但目前诊所在胚胎培养过程中使用的最低 O2 张力为 5%。因此，较低的 O2 可能会更好地模拟体内环境，从而改善 IVF 受孕后代的产前和产后结果。
- Abstract: Embryo culture, a required step during in vitro fertilization (IVF), exposes developing embryos to altered environmental conditions not normally experienced in vivo, including altered oxygen (O2) tension. Importantly, O2 influences gene expression, metabolism, and the activity of enzymes that sculpt the epigenetic landscape. The lowest O2 tension currently used in clinics during embryo culture is 5%, despite evidenc...
- Summary (fallback): 机器翻译摘要显示：胚胎培养是体外受精 (IVF) 过程中的必要步骤，它使发育中的胚胎暴露于体内通常不会经历的改变的环境条件，包括改变的氧 (O2) 张力。重要的是，氧气影响基因表达、新陈代谢和塑造表观遗传景观的酶的活性。尽管有证据表明哺乳动物雌性生殖道部分的 O2 水平低至 2%，但目前诊所在胚胎培养过程中使用的最低 O2 张力为 5%。因此，较低的 O2 可能会更好地模拟体内环境，从而改善 IVF 受孕后代的产前和产后结果。
- Keywords: culture, embryo, during, tension, outcomes

### 15. [Faf2 是胚胎神经祖细胞神经分化所必需的](https://www.biorxiv.org/content/10.64898/2026.07.12.737973v1)
- Original title: Faf2 is required for neural differentiation in embryonic neural progenitor cells
- Authors: Kakebeen, A. D., Dunphy, L., Hazen, H. K., Niswander, L. A.
- Meta: 2026-07-13 | developmental biology | DOI: 10.64898/2026.07.12.737973
- 中文摘要: 神经祖细胞分化是一个复杂的过程，需要指导性因素和许可性因素的适当整合。在这方面，包括信号分子和转录因子网络在内的指导性线索已得到充分研究，但细胞稳态等许可因素尚未得到充分研究。细胞稳态对于支持细胞的健康和稳定并使细胞能够根据指导性分化线索发挥作用至关重要。我们的研究调查了一种稳态蛋白 FAF2 及其在神经祖细胞中的功能。 FAF2 是一种接头蛋白，参与内质网 (ER) 相关降解，以去除错误折叠的蛋白并恢复 ER 稳态。在这里，我们表明敲除神经祖细胞中的 FAF2 会导致蛋白质和转录水平上的 ER 应激特征增加，这表明神经祖细胞中具有保守的功能作用。
- Abstract: Neural progenitor cell differentiation is a complex process requiring the proper integration of instructive and permissive factors. Instructive cues including signaling molecules and transcription factor networks have been well studied in this context, but permissive factors such as cell homeostasis have not. Cell homeostasis is critical to support the health and stability of a cell and enable the cell to act on ins...
- Summary (fallback): 机器翻译摘要显示：神经祖细胞分化是一个复杂的过程，需要指导性因素和许可性因素的适当整合。在这方面，包括信号分子和转录因子网络在内的指导性线索已得到充分研究，但细胞稳态等许可因素尚未得到充分研究。细胞稳态对于支持细胞的健康和稳定并使细胞能够根据指导性分化线索发挥作用至关重要。我们的研究调查了一种稳态蛋白 FAF2 及其在神经祖细胞中的功能。 FAF2 是一种接头蛋白，参与内质网 (ER) 相关降解，以去除错误折叠的蛋白并恢复 ER 稳态。在这里，我们表明敲除神经祖细胞中的 FAF2 会导致蛋白质和转录水平上的 ER 应激特征增加，这表明神经祖细胞中具有保守的功能作用。
- Keywords: neural, differentiation, faf2, cells, progenitor

### 16. [巨藻岩藻依聚糖可以激活生物碳泵](https://www.biorxiv.org/content/10.64898/2026.07.10.737761v1)
- Original title: Macroalgal fucoidan can activate the biological carbon pump
- Authors: Hellige, I., Buck-Wiese, H., Bligh, M., Thomson, T., White, L. et al.
- Meta: 2026-07-13 | ecology | DOI: 10.64898/2026.07.10.737761
- 中文摘要: 大型藻类分泌复杂的碳水化合物聚合物，即它们的细胞外基质，作为防止微生物降解的保护措施。通过抵抗分解，这些碳水化合物可以促进海洋碳固存，尽管其机制、程度和时间尺度仍然未知。通过船上采样和实验，我们发现棕色大型藻类以岩藻依聚糖的形式释放 1.7-4.2% 的固碳量，相当于每天每克干海藻组织释放 0.32-0.88 毫克岩藻依聚糖。根据我们的经验数据训练的贝叶斯模型，加上蒙特卡罗模拟表明，全球每年释放 13-37 兆吨岩藻依聚糖碳。此外，抗降解性与表面活性相结合，使岩藻依聚糖能够充当胶水，将包括微生物和蛋白质在内的异源有机碳交联成海洋雪。
- Abstract: Macroalgae secrete complex carbohydrate polymers, their extracellular matrix, as protection against microbial degradation. By resisting breakdown, these carbohydrates can contribute to marine carbon sequestration, though mechanisms, extent, and timescales remain unknown. Using ship-based sampling and experiments, we found that brown macroalgae release 1.7-4.2% of carbon fixation as fucoidan, equivalent to 0.32-0.88...
- Summary (fallback): 机器翻译摘要显示：大型藻类分泌复杂的碳水化合物聚合物，即它们的细胞外基质，作为防止微生物降解的保护措施。通过抵抗分解，这些碳水化合物可以促进海洋碳固存，尽管其机制、程度和时间尺度仍然未知。通过船上采样和实验，我们发现棕色大型藻类以岩藻依聚糖的形式释放 1.7-4.2% 的固碳量，相当于每天每克干海藻组织释放 0.32-0.88 毫克岩藻依聚糖。根据我们的经验数据训练的贝叶斯模型，加上蒙特卡罗模拟表明，全球每年释放 13-37 兆吨岩藻依聚糖碳。此外，抗降解性与表面活性相结合，使岩藻依聚糖能够充当胶水，将包括微生物和蛋白质在内的异源有机碳交联成海洋雪。
- Keywords: fucoidan, carbon, marine, macroalgal, macroalgae

### 17. [使用 BONCAT-FACS 探测一氧化二氮生产过程中活跃的土壤微生物群落](https://www.biorxiv.org/content/10.64898/2026.07.10.737762v1)
- Original title: Using BONCAT-FACS to probe the active soil microbial community during nitrous oxide production
- Authors: Gray, J., Harris, J. E., Kaye, J. P., Couradeau, E.
- Meta: 2026-07-13 | ecology | DOI: 10.64898/2026.07.10.737762
- 中文摘要: 一氧化二氮 (N2O) 是一种强效温室气体，主要是由不完全反硝化作用产生的。尽管我们知道许多反硝化微生物物种，但我们仍然无法可靠地预测土壤中 N2O 的产生量。微生物生态学的最新研究表明，当关键微生物被视为功能整体的成员而不是孤立的时，将其活动与突现特性联系起来的预测能力会急剧增加。我们假设，高 N2O 产生期间的活跃微生物群落在分类学上与非活跃部分不同，并且 N2O 生产率的增加与多个活性类群丰度增加的相关性比与单一活性物种的优势相关性更强。
- Abstract: Nitrous oxide (N2O) is a potent greenhouse gas and is largely produced by incomplete denitrification. Although we know many of the microbial species that denitrify, we are still unable to reliably predict N2O production from soils. Recent work in microbial ecology has shown that when key microbes are considered as members of functional ensembles rather than isolated, the predictive power linking their activity to em...
- Summary (fallback): 机器翻译摘要显示：一氧化二氮 (N2O) 是一种强效温室气体，主要是由不完全反硝化作用产生的。尽管我们知道许多反硝化微生物物种，但我们仍然无法可靠地预测土壤中 N2O 的产生量。微生物生态学的最新研究表明，当关键微生物被视为功能整体的成员而不是孤立的时，将其活动与突现特性联系起来的预测能力会急剧增加。我们假设，高 N2O 产生期间的活跃微生物群落在分类学上与非活跃部分不同，并且 N2O 生产率的增加与多个活性类群丰度增加的相关性比与单一活性物种的优势相关性更强。
- Keywords: active, microbial, community, production, rates

### 18. [冰桶挑战：研究实验室微观世界中的冰藻生理学。](https://www.biorxiv.org/content/10.64898/2026.07.10.737583v1)
- Original title: An ice-bucket challenge: investigating ice algae physiology in laboratory microcosms.
- Authors: Baker, M. L., Forss, E., Kolzenburg, R., Collins, S., Kranz, S. A.
- Meta: 2026-07-13 | ecology | DOI: 10.64898/2026.07.10.737583
- 中文摘要: 约翰·雷文 (John Raven) 开创了藻类生态生理学领域，增进了我们对细胞资源经济学、碳获取和能量分配的理解。他的工作为研究综合生理学奠定了基础，将不同环境中的生长与生存权衡联系起来。海冰栖息地为继续约翰倡导的研究提供了一个极好的框架。由于温度-盐度梯度陡峭，藻类的生存需要生理学的转变，而我们才刚刚开始了解这一点。我们开发了两个小规模、可重复的冰世界，以研究与海冰合并相关的生理变化以及融化后的生存潜力。
- Abstract: John Raven pioneered the field of algae ecophysiology, advancing our understanding of cellular resource economics, carbon acquisition, and energy allocation. His work laid the foundation for investigating integrative physiology, linking growth-survival trade-offs across diverse environments. The sea ice habitat provides an excellent framework to continue the research John championed. With steep temperature-salinity...
- Summary (fallback): 机器翻译摘要显示：约翰·雷文 (John Raven) 开创了藻类生态生理学领域，增进了我们对细胞资源经济学、碳获取和能量分配的理解。他的工作为研究综合生理学奠定了基础，将不同环境中的生长与生存权衡联系起来。海冰栖息地为继续约翰倡导的研究提供了一个极好的框架。由于温度-盐度梯度陡峭，藻类的生存需要生理学的转变，而我们才刚刚开始了解这一点。我们开发了两个小规模、可重复的冰世界，以研究与海冰合并相关的生理变化以及融化后的生存潜力。
- Keywords: algae, physiology, survival, cylindrus, frigida

### 19. [人口学如何塑造有或没有重组的连锁不平衡](https://www.biorxiv.org/content/10.1101/2023.12.13.571342v2)
- Original title: How demography shapes linkage disequilibrium with or without recombination
- Authors: Kerdoncuff, E., Ianni-Ravn, M. K., Roze, D., Novembre, J., Lambert, A. et al.
- Meta: 2026-07-13 | evolutionary biology | DOI: 10.1101/2023.12.13.571342
- 中文摘要: 连锁不平衡 (LD) 是群体内不同基因座等位基因之间统计关联的衡量标准。在这里，我们通过模拟和分析结果，对不同人口统计场景中的 LD 统计数据进行了详细的表征，重点关注了几种广泛使用的 LD 度量（D、|D'| 和 r2），并引入了第四类统计数据：2 位点配置概率，其对应于不同等位基因关联模式的频率。通过研究无重组、单个重组事件以及完全独立基因座之间的这些测量，我们能够获得关于这些测量在重组尺度上如何变化的新见解。我们还将重组事件分为四种类型，并根据它们各自的频率和对 LD 测量的影响对它们进行排序。
- Abstract: Linkage Disequilibrium (LD) is a measure of the statistical association, within a population, between alleles present at different loci. Here, we produce detailed characterizations of LD statistics in different demographic scenarios, with simulations and with analytic results, focusing on several widely used measures of LD (D, |D'|, and r2), and introducing a fourth class of statistics: 2-site configuration probabil...
- Summary (fallback): 机器翻译摘要显示：连锁不平衡 (LD) 是群体内不同基因座等位基因之间统计关联的衡量标准。在这里，我们通过模拟和分析结果，对不同人口统计场景中的 LD 统计数据进行了详细的表征，重点关注了几种广泛使用的 LD 度量（D、|D'| 和 r2），并引入了第四类统计数据：2 位点配置概率，其对应于不同等位基因关联模式的频率。通过研究无重组、单个重组事件以及完全独立基因座之间的这些测量，我们能够获得关于这些测量在重组尺度上如何变化的新见解。我们还将重组事件分为四种类型，并根据它们各自的频率和对 LD 测量的影响对它们进行排序。
- Keywords: recombination, measures, different, statistics, linkage

### 20. [从生物膜到出生：以水合聚合物为中心的生物转导、连贯性和复杂生命进化的定量默本原理](https://www.biorxiv.org/content/10.64898/2026.07.10.737745v1)
- Original title: From biofilms to birth: Quantitative murburn rationale for hydrated polymer-centred biological transduction, coherence, and evolution of complex life
- Authors: Manoj, K. M., Jaeken, L., Tamagawa, H., Burra, V. L. S. P.
- Meta: 2026-07-13 | biochemistry | DOI: 10.64898/2026.07.10.737745
- 中文摘要: 水合细胞外聚合物相（例如粘液、生物膜和细胞外基质）传统上被视为被动屏障。我们通过默本框架和液-液相分离（LLPS）生物物理学分析这些系统来补充和扩展这一观点。使用定量模型，我们首先证明了两栖动物卵团中的泡沫粘液如何增强氧气输送，同时缓冲可扩散反应物质（DRS），从而改善发育同步性。然后，我们对人类宫颈粘液系统进行建模，显示其在相干屏障（怀孕）、主动转导介质（排卵）和受控炎症重塑（分娩）之间的周期依赖性转变。
- Abstract: Hydrated extracellular polymeric phases (such as mucus, biofilms, and extracellular matrices) have traditionally been viewed as passive barriers. We complement and extend this view by analysing these systems through the murburn framework and liquid-liquid phase separation (LLPS) biophysics. Using quantitative modeling, we first demonstrate how frothy mucus in amphibian egg-masses enhances oxygen delivery while buffe...
- Summary (fallback): 机器翻译摘要显示：水合细胞外聚合物相（例如粘液、生物膜和细胞外基质）传统上被视为被动屏障。我们通过默本框架和液-液相分离（LLPS）生物物理学分析这些系统来补充和扩展这一观点。使用定量模型，我们首先证明了两栖动物卵团中的泡沫粘液如何增强氧气输送，同时缓冲可扩散反应物质（DRS），从而改善发育同步性。然后，我们对人类宫颈粘液系统进行建模，显示其在相干屏障（怀孕）、主动转导介质（排卵）和受控炎症重塑（分娩）之间的周期依赖性转变。
- Keywords: mucus, biofilms, murburn, hydrated, birth

### 21. [高尔基：一个开源图形平台，用于周围神经刺激的图像募集建模](https://www.biorxiv.org/content/10.64898/2026.07.10.737529v1)
- Original title: golgi: an open-source graphical platform for image-to-recruitment modeling of peripheral nerve stimulation
- Authors: Lung, D., Jia, Y., Blumer, R., Reissig, L., Zopf, L. M. et al.
- Meta: 2026-07-13 | bioengineering | DOI: 10.64898/2026.07.10.737529
- 中文摘要: 周围神经刺激的计算模型（将有限元生物电场与生物物理轴突模型耦合）已成为设计神经调节疗法的电极和波形的关键。然而，现有的开放工具都是代码优先的，并且需要大量的建模专业知识，其中一些工具依赖于商业有限元求解器，这使得许多实验学家和临床医生无法进行真实的神经建模。我们推出了高尔基（golgi），这是一个开源平台，它通过单个图形界面将周围神经从图像中提取到受刺激的纤维群，并具有等效的可编写脚本的 Python API 和用于批量研究的命令行界面。
- Abstract: Computational models of peripheral nerve stimulation-coupling finite-element bioelectric fields to biophysical axon models-have become essential for designing electrodes and waveforms for neuromodulation therapies. Yet the established open tools are code-first and assume substantial modeling expertise, and several depend on commercial finite-element solvers, placing realistic nerve modeling out of reach for many exp...
- Summary (fallback): 机器翻译摘要显示：周围神经刺激的计算模型（将有限元生物电场与生物物理轴突模型耦合）已成为设计神经调节疗法的电极和波形的关键。然而，现有的开放工具都是代码优先的，并且需要大量的建模专业知识，其中一些工具依赖于商业有限元求解器，这使得许多实验学家和临床医生无法进行真实的神经建模。我们推出了高尔基（golgi），这是一个开源平台，它通过单个图形界面将周围神经从图像中提取到受刺激的纤维群，并具有等效的可编写脚本的 Python API 和用于批量研究的命令行界面。
- Keywords: golgi, nerve, cardiac, fibers, modeling

### 22. [肽添加剂重新编程脂质纳米颗粒冠并增强肺上皮在无血清环境中的基因传递](https://www.biorxiv.org/content/10.64898/2026.07.10.737795v1)
- Original title: Peptide additives reprogram the lipid nanoparticle corona and enhance gene delivery in a serum-free environment for lung epithelium
- Authors: Hu, J., Papah, M. B., Ramirez, A., Alapati, D., Sullivan, M. O.
- Meta: 2026-07-13 | bioengineering | DOI: 10.64898/2026.07.10.737795
- 中文摘要: 脂质纳米颗粒 (LNP) 已成为全身给药的核酸药物和疫苗的临床标准，但用于局部递送 LNP 疗法的 LNP 管道仍然不太成熟。肺部局部递送代表了 DNA-LNP 疗法特别引人注目的应用空间，因为局部基因疗法可以支持各种肺部疾病的持续上皮恢复和功能恢复。然而，局部递送的 DNA-LNP 面临多重障碍，包括通常支持传统 LNP 活性的血清成分的可用性有限，以及细胞核带来的额外递送障碍。
- Abstract: Lipid nanoparticles (LNPs) have become a clinical standard for systemically-administered nucleic acid drugs and vaccines, but the LNP pipeline for locally-delivered LNP therapies remains much less mature. Local delivery in lung represents a particularly compelling application space for DNA-LNP therapeutics, as local gene therapies could support sustained epithelial recovery and functional restoration in various lung...
- Summary (fallback): 机器翻译摘要显示：脂质纳米颗粒 (LNP) 已成为全身给药的核酸药物和疫苗的临床标准，但用于局部递送 LNP 疗法的 LNP 管道仍然不太成熟。肺部局部递送代表了 DNA-LNP 疗法特别引人注目的应用空间，因为局部基因疗法可以支持各种肺部疾病的持续上皮恢复和功能恢复。然而，局部递送的 DNA-LNP 面临多重障碍，包括通常支持传统 LNP 活性的血清成分的可用性有限，以及细胞核带来的额外递送障碍。
- Keywords: serum, delivery, peptide, lung, lnps

### 23. [拓扑网络化蛋白质-MXene 复合材料中的各向异性热导率](https://www.biorxiv.org/content/10.64898/2026.07.10.737764v1)
- Original title: Anisotropic Thermal Conductivity in Topologically Networked Protein-MXene Composites
- Authors: Demirel, M., Hopkins, P., Vural, M., Jung, H., Tomko, J.
- Meta: 2026-07-13 | bioengineering | DOI: 10.64898/2026.07.10.737764
- 中文摘要: 控制工程材料中的热传输创造了重新定向和回收电子和能量转换设备中产生的多余热量的机会。将低跨面热导率与高面内热导率结合起来的材料特别有价值，因为它们可以限制热量并将其引导远离敏感区域，从而防止局部设备故障。二维晶体是此类各向异性热导体的有效构建块，但它们很脆，并且用于增韧它们的聚合物复合材料通常会丧失大部分固有的各向异性：在传统的基于渗流的设计中，填料分数是唯一可用的手柄，它控制面内和跨面传导。
- Abstract: Governing thermal transport in engineered materials creates opportunities to redirect and recover the excess heat generated in electronic and energy-conversion devices. Materials that pair low cross-plane thermal conductivity with high in-plane thermal conductivity are particularly valuable because they confine heat and channel it away from sensitive regions, preventing localized device failure. Two-dimensional crys...
- Summary (fallback): 机器翻译摘要显示：控制工程材料中的热传输创造了重新定向和回收电子和能量转换设备中产生的多余热量的机会。将低跨面热导率与高面内热导率结合起来的材料特别有价值，因为它们可以限制热量并将其引导远离敏感区域，从而防止局部设备故障。二维晶体是此类各向异性热导体的有效构建块，但它们很脆，并且用于增韧它们的聚合物复合材料通常会丧失大部分固有的各向异性：在传统的基于渗流的设计中，填料分数是唯一可用的手柄，它控制面内和跨面传导。
- Keywords: thermal, conductivity, anisotropy, cross-plane, composites

### 24. [组织纳米转染介导的神经源性程序的诱导促进去神经骨骼肌的肌肉保护反应](https://www.biorxiv.org/content/10.64898/2026.07.10.737742v1)
- Original title: Tissue nanotransfection-mediated induction of neurogenic programs promotes myoprotective responses in denervated skeletal muscle
- Authors: Salazar Puerta, A. I., Kheirkhah, S., Moore, J. T., Vasquez Martinez, C. A., Velasquez Quintero, C. et al.
- Meta: 2026-07-13 | bioengineering | DOI: 10.64898/2026.07.10.737742
- 中文摘要: 周围神经损伤通常会导致骨骼肌长期去神经支配，从而导致进行性萎缩、纤维化、神经肌肉不稳定以及轴突重新支配远端目标之前再生能力的丧失。在这里，我们开发了一种使用组织纳米转染 (TNT) 的非病毒策略，将神经源性转录因子混合物 Ascl1、Brn2 和 Myt1l (ABM) 直接递送至去神经骨骼肌。在体外，ABM 转染的成肌细胞持续表达重编程因子，获得神经元样形态，上调包括 Tuj1、Map2 和 Syp 在内的神经元标记，并表现出与膜兴奋性一致的电生理特性。
- Abstract: Peripheral nerve injuries often result in prolonged skeletal muscle denervation, leading to progressive atrophy, fibrosis, neuromuscular instability, and loss of regenerative capacity before axons can reinnervate distal targets. Here, we developed a non-viral strategy using tissue nanotransfection (TNT) to deliver the neurogenic transcription factor cocktail Ascl1, Brn2, and Myt1l (ABM) directly to denervated skelet...
- Summary (fallback): 机器翻译摘要显示：周围神经损伤通常会导致骨骼肌长期去神经支配，从而导致进行性萎缩、纤维化、神经肌肉不稳定以及轴突重新支配远端目标之前再生能力的丧失。在这里，我们开发了一种使用组织纳米转染 (TNT) 的非病毒策略，将神经源性转录因子混合物 Ascl1、Brn2 和 Myt1l (ABM) 直接递送至去神经骨骼肌。在体外，ABM 转染的成肌细胞持续表达重编程因子，获得神经元样形态，上调包括 Tuj1、Map2 和 Syp 在内的神经元标记，并表现出与膜兴奋性一致的电生理特性。
- Keywords: muscle, neurogenic, programs, denervated, skeletal

### 25. [高尔基体：用于自动神经模型生成和招募模拟的开源软件](https://www.biorxiv.org/content/10.64898/2026.07.10.737846v1)
- Original title: golgi: open-source software for automated nerve model generation and recruitment simulation
- Authors: Lung, D., Jia, Y., Moro, A., Fachino, M., Haberbusch, M.
- Meta: 2026-07-13 | bioengineering | DOI: 10.64898/2026.07.10.737846
- 中文摘要: golgi 是一个开源平台，通过单个图形界面将周围神经从图像转化为受刺激的纤维群，并具有等效的可编写脚本的 Python API 和命令行界面，用于批量和高性能使用。它集成了快速图像分割、自动多区域四面体网格划分、具有显式神经束膜接触阻抗的细胞外场的各向异性有限元解、生成真实的纤维群及其三维轨迹，以及通过可互换后端——NEURON（通过 PyFibers）和 GPU 加速代理（AxonML）设置生物物理激活阈值。每项研究都导出为经过完整性哈希处理的包，其图像到招聘的来源都是可逐字节验证的。
- Abstract: golgi is an open-source platform that takes a peripheral nerve from image to stimulated fiber population through a single graphical interface, with an equivalent scriptable Python API and command-line interface for batch and high-performance use. It integrates promptable image segmentation, automated multi-region tetrahedral meshing, anisotropic finite-element solution of the extracellular field with an explicit per...
- Summary (fallback): 机器翻译摘要显示：golgi 是一个开源平台，通过单个图形界面将周围神经从图像转化为受刺激的纤维群，并具有等效的可编写脚本的 Python API 和命令行界面，用于批量和高性能使用。它集成了快速图像分割、自动多区域四面体网格划分、具有显式神经束膜接触阻抗的细胞外场的各向异性有限元解、生成真实的纤维群及其三维轨迹，以及通过可互换后端——NEURON（通过 PyFibers）和 GPU 加速代理（AxonML）设置生物物理激活阈值。每项研究都导出为经过完整性哈希处理的包，其图像到招聘的来源都是可逐字节验证的。
- Keywords: golgi, nerve, open-source, automated, generation

### 26. [静电和局部芳香残基控制突触结合蛋白 C2 结构域的脂质结合和膜渗透](https://www.biorxiv.org/content/10.64898/2026.07.09.737582v1)
- Original title: Electrostatics and Local Aromatic Residues Govern Lipid Binding and Membrane Penetration of Synaptotagmin C2 Domains
- Authors: An, D., Lindau, M.
- Meta: 2026-07-13 | biophysics | DOI: 10.64898/2026.07.09.737582
- 中文摘要: 突触结合蛋白 (Syts) 是 Ca2+ 感应胞吐调节剂，其串联 C2 结构域与磷酸肌醇和细胞膜相互作用，触发神经递质和激素释放。尽管已知 Ca2+ 感应结合可增强 C2 结构域-膜相互作用，但控制脂质结合和跨 Syt 同工型膜渗透的序列决定因素仍不完全清楚。在这里，我们对八种 Ca2+ 传感 Syt 同种型（Syt1、Syt2、Syt3、Syt5、Syt6、Syt7、Syt9 和 Syt10）中分离的 C2A 和 C2B 结构域与含磷脂酰肌醇 4,5-二磷酸 (PIP2) 的质膜相互作用进行了 MARTINI 粗粒度分子动力学模拟。为了系统地调节静电特性，我们在钙结合环（CBL）内的保守酸性残基处引入了部分和全部电荷翻转突变。
- Abstract: Synaptotagmins (Syts) are Ca2+-sensing exocytosis regulators whose tandem C2 domains interact with phosphoinositides and membranes to trigger neurotransmitter and hormone release. Although Ca2+-sensing binding is known to enhance C2 domain-membrane interactions, the sequence determinants governing lipid binding and membrane penetration across Syt isoforms remain incompletely understood. Here, we performed MARTINI co...
- Summary (fallback): 机器翻译摘要显示：突触结合蛋白 (Syts) 是 Ca2+ 感应胞吐调节剂，其串联 C2 结构域与磷酸肌醇和细胞膜相互作用，触发神经递质和激素释放。尽管已知 Ca2+ 感应结合可增强 C2 结构域-膜相互作用，但控制脂质结合和跨 Syt 同工型膜渗透的序列决定因素仍不完全清楚。在这里，我们对八种 Ca2+ 传感 Syt 同种型（Syt1、Syt2、Syt3、Syt5、Syt6、Syt7、Syt9 和 Syt10）中分离的 C2A 和 C2B 结构域与含磷脂酰肌醇 4,5-二磷酸 (PIP2) 的质膜相互作用进行了 MARTINI 粗粒度分子动力学模拟。为了系统地调节静电特性，我们在钙结合环（CBL）内的保守酸性残基处引入了部分和全部电荷翻转突变。
- Keywords: membrane, charge, binding, penetration, loop

### 27. [遗传独特的微环境决定小鼠癌症的存活和对治疗的反应](https://www.biorxiv.org/content/10.64898/2026.07.10.737486v1)
- Original title: Genetically distinct microenvironment determines cancer survival and response to therapy in mice
- Authors: Warner, M. A., Sargent, J. K., Farley, S. R., Dumont, B. L., Hasham, M. G.
- Meta: 2026-07-13 | cancer biology | DOI: 10.64898/2026.07.10.737486
- 中文摘要: 肿瘤微环境的遗传独特性显着影响癌症的生长、存活和对治疗的反应，与癌细胞的内在特性或适应性免疫系统无关。这项研究使用遗传上不同的 Rag1-/- 小鼠模型，表明当异种移植相同的白血病和实体瘤细胞系时，不同品系表现出不同的肿瘤生长动力学和生存结果。这项研究进一步强调了骨髓免疫区室的关键作用，并表明破坏淋巴和骨髓系统可以改变癌症进展。这些结果还表明，肿瘤微环境可以永久性地改变癌细胞表型，并显着影响化疗效果，正如顺铂对不同菌株的不同作用所示。
- Abstract: Genetic uniqueness of the tumor microenvironment significantly influences cancer growth, survival, and response to therapy, independent of the cancer cell's intrinsic properties or the adaptive immune system. Using genetically distinct Rag1-/- mouse models, this study shows that different strains exhibit varied tumor growth kinetics and survival outcomes when xenografted with identical leukemic and solid tumor cell...
- Summary (fallback): 机器翻译摘要显示：肿瘤微环境的遗传独特性显着影响癌症的生长、存活和对治疗的反应，与癌细胞的内在特性或适应性免疫系统无关。这项研究使用遗传上不同的 Rag1-/- 小鼠模型，表明当异种移植相同的白血病和实体瘤细胞系时，不同品系表现出不同的肿瘤生长动力学和生存结果。这项研究进一步强调了骨髓免疫区室的关键作用，并表明破坏淋巴和骨髓系统可以改变癌症进展。这些结果还表明，肿瘤微环境可以永久性地改变癌细胞表型，并显着影响化疗效果，正如顺铂对不同菌株的不同作用所示。
- Keywords: cancer, tumor, microenvironment, survival, cell

### 28. [特异性 F1 ATP 合酶抑制可产生短暂的线粒体应激，选择性靶向急性髓系白血病](https://www.biorxiv.org/content/10.64898/2026.07.10.737821v1)
- Original title: Specific F1 ATP synthase inhibition delivers transient mitochondrial stress for selective targeting of acute myeloid leukemia
- Authors: Villaume, M. T., Ramsey, H. E., Impedovo, V., Davidson, M., Arrate, M. P. et al.
- Meta: 2026-07-13 | cancer biology | DOI: 10.64898/2026.07.10.737821
- 中文摘要: 靶向氧化磷酸化（OXPHOS）代表了急性髓系白血病的一种有吸引力的治疗策略，与正常造血细胞相比，急性髓系白血病表现出对线粒体呼吸的特殊依赖性。然而，利用这一漏洞的临床尝试受到了对健康组织的靶向毒性的限制。在这里，我们全面比较了抑制 AML 中电子传递链不同节点的细胞后果。我们证明，用 EB2023（阿莫西丁 A）选择性抑制 ATP 合酶的 F1 亚基可为 AML 细胞带来能量应激，而不会产生复合物 I 抑制所特有的深度氧化还原应激，从而防止 NAD/NADH 失衡并允许持续的 TCA 循环。
- Abstract: Targeting oxidative phosphorylation (OXPHOS) represents an attractive therapeutic strategy in acute myeloid leukemia, which exhibits exceptional dependence on mitochondrial respiration compared to normal hematopoietic cells. However, clinical attempts to exploit this vulnerability have been limited by on-target toxicity to healthy tissue. Here, we comprehensively compare the cellular consequences of inhibiting disti...
- Summary (fallback): 机器翻译摘要显示：靶向氧化磷酸化（OXPHOS）代表了急性髓系白血病的一种有吸引力的治疗策略，与正常造血细胞相比，急性髓系白血病表现出对线粒体呼吸的特殊依赖性。然而，利用这一漏洞的临床尝试受到了对健康组织的靶向毒性的限制。在这里，我们全面比较了抑制 AML 中电子传递链不同节点的细胞后果。我们证明，用 EB2023（阿莫西丁 A）选择性抑制 ATP 合酶的 F1 亚基可为 AML 细胞带来能量应激，而不会产生复合物 I 抑制所特有的深度氧化还原应激，从而防止 NAD/NADH 失衡并允许持续的 TCA 循环。
- Keywords: inhibition, oxphos, synthase, mitochondrial, stress

### 29. [微生物入侵和免疫抑制导致早期结直肠癌发展中的腺瘤进展](https://www.biorxiv.org/content/10.64898/2026.07.10.737736v1)
- Original title: Microbial Invasion and Immunosuppression Drives Adenoma Progression in Early Colorectal Cancer Development
- Authors: Liang, W., Falk, L., Lucarelli, D., Putze, P., Metwaly, A. et al.
- Meta: 2026-07-13 | cancer biology | DOI: 10.64898/2026.07.10.737736
- 中文摘要: 结直肠癌存在多种遗传倾向，其中最著名的是家族性腺瘤性息肉病 (FAP)，它通常涉及一个 APC 等位基因的种系功能丧失突变。 APC 或相关基因座的第二次打击会导致异常的 Wnt 信号传导，从而触发几乎完全外显的腺瘤形成。然而，即使在具有相同 APC 种系突变的兄弟姐妹中，疾病的发病和严重程度也存在很大差异，这与环境因素有关。新的证据表明肠道微生物组是腺瘤发生和进展的关键调节因子，特别是在早发性结直肠癌中。在这里，我们发现，在 FAP 猪模型中，细菌入侵与中性粒细胞免疫抑制、T 细胞排斥和腺瘤进展相关。
- Abstract: Several inherited predispositions to colorectal cancer exist, most notably familial adenomatous polyposis (FAP), which typically involves a germline loss-of-function mutation in one APC allele. A second hit in APC or related loci leads to aberrant Wnt signalling, triggering adenoma formation with near-complete penetrance. Yet, substantial variability in disease onset and severity, even among siblings with identical...
- Summary (fallback): 机器翻译摘要显示：结直肠癌存在多种遗传倾向，其中最著名的是家族性腺瘤性息肉病 (FAP)，它通常涉及一个 APC 等位基因的种系功能丧失突变。 APC 或相关基因座的第二次打击会导致异常的 Wnt 信号传导，从而触发几乎完全外显的腺瘤形成。然而，即使在具有相同 APC 种系突变的兄弟姐妹中，疾病的发病和严重程度也存在很大差异，这与环境因素有关。新的证据表明肠道微生物组是腺瘤发生和进展的关键调节因子，特别是在早发性结直肠癌中。在这里，我们发现，在 FAP 猪模型中，细菌入侵与中性粒细胞免疫抑制、T 细胞排斥和腺瘤进展相关。
- Keywords: progression, adenoma, microbial, early, colorectal

### 30. [EZH2 协调骨关节炎关节间室的炎症和疼痛相关通路](https://www.biorxiv.org/content/10.1101/2025.01.19.633762v2)
- Original title: EZH2 coordinates inflammatory and pain-associated pathways across joint compartments in osteoarthritis
- Authors: Brochard, S., Vanlaeys, A., Taieb, M., Richard, I., Aury-Landas, J. et al.
- Meta: 2026-07-13 | physiology | DOI: 10.1101/2025.01.19.633762
- 中文摘要: zeste 同源物增强子 2 (EZH2) 是一种负责 H3K27 三甲基化的组蛋白甲基转移酶，已成为骨关节炎 (OA) 的潜在治疗靶点。然而，它对驱动关节退化和疼痛的多细胞机制的贡献仍然知之甚少。在这里，我们研究了药物 EZH2 抑制在疼痛相关的小鼠 OA 模型中的作用，并探讨了其对 OA 相关细胞群的细胞和分子影响。通过关节内注射碘乙酸钠 (MIA)，然后局部施用 EZH2 抑制剂 EPZ-6438，诱导小鼠发生 OA。通过组织学和功能分析评估关节病理学和疼痛相关行为。
- Abstract: Enhancer of zeste homolog 2 (EZH2), a histone methyltransferase responsible for H3K27 trimethylation, has emerged as a potential therapeutic target in osteoarthritis (OA). However, its contribution to the multicellular mechanisms driving joint degeneration and pain remains poorly understood. Here, we investigated the effects of pharmacological EZH2 inhibition in a pain-relevant murine OA model and explored its cellu...
- Summary (fallback): 机器翻译摘要显示：zeste 同源物增强子 2 (EZH2) 是一种负责 H3K27 三甲基化的组蛋白甲基转移酶，已成为骨关节炎 (OA) 的潜在治疗靶点。然而，它对驱动关节退化和疼痛的多细胞机制的贡献仍然知之甚少。在这里，我们研究了药物 EZH2 抑制在疼痛相关的小鼠 OA 模型中的作用，并探讨了其对 OA 相关细胞群的细胞和分子影响。通过关节内注射碘乙酸钠 (MIA)，然后局部施用 EZH2 抑制剂 EPZ-6438，诱导小鼠发生 OA。通过组织学和功能分析评估关节病理学和疼痛相关行为。
- Keywords: ezh2, inflammatory, pathways, joint, pain-associated

## medrxiv

### 1. [微调大型语言模型，用于从非结构化临床记录中检测社交隔离](https://www.medrxiv.org/content/10.64898/2026.07.05.26357334v2)
- Original title: Fine-Tuned Large Language Models for Detecting Social Isolation from Unstructured Clinical Notes
- Authors: Chinthala, L. K., Lemon, C., Shaban-Nejad, A., Farage, G., Davis, R. L. et al.
- Meta: 2026-07-13 | health informatics | DOI: 10.64898/2026.07.05.26357334
- 中文摘要: 目标：通过利用微调的 FLAN-T5-Large、BERT、RoBERTa 和 Gemma-2-2B 模型来识别非结构化临床记录中的社会隔离和社会支持实例。材料和方法：该研究使用包含 2020 年至 2023 年间 326,847 名 50 岁以上成年人的社会背景线索的带注释的临床记录跨度来微调每个模型。使用准确度、精确度、召回率和 Macro-F1 分数来评估性能。使用结构化提示来指示模型执行分类任务并减轻过度概括。模型之间的性能比较评估了敏感性、稳健性和假阳性减少情况。
- Abstract: Objective: To identify instances of social isolation and social support within unstructured clinical notes by leveraging fine-tuned FLAN-T5-Large, BERT, RoBERTa, and Gemma-2-2B models. Materials and Methods: The study used annotated clinical note spans containing social context cues from 326,847 adults aged [&ge;] 50 years between 2020 and 2023 to fine-tune each model. Performance was evaluated using Accuracy, Preci...
- Summary (fallback): 机器翻译摘要显示：目标：通过利用微调的 FLAN-T5-Large、BERT、RoBERTa 和 Gemma-2-2B 模型来识别非结构化临床记录中的社会隔离和社会支持实例。材料和方法：该研究使用包含 2020 年至 2023 年间 326,847 名 50 岁以上成年人的社会背景线索的带注释的临床记录跨度来微调每个模型。使用准确度、精确度、召回率和 Macro-F1 分数来评估性能。使用结构化提示来指示模型执行分类任务并减轻过度概括。模型之间的性能比较评估了敏感性、稳健性和假阳性减少情况。
- Keywords: social, isolation, support, models, clinical
