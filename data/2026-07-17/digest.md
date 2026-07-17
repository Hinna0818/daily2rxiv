# daily2rxiv Digest - 2026-07-17

共收录 90 篇论文。

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
- 中文摘要: 多视图流视频的在线新颖视图合成面临着一个基本的权衡：在严格的实时约束下运行时，维持持久的长视野内存以重建暂时遮挡的区域。虽然测试时训练 (TTT) 提供了强大的记忆机制，但标准模型要求在每一帧进行基于梯度的记忆更新，以适应动态场景中不断变化的运动。大量内存更新的计算成本阻碍了实时应用，并可能导致长上下文中的不稳定。鉴于内存更新比内存申请要求更高，并且视频内容很大程度上是冗余的，我们建议将这两个过程的频率解耦。
- Abstract: Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes...
- Summary (fallback): 机器翻译摘要显示：多视图流视频的在线新颖视图合成面临着一个基本的权衡：在严格的实时约束下运行时，维持持久的长视野内存以重建暂时遮挡的区域。虽然测试时训练 (TTT) 提供了强大的记忆机制，但标准模型要求在每一帧进行基于梯度的记忆更新，以适应动态场景中不断变化的运动。大量内存更新的计算成本阻碍了实时应用，并可能导致长上下文中的不稳定。鉴于内存更新比内存申请要求更高，并且视频内容很大程度上是冗余的，我们建议将这两个过程的频率解耦。
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

### 1. [植物肌动蛋白网络是快速机械适应性支架](https://www.biorxiv.org/content/10.64898/2026.07.16.738884v1)
- Original title: Plant actin networks are rapid mechano-adaptive scaffolds
- Authors: Lamers, J., Daamen, A., Pinto, A., Tauber, J., Gosselink, S. et al.
- Meta: 2026-07-17 | plant biology | DOI: 10.64898/2026.07.16.738884
- 中文摘要: 肌动蛋白细胞骨架是最高度保守的真核结构之一。在动物细胞中，肌动蛋白在机械生物学中发挥着关键作用，作为塑造细胞力学的结构支架和响应机械线索而重组的机械响应网络。在植物中，这些作用通常归因于细胞壁和微管细胞骨架。这使得植物肌动蛋白在机械反应中的作用很大程度上不清楚。在这里，我们想知道动物力学生物学所必需的肌动蛋白关键特征是否也可以在植物中保留。我们使用定量活细胞成像和定量图像分析来表明植物肌动蛋白网络具有快速的机械响应性。我们发现皮质肌动蛋白网络的细胞分布与激光消融引起的细胞变形之间存在定量相关性。
- Abstract: The actin cytoskeleton is among the most highly conserved eukaryotic structures. In animal cells, actin plays a key role in mechanobiology, serving as a structural scaffold that shapes cellular mechanics and a mechanoresponsive network that reorganizes in response to mechanical cues. In plants, these roles are generally attributed to the cell wall and the microtubule cytoskeleton. This leaves the role of plant actin...
- Summary (fallback): 机器翻译摘要显示：肌动蛋白细胞骨架是最高度保守的真核结构之一。在动物细胞中，肌动蛋白在机械生物学中发挥着关键作用，作为塑造细胞力学的结构支架和响应机械线索而重组的机械响应网络。在植物中，这些作用通常归因于细胞壁和微管细胞骨架。这使得植物肌动蛋白在机械反应中的作用很大程度上不清楚。在这里，我们想知道动物力学生物学所必需的肌动蛋白关键特征是否也可以在植物中保留。我们使用定量活细胞成像和定量图像分析来表明植物肌动蛋白网络具有快速的机械响应性。我们发现皮质肌动蛋白网络的细胞分布与激光消融引起的细胞变形之间存在定量相关性。
- Keywords: actin, networks, plant, mechanical, rapid

### 2. [未标记的器官：解剖学和生理学文本中的脂肪组织和规范性](https://www.biorxiv.org/content/10.64898/2026.07.14.736897v1)
- Original title: The Unlabeled Organ: Adipose tissue and normativity in anatomy and physiology texts
- Authors: Hermsmeyer, I. D. K., MacDougald, O. A., Orczykowski, M. E.
- Meta: 2026-07-17 | scientific communication and education | DOI: 10.64898/2026.07.14.736897
- 中文摘要: 脂肪组织是一个动态且重要的器官系统，在新陈代谢、内分泌信号、免疫功能、体温调节和结构支持中发挥作用。尽管如此，它在历史上一直被认为是惰性的或病态的，这引发了人们对它在生物医学教育中如何表现的质疑。我们评估了广泛使用的解剖学、生理学和解剖生理学结合教科书中脂肪组织的视觉和文本表示。对图像的存在、标签和表示程度进行编码，并且在功能上下文中对“脂肪”和“脂肪”的文本提及进行量化。在解剖学教科书中，脂肪组织经常出现（图像的 6.6-21.7%），但很少被标记（所有图像的 <5%；含脂肪图像的 <25%）。
- Abstract: Adipose tissue is a dynamic and essential organ system with roles in metabolism, endocrine signaling, immune function, thermoregulation, and structural support. Despite this, it has historically been framed as inert or pathological, raising questions about how it is represented in biomedical education. We evaluated the visual and textual representation of adipose tissue across widely used anatomy, physiology, and co...
- Summary (fallback): 机器翻译摘要显示：脂肪组织是一个动态且重要的器官系统，在新陈代谢、内分泌信号、免疫功能、体温调节和结构支持中发挥作用。尽管如此，它在历史上一直被认为是惰性的或病态的，这引发了人们对它在生物医学教育中如何表现的质疑。我们评估了广泛使用的解剖学、生理学和解剖生理学结合教科书中脂肪组织的视觉和文本表示。对图像的存在、标签和表示程度进行编码，并且在功能上下文中对“脂肪”和“脂肪”的文本提及进行量化。在解剖学教科书中，脂肪组织经常出现（图像的 6.6-21.7%），但很少被标记（所有图像的 <5%；含脂肪图像的 <25%）。
- Keywords: adipose, tissue, images, organ, across

### 3. [优化富含培养物的混合宏基因组管道以评估厌氧消化物中牲畜粪便的 AMR 足迹](https://www.biorxiv.org/content/10.64898/2026.04.24.720626v2)
- Original title: Optimizing a Culture-Enriched Hybrid Metagenomics Pipeline to Assess the AMR Footprint of Livestock Manure in Anaerobic Digestate
- Authors: Rahman, N., Rahman, A. S. M. Z., Levin, D. B., McAllister, T., Cicek, N. et al.
- Meta: 2026-07-17 | microbiology | DOI: 10.64898/2026.04.24.720626
- 中文摘要: 厌氧消化物作为抗菌素抗性基因 (ARG) 库的程度可能被低估，因为传统的宏基因组学可能不足以代表低丰度决定因素，并且缺乏足够的分辨率来可靠地将 ARG 与移动遗传元件 (MGE) 连接起来。本研究使用混合组装来评估具有或不具有抗菌选择性的培养物富集宏基因组学 (CEMG) 是否可以改善消化物中 ARG 的检测以及 ARG-MGE-宿主连接的表征。培养物富集显着提高了 ARG 回收率：平均 ARG 信号从新鲜消化物（FD；直接宏基因组样本）中的 15.4 CPM 上升至不含抗生素的 CEMG 中的 124 CPM，以及抗生素选择性 CEMG 中的 160.0 CPM，相当于 FD 的约 10.4 倍增加。
- Abstract: The extent that anaerobic digestate acts as a reservoir of antimicrobial resistance genes (ARGs) is likely underestimated as conventional metagenomics may underrepresent low-abundance determinants and lacks sufficient resolution to reliably link ARGs to mobile genetic elements (MGE). This study used hybrid assemblies to evaluate whether culture-enriched metagenomics (CEMG), with and without antimicrobial selectivity...
- Summary (fallback): 机器翻译摘要显示：厌氧消化物作为抗菌素抗性基因 (ARG) 库的程度可能被低估，因为传统的宏基因组学可能不足以代表低丰度决定因素，并且缺乏足够的分辨率来可靠地将 ARG 与移动遗传元件 (MGE) 连接起来。本研究使用混合组装来评估具有或不具有抗菌选择性的培养物富集宏基因组学 (CEMG) 是否可以改善消化物中 ARG 的检测以及 ARG-MGE-宿主连接的表征。培养物富集显着提高了 ARG 回收率：平均 ARG 信号从新鲜消化物（FD；直接宏基因组样本）中的 15.4 CPM 上升至不含抗生素的 CEMG 中的 124 CPM，以及抗生素选择性 CEMG 中的 160.0 CPM，相当于 FD 的约 10.4 倍增加。
- Keywords: args, resistance, hybrid, digestate, enrichment

### 4. [PLA2G6 相关神经变性 (PLAN) 果蝇模型中的线粒体结构和功能缺陷](https://www.biorxiv.org/content/10.64898/2026.02.21.707236v2)
- Original title: Mitochondrial structural and functional defects in the Drosophila melanogaster model of PLA2G6 Associated Neurodegeneration (PLAN)
- Authors: Tasmin, R., Naoshin, A., Matam, D. P., Banerjee, S.
- Meta: 2026-07-17 | cell biology | DOI: 10.64898/2026.02.21.707236
- 中文摘要: PLA2G6 相关神经变性 (PLAN) 是一种罕见的进行性疾病，由 PLA2G6 突变引起，PLA2G6 编码不依赖于钙的磷脂酶 A2，这是一种通过 Lands 循环进行磷脂重塑和膜脂稳态所需的酶。尽管线粒体功能障碍与 PLAN 有关，但 PLA2G6 缺失如何影响跨组织、年龄和性别的线粒体结构和功能仍不清楚。在这里，我们使用纯合无效 iPLA2-VIA 突变体果蝇（一种 PLAN 模型）来检查线粒体超微结构、丰度、功能、DNA 含量和线粒体维持基因表达。透射电子显微镜显示，7 天大和 3 周大的突变果蝇的大脑、胸部和卵巢存在严重的线粒体异常，包括嵴破坏、形态异常和膜结构受损。
- Abstract: PLA2G6-associated neurodegeneration (PLAN) is a rare progressive disorder caused by mutations in PLA2G6, which encodes calcium-independent phospholipase A2, an enzyme required for phospholipid remodeling and membrane lipid homeostasis through the Lands cycle. Although mitochondrial dysfunction has been implicated in PLAN, how PLA2G6 loss affects mitochondrial structure and function across tissues, age, and sex remai...
- Summary (fallback): 机器翻译摘要显示：PLA2G6 相关神经变性 (PLAN) 是一种罕见的进行性疾病，由 PLA2G6 突变引起，PLA2G6 编码不依赖于钙的磷脂酶 A2，这是一种通过 Lands 循环进行磷脂重塑和膜脂稳态所需的酶。尽管线粒体功能障碍与 PLAN 有关，但 PLA2G6 缺失如何影响跨组织、年龄和性别的线粒体结构和功能仍不清楚。在这里，我们使用纯合无效 iPLA2-VIA 突变体果蝇（一种 PLAN 模型）来检查线粒体超微结构、丰度、功能、DNA 含量和线粒体维持基因表达。透射电子显微镜显示，7 天大和 3 周大的突变果蝇的大脑、胸部和卵巢存在严重的线粒体异常，包括嵴破坏、形态异常和膜结构受损。
- Keywords: mitochondrial, reduced, expression, plan, mutants

### 5. [VBIT-4 的膜破坏作用对其作为广泛使用的 VDAC 寡聚抑制剂的作用提出了挑战](https://www.biorxiv.org/content/10.1101/2025.06.30.661942v4)
- Original title: A Membrane-Disruptive Action of VBIT-4 Challenges Its Role as a Widely Used VDAC Oligomerization Inhibitor
- Authors: Ravishankar, V., Borges-Araujo, L., Rajendran, M., Lafargue, E., Byrne, D. et al.
- Meta: 2026-07-17 | biochemistry | DOI: 10.1101/2025.06.30.661942
- 中文摘要: VDAC 是线粒体外膜最丰富的蛋白质，也是代谢物交换和线粒体生理学的关键调节因子。其寡聚化已被提议用于控制线粒体 DNA 释放和膜重塑等过程，但其潜在机制仍不清楚。尽管机制验证有限，但 VBIT-4 在过去十年中已被广泛用作 VDAC1 寡聚化的推定抑制剂。在这里，我们使用高速原子力显微镜直接观察脂质膜中的 VDAC1 组装体并检查 VBIT-4 的效果。出乎意料的是，VBIT-4 在微摩尔浓度下诱导膜缺陷和透化，与 VDAC1 无关。定量 AFM 分析进一步表明 VBIT-4 不会改变 VDAC1 簇组织。
- Abstract: VDAC is the most abundant protein of the mitochondrial outer membrane and a key regulator of metabolite exchange and mitochondrial physiology. Its oligomerization has been proposed to control processes such as mitochondrial DNA release and membrane remodeling, yet the underlying mechanisms remain poorly defined. VBIT-4 has been widely used over the last decade as a putative inhibitor of VDAC1 oligomerization, despit...
- Summary (fallback): 机器翻译摘要显示：VDAC 是线粒体外膜最丰富的蛋白质，也是代谢物交换和线粒体生理学的关键调节因子。其寡聚化已被提议用于控制线粒体 DNA 释放和膜重塑等过程，但其潜在机制仍不清楚。尽管机制验证有限，但 VBIT-4 在过去十年中已被广泛用作 VDAC1 寡聚化的推定抑制剂。在这里，我们使用高速原子力显微镜直接观察脂质膜中的 VDAC1 组装体并检查 VBIT-4 的效果。出乎意料的是，VBIT-4 在微摩尔浓度下诱导膜缺陷和透化，与 VDAC1 无关。定量 AFM 分析进一步表明 VBIT-4 不会改变 VDAC1 簇组织。
- Keywords: vbit-4, membrane, vdac1, oligomerization, inhibitor

### 6. [同代和代际关系发展与协作的纵向 fNIRS 超级扫描数据集](https://www.biorxiv.org/content/10.64898/2026.06.26.734715v2)
- Original title: A longitudinal fNIRS hypercanning dataset of same generation and intergenerational relationship development and collaboration
- Authors: Moffat, R., Cross, E. S.
- Meta: 2026-07-17 | neuroscience | DOI: 10.64898/2026.06.26.734715
- 中文摘要: 社会脱节（即孤独和社会孤立）对健康构成严重风险，在老年人中尤其普遍。定性和行为证据表明，代际社会互动可以通过为成年人提供形成新社会联系的机会来减轻社会脱节，但支撑关系形成的神经生理学和运动学过程仍然知之甚少。本文介绍并验证了 InterGenSynchrony 数据集——一个在 6 个会话项目中获得的纵向、多模态超扫描数据集，其中 30 个同代人和 31 个代际情侣作为陌生人相遇，并通过创意绘画而熟悉。
- Abstract: Social disconnection (i.e., loneliness and social isolation) poses a severe risk to health and is particularly prevalent among older adults. Qualitative and behavioural evidence suggests that intergenerational social interactions can mitigate social disconnection by offering opportunities for adults to form new social connections, yet the neurophysiological and kinematic processes underpinning relationship formation...
- Summary (fallback): 机器翻译摘要显示：社会脱节（即孤独和社会孤立）对健康构成严重风险，在老年人中尤其普遍。定性和行为证据表明，代际社会互动可以通过为成年人提供形成新社会联系的机会来减轻社会脱节，但支撑关系形成的神经生理学和运动学过程仍然知之甚少。本文介绍并验证了 InterGenSynchrony 数据集——一个在 6 个会话项目中获得的纵向、多模态超扫描数据集，其中 30 个同代人和 31 个代际情侣作为陌生人相遇，并通过创意绘画而熟悉。
- Keywords: dataset, social, intergenerational, relationship, behavioural

### 7. [军蚁社会中的社会伤口护理动态](https://www.biorxiv.org/content/10.1101/2025.09.22.677721v2)
- Original title: Social wound care dynamics in an army ant society
- Authors: Lagos-Oviedo, J. J., Rajendra, D., Gokhale, C. S., Schmitt, T., Frank, E. T.
- Meta: 2026-07-17 | zoology | DOI: 10.1101/2025.09.22.677721
- 中文摘要: 受伤和感染对健康构成重大威胁。动物通过自我药疗或接受群体成员的社会护理来应对这个问题。虽然伤口护理在提高生存率方面的好处是显而易见的，但推动这些行为演变的力量尚不完全清楚。目前的假设是，由于个人的相对价值较高，社会伤口护理更有可能在小群体中发展，我们证明群体规模对于其发展或保留来说并不是必要的。相反，我们的理论模型正式阐述了受伤率和致死率如何成为护理的基本驱动因素，而不是群体规模。行军蚁 Eciton burchellii 的伤口护理功能进一步证明了这一点，该物种拥有约 100 万只蚂蚁，捕猎好斗的猎物。
- Abstract: Injuries and infections pose a significant threat to fitness. Animals cope with this problem by performing self-medication or receiving social care from members of the group. While the benefits of wound care in increasing survival are clear, the forces driving the evolution of these behaviours are not fully understood. Contrary to the current hypothesis that social wound care is more likely to evolve in small groups...
- Summary (fallback): 机器翻译摘要显示：受伤和感染对健康构成重大威胁。动物通过自我药疗或接受群体成员的社会护理来应对这个问题。虽然伤口护理在提高生存率方面的好处是显而易见的，但推动这些行为演变的力量尚不完全清楚。目前的假设是，由于个人的相对价值较高，社会伤口护理更有可能在小群体中发展，我们证明群体规模对于其发展或保留来说并不是必要的。相反，我们的理论模型正式阐述了受伤率和致死率如何成为护理的基本驱动因素，而不是群体规模。行军蚁 Eciton burchellii 的伤口护理功能进一步证明了这一点，该物种拥有约 100 万只蚂蚁，捕猎好斗的猎物。
- Keywords: care, wound, social, group, evolution

### 8. [使用 TMEformer 绘制肿瘤微环境依赖性：支持计算机扰动的空间基础框架](https://www.biorxiv.org/content/10.64898/2026.05.17.725770v2)
- Original title: Mapping Tumor-Microenvironment dependencies with TMEformer: A spatial foundation framework enabling in silico perturbation
- Authors: Chen, S., Zhu, G., Yang, L., Wei, X., Li, S. et al.
- Meta: 2026-07-17 | bioinformatics | DOI: 10.64898/2026.05.17.725770
- 中文摘要: 尽管空间背景在驱动肿瘤进展中发挥着重要作用，但当前大多数虚拟扰动的计算模型在很大程度上忽视了它的重要性。在这里，我们介绍 TMEformer，这是一种肿瘤微环境感知深度学习框架，它利用高分辨率空间转录组学，通过明确整合空间架构来联合建模内在肿瘤细胞程序和局部微环境信号。 TMEformer 经过不同肿瘤空间转录组队列的验证，能够实现虚拟扰动，捕获局部细胞生态系统内的功能依赖性。尽管接受了癌症特定空间数据集的训练，但 TMEformer 在捕获关键肿瘤转变（包括谱系可塑性和治疗耐药性的出现）方面优于在大规模语料库上预训练的基线模型。
- Abstract: Despite the fundamental role of spatial context in driving tumor progression, most current computational models for virtual perturbation have largely overlooked its importance. Here, we introduce TMEformer, a tumor microenvironment-aware deep learning framework that leverages high-resolution spatial transcriptomics to jointly model intrinsic tumor cell programs and local microenvironmental signals by explicitly inco...
- Summary (fallback): 机器翻译摘要显示：尽管空间背景在驱动肿瘤进展中发挥着重要作用，但当前大多数虚拟扰动的计算模型在很大程度上忽视了它的重要性。在这里，我们介绍 TMEformer，这是一种肿瘤微环境感知深度学习框架，它利用高分辨率空间转录组学，通过明确整合空间架构来联合建模内在肿瘤细胞程序和局部微环境信号。 TMEformer 经过不同肿瘤空间转录组队列的验证，能够实现虚拟扰动，捕获局部细胞生态系统内的功能依赖性。尽管接受了癌症特定空间数据集的训练，但 TMEformer 在捕获关键肿瘤转变（包括谱系可塑性和治疗耐药性的出现）方面优于在大规模语料库上预训练的基线模型。
- Keywords: spatial, tumor, tmeformer, framework, perturbation

### 9. [所有神经毒素的条件删除定义了神经毒素基本突触组织功能的多样性](https://www.biorxiv.org/content/10.64898/2026.07.15.738748v1)
- Original title: Conditional Deletion of All Neurexins Defines Diversity of Essential Synaptic Organizer Functions for Neurexins
- Authors: Jiang, M., Li, Y., Artyukhova, M., Zhang, L., Luo, S. et al.
- Meta: 2026-07-17 | neuroscience | DOI: 10.64898/2026.07.15.738748
- 中文摘要: 神经毒素可以说是研究最充分的突触前粘附分子。然而，尽管有数千篇论文，但仍无法直接比较不同类型突触中神经毒素的整体功能。十年前，我们提供了这样的分析，但最近我们撤回了这篇论文，因为四张图像包含微重复，尽管对论文的结论没有明显影响，但无法纠正。结果，科学界失去了建立神经毒素在不同类型突触中发挥深刻但独特功能这一基本原理的数据。因此，在本研究中，我们重新分析了原始数据，并通过新实验扩展了他们的结论，以在同一研究中记录神经毒素对多个不同突触的基本贡献。
- Abstract: Neurexins are arguably the best-studied presynaptic adhesion molecules. Despite thousands of papers, however, no direct comparisons of overall neurexin functions in different types of synapses is available. A decade ago, we provided such an analysis but we recently retracted this paper because four images contained microduplications that, although without discernible impact on the paper's conclusions, could not be c...
- Summary (fallback): 机器翻译摘要显示：神经毒素可以说是研究最充分的突触前粘附分子。然而，尽管有数千篇论文，但仍无法直接比较不同类型突触中神经毒素的整体功能。十年前，我们提供了这样的分析，但最近我们撤回了这篇论文，因为四张图像包含微重复，尽管对论文的结论没有明显影响，但无法纠正。结果，科学界失去了建立神经毒素在不同类型突触中发挥深刻但独特功能这一基本原理的数据。因此，在本研究中，我们重新分析了原始数据，并通过新实验扩展了他们的结论，以在同一研究中记录神经毒素对多个不同突触的基本贡献。
- Keywords: synapses, neurexins, different, functions, conditional

### 10. [通过重编程人类神经元自噬增强来逆转年龄依赖性线粒体动力学改变的后遗症和逆转](https://www.biorxiv.org/content/10.1101/2025.10.02.680077v2)
- Original title: Sequelae and reversal of age-dependent alterations in mitochondrial dynamics via autophagy enhancement in reprogrammed human neurons
- Authors: Klinman, E., Kwon, J.-S., Dolle, R. E., Pak, S. C., Silverman, G. A. et al.
- Meta: 2026-07-17 | neuroscience | DOI: 10.1101/2025.10.02.680077
- 中文摘要: 人类神经元的衰老如何影响线粒体和自噬体等重要细胞器的动态仍然很大程度上未知。 MicroRNA 诱导的源自成体成纤维细胞的直接重编程神经元 (miN) 保留了供体的​​年龄相关特征，从而能够研究人类神经元的年龄依赖性特征，包括纵向同基因样本。转录组分析表明，与年轻神经元相比，来自老年人的神经元的特征是与自噬体、溶酶体和线粒体调节相关的基因表达变化。为了在细胞水平上阐明这些变化，我们对不同年龄供体的 miN 中的细胞器进行了活细胞成像。
- Abstract: How aging of human neurons affects dynamics of essential organelle such as mitochondria and autophagosomes remains largely unknown. MicroRNA-induced directly reprogrammed neurons (miNs) derived from adult fibroblasts retain age-associated signatures of the donor, enabling the study of age-dependent features in human neurons, including longitudinal isogenic samples. Transcriptomic analysis revealed that neurons deriv...
- Summary (fallback): 机器翻译摘要显示：人类神经元的衰老如何影响线粒体和自噬体等重要细胞器的动态仍然很大程度上未知。 MicroRNA 诱导的源自成体成纤维细胞的直接重编程神经元 (miN) 保留了供体的​​年龄相关特征，从而能够研究人类神经元的年龄依赖性特征，包括纵向同基因样本。转录组分析表明，与年轻神经元相比，来自老年人的神经元的特征是与自噬体、溶酶体和线粒体调节相关的基因表达变化。为了在细胞水平上阐明这些变化，我们对不同年龄供体的 miN 中的细胞器进行了活细胞成像。
- Keywords: mitochondrial, age-dependent, neurons, lysosomes, fission

### 11. [MEG 信息导航 TMS 用于个性化语音皮质映射](https://www.biorxiv.org/content/10.64898/2026.07.10.737657v2)
- Original title: MEG-informed navigated TMS for individualized speech cortical mapping
- Authors: Autti, S., Korkealaakso, S., Gogulski, J., Engelhardt, M., Vaalto, S. et al.
- Meta: 2026-07-17 | neuroscience | DOI: 10.64898/2026.07.10.737657
- 中文摘要: 通过导航重复经颅磁刺激 (SCM nrTMS) 进行语音皮质映射，为神经外科医生提供有关个体皮质语音网络的非侵入性先验信息。需要个性化映射，因为语音产生的确切位置和激活模式显示出个体之间的高度可变性。我们假设，个人言语产生的脑磁图 (MEG) 数据可以在时间和空间上指导 SCM TMS 过程，从而导致在 MEG 定义的位置（TMS 脉冲时序与 MEG 活动一致）出现更高的错误率。 13 名健康受试者参与了 MEG 和 TMS 测量，其中 TMS 脉冲的时间（PTI；图片到 TMS 间隔）根据个人在图片命名任务中的 MEG 激活进行调整。
- Abstract: Speech cortical mapping by means of navigated repetitive transcranial magnetic stimulation (SCM nrTMS) provides neurosurgeons with noninvasive prior information about individual's cortical speech network. Individualized mapping is required, since the exact locations and activation patterns of speech production show high variability between individuals. We hypothesized that magnetoencephalography (MEG) data of an ind...
- Summary (fallback): 机器翻译摘要显示：通过导航重复经颅磁刺激 (SCM nrTMS) 进行语音皮质映射，为神经外科医生提供有关个体皮质语音网络的非侵入性先验信息。需要个性化映射，因为语音产生的确切位置和激活模式显示出个体之间的高度可变性。我们假设，个人言语产生的脑磁图 (MEG) 数据可以在时间和空间上指导 SCM TMS 过程，从而导致在 MEG 定义的位置（TMS 脉冲时序与 MEG 活动一致）出现更高的错误率。 13 名健康受试者参与了 MEG 和 TMS 测量，其中 TMS 脉冲的时间（PTI；图片到 TMS 间隔）根据个人在图片命名任务中的 MEG 激活进行调整。
- Keywords: speech, individual, activation, error, cortical

### 12. [使用深度注意力网络从细胞轨迹数据推断细胞间相互作用动力学](https://www.biorxiv.org/content/10.64898/2026.07.14.707033v1)
- Original title: Inferring Cell-Cell Interaction Dynamics from Cell Trajectory Data Using Deep Attention Networks
- Authors: Boyle, J., Baker, R. E., Byrne, H. M.
- Meta: 2026-07-17 | cell biology | DOI: 10.64898/2026.07.14.707033
- 中文摘要: 附近细胞之间的相互作用是许多生物系统中细胞运动的关键驱动因素，包括集体细胞迁移和对癌症的免疫反应。然而，以准确且可生物学解释的方式推断给定系统中的相互作用规则仍然是一个挑战。分析细胞间相互作用动力学的一种有价值的实验方法是在一系列延时图像上跟踪单个细胞的位置，在这项工作中，我们提出了一个基于深度注意力网络理论的模型，该模型可以直接从细胞轨迹数据中学习细胞间相互作用如何影响细胞运动。我们的方法不需要关于控制细胞行为的机制的先验假设，使其能够应用于源自多种生物系统的细胞轨迹数据。
- Abstract: Interactions between nearby cells are a key driver of cell movement in many biological systems, including collective cell migration and the immune response to cancer. However, inferring the interaction rules in a given system in a manner that is both accurate and biologically interpretable remains a challenge. A valuable experimental method for analysing cell-cell interaction dynamics is the tracking of individual c...
- Summary (fallback): 机器翻译摘要显示：附近细胞之间的相互作用是许多生物系统中细胞运动的关键驱动因素，包括集体细胞迁移和对癌症的免疫反应。然而，以准确且可生物学解释的方式推断给定系统中的相互作用规则仍然是一个挑战。分析细胞间相互作用动力学的一种有价值的实验方法是在一系列延时图像上跟踪单个细胞的位置，在这项工作中，我们提出了一个基于深度注意力网络理论的模型，该模型可以直接从细胞轨迹数据中学习细胞间相互作用如何影响细胞运动。我们的方法不需要关于控制细胞行为的机制的先验假设，使其能够应用于源自多种生物系统的细胞轨迹数据。
- Keywords: cell, cell-cell, interaction, movement, dynamics

### 13. [连续移植人类 iPSC 衍生的 HSC 的持续表观遗传复兴](https://www.biorxiv.org/content/10.64898/2026.07.15.732710v1)
- Original title: Sustained epigenetic rejuvenation of serially engrafting human iPSC-derived HSCs
- Authors: Jain, A., Li, J., Yu, X., Opejin, A., Yu, D. et al.
- Meta: 2026-07-17 | cell biology | DOI: 10.64898/2026.07.15.732710
- 中文摘要: 造血干细胞（HSC）功能随着年龄的增长而下降，导致免疫衰老和移植结果较差。在这里，我们从多个成年供体中生成了 iPSC 衍生的 HSC (iHSC)，并进行了综合表观遗传、转录、端粒和功能分析，以观察它们是否在分化和连续移植过程中保留了年轻的身份。纵向 DNA 甲基化分析显示，与供体年龄无关，iPSC 中的表观遗传年龄被重置为接近零，并且在分化和移植过程中保持在七岁以下。
- Abstract: Hematopoietic stem cell (HSC) function declines with age, contributing to immunosenescence and inferior transplantation outcomes. Here, we generated iPSC-derived HSCs (iHSCs) from multiple adult donors and performed integrated epigenetic, transcriptional, telomeric, and functional analyses to see if they retain youthful identity across differentiation and serial transplantation. Longitudinal DNA methylation profilin...
- Summary (fallback): 机器翻译摘要显示：造血干细胞（HSC）功能随着年龄的增长而下降，导致免疫衰老和移植结果较差。在这里，我们从多个成年供体中生成了 iPSC 衍生的 HSC (iHSC)，并进行了综合表观遗传、转录、端粒和功能分析，以观察它们是否在分化和连续移植过程中保留了年轻的身份。纵向 DNA 甲基化分析显示，与供体年龄无关，iPSC 中的表观遗传年龄被重置为接近零，并且在分化和移植过程中保持在七岁以下。
- Keywords: epigenetic, hscs, transplantation, hematopoietic, adult

### 14. [内源性自噬体记者揭示了 LGG-1 和 LGG-2 在秀丽隐杆线虫神经元自噬中的冗余和非冗余作用](https://www.biorxiv.org/content/10.64898/2026.07.15.738464v1)
- Original title: Endogenous autophagosome reporters reveal redundant and non-redundant roles of LGG-1 and LGG-2 in C. elegans neuronal autophagy
- Authors: Tsong, H., Rodriguez, M. N., Stavoe, A. K.
- Meta: 2026-07-17 | cell biology | DOI: 10.64898/2026.07.15.738464
- 中文摘要: 自噬是一种保守的细胞回收途径，对于神经元发育和稳态至关重要。神经元是高度极化的细胞，依靠细胞质内容物通过自噬等过程的持续更新来维持细胞功能。在这里，我们采用新型内源自噬体报告基因来定义两种秀丽隐杆线虫 Atg8 直系同源物 LGG-1 和 LGG-2 在神经系统中的不同表达模式、空间分布和补偿潜力。我们用 split wrmNeonGreen 标记 LGG-1 和 LGG-2，以内源性标记单个神经元中的自噬体。我们在泛神经元和单个 AIY 和 NSM 神经元中观察到更亮和更大的 wrmNGsplit:LGG-1 自噬体，相对于更小和更暗的 wrmNGsplit:LGG-2 自噬体。
- Abstract: Autophagy is a conserved cellular recycling pathway essential for neuronal development and homeostasis. Neurons are highly polarized cells that rely on the continual turnover of cytoplasmic content through processes like autophagy to maintain cellular function. Here, we employed novel endogenous autophagosome reporters to define the distinct expression patterns, spatial distribution, and compensatory potential of th...
- Summary (fallback): 机器翻译摘要显示：自噬是一种保守的细胞回收途径，对于神经元发育和稳态至关重要。神经元是高度极化的细胞，依靠细胞质内容物通过自噬等过程的持续更新来维持细胞功能。在这里，我们采用新型内源自噬体报告基因来定义两种秀丽隐杆线虫 Atg8 直系同源物 LGG-1 和 LGG-2 在神经系统中的不同表达模式、空间分布和补偿潜力。我们用 split wrmNeonGreen 标记 LGG-1 和 LGG-2，以内源性标记单个神经元中的自噬体。我们在泛神经元和单个 AIY 和 NSM 神经元中观察到更亮和更大的 wrmNGsplit:LGG-1 自噬体，相对于更小和更暗的 wrmNGsplit:LGG-2 自噬体。
- Keywords: lgg-2, lgg-1, autophagy, autophagosomes, endogenous

### 15. [重建序列语法轨迹可实现可解释和可调的顺式调控元件设计](https://www.biorxiv.org/content/10.64898/2026.07.10.737719v2)
- Original title: Reconstructing sequence-grammar trajectories enables interpretable and tunable cis-regulatory element design
- Authors: Ma, M., Bu, W., Liu, G., Liu, Y., Liu, S. et al.
- Meta: 2026-07-17 | genomics | DOI: 10.64898/2026.07.10.737719
- 中文摘要: 设计具有细胞类型特异性活性的合成顺式调控元件（CRE）对于精准基因和细胞治疗至关重要，但仍然具有挑战性，因为优化通常被视为黑匣子，模糊了调控语法如何出现以及如何纠正失败的轨迹。在这里，我们提出了 GO-CRE（顺式调节元件引导优化），这是一个集成了高效序列生成、预测引导强化学习和轨迹级解释的深度学习框架。 GO-CRE 在共享序列语法景观中重建迭代序列变化，并识别与搜索、承诺和优化相对应的协调更新程序。在 HepG2 中，GO-CRE 揭示了一个低复杂性的 PolyG 陷阱，并通过引入 PolyG 惩罚将优化重定向到功能性基序程序。
- Abstract: Designing synthetic cis-regulatory elements (CREs) with cell-type-specific activity is critical for precision gene and cell therapies, but remains challenging because optimization is often treated as a black box, obscuring how regulatory grammar emerges and how failed trajectories can be corrected. Here, we present GO-CRE (Guided Optimization of Cis-Regulatory Elements), a deep learning framework that integrates eff...
- Summary (fallback): 机器翻译摘要显示：设计具有细胞类型特异性活性的合成顺式调控元件（CRE）对于精准基因和细胞治疗至关重要，但仍然具有挑战性，因为优化通常被视为黑匣子，模糊了调控语法如何出现以及如何纠正失败的轨迹。在这里，我们提出了 GO-CRE（顺式调节元件引导优化），这是一个集成了高效序列生成、预测引导强化学习和轨迹级解释的深度学习框架。 GO-CRE 在共享序列语法景观中重建迭代序列变化，并识别与搜索、承诺和优化相对应的协调更新程序。在 HepG2 中，GO-CRE 揭示了一个低复杂性的 PolyG 陷阱，并通过引入 PolyG 惩罚将优化重定向到功能性基序程序。
- Keywords: optimization, hepg2, sequence-grammar, cis-regulatory, activity

### 16. [分子动力学模拟揭示脂质体中胆固醇浓度与膜曲率之间的相互作用](https://www.biorxiv.org/content/10.64898/2026.07.15.738831v1)
- Original title: Interplay Between Cholesterol Concentration and Membrane Curvature in Liposomes Revealed by Molecular Dynamics Simulations
- Authors: Khodadadi, E., Derakhshani-Molayousefi, M., Khodadadi, E., Moradi, M.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.15.738831
- 中文摘要: 脂质体被广泛用作模型膜和纳米级药物递送系统，其中胆固醇在调节双层结构和动力学中起着关键作用。然而，胆固醇浓度如何影响脂质体的结构和动力学以及这种影响如何依赖于膜曲率在分子水平上尚未完全了解。在这项工作中，利用 MARTINI 力场进行粗粒度分子动力学模拟，研究了由胆固醇和不饱和磷脂（即 DOPC）组成的平面和弯曲膜中胆固醇的浓度依赖性行为。更具体地说，模拟平面脂质双层和大约 50 nm 的脂质体，分别代表小曲率和大曲率的两个极限。
- Abstract: Liposomes are widely used as model membranes and nanoscale drug delivery systems, where cholesterol plays a key role in regulating bilayer structure and dynamics. However, how cholesterol concentration influences the structure and dynamics of liposome and how this influence is dependent on membrane curvature are not fully understood at the molecular level. In this work, coarse-grained molecular dynamics simulations...
- Summary (fallback): 机器翻译摘要显示：脂质体被广泛用作模型膜和纳米级药物递送系统，其中胆固醇在调节双层结构和动力学中起着关键作用。然而，胆固醇浓度如何影响脂质体的结构和动力学以及这种影响如何依赖于膜曲率在分子水平上尚未完全了解。在这项工作中，利用 MARTINI 力场进行粗粒度分子动力学模拟，研究了由胆固醇和不饱和磷脂（即 DOPC）组成的平面和弯曲膜中胆固醇的浓度依赖性行为。更具体地说，模拟平面脂质双层和大约 50 nm 的脂质体，分别代表小曲率和大曲率的两个极限。
- Keywords: cholesterol, curvature, dynamics, concentration, membrane

### 17. [N-聚糖供体的末端糖苷如何影响真核寡糖转移酶的催化效率](https://www.biorxiv.org/content/10.64898/2026.07.16.738906v1)
- Original title: How the terminal glucoside of the N-glycan donor affects the catalytic efficiency of the eukaryotic oligosaccharyltransferase
- Authors: Tropea, B., Fadda, E.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.16.738906
- 中文摘要: 真核寡糖转移酶 (OST) 是一种酶，负责通过将预组装的脂联寡糖 (LLO) 供体转移到 N-x-S/T 共有序列或序列序列中最常见的目标天冬酰胺残基来启动分泌蛋白的 N-糖基化。 OST 优先选择具有独特的糖苷 Glc-(1-2)-Glc-(1-3)-Glc-(1-3)- 封端 A 分支的 LLO 供体。 N-糖基化反应后，在折叠的糖蛋白退出内质网质量控制 (ERQC) 循环之前，该基序从不成熟的 N-聚糖结构中逐步裂解。
- Abstract: The eukaryotic oligosaccharyltransferase (OST) is the enzyme responsible for initiating N-glycosylation of secreted proteins by transferring a pre-assembled lipid-linked oligosaccharide (LLO) donor to target asparagine residues most often found within N-x-S/T consensus sequences, or sequons. OST preferentially selects LLO donors with a distinctive glucoside Glc-(1-2)-Glc-(1-3)-Glc-(1-3)- capping the A-branch. After...
- Summary (fallback): 机器翻译摘要显示：真核寡糖转移酶 (OST) 是一种酶，负责通过将预组装的脂联寡糖 (LLO) 供体转移到 N-x-S/T 共有序列或序列序列中最常见的目标天冬酰胺残基来启动分泌蛋白的 N-糖基化。 OST 优先选择具有独特的糖苷 Glc-(1-2)-Glc-(1-3)-Glc-(1-3)- 封端 A 分支的 LLO 供体。 N-糖基化反应后，在折叠的糖蛋白退出内质网质量控制 (ERQC) 循环之前，该基序从不成熟的 N-聚糖结构中逐步裂解。
- Keywords: glc-, terminal, donor, catalytic, efficiency

### 18. [代谢状态和能量储备共同调节适应性行为控制](https://www.biorxiv.org/content/10.64898/2026.03.22.713499v2)
- Original title: Metabolic state and energy reserves jointly regulate adaptive behavioural control
- Authors: Tittgemeyer, M., Kuzmanovic, B., Melzer, C., Jessen, F., Stephan, K. E. et al.
- Meta: 2026-07-17 | neuroscience | DOI: 10.64898/2026.03.22.713499
- 中文摘要: 动物通过行为控制的灵活调节，不断地使自己的行为适应不断变化的生理需求。然而，能量状态如何塑造人类这种适应性控制的不同组成部分仍然知之甚少。在这里，我们测试了禁食引起的能量不足和储存的能量储备如何共同调节健康参与者的抑制控制和激励动机。禁食选择性地增加了对食物奖励的冲动，这种影响会因体脂百分比而减弱。相比之下，禁食增加了食物和金钱奖励方面的努力支出，揭示了整体动机的增加，最好用相对能量赤字（禁食期间消耗的能量与储存的能量储备的比率）来解释。这两种影响都不能用主观奖励评价的变化来解释。
- Abstract: Animals continuously adapt their behaviour to changing physiological needs through flexible regulation of behavioural control. However, how the energetic state shapes the distinct components of this adaptive control in humans remains poorly understood. Here, we tested how fasting-induced energy deficits and stored energy reserves jointly regulate inhibitory control and incentive motivation in healthy participants. F...
- Summary (fallback): 机器翻译摘要显示：动物通过行为控制的灵活调节，不断地使自己的行为适应不断变化的生理需求。然而，能量状态如何塑造人类这种适应性控制的不同组成部分仍然知之甚少。在这里，我们测试了禁食引起的能量不足和储存的能量储备如何共同调节健康参与者的抑制控制和激励动机。禁食选择性地增加了对食物奖励的冲动，这种影响会因体脂百分比而减弱。相比之下，禁食增加了食物和金钱奖励方面的努力支出，揭示了整体动机的增加，最好用相对能量赤字（禁食期间消耗的能量与储存的能量储备的比率）来解释。这两种影响都不能用主观奖励评价的变化来解释。
- Keywords: energy, control, behavioural, fasting, metabolic

### 19. [蚜虫茎杆表皮蛋白有助于萝卜花叶病毒（Potyvirus）的传播](https://www.biorxiv.org/content/10.64898/2026.03.13.711641v3)
- Original title: Aphid stylin cuticular proteins contribute to turnip mosaic virus (Potyvirus) transmission
- Authors: Fu, Y., Achard, E., Monsion, B., Hoh, F., Le Blaye, S. et al.
- Meta: 2026-07-17 | microbiology | DOI: 10.64898/2026.03.13.711641
- 中文摘要: 数百种植物病毒通过蚜虫载体传播，其中非循环病毒在几秒钟内从一个宿主获得并接种到另一个宿主。这些病毒保留在位于蚜虫口器角质层表面的受体上。马铃薯病毒科的成员是感染植物的最丰富的RNA病毒，它们造成重大的经济损失。其中，马铃薯Y病毒属病毒由蚜虫通过管心丝传播。它们在蚜虫管心中的受体仍然知之甚少。使用芜菁花叶病毒（TuMV，Potyvirus rapae）作为模型，我们开发了互补方法来研究三种媒介物种中马铃薯Y病毒-蚜虫的相互作用。免疫荧光检测和透射电子显微镜显示，蚜虫上颌管心针的远端部分（食道和顶端）都存在 TuMV。
- Abstract: Hundreds of plant viruses are transmitted by aphid vectors, among which non-circulative ones are acquired and inoculated from one host to another within seconds. These viruses are retained on receptors located at the surface of the cuticle of aphid mouthparts. Members of the Potyviridae family are the most abundant RNA viruses infecting plants, and they cause significant economic losses. Among them, viruses of the P...
- Summary (fallback): 机器翻译摘要显示：数百种植物病毒通过蚜虫载体传播，其中非循环病毒在几秒钟内从一个宿主获得并接种到另一个宿主。这些病毒保留在位于蚜虫口器角质层表面的受体上。马铃薯病毒科的成员是感染植物的最丰富的RNA病毒，它们造成重大的经济损失。其中，马铃薯Y病毒属病毒由蚜虫通过管心丝传播。它们在蚜虫管心中的受体仍然知之甚少。使用芜菁花叶病毒（TuMV，Potyvirus rapae）作为模型，我们开发了互补方法来研究三种媒介物种中马铃薯Y病毒-蚜虫的相互作用。免疫荧光检测和透射电子显微镜显示，蚜虫上颌管心针的远端部分（食道和顶端）都存在 TuMV。
- Keywords: aphid, transmission, viruses, tumv, stylin

### 20. [肥厚型梗阻性心肌病中人心脏成纤维细胞的转录组学特征](https://www.biorxiv.org/content/10.64898/2026.07.12.738095v1)
- Original title: Transcriptomic signature of Human Cardiac Fibroblast in Hypertrophic Obstructive Cardiomyopathy
- Authors: Ibrahim, A. M., Halawa, S., Sidarous, L., Galal, A., Elshorbagy, S. et al.
- Meta: 2026-07-17 | cell biology | DOI: 10.64898/2026.07.12.738095
- 中文摘要: 背景：肥厚性心肌病（HCM）是一种以间质纤维化和细胞外基质（ECM）重塑增加为特征的心脏疾病。心脏成纤维细胞 (CF) 在 ECM 重塑以及影响收缩力中发挥着至关重要的作用。越来越多的证据表明 CF 的表型具有疾病特异性。在这里，我们研究了肥厚型梗阻性心肌病 (HOCM) 患者 CF 的转录组特征及其功能意义。方法：从 12 名临床表型 HOCM 患者和 3 名对照的肌切除标本中分离出原发性 CF。从细胞分离物中制备 RNA 文库，用于全转录组测序。使用 Tuxedo 管道进行差异表达分析。
- Abstract: Background: Hypertrophic Cardiomyopathy (HCM) is a cardiac disorder characterized by an increased interstitial fibrosis and Extracellular Matrix (ECM) remodeling. Cardiac fibroblasts (CFs) have a crucial role in ECM remodeling as well as influencing contractility. There is accumulating evidence that the phenotype of CFs is disease-specific. Here, we investigate the transcriptome signature of CFs in Hypertrophic obst...
- Summary (fallback): 机器翻译摘要显示：背景：肥厚性心肌病（HCM）是一种以间质纤维化和细胞外基质（ECM）重塑增加为特征的心脏疾病。心脏成纤维细胞 (CF) 在 ECM 重塑以及影响收缩力中发挥着至关重要的作用。越来越多的证据表明 CF 的表型具有疾病特异性。在这里，我们研究了肥厚型梗阻性心肌病 (HOCM) 患者 CF 的转录组特征及其功能意义。方法：从 12 名临床表型 HOCM 患者和 3 名对照的肌切除标本中分离出原发性 CF。从细胞分离物中制备 RNA 文库，用于全转录组测序。使用 Tuxedo 管道进行差异表达分析。
- Keywords: inflammatory, genes, transcriptome, analysis, identified

### 21. [对大利什曼原虫吡啶核苷酸稳态、氧化还原平衡和毒力至关重要的胞浆苹果酸酶的功能表征](https://www.biorxiv.org/content/10.64898/2026.07.14.735955v1)
- Original title: Functional characterization of a cytosolic malic enzyme crucial for pyridine nucleotide homeostasis, redox balance, and virulence in Leishmania major
- Authors: Pal, A., Modak, D., Khan, F., Mondal, D. K., Gourinath, S. et al.
- Meta: 2026-07-17 | cell biology | DOI: 10.64898/2026.07.14.735955
- 中文摘要: 苹果酸酶 (ME) 占据代谢的中心节点，通过催化苹果酸可逆氧化脱羧为丙酮酸，从而有助于维持 NADPH 稳态。利什曼原虫属已知编码两种 ME 亚型，但迄今为止，只有一种来自大型利什曼原虫的功能被鉴定为线粒体酶，在糖异生中发挥关键作用。在这里，我们克隆了第二种同工型 LmME2，并对其进行了功能表征。共定位和亚细胞分级分析证实 LmME2 定位于细胞质。纯化的 LmME2 的动力学分析揭示了苹果酸脱羧和丙酮酸羧化的速率相当，然而，丙酮酸羧化在寄生虫细胞裂解物中占主导地位，表明反应的方向性在细胞环境中受到代谢调节。
- Abstract: Malic enzymes (MEs) occupy a central node in metabolism, by catalyzing the reversible oxidative decarboxylation of malate to pyruvate, thereby contributing to maintenance of NADPH homeostasis. Leishmania spp. are known to encode two ME isoforms, however only one from Leishmania major has been functionally characterised till date to be a mitochondrial enzyme, playing critical role in gluconeogenesis. Here, we cloned...
- Summary (fallback): 机器翻译摘要显示：苹果酸酶 (ME) 占据代谢的中心节点，通过催化苹果酸可逆氧化脱羧为丙酮酸，从而有助于维持 NADPH 稳态。利什曼原虫属已知编码两种 ME 亚型，但迄今为止，只有一种来自大型利什曼原虫的功能被鉴定为线粒体酶，在糖异生中发挥关键作用。在这里，我们克隆了第二种同工型 LmME2，并对其进行了功能表征。共定位和亚细胞分级分析证实 LmME2 定位于细胞质。纯化的 LmME2 的动力学分析揭示了苹果酸脱羧和丙酮酸羧化的速率相当，然而，丙酮酸羧化在寄生虫细胞裂解物中占主导地位，表明反应的方向性在细胞环境中受到代谢调节。
- Keywords: lmme2, leishmania, cytosolic, malic, enzyme

### 22. [用于碳水化合物和糖蛋白结构预测的聚糖感知扩散模型](https://www.biorxiv.org/content/10.64898/2026.07.16.738959v1)
- Original title: A Glycan-Aware Diffusion Model for Carbohydrate and Glycoprotein Structure Prediction
- Authors: Sundar, K., Yang, H.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.16.738959
- 中文摘要: 生物分子扩散模型现在可以预测蛋白质和异质复合物，但聚糖仍然很困难，因为必须同时捕获它们的分支拓扑、构象灵活性和严格的立体化学规则。我们开发了 SweetFold，这是 Boltz-1x 的聚糖感知改编版，用于游离聚糖、糖蛋白和蛋白质-聚糖复合物的结构预测。 SweetFold 将聚糖表示为假聚合物而不是通用配体，保留单糖特性、异头状态、糖苷连接性和原子级立体化学。我们将这种表示与聚糖特异性结构、立体化学监督和以糖为中心的培训课程结合起来。
- Abstract: Biomolecular diffusion models can now predict proteins and heterogeneous complexes, but glycans remain difficult because their branched topology, conformational flexibility, and strict stereochemical rules must be captured simultaneously. We developed SweetFold, a glycan-aware adaptation of Boltz-1x for the structure prediction of free glycans, glycoproteins, and protein-glycan complexes. SweetFold represents glycan...
- Summary (fallback): 机器翻译摘要显示：生物分子扩散模型现在可以预测蛋白质和异质复合物，但聚糖仍然很困难，因为必须同时捕获它们的分支拓扑、构象灵活性和严格的立体化学规则。我们开发了 SweetFold，这是 Boltz-1x 的聚糖感知改编版，用于游离聚糖、糖蛋白和蛋白质-聚糖复合物的结构预测。 SweetFold 将聚糖表示为假聚合物而不是通用配体，保留单糖特性、异头状态、糖苷连接性和原子级立体化学。我们将这种表示与聚糖特异性结构、立体化学监督和以糖为中心的培训课程结合起来。
- Keywords: diffusion, models, glycans, sweetfold, glycan-aware

### 23. [GW182 沉默结构域与 CNOT1 的三四脯氨酸结合袋结合，将 CNOT1 招募到多蛋白凝聚物中](https://www.biorxiv.org/content/10.64898/2026.07.16.738963v1)
- Original title: GW182 silencing domain engages the tristetraprolin-binding pocket of CNOT1 to recruit CNOT1 into multiprotein condensates
- Authors: Bialobrzewski, M. K., Cieplak-Rotowska, M. K., Michas, A., Staszalek, Z., Sonenberg, N. et al.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.16.738963
- 中文摘要: GW182 通过其 CIM1 区域招募 CCR4-NOT 去腺苷酶复合物，但介导这种相互作用的 CNOT1 表面仍然未知。使用氢-氘交换质谱法，我们将 CIM1 与 CNOT1 残基 800-999 内的疏水沟结合。出乎意料的是，这个凹槽与三四脯氨酸（TTP）结合袋重合。尽管缺乏整体同源性，CIM1 和 C 端 TTP 肽通过共享的 RL(P/{zeta})X{Omega} 序列模式接合该表面，表明聚合进化的短线性基序 (SLiM)。我们进一步表明，使用正交体外测定，GW182沉默结构域（GW182 SD）和TTP竞争CNOT1结合，包括重建的液-液相分离系统，其中GW182 SD充当支架并通过特异性结合招募CNOT1作为客户。
- Abstract: GW182 recruits the CCR4-NOT deadenylase complex through its CIM1 region, yet the CNOT1 surface mediating this interaction has remained unknown. Using hydrogen-deuterium exchange mass spectrometry, we map CIM1 binding to a hydrophobic groove within CNOT1 residues 800-999. Unexpectedly, this groove coincides with the tristetraprolin (TTP)-binding pocket. CIM1 and the C-terminal TTP peptide engage this surface through...
- Summary (fallback): 机器翻译摘要显示：GW182 通过其 CIM1 区域招募 CCR4-NOT 去腺苷酶复合物，但介导这种相互作用的 CNOT1 表面仍然未知。使用氢-氘交换质谱法，我们将 CIM1 与 CNOT1 残基 800-999 内的疏水沟结合。出乎意料的是，这个凹槽与三四脯氨酸（TTP）结合袋重合。尽管缺乏整体同源性，CIM1 和 C 端 TTP 肽通过共享的 RL(P/{zeta})X{Omega} 序列模式接合该表面，表明聚合进化的短线性基序 (SLiM)。我们进一步表明，使用正交体外测定，GW182沉默结构域（GW182 SD）和TTP竞争CNOT1结合，包括重建的液-液相分离系统，其中GW182 SD充当支架并通过特异性结合招募CNOT1作为客户。
- Keywords: cnot1, gw182, binding, silencing, through

### 24. [足细胞足突网络的剪切滞后模型预测驱动渐进性消失的机械反馈回路](https://www.biorxiv.org/content/10.64898/2026.07.15.738799v1)
- Original title: A shear lag model of the podocyte foot process network predicts a mechanical feedback loop driving progressive effacement
- Authors: Bi, M., Jin, H., Puapatanakul, P., Huang, Y., Qu, C. et al.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.15.738799
- 中文摘要: 足细胞足突网络形成肾脏肾小球滤过系统的最后屏障。在机械应力下，该网络很容易受到损伤，足细胞失去与邻居的连接并开始逐渐消失，但控制其机械弹性的因素尚不清楚。我们表明，该网络的构建方式类似于搭接接头：两个主要过程通过叉指足突耦合，这种配置表现为经典的剪力滞系统，力集中在接头端部，并在由几何形状和刚度设置的特征传递长度上衰减。离散网络模型再现了连续剪力滞解，并确定了控制参数之间的层次结构，主要过程的细胞骨架硬化比基底膜刚度更有效地放大足部过程力。
- Abstract: The podocyte foot process network forms the final barrier of the kidney's glomerular filtration system. Under mechanical stress this network is prone to injury in which podocytes lose connectivity to their neighbors and begin the progression toward effacement, but what governs its mechanical resilience is unknown. We show that the network is built like a lap joint: two major processes coupled through interdigitating...
- Summary (fallback): 机器翻译摘要显示：足细胞足突网络形成肾脏肾小球滤过系统的最后屏障。在机械应力下，该网络很容易受到损伤，足细胞失去与邻居的连接并开始逐渐消失，但控制其机械弹性的因素尚不清楚。我们表明，该网络的构建方式类似于搭接接头：两个主要过程通过叉指足突耦合，这种配置表现为经典的剪力滞系统，力集中在接头端部，并在由几何形状和刚度设置的特征传递长度上衰减。离散网络模型再现了连续剪力滞解，并确定了控制参数之间的层次结构，主要过程的细胞骨架硬化比基底膜刚度更有效地放大足部过程力。
- Keywords: foot, process, network, model, mechanical

### 25. [用于区分 3T 时羟基磷灰石和草酸钙乳房钙化的定量磁敏图：一项模型研究](https://www.biorxiv.org/content/10.64898/2026.07.15.738683v1)
- Original title: Quantitative Susceptibility Mapping for Differentiating Hydroxyapatite and Calcium Oxalate Breast Calcifications at 3T: A Phantom Study
- Authors: Misak, K., De Vita, E., Clark, C. A., Cashmore, M. T., Walker-Samuel, S.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.15.738683
- 中文摘要: 目的：乳腺微钙化会引发 70-80% 不必要的活检，因为目前的成像技术无法区分恶性肿瘤相关的羟基磷灰石 (HA) 和良性相关的草酸钙 (CaOx)。定量磁化率图 (QSM) 可以利用这些矿物质之间的磁化率对比（HA：{Delta}{chi} {约} -7 ppm；CaOx：{Delta}{chi} {约} -1 ppm，相对于水），但没有研究证明临床场强下的成分差异。这项工作使用模拟组织模型评估了 3 T 下微钙化分化的敏感性和 R2* 弛豫率图。
- Abstract: Purpose: Breast microcalcifications trigger 70-80% of unnecessary biopsies because current imaging cannot distinguish malignancy-associated hydroxyapatite (HA) from benign-associated calcium oxalate (CaOx). Quantitative susceptibility mapping (QSM) could exploit the susceptibility contrast between these minerals (HA: {Delta}{chi} {approx} -7 ppm; CaOx: {Delta}{chi} {approx} -1 ppm relative to water), but no study ha...
- Summary (fallback): 机器翻译摘要显示：目的：乳腺微钙化会引发 70-80% 不必要的活检，因为目前的成像技术无法区分恶性肿瘤相关的羟基磷灰石 (HA) 和良性相关的草酸钙 (CaOx)。定量磁化率图 (QSM) 可以利用这些矿物质之间的磁化率对比（HA：{Delta}{chi} {约} -7 ppm；CaOx：{Delta}{chi} {约} -1 ppm，相对于水），但没有研究证明临床场强下的成分差异。这项工作使用模拟组织模型评估了 3 T 下微钙化分化的敏感性和 R2* 弛豫率图。
- Keywords: caox, susceptibility, mapping, phantom, delta

### 26. [几何衍生的哈密顿组织区分了循环生物 Fe S 结构](https://www.biorxiv.org/content/10.64898/2026.07.16.739031v1)
- Original title: Geometry derived Hamiltonian organization distinguishes recurrent biological Fe S architectures
- Authors: Sung, J.-Y., Cheong, J.-H.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.16.739031
- 中文摘要: 铁硫 (Fe S) 簇是最古老的生物辅助因子之一，但与特定 Fe S 结构的循环生物利用相关的物理性质仍不清楚。在这里，我们使用集成框架分析了 2,404 个实验解析的 Fe S 团簇，该框架结合了结构几何、几何导出的有效耦合网络鲁棒性和粗粒度开放系统量子传输模拟。我们表明，4Fe 4S 簇占据了结构描述符空间的紧凑且部分不同的区域，其特征是几何畸变低、几何衍生的网络鲁棒性提高以及可用结构数据集中的广泛分类表示。
- Abstract: Iron sulfur (Fe S) clusters are among the most ancient biological cofactors, yet the physical properties associated with the recurrent biological utilization of specific Fe S architectures remain unclear. Here, we analyzed 2,404 experimentally resolved Fe S clusters using an integrated framework combining structural geometry, geometry derived effective coupling network robustness, and coarse-grained open-system quan...
- Summary (fallback): 机器翻译摘要显示：铁硫 (Fe S) 簇是最古老的生物辅助因子之一，但与特定 Fe S 结构的循环生物利用相关的物理性质仍不清楚。在这里，我们使用集成框架分析了 2,404 个实验解析的 Fe S 团簇，该框架结合了结构几何、几何导出的有效耦合网络鲁棒性和粗粒度开放系统量子传输模拟。我们表明，4Fe 4S 簇占据了结构描述符空间的紧凑且部分不同的区域，其特征是几何畸变低、几何衍生的网络鲁棒性提高以及可用结构数据集中的广泛分类表示。
- Keywords: geometry, derived, hamiltonian, organization, biological

### 27. [无调摇摆：托卡伊壁虎基底乳头对声音的离体和体内反应](https://www.biorxiv.org/content/10.64898/2026.07.16.738899v1)
- Original title: Rocking Without a Tune: Ex vivo and in vivo Responses to Sound in the Basilar Papilla of the Tokay Gecko
- Authors: Frost, B. L., Vazquez, Y., Horii, K., Fabella, B. A., Hudspeth, A. J.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.16.738899
- 中文摘要: 与哺乳动物一样，一些爬行动物在高频下具有敏感的频率选择性听觉。两组都在内耳内使用位置频率图来编码声音刺激，但他们实现耳蜗神经激活的机制被认为是不同的。为了研究爬行动物听觉的机械起源，我们测量了托卡伊壁虎（Gekko gecko）听觉器官（称为基底乳头）的声音诱发位移反应。使用光学相干断层扫描，我们能够解决体内和离体整个器官的亚纳米级振动。我们发现器官内任何位置的组织尺度力学中都不存在调谐；相反，它表现出未经调整的旋转运动。
- Abstract: Like mammals, some reptiles possess sensitive and frequency-selective hearing at high frequencies. Both groups employ a place-frequency map within the inner ear to encode sound stimuli, but the mechanisms by which they achieve tuned nerve activation along the cochlea are believed to be distinct. To investigate the mechanical origins of auditory sensation in the reptiles, we measured sound-evoked displacement respons...
- Summary (fallback): 机器翻译摘要显示：与哺乳动物一样，一些爬行动物在高频下具有敏感的频率选择性听觉。两组都在内耳内使用位置频率图来编码声音刺激，但他们实现耳蜗神经激活的机制被认为是不同的。为了研究爬行动物听觉的机械起源，我们测量了托卡伊壁虎（Gekko gecko）听觉器官（称为基底乳头）的声音诱发位移反应。使用光学相干断层扫描，我们能够解决体内和离体整个器官的亚纳米级振动。我们发现器官内任何位置的组织尺度力学中都不存在调谐；相反，它表现出未经调整的旋转运动。
- Keywords: vivo, gecko, tokay, organ, responses

### 28. [多体量子渗流通过纳米限制 Fo 电机维持欧姆质子通量](https://www.biorxiv.org/content/10.64898/2026.07.15.738743v1)
- Original title: Many-body quantum percolation sustains ohmic proton flux through the nanoconfined Fo motor
- Authors: Adeniran, I., Lightfoot, A. P.
- Meta: 2026-07-17 | biophysics | DOI: 10.64898/2026.07.15.738743
- 中文摘要: FoF1-ATP 合酶通过使质子穿过线粒体内膜来驱动细胞生物能。我们最近证明，脂质心磷脂充当二维天线，主动将质子输送到纳米限制的 F_o 电机中，并实施严重的“维度挤压”。这种一维纳米限制迫使质子如此接近，以至于它们的水合壳在物理上重叠，理论上产生无限的经典空间僵局。然而，经验测量表明 F_o 电机的运行效率约为 90%，并表现出无障碍欧姆电导，呈现出生物物理悖论。
- Abstract: The FoF1-ATP synthase drives cellular bioenergetics by translocating protons across the inner mitochondrial membrane. We recently demonstrated that the lipid cardiolipin acts as a 2D antenna, actively funnelling protons into the nanoconfined F_o motor and enforcing severe "dimensional squeezing". This 1D nanoconfinement forces protons into such close proximity that their hydration shells physically overlap, theoreti...
- Summary (fallback): 机器翻译摘要显示：FoF1-ATP 合酶通过使质子穿过线粒体内膜来驱动细胞生物能。我们最近证明，脂质心磷脂充当二维天线，主动将质子输送到纳米限制的 F_o 电机中，并实施严重的“维度挤压”。这种一维纳米限制迫使质子如此接近，以至于它们的水合壳在物理上重叠，理论上产生无限的经典空间僵局。然而，经验测量表明 F_o 电机的运行效率约为 90%，并表现出无障碍欧姆电导，呈现出生物物理悖论。
- Keywords: classical, quantum, motor, protons, steric

### 29. [泛癌 NET 相关的免疫血栓耦合确定了中性粒细胞相关但中性粒细胞不可还原的肿瘤生态](https://www.biorxiv.org/content/10.64898/2026.07.14.738403v1)
- Original title: Pan-cancer NET-associated immunothrombosis coupling identifies a neutrophil-linked but neutrophil-irreducible tumor ecology
- Authors: Zhang, L.
- Meta: 2026-07-17 | cancer biology | DOI: 10.64898/2026.07.14.738403
- 中文摘要: 背景：中性粒细胞胞外陷阱（NET）将先天免疫与血栓形成、转移和免疫逃逸联系起来，但大块肿瘤的 NET 相关特征可能主要报告中性粒细胞丰度。我们测试了既定的 NET 评分是否也能捕捉中性粒细胞不可还原的肿瘤生态。方法：我们重新分析了已发表的 32 种癌症类型的 9,496 个 TCGA 肿瘤的 19 基因 NET 评分。肿瘤分层相关性映射了 Hallmark 和定制免疫血栓形成模块。在每种癌症类型中，分数根据策划的中性粒细胞代理进行残差，并分为四个中值定义的生态象限。临床生存率和两个独立的免疫检查点封锁队列提供了结果背景。
- Abstract: Background: Neutrophil extracellular traps (NETs) connect innate immunity with thrombosis, metastasis and immune escape, but bulk-tumor NET-associated signatures may mainly report neutrophil abundance. We tested whether an established NETs score also captures a neutrophil-irreducible tumor ecology. Methods: We reanalysed a published 19-gene NETs score in 9,496 TCGA tumors across 32 cancer types. Tumor-stratified cor...
- Summary (fallback): 机器翻译摘要显示：背景：中性粒细胞胞外陷阱（NET）将先天免疫与血栓形成、转移和免疫逃逸联系起来，但大块肿瘤的 NET 相关特征可能主要报告中性粒细胞丰度。我们测试了既定的 NET 评分是否也能捕捉中性粒细胞不可还原的肿瘤生态。方法：我们重新分析了已发表的 32 种癌症类型的 9,496 个 TCGA 肿瘤的 19 基因 NET 评分。肿瘤分层相关性映射了 Hallmark 和定制免疫血栓形成模块。在每种癌症类型中，分数根据策划的中性粒细胞代理进行残差，并分为四个中值定义的生态象限。临床生存率和两个独立的免疫检查点封锁队列提供了结果背景。
- Keywords: nets, score, neutrophil, median, tumor

### 30. [色彩对比预测自然搜索任务中的人类目标检测](https://www.biorxiv.org/content/10.64898/2026.07.11.737926v1)
- Original title: Chromatic contrasts predict human target detection in a natural search task
- Authors: White, T. E., Rojas, B., Mappes, J., Kemp, D. J.
- Meta: 2026-07-17 | animal behavior and cognition | DOI: 10.64898/2026.07.11.737926
- 中文摘要: 自然场景在视觉上非常复杂，颜色和亮度的动态变化给检测显着物体带来了挑战。然而，在这种自然条件下指导人类检测的线索在很大程度上仍未经过测试。我们将定制的彩色目标放置在类似森林的环境中，并使用人类视觉模型量化它们与自然背景的对比度。在人类观察者 (n = 51) 中，检测性能随着色调和饱和度对比度的提高而急剧上升，而长期以来被认为是视觉搜索的主要驱动因素的亮度对比度几乎没有提供解释力。引人注目的是，尽管栖息地的照明不均匀，但即使环境光色度发生巨大变化也几乎不会改变检测结果。
- Abstract: Natural scenes are visually complex, with dynamic variation in colour and luminance presenting challenges for detecting salient objects. However, the cues guiding human detection under such natural conditions remain largely untested. We placed custom-built coloured targets in a forest-like setting and quantified their contrasts against natural backgrounds using human visual models. Across human observers (n = 51) de...
- Summary (fallback): 机器翻译摘要显示：自然场景在视觉上非常复杂，颜色和亮度的动态变化给检测显着物体带来了挑战。然而，在这种自然条件下指导人类检测的线索在很大程度上仍未经过测试。我们将定制的彩色目标放置在类似森林的环境中，并使用人类视觉模型量化它们与自然背景的对比度。在人类观察者 (n = 51) 中，检测性能随着色调和饱和度对比度的提高而急剧上升，而长期以来被认为是视觉搜索的主要驱动因素的亮度对比度几乎没有提供解释力。引人注目的是，尽管栖息地的照明不均匀，但即使环境光色度发生巨大变化也几乎不会改变检测结果。
- Keywords: human, detection, natural, contrasts, luminance

## medrxiv

### 1. [2020-2025 年加纳蛇咬伤的时空模式：全国监测分析](https://www.medrxiv.org/content/10.64898/2026.07.12.26357875v1)
- Original title: Temporal and Spatial Patterns of Snakebite Envenoming in Ghana, 2020-2025: A Nationwide Surveillance Analysis
- Authors: Nyarko, E., Antwi, P., Amponsah, E. B., Ofori-Boadu, L., Oduro-Mensah, E. et al.
- Meta: 2026-07-16 | epidemiology | DOI: 10.64898/2026.07.12.26357875
- 中文摘要: 蛇咬伤是一种被忽视的主要热带疾病，对撒哈拉以南非洲的农村人口影响尤为严重。在加纳，有关风险时空分布的证据仍然有限，限制了有针对性的预防和资源分配。这项研究量化了加纳各地区的蛇咬伤风险，确定了持续存在的热点和环境驱动因素，并评估了蛇咬伤负担与获得治疗的地理机会之间的关系。使用贝叶斯时空模型分析了加纳地区卫生信息管理系统（2020 年至 2025 年）的每月地区级蛇咬伤病例，该模型结合了空间效应、时间随机效应和时空相互作用，并通过集成嵌套拉普拉斯逼近进行拟合。
- Abstract: Snakebite envenoming is a major neglected tropical disease disproportionately affecting rural populations in sub-Saharan Africa. In Ghana, evidence on the spatial and temporal distribution of risk remains limited, constraining targeted prevention and resource allocation. This study quantified district-level snakebite risk across Ghana, identified persistent hotspots and environmental drivers, and evaluated the relat...
- Summary (fallback): 机器翻译摘要显示：蛇咬伤是一种被忽视的主要热带疾病，对撒哈拉以南非洲的农村人口影响尤为严重。在加纳，有关风险时空分布的证据仍然有限，限制了有针对性的预防和资源分配。这项研究量化了加纳各地区的蛇咬伤风险，确定了持续存在的热点和环境驱动因素，并评估了蛇咬伤负担与获得治疗的地理机会之间的关系。使用贝叶斯时空模型分析了加纳地区卫生信息管理系统（2020 年至 2025 年）的每月地区级蛇咬伤病例，该模型结合了空间效应、时间随机效应和时空相互作用，并通过集成嵌套拉普拉斯逼近进行拟合。
- Keywords: risk, snakebite, temporal, spatial, east

### 2. [单细胞基因程序定义肾细胞癌的亚型身份和转移轨迹](https://www.medrxiv.org/content/10.64898/2026.07.14.26357682v1)
- Original title: Single-cell gene programs define subtype identity and metastatic trajectories in renal cell carcinoma
- Authors: Madrigal, A., Kim, M., Mehrjoo, Z., Nishimura, T., Saatci, O. et al.
- Meta: 2026-07-16 | genetic and genomic medicine | DOI: 10.64898/2026.07.14.26357682
- 中文摘要: 虽然肾细胞癌 (RCC) 中广泛的细胞异质性与不同的临床结果相关，但我们对这种多样性的理解仅限于由克隆模式或典型途径活性驱动的那些。在这里，我们展示了来自原发性和转移性肿瘤以及四种 RCC 亚型的患者衍生模型的超过 85,000 个单细胞基因表达谱的概要，其中包括罕见的透明细胞乳头状肾细胞肿瘤，我们发现这些肿瘤经常被错误分类，因此我们将 CASP14 确定为高度敏感和特异性的生物标志物。
- Abstract: While extensive cellular heterogeneity in renal cell carcinomas (RCC) is linked to diverse clinical outcomes, our understanding of this diversity is limited to those driven by clonal patterns or activity of canonical pathways. Here, we present a compendium of over 85,000 single-cell gene expression profiles from primary and metastatic tumors as well as patient-derived models across four RCC subtypes, including the r...
- Summary (fallback): 机器翻译摘要显示：虽然肾细胞癌 (RCC) 中广泛的细胞异质性与不同的临床结果相关，但我们对这种多样性的理解仅限于由克隆模式或典型途径活性驱动的那些。在这里，我们展示了来自原发性和转移性肿瘤以及四种 RCC 亚型的患者衍生模型的超过 85,000 个单细胞基因表达谱的概要，其中包括罕见的透明细胞乳头状肾细胞肿瘤，我们发现这些肿瘤经常被错误分类，因此我们将 CASP14 确定为高度敏感和特异性的生物标志物。
- Keywords: cell, programs, metastatic, tumors, gene

### 3. [第 8 周了解什么：预测 6 个月的 GLP-1 结果](https://www.medrxiv.org/content/10.64898/2026.07.14.26357506v1)
- Original title: What Week 8 Knows: Forecasting Six-Month GLP-1 Outcomes
- Authors: Erly, B., Raja, S.
- Meta: 2026-07-16 | health informatics | DOI: 10.64898/2026.07.14.26357506
- 中文摘要: 背景。接受 GLP-1 药物治疗的患者体重减轻量差异很大，而且大多数已发表的预测模型仅包括完成六个月治疗的患者。这种设计忽略了所有较早脱离的人，这是该群体中的大多数。我们构建了一个工具，其中包括在第 8 周就诊时脱离接触并提供有用预测的患者，临床决策实际上是在该处做出的。方法。从参加美国远程医疗 GLP-1 计划的 237,800 名成年人开始，我们需要记录第 8 周的体重、补充确认的剂量和报告的种族，得出 22,538 人的分析队列。我们回答了三个问题：患者六个月内体重减轻的可能性以及我们对此的信心；六个月前辍学的概率；当减肥停滞不前时。
- Abstract: Background. Patients on GLP-1 medications lose very different amounts of weight, and most published prediction models include only patients who complete six months. That design omits everyone who disengages earlier, which is the majority of the cohort. We built a tool that includes patients who disengage and delivers useful predictions at the week-8 visit, where the clinical decision is actually made. Methods. Begin...
- Summary (fallback): 机器翻译摘要显示：背景。接受 GLP-1 药物治疗的患者体重减轻量差异很大，而且大多数已发表的预测模型仅包括完成六个月治疗的患者。这种设计忽略了所有较早脱离的人，这是该群体中的大多数。我们构建了一个工具，其中包括在第 8 周就诊时脱离接触并提供有用预测的患者，临床决策实际上是在该处做出的。方法。从参加美国远程医疗 GLP-1 计划的 237,800 名成年人开始，我们需要记录第 8 周的体重、补充确认的剂量和报告的种族，得出 22,538 人的分析队列。我们回答了三个问题：患者六个月内体重减轻的可能性以及我们对此的信心；六个月前辍学的概率；当减肥停滞不前时。
- Keywords: patients, weight, decision, week-8, six-month

### 4. [MedSafe-Dx (v0)：用于评估临床诊断决策支持中法学硕士的以安全为中心的基准](https://www.medrxiv.org/content/10.64898/2026.04.14.26350711v3)
- Original title: MedSafe-Dx (v0): A Safety-Focused Benchmark for Evaluating LLMs in Clinical Diagnostic Decision Support
- Authors: Van Oyen, C., Mirza-Haq, N.
- Meta: 2026-07-16 | health informatics | DOI: 10.64898/2026.04.14.26350711
- 中文摘要: MedSafe-Dx (v0) 引入了一个以安全为中心的基准，用于使用 DDx Plus 数据集的过滤子集 (N=250) 评估临床诊断决策支持中的大型语言模型。 MedSafe-Dx 评估三个维度：升级敏感性、避免虚假保证以及校准不确定性。模型的任务是提供排名差异 (ICD-10)、升级决策（紧急与常规）和置信标志。我们采用分诊成功率（TSR）作为主要排名指标，定义为安全案例数量减去不必要的升级，除以案例总数（N）。安全通过率 (SPR) 保留为辅助指标，用于隔离三种硬故障模式：错过升级、过度自信的错误诊断和不安全的保证。对 12 名前沿法学硕士进行了评估。
- Abstract: MedSafe-Dx (v0) introduces a safety-focused benchmark for evaluating large language models in clinical diagnostic decision support using a filtered subset of the DDx Plus dataset (N=250). MedSafe-Dx evaluates three dimensions: escalation sensitivity, avoidance of false reassurance, and calibration of uncertainty. Models were tasked with providing a ranked differential (ICD-10), an escalation decision (Urgent vs. Rou...
- Summary (fallback): 机器翻译摘要显示：MedSafe-Dx (v0) 引入了一个以安全为中心的基准，用于使用 DDx Plus 数据集的过滤子集 (N=250) 评估临床诊断决策支持中的大型语言模型。 MedSafe-Dx 评估三个维度：升级敏感性、避免虚假保证以及校准不确定性。模型的任务是提供排名差异 (ICD-10)、升级决策（紧急与常规）和置信标志。我们采用分诊成功率（TSR）作为主要排名指标，定义为安全案例数量减去不必要的升级，除以案例总数（N）。安全通过率 (SPR) 保留为辅助指标，用于隔离三种硬故障模式：错过升级、过度自信的错误诊断和不安全的保证。对 12 名前沿法学硕士进行了评估。
- Keywords: clinical, safety, medsafe-dx, llms, decision

### 5. [原发性醛固酮增多症的醛固酮抑制测试和亚型预测](https://www.medrxiv.org/content/10.64898/2026.05.14.26353176v2)
- Original title: Aldosterone Suppression Testing and Subtype Prediction for Primary Aldosteronism
- Authors: Payanundana, M., Parksook, W. W., Piyanirun, K., Charunvarakornchai, D., Siriwan, C. et al.
- Meta: 2026-07-16 | endocrinology | DOI: 10.64898/2026.05.14.26353176
- 中文摘要: 目的：使用以下方法评估预测 PA 亚型的准确性：1) 2025 年内分泌学会原发性醛固酮增多症 (PA) 指南认可的分类为“高”、“中”和“低”侧化概率； 2) 坐位盐水抑制试验（SST）结果。设计：一项多中心、回顾性队列研究方法：在来自泰国曼谷两个大型三级中心的 319 名 PA 患者队列中评估了指南认可的 PA 亚型分型概率框架的辨别能力，这些患者无论概率状态如何都接受了亚型分型评估。 PA 亚型是通过肾上腺静脉取样 (AVS) 和/或使用 PASO 标准的肾上腺切除术后结果来确定的。
- Abstract: Objectives: To evaluate the accuracy of predicting PA subtype using: 1) the 2025 Endocrine Society primary aldosteronism (PA) guideline-endorsed classification to "high," "intermediate," and "low" probabilities of lateralization; and 2) the seated saline suppression test (SST) results. Design: A multicenter, retrospective, cohort study Methods: The discriminatory capacity of guideline-endorsed probability frameworks...
- Summary (fallback): 机器翻译摘要显示：目的：使用以下方法评估预测 PA 亚型的准确性：1) 2025 年内分泌学会原发性醛固酮增多症 (PA) 指南认可的分类为“高”、“中”和“低”侧化概率； 2) 坐位盐水抑制试验（SST）结果。设计：一项多中心、回顾性队列研究方法：在来自泰国曼谷两个大型三级中心的 319 名 PA 患者队列中评估了指南认可的 PA 亚型分型概率框架的辨别能力，这些患者无论概率状态如何都接受了亚型分型评估。 PA 亚型是通过肾上腺静脉取样 (AVS) 和/或使用 PASO 标准的肾上腺切除术后结果来确定的。
- Keywords: probability, lateralizing, patients, subtype, guideline-endorsed

### 6. [全球癌症更新计划 (CUP Global) 中将软饮料消费与特定地点癌症风险联系起来的生物过程](https://www.medrxiv.org/content/10.64898/2026.07.13.26356051v1)
- Original title: Biological processes linking soft drink consumption with site-specific cancer risk within the Global Cancer Update Programme (CUP Global)
- Authors: Fontvieille, E., Ahmadi, N., Mahamat-saleh, Y., Hashem, N., Lauby-Secretan, B. et al.
- Meta: 2026-07-16 | epidemiology | DOI: 10.64898/2026.07.13.26356051
- 中文摘要: 本综述评估了全球癌症更新计划 (CUP Global) 框架内将软饮料消费与多种癌症风险联系起来的生物学途径。软饮料的消费与多种癌症的风险增加有关，并且葡萄糖或胰岛素失调被认为是潜在的潜在机制。我们应用了三阶段框架。在第一阶段，我们结合专家知识和基于网络的文本挖掘工具，将胰岛素敏感性确定为可能将软饮料消费（加糖或人工加糖）与癌症风险联系起来的关键生物过程，并将葡萄糖相关和胰岛素相关生物标志物作为潜在的中间表型。
- Abstract: This review evaluates the biological pathways linking soft drink consumption with the risk of several cancers within the framework of the Global Cancer Update Programme (CUP Global). Soft drink consumption has been associated with increased risk of multiple cancers, and glucose or insulin dysregulation has been proposed as a potential underlying mechanism. We applied a three-stage framework. In the first stage, we i...
- Summary (fallback): 机器翻译摘要显示：本综述评估了全球癌症更新计划 (CUP Global) 框架内将软饮料消费与多种癌症风险联系起来的生物学途径。软饮料的消费与多种癌症的风险增加有关，并且葡萄糖或胰岛素失调被认为是潜在的潜在机制。我们应用了三阶段框架。在第一阶段，我们结合专家知识和基于网络的文本挖掘工具，将胰岛素敏感性确定为可能将软饮料消费（加糖或人工加糖）与癌症风险联系起来的关键生物过程，并将葡萄糖相关和胰岛素相关生物标志物作为潜在的中间表型。
- Keywords: consumption, risk, soft, cancer, linking

### 7. [艾滋病毒感染者的孤独感和邻里稳定轨迹与抑郁、酗酒和药物滥用以及生活质量之间的关系](https://www.medrxiv.org/content/10.64898/2026.07.14.26358061v1)
- Original title: Associations of Trajectories of Loneliness and Neighborhood Stability with Depression, Alcohol and Substance Use, and Quality of Life among Women Living with HIV
- Authors: Barr, P. B., Edmonds, A., Aouizerat, B., Cohen, M., Cook, J. A. et al.
- Meta: 2026-07-16 | epidemiology | DOI: 10.64898/2026.07.14.26358061
- 中文摘要: 社会关系是健康的重要社会决定因素。孤独是人们对现实关系和理想关系之间的感知差距，它已成为社会关系影响健康的重要机制。与其他与健康相关的个人内部因素一样，孤独感受到更广泛的社会和结构因素的影响，包括邻里社会环境的特征。尽管已经确定了邻里层面的孤独感和心理健康的保护因素和风险因素，但之前的研究往往只关注自我报告的对邻里环境的看法。此外，很少有人考虑独立于社区社会经济条件的社区社会环境的各个方面，例如社区稳定性（即具有长期或短期居民的社区的稳定性）。
- Abstract: Social relationships are an important social determinant of health. Loneliness, the perceived gap between one's actual and desired relationships, has emerged as an important mechanism through which social relationships impact health. Like other intrapersonal-level factors associated with health, loneliness is influenced by broader social and structural factors, including characteristics of one's neighborhood social...
- Summary (fallback): 机器翻译摘要显示：社会关系是健康的重要社会决定因素。孤独是人们对现实关系和理想关系之间的感知差距，它已成为社会关系影响健康的重要机制。与其他与健康相关的个人内部因素一样，孤独感受到更广泛的社会和结构因素的影响，包括邻里社会环境的特征。尽管已经确定了邻里层面的孤独感和心理健康的保护因素和风险因素，但之前的研究往往只关注自我报告的对邻里环境的看法。此外，很少有人考虑独立于社区社会经济条件的社区社会环境的各个方面，例如社区稳定性（即具有长期或短期居民的社区的稳定性）。
- Keywords: loneliness, neighborhood, stability, health, social

### 8. [在呼吸队列研究中使用自动提取的常规临床数据的可行性：SPHN-SPAC 演示项目。](https://www.medrxiv.org/content/10.64898/2026.07.14.26357927v1)
- Original title: Feasibility of using automatically extracted routine clinical data in a respiratory cohort study: The SPHN-SPAC demonstrator project.
- Authors: Romero, F., Sasaki, M., Mallet, M. C., Pedersen, E. S. L., Leuenberger, L. M. et al.
- Meta: 2026-07-16 | epidemiology | DOI: 10.64898/2026.07.14.26357927
- 中文摘要: 目标 评估使用通过瑞士个性化健康网络 (SPHN) 自动提取的临床数据来补充或替换瑞士儿童气道队列 (SPAC) 中手动提取的临床数据的可行性。材料和方法 我们研究了 2017 年至 2023 年间在两家瑞士儿童医院注册的 1,075 名 SPAC 参与者。通过 SPHN 以资源描述框架格式从电子健康记录中提取临床数据，转换为以就诊为中心的数据集，并与手动提取的 SPAC 临床数据以及随访问卷中家长报告的急诊科 (ED) 就诊和住院情况进行比较。我们通过识别获取数据的挑战来评估可行性，并评估数据数量、完整性和数据集之间的一致性。
- Abstract: Objectives To assess the feasibility of using clinical data automatically extracted via the Swiss Personalized Health Network (SPHN) to complement or replace manually abstracted clinical data in the Swiss Paediatric Airway Cohort (SPAC). Materials and Methods We studied 1,075 SPAC participants enrolled between 2017-2023 at two Swiss children's hospitals. Clinical data were extracted from electronic health records vi...
- Summary (fallback): 机器翻译摘要显示：目标 评估使用通过瑞士个性化健康网络 (SPHN) 自动提取的临床数据来补充或替换瑞士儿童气道队列 (SPAC) 中手动提取的临床数据的可行性。材料和方法 我们研究了 2017 年至 2023 年间在两家瑞士儿童医院注册的 1,075 名 SPAC 参与者。通过 SPHN 以资源描述框架格式从电子健康记录中提取临床数据，转换为以就诊为中心的数据集，并与手动提取的 SPAC 临床数据以及随访问卷中家长报告的急诊科 (ED) 就诊和住院情况进行比较。我们通过识别获取数据的挑战来评估可行性，并评估数据数量、完整性和数据集之间的一致性。
- Keywords: clinical, sphn-derived, extracted, datasets, feasibility

### 9. [氟喹诺酮类药物预防自发性细菌性腹膜炎的真实实践：来自印度北部三级护理中心的纵向研究](https://www.medrxiv.org/content/10.64898/2026.07.14.26357717v1)
- Original title: Real-World Practices of Fluoroquinolone Prophylaxis in Spontaneous Bacterial Peritonitis: A Longitudinal Study from a Tertiary Care Center in North India
- Authors: Malviya, A., Panda, P. K., Sharma, A., Kant, R., Bairwa, M. et al.
- Meta: 2026-07-16 | gastroenterology | DOI: 10.64898/2026.07.14.26357717
- 中文摘要: 背景和目的自发性细菌性腹膜炎（SBP）是肝硬化腹水的一种危及生命的并发症，一年和两年死亡率分别超过 70% 和 80%。氟喹诺酮类药物预防是预防 SBP 的基石。印度三级医疗中心的处方实践和临床结果的真实纵向数据很少。我们的目的是在印度北部的一个三级学术中心评估 SBP 患者的氟喹诺酮处方模式、指南依从性和六个月的临床结果。方法 这是对 AIIMS Rishikesh 进行的 15 个月纵向分析研究进行的预先指定的子分析。因 SBP 入院并开始接受氟喹诺酮预防的成人（年龄 >/= 18 岁）连续入组并随访六个月。将处方实践与 EASL 和 AASLD 建议进行比较。
- Abstract: Background and objectives Spontaneous bacterial peritonitis (SBP) is a life-threatening complication of cirrhosis with ascites, carrying one- and two-year mortality rates exceeding 70% and 80%, respectively. Fluoroquinolone prophylaxis is the cornerstone of SBP prevention. Real-world longitudinal data on prescribing practices and clinical outcomes from Indian tertiary care centers are sparse. We aimed to evaluate fl...
- Summary (fallback): 机器翻译摘要显示：背景和目的自发性细菌性腹膜炎（SBP）是肝硬化腹水的一种危及生命的并发症，一年和两年死亡率分别超过 70% 和 80%。氟喹诺酮类药物预防是预防 SBP 的基石。印度三级医疗中心的处方实践和临床结果的真实纵向数据很少。我们的目的是在印度北部的一个三级学术中心评估 SBP 患者的氟喹诺酮处方模式、指南依从性和六个月的临床结果。方法 这是对 AIIMS Rishikesh 进行的 15 个月纵向分析研究进行的预先指定的子分析。因 SBP 入院并开始接受氟喹诺酮预防的成人（年龄 >/= 18 岁）连续入组并随访六个月。将处方实践与 EASL 和 AASLD 建议进行比较。
- Keywords: fluoroquinolone, prophylaxis, prescribing, tertiary, cure

### 10. [结果相同，价格不同：复方替西帕肽与品牌替西帕肽](https://www.medrxiv.org/content/10.64898/2026.07.14.26357505v1)
- Original title: Same Result, Different Price: Compounded versus Branded Tirzepatide
- Authors: Erly, B., Raja, S.
- Meta: 2026-07-16 | pharmacology and therapeutics | DOI: 10.64898/2026.07.14.26357505
- 中文摘要: 背景。复方替西帕肽被大规模开出，作为品牌 Mounjaro 和 Zepbound 的更便宜的替代品，但成本案例几乎总是通过针对一个品牌标价设定一个复合价格来建立。这种框架忽略了真正决定答案的问题：比患者可以达到的品牌价格更便宜。品牌替西帕肽现在以截然不同的价格出售，即保险共付额（通常为 25-150 美元/月）、LillyDirect 自付（299-449 美元/月）和零售现金价格（1,000-1,200 美元/月）。复合疗法是否能省钱完全取决于特定患者所面临的情况。第二个悬而未决的问题是，这两种制剂是否产生了可比的有效性，因为观察到的差异可能反映了对保险、基线特征和依从性的选择，而不是药物的选择。方法。
- Abstract: Background. Compounded tirzepatide is prescribed at scale as a cheaper substitute for branded Mounjaro and Zepbound, yet the cost case is almost always built by setting one compounded price against one branded list price. That framing ignores the question that actually decides the answer: cheaper than which branded price the patient can reach. Branded tirzepatide is now sold at sharply different tiers, namely insura...
- Summary (fallback): 机器翻译摘要显示：背景。复方替西帕肽被大规模开出，作为品牌 Mounjaro 和 Zepbound 的更便宜的替代品，但成本案例几乎总是通过针对一个品牌标价设定一个复合价格来建立。这种框架忽略了真正决定答案的问题：比患者可以达到的品牌价格更便宜。品牌替西帕肽现在以截然不同的价格出售，即保险共付额（通常为 25-150 美元/月）、LillyDirect 自付（299-449 美元/月）和零售现金价格（1,000-1,200 美元/月）。复合疗法是否能省钱完全取决于特定患者所面临的情况。第二个悬而未决的问题是，这两种制剂是否产生了可比的有效性，因为观察到的差异可能反映了对保险、基线特征和依从性的选择，而不是药物的选择。方法。
- Keywords: branded, price, compounded, insurance, cost

### 11. [Cas12a 的 CRISPR RNA 独立激活](https://www.medrxiv.org/content/10.64898/2026.07.14.26358058v1)
- Original title: CRISPR RNA-independent activation of Cas12a
- Authors: Iwe, I. A., Singh, S., Guan, K., Ocampo, R. F., Ribeiro da Silva, S. J. et al.
- Meta: 2026-07-16 | primary care research | DOI: 10.64898/2026.07.14.26358058
- 中文摘要: CRISPR-Cas12a 核酸酶通常通过 CRISPR RNA (crRNA) 引导和 PAM 依赖性靶标识别来激活，它们共同建立与核酸酶激活相关的规范异源双链体。在这里，我们确定了 Cas12a 的独立于 crRNA 和 PAM 的激活途径，揭示了其核酸识别界面内以前未被识别的构象可塑性。我们证明，短 RNA 可以直接占据经典 crRNA 结合通道，并在没有 PAM 识别或经典 R 环形成的情况下触发具有催化能力的反式裂解状态。生化测定表明，短 RNA 与 crRNA 结合通道结合，并被同源 crRNA 竞争性取代，这与在保守的核酸结合界面处的结合一致。
- Abstract: CRISPR-Cas12a nucleases are classically activated through CRISPR RNA (crRNA) guided and PAM-dependent target recognition, which together establish a canonical heteroduplex associated with nuclease activation. Here we identify a crRNA- and PAM-independent activation pathway for Cas12a that reveals previously unrecognized conformational plasticity within its nucleic acid recognition interface. We show that short RNAs...
- Summary (fallback): 机器翻译摘要显示：CRISPR-Cas12a 核酸酶通常通过 CRISPR RNA (crRNA) 引导和 PAM 依赖性靶标识别来激活，它们共同建立与核酸酶激活相关的规范异源双链体。在这里，我们确定了 Cas12a 的独立于 crRNA 和 PAM 的激活途径，揭示了其核酸识别界面内以前未被识别的构象可塑性。我们证明，短 RNA 可以直接占据经典 crRNA 结合通道，并在没有 PAM 识别或经典 R 环形成的情况下触发具有催化能力的反式裂解状态。生化测定表明，短 RNA 与 crRNA 结合通道结合，并被同源 crRNA 竞争性取代，这与在保守的核酸结合界面处的结合一致。
- Keywords: activation, recognition, canonical, cas12a, crispr

### 12. [处于十字路口的自闭症研究：全球进展、持续差距和未来途径：文献计量分析](https://www.medrxiv.org/content/10.64898/2026.07.14.26358066v1)
- Original title: Autism Research at a Crossroads: Global Progress, Persistent Gaps, and Future Pathways: A Bibliometric Analysis
- Authors: zhong, Q., Chen, L., Ji, Y., Zhu, F., Zou, X.
- Meta: 2026-07-16 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.14.26358066
- 中文摘要: 背景 在过去的二十年里，全球自闭症谱系障碍（ASD）的患病率显着增加。尽管研究取得了实质性进展，但包括病因学、诊断生物标志物和药理学干预在内的关键方面仍未完全阐明。这种持续存在的知识差距需要系统地绘制该领域的演变图，以便为未来的研究重点提供信息。方法 对 2020 年 1 月至 2025 年 5 月 Web of Science 索引的 ASD 相关出版物进行文献计量分析。经过系统的重复数据删除过程，原始文章、评论、病例报告和临床试验均纳入分析。
- Abstract: Background The global prevalence of autism spectrum disorder (ASD) has significantly increased over the past two decades. Despite substantial research advances, critical aspects, including etiology, diagnostic biomarkers, and pharmacological interventions, remain incompletely elucidated. This persistent knowledge gap warrants systematic mapping of the field's evolution to inform future research priorities. Methods A...
- Summary (fallback): 机器翻译摘要显示：背景 在过去的二十年里，全球自闭症谱系障碍（ASD）的患病率显着增加。尽管研究取得了实质性进展，但包括病因学、诊断生物标志物和药理学干预在内的关键方面仍未完全阐明。这种持续存在的知识差距需要系统地绘制该领域的演变图，以便为未来的研究重点提供信息。方法 对 2020 年 1 月至 2025 年 5 月 Web of Science 索引的 ASD 相关出版物进行文献计量分析。经过系统的重复数据删除过程，原始文章、评论、病例报告和临床试验均纳入分析。
- Keywords: research, autism, future, analysis, which

### 13. [CNV 风险评分是否与 CNV 相关智力障碍的神经发育和心理健康特征相关？](https://www.medrxiv.org/content/10.64898/2026.07.14.26358034v1)
- Original title: Are CNV Risk Scores Linked to Neurodevelopmental and Mental Health Characteristics Within CNV-Associated Intellectual Disability?
- Authors: Chi, Z., Alexander-Bloch, A., Neufeld, S. A., Wolstencroft, J., Skuse, D. et al.
- Meta: 2026-07-16 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.14.26358034
- 中文摘要: 背景：患有智力障碍（ID）的儿童和青少年（CYP）经常同时出现神经发育（ND）和心理健康（MH）困难。虽然拷贝数变异 (CNV) 被认为是 ID 的重要病因，但尚不清楚 CNV 风险评分是否以及如何预测 CNV 相关 ID 人群中的 ND 和 MH 特征。方法：我们分析了来自英国 IMAGINE-ID CYP 队列（4-19 岁）的 ID 和临床报告的 CNV 的数据 (N = 1,640)。 CNV 在 ENSEMBL 中使用 Gencode 19 进行注释，以计算 CNV 风险评分，包括功能丧失不耐受 (pLI) 和剂量敏感性的总概率。多元回归模型检查了 CNV 变量的预测以及 ND 和 MH 特征的遗传，并通过发育和健康评估 (DAWBA) 进行评估。
- Abstract: Background: Children and young people (CYP) with intellectual disability (ID) frequently have co-occurring neurodevelopmental (ND) and mental health (MH) difficulties. While copy number variants (CNVs) are identified as an important aetiology of ID, it is unclear whether and how CNV risk scores predict ND and MH characteristics within the CNV-associated ID population. Methods: We analysed data from the UK-based IMAG...
- Summary (fallback): 机器翻译摘要显示：背景：患有智力障碍（ID）的儿童和青少年（CYP）经常同时出现神经发育（ND）和心理健康（MH）困难。虽然拷贝数变异 (CNV) 被认为是 ID 的重要病因，但尚不清楚 CNV 风险评分是否以及如何预测 CNV 相关 ID 人群中的 ND 和 MH 特征。方法：我们分析了来自英国 IMAGINE-ID CYP 队列（4-19 岁）的 ID 和临床报告的 CNV 的数据 (N = 1,640)。 CNV 在 ENSEMBL 中使用 Gencode 19 进行注释，以计算 CNV 风险评分，包括功能丧失不耐受 (pLI) 和剂量敏感性的总概率。多元回归模型检查了 CNV 变量的预测以及 ND 和 MH 特征的遗传，并通过发育和健康评估 (DAWBA) 进行评估。
- Keywords: scores, risk, within, difficulties, higher

### 14. [从基因到神经化学：自闭症感觉差异的兴奋和抑制机制](https://www.medrxiv.org/content/10.64898/2026.07.14.26358047v1)
- Original title: From Genes to Neurochemistry: Excitation and Inhibition Mechanisms of Sensory Differences in Autism
- Authors: Thomson, A. R., Hollestein, V., Arenella, M., Powell, H., He, J. et al.
- Meta: 2026-07-16 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.14.26358047
- 中文摘要: 感觉处理差异是自闭症的核心特征，影响 60-95% 的个体，但相关的神经机制仍不清楚。大脑回路中的兴奋抑制 (E/I) 失衡已被提出，但缺乏将 E/I 通路的遗传变异、区域神经化学、神经回路功能和感觉行为联系起来的体内证据。在这里，我们对 206 名个体（130 名自闭症患者）进行了多模式调查，整合了兴奋性谷氨酸和抑制性 γ-氨基丁酸 (GABA) 能途径的基因组多基因评分、区域 GABA 和 Glx（谷氨酸 + 谷氨酰胺）水平的磁共振波谱 (MRS) 测量、触觉感知的振动触觉心理物理测量以及行为感觉反应性的问卷测量。
- Abstract: Sensory processing differences are a core feature of autism, affecting 60-95% of individuals, yet the associated neural mechanisms remain unclear. An excitation-inhibition (E/I) imbalance in brain circuits has been proposed, but in vivo evidence linking genetic variation in E/I pathways, regional neurochemistry, neural circuit function, and sensory behaviour has been lacking. Here we performed a multimodal investiga...
- Summary (fallback): 机器翻译摘要显示：感觉处理差异是自闭症的核心特征，影响 60-95% 的个体，但相关的神经机制仍不清楚。大脑回路中的兴奋抑制 (E/I) 失衡已被提出，但缺乏将 E/I 通路的遗传变异、区域神经化学、神经回路功能和感觉行为联系起来的体内证据。在这里，我们对 206 名个体（130 名自闭症患者）进行了多模式调查，整合了兴奋性谷氨酸和抑制性 γ-氨基丁酸 (GABA) 能途径的基因组多基因评分、区域 GABA 和 Glx（谷氨酸 + 谷氨酰胺）水平的磁共振波谱 (MRS) 测量、触觉感知的振动触觉心理物理测量以及行为感觉反应性的问卷测量。
- Keywords: sensory, individuals, autistic, mechanisms, differences

### 15. [拉丁美洲西班牙语医疗咨询语音识别模型的基准测试：微调的比较评估](https://www.medrxiv.org/content/10.64898/2026.07.14.26358062v1)
- Original title: Benchmarking Speech Recognition Models for Medical Consultations in Latin American Spanish: A Comparative Evaluation with Fine-Tuning
- Authors: Carrillo, R. M., Carbajal Serrano, A., Condori Pinedo, P. S.
- Meta: 2026-07-16 | public and global health | DOI: 10.64898/2026.07.14.26358062
- 中文摘要: 背景：人工智能 (AI) 医学抄写员依靠语音转文本 (STT) 模型进行转录。非英语环境中 STT 模型的评估仍然很少。我们对来自拉丁美洲 (LatAm) 西班牙语的医疗咨询的 10 个 STT 模型进行了基准测试，并评估了微调是否可以提高转录准确性。方法：十个描述医疗咨询的 YouTube 视频。人类转录是基本事实。评估了五种开源模型：Whisper Large、Whisper Large v3、Whisper Large v3 Turbo、Voxtral Mini 3B 和 Canary 1B v2；还有五个闭源模型：gpt-4o-transcribe、gpt-4o-mini-transcribe、gemini-2.5-pro、Eleven Labs 和 Assembly AI。 Whisper Large v3 进行了微调。培训中保留了一段视频。
- Abstract: BACKGROUND: Artificial intelligence (AI) medical scribes rely on speech-to-text (STT) models for transcription. Evaluations of STT models in non-English settings remain scarce. We benchmarked ten STT models on medical consultations from Latin American (LatAm) Spanish and assessed whether fine-tuning improves transcription accuracy. METHODS: Ten YouTube videos depicting medical consultations. Human transcriptions wer...
- Summary (fallback): 机器翻译摘要显示：背景：人工智能 (AI) 医学抄写员依靠语音转文本 (STT) 模型进行转录。非英语环境中 STT 模型的评估仍然很少。我们对来自拉丁美洲 (LatAm) 西班牙语的医疗咨询的 10 个 STT 模型进行了基准测试，并评估了微调是否可以提高转录准确性。方法：十个描述医疗咨询的 YouTube 视频。人类转录是基本事实。评估了五种开源模型：Whisper Large、Whisper Large v3、Whisper Large v3 Turbo、Voxtral Mini 3B 和 Canary 1B v2；还有五个闭源模型：gpt-4o-transcribe、gpt-4o-mini-transcribe、gemini-2.5-pro、Eleven Labs 和 Assembly AI。 Whisper Larg...
- Keywords: models, medical, whisper, large, close-source

### 16. [重塑专业界限以扩大艾滋病毒暴露前预防 (PrEP) 服务：比利时的协作护理和权力动态](https://www.medrxiv.org/content/10.64898/2026.07.14.26357825v1)
- Original title: Re-shaping professional boundaries to scale-up HIV pre-exposure prophylaxis (PrEP) services: collaborative care and power dynamics in Belgium
- Authors: Vanhamel, J., Kielmann, K., Reyniers, T., Scheerder, G., Nostlinger, C.
- Meta: 2026-07-16 | public and global health | DOI: 10.64898/2026.07.14.26357825
- 中文摘要: 在卫生系统中扩大艾滋病毒暴露前预防（PrEP）服务需要专业人员之间以及专科护理和初级护理之间的合作和明确的角色区分。这项研究探讨了权力动态如何影响比利时将 PrEP 护理扩展到专门的艾滋病毒诊所之外的努力。我们对 36 名 HIV 诊所提供者和两名社区组织 (CBO) 代表进行了半结构化访谈，并与全科医生 (GP) 进行了 16 次在线小组讨论。我们以协作和竞争力概念为指导，对数据进行了主题分析，以研究提供者如何跨专业和组织边界协商 PrEP 交付中的专业知识和角色分工。我们发现报销规定将 PrEP 的启动和后续工作固定在 HIV 诊所内，在护理途径中嵌入了专家管辖权。
- Abstract: Scaling HIV pre-exposure prophylaxis (PrEP) services in health systems will require collaboration and clear role distinction among professionals, and between specialist and primary care. This study examined how power dynamics shape efforts to expand PrEP care beyond specialised HIV clinics in Belgium. We conducted semi-structured interviews with 36 HIV clinic providers and two community-based organisation (CBO) repr...
- Summary (fallback): 机器翻译摘要显示：在卫生系统中扩大艾滋病毒暴露前预防（PrEP）服务需要专业人员之间以及专科护理和初级护理之间的合作和明确的角色区分。这项研究探讨了权力动态如何影响比利时将 PrEP 护理扩展到专门的艾滋病毒诊所之外的努力。我们对 36 名 HIV 诊所提供者和两名社区组织 (CBO) 代表进行了半结构化访谈，并与全科医生 (GP) 进行了 16 次在线小组讨论。我们以协作和竞争力概念为指导，对数据进行了主题分析，以研究提供者如何跨专业和组织边界协商 PrEP 交付中的专业知识和角色分工。我们发现报销规定将 PrEP 的启动和后续工作固定在 HIV 诊所内，在护理途径中嵌入了专家管辖权。
- Keywords: care, prep, services, professional, power

### 17. [使用子空间低阶重建加速 MCDW-pCASL 量化 BBB 水交换和渗透性](https://www.medrxiv.org/content/10.64898/2026.07.13.26357046v1)
- Original title: Accelerated MCDW-pCASL Using Subspace Low-Rank Reconstruction for Quantification of BBB Water Exchange and Permeability
- Authors: Liu, Z., Zhao, C., Huang, Z., Guo, F., Wang, D. J. et al.
- Meta: 2026-07-16 | radiology and imaging | DOI: 10.64898/2026.07.13.26357046
- 中文摘要: 目的：开发一种加速运动补偿扩散加权伪连续动脉自旋标记（MCDW-pCASL）方法，使用空间子空间低秩重建方法来有效量化血脑屏障（BBB）水交换（kw）和渗透性（PSw）。方法：开发了加速多延迟 MCDW-pCASL 序列，以跨多个标记后延迟 (PLD) 同时编码血管内和血管外扩散加权 ASL 信号。优化了空间子空间低阶重建框架，能够联合估计脑血流量（CBF）和BBB水交换率和渗透性。 14 名年轻健康成年人在 3T 时接受了加速 MCDW-pCASL 和传统扩散制备 (DP) pCASL 序列的重测扫描（间隔约 1 周）。
- Abstract: Purpose: To develop an accelerated motion-compensated diffusion-weighted pseudo-continuous arterial spin labeling (MCDW-pCASL) method using a spatial subspace low-rank reconstruction method for efficient quantification of blood-brain barrier (BBB) water exchange (kw) and permeability (PSw). Methods: An accelerated multidelay MCDW-pCASL sequence was developed to simultaneously encode intravascular and extravascular d...
- Summary (fallback): 机器翻译摘要显示：目的：开发一种加速运动补偿扩散加权伪连续动脉自旋标记（MCDW-pCASL）方法，使用空间子空间低秩重建方法来有效量化血脑屏障（BBB）水交换（kw）和渗透性（PSw）。方法：开发了加速多延迟 MCDW-pCASL 序列，以跨多个标记后延迟 (PLD) 同时编码血管内和血管外扩散加权 ASL 信号。优化了空间子空间低阶重建框架，能够联合估计脑血流量（CBF）和BBB水交换率和渗透性。 14 名年轻健康成年人在 3T 时接受了加速 MCDW-pCASL 和传统扩散制备 (DP) pCASL 序列的重测扫描（间隔约 1 周）。
- Keywords: mcdw-pcasl, accelerated, subspace, low-rank, reconstruction

### 18. [患有卵巢早衰的年轻女性的认知](https://www.medrxiv.org/content/10.64898/2026.07.14.26358044v1)
- Original title: Cognition in younger women with premature ovarian insufficiency
- Authors: Naysmith, L., Rida, L., Hampshire, A.
- Meta: 2026-07-16 | sexual and reproductive health | DOI: 10.64898/2026.07.14.26358044
- 中文摘要: 卵巢早衰 (POI) 显着影响生活质量，但年轻女性的直接认知状况和生活经历仍未得到充分研究。在 125 名年轻女性（19-48 岁；66 名特发性 POI，59 名年龄匹配的对照）中，我们检查了 POI 队列中自我报告的认知困扰和症状负担，并比较了各组之间客观的整体和特定领域的认知表现。客观准确度分数来自六项在线任务（Cognitron），并合并成一个强大的全局衡量标准。在 POI 队列中，症状负担范围存在显着差异 ({chi}(3) = 61.90，p<0.001），报告的心理和性症状的强度显着高于身体和血管舒缩症状（均 p<0.001）。
- Abstract: Premature ovarian insufficiency (POI) significantly impacts quality of life, yet the immediate cognitive landscape and lived experience of younger women remain under-researched. In 125 young women (aged 19-48; 66 with idiopathic POI, 59 age-matched controls), we examined self-reported cognitive distress and symptom burden within the POI cohort and compared objective global and domain-specific cognitive performance b...
- Summary (fallback): 机器翻译摘要显示：卵巢早衰 (POI) 显着影响生活质量，但年轻女性的直接认知状况和生活经历仍未得到充分研究。在 125 名年轻女性（19-48 岁；66 名特发性 POI，59 名年龄匹配的对照）中，我们检查了 POI 队列中自我报告的认知困扰和症状负担，并比较了各组之间客观的整体和特定领域的认知表现。客观准确度分数来自六项在线任务（Cognitron），并合并成一个强大的全局衡量标准。在 POI 队列中，症状负担范围存在显着差异 ({chi}(3) = 61.90，p<0.001），报告的心理和性症状的强度显着高于身体和血管舒缩症状（均 p<0.001）。
- Keywords: cognitive, significantly, women, distress, symptom

### 19. [3000 多个轨迹的立体脑电图准确性](https://www.medrxiv.org/content/10.64898/2026.07.14.26358071v1)
- Original title: Stereoelectroencephalography accuracy in a series of over 3000 trajectories
- Authors: Thurairajah, A., Gilmore, G., Persad, A. R., Youshani, A. S., Taha, A. et al.
- Meta: 2026-07-16 | surgery | DOI: 10.64898/2026.07.14.26358071
- 中文摘要: 背景和目的：立体脑电图（SEEG）涉及植入脑内电极来研究耐药性癫痫。 SEEG 需要毫米级精度来确保安全和最佳测绘。尽管研究评估了 SEEG 的准确性，但报告存在很大差异。在这里，我们使用文献中描述的最常见的准确性指标报告一个大系列的植入准确性，并对影响因素进行详细分析。方法：包括 2013 年至 2025 年期间的 SEEG 植入。计算每个植入电极的应用精度。具体而言，在目标点和进入点处计算欧几里德误差、径向误差、深度误差和角度误差。在每个变量和误差指标之间进行相关和多变量分析。轨迹还按图谱衍生的脑叶目标进行分组。
- Abstract: Background and Objectives: Stereoelectroencephalography (SEEG) involves the implantation of intracerebral electrodes to investigate drug-resistant epilepsy. SEEG requires millimetric accuracy to ensure safety and optimal mapping. Although studies have evaluated SEEG accuracy, there is substantial variability in reporting. Here we report on implantation accuracy in a large series using the most common accuracy metric...
- Summary (fallback): 机器翻译摘要显示：背景和目的：立体脑电图（SEEG）涉及植入脑内电极来研究耐药性癫痫。 SEEG 需要毫米级精度来确保安全和最佳测绘。尽管研究评估了 SEEG 的准确性，但报告存在很大差异。在这里，我们使用文献中描述的最常见的准确性指标报告一个大系列的植入准确性，并对影响因素进行详细分析。方法：包括 2013 年至 2025 年期间的 SEEG 植入。计算每个植入电极的应用精度。具体而言，在目标点和进入点处计算欧几里德误差、径向误差、深度误差和角度误差。在每个变量和误差指标之间进行相关和多变量分析。轨迹还按图谱衍生的脑叶目标进行分组。
- Keywords: accuracy, trajectories, seeg, target, implantation

### 20. [明天的医生陷入困境：巴西南部 1,560 名医学生心理健康问题的患病率、社会经济梯度和可改变的决定因素 - 一项多中心横断面研究](https://www.medrxiv.org/content/10.64898/2026.07.14.26357843v1)
- Original title: Tomorrow's physicians in distress: prevalence, socioeconomic gradients, and modifiable determinants of mental health problems among 1,560 medical students in Southern Brazil - a multicentre cross-sectional study
- Authors: Bacchi, G. N. V., Furukawa, L. H., Soares, A. B., Turatti, A. P., Horst, E. G. et al.
- Meta: 2026-07-16 | medical education | DOI: 10.64898/2026.07.14.26357843
- 中文摘要: 摘要背景：医学生承受着不成比例的心理健康问题负担，但来自低收入和中等收入国家的大型多中心研究仍然很少，大多数证据依赖于单一机构样本和基于比值比的分析，这些分析夸大了常见结果的关联。我们对巴西全州医学生的心理健康状况进行了全面的流行病学概述，量化了其负担、其共现情况及其社会经济和学术决定因素。方法：对巴西南里奥格兰德州所有 20 所正在运营的医学院的 1,560 名医学生进行横断面在线调查（2023 年 8 月至 12 月）。
- Abstract: Abstract Background: Medical students carry a disproportionate burden of mental health problems, but large multicentre studies from low- and middle-income countries remain scarce, and most evidence relies on single-institution samples and odds-ratio-based analyses that overstate associations for common outcomes. We provide a comprehensive epidemiological overview of mental health among medical students across an ent...
- Summary (fallback): 机器翻译摘要显示：摘要背景：医学生承受着不成比例的心理健康问题负担，但来自低收入和中等收入国家的大型多中心研究仍然很少，大多数证据依赖于单一机构样本和基于比值比的分析，这些分析夸大了常见结果的关联。我们对巴西全州医学生的心理健康状况进行了全面的流行病学概述，量化了其负担、其共现情况及其社会经济和学术决定因素。方法：对巴西南里奥格兰德州所有 20 所正在运营的医学院的 1,560 名医学生进行横断面在线调查（2023 年 8 月至 12 月）。
- Keywords: medical, students, outcomes, mental, health

### 21. [利用 Milestones、EPA 和 ITE 对阿联酋家庭医学计划中六个队列的常规临床能力委员会数据进行诊断分析](https://www.medrxiv.org/content/10.64898/2026.07.13.26356644v1)
- Original title: Diagnostic analytics of routine Clinical Competency Committee data of six cohorts in family medicine program in the UAE, utilizing Milestones, EPA, and ITE
- Authors: Baynouna Alketbi, L. M., Nagelkerke, N., Alzarouni, A., AlKwuiti, M.
- Meta: 2026-07-16 | medical education | DOI: 10.64898/2026.07.13.26356644
- 中文摘要: 在基于能力的医学教育（CBME）中，纵向数据是连续生成的。临床能力委员会 (CCC) 对学员学习和表现做出的判断是宝贵的资源，支持住院医生和项目的发展。此类数据还可以评估评级质量和 CBME 工具（例如里程碑和可信赖的专业活动 (EPA)），这有助于弥补 CBME 文献中的空白，因为有关这些工具性能的证据仍然有限。目的 研究定期收集阿拉伯联合酋长国艾恩市四次 ACGME-I 认证家庭医学住院医师培训中的 6 个队列的 CCC 数据，以描述生长轨迹、评级系统行为和 CBME 工具的并发一致性。
- Abstract: In Competency-based medical education (CBME), longitudinal data is generated continuously. The judgments a Clinical Competency Committee (CCC) makes about trainee learning and performance are a valuable resource, supporting both resident and program development. Such data as well can enables the evaluation of rating quality and of CBME instruments such as Milestones and Entrustable Professional Activities (EPAs) whi...
- Summary (fallback): 机器翻译摘要显示：在基于能力的医学教育（CBME）中，纵向数据是连续生成的。临床能力委员会 (CCC) 对学员学习和表现做出的判断是宝贵的资源，支持住院医生和项目的发展。此类数据还可以评估评级质量和 CBME 工具（例如里程碑和可信赖的专业活动 (EPA)），这有助于弥补 CBME 文献中的空白，因为有关这些工具性能的证据仍然有限。目的 研究定期收集阿拉伯联合酋长国艾恩市四次 ACGME-I 认证家庭医学住院医师培训中的 6 个队列的 CCC 数据，以描述生长轨迹、评级系统行为和 CBME 工具的并发一致性。
- Keywords: milestones, instruments, competency, ratings, cbme

### 22. [我属于哪里？寻找未知专业的契合点：医学生通往青年医疗保健的道路](https://www.medrxiv.org/content/10.64898/2026.07.14.26358057v1)
- Original title: Where Do I Belong? Searching for fit in an unseen specialty: medical students paths to Youth Health Care
- Authors: Muyselaar-Jellema, J. Z., Könings, K. D., van Dijk, A., Kiefte-de Jong, J. C., Nierkens, V.
- Meta: 2026-07-16 | medical education | DOI: 10.64898/2026.07.14.26358057
- 中文摘要: 简介：随着医疗保健系统日益转向预防和社区护理，对校外专业医生的需求持续增长。然而，劳动力需求与医学生职业抱负之间仍然存在不匹配。关于医学生和实习生如何对青年医疗保健 (YHC) 等校外专业产生兴趣，人们知之甚少。本研究探讨了学员成为青年保健医生 (YHCP) 的轨迹。方法：我们使用半结构化在线访谈对 14 名接受培训的 YHCP 进行了定性研究。我们结合了归纳法和演绎法，应用人与环境（PE）契合框架来探索参与者不断演变的适应和不适应经历。结果：参与者描述了对医学院临床文化的日益不适应（即。
- Abstract: Introduction: As healthcare systems increasingly shift toward prevention and community-based care, the demand for physicians in extramural specialties continues to grow. Yet, a mismatch persists between workforce needs and medical students career aspirations. Little is known about how medical students and trainees develop an interest in extramural specialties such as youth health care (YHC). This study explores trai...
- Summary (fallback): 机器翻译摘要显示：简介：随着医疗保健系统日益转向预防和社区护理，对校外专业医生的需求持续增长。然而，劳动力需求与医学生职业抱负之间仍然存在不匹配。关于医学生和实习生如何对青年医疗保健 (YHC) 等校外专业产生兴趣，人们知之甚少。本研究探讨了学员成为青年保健医生 (YHCP) 的轨迹。方法：我们使用半结构化在线访谈对 14 名接受培训的 YHCP 进行了定性研究。我们结合了归纳法和演绎法，应用人与环境（PE）契合框架来探索参与者不断演变的适应和不适应经历。结果：参与者描述了对医学院临床文化的日益不适应（即。
- Keywords: medical, specialties, students, care, extramural

### 23. [大脑网络兴奋性预测多发性硬化症的临床严重程度](https://www.medrxiv.org/content/10.64898/2026.07.10.26357763v1)
- Original title: Brain Network Excitability Predicts Clinical Severity in Multiple Sclerosis
- Authors: Amato, L. G., Angiolelli, M., Demuru, M., Troisi Lopez, E., Quarantelli, M. et al.
- Meta: 2026-07-16 | neurology | DOI: 10.64898/2026.07.10.26357763
- 中文摘要: 能够同时诊断病情、捕获症状严重程度和预测治疗效果的多发性硬化症 (MS) 综合生物标志物仍然难以捉摸。尽管一些研究强调了脱髓鞘病变在确定多发性硬化症结构病理学中发挥的关键作用，但它们与症状严重程度的关系是有限的。在这里，我们将个性化计算大脑模型与 17 名多发性硬化症患者和 20 名健康对照 (CTR) 的脑磁图 (MEG) 记录相结合，得出个性化的大脑网络兴奋性参数，我们将其作为多发性硬化症生物标志物进行测试。个性化参数可高精度区分 CTR 和 MS 参与者，还可对进展型和缓解型 MS 患者进行分类。值得注意的是，他们还预测了跨多个领域的多发性硬化症临床规模。
- Abstract: Comprehensive biomarkers of multiple sclerosis (MS) capable of simultaneously diagnosing the condition, capturing symptom severity and predicting treatment efficacy remain elusive. Although several studies have highlighted the pivotal role played by demyelinating lesions in determining MS structural pathology, their relationship with symptom severity is limited. Here, we combined personalized computational brain mod...
- Summary (fallback): 机器翻译摘要显示：能够同时诊断病情、捕获症状严重程度和预测治疗效果的多发性硬化症 (MS) 综合生物标志物仍然难以捉摸。尽管一些研究强调了脱髓鞘病变在确定多发性硬化症结构病理学中发挥的关键作用，但它们与症状严重程度的关系是有限的。在这里，我们将个性化计算大脑模型与 17 名多发性硬化症患者和 20 名健康对照 (CTR) 的脑磁图 (MEG) 记录相结合，得出个性化的大脑网络兴奋性参数，我们将其作为多发性硬化症生物标志物进行测试。个性化参数可高精度区分 CTR 和 MS 参与者，还可对进展型和缓解型 MS 患者进行分类。值得注意的是，他们还预测了跨多个领域的多发性硬化症临床规模。
- Keywords: brain, severity, personalized, clinical, biomarkers

### 24. [使用 E-norms 方法建立患者特定的脑电图基线，用于在没有标记训练数据的情况下检测儿科癫痫发作](https://www.medrxiv.org/content/10.64898/2026.07.13.26357876v1)
- Original title: Patient-Specific EEG Baseline Establishment Using the E-norms Method for Pediatric Seizure Detection Without Labeled Training Data
- Authors: Jabre, J. F.
- Meta: 2026-07-16 | neurology | DOI: 10.64898/2026.07.13.26357876
- 中文摘要: 这项工作的目的是使用电子规范方法作为小儿癫痫发作检测的筛查和回顾性审查工具来验证患者特异性脑电图基线的建立。该方法适用于 CHB-MIT 头皮脑电图数据库（3-18 岁）中 10 名患者的 247 条无癫痫发作脑电图记录（263.92 小时）。跨 23 个通道的每 2 秒周期计算结合一阶导数动力学、谱熵、方差和线长度的复合稳定性度量。患者特定的检测阈值是使用加权统计程序根据每位患者的无癫痫发作基线得出的。性能根据 62 个癫痫发作文件中的 72 次专家注释的癫痫发作（2,705 个时期）进行验证，持续时间跨度为 6 至 264 秒（44 倍范围）。
- Abstract: The aim of this work is to validate patient-specific EEG baseline establishment using the e-norms method as a screening and retrospective-review tool for seizure detection in pediatric epilepsy. The method was applied to 247 seizure-free EEG recordings (263.92 hours) from 10 patients in the CHB-MIT Scalp EEG Database (ages 3-18). A composite stability metric combining first-derivative dynamics, spectral entropy, var...
- Summary (fallback): 机器翻译摘要显示：这项工作的目的是使用电子规范方法作为小儿癫痫发作检测的筛查和回顾性审查工具来验证患者特异性脑电图基线的建立。该方法适用于 CHB-MIT 头皮脑电图数据库（3-18 岁）中 10 名患者的 247 条无癫痫发作脑电图记录（263.92 小时）。跨 23 个通道的每 2 秒周期计算结合一阶导数动力学、谱熵、方差和线长度的复合稳定性度量。患者特定的检测阈值是使用加权统计程序根据每位患者的无癫痫发作基线得出的。性能根据 62 个癫痫发作文件中的 72 次专家注释的癫痫发作（2,705 个时期）进行验证，持续时间跨度为 6 至 264 秒（44 倍范围）。
- Keywords: detection, patient-specific, seizure, sensitivity, method

### 25. [VA 百万退伍军人计划 (MVP) 中简易精神状态检查 (MMSE) 分数的管理：认知老化研究的应用](https://www.medrxiv.org/content/10.64898/2026.07.14.26358064v1)
- Original title: Curation of Mini Mental State Examination (MMSE) Scores in the VA Million Veteran Program (MVP): Applications for Cognitive Aging Research
- Authors: Lopez, F. V., Gillis, M., Lee, S., Sakamoto, M. S., Zhang, R. et al.
- Meta: 2026-07-16 | neurology | DOI: 10.64898/2026.07.14.26358064
- 中文摘要: 背景：电子健康记录（EHR）相关的生物存储库为推进阿尔茨海默病（AD）和相关痴呆症的流行病学研究提供了机会。目的：评估 VA 百万退伍军人计划 (MVP) 参与者的 VA EHR 简易精神状态检查 (MMSE) 分数的提取、管理和联想效度。方法：样本（N = 49,555；7.4% 女性）包括多种族队列（欧洲人 [68.3%]、非洲人 [20.4%]、西班牙人 [9.0%]），并具有 EHR 提取的 MMSE 评分； 30.7% 为载脂蛋白 E (APOE) {ε}4 携带者，25.8% 具有多重评分。线性回归检查了ε4剂量(0,1,2)与第一和最低MMSE分数之间的横截面关联。还针对年龄≥65 岁的参与者的 MVP 痴呆诊断算法评估了 MMSE 评分。
- Abstract: Background: Electronic health record (EHR)-linked biorepositories provide opportunities to advance epidemiological research in Alzheimer's disease (AD) and related dementias. Objective: Evaluate the extraction, curation, and associative validity of Mini Mental State Examination (MMSE) scores from the VA EHR for participants in the VA Million Veteran Program (MVP). Methods: The sample (N = 49,555; 7.4% women) include...
- Summary (fallback): 机器翻译摘要显示：背景：电子健康记录（EHR）相关的生物存储库为推进阿尔茨海默病（AD）和相关痴呆症的流行病学研究提供了机会。目的：评估 VA 百万退伍军人计划 (MVP) 参与者的 VA EHR 简易精神状态检查 (MMSE) 分数的提取、管理和联想效度。方法：样本（N = 49,555；7.4% 女性）包括多种族队列（欧洲人 [68.3%]、非洲人 [20.4%]、西班牙人 [9.0%]），并具有 EHR 提取的 MMSE 评分； 30.7% 为载脂蛋白 E (APOE) {ε}4 携带者，25.8% 具有多重评分。线性回归检查了ε4剂量(0,1,2)与第一和最低MMSE分数之间的横截面关联。还针对年龄≥65 岁的参与者的 MVP 痴呆诊断算法评估了 MMSE 评分。
- Keywords: mmse, scores, epsilon, carriers, participants

### 26. [评估发音和语音后部的良好程度作为运动言语障碍言语严重程度的客观标志](https://www.medrxiv.org/content/10.64898/2026.07.14.26358076v1)
- Original title: Evaluating Goodness of Pronunciation and Phonological Posteriors as Objective Markers of Speech Severity in Motor Speech Disorders
- Authors: Wang, F., Utianski, R. L., Duffy, J. R., Barnard, L. R., Botha, H.
- Meta: 2026-07-16 | neurology | DOI: 10.64898/2026.07.14.26358076
- 中文摘要: 这项研究检验了发音良好度 (GoP) 分数和语音后验概率在多大程度上反映了运动性言语障碍 (MSD) 患者言语严重程度的感知评级。灾难一词的语音录音来自 489 名参与者，其中包括 333 名神经学典型对照者和 156 名 MSD 患者。 GoP 分数是使用传统声学特征和自监督语音表示（包括 WavLM 和 XLS-R）跨多种建模方法得出的，而语音后验概率是使用 Phonet 提取的。使用肯德尔的等级相关性、回归和接收者操作特征分析以及言语病理学家对声音失真和可懂度的感知评级来评估模型性能。
- Abstract: This study examined the extent to which goodness of pronunciation (GoP) scores and phonological posterior probabilities capture perceptual ratings of speech severity in individuals with motor speech disorders (MSD). Speech recordings of the word catastrophe were obtained from 489 participants, including 333 neurologically typical controls and 156 individuals with MSD. GoP scores were derived using traditional acoust...
- Summary (fallback): 机器翻译摘要显示：这项研究检验了发音良好度 (GoP) 分数和语音后验概率在多大程度上反映了运动性言语障碍 (MSD) 患者言语严重程度的感知评级。灾难一词的语音录音来自 489 名参与者，其中包括 333 名神经学典型对照者和 156 名 MSD 患者。 GoP 分数是使用传统声学特征和自监督语音表示（包括 WavLM 和 XLS-R）跨多种建模方法得出的，而语音后验概率是使用 Phonet 提取的。使用肯德尔的等级相关性、回归和接收者操作特征分析以及言语病理学家对声音失真和可懂度的感知评级来评估模型性能。
- Keywords: speech, phonological, posterior, probabilities, perceptual

### 27. [将白质高信号与疼痛敏感性联系起来的大脑结构通路](https://www.medrxiv.org/content/10.64898/2026.07.14.26358028v1)
- Original title: Structural Brain Pathways Linking White Matter Hyperintensities to Pain Sensitivity
- Authors: LIU, X., Vangberg, T. R., Kuiper, L. M., Vernooij, M. W., Stubhaug, A. et al.
- Meta: 2026-07-16 | neurology | DOI: 10.64898/2026.07.14.26358028
- 中文摘要: 人们对疼痛的敏感性存在很大差异，这种差异具有临床相关性，但人们对潜在的大脑结构机制仍知之甚少。白质高信号（WMH）是脑小血管疾病的常见影像学标志物，与白质束的微结构异常相关，也与疼痛相关的结果有关；然而，WMH 与疼痛感知改变之间的联系机制仍不清楚。我们研究了 WMH 是否通过特定的微结构改变和皮质结构差异与疼痛敏感性相关。我们分析了基于人口的鹿特丹研究中 1,448 名参与者（平均年龄 73 岁；53% 女性）的数据，并在基于人口的特罗姆瑟研究中独立复制了 1,522 名参与者（平均年龄 63 岁；52% 女性）的研究结果。
- Abstract: People differ widely in their sensitivity to pain, and this variability is clinically relevant, yet the underlying structural brain mechanisms remain poorly understood. White matter hyperintensities (WMH), a common imaging marker of cerebral small vessel disease, are associated with microstructural abnormalities in white matter tracts and have also been linked to pain related outcomes; however, the mechanisms linkin...
- Summary (fallback): 机器翻译摘要显示：人们对疼痛的敏感性存在很大差异，这种差异具有临床相关性，但人们对潜在的大脑结构机制仍知之甚少。白质高信号（WMH）是脑小血管疾病的常见影像学标志物，与白质束的微结构异常相关，也与疼痛相关的结果有关；然而，WMH 与疼痛感知改变之间的联系机制仍不清楚。我们研究了 WMH 是否通过特定的微结构改变和皮质结构差异与疼痛敏感性相关。我们分析了基于人口的鹿特丹研究中 1,448 名参与者（平均年龄 73 岁；53% 女性）的数据，并在基于人口的特罗姆瑟研究中独立复制了 1,522 名参与者（平均年龄 63 岁；52% 女性）的研究结果。
- Keywords: pain, sensitivity, white, matter, thalamic

### 28. [血浆中的肌肉蛋白与肌萎缩侧索硬化症的显着表型相关](https://www.medrxiv.org/content/10.64898/2026.07.14.26357727v1)
- Original title: Muscle proteins in plasma associate to distinguished phenotypes in amyotrophic lateral sclerosis
- Authors: Azizi, L., Aksoylu, I., Bueno Alvez, M., Foucher, J., Juto, A. et al.
- Meta: 2026-07-16 | neurology | DOI: 10.64898/2026.07.14.26357727
- 中文摘要: 背景：肌萎缩侧索硬化症（ALS）是一种以上运动神经元和下运动神经元死亡为特征的神经退行性疾病，通常呈现临床异质性。液体生物标志物的发展仍然以神经丝轻链（NEFL）为主，神经丝轻链是神经轴突损伤的标志物。然而，NEFL 对 ALS 及其表型不具有特异性，目前缺乏捕获 ALS 异质性的生物标志物，例如发病部位和 ALS 额颞叶谱系障碍 (ALS-FTSD)。因此，我们研究了血浆蛋白质组学是否可以揭示分层和解释 ALS 异质性的通路水平特征。方法：我们分析了 299 名 ALS 患者和 50 名年龄和性别相当的健康对照者的约 5,400 种血浆蛋白 (Olink Explore HT)。
- Abstract: Background: Amyotrophic lateral sclerosis (ALS) is a neurodegenerative disease characterized by death of upper and lower motor neurons, usually presented with clinical heterogeneity. Fluid biomarker development remains dominated by neurofilament light chain (NEFL), a marker of neuroaxonal injury. NEFL is however unspecific to ALS and its phenotypes and there is currently a lack of biomarkers that capture ALS heterog...
- Summary (fallback): 机器翻译摘要显示：背景：肌萎缩侧索硬化症（ALS）是一种以上运动神经元和下运动神经元死亡为特征的神经退行性疾病，通常呈现临床异质性。液体生物标志物的发展仍然以神经丝轻链（NEFL）为主，神经丝轻链是神经轴突损伤的标志物。然而，NEFL 对 ALS 及其表型不具有特异性，目前缺乏捕获 ALS 异质性的生物标志物，例如发病部位和 ALS 额颞叶谱系障碍 (ALS-FTSD)。因此，我们研究了血浆蛋白质组学是否可以揭示分层和解释 ALS 异质性的通路水平特征。方法：我们分析了 299 名 ALS 患者和 50 名年龄和性别相当的健康对照者的约 5,400 种血浆蛋白 (Olink Explore HT)。
- Keywords: proteins, protein, nefl, plasma, heterogeneity

### 29. [伊朗育龄妇女接种 COVID-19 疫苗后月经周期发生变化](https://www.medrxiv.org/content/10.64898/2026.07.07.26357499v1)
- Original title: Menstrual Cycle Changes among Reproduction-Aged Iranian Women Following COVID-19 Vaccination
- Authors: Azad, A., Darsareh, F., Ebrahimi abshur, M., Hajisafari, M., Mahmoudi Essaabadi, A.
- Meta: 2026-07-16 | obstetrics and gynecology | DOI: 10.64898/2026.07.07.26357499
- 中文摘要: 背景 接种 COVID-19 疫苗后，月经周期紊乱的报道越来越多，这引发了人们对其在育龄妇女中的患病率和临床意义的疑问。目的 本研究旨在调查伊朗育龄妇女接种不同剂量的 COVID-19 疫苗后月经周期改变的发生率和类型。方法 对已接种疫苗的女性进行横断面调查，报告每次疫苗接种前后的月经周期状况。收集并分析有关周期规律、血流特征和特定月经失调的数据。结果 在接种第一剂、第二剂、第三剂和第四剂疫苗后，分别有 28.8%、25.4%、30.3% 和 68.4% 的参与者报告月经周期发生变化。
- Abstract: Background Menstrual cycle disturbances have been increasingly reported after COVID-19 vaccination, raising questions about their prevalence and clinical significance among women of reproductive age. Objective This study aimed to investigate the incidence and types of menstrual cycle alterations following different doses of COVID-19 vaccines among Iranian women of reproductive age. Methods A cross-sectional survey w...
- Summary (fallback): 机器翻译摘要显示：背景 接种 COVID-19 疫苗后，月经周期紊乱的报道越来越多，这引发了人们对其在育龄妇女中的患病率和临床意义的疑问。目的 本研究旨在调查伊朗育龄妇女接种不同剂量的 COVID-19 疫苗后月经周期改变的发生率和类型。方法 对已接种疫苗的女性进行横断面调查，报告每次疫苗接种前后的月经周期状况。收集并分析有关周期规律、血流特征和特定月经失调的数据。结果 在接种第一剂、第二剂、第三剂和第四剂疫苗后，分别有 28.8%、25.4%、30.3% 和 68.4% 的参与者报告月经周期发生变化。
- Keywords: menstrual, cycle, women, covid-19, changes

### 30. [绘制有影响力的肝细胞癌研究的主题变化：两队列文献计量分析](https://www.medrxiv.org/content/10.64898/2026.07.07.26357427v1)
- Original title: Mapping Topic Change in Influential Hepatocellular Carcinoma Research: A Two-Cohort Bibliometric Analysis
- Authors: Su, Z., Li, T.
- Meta: 2026-07-16 | oncology | DOI: 10.64898/2026.07.07.26357427
- 中文摘要: 肝细胞癌 (HCC) 的治疗前景正在迅速发展，需要可扩展的方法来综合不断扩大的科学文献。我们通过对 2023 年和 2024 年有影响力的出版物进行回顾性文献计量分析，描述了 HCC 治疗和预后研究的主题转变。使用 OpenAlex 数据库，我们根据 18 个月的发表后引用计数，确定了每年 50 篇引用率最高的论文。部署大型语言模型来提取、规范化非结构化文本中的概念并将其分类为规范主题和父主题，从而实现定量的逐年频率比较。对这 100 篇论文的分析揭示了研究重点的明显成熟。
- Abstract: The therapeutic landscape for hepatocellular carcinoma (HCC) is evolving rapidly, necessitating scalable approaches to synthesize the expanding scientific literature. We characterized thematic shifts in HCC treatment and prognosis research by conducting a retrospective bibliometric analysis of influential publications from 2023 and 2024. Using the OpenAlex database, we identified the 50 most highly cited papers from...
- Summary (fallback): 机器翻译摘要显示：肝细胞癌 (HCC) 的治疗前景正在迅速发展，需要可扩展的方法来综合不断扩大的科学文献。我们通过对 2023 年和 2024 年有影响力的出版物进行回顾性文献计量分析，描述了 HCC 治疗和预后研究的主题转变。使用 OpenAlex 数据库，我们根据 18 个月的发表后引用计数，确定了每年 50 篇引用率最高的论文。部署大型语言模型来提取、规范化非结构化文本中的概念并将其分类为规范主题和父主题，从而实现定量的逐年频率比较。对这 100 篇论文的分析揭示了研究重点的明显成熟。
- Keywords: research, analysis, influential, hepatocellular, carcinoma
