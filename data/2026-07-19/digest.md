# daily2rxiv Digest - 2026-07-19

共收录 44 篇论文。

## arxiv

### 1. [RoboTTT：机器人策略的上下文扩展](https://arxiv.org/abs/2607.15275v1)
- Original title: RoboTTT: Context Scaling for Robot Policies
- Authors: Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, Yunhao Ge et al.
- Meta: 2026-07-16 | cs.RO
- 中文摘要: 最近的机器人基础模型在单步或短历史视觉运动环境下运行。我们引入了测试时间训练机器人策略 (RoboTTT)，这是一种机器人模型和训练方法，可将视觉运动上下文扩展到 8K 时间步长，比最先进的策略高出三个数量级，并且不会增加推理延迟。在这一上下文长度下，我们解锁了新的机器人功能：从人类视频演示中进行一次性上下文模仿、动态策略改进、对扰动的鲁棒性以及在多阶段、长期任务上的更强性能。我们还首次观察到，随着预训练上下文长度的增加，闭环性能稳步提高。
- Abstract: Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new robot capabilities: one-shot in-context imitation from...
- Summary (fallback): 机器翻译摘要显示：最近的机器人基础模型在单步或短历史视觉运动环境下运行。我们引入了测试时间训练机器人策略 (RoboTTT)，这是一种机器人模型和训练方法，可将视觉运动上下文扩展到 8K 时间步长，比最先进的策略高出三个数量级，并且不会增加推理延迟。在这一上下文长度下，我们解锁了新的机器人功能：从人类视频演示中进行一次性上下文模仿、动态策略改进、对扰动的鲁棒性以及在多阶段、长期任务上的更强性能。我们还首次观察到，随着预训练上下文长度的增加，闭环性能稳步提高。
- Keywords: context, robot, robottt, policies, training

### 2. [MeanFlowNFT：将前向过程强化学习引入平均速度生成器](https://arxiv.org/abs/2607.15273v1)
- Original title: MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators
- Authors: Yushi Huang, Xiangxin Zhou, Jun Zhang, Liefeng Bo, Tianyu Pang
- Meta: 2026-07-16 | cs.CV
- 中文摘要: MeanFlow 生成器通过预测时间间隔内的平均速度来实现快速的几步采样，这使得它们对于高效生成具有吸引力。强化学习 (RL) 已成为将扩散和流动模型与人类偏好和特定任务目标结合起来的强大方法。特别是，DiffusionNFT 提供了一种高效的前向过程 RL 框架，不需要逆向过程轨迹或似然估计。然而，将此类 RL 方法应用于 MeanFlow 的探索仍未充分。 DiffusionNFT 优化瞬时速度，而 MeanFlow 以平均速度采样。为了弥补这一差距，我们引入了 MeanFlowNFT。受到连接平均速度和瞬时速度的 MeanFlow 恒等式的启发，我们构建了诱导瞬时速度预测器。
- Abstract: MeanFlow generators achieve fast few-step sampling by predicting average velocities over time intervals, making them attractive for efficient generation. Reinforcement learning (RL) has become a powerful way to align diffusion and flow models with human preferences and task-specific objectives. In particular, DiffusionNFT offers an efficient forward-process RL framework that does not require reverse-process trajecto...
- Summary (fallback): 机器翻译摘要显示：MeanFlow 生成器通过预测时间间隔内的平均速度来实现快速的几步采样，这使得它们对于高效生成具有吸引力。强化学习 (RL) 已成为将扩散和流动模型与人类偏好和特定任务目标结合起来的强大方法。特别是，DiffusionNFT 提供了一种高效的前向过程 RL 框架，不需要逆向过程轨迹或似然估计。然而，将此类 RL 方法应用于 MeanFlow 的探索仍未充分。 DiffusionNFT 优化瞬时速度，而 MeanFlow 以平均速度采样。为了弥补这一差距，我们引入了 MeanFlowNFT。受到连接平均速度和瞬时速度的 MeanFlow 恒等式的启发，我们构建了诱导瞬时速度预测器。
- Keywords: meanflow, meanflownft, average, velocities, diffusionnft

### 3. [用于动态小说视图合成的在线神经时空记忆](https://arxiv.org/abs/2607.15271v1)
- Original title: Online Neural Space Time Memory for Dynamic Novel View Synthesis
- Authors: Baback Elmieh, Lynn Tsai, Zeman Li, Srinivas Kaza, Tiancheng Sun et al.
- Meta: 2026-07-16 | cs.CV
- 中文摘要: Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes.大量内存更新的计算成本阻碍了实时应用，并可能导致长上下文中的不稳定。鉴于内存更新比内存申请要求更高，并且视频内容很大程度上是冗余的，我们建议将这两个过程的频率解耦。
- Abstract: Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes...
- Summary (fallback): 机器翻译摘要显示：Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints.
- Keywords: memory, updates, online, dynamic, while

### 4. [从区块链活动解码市场情绪：数据驱动的情绪分类器](https://arxiv.org/abs/2607.15258v1)
- Original title: Decoding Market Emotion from Blockchain Activity: A Data-Driven Sentiment Classifier
- Authors: Arthur G. Bubolz, Abreu Quevedo, Giancarlo Lucca, Rafael A. Berri, Eduardo Borges et al.
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 比特币作为一种去中心化数字资产和投资工具的使用日益广泛，引发了人们对了解其市场行为的强烈兴趣。这项研究提出了一种通过将链上和财务数据与社交媒体帖子相结合来分析比特币市场情绪的新方法。与旨在预测价格的模型不同，这项工作的重点是使用区块链交易、比特币的历史价格数据和每日 Twitter 情绪分类来解释市场情绪。该方法将情绪趋势与链上和财务指标合并，标准化为数据集以进行详细的市场分析。使用交叉验证对多个机器学习模型进行了测试，梯度提升 (XGBoost) 成为情感分类最可靠的模型，平均 F1 分数约为 0.84。
- Abstract: The growing use of Bitcoin as a decentralized digital asset and investment tool has sparked strong interest in understanding its market behavior. This study presents a new approach to analyze Bitcoin market sentiment by combining on-chain and financial data with social media posts. Unlike models that aim to predict prices, this work focuses on explaining market sentiment using blockchain transactions, historical pri...
- Summary (fallback): 机器翻译摘要显示：比特币作为一种去中心化数字资产和投资工具的使用日益广泛，引发了人们对了解其市场行为的强烈兴趣。这项研究提出了一种通过将链上和财务数据与社交媒体帖子相结合来分析比特币市场情绪的新方法。与旨在预测价格的模型不同，这项工作的重点是使用区块链交易、比特币的历史价格数据和每日 Twitter 情绪分类来解释市场情绪。该方法将情绪趋势与链上和财务指标合并，标准化为数据集以进行详细的市场分析。使用交叉验证对多个机器学习模型进行了测试，梯度提升 (XGBoost) 成为情感分类最可靠的模型，平均 F1 分数约为 0.84。
- Keywords: sentiment, market, bitcoin, on-chain, model

### 5. [用于免重新训练推荐的可变低阶草图](https://arxiv.org/abs/2607.15242v1)
- Original title: Mutable Low-Rank Sketches for Retrain-Free Recommendation
- Authors: Hector J. Garcia, Nick Clayton
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 两阶段推荐的一个常见瓶颈是嵌入过时：当用户对新项目进行评分时，其嵌入保持固定，直到下一个重新训练周期。我们提出了可变草图，它将每个用户的偏好存储在 KP 树（具有求和聚合的稀疏线段树）中，拟合一次低秩投影，并在评分到达时即时重新计算嵌入。我们证明，每个新的观察结果都会单调收紧预测误差包络线（定理 1），这是 FunkSVD 和 eALS 所缺乏的保证。在 KuaiRec 上，可变草图在 1.8% 数据读取时达到 0.810 RMSE，而 ALS 在 100% 时达到 0.822，每批更新速度提高 8 倍。新用户在首次评分后不到 1 毫秒内就会收到个性化推荐，无需重新训练模型。
- Abstract: A common bottleneck in two-stage recommendation is embedding staleness: when a user rates a new item, their embedding remains fixed until the next retrain cycle. We propose mutable sketches, which store each user's preferences in a KP-tree (a sparse segment tree with sum aggregation), fit a low-rank projection once, and recompute embeddings on-the-fly as ratings arrive. We prove that each new observation monotonical...
- Summary (fallback): 机器翻译摘要显示：两阶段推荐的一个常见瓶颈是嵌入过时：当用户对新项目进行评分时，其嵌入保持固定，直到下一个重新训练周期。我们提出了可变草图，它将每个用户的偏好存储在 KP 树（具有求和聚合的稀疏线段树）中，拟合一次低秩投影，并在评分到达时即时重新计算嵌入。我们证明，每个新的观察结果都会单调收紧预测误差包络线（定理 1），这是 FunkSVD 和 eALS 所缺乏的保证。在 KuaiRec 上，可变草图在 1.8% 数据读取时达到 0.810 RMSE，而 ALS 在 100% 时达到 0.822，每批更新速度提高 8 倍。新用户在首次评分后不到 1 毫秒内就会收到个性化推荐，无需重新训练模型。
- Keywords: mutable, user, sampling, low-rank, sketches

### 6. [超越排行榜：值得信赖的多模式 VQA 设计课程](https://arxiv.org/abs/2607.15241v1)
- Original title: Beyond the Leaderboard: Design Lessons for Trustworthy Multimodal VQA
- Authors: Sushant Gautam, Vajira Thambawita, Michael A. Riegler, Pål Halvorsen, Steven A. Hicks
- Meta: 2026-07-16 | cs.CL
- 中文摘要: 医疗保健多模式人工智能必须结合视觉和文本证据，同时保持可靠和可解释。我们使用 MediaEval Medico 2025 作为回顾性胃肠道内窥镜检查案例研究，分析了九个记录系统的设计选择，以提高问答和解释质量。预训练主干的参数高效适应提供了强大的挑战性能，但答案级别的收益并不能始终转化为忠实和完整的临床推理。尽管证据是相关的而不是基于消融的，但强制结构化推理和显式基础的方法在异构问题类型中显示出更可靠的行为。这些结果激励评估超越词汇重叠、标准化证据相关解释、泄漏感知数据治理以及轻量级鲁棒性和校准检查。
- Abstract: Healthcare multimodal AI must combine visual and textual evidence while remaining reliable and interpretable. Using MediaEval Medico 2025 as a retrospective GI endoscopy case study, we analyze design choices across nine documented systems for question answering and explanation quality. Parameter-efficient adaptation of pretrained backbones provides strong challenge performance, but answer-level gains do not consiste...
- Summary (fallback): 机器翻译摘要显示：医疗保健多模式人工智能必须结合视觉和文本证据，同时保持可靠和可解释。我们使用 MediaEval Medico 2025 作为回顾性胃肠道内窥镜检查案例研究，分析了九个记录系统的设计选择，以提高问答和解释质量。预训练主干的参数高效适应提供了强大的挑战性能，但答案级别的收益并不能始终转化为忠实和完整的临床推理。尽管证据是相关的而不是基于消融的，但强制结构化推理和显式基础的方法在异构问题类型中显示出更可靠的行为。这些结果激励评估超越词汇重叠、标准化证据相关解释、泄漏感知数据治理以及轻量级鲁棒性和校准检查。
- Keywords: multimodal, beyond, design, trustworthy, healthcare

### 7. [针对预训练 LLM 的就地分词器扩展](https://arxiv.org/abs/2607.15232v1)
- Original title: In-Place Tokenizer Expansion for Pre-trained LLMs
- Authors: Jimmy T. H. Smith, Tarek Dakhran, Alberto Cabrera, Simon S. Lee, Paul Pak et al.
- Meta: 2026-07-16 | cs.CL
- 中文摘要: 在预训练开始时固定的分词器会根据预训练语料库的比例分配词汇，反映当时的部署优先级。当这些优先级发生变化时，后来添加的语言会被分成每个单词更多的标记，这可能会增加这些语言用户的延迟、计算和能源消耗。云模型可以提供广泛的词汇量，因为嵌入和 LM-head 矩阵只是其参数的一小部分。在紧凑模型上，这些矩阵占每个令牌解码带宽的重要份额，因此设备上模型提供较小的词汇表并接受固定语言集之外的碎片。我们提出了分词器扩展，这是一种在模型生产者控制其设计时升级预训练模型的分词器的就地方法。
- Abstract: A tokenizer fixed at the start of pre-training allocates vocabulary in proportion to the pre-training corpus, reflecting the deployment priorities at that time. When those priorities shift, languages added later are split into many more tokens per word, which can raise latency, compute, and energy consumption for users of those languages. Cloud models can afford a broad vocabulary because the embedding and LM-head m...
- Summary (fallback): 机器翻译摘要显示：在预训练开始时固定的分词器会根据预训练语料库的比例分配词汇，反映当时的部署优先级。当这些优先级发生变化时，后来添加的语言会被分成每个单词更多的标记，这可能会增加这些语言用户的延迟、计算和能源消耗。云模型可以提供广泛的词汇量，因为嵌入和 LM-head 矩阵只是其参数的一小部分。在紧凑模型上，这些矩阵占每个令牌解码带宽的重要份额，因此设备上模型提供较小的词汇表并接受固定语言集之外的碎片。我们提出了分词器扩展，这是一种在模型生产者控制其设计时升级预训练模型的分词器的就地方法。
- Keywords: tokenizer, tokens, model, source, times

### 8. [CRISP：通过迭代压缩过程进行约束细化，以实现域转移下的鲁棒医学图像分割](https://arxiv.org/abs/2607.15231v1)
- Original title: CRISP: Constrained Refinement via Iterative Squeezing Process for Robust Medical Image Segmentation under Domain Shift
- Authors: Yizhou Fang, Pujin Cheng, Yixiang Liu, Xiaoying Tang, Longxi Zhou
- Meta: 2026-07-16 | cs.CV
- 中文摘要: 医学影像的分布变化仍然是医学人工智能临床转化的核心瓶颈。如果不解决这个问题，可能会导致在看不见的环境中性能严重下降，并加剧健康不平等。现有的域适应方法本质上受到通过模拟移位或伪监督耗尽预定义可能性的限制。此类策略在开放且不可预测的现实世界中举步维艰，而现实世界中的分配变化实际上是无限的。为了应对这一挑战，我们采用“正区域的排名稳定性”作为分布变化下的工作假设，并用它来导出用于纯源分割的稳健空间提示。
- Abstract: Distribution shift in medical imaging remains a central bottleneck for the clinical translation of medical AI. Failure to address it can lead to severe performance degradation in unseen environments and exacerbate health inequities. Existing methods for domain adaptation are inherently limited by exhausting predefined possibilities through simulated shifts or pseudo-supervision. Such strategies struggle in the open-...
- Summary (fallback): 机器翻译摘要显示：医学影像的分布变化仍然是医学人工智能临床转化的核心瓶颈。如果不解决这个问题，可能会导致在看不见的环境中性能严重下降，并加剧健康不平等。现有的域适应方法本质上受到通过模拟移位或伪监督耗尽预定义可能性的限制。此类策略在开放且不可预测的现实世界中举步维艰，而现实世界中的分配变化实际上是无限的。为了应对这一挑战，我们采用“正区域的排名稳定性”作为分布变化下的工作假设，并用它来导出用于纯源分割的稳健空间提示。
- Keywords: under, crisp, segmentation, shift, distribution

### 9. [数据驱动的块替换调度](https://arxiv.org/abs/2607.15229v1)
- Original title: Data Driven Block Replacement Scheduling
- Authors: Aniruddhan Ganesaraman, VIdyadhar Kulkarni
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 我们开发了数据驱动算法，用于在\textit{块替换策略}下维护$N$个独立的相同机器，其中每台机器在发生故障时被替换，并且所有机器以长度$k$的定期间隔联合替换。目标是在寿命分布未知时从操作数据中了解成本最小化区间 $k^*$。在每个决策时期，操作员选择 $k \in \{1, 2, \ldots, K\}$，观察由此产生的故障历史记录（完整生命周期和右删失生命周期的混合），并产生由更新函数控制的单位时间成本。我们将其表述为随机多臂老虎机，并提出基于 Hoeffding 和 Bernstein 的置信下限算法，实现 $O(K \log T)$ 遗憾，与 Lai--Robbins 下限相匹配。
- Abstract: We develop data-driven algorithms for maintaining $N$ independent identical machines under a \textit{block replacement policy}, in which each machine is replaced upon failure and all machines are jointly replaced at regular intervals of length $k$. The goal is to learn the cost-minimizing interval $k^*$ from operational data when the lifetime distribution is unknown. At each decision epoch, the operator selects $k \...
- Summary (fallback): 机器翻译摘要显示：我们开发了数据驱动算法，用于在\textit{块替换策略}下维护$N$个独立的相同机器，其中每台机器在发生故障时被替换，并且所有机器以长度$k$的定期间隔联合替换。目标是在寿命分布未知时从操作数据中了解成本最小化区间 $k^*$。在每个决策时期，操作员选择 $k \in \{1, 2, \ldots, K\}$，观察由此产生的故障历史记录（完整生命周期和右删失生命周期的混合），并产生由更新函数控制的单位时间成本。我们将其表述为随机多臂老虎机，并提出基于 Hoeffding 和 Bernstein 的置信下限算法，实现 $O(K \log T)$ 遗憾，与 Lai--Robbins 下限相匹配。
- Keywords: block, replacement, policy, failure, lifetime

### 10. [NeuronSoup：无需反向传播即可演化异步、共享神经元时间图](https://arxiv.org/abs/2607.15217v1)
- Original title: NeuronSoup: Evolving Asynchronous, Shared-Neuron Temporal Graphs without Backpropagation
- Authors: Subodh Kalia
- Meta: 2026-07-16 | cs.NE
- 中文摘要: 我们提出了 NeuronSoup，一种神经计算架构，它用通过共享神经元池的异步、延迟介导的信号传播来取代同步的逐层处理。网络中的每条路径通过可变数量的中间隐藏神经元将连续值信号从一个输入神经元路由到一个输出神经元。隐藏神经元在物理上跨路径共享：当两条路径经过同一神经元时，第二个到达的神经元遇到第一个神经元留下的累积状态，产生建设性或破坏性干扰，具体取决于信号极性和到达时间。整个架构——拓扑、权重、延迟和连接——是由在 14,602 个基因的平坦实值基因组上运行的遗传算法共同进化的。
- Abstract: We present NeuronSoup, a neural computation architecture that replaces synchronous layer-by-layer processing with asynchronous, delay-mediated signal propagation through a pool of shared neurons. Each path in the network routes a continuous-valued signal from one input neuron to one output neuron through a variable number of intermediate hidden neurons. Hidden neurons are physically shared across paths: when two pat...
- Summary (fallback): 机器翻译摘要显示：我们提出了 NeuronSoup，一种神经计算架构，它用通过共享神经元池的异步、延迟介导的信号传播来取代同步的逐层处理。网络中的每条路径通过可变数量的中间隐藏神经元将连续值信号从一个输入神经元路由到一个输出神经元。隐藏神经元在物理上跨路径共享：当两条路径经过同一神经元时，第二个到达的神经元遇到第一个神经元留下的累积状态，产生建设性或破坏性干扰，具体取决于信号极性和到达时间。整个架构——拓扑、权重、延迟和连接——是由在 14,602 个基因的平坦实值基因组上运行的遗传算法共同进化的。
- Keywords: paths, architecture, through, neurons, neuron

### 11. [未调整哈密顿量蒙特卡罗和欠阻尼朗之万的偏差离域](https://arxiv.org/abs/2607.15208v1)
- Original title: Delocalization of bias in unadjusted Hamiltonian Monte Carlo and underdamped Langevin
- Authors: Yifan Chen, Xiaoou Cheng, Jonathan Niles-Weed, Jonathan Weare
- Meta: 2026-07-16 | stat.CO
- 中文摘要: 未经调整的采样器（例如未经调整的哈密顿蒙特卡罗和欠阻尼朗之万）众所周知是有偏差的。 Metropolis-Hastings 调整通常被纳入哈密顿蒙特卡罗以消除偏差。然而，由于合理的 Metropolis 接受率所需的步长较小，这种调整会显着增加迭代复杂度。在这项工作中，我们将先前为过阻尼 Langevin 算法建立的 \emph{偏差离域} 现象扩展到这两种未经调整的算法。我们证明，为了控制高维分布的任何 $K$ 维边缘的 $W_2$ 偏差，假设变量之间的相互作用弱或稀疏，$O(\sqrt{K})$ 积分步骤足以满足 $\log d$ 项。
- Abstract: Unadjusted samplers such as unadjusted Hamiltonian Monte Carlo and underdamped Langevin are well-known to be biased. Metropolis--Hastings adjustment has been conventionally incorporated into Hamiltonian Monte Carlo to eliminate the bias. However, this adjustment can significantly increase the iteration complexity due to the small step size required for reasonable Metropolis acceptance rates. In this work, we extend...
- Summary (fallback): 机器翻译摘要显示：未经调整的采样器（例如未经调整的哈密顿蒙特卡罗和欠阻尼朗之万）众所周知是有偏差的。 Metropolis-Hastings 调整通常被纳入哈密顿蒙特卡罗以消除偏差。然而，由于合理的 Metropolis 接受率所需的步长较小，这种调整会显着增加迭代复杂度。在这项工作中，我们将先前为过阻尼 Langevin 算法建立的 \emph{偏差离域} 现象扩展到这两种未经调整的算法。我们证明，为了控制高维分布的任何 $K$ 维边缘的 $W_2$ 偏差，假设变量之间的相互作用弱或稀疏，$O(\sqrt{K})$ 积分步骤足以满足 $\log d$ 项。
- Keywords: bias, langevin, unadjusted, delocalization, hamiltonian

### 12. [BadWAM：当世界行动模型梦想正确但行动错误时](https://arxiv.org/abs/2607.15207v1)
- Original title: BadWAM: When World-Action Models Dream Right but Act Wrong
- Authors: Qi Li, Xingyi Yang, Xinchao Wang
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 世界行动模型（WAM）正在成为体现控制的有希望的基础：它们不是单独预测行动，而是学习将行动生成与未来世界预测结合起来的表示。这种耦合通常被视为鲁棒性、可解释性和安全性的来源，因为机器人的动作原则上可以根据其想象的未来进行检查。在本文中，我们表明这种假设是脆弱的。我们引入了 BadWAM，这是一个用于建模和评估世界动作漂移攻击的统一框架：一种新型的特定于 WAM 的对抗性攻击，它使用小的视觉扰动来打破 WAM 想象和执行之间的一致性。 BadWAM 按照两个自然标准来描述此攻击面：攻击强度和隐蔽性。
- Abstract: World-action models (WAMs) are emerging as a promising foundation for embodied control: rather than predicting actions alone, they learn representations that couple action generation with future world prediction. This coupling is often viewed as a source of robustness, interpretability, and safety, as a robot's action can in principle be checked against its imagined future. In this paper, we show that this assumptio...
- Summary (fallback): 机器翻译摘要显示：世界行动模型（WAM）正在成为体现控制的有希望的基础：它们不是单独预测行动，而是学习将行动生成与未来世界预测结合起来的表示。这种耦合通常被视为鲁棒性、可解释性和安全性的来源，因为机器人的动作原则上可以根据其想象的未来进行检查。在本文中，我们表明这种假设是脆弱的。我们引入了 BadWAM，这是一个用于建模和评估世界动作漂移攻击的统一框架：一种新型的特定于 WAM 的对抗性攻击，它使用小的视觉扰动来打破 WAM 想象和执行之间的一致性。 BadWAM 按照两个自然标准来描述此攻击面：攻击强度和隐蔽性。
- Keywords: attack, badwam, action, future, attacks

### 13. [用于可解释抑郁症症状注释的自我进化的以人为中心的框架](https://arxiv.org/abs/2607.15202v1)
- Original title: Self-Evolving Human-Centered Framework for Explainable Depression Symptom Annotation
- Authors: Hoang-Loc Cao, Van Pham, Truong Thanh Hung Nguyen, Phuc Truong Loc Nguyen, Phuc Ho et al.
- Meta: 2026-07-16 | cs.AI
- 中文摘要: 注释质量是为心理健康研究构建可靠且可解释的人工智能（XAI）系统的主要瓶颈。在抑郁症相关数据集中，标签的分配通常没有结构化证据、症状水平论证或与《精神疾病诊断和统计手册》第五版文本修订版 (DSM-5-TR) 标准的可追踪一致性，从而限制了透明度和下游模型的可解释性。我们提出了一种针对重度抑郁症（MDD）的自我进化、专家循环注释框架，该框架将大语言模型（LLM）辅助标记与专家验证相结合。该框架旨在支持构建可解释的、符合 DSM-5-TR 的数据集，而不是执行临床诊断。
- Abstract: Annotation quality is a major bottleneck in building reliable and explainable artificial intelligence (XAI) systems for mental health research. In depression-related datasets, labels are often assigned without structured evidence, symptom-level justification, or traceable alignment with the criteria of the Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR), limiting both t...
- Summary (fallback): 机器翻译摘要显示：注释质量是为心理健康研究构建可靠且可解释的人工智能（XAI）系统的主要瓶颈。在抑郁症相关数据集中，标签的分配通常没有结构化证据、症状水平论证或与《精神疾病诊断和统计手册》第五版文本修订版 (DSM-5-TR) 标准的可追踪一致性，从而限制了透明度和下游模型的可解释性。我们提出了一种针对重度抑郁症（MDD）的自我进化、专家循环注释框架，该框架将大语言模型（LLM）辅助标记与专家验证相结合。该框架旨在支持构建可解释的、符合 DSM-5-TR 的数据集，而不是执行临床诊断。
- Keywords: framework, annotation, explainable, evidence, self-evolving

### 14. [扩散语言模型的掩模感知策略梯度](https://arxiv.org/abs/2607.15200v1)
- Original title: Mask-Aware Policy Gradients for Diffusion Language Models
- Authors: Haran Raajesh, Kulin Shah, Adam Klivans, Philipp Krähenbühl
- Meta: 2026-07-16 | cs.CL
- 中文摘要: 强化学习已被证明对于改善大型语言模型的推理是有效的，但由于对数似然估计的棘手性，将其扩展到掩蔽扩散语言模型（MDLM）仍然具有挑战性。现有方法通过仅对标记预测进行建模来近似这种对数似然，忽略生成过程中位置被揭露的顺序。我们观察到 MDLM 的生成在每个步骤都涉及两个决策：在每个屏蔽位置放置什么令牌以及重新屏蔽哪些位置。我们将其形式化为两阶段操作 MDP，表明策略梯度自然分解为标记项和掩蔽项。结合这两个术语的优化，可以在数学推理和编码基准上获得最先进的结果，在 GSM8K 上得分为 87.1%，在 MBPP 上得分为 53.4%。
- Abstract: Reinforcement learning has proven effective for improving reasoning in large language models, but extending it to Masked Diffusion Language Models (MDLMs) remains challenging due to the intractability of the log-likelihood estimation. Existing approaches approximate this log-likelihood by modeling only the token predictions, ignoring the order in which positions are unmasked during generation. We observe that MDLM g...
- Summary (fallback): 机器翻译摘要显示：强化学习已被证明对于改善大型语言模型的推理是有效的，但由于对数似然估计的棘手性，将其扩展到掩蔽扩散语言模型（MDLM）仍然具有挑战性。现有方法通过仅对标记预测进行建模来近似这种对数似然，忽略生成过程中位置被揭露的顺序。我们观察到 MDLM 的生成在每个步骤都涉及两个决策：在每个屏蔽位置放置什么令牌以及重新屏蔽哪些位置。我们将其形式化为两阶段操作 MDP，表明策略梯度自然分解为标记项和掩蔽项。结合这两个术语的优化，可以在数学推理和编码基准上获得最先进的结果，在 GSM8K 上得分为 87.1%，在 MBPP 上得分为 53.4%。
- Keywords: language, models, policy, diffusion, reasoning

### 15. [主观风险分解：不确定性量化的新视角](https://arxiv.org/abs/2607.15196v1)
- Original title: Subjective Risk Decomposition: A New View for Uncertainty Quantification
- Authors: Raghad Alamri, Michele Caprio, Gavin Brown
- Meta: 2026-07-16 | stat.ML
- 中文摘要: 我们提出了不确定性量化的新观点。不确定性度量不是需要公理和论证的原语，而是更高级别建模决策的结果。我们展示了如何基于严格适当的损失，通过分解主观风险来导出认知和任意不确定性度量。逆交叉熵提供了一个突出的例子，其中分解恢复了经典的信息论不确定性项。同样的方法恢复了昆士兰大学文献中先前提出的许多措施，为它们提供了共同的理论基础。从实践的角度来看，这提出了一种新的 UQ 方法：给定建模场景和严格适当的损失，相应的认知项和任意项由主观风险分解得出。
- Abstract: We present a novel viewpoint for uncertainty quantification. Uncertainty measures are not primitives, in need of axioms and argumentation, but instead consequences, of higher-level modelling decisions. We show how epistemic and aleatoric uncertainty measures can be derived via decomposition of a subjective risk, based on a strictly proper loss. Reverse cross-entropy provides a prominent example, where decomposition...
- Summary (fallback): 机器翻译摘要显示：我们提出了不确定性量化的新观点。不确定性度量不是需要公理和论证的原语，而是更高级别建模决策的结果。我们展示了如何基于严格适当的损失，通过分解主观风险来导出认知和任意不确定性度量。逆交叉熵提供了一个突出的例子，其中分解恢复了经典的信息论不确定性项。同样的方法恢复了昆士兰大学文献中先前提出的许多措施，为它们提供了共同的理论基础。从实践的角度来看，这提出了一种新的 UQ 方法：给定建模场景和严格适当的损失，相应的认知项和任意项由主观风险分解得出。
- Keywords: uncertainty, risk, decomposition, subjective, view

### 16. [用于电信铷光谱的重入芯片自由空间光子接口](https://arxiv.org/abs/2607.15186v1)
- Original title: A re-entrant chip-free-space photonic interface for telecom-to-Rubidium spectroscopy
- Authors: Jia-Lin Chen, Ruixin Zhou, Deng-Hong Liu, You-Long Fan, Zhu-Bo Wang et al.
- Meta: 2026-07-16 | physics.optics
- 中文摘要: 光子集成电路 (PIC) 在单个芯片上以高效率、可扩展性和功能密度生成、路由和处理光。然而，严格限制的片上模式无法轻松访问原子蒸气、流体、增益介质和生物样本或与原子蒸气、流体、增益介质和生物样本有效地相互作用。现有的方法需要将介质带到芯片上或进入一个弱的、严格限制的渐逝场，这限制了交互量和可访问介质的范围。在这里，我们演示了一种可重入芯片自由空间接口，其中薄膜铌酸锂电路将电信光倍频，通过铷蒸气池发射 780 nm 场，并在同一芯片上重新收集反射探针。这种发射-相互作用-再收集循环可解析饱和吸收光谱，并在 2 小时内将电信激光器稳定在 $\pm 280$~kHz 范围内。
- Abstract: Photonic integrated circuits (PICs) generate, route, and process light with high efficiency, scalability, and functional density on a single chip. Yet the tightly confined on-chip modes can not easily access or effectively interact with atomic vapors, fluids, gain media, and biological samples. Existing approaches require bringing the medium onto the chip or into a weak, tightly confined evanescent field, which rest...
- Summary (fallback): 机器翻译摘要显示：光子集成电路 (PIC) 在单个芯片上以高效率、可扩展性和功能密度生成、路由和处理光。然而，严格限制的片上模式无法轻松访问原子蒸气、流体、增益介质和生物样本或与原子蒸气、流体、增益介质和生物样本有效地相互作用。现有的方法需要将介质带到芯片上或进入一个弱的、严格限制的渐逝场，这限制了交互量和可访问介质的范围。在这里，我们演示了一种可重入芯片自由空间接口，其中薄膜铌酸锂电路将电信光倍频，通过铷蒸气池发射 780 nm 场，并在同一芯片上重新收集反射探针。这种发射-相互作用-再收集循环可解析饱和吸收光谱，并在 2 小时内将电信激光器稳定在 $\pm 280$~kHz 范围内。
- Keywords: re-entrant, photonic, interface, chip, media

### 17. [基于物理的神经微分模型的 RTS 平滑引导学习](https://arxiv.org/abs/2607.15180v1)
- Original title: RTS Smoother-Guided Learning of Physics-Based Neural Differential Models
- Authors: Ahmet Demirkaya, Georgios Stratis, Tales Imbiriba, Zachary D. Danziger, Deniz Erdogmus
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 常微分方程 (ODE) 广泛用于模拟物理学、生物学、神经科学和生理学中的动力学系统，但在许多应用中，某些动力学方程是未知的，并且仅测量状态变量的子集。我们提出了一种混合神经物理框架，其中 ODE 的已知组件保持明确，而缺失的组件则由神经网络表示。所提出的方法由两个阶段组成，我们在状态估计和参数估计之间交替并迭代，直到满足预定标准。具体来说，在第一步中，我们将模型参数视为已知，并使用 Rauch-Tung-Striebel (RTS) 平滑器从可用测量中推断潜在状态。
- Abstract: Ordinary differential equations (ODEs) are widely used to model dynamical systems in physics, biology, neuroscience, and physiology, but in many applications some equations of the dynamics are unknown and only a subset of the state variables are measured. We propose a hybrid neural--physics framework in which the known components of the ODE are kept explicit and the missing components are represented by a neural net...
- Summary (fallback): 机器翻译摘要显示：常微分方程 (ODE) 广泛用于模拟物理学、生物学、神经科学和生理学中的动力学系统，但在许多应用中，某些动力学方程是未知的，并且仅测量状态变量的子集。我们提出了一种混合神经物理框架，其中 ODE 的已知组件保持明确，而缺失的组件则由神经网络表示。所提出的方法由两个阶段组成，我们在状态估计和参数估计之间交替并迭代，直到满足预定标准。具体来说，在第一步中，我们将模型参数视为已知，并使用 Rauch-Tung-Striebel (RTS) 平滑器从可用测量中推断潜在状态。
- Keywords: neural, state, known, components, method

### 18. [MedFailBench：临床医生构建的医疗 AI 安全边界检查开源基准](https://arxiv.org/abs/2607.15166v1)
- Original title: MedFailBench: A Clinician-Built Open-Source Benchmark for Medical AI Safety Boundary Inspection
- Authors: Goktug Ozkan
- Meta: 2026-07-16 | cs.AI
- 中文摘要: 大多数医疗人工智能基准测试都会衡量模型是否知道正确答案。 MedFailBench 提出了一个不同的问题：哪个安全边界失败了？我们提出了一个临床医生构建的综合基准和故障图集，按严重性 (1--5) 和安全门类型（错过紧急升级、不安全远程给药、不安全出院保证、证据伪造、不安全协议执行、来源支持差距）来标记医疗 AI 错误。当前的公开版本 (v0.2.1) 包含 44 个经过临床医生审查的综合病例，带有严重性注释、实时 HuggingFace 排行榜预览、安全门分类法、临床严重性评分标准以及用于存档模型响应筛选运行的自动化管道。不包括患者数据、临床验证声明或模型排名。 MedFailBench 在 Apache-2.0 和 CC-BY-4.0 下发布，并带有 Zenodo DOI 10.5281/zenodo.21205535。
- Abstract: Most medical AI benchmarks measure whether a model knows the correct answer. MedFailBench asks a different question: which safety boundary failed? We present a clinician-built synthetic benchmark and failure atlas that labels medical AI errors by severity (1--5) and safety gate type (missed urgent escalation, unsafe remote dosing, unsafe discharge reassurance, evidence fabrication, unsafe protocol execution, source...
- Summary (fallback): 机器翻译摘要显示：大多数医疗人工智能基准测试都会衡量模型是否知道正确答案。 MedFailBench 提出了一个不同的问题：哪个安全边界失败了？我们提出了一个临床医生构建的综合基准和故障图集，按严重性 (1--5) 和安全门类型（错过紧急升级、不安全远程给药、不安全出院保证、证据伪造、不安全协议执行、来源支持差距）来标记医疗 AI 错误。当前的公开版本 (v0.2.1) 包含 44 个经过临床医生审查的综合病例，带有严重性注释、实时 HuggingFace 排行榜预览、安全门分类法、临床严重性评分标准以及用于存档模型响应筛选运行的自动化管道。不包括患者数据、临床验证声明或模型排名。 MedFailBench 在 Apache-2.0 和 CC-BY-4.0 下发布，并带有 Zenodo DOI 10.5281/zenodo.2...
- Keywords: safety, medfailbench, medical, severity, unsafe

### 19. [符合政策的 Delta 蒸馏](https://arxiv.org/abs/2607.15161v1)
- Original title: On-Policy Delta Distillation
- Authors: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 在策略蒸馏是强化学习中的另一种训练后方法，它通过从教师模型提供令牌级监督来减轻奖励模型施加的约束。尽管同政策蒸馏已经在各种环境中进行了研究和应用，但其基本设计仍未得到充分探索。在本文中，我们引入了一种新的蒸馏奖励，称为增量信号，而不是直接模仿教师的输出分布。增量信号被定义为在推理能力的指令调整之前教师模型与其基本模型之间的差异。因此，它捕获推理调整引起的变化，并为传递推理能力提供更直接的信号。
- Abstract: On-policy distillation is an alternative post-training method in reinforcement learning that alleviates the constraints imposed by reward models by providing token-level supervision from a teacher model. Although on-policy distillation has been studied and applied across various settings, its fundamental design remains underexplored. In this paper, we introduce a new distillation reward, termed the delta signal, ins...
- Summary (fallback): 机器翻译摘要显示：在策略蒸馏是强化学习中的另一种训练后方法，它通过从教师模型提供令牌级监督来减轻奖励模型施加的约束。尽管同政策蒸馏已经在各种环境中进行了研究和应用，但其基本设计仍未得到充分探索。在本文中，我们引入了一种新的蒸馏奖励，称为增量信号，而不是直接模仿教师的输出分布。增量信号被定义为在推理能力的指令调整之前教师模型与其基本模型之间的差异。因此，它捕获推理调整引起的变化，并为传递推理能力提供更直接的信号。
- Keywords: distillation, on-policy, delta, signal, reasoning

### 20. [时间序列数据贝叶斯谱建模中的频率选择及其在可穿戴设备测量中的应用](https://arxiv.org/abs/2607.15157v1)
- Original title: Frequency Selection in Bayesian Spectral Modeling of Time Series Data with Applications to Wearable Device Measurements
- Authors: Beniamino Hadj-Amar, Vaishnav Krishnan, Marina Vannucci
- Meta: 2026-07-16 | stat.ME
- 中文摘要: 本文介绍了用于时间序列数据谱分析的贝叶斯尖峰和平板框架。所提出的方法将频率选择和降维与候选频率的细化网格相结合，实现振荡分量的高分辨率恢复，同时通过结构化的尖峰和平板先验促进稀疏性。随机搜索算法有效地探索后验空间，产生量化每个频率相关性的后验包含概率。我们通过频率包含模式的分层先验将框架扩展到多变量信号，使模型能够捕获多个时间序列中的共享节律和特定于组件的节律。广泛的仿真研究表明，与现有方法相比，该方法在频率估计和频谱功率重建方面具有鲁棒性和优越的性能。
- Abstract: This paper introduces a Bayesian spike-and-slab framework for spectral analysis of time series data. The proposed method combines frequency selection and dimensionality reduction with a refined grid of candidate frequencies, enabling high-resolution recovery of oscillatory components while promoting sparsity through a structured spike-and-slab prior. A stochastic search algorithm efficiently explores the posterior s...
- Summary (fallback): 机器翻译摘要显示：本文介绍了用于时间序列数据谱分析的贝叶斯尖峰和平板框架。所提出的方法将频率选择和降维与候选频率的细化网格相结合，实现振荡分量的高分辨率恢复，同时通过结构化的尖峰和平板先验促进稀疏性。随机搜索算法有效地探索后验空间，产生量化每个频率相关性的后验包含概率。我们通过频率包含模式的分层先验将框架扩展到多变量信号，使模型能够捕获多个时间序列中的共享节律和特定于组件的节律。广泛的仿真研究表明，与现有方法相比，该方法在频率估计和频谱功率重建方面具有鲁棒性和优越的性能。
- Keywords: frequency, spectral, time, series, analysis

### 21. [使用社交机器人评估身体虚弱和跌倒风险指标：对老年人的现场评估](https://arxiv.org/abs/2607.15156v1)
- Original title: Assessing Physical Frailty and Fall-Risk Indicators with Social Robots: An in situ Evaluation with Older Adults
- Authors: Aniol Civit, Antonio Andriella, Alba Martínez, Joan Ars, Aida Ribera et al.
- Meta: 2026-07-16 | cs.RO
- 中文摘要: 衰弱评估对于评估不良事件的风险以及老年人的健康和社会护理需求至关重要，但其管理仍然需要大量资源，并且通常依赖于粗略的临床结果，例如任务完成时间，这可能会忽视功能衰退的生物力学指标。为了解决这个问题，我们提出了一个机器人框架，指导老年人进行标准化的虚弱和跌倒风险测试，同时捕获临床评分和其他虚弱相关指标，从而更深入地了解用户的状况。该系统采用行为树架构，协调感知、决策、交互和测量模块。该机器人使用基于视觉的骨骼跟踪来评估已建立的临床测试，包括短期物理性能电池（SPPB）和定时起立（TUG）。
- Abstract: Frailty assessments are crucial to evaluate the risk of adverse events and the health and social care needs of older adults, yet their administration remains resource-intensive and typically relies on coarse clinical outcomes, such as task completion times, which may overlook biomechanical indicators of functional decline. To address this, we present a robotic framework that guides older adults through standardised...
- Summary (fallback): 机器翻译摘要显示：衰弱评估对于评估不良事件的风险以及老年人的健康和社会护理需求至关重要，但其管理仍然需要大量资源，并且通常依赖于粗略的临床结果，例如任务完成时间，这可能会忽视功能衰退的生物力学指标。为了解决这个问题，我们提出了一个机器人框架，指导老年人进行标准化的虚弱和跌倒风险测试，同时捕获临床评分和其他虚弱相关指标，从而更深入地了解用户的状况。该系统采用行为树架构，协调感知、决策、交互和测量模块。该机器人使用基于视觉的骨骼跟踪来评估已建立的临床测试，包括短期物理性能电池（SPPB）和定时起立（TUG）。
- Keywords: frailty, older, adults, clinical, indicators

### 22. [Atari Pong 中世界模型的概念引导空间正则化](https://arxiv.org/abs/2607.15142v1)
- Original title: Concept-Guided Spatial Regularization for World Models in Atari Pong
- Authors: Yukuan Lu, Zaishuo Xia, Weyl Lu, Yubei Chen
- Meta: 2026-07-16 | cs.AI
- 中文摘要: 世界模型通常被评估为基于模型的强化学习（MBRL）系统的组成部分，而世界模型本身很少被孤立地研究。我们研究了 Atari Pong 中的五个代表性视觉世界模型代理：DreamerV3、DIAMOND、TWISTER、Simulus 和 STORM。在重现训练管道并匹配报告的代理性能后，我们冻结学习的世界模型并使用闭环推出诊断对其进行评估：与相应的 MBRL 代理分开训练的策略与每个冻结模型交互，并检查生成的视频轨迹是否存在视觉和动态错误。在所有五个模型中，推出都包含明显的失败，包括球消失、球运动不正确以及球与桨的相互作用无效。
- Abstract: World models are usually evaluated as components of model-based reinforcement learning (MBRL) systems, while the world models themselves are rarely studied in isolation. We examine five representative visual world-model agents in Atari Pong: DreamerV3, DIAMOND, TWISTER, Simulus, and STORM. After reproducing their training pipelines and matching the reported agent performance, we freeze the learned world models and e...
- Summary (fallback): 机器翻译摘要显示：世界模型通常被评估为基于模型的强化学习（MBRL）系统的组成部分，而世界模型本身很少被孤立地研究。我们研究了 Atari Pong 中的五个代表性视觉世界模型代理：DreamerV3、DIAMOND、TWISTER、Simulus 和 STORM。在重现训练管道并匹配报告的代理性能后，我们冻结学习的世界模型并使用闭环推出诊断对其进行评估：与相应的 MBRL 代理分开训练的策略与每个冻结模型交互，并检查生成的视频轨迹是否存在视觉和动态错误。在所有五个模型中，推出都包含明显的失败，包括球消失、球运动不正确以及球与桨的相互作用无效。
- Keywords: models, world, mbrl, pong, five

### 23. [学习无穷小非构图草图](https://arxiv.org/abs/2607.15107v1)
- Original title: Learning in Infinitesimal Non-Compositional Sketches
- Authors: Sridhar Mahadevan
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 本文开发了一个分类框架——无穷小非组合草图学习（LINCS）——作为非组合性的修复：图表无法通过商草图分解提升到切线类别设置。机器学习问题被指定为草图：具有交换条件 $\mathcal D$、极限锥 $\mathcal L$ 和余极限 cocones $\mathcal K$ 的图，概括了损失函数或向量空间假设的常见标量化。非组合性纯粹被定义为通用因式分解问题的失败，而不是期望预测和实际预测之间的算术错误。给定一个学习草图 $\mathbb S=(S,\mathcal D,\mathcal L,\mathcal K)$（其底层图为 $S$）和模型 $D:J \rightarrow C$，基本缺陷是阻碍分解 $\mbox{Obs}(\mbox{Fact}_{\mathbb S}(D))$。
- Abstract: This paper develops a categorical framework -- Learning in Infinitesimal Non-Compositional Sketches (LINCS) -- as the repair of non-compositionality: failures of diagrams to factor through quotient sketches lifted to the tangent category setting. Machine learning problems are specified as sketches: graphs with commutativity conditions $\mathcal D$, limit cones $\mathcal L$, and colimit cocones $\mathcal K$, generali...
- Summary (fallback): 机器翻译摘要显示：本文开发了一个分类框架——无穷小非组合草图学习（LINCS）——作为非组合性的修复：图表无法通过商草图分解提升到切线类别设置。机器学习问题被指定为草图：具有交换条件 $\mathcal D$、极限锥 $\mathcal L$ 和余极限 cocones $\mathcal K$ 的图，概括了损失函数或向量空间假设的常见标量化。非组合性纯粹被定义为通用因式分解问题的失败，而不是期望预测和实际预测之间的算术错误。给定一个学习草图 $\mathbb S=(S,\mathcal D,\mathcal L,\mathcal K)$（其底层图为 $S$）和模型 $D:J \rightarrow C$，基本缺陷是阻碍分解 $\mbox{Obs}(\mbox{Fact}_{\mathbb S}(D))$。
- Keywords: learning, tangent, sketches, mathcal, mbox

### 24. [流行病学意义上的暴露模型。第 1 部分——基础模型](https://arxiv.org/abs/2607.15104v1)
- Original title: A model with exposure in the epidemiological sense. Part 1 -- Base model
- Authors: CI Hameni Nkwayep, Julien Arino, PM Tchepmo Djomegni
- Meta: 2026-07-16 | q-bio.PE
- 中文摘要: 我们探索了一种传染病传播模型，该模型将接触病原体纳入该术语的经典流行病学接受中，即与感染者发生了接触，但不一定获得感染。该模型还包括（离散）感染年龄结构，允许隐式描述受感染个体的病毒载量，进而描述发生感染的概率作为感染接触者病毒载量的函数。
- Abstract: We explore a model of infectious disease spread that incorporates exposure to the pathogen in the classic epidemiological acceptation of the term, i.e., a contact with an infectious individual has taken place but the infection has not necessarily been acquired. The model also includes a (discrete) age of infection structure, allowing to implicitly describe the viral load of infected individuals and in turn, to descr...
- Summary (fallback): 机器翻译摘要显示：我们探索了一种传染病传播模型，该模型将接触病原体纳入该术语的经典流行病学接受中，即与感染者发生了接触，但不一定获得感染。该模型还包括（离散）感染年龄结构，允许隐式描述受感染个体的病毒载量，进而描述发生感染的概率作为感染接触者病毒载量的函数。
- Keywords: model, infectious, infection, exposure, epidemiological

### 25. [蛋白质-配体结合动力学的加速无描述符路径采样](https://arxiv.org/abs/2607.15101v1)
- Original title: Accelerated descriptor-free path sampling for protein-ligand binding kinetics
- Authors: Simon M. Lichtinger, Roberto Covino
- Meta: 2026-07-16 | physics.chem-ph
- 中文摘要: 蛋白质-配体结合系统的动力学越来越被认为是药物功效的关键决定因素，但仍然比结合亲和力更难计算。现有的动力学方法要么沿着集体变量 (CV) 偏置动力学，要求仔细的系统特定 CV 设计，要么使用路径采样，这保持动力学无偏差，但很难从深自由能井中收敛速率，并且通常依赖于手工设计的描述符。通过结合“两全其美”，我们提出了一种方法，以适度的计算成本和最小的微调来计算一般配体非结合问题的精确动力学，该方法建立在人工智能分子机制发现（AIMMD）路径采样框架的基础上。
- Abstract: The kinetics of protein-ligand binding systems are increasingly recognized as a key determinant of drug efficacy, yet remain far harder to compute than binding affinities. Existing kinetics methods either bias the dynamics along a collective variable (CV), demanding careful system-specific CV design, or use path sampling, which keeps the dynamics unbiased but can struggle to converge rates out of deep free-energy we...
- Summary (fallback): 机器翻译摘要显示：蛋白质-配体结合系统的动力学越来越被认为是药物功效的关键决定因素，但仍然比结合亲和力更难计算。现有的动力学方法要么沿着集体变量 (CV) 偏置动力学，要求仔细的系统特定 CV 设计，要么使用路径采样，这保持动力学无偏差，但很难从深自由能井中收敛速率，并且通常依赖于手工设计的描述符。通过结合“两全其美”，我们提出了一种方法，以适度的计算成本和最小的微调来计算一般配体非结合问题的精确动力学，该方法建立在人工智能分子机制发现（AIMMD）路径采样框架的基础上。
- Keywords: kinetics, sampling, path, binding, committor

### 26. [AlphaWiSE：用于持续多模态表示学习的自适应权重插值](https://arxiv.org/abs/2607.15094v1)
- Original title: AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning
- Authors: Sarthak Jain, Qiran Hu, Zhen Zhu, Yaoyao Liu
- Meta: 2026-07-16 | cs.CV
- 中文摘要: 多模态模型（例如 CLIP）学习用于跨模态检索的共享嵌入空间，但对顺序到达的数据的持续适应可能会破坏从早期阶段获得的跨模态对齐。传统的持续学习方法返回单个检查点，这使得每个检索方向都遵循相同的稳定性-可塑性权衡。我们提出了 AlphaWiSE，一种事后权重空间插值方法，由两个冻结源检查点组成。对于由其检查点键标识的每个对齐参数张量，AlphaWiSE 拟合所有张量条目共享的一个标量插值系数。这些系数适合较小的样本存储器，并用于实现一个插值检查点。部署的模型与任一源检查点具有相同的架构和参数计数，不需要额外的推理时间。
- Abstract: Multimodal models such as CLIP learn a shared embedding space for cross-modal retrieval, but continual adaptation to sequentially arriving data can disrupt the cross-modal alignment acquired from earlier phases. Conventional continual-learning methods return a single checkpoint, which commits every retrieval direction to the same stability-plasticity trade-off. We propose AlphaWiSE, a post-hoc weight-space interpola...
- Summary (fallback): 机器翻译摘要显示：多模态模型（例如 CLIP）学习用于跨模态检索的共享嵌入空间，但对顺序到达的数据的持续适应可能会破坏从早期阶段获得的跨模态对齐。传统的持续学习方法返回单个检查点，这使得每个检索方向都遵循相同的稳定性-可塑性权衡。我们提出了 AlphaWiSE，一种事后权重空间插值方法，由两个冻结源检查点组成。对于由其检查点键标识的每个对齐参数张量，AlphaWiSE 拟合所有张量条目共享的一个标量插值系数。这些系数适合较小的样本存储器，并用于实现一个插值检查点。部署的模型与任一源检查点具有相同的架构和参数计数，不需要额外的推理时间。
- Keywords: retrieval, checkpoint, alphawise, interpolation, continual

### 27. [评估长期马尔可夫决策过程的协变量平衡](https://arxiv.org/abs/2607.15080v1)
- Original title: Evaluating covariate balance for long time horizon Markov decision processes
- Authors: Joshua Spear, Rebecca Pope, Neil J Sebire
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 本文探讨了在应用离线强化学习 (RL) 得出最佳治疗建议的研究中，协变量平衡诊断的应用，用于检测隐藏的混杂/模型错误规范的存在。结果表明，要么现有的离线强化学习研究中的治疗建议存在较高的偏倚风险，要么现有的协变量平衡指标不足以评估此类研究。无论如何，现有的离线强化学习研究不能得出统计上稳健的结论。结论提出了未来的研究方向，以获得方法上更稳健的离线强化学习在治疗推荐问题上的应用。
- Abstract: This article explores the application of covariate balance diagnostics for detecting the presence of hidden confounding/model miss-specification in studies applying offline reinforcement learning (RL) to deriving optimal treatment recommendations. The results demonstrate that, either there is a high risk of bias within existing offline RL studies for treatment recommendations or, existing covariate balance metrics a...
- Summary (fallback): 机器翻译摘要显示：本文探讨了在应用离线强化学习 (RL) 得出最佳治疗建议的研究中，协变量平衡诊断的应用，用于检测隐藏的混杂/模型错误规范的存在。结果表明，要么现有的离线强化学习研究中的治疗建议存在较高的偏倚风险，要么现有的协变量平衡指标不足以评估此类研究。无论如何，现有的离线强化学习研究不能得出统计上稳健的结论。结论提出了未来的研究方向，以获得方法上更稳健的离线强化学习在治疗推荐问题上的应用。
- Keywords: studies, offline, covariate, balance, treatment

### 28. [工程应用非线性动力学稀疏辨识简介](https://arxiv.org/abs/2607.15077v1)
- Original title: An Introduction to Sparse Identification of Nonlinear Dynamics for Engineering Applications
- Authors: Yao Cheng Li, Ana Larrañaga, Steven L. Brunton, Urban Fasel
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 许多工程问题涉及的现象的控制方程很难表征或仅部分已知。神经网络等替代建模技术可以捕获这些系统的行为，但它们通常需要大量的训练数据集，而这些数据集在工程环境中很难获得，并且产生的模型的物理可解释性有限。非线性动力学稀疏识别 (SINDy) 方法通过对候选非线性项库执行稀疏回归，从相对较小的数据集中恢复可解释的控制方程，解决了这两个限制。尽管 SINDy 已在规范基准系统上得到广泛论证，但其在实际工程问题中的应用却鲜有广泛记录。
- Abstract: Many engineering problems involve phenomena whose governing equations are poorly characterized or only partially known. Surrogate modeling techniques such as neural networks can capture the behavior of these systems, but they typically demand large training datasets that are difficult to obtain in engineering contexts and yield models with limited physical interpretability. The Sparse Identification of Nonlinear Dyn...
- Summary (fallback): 机器翻译摘要显示：许多工程问题涉及的现象的控制方程很难表征或仅部分已知。神经网络等替代建模技术可以捕获这些系统的行为，但它们通常需要大量的训练数据集，而这些数据集在工程环境中很难获得，并且产生的模型的物理可解释性有限。非线性动力学稀疏识别 (SINDy) 方法通过对候选非线性项库执行稀疏回归，从相对较小的数据集中恢复可解释的控制方程，解决了这两个限制。尽管 SINDy 已在规范基准系统上得到广泛论证，但其在实际工程问题中的应用却鲜有广泛记录。
- Keywords: engineering, sindy, identification, sparse, nonlinear

### 29. [用于上下文强盗中离策略评估的内核加权重要性采样](https://arxiv.org/abs/2607.15067v1)
- Original title: Kernel weighted importance sampling for off-policy evaluation in contextual bandits
- Authors: Joshua Spear, Matthieu Komorowski, Rebecca Pope, Neil J Sebire, Erica E. M. Moodie
- Meta: 2026-07-16 | cs.LG
- 中文摘要: 本文提出了一种新颖的估计器，用于仅使用上下文强盗的离线数据来执行离策略评估。所提出的估计器 Kernel-WIS 被证明是渐近一致的，并且在经验上优于强基线（包括普通加权重要性抽样），特别是在包括行为政策未规范在内的复杂条件下。 Kernel-WIS 的好处源自将普通加权重要性采样的有界属性与普通重要性采样的线性相结合。
- Abstract: This article presents a novel estimator for performing off-policy evaluation using only offline data for contextual bandits. The proposed estimator, Kernel-WIS is demonstrated to be asymptotically consistent and to empirically outperform strong baselines (including vanilla weighted importance sampling), particularly under complex conditions including behaviour policy miss-specification. The benefit of Kernel-WIS is...
- Summary (fallback): 机器翻译摘要显示：本文提出了一种新颖的估计器，用于仅使用上下文强盗的离线数据来执行离策略评估。所提出的估计器 Kernel-WIS 被证明是渐近一致的，并且在经验上优于强基线（包括普通加权重要性抽样），特别是在包括行为政策未规范在内的复杂条件下。 Kernel-WIS 的好处源自将普通加权重要性采样的有界属性与普通重要性采样的线性相结合。
- Keywords: importance, sampling, weighted, vanilla, off-policy

### 30. [DriftWorld：通过漂移进行快速世界建模](https://arxiv.org/abs/2607.15065v1)
- Original title: DriftWorld: Fast World Modeling through Drifting
- Authors: Susie Lu, Haonan Chen, Weirui Ye, Yilun Du
- Meta: 2026-07-16 | cs.RO
- 中文摘要: 预测世界模型使机器人能够通过想象其行为的结果来进行计划，但它们的控制价值取决于快速生成许多部署。这给基于扩散的世界模型带来了瓶颈：多步采样使得每次部署都变得昂贵，限制了推理时的大规模动作搜索。我们介绍 DriftWorld，一个基于漂移生成模型的动作条件世界模型。 DriftWorld 不是在推理时迭代去噪，而是在训练期间学习动作条件漂移，使其能够以 30+ fps 的单次正向传递从当前观察生成未来帧和候选动作序列，这比基于扩散的基线平均快 17 倍。我们在标准的基于视觉的机器人操作基准上评估 DriftWorld，包括 Bridge-V2、RT-1、语言表、Push-T 和 Robomimic。
- Abstract: Predictive world models enable robots to plan by imagining the outcomes of their actions, but their value for control hinges on generating many rollouts quickly. This creates a bottleneck for diffusion-based world models: multistep sampling makes each rollout expensive, limiting large-scale action search at inference time. We introduce DriftWorld, an action-conditioned world model based on drifting generative models...
- Summary (fallback): 机器翻译摘要显示：预测世界模型使机器人能够通过想象其行为的结果来进行计划，但它们的控制价值取决于快速生成许多部署。这给基于扩散的世界模型带来了瓶颈：多步采样使得每次部署都变得昂贵，限制了推理时的大规模动作搜索。我们介绍 DriftWorld，一个基于漂移生成模型的动作条件世界模型。 DriftWorld 不是在推理时迭代去噪，而是在训练期间学习动作条件漂移，使其能够以 30+ fps 的单次正向传递从当前观察生成未来帧和候选动作序列，这比基于扩散的基线平均快 17 倍。我们在标准的基于视觉的机器人操作基准上评估 DriftWorld，包括 Bridge-V2、RT-1、语言表、Push-T 和 Robomimic。
- Keywords: driftworld, world, models, fast, drifting

## biorxiv

### 1. [斑马雀听觉端脑中芳香酶和非芳香酶神经元的相似突触和电流输入特性](https://www.biorxiv.org/content/10.64898/2026.07.16.738905v1)
- Original title: Similar Synaptic and Current Input Properties of Aromatase and Nonaromatase Neurons in the Zebra Finch Auditory Telencephalon
- Authors: Furest Cataldo, B., Anderson, P. N., Remage-Healey, L.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.16.738905
- 中文摘要: 雌激素因其在性发育和成熟中的作用而闻名，支持多种大脑功能，包括认知、神经保护和感觉处理。例如，在鸣禽的听觉前脑区域尾内侧nidopallium（NCM）中，神经雌激素会因同种声音和社交刺激而升高；反过来，NCM 中神经雌激素升高会迅速增强听觉处理能力，与性别无关。尽管神经雌激素对大脑功能起着关键作用，但芳香酶（神经雌激素合成）神经元的细胞和生理特性是否与不表达芳香酶的神经元不同，仍然很大程度上未知，正如其他类固醇生成细胞类型（例如肾上腺细胞）中所见的专门化所预期的那样。
- Abstract: Estrogens, commonly known for their role in sexual development and maturation, support a wide variety of brain functions, including cognition, neuroprotection, and sensory processing. For example, in a songbird auditory forebrain region, caudomedial nidopallium (NCM), neuroestrogens are elevated in response to conspecific vocal and social stimuli; in turn, elevated neuroestrogens in NCM are known to rapidly enhance...
- Summary (fallback): 机器翻译摘要显示：雌激素因其在性发育和成熟中的作用而闻名，支持多种大脑功能，包括认知、神经保护和感觉处理。例如，在鸣禽的听觉前脑区域尾内侧nidopallium（NCM）中，神经雌激素会因同种声音和社交刺激而升高；反过来，NCM 中神经雌激素升高会迅速增强听觉处理能力，与性别无关。尽管神经雌激素对大脑功能起着关键作用，但芳香酶（神经雌激素合成）神经元的细胞和生理特性是否与不表达芳香酶的神经元不同，仍然很大程度上未知，正如其他类固醇生成细胞类型（例如肾上腺细胞）中所见的专门化所预期的那样。
- Keywords: aromatase, neurons, synaptic, input, properties

### 2. [发育丰富增强了地形结构的本体感受皮层代码](https://www.biorxiv.org/content/10.64898/2026.07.14.738599v1)
- Original title: Developmental enrichment enhances a topographically structured proprioceptive cortical code
- Authors: Palacio Manzano, M., Ma, F., Hoffmann Schreiner, C., Ravussin, Y., Prsa, M.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.14.738599
- 中文摘要: 本体感觉皮层的组织源自发育过程中依赖经验的肢体使用模式，而不仅仅是反映周围神经支配。然而，人们对这些发展变化的程度和细节仍然知之甚少。为了解决这个问题，我们研究了早期环境富集（EE）如何重塑小鼠前肢本体感觉皮层的地形和功能特性。使用宽视野钙成像，我们发现 EE 不会引起中尺度激活图的重大重组。为了解决细胞级拓扑结构，我们开发了一种大视场荧光宏观显微镜，能够在整个激活区域进行无偏差的单神经元成像。
- Abstract: The organization of proprioceptive cortex emerges from experience-dependent patterns of limb use during development, rather than merely reflecting peripheral innervation. However, the degree and specifics of these developmental changes remain poorly understood. To address this question, we investigated how early environmental enrichment (EE) reshapes the topography and functional properties of the mouse forelimb pro...
- Summary (fallback): 机器翻译摘要显示：本体感觉皮层的组织源自发育过程中依赖经验的肢体使用模式，而不仅仅是反映周围神经支配。然而，人们对这些发展变化的程度和细节仍然知之甚少。为了解决这个问题，我们研究了早期环境富集（EE）如何重塑小鼠前肢本体感觉皮层的地形和功能特性。使用宽视野钙成像，我们发现 EE 不会引起中尺度激活图的重大重组。为了解决细胞级拓扑结构，我们开发了一种大视场荧光宏观显微镜，能够在整个激活区域进行无偏差的单神经元成像。
- Keywords: proprioceptive, developmental, enrichment, cortex, tuning

### 3. [星形细胞 FMRP 调节脆性 X 综合征中脊髓小白蛋白表达神经元的功能](https://www.biorxiv.org/content/10.64898/2026.07.17.737291v1)
- Original title: Astrocytic FMRP regulates the function of spinal parvalbumin-expressing neurons in Fragile X Syndrome
- Authors: Qiu, H., Jalandoni, R. F., Derham, A., Reinisch, N., Chen, C. et al.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.17.737291
- 中文摘要: 触觉过敏是脆性 X 综合症 (FXS) 的常见症状，其特征是对无害的触摸或纹理过度反应。然而，这种感觉处理改变背后的神经回路仍然不完全清楚。先前的研究主要集中在皮质和周围神经元功能障碍。然而，构成体感整合第一个中心部位的脊髓背角回路也包含可能导致对无害刺激过敏的元件，但其在这种病理学中的参与仍不完全清楚。在这里，我们发现表达脊髓小清蛋白 (PV) 的中间神经元 (PVN) 在 FXS 中功能失调，PVN 是一种抑制性群体，可控制触摸感觉输入以激活伤害感受通路。
- Abstract: Tactile hypersensitivity is a common symptom of Fragile X Syndrome (FXS) characterized by over-responsiveness to innocuous touch or textures. Yet, the neural circuitry underlying this altered sensory processing remains incompletely understood. Previous studies have focused on cortical and peripheral neuron dysfunction. However, the spinal dorsal horn circuits, which make up the first central site of somatosensory in...
- Summary (fallback): 机器翻译摘要显示：触觉过敏是脆性 X 综合症 (FXS) 的常见症状，其特征是对无害的触摸或纹理过度反应。然而，这种感觉处理改变背后的神经回路仍然不完全清楚。先前的研究主要集中在皮质和周围神经元功能障碍。然而，构成体感整合第一个中心部位的脊髓背角回路也包含可能导致对无害刺激过敏的元件，但其在这种病理学中的参与仍不完全清楚。在这里，我们发现表达脊髓小清蛋白 (PV) 的中间神经元 (PVN) 在 FXS 中功能失调，PVN 是一种抑制性群体，可控制触摸感觉输入以激活伤害感受通路。
- Keywords: pvns, spinal, firing, fmrp, dorsal

### 4. [兴奋性延迟耦合解释了同相和反相功能连接](https://www.biorxiv.org/content/10.64898/2026.07.17.739148v1)
- Original title: Excitatory delay-coupling explains in-phase and antiphase functional connectivity
- Authors: Omurtag, A., Dragomir, A., Crofts, J., Lytton, W. W.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.17.739148
- 中文摘要: 大脑区域之间协调的振荡活动支撑着认知，但控制这种协调的相位关系仍然知之甚少。使用 31 名执行运动学习任务的参与者的头皮脑电图，我们发现站点间相位聚类主要发生在同相或反相关系中，它们之间的过渡由传导延迟控制。尽管距离很远，同源半球间对仍保持同相，这与更快的胼胝体传导一致。两个延迟耦合兴奋群体的最小模型无需参数调整即可重现这些特征；稳定性分析表明，同相和反相振荡是由竞争不稳定性引起的，延迟决定了哪一个占主导地位。
- Abstract: Coordinated oscillatory activity between brain regions underpins cognition, yet the phase relationships governing this coordination remain poorly understood. Using scalp EEG from 31 participants performing a motor learning task, we show that inter-site phase clustering occurs predominantly at in-phase or antiphase relationships, with the transition between them governed by conduction delay. Homologous interhemispher...
- Summary (fallback): 机器翻译摘要显示：大脑区域之间协调的振荡活动支撑着认知，但控制这种协调的相位关系仍然知之甚少。使用 31 名执行运动学习任务的参与者的头皮脑电图，我们发现站点间相位聚类主要发生在同相或反相关系中，它们之间的过渡由传导延迟控制。尽管距离很远，同源半球间对仍保持同相，这与更快的胼胝体传导一致。两个延迟耦合兴奋群体的最小模型无需参数调整即可重现这些特征；稳定性分析表明，同相和反相振荡是由竞争不稳定性引起的，延迟决定了哪一个占主导地位。
- Keywords: in-phase, connectivity, phase, conduction, antiphase

### 5. [早期逆境选择性地重塑大脑发育中的躯体认知行动网络](https://www.biorxiv.org/content/10.64898/2026.07.17.739165v1)
- Original title: Early Adversity Selectively Reshapes the Somato-Cognitive Action Network in the Developing Brain
- Authors: Antonacci, C., Giampetruzzi, E., Grimsrud, G., Koirala, S., Uy, J. P. et al.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.17.739165
- 中文摘要: 早期的逆境是对大脑发育最有力的环境影响之一。然而，它是否重塑了皮质网络的区域布局，以及沿着哪些维度，尚不清楚。在 4,525 名 9-18 岁青少年的纵向样本中，我们得出了个性化的皮质分区，并将 15 个网络的拓扑结构与 10 个数据驱动的逆境维度相关联。更大程度地暴露于威胁，但不是剥夺或不可预测性，可以预测躯体认知行动网络（SCAN）的剂量依赖性扩张，其效果比任何其他网络大近七倍。 SCAN 向感觉运动极扩展，侵占邻居，并将功能连接转向感觉运动，远离控制系统。扩张介导了威胁与较差认知之间的关联，在波浪中、儿童内部和样本外复制。
- Abstract: Early adversity is among the most potent environmental influences on the developing brain; yet whether it remodels the areal layout of cortical networks, and along which dimensions, is unknown. In a longitudinal sample of 4,525 youth aged 9-18, we derived individualized cortical parcellations and related the topography of 15 networks to 10 data-driven dimensions of adversity. Greater exposure to threat, but not depr...
- Summary (fallback): 机器翻译摘要显示：早期的逆境是对大脑发育最有力的环境影响之一。然而，它是否重塑了皮质网络的区域布局，以及沿着哪些维度，尚不清楚。在 4,525 名 9-18 岁青少年的纵向样本中，我们得出了个性化的皮质分区，并将 15 个网络的拓扑结构与 10 个数据驱动的逆境维度相关联。更大程度地暴露于威胁，但不是剥夺或不可预测性，可以预测躯体认知行动网络（SCAN）的剂量依赖性扩张，其效果比任何其他网络大近七倍。 SCAN 向感觉运动极扩展，侵占邻居，并将功能连接转向感觉运动，远离控制系统。扩张介导了威胁与较差认知之间的关联，在波浪中、儿童内部和样本外复制。
- Keywords: adversity, network, developing, brain, early

### 6. [学习阅读第二语言在 VWFA 中建立与母语表示并行的 L2 表示](https://www.biorxiv.org/content/10.64898/2026.07.16.739038v1)
- Original title: Learning to read a second language establishes a parallel L2 representation alongside the native one in the VWFA
- Authors: Fan, S., Feng, X., Yu, X., Zhan, M., Zhang, M. et al.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.16.739038
- 中文摘要: 学习阅读第二语言需要大脑将新的书写系统融入到已经建立的母语阅读网络中，但这个过程如何重塑视觉词形区域（VWFA）仍然知之甚少。使用功能磁共振成像和被动观看范式，我们系统地研究了三组以普通话为母语的儿童在二语读写能力习得的不同阶段（二语预读者、二语初级读者和二语高级读者）中 VWFA 对中文 (L1) 和英语 (L2) 单词的反应如何演变。
- Abstract: Learning to read a second language requires the brain to incorporate a new writing system into an already established native-language reading network, yet how this process reshapes the Visual Word Form Area (VWFA) remains poorly understood. Using fMRI with a passive viewing paradigm, we systematically investigated how VWFA responses to Chinese (L1) and English (L2) words evolved across three groups of native Mandari...
- Summary (fallback): 机器翻译摘要显示：学习阅读第二语言需要大脑将新的书写系统融入到已经建立的母语阅读网络中，但这个过程如何重塑视觉词形区域（VWFA）仍然知之甚少。使用功能磁共振成像和被动观看范式，我们系统地研究了三组以普通话为母语的儿童在二语读写能力习得的不同阶段（二语预读者、二语初级读者和二语高级读者）中 VWFA 对中文 (L1) 和英语 (L2) 单词的反应如何演变。
- Keywords: vwfa, learning, responses, model, read

### 7. [大规模群体神经影像揭示功能性大脑组织中的潜在亚群结构](https://www.biorxiv.org/content/10.64898/2026.07.17.739129v1)
- Original title: Large-scale population neuroimaging reveals latent subgroup structure in functional brain organisation
- Authors: Farahibozorg, S. R., Smith, S. M., Elliott, L. T., Woolrich, M. W.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.17.739129
- 中文摘要: 大规模功能 MRI 数据集提供了了解人脑功能个体间差异并将这种差异与行为和健康联系起来的资源。然而，大多数现有方法无法弥合总体平均模型和个体特定模型之间的差距，限制了个体间结构化亚组异质性的识别。在这里，我们开发了一个可扩展的框架，用于在来自 19,993 名英国生物银行参与者的群体规模静息态 fMRI 数据中进行无监督亚组发现。使用随机概率功能模式，我们估计静息状态网络的人口信息个体化空间拓扑，并为每个参与者导出高维功能指纹。
- Abstract: Large-scale functional MRI datasets provide resources to understand inter-individual variation in human brain function and relate this variation to behaviour and health. However, most existing approaches fail to bridge the gap between population-average and individual-specific modelling, limiting the identification of structured subgroup heterogeneity across individuals. Here we develop a scalable framework for unsu...
- Summary (fallback): 机器翻译摘要显示：大规模功能 MRI 数据集提供了了解人脑功能个体间差异并将这种差异与行为和健康联系起来的资源。然而，大多数现有方法无法弥合总体平均模型和个体特定模型之间的差距，限制了个体间结构化亚组异质性的识别。在这里，我们开发了一个可扩展的框架，用于在来自 19,993 名英国生物银行参与者的群体规模静息态 fMRI 数据中进行无监督亚组发现。使用随机概率功能模式，我们估计静息状态网络的人口信息个体化空间拓扑，并为每个参与者导出高维功能指纹。
- Keywords: subgroup, functional, brain, large-scale, latent

### 8. [功能连接梯度取决于皮质采样位置和大脑状态](https://www.biorxiv.org/content/10.64898/2026.07.14.738484v1)
- Original title: Functional connectivity gradients depend on cortical sampling position and brain state
- Authors: Li, M., Ding, Z., Gore, J. C.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.14.738484
- 中文摘要: 功能连接分析通常将从附近皮质位置采样的信号视为可互换的，尽管灰白色边界存在解剖学和血流动力学转变。我们测试了抽样位置是否构成宏观功能组织的状态敏感维度。在 176 名具有 4 次 7 T 静息状态和 4 次电影观看运行的人类连接组计划年轻人中，BOLD 时间序列是从特定主题的中层和灰白色边界表面中采样的，在 400 个皮质块中进行总结，并嵌入到一个共同的功能梯度空间中。观看电影减少了表面之间的主梯度分离，但这种效果在空间上是异质的：视觉、边缘和默认网络聚合，而显着/腹侧注意皮层则不同。
- Abstract: Functional-connectivity analyses often treat signals sampled from nearby cortical positions as interchangeable, despite anatomical and hemodynamic transitions at the gray-white boundary. We tested whether sampling position constitutes a state-sensitive dimension of macroscale functional organization. In 176 Human Connectome Project young adults with four 7 T resting-state and four movie-watching runs, BOLD time seri...
- Summary (fallback): 机器翻译摘要显示：功能连接分析通常将从附近皮质位置采样的信号视为可互换的，尽管灰白色边界存在解剖学和血流动力学转变。我们测试了抽样位置是否构成宏观功能组织的状态敏感维度。在 176 名具有 4 次 7 T 静息状态和 4 次电影观看运行的人类连接组计划年轻人中，BOLD 时间序列是从特定主题的中层和灰白色边界表面中采样的，在 400 个皮质块中进行总结，并嵌入到一个共同的功能梯度空间中。观看电影减少了表面之间的主梯度分离，但这种效果在空间上是异质的：视觉、边缘和默认网络聚合，而显着/腹侧注意皮层则不同。
- Keywords: cortical, organization, functional, connectivity, sampling

### 9. [通过微流体分离和 DIA-MS 对人 iPSC 衍生神经元进行深层轴突蛋白质组学](https://www.biorxiv.org/content/10.64898/2026.07.17.739061v1)
- Original title: Deep axonal proteomics of human iPSC-derived neurons by microfluidic separation and DIA-MS
- Authors: Sauter, C. M., Sandy, Z., Korneck, M., Albrecht, V., Kraft, M. et al.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.17.739061
- 中文摘要: 神经元的定义特征之一是它们分为体细胞、树突和轴突。轴突高度专门用于长距离信号传输，但在神经退行性变的情况下也表现出独特的脆弱性，这意味着特殊的轴突蛋白质组。然而，轴突的深入蛋白质组学表征由于难以分离足够数量的纯轴突材料以进行常规质谱分析而受到限制。在这里，我们将基于微流体的轴突-体分离与 Orbitrap Astral 质谱仪上的数据独立采集质谱 (DIA-MS) 相结合，对人类诱导多能干细胞 (iPSC) 衍生的皮质神经元的区室解析蛋白质组进行深度分析。
- Abstract: One of the defining features of neurons is their compartmentalisation into soma, dendrites and axon. Axons are highly specialised for the transmission of signals over long distances but also exhibit unique vulnerabilities in the context of neurodegeneration, implying a specialised axonal proteome. However, in-depth proteomic characterisation of axons has been limited by the difficulty of isolating pure axonal materi...
- Summary (fallback): 机器翻译摘要显示：神经元的定义特征之一是它们分为体细胞、树突和轴突。轴突高度专门用于长距离信号传输，但在神经退行性变的情况下也表现出独特的脆弱性，这意味着特殊的轴突蛋白质组。然而，轴突的深入蛋白质组学表征由于难以分离足够数量的纯轴突材料以进行常规质谱分析而受到限制。在这里，我们将基于微流体的轴突-体分离与 Orbitrap Astral 质谱仪上的数据独立采集质谱 (DIA-MS) 相结合，对人类诱导多能干细胞 (iPSC) 衍生的皮质神经元的区室解析蛋白质组进行深度分析。
- Keywords: axonal, neurons, proteins, human, proteome

### 10. [自发脑类器官活动中的涌现拓扑结构](https://www.biorxiv.org/content/10.64898/2026.07.17.739228v1)
- Original title: Emergent topological structure in spontaneous brain-organoid activity
- Authors: Bodnia, E., Basart, M., Hai, S., Ford, L., Miolane, N. et al.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.17.739228
- 中文摘要: 神经活动被广泛认为是在嵌入高维状态空间的低维结构上组织的。持久同源性直接从成对相关的模式中读取这种结构，而不需要提前假设哪些变量是相关的。我们将持久同源性应用于人类 (Lancaster) 和小鼠 (Pa\c{s}ca) 皮质类器官自发活动的微电极阵列 (MEA) 记录，涵盖 26$--234$ 同时排序的单元，并询问拓扑数据分析是否可以解析神经记录实际提供的节点计数的结构。在相关空间中构建加权网络并通过 Vietoris-Rips 过滤对其进行表征，我们发现第一个同源性（$H_1$，循环）显着高于 $14$ 的 $18$ 数据集中的速率和群体保留零值。
- Abstract: Neural activity is widely held to organize on low-dimensional structure embedded in a high-dimensional state space. Persistent homology reads such structure directly from the pattern of pairwise correlations, without assuming in advance which variables are relevant. We apply persistent homology to microelectrode-array (MEA) recordings of spontaneous activity from human (Lancaster) and mouse (Pa\c{s}ca) cortical orga...
- Summary (fallback): 机器翻译摘要显示：神经活动被广泛认为是在嵌入高维状态空间的低维结构上组织的。持久同源性直接从成对相关的模式中读取这种结构，而不需要提前假设哪些变量是相关的。我们将持久同源性应用于人类 (Lancaster) 和小鼠 (Pa\c{s}ca) 皮质类器官自发活动的微电极阵列 (MEA) 记录，涵盖 26$--234$ 同时排序的单元，并询问拓扑数据分析是否可以解析神经记录实际提供的节点计数的结构。在相关空间中构建加权网络并通过 Vietoris-Rips 过滤对其进行表征，我们发现第一个同源性（$H_1$，循环）显着高于 $14$ 的 $18$ 数据集中的速率和群体保留零值。
- Keywords: structure, homology, topological, activity, neural

### 11. [通过调幅千赫兹磁扰 (AM-kTMP) 操纵语音感知](https://www.biorxiv.org/content/10.64898/2026.07.17.739132v1)
- Original title: Manipulating speech perception with amplitude-modulated kilohertz magnetic perturbation (AM-kTMP)
- Authors: Pari, R. K., Merrick, C., Reber, P., Luu, C., Ivry, R. B. et al.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.17.739132
- 中文摘要: 语音感知被假设为利用神经活动来影响话语的节奏特性。感知灵敏度随言语引起的振荡活动的阶段以及颞叶经颅交流电刺激（tACS）引起的外部振荡扰动而变化。在这里，我们使用了一种新形式的非侵入性脑刺激（NIBS），即千赫兹经颅磁扰动（kTMP），其中通过连续高频载波信号（3.5 kHz）的幅度调制（AM）产生低频扰动。作为一种磁感应方法，kTMP 可以在皮质表面产生比 tACS 更高的电场，并减少皮肤共刺激。人类参与者 (n=40) 在接收 AM 分量为 3.125 Hz 的 kTMP 的同时聆听有节奏的语音序列。
- Abstract: Speech perception has been hypothesized to exploit neural activity that entrains to the rhythmic properties of the utterance. Perceptual sensitivity varies with the phase of oscillatory activity induced by speech, and with an external oscillatory perturbation induced by transcranial alternating current stimulation (tACS) over the temporal lobe. Here we used a new form of non-invasive brain stimulation (NIBS), kilohe...
- Summary (fallback): 机器翻译摘要显示：语音感知被假设为利用神经活动来影响话语的节奏特性。感知灵敏度随言语引起的振荡活动的阶段以及颞叶经颅交流电刺激（tACS）引起的外部振荡扰动而变化。在这里，我们使用了一种新形式的非侵入性脑刺激（NIBS），即千赫兹经颅磁扰动（kTMP），其中通过连续高频载波信号（3.5 kHz）的幅度调制（AM）产生低频扰动。作为一种磁感应方法，kTMP 可以在皮质表面产生比 tACS 更高的电场，并减少皮肤共刺激。人类参与者 (n=40) 在接收 AM 分量为 3.125 Hz 的 kTMP 的同时聆听有节奏的语音序列。
- Keywords: speech, stimulation, perception, perturbation, am-ktmp

### 12. [从青春期到成年过渡期间皮质纹状体回路的神经发育和饮酒风险](https://www.biorxiv.org/content/10.64898/2026.07.15.738690v1)
- Original title: Neurodevelopment of Corticostriatal Circuits and Risk for Alcohol Use During the Transition from Adolescence to Adulthood
- Authors: Petrie, D. J., Parr, A. C., Calabro, F. J., Foran, W., Brown, S. A. et al.
- Meta: 2026-07-19 | neuroscience | DOI: 10.64898/2026.07.15.738690
- 中文摘要: 青春期和成年早期的特点是奖励和决策过程中神经行为的快速发展，与饮酒的开始和升级同时发生。虽然青少年和青年时期开始饮酒并不罕见，但成人的轨迹却有所不同：一些人减少或停止饮酒，而另一些人则升级为更频繁或有问题的模式，导致物质使用障碍。皮质纹状体回路，包括腹侧纹状体（伏隔核；NAcc）和背侧纹状体（尾状核和壳核），支持奖励处理、目标导向行为和习惯形成，并被认为有助于酒精使用的不同阶段。然而，这些回路的规范成熟与饮酒起始和向习惯性消费的转变如何相关仍不清楚。
- Abstract: Adolescence and early adulthood are marked by rapid neurobehavioral development in reward and decision-making processes, coinciding with the initiation and escalation of alcohol use. While adolescent and young adulthood alcohol initiation is not atypical, adult trajectories diverge: some individuals reduce or discontinue use, whereas others escalate to more frequent or problematic patterns leading to substance use d...
- Summary (fallback): 机器翻译摘要显示：青春期和成年早期的特点是奖励和决策过程中神经行为的快速发展，与饮酒的开始和升级同时发生。虽然青少年和青年时期开始饮酒并不罕见，但成人的轨迹却有所不同：一些人减少或停止饮酒，而另一些人则升级为更频繁或有问题的模式，导致物质使用障碍。皮质纹状体回路，包括腹侧纹状体（伏隔核；NAcc）和背侧纹状体（尾状核和壳核），支持奖励处理、目标导向行为和习惯形成，并被认为有助于酒精使用的不同阶段。然而，这些回路的规范成熟与饮酒起始和向习惯性消费的转变如何相关仍不清楚。
- Keywords: alcohol, adulthood, adolescence, initiation, while

### 13. [热诱导珊瑚白化和恢复过程中细胞解析的转录反应](https://www.biorxiv.org/content/10.64898/2026.07.18.739195v1)
- Original title: Cell-resolved transcriptional responses during heat-induced coral bleaching and recovery
- Authors: Grau-Bove, X., Montes-Espuna, L., Ksiezopolska, E., Najle, S. R., Mass, T. et al.
- Meta: 2026-07-19 | genomics | DOI: 10.64898/2026.07.18.739195
- 中文摘要: 珊瑚礁依赖于刺胞动物宿主和光合甲藻之间的细胞内共生，这种共生被海洋变暖破坏，导致珊瑚白化。然而，这些反应在压力和恢复过程中如何分布在珊瑚细胞类型中仍不清楚。在这里，我们生成了造礁珊瑚 Stylophora pistillata 的时间单细胞转录组图谱，对 32°C 下 7 天和恢复 45 天后的 20,000 个细胞进行了分析。热应激降低了共生体丰度和光合作用效率，随后部分恢复。早期的氧化应激、解毒和蛋白质稳态程序让位于线粒体、细胞骨架和囊泡重塑。
- Abstract: Coral reefs depend on an intracellular symbiosis between cnidarian hosts and photosynthetic dinoflagellates that is disrupted by ocean warming, causing coral bleaching. Yet how these responses are distributed across coral cell types during stress and recovery remains unclear. Here, we generate a temporal single-cell transcriptomic atlas of the reef-building coral Stylophora pistillata, profiling 20,000 cells during...
- Summary (fallback): 机器翻译摘要显示：珊瑚礁依赖于刺胞动物宿主和光合甲藻之间的细胞内共生，这种共生被海洋变暖破坏，导致珊瑚白化。然而，这些反应在压力和恢复过程中如何分布在珊瑚细胞类型中仍不清楚。在这里，我们生成了造礁珊瑚 Stylophora pistillata 的时间单细胞转录组图谱，对 32°C 下 7 天和恢复 45 天后的 20,000 个细胞进行了分析。热应激降低了共生体丰度和光合作用效率，随后部分恢复。早期的氧化应激、解毒和蛋白质稳态程序让位于线粒体、细胞骨架和囊泡重塑。
- Keywords: coral, recovery, cells, responses, during

## medrxiv

### 1. [用于预测强迫症深部脑刺激治疗反应的术前脑电图特征](https://www.medrxiv.org/content/10.64898/2026.03.03.26347351v3)
- Original title: A Preoperative Electroencephalography Signature for Predicting Treatment Response to Deep Brain Stimulation in Obsessive-Compulsive Disorder
- Authors: Wang, W., Cheng, J., Zhang, X., Wu, X., Ruan, H. et al.
- Meta: 2026-07-19 | psychiatry and clinical psychology | DOI: 10.64898/2026.03.03.26347351
- 中文摘要: 深部脑刺激（DBS）对难治性强迫症（OCD）有效，但结果参差不齐，无反应者会承受手术和经济负担。我们寻求一种可扩展的、非侵入性的术前 DBS 响应特征。利用来自伏核/内囊 DBS 前肢的随机、双盲、假对照试验（N = 24；NCT04967560）的术前静息态脑电图 (EEG)，我们开发了一种针对小样本的机器学习方法，以确定右额颞电极的较低相对 delta 功率作为六个月症状减轻程度的稳健预测因子，解释了 >40% 的结果方差并提高了响应率超过所有参与者的 20%。
- Abstract: Deep brain stimulation (DBS) is effective for treatment-refractory obsessive-compulsive disorder (OCD), but outcomes are heterogeneous and non-responders incur surgical and financial burden. We sought a scalable, non-invasive preoperative signature of DBS response. Using preoperative resting-state electroencephalography (EEG) from a randomized, double-blind, sham-controlled trial of nucleus accumbens/anterior limb o...
- Summary (fallback): 机器翻译摘要显示：深部脑刺激（DBS）对难治性强迫症（OCD）有效，但结果参差不齐，无反应者会承受手术和经济负担。我们寻求一种可扩展的、非侵入性的术前 DBS 响应特征。利用来自伏核/内囊 DBS 前肢的随机、双盲、假对照试验（N = 24；NCT04967560）的术前静息态脑电图 (EEG)，我们开发了一种针对小样本的机器学习方法，以确定右额颞电极的较低相对 delta 功率作为六个月症状减轻程度的稳健预测因子，解释了 >40% 的结果方差并提高了响应率超过所有参与者的 20%。
- Keywords: signature, preoperative, response, stimulation, electroencephalography
