# daily2rxiv Digest - 2026-07-10

共收录 65 篇论文。

## arxiv

### 1. [准确、跨学科、透明的结构属性理解与深层的原生结构推理](https://arxiv.org/abs/2607.07708v1)
- Original title: Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning
- Authors: Chen Tang, Yizhou Wang, Jianyu Wu, Lintao Wang, Shixiang Tang et al.
- Meta: 2026-07-08 | cs.CL
- 中文摘要: 结构-性质关系是生物学、化学和材料科学的基础，其中功能、反应性和物理响应产生于空间、化学和周期性组织。从机械上解释这些关系需要通过科学原理和物理约束来解释结构证据，从立体化学和键合到对称性、能量学和周期顺序。然而，将人工智能应用于这一过程提出了表示和推理的共同挑战：模型必须保留领域本机结构信息，同时显示特定证据如何支持这些约束下的预测。在这里，我们介绍 SciReasoner，这是一种多模式科学基础模型，用于蛋白质、小分子和无机晶体的本机结构推理。
- Abstract: Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic ord...
- Summary (fallback): 机器翻译摘要显示：结构-性质关系是生物学、化学和材料科学的基础，其中功能、反应性和物理响应产生于空间、化学和周期性组织。从机械上解释这些关系需要通过科学原理和物理约束来解释结构证据，从立体化学和键合到对称性、能量学和周期顺序。然而，将人工智能应用于这一过程提出了表示和推理的共同挑战：模型必须保留领域本机结构信息，同时显示特定证据如何支持这些约束下的预测。在这里，我们介绍 SciReasoner，这是一种多模式科学基础模型，用于蛋白质、小分子和无机晶体的本机结构推理。
- Keywords: reasoning, structural, scireasoner, scientific, periodic

### 2. [Co-LMLM：连续查询有限内存语言模型](https://arxiv.org/abs/2607.07707v1)
- Original title: Co-LMLM: Continuous-Query Limited Memory Language Models
- Authors: Yair Feldman, Linxi Zhao, Nathan Godey, Dongyoung Go, Yilun Hua et al.
- Meta: 2026-07-08 | cs.CL
- 中文摘要: 有限记忆语言模型 (LMLM) 在预训练期间将事实知识外化到知识库 (KB)，而不是将其记忆在权重中。在生成过程中，模型根据需要从知识库中获取知识。这种最近引入的范例提供了多种优势，包括超越传统法学硕士的知识控制能力。我们提出连续查询 LMLM (CO-LMLM)，其中知识库将连续键与文本知识值配对，这与之前对关系知识库和查询的依赖有很大不同。 CO-LMLM 以最低的成本生成灵活的矢量查询，同时仍然将人类可读和可归因的检索知识集成到其生成中。我们将此设计与注释管道配对，该注释管道可以在任意文本中标记自由形式的事实跨度，从而消除了先前工作对维基百科的限制。
- Abstract: Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM),...
- Summary (fallback): 机器翻译摘要显示：有限记忆语言模型 (LMLM) 在预训练期间将事实知识外化到知识库 (KB)，而不是将其记忆在权重中。在生成过程中，模型根据需要从知识库中获取知识。这种最近引入的范例提供了多种优势，包括超越传统法学硕士的知识控制能力。我们提出连续查询 LMLM (CO-LMLM)，其中知识库将连续键与文本知识值配对，这与之前对关系知识库和查询的依赖有很大不同。 CO-LMLM 以最低的成本生成灵活的矢量查询，同时仍然将人类可读和可归因的检索知识集成到其生成中。我们将此设计与注释管道配对，该注释管道可以在任意文本中标记自由形式的事实跨度，从而消除了先前工作对维基百科的限制。
- Keywords: knowledge, co-lmlm, models, factual, prior

### 3. [实现线性化的关键：分析驱动的变压器线性化](https://arxiv.org/abs/2607.07706v1)
- Original title: The Key to Going Linear: Analysis-Driven Transformer Linearization
- Authors: Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 因果自注意力的二次成本严重阻碍了长上下文变换器推理。尽管存在大量事后线性化管道，但很难确定哪些组件可以保持模型质量。这项工作在严格的冻结主干机制中隔离了状态更新设计的影响。我们证明了 softmax 依赖于 key-dependent、rank-1 正交投影，阐明了为什么 delta 式网络优于纯门控累积。我们确定了近似误差的潜在来源，并引入了结构干预措施，特别是接收器令牌、短卷积和固定预算缓存路由，从而减少了剩余差距。我们将 LLaMA 和 Qwen 模型的线性化方法扩展至 32B 参数，优于 MMLU 上的先前事后基线，并匹配复杂自适应缓存框架的长上下文检索。
- Abstract: The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style...
- Summary (fallback): 机器翻译摘要显示：因果自注意力的二次成本严重阻碍了长上下文变换器推理。尽管存在大量事后线性化管道，但很难确定哪些组件可以保持模型质量。这项工作在严格的冻结主干机制中隔离了状态更新设计的影响。我们证明了 softmax 依赖于 key-dependent、rank-1 正交投影，阐明了为什么 delta 式网络优于纯门控累积。我们确定了近似误差的潜在来源，并引入了结构干预措施，特别是接收器令牌、短卷积和固定预算缓存路由，从而减少了剩余差距。我们将 LLaMA 和 Qwen 模型的线性化方法扩展至 32B 参数，优于 MMLU 上的先前事后基线，并匹配复杂自适应缓存框架的长上下文检索。
- Keywords: linearization, transformer, long-context, post, identify

### 4. [在控制多重性的同时减轻赢家的诅咒：剂量范围试验中随时有效推理的电子处理方法](https://arxiv.org/abs/2607.07699v1)
- Original title: Mitigating the Winner's Curse While Controlling Multiplicity: e-Process Methods for Anytime-Valid Inference in Dose-Ranging Trials
- Authors: Victor K. de la Pena, Fangyuan Lin, Demissie Alemayehu, Victor H. de la Pena
- Meta: 2026-07-08 | stat.ME
- 中文摘要: II 期剂量范围试验经常报告观察到的最大剂量控制效果，同时反复检查积累的数据。这造成了两种耦合的扭曲：选择经验获胜者的选择乐观主义，称为获胜者的诅咒，以及由于剂量和临时外观的多重性而导致的第一类错误膨胀。我们开发了一种随时有效的程序来测试最佳真实剂量效应是否超过有临床意义的裕度。数学起点是运行最大值的最近选择溢价恒等式：对于剂量控制分数，重新选择当前领导者的预期收益变成了可预测的选择费用。减去该电荷会得到在复合零点下具有非正漂移的残差；应用单边混合指数构造然后产生电子过程，从而产生任何时候有效的全局测试。
- Abstract: Phase II dose-ranging trials often report the largest observed dose-control effect while inspecting accumulating data repeatedly. This creates two coupled distortions: selection optimism from choosing the empirical winner, known as the winner's curse, and Type I error inflation from multiplicity across doses and interim looks. We develop an anytime-valid procedure for testing whether the best true dose effect exceed...
- Summary (fallback): 机器翻译摘要显示：II 期剂量范围试验经常报告观察到的最大剂量控制效果，同时反复检查积累的数据。这造成了两种耦合的扭曲：选择经验获胜者的选择乐观主义，称为获胜者的诅咒，以及由于剂量和临时外观的多重性而导致的第一类错误膨胀。我们开发了一种随时有效的程序来测试最佳真实剂量效应是否超过有临床意义的裕度。数学起点是运行最大值的最近选择溢价恒等式：对于剂量控制分数，重新选择当前领导者的预期收益变成了可预测的选择费用。减去该电荷会得到在复合零点下具有非正漂移的残差；应用单边混合指数构造然后产生电子过程，从而产生任何时候有效的全局测试。
- Keywords: effect, winner, anytime-valid, selection, best

### 5. [用于样本高效扩散 RLHF 的选择性时间步长加权和基于优势的重播](https://arxiv.org/abs/2607.07693v1)
- Original title: Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF
- Authors: Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 来自人类反馈的强化学习（RLHF）已成为使生成模型与人类偏好保持一致的强大范例。然而，将 RLHF 应用于扩散模型仍然是非常低效的反馈，因为现有方法通常需要大量的人工或奖励模型评估。这种限制降低了扩散 RLHF 在反馈是主要瓶颈的现实环境中的实用性。在本文中，我们提出了两种互补策略，可以显着提高扩散 RLHF 的反馈效率，同时保留对未见提示的泛化能力。我们的主要观察结果是，扩散轨迹中的奖励信息分布不均匀：并非所有去噪时间步长或轨迹都对从奖励信号中学习做出同样的贡献。
- Abstract: Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the pri...
- Summary (fallback): 机器翻译摘要显示：来自人类反馈的强化学习（RLHF）已成为使生成模型与人类偏好保持一致的强大范例。然而，将 RLHF 应用于扩散模型仍然是非常低效的反馈，因为现有方法通常需要大量的人工或奖励模型评估。这种限制降低了扩散 RLHF 在反馈是主要瓶颈的现实环境中的实用性。在本文中，我们提出了两种互补策略，可以显着提高扩散 RLHF 的反馈效率，同时保留对未见提示的泛化能力。我们的主要观察结果是，扩散轨迹中的奖励信息分布不均匀：并非所有去噪时间步长或轨迹都对从奖励信号中学习做出同样的贡献。
- Keywords: diffusion, rlhf, feedback, weighting, trajectories

### 6. [Agon：具有隐式竞争推理评分的竞争性跨模型强化学习](https://arxiv.org/abs/2607.07690v1)
- Original title: Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning
- Authors: Vladislav Beliaev
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 来自可验证奖励（例如 GRPO）的强化学习是当今推理模型背后的引擎，但它仅对最终答案进行评分。在解决困难问题时，这会训练模型写更多而不是更好地思考，因为轨迹本身永远不会被评分，并且不存在良好思维的标签。我们介绍 Agon，它使两个竞争模型成为彼此的评分者。两者都尝试同样的问题；在交替角色中，一个起草解决方案，另一个在解决问题时阅读该解决方案，并且每个人都会因解决另一个问题而获得奖励。为了获胜，模型必须推理出已经看过其工作的竞争对手，因此推理是在训练过程中隐式判断的，没有过程标签，也没有奖励模型。由于这两个模型都经过优化，因此每个模型都面临着越来越强大的竞争对手，这是单模型强化学习无法提供的。两者只需要相当强大并且行为上不同即可。
- Abstract: Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating...
- Summary (fallback): 机器翻译摘要显示：来自可验证奖励（例如 GRPO）的强化学习是当今推理模型背后的引擎，但它仅对最终答案进行评分。在解决困难问题时，这会训练模型写更多而不是更好地思考，因为轨迹本身永远不会被评分，并且不存在良好思维的标签。我们介绍 Agon，它使两个竞争模型成为彼此的评分者。两者都尝试同样的问题；在交替角色中，一个起草解决方案，另一个在解决问题时阅读该解决方案，并且每个人都会因解决另一个问题而获得奖励。为了获胜，模型必须推理出已经看过其工作的竞争对手，因此推理是在训练过程中隐式判断的，没有过程标签，也没有奖励模型。由于这两个模型都经过优化，因此每个模型都面临着越来越强大的竞争对手，这是单模型强化学习无法提供的。两者只需要相当强大并且行为上不同即可。
- Keywords: models, other, model, rival, reasoning

### 7. [ECGLight：用于纸质心电​​图数字化和心肌梗死筛查的计算光框架](https://arxiv.org/abs/2607.07683v1)
- Original title: ECGLight: Compute-Light Framework For Paper ECG Digitization and Myocardial Infarction Screening
- Authors: Shreyasvi Natraj, Cyrus Achtari, Felice Gragnano, Andrea Milzi, Marco Valgimigli et al.
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 心电图（ECG）是诊断心血管疾病最广泛使用的测试之一。然而，由于连接性和计算能力有限，一些远程诊所仍然使用纸质心电图打印输出进行分析。因此，在偏远地区获得的大量物理心电图仍然无法被当代基于人工智能 (AI) 的决策支持访问，因为它们需要大量的计算资源或强大的高速互联网连接。这导致在一些情况下，急性冠状动脉闭塞（ACS）等疾病被忽视，再灌注治疗被延迟。
- Abstract: Electrocardiography (ECG) is one of the most widely used tests for diagnosing cardiovascular disease. Yet several remote clinics still utilize paper ECG printouts for their analysis due to limited connectivity and computational capacity. As a result, vast numbers of physical ECGs obtained in remote areas still remain incapable of being accessed by contemporary artificial-intelligence (AI)-based decision support as t...
- Summary (fallback): 机器翻译摘要显示：心电图（ECG）是诊断心血管疾病最广泛使用的测试之一。然而，由于连接性和计算能力有限，一些远程诊所仍然使用纸质心电图打印输出进行分析。因此，在偏远地区获得的大量物理心电图仍然无法被当代基于人工智能 (AI) 的决策支持访问，因为它们需要大量的计算资源或强大的高速互联网连接。这导致在一些情况下，急性冠状动脉闭塞（ACS）等疾病被忽视，再灌注治疗被延迟。
- Keywords: still, connectivity, ecgs, support, compute-light

### 8. [用于偏微分方程约束优化的神经算子支持的拓扑通知进化策略](https://arxiv.org/abs/2607.07682v1)
- Original title: Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization
- Authors: Xiangming Huang, Guannan Zhang, Lu Lu, Raphaël Pestourie
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 由于设计空间的高维性和非凸性，由偏微分方程控制的物理系统的逆设计在计算上要求很高。逆向设计的生成模型通常缺乏稳健性和可迁移性，而进化策略虽然稳健，但在高维空间中却举步维艰。本文介绍了一种基于神经算子的拓扑通知进化策略（NOTES），它集成了降维、表示学习和进化优化，以实现高效且可转移的逆向设计。 NOTES 将基于 DeepONet 的神经算子与协方差矩阵适应进化策略 (CMA-ES) 结合起来，在紧凑的潜在空间中执行全局优化，对拓扑感知先验进行编码，同时发现针对未见操作条件的高性能设计。
- Abstract: The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust but struggle in high-dimensional spaces. This paper introduces a Neural Operator-enabled Topology-informed Evolutionar...
- Summary (fallback): 机器翻译摘要显示：由于设计空间的高维性和非凸性，由偏微分方程控制的物理系统的逆设计在计算上要求很高。逆向设计的生成模型通常缺乏稳健性和可迁移性，而进化策略虽然稳健，但在高维空间中却举步维艰。本文介绍了一种基于神经算子的拓扑通知进化策略（NOTES），它集成了降维、表示学习和进化优化，以实现高效且可转移的逆向设计。 NOTES 将基于 DeepONet 的神经算子与协方差矩阵适应进化策略 (CMA-ES) 结合起来，在紧凑的潜在空间中执行全局优化，对拓扑感知先验进行编码，同时发现针对未见操作条件的高性能设计。
- Keywords: design, optimization, inverse, notes, evolutionary

### 9. [通过采样进行任意维度的学习](https://arxiv.org/abs/2607.07680v1)
- Original title: Any-Dimensional Learning by Sampling
- Authors: Eitan Levin, Venkat Chandrasekaran
- Meta: 2026-07-08 | math.ST
- 中文摘要: 许多机器学习模型是针对不同大小的输入定义的，例如包含不同数量点的点云、不同长度的标记序列以及不同数量节点上的图。此类模型是在大小必然有限的有限多个示例上进行训练的。这些模型从小尺寸输入泛化到训练期间未见过的较大尺寸输入的效果如何？此外，在大量输入上评估此类模型通常成本高昂。我们如何绘制大输入以获得模型采用相似值的较小输入？这两个问题的核心是需要比较不同大小的输入并用小输入来近似大输入。我们提出了一种统一的方法来解决这些问题，即使用随机采样图来比较不同大小的输入。
- Abstract: Many machine learning models are defined for inputs of different sizes, such as point clouds containing different numbers of points, sequences of tokens of different lengths, and graphs on different numbers of nodes. Such models are trained on finitely-many examples of necessarily limited sizes. How well do these models generalize from inputs of small size to larger inputs of size not seen during training? Furthermo...
- Summary (fallback): 机器翻译摘要显示：许多机器学习模型是针对不同大小的输入定义的，例如包含不同数量点的点云、不同长度的标记序列以及不同数量节点上的图。此类模型是在大小必然有限的有限多个示例上进行训练的。这些模型从小尺寸输入泛化到训练期间未见过的较大尺寸输入的效果如何？此外，在大量输入上评估此类模型通常成本高昂。我们如何绘制大输入以获得模型采用相似值的较小输入？这两个问题的核心是需要比较不同大小的输入并用小输入来近似大输入。我们提出了一种统一的方法来解决这些问题，即使用随机采样图来比较不同大小的输入。
- Keywords: inputs, different, sampling, sizes, models

### 10. [数据如何影响 RoPE 频率使用：从位置尺度匹配到长度概括](https://arxiv.org/abs/2607.07678v1)
- Original title: How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length Generalization
- Authors: Xinyi Wu, Siyuan Liu, Ali Jadbabaie
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 旋转位置嵌入 (RoPE) 为变压器提供了固定的位置频率网格，但经过训练的模型使用这些频率的程度非常不均匀。我们研究了决定这种频率使用的因素，并提出了一种以数据为中心的解释：选择 RoPE 频率来匹配训练数据的相对距离结构。将每个频率视为位置透镜，我们形式化了场分辨率权衡，并表明，对于宽度为 $W$ 的数据引起的依赖性剖面，最佳频率缩放为 $1/W$。这种频率匹配原理解释了对合成数据和基于文本的数据的受控观察，并表明在语言模型中观察到的中低频段源于自然语言的多尺度依赖结构。
- Abstract: Rotary Position Embeddings (RoPE) provide transformers with a fixed grid of positional frequencies, yet trained models use these frequencies highly non-uniformly. We study what determines this frequency usage and propose a data-centered explanation: RoPE frequencies are selected to match the relative-distance structure of the training data. Viewing each frequency as a positional lens, we formalize a field-resolution...
- Summary (fallback): 机器翻译摘要显示：旋转位置嵌入 (RoPE) 为变压器提供了固定的位置频率网格，但经过训练的模型使用这些频率的程度非常不均匀。我们研究了决定这种频率使用的因素，并提出了一种以数据为中心的解释：选择 RoPE 频率来匹配训练数据的相对距离结构。将每个频率视为位置透镜，我们形式化了场分辨率权衡，并表明，对于宽度为 $W$ 的数据引起的依赖性剖面，最佳频率缩放为 $1/W$。这种频率匹配原理解释了对合成数据和基于文本的数据的受控观察，并表明在语言模型中观察到的中低频段源于自然语言的多尺度依赖结构。
- Keywords: frequency, frequencies, rope, positional, generalization

### 11. [重新思考细菌糖代谢的选择行为](https://arxiv.org/abs/2607.07677v1)
- Original title: Rethinking the Choice Behavior of Sugar Metabolism in Bacteria
- Authors: Jeffrey D. Varner
- Meta: 2026-07-08 | q-bio.QM
- 中文摘要: Ramkrishna、Kompala 和 Tsao 提出了微生物生长的控制论模型，其中细胞根据模仿理性决策的匹配规则分配酶合成资源。后来证明，在有关潜在投资回报结构的一般假设下，匹配规则是最优的，但单元最大化的具体目标以及限制该选择的约束从未被写为明确的经济决策。在这里，我们提供了这个缺失的决策，将控制论酶合成控制重塑为微观经济学理论中的消费者选择问题：细胞将有限的蛋白质组预算在竞争性分解代谢酶之间分配为线性程序（LP），在线性蛋白质组预算约束下最大化线性增长效用。
- Abstract: Ramkrishna, Kompala, and Tsao proposed the cybernetic model of microbial growth, in which cells allocate enzyme synthesis resources according to a matching rule that mimics rational decision-making. The matching rule was later shown to be optimal under general assumptions about the underlying return-on-investment structure, yet the specific objective the cell maximizes, and the constraints bounding that choice, were...
- Summary (fallback): 机器翻译摘要显示：Ramkrishna、Kompala 和 Tsao 提出了微生物生长的控制论模型，其中细胞根据模仿理性决策的匹配规则分配酶合成资源。后来证明，在有关潜在投资回报结构的一般假设下，匹配规则是最优的，但单元最大化的具体目标以及限制该选择的约束从未被写为明确的经济决策。在这里，我们提供了这个缺失的决策，将控制论酶合成控制重塑为微观经济学理论中的消费者选择问题：细胞将有限的蛋白质组预算在竞争性分解代谢酶之间分配为线性程序（LP），在线性蛋白质组预算约束下最大化线性增长效用。
- Keywords: budget, choice, growth, linear, corner

### 12. [最大化 GRPO 信号：针对硬推理问题的自适应跟踪前缀控制](https://arxiv.org/abs/2607.07674v1)
- Original title: Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning Problems
- Authors: Vladislav Beliaev
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 组相对策略优化（GRPO）在模型最难的问题上停滞不前：当组中没有成功推出时，组相对优势就会消失，问题不会贡献梯度，浪费了我们最想学习的前沿示例。在参考解决方案前面添加正确的前缀可以提高成功率，使前缀长度成为难度的连续旋钮。并发方法设置旋钮一次； AdaPrefix-GRPO 将其变成反馈控制器：在整个训练过程中，它会调整每个问题获得的解决方案的数量，将其成功率保持在 50% 附近，其中 GRPO 的梯度信号最大，然后完全撤回辅助，因此部署的模型可以独立解决问题。
- Abstract: Group Relative Policy Optimization (GRPO) stalls on a model's hardest problems: when no rollout in a group succeeds, the group-relative advantages vanish and the problem contributes no gradient, wasting the frontier examples we most want to learn from. Prepending a correct prefix of a reference solution raises the success rate, making prefix length a continuous knob on difficulty. Concurrent methods set the knob onc...
- Summary (fallback): 机器翻译摘要显示：组相对策略优化（GRPO）在模型最难的问题上停滞不前：当组中没有成功推出时，组相对优势就会消失，问题不会贡献梯度，浪费了我们最想学习的前沿示例。在参考解决方案前面添加正确的前缀可以提高成功率，使前缀长度成为难度的连续旋钮。并发方法设置旋钮一次； AdaPrefix-GRPO 将其变成反馈控制器：在整个训练过程中，它会调整每个问题获得的解决方案的数量，将其成功率保持在 50% 附近，其中 GRPO 的梯度信号最大，然后完全撤回辅助，因此部署的模型可以独立解决问题。
- Keywords: grpo, prefix, problems, model, training

### 13. [MedPMC：用于扩展基础模型高保真医学多模态数据的系统框架](https://arxiv.org/abs/2607.07673v1)
- Original title: MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models
- Authors: Hyunjae Kim, Dain Kim, Pan Xiao, Serina S. Applebaum, Younjoon Chung et al.
- Meta: 2026-07-08 | cs.CV
- 中文摘要: 医学本质上是多模式的，要求临床医生综合不同数据流的信息。然而，多模式基础模型的发展受到大规模、高质量临床数据的限制。尽管 PubMed Central (PMC) 提供了专家创作的图像文本数据的补充来源，但现有的 PMC 衍生资源在保真度、再现性和临床验证方面仍然有限。我们推出 MedPMC，这是一个自动化、可持续更新的框架，可将许可的文献转化为医疗多模式模型的高保真基础设施。 MedPMC 应用于 610 万篇 PMC 文章，策划了 1100 万个医学图像-文本对。
- Abstract: Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and cli...
- Summary (fallback): 机器翻译摘要显示：医学本质上是多模式的，要求临床医生综合不同数据流的信息。然而，多模式基础模型的发展受到大规模、高质量临床数据的限制。尽管 PubMed Central (PMC) 提供了专家创作的图像文本数据的补充来源，但现有的 PMC 衍生资源在保真度、再现性和临床验证方面仍然有限。我们推出 MedPMC，这是一个自动化、可持续更新的框架，可将许可的文献转化为医疗多模式模型的高保真基础设施。 MedPMC 应用于 610 万篇 PMC 文章，策划了 1100 万个医学图像-文本对。
- Keywords: medical, multimodal, models, medpmc, across

### 14. [Peter：概率电路的训练后鲁棒性](https://arxiv.org/abs/2607.07671v1)
- Original title: PeTeR: Post-Training Robustification of Probabilistic Circuits
- Authors: Adrian Ciotinga, Yeming Dai, YooJung Choi
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 概率电路 (PC) 可以对复杂的联合分布进行建模，同时支持许多推理查询的精确高效计算。然而，当面临数据噪声、小样本量或分布变化时，标准的基于可能性的 PC 学习很容易出现过度拟合和脆弱的泛化。这可以通过使用分布稳健优化来缓解，该优化考虑经验分布的 Wasserstein 球内的最坏情况分布，但当前的方法仅限于在此框架中从头开始训练模型。相反，我们提出了 PeTeR：一种新颖的、无数据的后训练框架，旨在增强预训练的 PC 的能力以应对分布变化，而无需从头开始重新训练。
- Abstract: Probabilistic circuits (PCs) can model complex joint distributions while supporting exact and efficient computation of many inference queries. However, standard likelihood-based PC learning is vulnerable to overfitting and fragile generalization when confronted with data noise, small sample sizes, or distribution shifts. This can be mitigated using distributionally-robust optimization which consider worst-case distr...
- Summary (fallback): 机器翻译摘要显示：概率电路 (PC) 可以对复杂的联合分布进行建模，同时支持许多推理查询的精确高效计算。然而，当面临数据噪声、小样本量或分布变化时，标准的基于可能性的 PC 学习很容易出现过度拟合和脆弱的泛化。这可以通过使用分布稳健优化来缓解，该优化考虑经验分布的 Wasserstein 球内的最坏情况分布，但当前的方法仅限于在此框架中从头开始训练模型。相反，我们提出了 PeTeR：一种新颖的、无数据的后训练框架，旨在增强预训练的 PC 的能力以应对分布变化，而无需从头开始重新训练。
- Keywords: peter, distribution, post-training, probabilistic, circuits

### 15. [别利克知道它不知道的事情吗？激活离散度将模型尺度上的实体熟悉度与事实可靠性分开](https://arxiv.org/abs/2607.07670v1)
- Original title: Does Bielik Know What It Doesn't Know? Activation Dispersion Separates Entity Familiarity from Factual Reliability Across Model Scale
- Authors: Grzegorz Brzezinka
- Meta: 2026-07-08 | cs.CL
- 中文摘要: 大型语言模型对它们从未见过的实体产生最多的幻觉。我们询问在生成单个答案标记之前模型的激活是否背叛了实体熟悉度，以及该信号是否预测了答案的事实可靠性。在四个波兰 Bielik 模型（1.5B-11B 参数）上，我们探测了四个实体域（运动员、城市、作家、音乐家），每个域都有 42 个众所周知的实体、42 个模糊但真实的实体以及 42 个由一句话问题解决的虚构实体（每个模型 504 个提示）。针对 SwiGLU MLP 激活后的两个无监督、单前向色散测量、逆参与比和谱熵，在所有域和尺度上与 AUROC 0.95-1.00 的制造实体分开已知；受监督的线性探针达到 0.99-1.00。
- Abstract: Large language models hallucinate most about entities they have never seen. We ask whether a model's activations betray entity familiarity before a single answer token is generated, and whether that signal predicts the factual reliability of the answers. On four Polish Bielik models (1.5B-11B parameters), we probe four entity domains (athletes, cities, writers, musicians), each with 42 well-known, 42 obscure-but-rea...
- Summary (fallback): 机器翻译摘要显示：大型语言模型对它们从未见过的实体产生最多的幻觉。我们询问在生成单个答案标记之前模型的激活是否背叛了实体熟悉度，以及该信号是否预测了答案的事实可靠性。在四个波兰 Bielik 模型（1.5B-11B 参数）上，我们探测了四个实体域（运动员、城市、作家、音乐家），每个域都有 42 个众所周知的实体、42 个模糊但真实的实体以及 42 个由一句话问题解决的虚构实体（每个模型 504 个提示）。针对 SwiGLU MLP 激活后的两个无监督、单前向色散测量、逆参与比和谱熵，在所有域和尺度上与 AUROC 0.95-1.00 的制造实体分开已知；受监督的线性探针达到 0.99-1.00。
- Keywords: entity, factual, reliability, across, models

### 16. [分层内存架构克服了长视野多智能体计算建模中的上下文限制](https://arxiv.org/abs/2607.07666v1)
- Original title: A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling
- Authors: Shivendra G. Tewari, Holly Kimko
- Meta: 2026-07-08 | q-bio.QM
- 中文摘要: 大型语言模型 (LLM) 展示了卓越的推理能力，但其无状态架构从根本上限制了在需要多会话连续性和定量严谨性的长期研究工作流程中的部署。在这里，我们介绍了 Ensemble QSP，这是一个多代理框架，具有三层分层内存架构，通过限制每个状态类别并逐出已完成的工作，在项目持续时间（中期项目状态：中位数 301 个令牌，最多 4,050 个令牌，最多 4,050 个运行）中保持注入的上下文有界和恒定，从而实现连续自主操作而不会降低上下文。该系统在领域专家主要调查员的领导下协调五个专业工作代理，通过基于物理的检查表和结构化领域知识强制实施物理约束。
- Abstract: Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session continuity and quantitative rigor. Here we present Ensemble QSP, a multi-agent framework featuring a three-layer hierarchical memory architecture that keeps injected context bounded and constant in project duration (mid...
- Summary (fallback): 机器翻译摘要显示：大型语言模型 (LLM) 展示了卓越的推理能力，但其无状态架构从根本上限制了在需要多会话连续性和定量严谨性的长期研究工作流程中的部署。在这里，我们介绍了 Ensemble QSP，这是一个多代理框架，具有三层分层内存架构，通过限制每个状态类别并逐出已完成的工作，在项目持续时间（中期项目状态：中位数 301 个令牌，最多 4,050 个令牌，最多 4,050 个运行）中保持注入的上下文有界和恒定，从而实现连续自主操作而不会降低上下文。该系统在领域专家主要调查员的领导下协调五个专业工作代理，通过基于物理的检查表和结构化领域知识强制实施物理约束。
- Keywords: across, architecture, context, hierarchical, memory

### 17. [指导打破了安装的操作员：无分类器指导的终端安装修复](https://arxiv.org/abs/2607.07665v1)
- Original title: Guidance Breaks the Fitted Operator: A Terminal-Fitted Repair for Classifier-Free Guidance
- Authors: Shiheng Zhang
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 无分类器指导（CFG）是在扩散和流量匹配采样器中加强类别调节的标准方法，但在很大程度上，它会过度饱和并不稳定，从业者会通过更多步骤或有限的间隔时间表来抑制症状。我们通过渐近保持的数值分析镜头来分析 CFG。基于最近的结果，即确定性 DDIM 步骤是无引导终端层的独特拟合算子，精确地在采样的最终小西格玛延伸上，我们表明引导将判别子空间精确地重新强化到异常指数 1+w。因此，DDIM 不再适合那里，并且在粗网格上，当 sigma_min 变为零时，其引导残差会发散。
- Abstract: Classifier-free guidance (CFG) is the standard way to strengthen class-conditioning in diffusion and flow-matching samplers, yet at large guidance it oversaturates and destabilizes, symptoms practitioners suppress with more steps or limited-interval schedules. We analyze CFG through an asymptotic-preserving, numerical-analysis lens. Building on a recent result that the deterministic DDIM step is the unique fitted op...
- Summary (fallback): 机器翻译摘要显示：无分类器指导（CFG）是在扩散和流量匹配采样器中加强类别调节的标准方法，但在很大程度上，它会过度饱和并不稳定，从业者会通过更多步骤或有限的间隔时间表来抑制症状。我们通过渐近保持的数值分析镜头来分析 CFG。基于最近的结果，即确定性 DDIM 步骤是无引导终端层的独特拟合算子，精确地在采样的最终小西格玛延伸上，我们表明引导将判别子空间精确地重新强化到异常指数 1+w。因此，DDIM 不再适合那里，并且在粗网格上，当 sigma_min 变为零时，其引导残差会发散。
- Keywords: guidance, guided, fitted, ddim, sigma

### 18. [Pic2Spec：生成建模从明场图像重建单细胞拉曼指纹](https://arxiv.org/abs/2607.07651v1)
- Original title: Pic2Spec: Generative Modeling Reconstructs Single Cell Raman Fingerprints from Brightfield Images
- Authors: Srilakshmi Premachandran, Amit Kumar Bhuyan, Loza F. Tadesse
- Meta: 2026-07-08 | physics.optics
- 中文摘要: 由于标记要求、有限的多重分析以及干扰生理学的试剂，单细胞分子表征仍然是可扩展生物分析的瓶颈。拉曼光谱通过提供化学特异性、无标记振动指纹来解决这些限制，但较长的采集时间和专用仪器限制了高通量的使用。在这里，我们通过证明可以使用生成模型从明场显微镜重建光谱指纹来克服这一障碍。我们推出了 Pic2Spec，这是一个学习共享潜在生化表示的框架，将图像形态与振动光谱结构联系起来，无需硬件即可实现虚拟拉曼光谱。
- Abstract: Single-cell molecular characterization remains a bottleneck in scalable biological analysis because of labeling requirements, limited multiplexing, and reagents that perturb physiology. Raman spectroscopy addresses these limits by providing chemically specific, label-free vibrational fingerprints, but long acquisition times and specialized instruments restrict high-throughput use. Here, we overcome this barrier by s...
- Summary (fallback): 机器翻译摘要显示：由于标记要求、有限的多重分析以及干扰生理学的试剂，单细胞分子表征仍然是可扩展生物分析的瓶颈。拉曼光谱通过提供化学特异性、无标记振动指纹来解决这些限制，但较长的采集时间和专用仪器限制了高通量的使用。在这里，我们通过证明可以使用生成模型从明场显微镜重建光谱指纹来克服这一障碍。我们推出了 Pic2Spec，这是一个学习共享潜在生化表示的框架，将图像形态与振动光谱结构联系起来，无需硬件即可实现虚拟拉曼光谱。
- Keywords: pic2spec, raman, fingerprints, molecular, spectroscopy

### 19. [ALER-TI：时间序列插补的对齐潜在嵌入检索](https://arxiv.org/abs/2607.07640v1)
- Original title: ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation
- Authors: Xuan-Thong Truong, Trung-Kien Le, Tung Kieu, Thi-Thu Nguyen, Nhat-Hai Nguyen
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 深度学习具有显着先进的时间序列插补，但大多数现有架构主要依赖于损坏的输入序列中的局部时间上下文。这种依赖性在现实世界场景中可能会受到限制，其中时间序列通常表现出非平稳动态、弱时间相关性以及难以仅根据附近观测来重建的罕见模式。在本文中，我们提出了 ALER-TI（用于时间序列插补的对齐潜在嵌入检索），这是一种检索增强框架，明确利用历史模式来补充退化的局部上下文，以实现更可靠的缺失值重建。 ALER-TI 的核心是潜在嵌入对齐 (LEA)，它可以减轻损坏的查询和完整的历史候选之间的表示不匹配。
- Abstract: Deep learning has significantly advanced time series imputation, yet most existing architectures primarily rely on localized temporal context within the corrupted input sequence. This reliance can be limiting in real-world scenarios, where time series often exhibit non-stationary dynamics, weak temporal correlations, and infrequent patterns that are difficult to reconstruct from nearby observations alone. In this pa...
- Summary (fallback): 机器翻译摘要显示：深度学习具有显着先进的时间序列插补，但大多数现有架构主要依赖于损坏的输入序列中的局部时间上下文。这种依赖性在现实世界场景中可能会受到限制，其中时间序列通常表现出非平稳动态、弱时间相关性以及难以仅根据附近观测来重建的罕见模式。在本文中，我们提出了 ALER-TI（用于时间序列插补的对齐潜在嵌入检索），这是一种检索增强框架，明确利用历史模式来补充退化的局部上下文，以实现更可靠的缺失值重建。 ALER-TI 的核心是潜在嵌入对齐 (LEA)，它可以减轻损坏的查询和完整的历史候选之间的表示不匹配。
- Keywords: aler-ti, imputation, latent, time, series

### 20. [具有后验误差估计的神经网络架构自适应的最优控制方法](https://arxiv.org/abs/2607.07637v1)
- Original title: An optimal control approach for neural network architecture adaptation with a posteriori error estimation
- Authors: C G Krishnanunni, Thomas Scott, Tan Bui-Thanh
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 这项工作提出了一种基于后验误差估计沿深度调整神经网络架构的新颖方法。通过将神经网络训练表述为连续时间最优控制问题，我们得出了严格的误差估计，量化了近似误差在网络层中的分布情况。这种误差分解实现了有原则的深度适应策略：在最大估计误差的位置插入新层，使网络能够有效地捕获潜在问题中复杂的非线性变化。我们的框架引入了一种新颖的网络架构，它将权重和偏差视为跨层变化的分段线性函数，误差估计器限制了这种离散表示与真正的连续最优控制解决方案之间的差异。
- Abstract: This work presents a novel approach for adapting neural network architecture along the depth based on a posteriori error estimation. By formulating neural network training as a continuous-time optimal control problem, we derive rigorous error estimates that quantify how approximation error distributes across network layers. This error decomposition enables a principled depth adaptation strategy: new layers are inser...
- Summary (fallback): 机器翻译摘要显示：这项工作提出了一种基于后验误差估计沿深度调整神经网络架构的新颖方法。通过将神经网络训练表述为连续时间最优控制问题，我们得出了严格的误差估计，量化了近似误差在网络层中的分布情况。这种误差分解实现了有原则的深度适应策略：在最大估计误差的位置插入新层，使网络能够有效地捕获潜在问题中复杂的非线性变化。我们的框架引入了一种新颖的网络架构，它将权重和偏差视为跨层变化的分段线性函数，误差估计器限制了这种离散表示与真正的连续最优控制解决方案之间的差异。
- Keywords: error, network, architecture, approach, optimal

### 21. [通过黎曼法线坐标对 Levenberg-Marquardt 方法进行高阶几何更新](https://arxiv.org/abs/2607.07623v1)
- Original title: Higher-Order Geometric Updates for Levenberg-Marquardt Method via Riemann Normal Coordinates
- Authors: Jianing Liu, Dong H. Zhang
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 非线性最小二乘优化是回归、基于物理的神经网络和其他机器学习任务的核心。此类问题具有自然的几何解释，模型预测在数据空间中形成流形，而所选的参数化可能会引入参数效应曲率，从而成为非线性的主要来源。这暴露了 Levenberg-Marquardt (LM) 方法的局限性，其切线空间步骤被应用为参数坐标的直接更新。测地加速度提供二阶校正，但其参数效应曲率的消除仅在无穷小步长限制下是精确的。我们提出了黎曼正态坐标 Levenberg-Marquardt 方法 (RNC-LM) 来提高有限优化步骤的一致性。
- Abstract: Nonlinear least-squares optimization is central to regression, physics-informed neural networks, and other machine-learning tasks. Such problems have a natural geometric interpretation, model predictions form a manifold in data space, while the chosen parameterization can introduce parameter-effects curvature that becomes a dominant source of nonlinearity. This exposes a limitation of the Levenberg-Marquardt (LM) me...
- Summary (fallback): 机器翻译摘要显示：非线性最小二乘优化是回归、基于物理的神经网络和其他机器学习任务的核心。此类问题具有自然的几何解释，模型预测在数据空间中形成流形，而所选的参数化可能会引入参数效应曲率，从而成为非线性的主要来源。这暴露了 Levenberg-Marquardt (LM) 方法的局限性，其切线空间步骤被应用为参数坐标的直接更新。测地加速度提供二阶校正，但其参数效应曲率的消除仅在无穷小步长限制下是精确的。我们提出了黎曼正态坐标 Levenberg-Marquardt 方法 (RNC-LM) 来提高有限优化步骤的一致性。
- Keywords: method, levenberg-marquardt, geodesic, acceleration, rnc-lm

### 22. [非对称焦点损失改善了药物-药物相互作用的图神经网络预测](https://arxiv.org/abs/2607.07611v1)
- Original title: Asymmetric Focal Loss Improves Graph Neural Network Prediction of Drug-Drug Interactions
- Authors: Faranak Hatami, Mousa Moradi
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 背景：图神经网络改进了多药副作用的计算预测，但标准二元交叉熵训练为分类良好且困难的示例分配了相同的容量，可能会丢失临床上重要的相互作用。我们评估了不对称焦点目标是否可以通过强调困难的正相互作用来改善多关系药物相互作用（DDI）预测。方法：使用分子指纹、物理化学描述符和学习嵌入将 ClinicalFocal 损失集成到关系感知图卷积网络中。该模型在 TWOSIDES 上使用五重交叉验证和相同的实验条件（架构、特征、数据分区、超参数和随机种子）对 ClinicalFocal 损失和二元交叉熵基线进行评估。
- Abstract: Background: Graph neural networks improve computational prediction of polypharmacy side effects, but standard binary cross-entropy training allocates equal capacity to well-classified and difficult examples, potentially missing clinically significant interactions. We evaluated whether an asymmetric focal objective could improve multi-relational drug-drug interaction (DDI) prediction by emphasizing difficult positive...
- Summary (fallback): 机器翻译摘要显示：背景：图神经网络改进了多药副作用的计算预测，但标准二元交叉熵训练为分类良好且困难的示例分配了相同的容量，可能会丢失临床上重要的相互作用。我们评估了不对称焦点目标是否可以通过强调困难的正相互作用来改善多关系药物相互作用（DDI）预测。方法：使用分子指纹、物理化学描述符和学习嵌入将 ClinicalFocal 损失集成到关系感知图卷积网络中。该模型在 TWOSIDES 上使用五重交叉验证和相同的实验条件（架构、特征、数据分区、超参数和随机种子）对 ClinicalFocal 损失和二元交叉熵基线进行评估。
- Keywords: loss, prediction, increased, asymmetric, focal

### 23. [由参考和记忆引导的心脏 MRI 平面超分辨率](https://arxiv.org/abs/2607.07581v1)
- Original title: Cardiac MRI Through-Plane Super-Resolution Guided by Reference and Memory
- Authors: Shaoming Pan, Chenchuhui Hu, Leon Axel, Meng Ye
- Meta: 2026-07-08 | cs.CV
- 中文摘要: 临床心脏 MRI 通常以高平面内分辨率和粗平面分辨率采集，以减少扫描时间并适应屏气和心脏运动限制，从而限制了 3D 分析和诊断准确性。我们提出了 STRMSR，一种参考和记忆引导的贯通平面超分辨率 (SR) 框架，它通过利用从同一受试者获取的 HR 参考视图和作为记忆的中间 SR 结果来重建高分辨率 (HR) 心脏体积。我们的方法使用从粗到细的上下文匹配来在空间失准的情况下在低分辨率目标和参考/内存图像之间建立鲁棒的对应关系。可学习的补丁式动态特征聚合模块可以预测每个局部补丁的内容自适应混合权重，有效地融合动态信息，同时抑制不可靠的特征传输。
- Abstract: Clinical cardiac MRI is commonly acquired with high in-plane resolution but coarse through-plane resolution to reduce scan time and accommodate breath-hold and cardiac-motion constraints, which limits 3D analysis and diagnostic accuracy. We propose STRMSR, a reference- and memory-guided through-plane super-resolution (SR) framework that reconstructs high-resolution (HR) cardiac volumes by leveraging HR reference vie...
- Summary (fallback): 机器翻译摘要显示：临床心脏 MRI 通常以高平面内分辨率和粗平面分辨率采集，以减少扫描时间并适应屏气和心脏运动限制，从而限制了 3D 分析和诊断准确性。我们提出了 STRMSR，一种参考和记忆引导的贯通平面超分辨率 (SR) 框架，它通过利用从同一受试者获取的 HR 参考视图和作为记忆的中间 SR 结果来重建高分辨率 (HR) 心脏体积。我们的方法使用从粗到细的上下文匹配来在空间失准的情况下在低分辨率目标和参考/内存图像之间建立鲁棒的对应关系。可学习的补丁式动态特征聚合模块可以预测每个局部补丁的内容自适应混合权重，有效地融合动态信息，同时抑制不可靠的特征传输。
- Keywords: cardiac, reference, memory, through-plane, views

### 24. [通过转移概率相关性进行自动超声心动图分割以实现稳定的语义提取](https://arxiv.org/abs/2607.07580v1)
- Original title: Automatic Echocardiography Segmentation via Transition Probability Correlation for Stable Semantic Extraction
- Authors: Xinran Chen, Xiyuan Wang, Guangquan Zhou, Chuan Chen
- Meta: 2026-07-08 | cs.CV
- 中文摘要: 虽然超声心动图对于心血管诊断至关重要，但固有的散斑噪声和低信噪比常常导致模糊的语义特征和支离破碎的边界。这些限制极大地阻碍了深度学习模型在复杂临床病例中的分割准确性。此外，心脏的时间运动在识别解剖结构中起着至关重要的作用。为了解决这些挑战，我们设计了一个 STLSF 模块，其中包括基于窗口匹配的语义校正组件和语义引导的纹理增强组件。通过利用局部转移概率相关性来纠正语义并采用语义引导的纹理增强，STLSF 模块有效地减轻了由于超声心动图质量较差而导致的纹理不稳定和语义解释模糊。
- Abstract: While echocardiography is essential for cardiovascular diagnosis, inherent speckle noise and low signal-to-noise ratio often lead to ambiguous semantic features and fragmented boundaries. These limitations significantly hinder the segmentation accuracy of deep learning models in complex clinical cases. Moreover, temporal motion of the heart plays a critical role in recognizing anatomical structures. To address these...
- Summary (fallback): 机器翻译摘要显示：虽然超声心动图对于心血管诊断至关重要，但固有的散斑噪声和低信噪比常常导致模糊的语义特征和支离破碎的边界。这些限制极大地阻碍了深度学习模型在复杂临床病例中的分割准确性。此外，心脏的时间运动在识别解剖结构中起着至关重要的作用。为了解决这些挑战，我们设计了一个 STLSF 模块，其中包括基于窗口匹配的语义校正组件和语义引导的纹理增强组件。通过利用局部转移概率相关性来纠正语义并采用语义引导的纹理增强，STLSF 模块有效地减轻了由于超声心动图质量较差而导致的纹理不稳定和语义解释模糊。
- Keywords: semantic, echocardiography, texture, segmentation, transition

### 25. [限制下单个极化细胞的方向偏差](https://arxiv.org/abs/2607.07578v1)
- Original title: Directional bias of a single polarized cell under confinement
- Authors: Andreas Buttenschön, Calina Copos
- Meta: 2026-07-08 | physics.bio-ph
- 中文摘要: 从旋转细菌菌落到组织形态发生和细胞骨架组织的各种过程中都观察到了手性模式，但手性细胞运动背后的物理机制仍然知之甚少。在证明受限细胞圆周运动中方向偏差的实验的推动下，我们使用动力系统分析工具和计算机模拟来识别能够产生持续偏差迁移的最小内在和外在机制。动力系统框架揭示了一个共同的组织原则：方向偏差是通过顺时针和逆时针运动状态的稳定性和/或吸引力盆地的变化而出现的。我们发现了导致这种偏见的四种不同途径。首先，极化细胞骨架中的内在扭矩可以在空间上积分以产生偏置的圆周运动。
- Abstract: Chiral patterns have been observed in various processes from swirling bacterial colonies to tissue morphogenesis and cytoskeletal organization, yet the physical mechanisms underlying chiral cell motion remain poorly understood. Motivated by experiments demonstrating directional bias in the circular motion of confined cells, we use the tools of dynamical systems analysis with computer simulations to identify minimal...
- Summary (fallback): 机器翻译摘要显示：从旋转细菌菌落到组织形态发生和细胞骨架组织的各种过程中都观察到了手性模式，但手性细胞运动背后的物理机制仍然知之甚少。在证明受限细胞圆周运动中方向偏差的实验的推动下，我们使用动力系统分析工具和计算机模拟来识别能够产生持续偏差迁移的最小内在和外在机制。动力系统框架揭示了一个共同的组织原则：方向偏差是通过顺时针和逆时针运动状态的稳定性和/或吸引力盆地的变化而出现的。我们发现了导致这种偏见的四种不同途径。首先，极化细胞骨架中的内在扭矩可以在空间上积分以产生偏置的圆周运动。
- Keywords: directional, bias, chiral, motion, mechanisms

### 26. [用于 CVE 到 CWE 映射的多类与多标签 BERT：分类结构如何塑造错误](https://arxiv.org/abs/2607.07573v1)
- Original title: Multi-Class vs. Multi-Label BERT for CVE-to-CWE Mapping: How Taxonomy Structure Shapes the Errors
- Authors: Ana Schwengber Kelm, Christian Bockermann, Jörg Frochte
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 将常见漏洞枚举 (CWE) 类别分配给常见漏洞和暴露 (CVE) 记录仍然是漏洞分析中的一个重要步骤，但主要是手动步骤。我们将此任务作为文本分类问题进行研究，并比较两种建模选择：预测每个 CVE 的单个 CWE 的 \emph{multi-class} 公式和允许多个分配的 \emph{multi-label} 公式。在三个嵌套标签空间（83、47 和 25 类）上评估三个 Transformer 编码器（BERT Base、SecureBERT 和 CySecBERT）。多类训练在所有设置中都实现了更高的宏观 F1，尽管随着标签空间的缩小，与多标签的差距从 21 个百分点缩小到 2 个百分点。多标签方面的事后阈值优化弥补了 25 类设置上的这一差距。
- Abstract: Assigning Common Weakness Enumeration (CWE) categories to Common Vulnerabilities and Exposures (CVE) records remains an important but largely manual step in vulnerability analysis. We study this task as a text classification problem and compare two modelling choices: a \emph{multi-class} formulation that predicts a single CWE per CVE and a \emph{multi-label} formulation that allows multiple assignments. Three transf...
- Summary (fallback): 机器翻译摘要显示：将常见漏洞枚举 (CWE) 类别分配给常见漏洞和暴露 (CVE) 记录仍然是漏洞分析中的一个重要步骤，但主要是手动步骤。我们将此任务作为文本分类问题进行研究，并比较两种建模选择：预测每个 CVE 的单个 CWE 的 \emph{multi-class} 公式和允许多个分配的 \emph{multi-label} 公式。在三个嵌套标签空间（83、47 和 25 类）上评估三个 Transformer 编码器（BERT Base、SecureBERT 和 CySecBERT）。多类训练在所有设置中都实现了更高的宏观 F1，尽管随着标签空间的缩小，与多标签的差距从 21 个百分点缩小到 2 个百分点。多标签方面的事后阈值优化弥补了 25 类设置上的这一差距。
- Keywords: multi-label, multi-class, three, bert, taxonomy

### 27. [联邦学习中知识转移的协作合成数据生成](https://arxiv.org/abs/2607.07565v1)
- Original title: Collaborative Synthetic Data Generation for Knowledge Transfer in Federated Learning
- Authors: Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek
- Meta: 2026-07-08 | cs.LG
- 中文摘要: 一次性联邦学习 (OSFL) 通过将训练限制为单轮来解决联邦学习的通信开销，但在不牺牲模型质量的情况下这样做是很重要的，特别是当客户端数据分布存在分歧时。最近的工作通过构建可转移的合成数据集或蒸馏数据在服务器上聚合客户端知识来解决这一挑战。然而，这些方法大多数缺乏正式的隐私保证，在共同实现低通信、对异质性的鲁棒性和严格的隐私方面存在差距。我们提出了 FedKT-CSD（通过协作合成数据进行联合知识转移），这是一个受神经图像压缩启发的框架，它通过利用公开预训练的自动编码器作为共享潜在空间来缩小这一差距。
- Abstract: One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, particularly when client data distributions diverge. Recent work has addressed this challenge by aggregating client knowledge on the server through the construction of transferable synthetic datasets or distillates. Howeve...
- Summary (fallback): 机器翻译摘要显示：一次性联邦学习 (OSFL) 通过将训练限制为单轮来解决联邦学习的通信开销，但在不牺牲模型质量的情况下这样做是很重要的，特别是当客户端数据分布存在分歧时。最近的工作通过构建可转移的合成数据集或蒸馏数据在服务器上聚合客户端知识来解决这一挑战。然而，这些方法大多数缺乏正式的隐私保证，在共同实现低通信、对异质性的鲁棒性和严格的隐私方面存在差距。我们提出了 FedKT-CSD（通过协作合成数据进行联合知识转移），这是一个受神经图像压缩启发的框架，它通过利用公开预训练的自动编码器作为共享潜在空间来缩小这一差距。
- Keywords: privacy, synthetic, federated, knowledge, learning

### 28. [PALS：LLM 剪枝的百分位感知分层稀疏性](https://arxiv.org/abs/2607.07557v1)
- Original title: PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning
- Authors: Yazdan Jamshidi, Alexey Shvets
- Meta: 2026-07-08 | cs.CL
- 中文摘要: Wanda 和 SparseGPT 等一次性剪枝方法对变压器的每一层应用相同的稀疏率，忽略层重要性的已知变化。我们提出 PALS（Percentile-Aware Layerwise Sparsity），它根据激活幅度的第 99 个百分位数调整每层稀疏性，在目标比率周围限制为 $\pm 5\%$。在 LLaMA-2-7B 上，稀疏度为 50% 时，PALS 的 WikiText-2 困惑度为 10.96，而均匀 Wanda 的困惑度为 12.92（平均运行 9 次，$p < 0.001$）。好处取决于架构：LLaMA-3-8B 显示出边际收益，而 Mistral-7B 则没有显示。我们还发现基于梯度的分配（看似更有原则的方法）产生的结果比随机分配更糟糕，这表明梯度大小不能预测离散权重去除的影响。 PALS 给修剪管道增加的成本可以忽略不计，并且不需要微调。
- Abstract: One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance. We propose PALS (Percentile-Aware Layerwise Sparsity), which adjusts per-layer sparsity based on the 99th percentile of activation magnitudes, bounded to $\pm 5\%$ around the target ratio. On LLaMA-2-7B at 50\% sparsity, PALS achieves 10.96 WikiText-2 perplexi...
- Summary (fallback): 机器翻译摘要显示：Wanda 和 SparseGPT 等一次性剪枝方法对变压器的每一层应用相同的稀疏率，忽略层重要性的已知变化。我们提出 PALS（Percentile-Aware Layerwise Sparsity），它根据激活幅度的第 99 个百分位数调整每层稀疏性，在目标比率周围限制为 $\pm 5\%$。在 LLaMA-2-7B 上，稀疏度为 50% 时，PALS 的 WikiText-2 困惑度为 10.96，而均匀 Wanda 的困惑度为 12.92（平均运行 9 次，$p < 0.001$）。好处取决于架构：LLaMA-3-8B 显示出边际收益，而 Mistral-7B 则没有显示。我们还发现基于梯度的分配（看似更有原则的方法）产生的结果比随机分配更糟糕，这表明梯度大小不能预测离散权重去除的影响。 PALS 给...
- Keywords: sparsity, pals, pruning, percentile-aware, layerwise

### 29. [AA-ViT：具有结构和频率指导的解剖感知视觉变压器，用于对比增强脑 MRI 合成](https://arxiv.org/abs/2607.07553v1)
- Original title: AA-ViT: Anatomically Aware Vision Transformer with Structural and Frequency Guidance for Contrast Enhanced Brain MRI Synthesis
- Authors: Talha Meraj, Tom Flannery, Charlie Cummins, Matt Townend, Thomas C Booth et al.
- Meta: 2026-07-08 | cs.CV
- 中文摘要: 准确的肿瘤定位和诊断是脑癌临床护理的重要组成部分。磁共振成像 (MRI) 因其卓越的软组织对比度而成为最常用的成像方式。然而，标准 MRI 通常表现出有限的对比度和成像伪影，这需要使用造影剂来增强病变可见度。化学造影剂的施用并不总是可行，并且对于肾功能不全或其他健康状况的患者可能是禁忌的。因此，开发准确且非侵入性的对比增强磁共振成像（CEMRI）合成方法具有临床重要性。近年来，人们提出了多种 CEMRI 合成方法，主要依赖于生成人工智能模型。
- Abstract: Accurate tumour localization and diagnosis is a critical component of clinical care for brain cancers. Magnetic Resonance Imaging (MRI) is the most commonly used imaging modality due to its superior soft-tissue contrast. However, standard MRI often exhibits limited contrast and imaging artifacts, which necessitates the use of contrast agents to enhance lesion visibility. The administration of chemical contrast agent...
- Summary (fallback): 机器翻译摘要显示：准确的肿瘤定位和诊断是脑癌临床护理的重要组成部分。磁共振成像 (MRI) 因其卓越的软组织对比度而成为最常用的成像方式。然而，标准 MRI 通常表现出有限的对比度和成像伪影，这需要使用造影剂来增强病变可见度。化学造影剂的施用并不总是可行，并且对于肾功能不全或其他健康状况的患者可能是禁忌的。因此，开发准确且非侵入性的对比增强磁共振成像（CEMRI）合成方法具有临床重要性。近年来，人们提出了多种 CEMRI 合成方法，主要依赖于生成人工智能模型。
- Keywords: contrast, synthesis, clinical, imaging, agents

### 30. [农药风险评估中的等效性检验——设计、分析和解释的评估和实践指南](https://arxiv.org/abs/2607.07543v1)
- Original title: Equivalence testing in pesticide risk assessment -- Evaluation and practical guidance for design, analysis and interpretation
- Authors: Dimitry Wintermantel, Julia Osterman, Magdalena M. Mair, Florian Hartig
- Meta: 2026-07-08 | stat.ME
- 中文摘要: 在动力不足的实验设计中，超过特定保护目标 (SPG) 的有害农药效应可能无法被发现。监管蜜蜂实地研究始终未能达到欧洲食品安全局 (EFSA) 指导下所需的统计能力，这可能导致高风险物质获得批准。因此，欧洲食品安全局建议从检验“无效”的零假设转向等效检验。根据这种方法，如果可以拒绝农药效果超过 SPG 的零假设，则该农药被归类为“低风险”。对于蜜蜂，推荐的 SPG 是将蜂群大小减少到 10% 以下。批评者认为，该框架需要过度的位点复制来证明农药安全性，并提出了一种替代的等效测试，定义相对于 90% 对照组置信区间下限的治疗效果。
- Abstract: Harmful pesticide effects exceeding specific protection goals (SPG) may go undetected in underpowered experimental designs. Regulatory honeybee field studies have consistently failed to reach the statistical power required under European Food Safety Authority (EFSA) guidance, which may have caused approval of high-risk substances. Therefore, EFSA advised a shift from testing the null hypothesis of 'no effect' to equ...
- Summary (fallback): 机器翻译摘要显示：在动力不足的实验设计中，超过特定保护目标 (SPG) 的有害农药效应可能无法被发现。监管蜜蜂实地研究始终未能达到欧洲食品安全局 (EFSA) 指导下所需的统计能力，这可能导致高风险物质获得批准。因此，欧洲食品安全局建议从检验“无效”的零假设转向等效检验。根据这种方法，如果可以拒绝农药效果超过 SPG 的零假设，则该农药被归类为“低风险”。对于蜜蜂，推荐的 SPG 是将蜂群大小减少到 10% 以下。批评者认为，该框架需要过度的位点复制来证明农药安全性，并提出了一种替代的等效测试，定义相对于 90% 对照组置信区间下限的治疗效果。
- Keywords: equivalence, pesticide, testing, guidance, efsa

## biorxiv

### 1. [猪繁殖与呼吸综合征病毒三种群体水平监测方法的比较](https://www.biorxiv.org/content/10.64898/2026.03.31.713744v2)
- Original title: Comparison of Three Herd-Level Surveillance Methods for Porcine Reproductive and Respiratory Syndrome Virus
- Authors: Neujahr, A. C., Williams, T. E., DeMers, J. L., Barcal, B. M., Peterson, J. S. et al.
- Meta: 2026-07-09 | molecular biology | DOI: 10.64898/2026.03.31.713744
- 中文摘要: 猪繁殖与呼吸综合征病毒（PRRSV）给养猪业带来了相当大的健康和经济负担。强调疾病监测和缓解策略的重要性。因此，本研究旨在评估一种新的环境监测方法（称为 DARO 系统），以针对已建立的血清和口腔液方法检测 PRRSV。研究设计包括一头感染 PRRSV 的种猪和 46 头幼仔猪，每种监测方法均用于评估 PRRSV 检测的时间。结果显示，DARO Systems 监测方法比血清和口腔液监测方法早 1-2 天检测到 PRRSV。
- Abstract: Porcine Reproductive and Respiratory Syndrome Virus (PRRSV) represents a considerable health and economic burden for the swine production industry. highlighting the importance of disease surveillance and mitigation strategies. Accordingly, this study aimed to evaluate a novel environmental surveillance approach, referred to as DARO Systems, to detect PRRSV against established serum and oral fluids approaches. The st...
- Summary (fallback): 机器翻译摘要显示：猪繁殖与呼吸综合征病毒（PRRSV）给养猪业带来了相当大的健康和经济负担。强调疾病监测和缓解策略的重要性。因此，本研究旨在评估一种新的环境监测方法（称为 DARO 系统），以针对已建立的血清和口腔液方法检测 PRRSV。研究设计包括一头感染 PRRSV 的种猪和 46 头幼仔猪，每种监测方法均用于评估 PRRSV 检测的时间。结果显示，DARO Systems 监测方法比血清和口腔液监测方法早 1-2 天检测到 PRRSV。
- Keywords: surveillance, prrsv, approach, porcine, reproductive

### 2. [超越 Delta 质量：MS Andrea 直接解析开放搜​​索中的组合肽修饰](https://www.biorxiv.org/content/10.64898/2026.03.27.714851v2)
- Original title: Beyond Delta Masses: MS Andrea Directly Resolves Combinatorial Peptide Modifications in Open Searches
- Authors: Buur, L. M., Winkler, S., Dorfer, V.
- Meta: 2026-07-09 | molecular biology | DOI: 10.64898/2026.03.27.714851
- 中文摘要: 开放修饰搜索 (OMS) 策略在基于质谱的蛋白质组学中越来越受欢迎，用于识别携带未知或意外翻译后修饰的肽。然而，大多数 OMS 搜索引擎仅报告前体和匹配肽之间的总体质量差异，并且没有在肽谱匹配 (PSM) 水平上明确识别或评分多个修饰的组合，从而将质量变化的解释留给最终用户并使用下游分析工具。在这里，我们介绍 MS Andrea，这是一种新型 OMS 搜索引擎，旨在直接识别每个肽最多四个可变修饰的组合并对其进行评分，而无需预先定义它们。 MS Andrea 使用基于序列标签的策略在评分之前有效过滤候选肽。
- Abstract: Open modification search (OMS) strategies have gained popularity in mass spectrometry-based proteomics for identification of peptides carrying unknown or unexpected post-translational modifications. However, most OMS search engines report only the overall mass difference between the precursor and the matched peptide and do not explicitly identify or score combinations of multiple modifications at the peptide-spectru...
- Summary (fallback): 机器翻译摘要显示：开放修饰搜索 (OMS) 策略在基于质谱的蛋白质组学中越来越受欢迎，用于识别携带未知或意外翻译后修饰的肽。然而，大多数 OMS 搜索引擎仅报告前体和匹配肽之间的总体质量差异，并且没有在肽谱匹配 (PSM) 水平上明确识别或评分多个修饰的组合，从而将质量变化的解释留给最终用户并使用下游分析工具。在这里，我们介绍 MS Andrea，这是一种新型 OMS 搜索引擎，旨在直接识别每个肽最多四个可变修饰的组合并对其进行评分，而无需预先定义它们。 MS Andrea 使用基于序列标签的策略在评分之前有效过滤候选肽。
- Keywords: modifications, andrea, peptide, mass, directly

### 3. [精确靶向肌钙蛋白 I 磷酸化可预防舒张功能障碍，同时保持收缩性能](https://www.biorxiv.org/content/10.1101/2025.11.18.689162v3)
- Original title: Precision Targeting of Troponin I Phosphorylation Prevents Diastolic Dysfunction while Preserving Systolic Performance
- Authors: Chao, Y.-C., McAndrew, D. J., Revuelta, D., Yadav, R., Hong, W.-H. et al.
- Meta: 2026-07-09 | cell biology | DOI: 10.1101/2025.11.18.689162
- 中文摘要: 背景心脏舒张缺陷（舒张功能障碍）在心力衰竭中普遍存在，特别是在糖尿病、肥胖、高血压和衰老的情况下，并且与死亡率增加相关。然而，还没有直接针对这种异常放松的可用治疗方法。 cAMP 依赖性蛋白激酶 A (PKA) 磷酸化肌钙蛋白 I 可促进松弛，但整体 PKA 激活会产生广泛的不良影响。在这里，我们研究了选择性增强肌钙蛋白 I 磷酸化是否可以在不参与更广泛的 PKA 信号网络的情况下改善放松。方法为了解决亚细胞尺度的 cAMP 信号传导问题，我们将实时 cAMP 测量与针对特定纳米结构域的基于 FRET 的基因编码报告基因以及生化和遗传方法结合起来。
- Abstract: BackgroundDefective cardiac relaxation (diastolic dysfunction) is prevalent in heart failure, particularly in the context of diabetes, obesity, hypertension, and ageing, and is associated with increased mortality. Yet there is no available treatment that directly targets this abnormal relaxation. Phosphorylation of troponin I by cAMP-dependent protein kinase A (PKA) promotes relaxation, but global PKA activation has...
- Summary (fallback): 机器翻译摘要显示：背景心脏舒张缺陷（舒张功能障碍）在心力衰竭中普遍存在，特别是在糖尿病、肥胖、高血压和衰老的情况下，并且与死亡率增加相关。然而，还没有直接针对这种异常放松的可用治疗方法。 cAMP 依赖性蛋白激酶 A (PKA) 磷酸化肌钙蛋白 I 可促进松弛，但整体 PKA 激活会产生广泛的不良影响。在这里，我们研究了选择性增强肌钙蛋白 I 磷酸化是否可以在不参与更广泛的 PKA 信号网络的情况下改善放松。方法为了解决亚细胞尺度的 cAMP 信号传导问题，我们将实时 cAMP 测量与针对特定纳米结构域的基于 FRET 的基因编码报告基因以及生化和遗传方法结合起来。
- Keywords: troponin, relaxation, phosphorylation, camp, dysfunction

### 4. [miR-425-5p 通过调节视网膜母细胞瘤蛋白磷酸化来调节细胞衰老](https://www.biorxiv.org/content/10.64898/2026.06.15.732173v2)
- Original title: miR-425-5p Regulates Cellular Senescence Through Modulation of Retinoblastoma Protein Phosphorylation
- Authors: Matai, L., Haggenmueller, S., Lee, J. D., Slack, F. J.
- Meta: 2026-07-09 | cell biology | DOI: 10.64898/2026.06.15.732173
- 中文摘要: MicroRNA (miRNA) 是一种小型非编码 RNA，在调节细胞衰老和老化中发挥着关键作用。我们最近的研究发现了正常成年寿命所需的保守的秀丽隐杆线虫 miRNA 簇 (miR-229/64/65/66)，过度表达可显着延长寿命。值得注意的是，cel-miR-229 在人类中在进化上是保守的，而 hsa-miR-425 具有相同的种子序列。在这里，我们研究了 miR-425 在哺乳动物细胞衰老中的作用。我们发现，在药物诱导的人肺癌细胞衰老过程中，miR-425 的表达显着降低。 miR-425 表达的恢复可减轻衰老并抑制衰老诱导后衰老相关分泌表型 (SASP) 细胞因子的表达。
- Abstract: MicroRNAs (miRNAs) are small non-coding RNAs that play critical roles in regulating cellular senescence and aging. Our recent studies identified a conserved C. elegans miRNA cluster (miR-229/64/65/66) that is required for normal adult lifespan, with overexpression significantly extending longevity. Notably, cel-miR-229 is evolutionarily conserved in humans, with hsa-miR-425 sharing an identical seed sequence. Here,...
- Summary (fallback): 机器翻译摘要显示：MicroRNA (miRNA) 是一种小型非编码 RNA，在调节细胞衰老和老化中发挥着关键作用。我们最近的研究发现了正常成年寿命所需的保守的秀丽隐杆线虫 miRNA 簇 (miR-229/64/65/66)，过度表达可显着延长寿命。值得注意的是，cel-miR-229 在人类中在进化上是保守的，而 hsa-miR-425 具有相同的种子序列。在这里，我们研究了 miR-425 在哺乳动物细胞衰老中的作用。我们发现，在药物诱导的人肺癌细胞衰老过程中，miR-425 的表达显着降低。 miR-425 表达的恢复可减轻衰老并抑制衰老诱导后衰老相关分泌表型 (SASP) 细胞因子的表达。
- Keywords: senescence, mir-425, expression, cellular, phosphorylation

### 5. [高精度荧光引导冷冻聚焦离子束铣削](https://www.biorxiv.org/content/10.64898/2026.05.11.724418v2)
- Original title: High accuracy fluorescence-guided cryo-focused ion beam milling
- Authors: Perez, D., Betzler, S., Cleeve, P., Villegas, C., Antolini, C. et al.
- Meta: 2026-07-09 | cell biology | DOI: 10.64898/2026.05.11.724418
- 中文摘要: 冷冻电子断层扫描 (cryo-ET) 是一种直接可视化细胞内大分子结构的强大方法，但其更广泛的应用受到样品制备过程中难以可靠地定位特定结构的限制。特别是，在冷冻聚焦离子束 (cryo-FIB) 铣削片层中捕获小型或稀有物体仍然是一个主要瓶颈。在这里，我们提出了两种荧光引导的冷冻 FIB 铣削工作流程，这些工作流程克服了目标误差的关键来源，并能够在广泛的空间尺度上常规捕获结构。对于较大的目标（> 500 nm），我们提出了一种改进的基于配准的策略，将 FIB 铣削基准与折射率失配的深度校正相结合。
- Abstract: Cryo-electron tomography (cryo-ET) is a powerful approach for visualizing macromolecular structures directly within cells, but its broader application is limited by the difficulty of reliably targeting specific structures during sample preparation. In particular, capturing small or rare objects within cryo-focused ion beam (cryo-FIB) milled lamellae remains a major bottleneck. Here, we present two fluorescence-guide...
- Summary (fallback): 机器翻译摘要显示：冷冻电子断层扫描 (cryo-ET) 是一种直接可视化细胞内大分子结构的强大方法，但其更广泛的应用受到样品制备过程中难以可靠地定位特定结构的限制。特别是，在冷冻聚焦离子束 (cryo-FIB) 铣削片层中捕获小型或稀有物体仍然是一个主要瓶颈。在这里，我们提出了两种荧光引导的冷冻 FIB 铣削工作流程，这些工作流程克服了目标误差的关键来源，并能够在广泛的空间尺度上常规捕获结构。对于较大的目标（> 500 nm），我们提出了一种改进的基于配准的策略，将 FIB 铣削基准与折射率失配的深度校正相结合。
- Keywords: structures, milling, fluorescence-guided, cryo-focused, beam

### 6. [免疫原性肿瘤块休眠是免疫治疗黑色素瘤中持续残留病灶的驱动因素](https://www.biorxiv.org/content/10.64898/2025.12.11.692633v2)
- Original title: Immunogenic tumor mass dormancy as a driver of persistent residual lesions in immunotherapy-treated melanoma
- Authors: Shi, Y., Maliga, Z., Vallius, T., Pant, S. M., Pelletier, R. et al.
- Meta: 2026-07-09 | cancer biology | DOI: 10.64898/2025.12.11.692633
- 中文摘要: 肿瘤休眠被认为会导致癌症复发，但患者休眠的环境和机制尚不清楚。在临床前模型中已经观察到免疫原性肿瘤大量休眠，涉及持续的肿瘤细胞增殖和平衡的免疫介导的细胞死亡，以及细胞水平的静止。在这里，我们证明了接受免疫检查点抑制剂（ICI）治疗的黑色素瘤患者的长期稳定残留病灶中存在大量休眠而不是静止。在进行详细空间分析的大的稳定病灶中，增殖肿瘤细胞的比例与 ICI 后进展的患者的部位匹配肿瘤中的比例相似。其他患者残留的稳定病变，经临床病理学检查判断仅包含疤痕组织，也包含被活跃免疫细胞包围的分裂肿瘤细胞巢。
- Abstract: Tumor dormancy is thought to enable cancer recurrence, but the settings and mechanisms of dormancy in patients are poorly characterized. Both immunogenic tumor mass dormancy, involving continued tumor cell proliferation and balanced immune-mediated cell death, and cell-level quiescence have been observed in preclinical models. Here, we demonstrate the existence of mass dormancy rather than quiescence in long-term st...
- Summary (fallback): 机器翻译摘要显示：肿瘤休眠被认为会导致癌症复发，但患者休眠的环境和机制尚不清楚。在临床前模型中已经观察到免疫原性肿瘤大量休眠，涉及持续的肿瘤细胞增殖和平衡的免疫介导的细胞死亡，以及细胞水平的静止。在这里，我们证明了接受免疫检查点抑制剂（ICI）治疗的黑色素瘤患者的长期稳定残留病灶中存在大量休眠而不是静止。在进行详细空间分析的大的稳定病灶中，增殖肿瘤细胞的比例与 ICI 后进展的患者的部位匹配肿瘤中的比例相似。其他患者残留的稳定病变，经临床病理学检查判断仅包含疤痕组织，也包含被活跃免疫细胞包围的分裂肿瘤细胞巢。
- Keywords: tumor, dormancy, mass, lesions, patients

### 7. [子宫平滑肌肉瘤的多维单细胞转录组分析揭示了不同的肿瘤状态以及推断的治疗漏洞](https://www.biorxiv.org/content/10.1101/2025.11.17.688894v2)
- Original title: Multidimensional Single-Cell Transcriptomic Profiling of Uterine Leiomyosarcomas Reveals Distinct Tumor States with Inferred Therapeutic Vulnerabilities
- Authors: Korah, M., Agolia, J. P., Reddy, B., Flojo, R. A. B., Goncalves, A. et al.
- Meta: 2026-07-09 | cancer biology | DOI: 10.1101/2025.11.17.688894
- 中文摘要: 子宫平滑肌肉瘤（ULMS）是一种经常复发和转移的孤儿疾病，由于缺乏有效的治疗靶点，患者需要接受多线化疗。为了解决这一差距，我们使用单细胞 RNA 测序和空间转录组分析来全面分析 ULMS。我们发现了肿瘤细胞的多种状态，包括具有间充质样特征的肿瘤细胞、MYC程序定义的缺血性肿瘤细胞、具有活跃干扰素信号传导的炎性肿瘤细胞以及干细胞样激素受体阳性细胞。这些肿瘤细胞状态的推断空间相关性证明了独特的定位模式。通过将这些特征与大量 RNA 测序数据相关联，我们证明了这些发现与临床结果的相关性。
- Abstract: Uterine leiomyosarcoma (ULMS) is an orphan disease that frequently recurs and metastasizes, with patients undergoing multiple lines of chemotherapy due to lack of effective therapeutic targets. To address this gap, we used single-cell RNA sequencing and spatial transcriptomic analysis to comprehensively profile ULMS. We uncovered multiple states of tumor cells, including tumor cells with mesenchyme-like features, is...
- Summary (fallback): 机器翻译摘要显示：子宫平滑肌肉瘤（ULMS）是一种经常复发和转移的孤儿疾病，由于缺乏有效的治疗靶点，患者需要接受多线化疗。为了解决这一差距，我们使用单细胞 RNA 测序和空间转录组分析来全面分析 ULMS。我们发现了肿瘤细胞的多种状态，包括具有间充质样特征的肿瘤细胞、MYC程序定义的缺血性肿瘤细胞、具有活跃干扰素信号传导的炎性肿瘤细胞以及干细胞样激素受体阳性细胞。这些肿瘤细胞状态的推断空间相关性证明了独特的定位模式。通过将这些特征与大量 RNA 测序数据相关联，我们证明了这些发现与临床结果的相关性。
- Keywords: tumor, cells, states, single-cell, therapeutic

### 8. [液泡膜细胞分裂素核苷转运蛋白控制根-微生物界面上细胞内激素的可用性](https://www.biorxiv.org/content/10.64898/2026.05.31.727005v2)
- Original title: A tonoplast cytokinin riboside transporter gates intracellular hormone availability at the root-microbe interface
- Authors: Hudecek, M., Nedved, D., Kucharova, A., Forczek, S. T., Kuzmenko, M. et al.
- Meta: 2026-07-09 | plant biology | DOI: 10.64898/2026.05.31.727005
- 中文摘要: 细胞分裂素核苷是细胞分裂素的主要移动形式和前体形式，细胞分裂素是植物激素，其运输和亚细胞分布影响发育和应激反应。在这里，我们将拟南芥平衡核苷转运蛋白 1 (ENT1) 鉴定为液泡膜定位的细胞分裂素核苷转运蛋白。天然调控元件下的组织特异性亚细胞分析将 ENT1 主要定位于根表皮和侧根帽细胞的液泡膜，在那里它控制细胞内细胞分裂素核苷的可用性。因此，ENT1过表达增强了细胞分裂素核苷敏感性和信号传导，而ENT1的缺失改变了腺苷代谢并破坏了细胞分裂素稳态，导致多种玉米素型细胞分裂素的积累。
- Abstract: Cytokinin ribosides are major mobile and precursor forms of cytokinins, plant hormones whose transport and subcellular distribution shape developmental and stress responses. Here, we identify Arabidopsis thaliana EQUILIBRATIVE NUCLEOSIDE TRANSPORTER1 (ENT1) as a tonoplast-localized cytokinin riboside transporter. Tissue-specific subcellular analysis under native regulatory elements localized ENT1 predominantly to th...
- Summary (fallback): 机器翻译摘要显示：细胞分裂素核苷是细胞分裂素的主要移动形式和前体形式，细胞分裂素是植物激素，其运输和亚细胞分布影响发育和应激反应。在这里，我们将拟南芥平衡核苷转运蛋白 1 (ENT1) 鉴定为液泡膜定位的细胞分裂素核苷转运蛋白。天然调控元件下的组织特异性亚细胞分析将 ENT1 主要定位于根表皮和侧根帽细胞的液泡膜，在那里它控制细胞内细胞分裂素核苷的可用性。因此，ENT1过表达增强了细胞分裂素核苷敏感性和信号传导，而ENT1的缺失改变了腺苷代谢并破坏了细胞分裂素稳态，导致多种玉米素型细胞分裂素的积累。
- Keywords: cytokinin, riboside, ent1, intracellular, availability

### 9. [LUstiGE，光响应玉米黑粉菌基因表达：玉米真菌病原体玉米黑粉菌形态发生和发病机制的光遗传学控制](https://www.biorxiv.org/content/10.64898/2026.06.25.734638v1)
- Original title: LUstiGE, Light responsive Ustilago maydis Gene Expression: Optogenetic control of morphogenesis and pathogenesis in the corn fungal pathogen Ustilago maydis
- Authors: Tang, K., Müller, M. D., Hüsemann, L., Zuo, W., Rybecky, A. et al.
- Meta: 2026-07-09 | synthetic biology | DOI: 10.64898/2026.06.25.734638
- 中文摘要: 担子菌玉米黑粉菌 (Ustilago maydis) 是一种特征明确的模式生物，用于研究病原体与宿主的相互作用，并且对广泛的生物技术应用具有极大的兴趣。我们致力于开发光诱导分子工具，以实现信号网络和真菌宿主通讯的动态研究以及代谢工程方法。特别是，光控光遗传学开关提供定量、时空控制能力，是微创且可逆的。我们设计了两个基于蓝光诱导的 LOV 结构域的基因表达开关，以上调 (Blue-ON) 和下调 (Blue-OFF) 基因表达，并在玉米须孢子虫和菌丝中进行了功能表征。
- Abstract: The basidiomycete Ustilago maydis is a well-characterized model organism for studying pathogen-host interactions and of great interest for a broad spectrum of biotechnological applications. We set here to develop light inducible molecular tools to enable dynamic studies on signaling networks and fungi-host communication, and for metabolic engineering approaches. In particular, light-controlled, optogenetic switches...
- Summary (fallback): 机器翻译摘要显示：担子菌玉米黑粉菌 (Ustilago maydis) 是一种特征明确的模式生物，用于研究病原体与宿主的相互作用，并且对广泛的生物技术应用具有极大的兴趣。我们致力于开发光诱导分子工具，以实现信号网络和真菌宿主通讯的动态研究以及代谢工程方法。特别是，光控光遗传学开关提供定量、时空控制能力，是微创且可逆的。我们设计了两个基于蓝光诱导的 LOV 结构域的基因表达开关，以上调 (Blue-ON) 和下调 (Blue-OFF) 基因表达，并在玉米须孢子虫和菌丝中进行了功能表征。
- Keywords: maydis, control, expression, ustilago, gene

### 10. [参与细菌 DNA 分割的 ParBF 生物缩合物的快速组装和体内聚结](https://www.biorxiv.org/content/10.1101/2025.10.27.684735v3)
- Original title: Fast assembly and in vivo coalescence of ParBF biocondensates involved in bacterial DNA partition
- Authors: Revoil, P., Delimi, L., Rech, J., Cailhau, J., Cornet, F. et al.
- Meta: 2026-07-09 | systems biology | DOI: 10.1101/2025.10.27.684735
- 中文摘要: 细菌中 DNA 的忠实分离依赖于 ParABS 系统，其中 ParB 在类似着丝粒的 parS 位点组装成冷凝物，而 ATP 酶 ParA 在空间上组织这些复合物。这些 ParB 凝聚物如何保持动态行为而不塌陷成单一结构仍不清楚。在这里，我们将染色体降解与定量成像结合起来，剖析控制体内 ParB 凝聚动力学的动力学和物理原理。在不存在类核的情况下，来自质粒 F 的 ParB 缩合物自由扩散并在遇到后几秒钟内合并。引人注目的是，定量分析表明凝聚态可能在聚变分离边界附近运行，因此最小的能量足以在复制后分裂它们，从而防止不可逆的聚结。
- Abstract: Faithful DNA segregation in bacteria relies on ParABS systems, in which ParB assembles into condensates at centromere-like parS sites, while the ATPase ParA spatially organizes these complexes. How these ParB condensates maintain dynamic behavior without collapsing into a single structure has remained unclear. Here, we combine chromosome degradation with quantitative imaging to dissect the kinetics and physical prin...
- Summary (fallback): 机器翻译摘要显示：细菌中 DNA 的忠实分离依赖于 ParABS 系统，其中 ParB 在类似着丝粒的 parS 位点组装成冷凝物，而 ATP 酶 ParA 在空间上组织这些复合物。这些 ParB 凝聚物如何保持动态行为而不塌陷成单一结构仍不清楚。在这里，我们将染色体降解与定量成像结合起来，剖析控制体内 ParB 凝聚动力学的动力学和物理原理。在不存在类核的情况下，来自质粒 F 的 ParB 缩合物自由扩散并在遇到后几秒钟内合并。引人注目的是，定量分析表明凝聚态可能在聚变分离边界附近运行，因此最小的能量足以在复制后分裂它们，从而防止不可逆的聚结。
- Keywords: condensates, coalescence, parb, assembly, parbf

### 11. [布尔乳腺癌网络（BBCN）：细胞命运信号的结构可控性和双稳态抗性-凋亡开关](https://www.biorxiv.org/content/10.64898/2026.06.18.733086v1)
- Original title: The Boolean Breast-Cancer Network (BBCN): structural controllability of cell-fate signalling and a bistable resistance-apoptosis switch
- Authors: Bhatti, A. I.
- Meta: 2026-07-09 | systems biology | DOI: 10.64898/2026.06.18.733086
- 中文摘要: 我们将乳腺肿瘤建模为信号通路的布尔网络，并将治疗作为一个控制问题：找到最小的、可药物的干预措施，将网络驱动到所需的细胞命运表型，作为自由动力学的真正固定点，而不永久强迫任何节点。
- Abstract: We model a breast tumour as a Boolean network of signalling pathways and pose therapy as a control problem: find minimal, druggable interventions that drive the network to a desired cell-fate phenotype as a genuine fixed point of the free dynamics, without permanently forcing any node. A 135-node breast-cancer network, adapted from a published Boolean model and carrying the feedback simplifications usual to such mod...
- Summary (fallback): 机器翻译摘要显示：我们将乳腺肿瘤建模为信号通路的布尔网络，并将治疗作为一个控制问题：找到最小的、可药物的干预措施，将网络驱动到所需的细胞命运表型，作为自由动力学的真正固定点，而不永久强迫任何节点。
- Keywords: network, three, boolean, switch, model

### 12. [过度膨胀和过度集中：为什么柯西微扰核是 ABC-SMC 的正确选择](https://www.biorxiv.org/content/10.64898/2026.06.24.734205v1)
- Original title: Overinflation and overconcentration: why Cauchy perturbation kernels are the right choice for ABC-SMC
- Authors: Sturrock, M., Shahrezaei, V.
- Meta: 2026-07-09 | systems biology | DOI: 10.64898/2026.06.24.734205
- 中文摘要: 近似贝叶斯计算顺序蒙特卡罗 (ABC-SMC) 使用扰动核传播其粒子，并且使用标准正态核，它会随着参数维度的增长而急剧退化，这种失败通常归因于维度本身。相反，我们表明它是由汇总统计的质量控制的，维度仅通过单独且更温和的机制输入，并且两者必须共同作用才能破坏正常内核。第一个成分是协方差过度膨胀：从粒子云估计的核协方差超过了真实后验协方差，其超出了汇总统计中信息丢失设置的因子。
- Abstract: Approximate Bayesian computation sequential Monte Carlo (ABC-SMC) propagates its particles with a perturbation kernel, and with the standard Normal kernel it degrades sharply as the parameter dimension grows, a failure usually attributed to dimension itself. We show instead that it is governed by the quality of the summary statistics, with dimension entering only through a separate and milder mechanism, and that the...
- Summary (fallback): 机器翻译摘要显示：近似贝叶斯计算顺序蒙特卡罗 (ABC-SMC) 使用扰动核传播其粒子，并且使用标准正态核，它会随着参数维度的增长而急剧退化，这种失败通常归因于维度本身。相反，我们表明它是由汇总统计的质量控制的，维度仅通过单独且更温和的机制输入，并且两者必须共同作用才能破坏正常内核。第一个成分是协方差过度膨胀：从粒子云估计的核协方差超过了真实后验协方差，其超出了汇总统计中信息丢失设置的因子。
- Keywords: kernel, dimension, cauchy, perturbation, normal

### 13. [行星规模异养微生物群落模型评估代谢协同作用和病毒影响](https://www.biorxiv.org/content/10.1101/2025.02.13.638167v3)
- Original title: Planetary-scale heterotrophic microbial community modeling assesses metabolic synergy and viral impacts
- Authors: Regimbeau, A., Tian, F., Smith, G., Riddell, V. J., Andreani-Gerard, C. M. et al.
- Meta: 2026-07-09 | systems biology | DOI: 10.1101/2025.02.13.638167
- 中文摘要: 海洋通过微生物代谢活动支持的生物地球化学循环来缓冲气候变化。虽然全球范围的调查提供了基线微生物组数据，但推断代谢和生物地球化学影响仍然具有挑战性。基因组规模模型解决了细胞水平上的类似问题，突出了取决于特定环境条件的关键代谢反应。在这里，我们采用这种机械建模框架来分析全球海洋微生物群落，以揭示预测维持生态系统功能的代谢过程。为了实现这一目标，我们为每个 TARA Ocean 宏基因组或宏转录组（即仅限于异养原核生物和病毒已知的反应）开发了一个基因组规模的超有机体代谢模型，并评估了这些模型，为每个样本建立了群落范围内的代谢表型。
- Abstract: The oceans buffer against climate change via biogeochemical cycles underpinned by microbial metabolic activities. While planetary-scale surveys provide baseline microbiome data, inferring metabolic and biogeochemical impacts remains challenging. Genome-scale modeling has addressed analogous issues at the cellular level, highlighting key metabolic reactions contingent upon specific environmental conditions. Here we a...
- Summary (fallback): 机器翻译摘要显示：海洋通过微生物代谢活动支持的生物地球化学循环来缓冲气候变化。虽然全球范围的调查提供了基线微生物组数据，但推断代谢和生物地球化学影响仍然具有挑战性。基因组规模模型解决了细胞水平上的类似问题，突出了取决于特定环境条件的关键代谢反应。在这里，我们采用这种机械建模框架来分析全球海洋微生物群落，以揭示预测维持生态系统功能的代谢过程。为了实现这一目标，我们为每个 TARA Ocean 宏基因组或宏转录组（即仅限于异养原核生物和病毒已知的反应）开发了一个基因组规模的超有机体代谢模型，并评估了这些模型，为每个样本建立了群落范围内的代谢表型。
- Keywords: metabolic, microbial, modeling, model, viruses

### 14. [源自患者的 tau 种子人类神经元嵌合体重现了成熟的阿尔茨海默病 tau 病理学并揭示了人类特有的神经元脆弱性](https://www.biorxiv.org/content/10.64898/2026.07.06.736894v2)
- Original title: Patient-derived tau-seeded human neuronal chimeras recapitulate mature Alzheimer's tau pathology and uncover human-specific neuronal vulnerability
- Authors: Ji, Y., Mandal, P., Liu, J., Hu, W., Colon, B. D. et al.
- Meta: 2026-07-09 | neuroscience | DOI: 10.64898/2026.07.06.736894
- 中文摘要: Tau pathology is a central hallmark of Alzheimer's disease (AD) and strongly correlates with cognitive decline, yet the development of tau-targeted therapies has been hindered by the inability of existing models to capture human-specific disease features, particularly the mature forms of AD tau pathology.此外，tau 病理学的物种特异性机制仍然知之甚少。 Here, we establish a patient-derived tau-seeded human neuronal chimera model by transplanting human pluripotent stem cell (hPSC)-derived neural progenitor cells into neonatal mouse brains, followed by intracerebral injection of pathological tau seeds from postmortem AD brains.人类神经元在体内成熟并重现了成人 tau 特征，包括所有六种亚型，3R:4R 比例约为 1:1。
- Abstract: Tau pathology is a central hallmark of Alzheimer's disease (AD) and strongly correlates with cognitive decline, yet the development of tau-targeted therapies has been hindered by the inability of existing models to capture human-specific disease features, particularly the mature forms of AD tau pathology. Moreover, species-specific mechanisms underlying tau pathology remain poorly understood. Here, we establish a pa...
- Summary (fallback): 机器翻译摘要显示：Tau pathology is a central hallmark of Alzheimer's disease (AD) and strongly correlates with cognitive decline, yet the development of tau-targeted therapies has been hindered by the inability of existing models to capture human-specific disease features, particularly the mature forms of AD tau pathology.此外，tau 病理学的物种特异性机制仍然知之甚少。 Here, we establish a patien...
- Keywords: human, pathology, neurons, mature, neuronal

### 15. [夜间 Th1 免疫激活可预测皮质醇觉醒反应](https://www.biorxiv.org/content/10.64898/2026.07.06.735751v1)
- Original title: Overnight Th1 immune activation predicts the cortisol awakening response
- Authors: Seizer, L., Matuskov, M. G., Gostner, J., Schubert, C.
- Meta: 2026-07-09 | neuroscience | DOI: 10.64898/2026.07.06.735751
- 中文摘要: 皮质醇觉醒反应（CAR）通过早上醒来时皮质醇水平急剧增加来标记从休息阶段到清醒阶段的过渡。这种增加可能有助于认知和行为觉醒，但其功能尚未完全了解。在这项试点研究中，我们旨在提供有关免疫系统活动对 CAR 影响的第一批数据。因此，应用受试者内分析方法来避免受试者间偏差造成的混淆并改善结果的推断。三名健康受试者收集过夜尿液以分析新蝶呤（Th1 免疫激活标记物），并在早晨醒来后 0、30 和 45 分钟采集唾液样本以进行皮质醇测定和 CAR 估算。此外，受试者整夜佩戴脑电图头带，以客观确定觉醒时间点。
- Abstract: The cortisol awakening response (CAR) marks the transition from rest to wake phase by a sharp increase in cortisol levels upon awakening in the morning. This increase may assist in cognitive and behavioral awakening, but its function is not fully understood yet. In this pilot study we aimed to provide first data on the influence of immune system activity on the CAR. Thereby, a within-subject analysis approach was ap...
- Summary (fallback): 机器翻译摘要显示：皮质醇觉醒反应（CAR）通过早上醒来时皮质醇水平急剧增加来标记从休息阶段到清醒阶段的过渡。这种增加可能有助于认知和行为觉醒，但其功能尚未完全了解。在这项试点研究中，我们旨在提供有关免疫系统活动对 CAR 影响的第一批数据。因此，应用受试者内分析方法来避免受试者间偏差造成的混淆并改善结果的推断。三名健康受试者收集过夜尿液以分析新蝶呤（Th1 免疫激活标记物），并在早晨醒来后 0、30 和 45 分钟采集唾液样本以进行皮质醇测定和 CAR 估算。此外，受试者整夜佩戴脑电图头带，以客观确定觉醒时间点。
- Keywords: awakening, overnight, immune, cortisol, activation

### 16. [一击：迷幻的见解是独特的强烈、有意义和难以言喻的](https://www.biorxiv.org/content/10.64898/2026.06.02.729484v2)
- Original title: One-shotted: psychedelic insights are uniquely intense, meaningful and ineffable
- Authors: Pogliani, A., Zachary, A., Hall, L., Tangen, J. M., Mond, J. et al.
- Meta: 2026-07-09 | neuroscience | DOI: 10.64898/2026.06.02.729484
- 中文摘要: 洞察力通常在实验室范式中被研究为伴随着特征性的“啊哈！”的理解的突然转变。经验。然而，这样的范式可能无法捕捉自然主义背景下发生的全部现象学洞察力。 This study compared the phenomenology of insight across four contexts: psychedelic experiences, everyday-life insights, Compound Remote Associates problems, and ambiguous images, in a within-subject online study of adults with prior psychedelic experience (N = 73).参与者对每个洞察的强度、惊喜、自信、愉悦、动力、意义、不可言喻和感知信念变化进行评分。
- Abstract: Insight is commonly studied in laboratory paradigms as a sudden shift in understanding accompanied by characteristic "Aha!" experiences. However, such paradigms may not capture the full phenomenological range of insight as it occurs in naturalistic contexts. This study compared the phenomenology of insight across four contexts: psychedelic experiences, everyday-life insights, Compound Remote Associates problems, and...
- Summary (fallback): 机器翻译摘要显示：洞察力通常在实验室范式中被研究为伴随着特征性的“啊哈！”的理解的突然转变。经验。然而，这样的范式可能无法捕捉自然主义背景下发生的全部现象学洞察力。 This study compared the phenomenology of insight across four contexts: psychedelic experiences, everyday-life insights, Compound Remote Associates problems, and ambiguous images, in a within-subject online study of adults with prior psychedelic experience (N = 73).参与者对每个洞察的强度、惊喜、自信、愉悦...
- Keywords: belief, insight, change, insights, meaning

### 17. [空间转录组程序与猕猴皮层的谱层节律相关](https://www.biorxiv.org/content/10.64898/2026.07.08.737187v1)
- Original title: Spatial transcriptomic programs relate to spectrolaminar rhythms across macaque cortex
- Authors: Reyes, R. G., Vezoli, J., Valdes-Sosa, P. A.
- Meta: 2026-07-09 | neuroscience | DOI: 10.64898/2026.07.08.737187
- 中文摘要: 皮层动力学的层状组织被认为反映了潜在的细胞类型结构，但这种关系尚未在灵长类皮层中得到解决。在这里，我们开发了一个光谱组学框架，允许在共同的第 4 层参考坐标系内比较层流局部场电位和单细胞空间转录组学。我们没有依赖原始频带功率分析，而是使用局部频谱扩展 (LSE)，这是一种频谱层分量模型，可将频率按深度的 LFP 功率图解析为不同的 {delta}、{theta}、...、{beta}、低 {gamma} 和高 {gamma} 分量。然后，我们引入了第 4 层投影（L4P），将非线性空间转录组皮层带展开为与电生理深度剖面兼容的平坦第 4 层参考流形。
- Abstract: The laminar organization of cortical dynamics is thought to reflect underlying cell-type architecture, but this relationship has not been resolved across primate cortex. Here we developed a spectro-omic framework that allows laminar local field potentials and single-cell spatial transcriptomics to be compared within a common layer-4-referenced coordinate system. Instead of relying on raw band-power analysis, we used...
- Summary (fallback): 机器翻译摘要显示：皮层动力学的层状组织被认为反映了潜在的细胞类型结构，但这种关系尚未在灵长类皮层中得到解决。在这里，我们开发了一个光谱组学框架，允许在共同的第 4 层参考坐标系内比较层流局部场电位和单细胞空间转录组学。我们没有依赖原始频带功率分析，而是使用局部频谱扩展 (LSE)，这是一种频谱层分量模型，可将频率按深度的 LFP 功率图解析为不同的 {delta}、{theta}、...、{beta}、低 {gamma} 和高 {gamma} 分量。然后，我们引入了第 4 层投影（L4P），将非线性空间转录组皮层带展开为与电生理深度剖面兼容的平坦第 4 层参考流形。
- Keywords: across, gamma, spatial, transcriptomic, programs

### 18. [抗微生物质粒编码 Evangelion，一种广泛使用的 DUF4062 抗噬菌体防御家族](https://www.biorxiv.org/content/10.64898/2026.06.25.731849v2)
- Original title: Antimicrobial-resistance plasmids encode Evangelion, a widespread DUF4062 anti-phage defence family
- Authors: Ibarra-Chavez, R., Azam, A. H., Chihara, K., Miranda Djurhuus, A., Gottlieb, K. A. et al.
- Meta: 2026-07-09 | molecular biology | DOI: 10.64898/2026.06.25.731849
- 中文摘要: 许多细菌抗噬菌体防御系统是由移动遗传元件编码的，但这种抗病毒库的大部分仍未被发现。众所周知，抗菌素耐药性质粒可以传播抗菌素耐药性基因，但它们对细菌免疫的贡献在很大程度上仍未被探索。通过对天然存在的耐甲氧西林金黄色葡萄球菌质粒进行表型引导的询问，我们鉴定出 Evangelion，这是一个广泛的单基因抗噬菌体防御系统家族，其中保守的 DUF4062 核心与防御活动所需的多样化辅助区域偶联。
- Abstract: Many bacterial anti-phage defence systems are encoded by mobile genetic elements, yet much of this antiviral repertoire remains undiscovered. Antimicrobial-resistance plasmids are well known for disseminating antibiotic-resistance genes, but their contribution to bacterial immunity remains largely unexplored. Using phenotype-guided interrogation of a naturally occurring methicillin-resistant Staphylococcus aureus pl...
- Summary (fallback): 机器翻译摘要显示：许多细菌抗噬菌体防御系统是由移动遗传元件编码的，但这种抗病毒库的大部分仍未被发现。众所周知，抗菌素耐药性质粒可以传播抗菌素耐药性基因，但它们对细菌免疫的贡献在很大程度上仍未被探索。通过对天然存在的耐甲氧西林金黄色葡萄球菌质粒进行表型引导的询问，我们鉴定出 Evangelion，这是一个广泛的单基因抗噬菌体防御系统家族，其中保守的 DUF4062 核心与防御活动所需的多样化辅助区域偶联。
- Keywords: defence, anti-phage, systems, duf4062, bacterial

### 19. [通过 3'UTR 异构体的选择性翻译调节神经元中的蛋白质丰度](https://www.biorxiv.org/content/10.64898/2026.07.08.737200v1)
- Original title: Regulation of protein abundance in neurons by selective translation of 3'UTR isoforms
- Authors: Gorey, S., Ozbulut, H. C., Carrasco, J., Zhang, Y., Hess, A. et al.
- Meta: 2026-07-09 | molecular biology | DOI: 10.64898/2026.07.08.737200
- 中文摘要: 蛋白质合成的精确调节对于细胞功能和生存至关重要。特别是在神经元中，mRNA 翻译失调与记忆形成受损有关，是神经退行性疾病的一个标志。神经元的特征是组织特异性的长 3' 非翻译区 (3'UTR)；在这项研究中，我们证明，在果蝇和哺乳动物大脑中，具有这些神经元 3'UTR 的 mRNA 亚型的翻译效率低于其短对应物。 3'UTR 依赖性翻译基于以两种神经富集蛋白 ELAV 和 Pumilio 为中心的负反馈机制。长 elav 3'UTR 抑制神经元 ELAV 蛋白的产生，进而介导数百个神经元基因的 3'UTR 延伸。那些长 3'UTR 同工型优先与 Pumilio 结合并进行翻译抑制。
- Abstract: The precise regulation of protein synthesis is essential for cellular function and survival. In particular, in neurons, dysregulated mRNA translation is linked to impaired memory formation and is a hallmark of neurodegenerative diseases. Neurons are characterized by tissue- specific, long 3' untranslated regions (3'UTRs); in this study, we demonstrate that mRNA isoforms with these neuronal 3'UTRs are less efficientl...
- Summary (fallback): 机器翻译摘要显示：蛋白质合成的精确调节对于细胞功能和生存至关重要。特别是在神经元中，mRNA 翻译失调与记忆形成受损有关，是神经退行性疾病的一个标志。神经元的特征是组织特异性的长 3' 非翻译区 (3'UTR)；在这项研究中，我们证明，在果蝇和哺乳动物大脑中，具有这些神经元 3'UTR 的 mRNA 亚型的翻译效率低于其短对应物。 3'UTR 依赖性翻译基于以两种神经富集蛋白 ELAV 和 Pumilio 为中心的负反馈机制。长 elav 3'UTR 抑制神经元 ELAV 蛋白的产生，进而介导数百个神经元基因的 3'UTR 延伸。那些长 3'UTR 同工型优先与 Pumilio 结合并进行翻译抑制。
- Keywords: protein, neuronal, neurons, translation, isoforms

### 20. [JMJD5 通过羟基化 ISY1 和调节精氨酸甲基转移酶 PRMT6 来调节代谢](https://www.biorxiv.org/content/10.1101/2025.09.27.678987v2)
- Original title: JMJD5 regulates metabolism by hydroxylating ISY1, and regulating the Arginine Methyltransferase PRMT6
- Authors: Khan, Z. A., Chutoe, C., Marques Junior, J., Jarman, E. J., Gradinaru, A. et al.
- Meta: 2026-07-09 | cell biology | DOI: 10.1101/2025.09.27.678987
- 中文摘要: 2-氧戊二酸依赖性双加氧酶 (2OGDD) 利用分子氧、2-氧戊二酸和亚铁来催化双电子氧化。这种依赖性使一些 2OGDD 能够充当细胞代谢状态的传感器，在氧气或代谢稳态受到干扰时驱动关键功能，包括适应低氧、基因转录的表观遗传控制以及代谢途径的重塑。 Jumonji-C (JmjC) 结构域包含蛋白 5 (JMJD5) 是一种调节表观遗传标记的 2OGDD，对于 DNA 损伤修复至关重要，并且是细胞代谢的关键调节因子。值得注意的是，JMJD5 在肝细胞癌中经常降低，与较差的总生存率相关。尽管具有生物学意义，但 JMJD5 的分子功能仍未解决，其生理目标也难以捉摸。
- Abstract: 2-Oxoglutarate-dependent dioxygenases (2OGDDs) employ molecular oxygen, 2-oxoglutarate, and ferrous iron to catalyse two-ectron oxidations. This dependency enables some 2OGDD to act as sensors of cellular metabolic states, driving crucial functions when oxygen or metabolic homeostasis is perturbed, including adaptation to low oxygen, epigenetic control of gene transcription, and the reshaping of metabolic pathways....
- Summary (fallback): 机器翻译摘要显示：2-氧戊二酸依赖性双加氧酶 (2OGDD) 利用分子氧、2-氧戊二酸和亚铁来催化双电子氧化。这种依赖性使一些 2OGDD 能够充当细胞代谢状态的传感器，在氧气或代谢稳态受到干扰时驱动关键功能，包括适应低氧、基因转录的表观遗传控制以及代谢途径的重塑。 Jumonji-C (JmjC) 结构域包含蛋白 5 (JMJD5) 是一种调节表观遗传标记的 2OGDD，对于 DNA 损伤修复至关重要，并且是细胞代谢的关键调节因子。值得注意的是，JMJD5 在肝细胞癌中经常降低，与较差的总生存率相关。尽管具有生物学意义，但 JMJD5 的分子功能仍未解决，其生理目标也难以捉摸。
- Keywords: jmjd5, prmt6, metabolism, isy1, arginine

### 21. [化学遗传学 CRISPR 敲除筛选鉴定了 T 细胞激活中泛素介导的钙调磷酸酶-BMP 通路中继](https://www.biorxiv.org/content/10.64898/2026.07.08.737199v1)
- Original title: A chemogenetic CRISPR knockout screen identifies a ubiquitin-mediated calcineurin-BMP pathway relay in T cell activation
- Authors: Diallo, M., Mueller, L., Uhlig, S., Hendriks, I., Kzhyshkowska, J. et al.
- Meta: 2026-07-09 | cell biology | DOI: 10.64898/2026.07.08.737199
- 中文摘要: T 细胞激活依赖于钙调神经磷酸酶信号传导，但该途径如何与其他调节系统整合仍不完全清楚。在这里，我们利用 FK506 的双重药理学来剖析 T 细胞反应期间的信号串扰，FK506 抑制钙调神经磷酸酶，同时释放 FKBP12 介导的 BMP 受体抑制。使用 FK506 和环孢菌素 A 进行的比较全基因组 CRISPR 敲除筛选显示，FK506 独特地参与 BMP 途径组件和泛素调控网络。 Jurkat 和原代人 T 细胞的功能分析表明，FK506 诱导 BMP 受体依赖性 SMAD1/5/8 激活，并触发 K48 和 K29 连接的泛素链的快速重塑。
- Abstract: T cell activation is dependent on calcineurin signalling, yet how this pathway integrates with other regulatory systems remains incompletely understood. Here, we exploit the dual pharmacology of FK506, which inhibits calcineurin while also releasing FKBP12-mediated repression of BMP receptors, to dissect signalling crosstalk during T cell responses. A comparative genome-wide CRISPR knockout screen using FK506 and Cy...
- Summary (fallback): 机器翻译摘要显示：T 细胞激活依赖于钙调神经磷酸酶信号传导，但该途径如何与其他调节系统整合仍不完全清楚。在这里，我们利用 FK506 的双重药理学来剖析 T 细胞反应期间的信号串扰，FK506 抑制钙调神经磷酸酶，同时释放 FKBP12 介导的 BMP 受体抑制。使用 FK506 和环孢菌素 A 进行的比较全基因组 CRISPR 敲除筛选显示，FK506 独特地参与 BMP 途径组件和泛素调控网络。 Jurkat 和原代人 T 细胞的功能分析表明，FK506 诱导 BMP 受体依赖性 SMAD1/5/8 激活，并触发 K48 和 K29 连接的泛素链的快速重塑。
- Keywords: signalling, activation, ubiquitin, pathway, cell

### 22. [DSCAM 通过拮抗 N-钙粘蛋白粘附和 UNC5c 排斥在径向迁移过程中保留神经元秩序](https://www.biorxiv.org/content/10.1101/2025.06.16.659927v2)
- Original title: DSCAM preserves neuronal order during radial migration by antagonizing N-Cadherin adhesion and UNC5c repulsion
- Authors: Yang, T., Hergenreder, T., Veling, M. W., Chang, W.-C., Cui, E. J. et al.
- Meta: 2026-07-09 | developmental biology | DOI: 10.1101/2025.06.16.659927
- 中文摘要: 发育中的皮质神经元的适当径向迁移对于哺乳动物大脑皮层的“由内而外”的层状组织至关重要。虽然我们对神经元如何在皮质板（CP）/边缘层（ML）边界终止迁移的理解取得了实质性进展，但控制神经元迁移顺序的机制仍然知之甚少。在这里，我们发现上层锥体神经元的径向迁移在上皮层板（UCP）内被暂时限制，迁移的神经元组装成垂直组织的径向队列，维持神经元间的间距和迁移顺序。使用胚胎小鼠皮层的延时成像，我们发现前导神经元短暂延迟尾随神经元的核运动，从而同步 UCP 内的神经元运动。
- Abstract: Proper radial migration of developing cortical neurons is critical for the "inside-out" laminar organization of the mammalian cerebral cortex. While substantial progress has been made in our understanding of how neurons terminate migration at the cortical plate (CP)/marginal layer (ML) boundary, the mechanisms that control the sequential order of migrating neurons remain poorly understood. Here, we show that radial...
- Summary (fallback): 机器翻译摘要显示：发育中的皮质神经元的适当径向迁移对于哺乳动物大脑皮层的“由内而外”的层状组织至关重要。虽然我们对神经元如何在皮质板（CP）/边缘层（ML）边界终止迁移的理解取得了实质性进展，但控制神经元迁移顺序的机制仍然知之甚少。在这里，我们发现上层锥体神经元的径向迁移在上皮层板（UCP）内被暂时限制，迁移的神经元组装成垂直组织的径向队列，维持神经元间的间距和迁移顺序。使用胚胎小鼠皮层的延时成像，我们发现前导神经元短暂延迟尾随神经元的核运动，从而同步 UCP 内的神经元运动。
- Keywords: neurons, migration, dscam, neuronal, radial

### 23. [大脑折叠作为傅里叶级数产生发育时钟](https://www.biorxiv.org/content/10.64898/2026.07.07.737104v1)
- Original title: Brain folding as a Fourier series yields a developmental clock
- Authors: Goldschmidt, E.
- Meta: 2026-07-09 | developmental biology | DOI: 10.64898/2026.07.07.737104
- 中文摘要: 人类大脑皮层在妊娠期间会折叠成固定形状。不同的原理决定了最终大脑几何形状的大小。在这里，我证明胎儿大脑可以被描述为带限球谐傅立叶对象，其整个回转过程塌陷为单个一维曲线，其中最大调和度充当发育坐标。闭合形式描述符预测胎儿大脑图谱的孕龄，平均绝对误差为 0.13 周和 0.38 周，比已发表的基于学习的现有技术水平高出三到七倍。将相同的描述符应用于 FeTA 病理数据集中的单个受试者，可以对每个受试者与正常轨迹的距离进行分类，并区分病理胎儿和神经典型胎儿。
- Abstract: The human cerebral cortex folds into a stereotyped shape during gestation. Different principles govern the large and small scales of the final brain geometry. Here, I show that the fetal cerebrum can be described as a band limited spherical harmonic Fourier object which entire gyrification process collapses to a single one-dimensional curve, in which the maximum harmonic degree acts as a developmental coordinate. Th...
- Summary (fallback): 机器翻译摘要显示：人类大脑皮层在妊娠期间会折叠成固定形状。不同的原理决定了最终大脑几何形状的大小。在这里，我证明胎儿大脑可以被描述为带限球谐傅立叶对象，其整个回转过程塌陷为单个一维曲线，其中最大调和度充当发育坐标。闭合形式描述符预测胎儿大脑图谱的孕龄，平均绝对误差为 0.13 周和 0.38 周，比已发表的基于学习的现有技术水平高出三到七倍。将相同的描述符应用于 FeTA 病理数据集中的单个受试者，可以对每个受试者与正常轨迹的距离进行分类，并区分病理胎儿和神经典型胎儿。
- Keywords: brain, fetal, single, descriptor, fourier

### 24. [相当好的产量允许对农业景观中的多个目标进行空间管理](https://www.biorxiv.org/content/10.64898/2026.07.06.736684v1)
- Original title: Pretty Good Yields allow the spatial management of multiple objectives in agricultural landscapes
- Authors: Kubasch, M., Costa, M., Loeuille, N.
- Meta: 2026-07-09 | ecology | DOI: 10.64898/2026.07.06.736684
- 中文摘要: 为了在不影响自然的情况下养活不断增长的全球人口，制定协调产量和保护目标的农业管理战略是关键。使用元群落模型的数值模拟，我们探索了农田空间管理策略提供的妥协的可能性。每种策略的特点是耕作强度、耕地比例及其空间聚集。我们表明，实现公平的产量与生物多样性妥协是困难的。虽然提供最高产量和生物多样性的安抚策略通常是不可能的，但接受稍低的产量（即“相当好的产量策略”）可以恢复大量的生物多样性。对于散布程度较小的物种来说，这种协调的可能性是有限的。
- Abstract: In order to feed a growing global population without silencing nature, conceiving agricultural management strategies reconciling yield and conservation goals is key. Using numerical simulations of a metacommunity model, we explore the possibilities for compromise offered by spatial management strategies of farmed areas. Each strategy is characterized by its farming intensity, the proportion of farmed lands and their...
- Summary (fallback): 机器翻译摘要显示：为了在不影响自然的情况下养活不断增长的全球人口，制定协调产量和保护目标的农业管理战略是关键。使用元群落模型的数值模拟，我们探索了农田空间管理策略提供的妥协的可能性。每种策略的特点是耕作强度、耕地比例及其空间聚集。我们表明，实现公平的产量与生物多样性妥协是困难的。虽然提供最高产量和生物多样性的安抚策略通常是不可能的，但接受稍低的产量（即“相当好的产量策略”）可以恢复大量的生物多样性。对于散布程度较小的物种来说，这种协调的可能性是有限的。
- Keywords: strategies, yield, biodiversity, spatial, management

### 25. [瞬态动态期间，人口和群落变异性偏离固定预期](https://www.biorxiv.org/content/10.64898/2026.07.08.737188v1)
- Original title: Population and community variability deviate from stationary expectations during transient dynamics
- Authors: Guerber, J., Genettais, D., Fontaine, C., Thebault, E.
- Meta: 2026-07-09 | ecology | DOI: 10.64898/2026.07.08.737188
- 中文摘要: 在复杂的扰动机制下，生物多样性动态显示物种和群落丰度围绕长期人口趋势的时间变化。许多物种确实表现出长期下降，而其他物种却在增加，使自然群落远离静止状态，而变异性通常在接近平衡的情况下进行研究。我们通过调查人口动态随机模型中的新闻扰动引起的长期趋势中的人口和社区变异性，为缩小这一差距做出了贡献。通过估计瞬态期间均值和方差的确定性变化，我们表明总体变异性偏离平稳预期。此外，偏差在很大程度上取决于人口趋势的迹象：增加会产生过度的变异性，而下降会产生赤字。
- Abstract: Under complex perturbation regimes, biodiversity dynamics show temporal variability in species and community abundance around long-term population trends. Many species indeed show long-term declines while other species increase, putting natural communities far from stationary regimes, while variability is often studied near equilibrium. We contribute to bridging this gap by investigating population and community var...
- Summary (fallback): 机器翻译摘要显示：在复杂的扰动机制下，生物多样性动态显示物种和群落丰度围绕长期人口趋势的时间变化。许多物种确实表现出长期下降，而其他物种却在增加，使自然群落远离静止状态，而变异性通常在接近平衡的情况下进行研究。我们通过调查人口动态随机模型中的新闻扰动引起的长期趋势中的人口和社区变异性，为缩小这一差距做出了贡献。通过估计瞬态期间均值和方差的确定性变化，我们表明总体变异性偏离平稳预期。此外，偏差在很大程度上取决于人口趋势的迹象：增加会产生过度的变异性，而下降会产生赤字。
- Keywords: variability, population, community, species, stationary

### 26. [当从荟萃分析或估算变量获得汇总统计数据时，基于 LDSC 回归的遗传力估计可能会出现偏差](https://www.biorxiv.org/content/10.64898/2026.07.05.736573v1)
- Original title: LDSC regression-based heritability estimates can be biased when summary statistics are obtained from meta-analysis or imputed variants
- Authors: Dong, R., Wang, M., Wang, G. T., deWan, A. T., Leal, S. M.
- Meta: 2026-07-09 | genetics | DOI: 10.64898/2026.07.05.736573
- 中文摘要: 动机：连锁不平衡评分 (LDSC) 回归是一种流行的方法，使用汇总统计和连锁不平衡 (LD) 参考面板来估计复杂性状的遗传力，为需要个体水平数据的方法提供了实用的替代方案。尽管 LDSC 回归被广泛使用，但它可能会产生有偏差的遗传力估计。使用多项大规模阿尔茨海默病 (AD) 研究的汇总统计数据和各种 LD 参考组研究了 LDSC 回归的特性。将这些遗传力估计值与从个体水平数据获得的估计值进行比较。结果：当 LDSC 回归应用于荟萃分析获得的汇总统计时，会导致遗传力被低估。
- Abstract: Motivation: Linkage disequilibrium score (LDSC) regression is a popular method to estimate heritability for complex traits using summary statistics and linkage disequilibrium (LD) reference panels, offering a practical alternative to methods requiring individual-level data. Despite its widespread use, LDSC regression can produce biased heritability estimates. The properties of LDSC regression were investigated using...
- Summary (fallback): 机器翻译摘要显示：动机：连锁不平衡评分 (LDSC) 回归是一种流行的方法，使用汇总统计和连锁不平衡 (LD) 参考面板来估计复杂性状的遗传力，为需要个体水平数据的方法提供了实用的替代方案。尽管 LDSC 回归被广泛使用，但它可能会产生有偏差的遗传力估计。使用多项大规模阿尔茨海默病 (AD) 研究的汇总统计数据和各种 LD 参考组研究了 LDSC 回归的特性。将这些遗传力估计值与从个体水平数据获得的估计值进行比较。结果：当 LDSC 回归应用于荟萃分析获得的汇总统计时，会导致遗传力被低估。
- Keywords: heritability, estimates, summary, statistics, ldsc

### 27. [戒烟后烟草突变的肺泡祖细胞的持续存在反映了肺腺癌的长期风险](https://www.biorxiv.org/content/10.64898/2026.07.06.736766v1)
- Original title: Persistence of tobacco-mutated alveolar progenitor cells after smoking cessation mirrors long term risk of lung adenocarcinoma
- Authors: Przybilla, M. J., Ammar, A., Selway-Clarke, H., Lawson, A. R. J., Spencer Chapman, M. et al.
- Meta: 2026-07-09 | genomics | DOI: 10.64898/2026.07.06.736766
- 中文摘要: 烟草烟雾影响肺上皮细胞的突变、选择和克隆扩张。戒烟导致两种最常见肺癌的流行病学有所不同：鳞状细胞癌的风险急剧下降，而腺癌的风险则保持不变。为了研究这种差异，我们分析了 806 个肺泡 II 型 (AT2) 细胞的基因组，发现戒烟后突变负担持续升高。相比之下，在近端气道中，突变负荷接近正常的罕见基底干细胞在停止治疗后会扩张，从而预防鳞状细胞癌。 AT2 细胞的靶向单分子 DNA 测序揭示了 TP53、细胞周期和 MAPK 基因的阳性选择，支持持续的癌症风险。
- Abstract: Tobacco smoke shapes mutations, selection and clonal expansion in lung epithelial cells. Smoking cessation leads to divergent epidemiology in the two most common lung cancers: squamous cell carcinoma risk declines sharply, while adenocarcinoma risk is preserved. To investigate this discrepancy, we analysed 806 genomes of alveolar type II (AT2) cells and found persistently elevated mutation burdens after cessation. I...
- Summary (fallback): 机器翻译摘要显示：烟草烟雾影响肺上皮细胞的突变、选择和克隆扩张。戒烟导致两种最常见肺癌的流行病学有所不同：鳞状细胞癌的风险急剧下降，而腺癌的风险则保持不变。为了研究这种差异，我们分析了 806 个肺泡 II 型 (AT2) 细胞的基因组，发现戒烟后突变负担持续升高。相比之下，在近端气道中，突变负荷接近正常的罕见基底干细胞在停止治疗后会扩张，从而预防鳞状细胞癌。 AT2 细胞的靶向单分子 DNA 测序揭示了 TP53、细胞周期和 MAPK 基因的阳性选择，支持持续的癌症风险。
- Keywords: cells, cessation, risk, lung, cell

### 28. [精神分裂症相关皮质 DNA 甲基化差异是神经元特异性的](https://www.biorxiv.org/content/10.64898/2026.07.08.737176v1)
- Original title: Schizophrenia-associated DNA methylation differences in the cortex are neuron-specific
- Authors: Hannon, E., Walker, E. M., Chioza, B., Burrage, J., Blake, G. E. T. et al.
- Meta: 2026-07-09 | genomics | DOI: 10.64898/2026.07.08.737176
- 中文摘要: 精神分裂症是一种复杂的神经精神疾病，遗传风险被认为集中在大脑中细胞类型特异性的调节机制上。我们使用荧光激活核分选 (FANS) 进行了精神分裂症的细胞类型解析表观基因组范围关联研究 (EWAS)，以分离富含神经元 (NeuN+)、少突胶质细胞 (SOX10+) 和其他富含神经胶质 (NeuN-/SOX10-) 的细胞核群以及来自 216 个前额皮质细胞核的总分数捐赠者（104 名精神分裂症患者和 112 名对照者）。我们在实验范围内的神经元富集核中鉴定出了 16 个差异甲基化位置 (DMP)，并在发现阈值上鉴定了 400 多个额外的神经元 DMP。
- Abstract: Schizophrenia is a complex neuropsychiatric disorder in which genetic risk is thought to converge on cell type-specific regulatory mechanisms in the brain. We performed a cell type-resolved epigenome-wide association study (EWAS) of schizophrenia using fluorescence-activated nuclei sorting (FANS) to isolate neuron-enriched (NeuN+), oligodendrocyte-enriched (SOX10+) and other glial-enriched (NeuN-/SOX10-) nuclei popu...
- Summary (fallback): 机器翻译摘要显示：精神分裂症是一种复杂的神经精神疾病，遗传风险被认为集中在大脑中细胞类型特异性的调节机制上。我们使用荧光激活核分选 (FANS) 进行了精神分裂症的细胞类型解析表观基因组范围关联研究 (EWAS)，以分离富含神经元 (NeuN+)、少突胶质细胞 (SOX10+) 和其他富含神经胶质 (NeuN-/SOX10-) 的细胞核群以及来自 216 个前额皮质细胞核的总分数捐赠者（104 名精神分裂症患者和 112 名对照者）。我们在实验范围内的神经元富集核中鉴定出了 16 个差异甲基化位置 (DMP)，并在发现阈值上鉴定了 400 多个额外的神经元 DMP。
- Keywords: nuclei, schizophrenia, cell, schizophrenia-associated, cortex

### 29. [猪的发声包含人类和机器共享的声学结构，但推测情感效价的证据有限](https://www.biorxiv.org/content/10.64898/2026.07.06.736900v1)
- Original title: Pig vocalizations contain shared acoustic structure for humans and machines, but limited evidence for presumed affective valence
- Authors: Gorssen, W., Sleurs, B., Winters, C.
- Meta: 2026-07-09 | animal behavior and cognition | DOI: 10.64898/2026.07.06.736900
- 中文摘要: 在动物福利研究中，发声越来越多地被提议作为情感状态的指标。然而，许多研究将上下文衍生的情感效价分配给发声，然后根据这些上下文衍生的标签使用机器学习对它们进行分类。这种循环依赖使得我们不清楚成功的分类是否反映了情感状态本身、更广泛的上下文或声学差异，或者任务强加的解释类别。因此，我们使用自由分类和强制选择任务检查了猪发声的人类组织，并将这些模式与卷积神经网络模型恢复的声学结构进行了比较。在一项自由分类任务中，224 名参与者将 2,192 种猪的叫声分类为自定义类别。
- Abstract: Vocalizations are increasingly proposed as indicators of affective state in animal welfare research. Yet many studies assign context-derived affective valence to vocalizations and then classify these using machine learning according to those context-derived labels. This circular dependence makes it unclear whether successful classification reflects affective state itself, broader contextual or acoustic differences,...
- Summary (fallback): 机器翻译摘要显示：在动物福利研究中，发声越来越多地被提议作为情感状态的指标。然而，许多研究将上下文衍生的情感效价分配给发声，然后根据这些上下文衍生的标签使用机器学习对它们进行分类。这种循环依赖使得我们不清楚成功的分类是否反映了情感状态本身、更广泛的上下文或声学差异，或者任务强加的解释类别。因此，我们使用自由分类和强制选择任务检查了猪发声的人类组织，并将这些模式与卷积神经网络模型恢复的声学结构进行了比较。在一项自由分类任务中，224 名参与者将 2,192 种猪的叫声分类为自定义类别。
- Keywords: vocalizations, valence, acoustic, structure, affective

### 30. [CircDiscoverer：circRNA-蛋白质相互作用和 RNA 修饰景观的多物种综合资源](https://www.biorxiv.org/content/10.64898/2026.01.08.698416v2)
- Original title: CircDiscoverer: A multispecies comprehensive resource for circRNA-protein interactions and RNA modification landscapes
- Authors: Srinivasan, S., Kumar, S., Chatterjee, S., Chande, A.
- Meta: 2026-07-09 | bioinformatics | DOI: 10.64898/2026.01.08.698416
- 中文摘要: 环状 RNA (circRNA) 通过与 miRNA、蛋白质相互作用以及编码肽来调节各种细胞过程。与 circRNA-miRNA 相互作用相比，circRNA-蛋白质相互作用（CPI）和 circRNA 修饰的研究相对较少。在这里，我们开发了一个全面的用户友好型网络资源 CircDiscoverer，用于探索多个物种的 CPI 和修饰景观，包括智人、小家鼠、果蝇和拟南芥。 CircDiscoverer 将手动策划的文献支持的 CPI 与计算预测的交互集成在一起。
- Abstract: Circular RNAs (circRNAs) regulate various cellular processes by interacting with miRNAs, proteins, and by encoding peptides. Compared to circRNA-miRNA interactions, circRNA-protein interactions (CPIs) and circRNA modifications have been relatively less explored. Here, we developed a comprehensive user-friendly web resource, CircDiscoverer, to explore CPIs and modification landscapes across multiple species, includin...
- Summary (fallback): 机器翻译摘要显示：环状 RNA (circRNA) 通过与 miRNA、蛋白质相互作用以及编码肽来调节各种细胞过程。与 circRNA-miRNA 相互作用相比，circRNA-蛋白质相互作用（CPI）和 circRNA 修饰的研究相对较少。在这里，我们开发了一个全面的用户友好型网络资源 CircDiscoverer，用于探索多个物种的 CPI 和修饰景观，包括智人、小家鼠、果蝇和拟南芥。 CircDiscoverer 将手动策划的文献支持的 CPI 与计算预测的交互集成在一起。
- Keywords: circdiscoverer, interactions, comprehensive, cpis, resource

## medrxiv

### 1. [77,000 名患有神经发育障碍的参与者的具象绘画能力与非具象能力形成了独特的认知机制](https://www.medrxiv.org/content/10.1101/2024.07.26.24310995v3)
- Original title: Figurative Drawing Abilities Map onto Distinct Cognitive Mechanism from Non-Figurative Abilities in 77,000 Participants with Neurodevelopmental Disorders
- Authors: Murphy, E. M., Venkatesh, R., Khokhlovich, E., Vyshedskiy, A.
- Meta: 2026-07-09 | pediatrics | DOI: 10.1101/2024.07.26.24310995
- 中文摘要: 非具象图案（平行线、手工模板）构成了已知最早的人类艺术，其历史可以追溯到约 40 万年前。相比之下，具象艺术——描绘可识别的动物和人类——突然出现约 45,000 年。我们假设这种时间分离反映了语言和视觉操纵背后的不同神经认知机制的顺序进化。基于我们之前识别出不同的表达和接受语言机制的分类框架，我们检查了它们与神经发育障碍个体的绘画能力的共现情况。结果揭示了特定的分离：比喻绘画与句法机制（负责句法理解）同时出现。相比之下，非具象艺术与修饰语机制（调解名词与形容词的整合）相关。
- Abstract: Non-figurative motifs (parallel lines, hand stencils) constitute the earliest known human art, dating to ~400,000 years ago. In contrast, figurative art-depicting recognizable animals and humans-emerges abruptly ~45,000 ya. We hypothesized that this temporal dissociation reflects the sequential evolution of distinct neurocognitive mechanisms underlying language and visual manipulation. Building on our prior taxonomi...
- Summary (fallback): 机器翻译摘要显示：非具象图案（平行线、手工模板）构成了已知最早的人类艺术，其历史可以追溯到约 40 万年前。相比之下，具象艺术——描绘可识别的动物和人类——突然出现约 45,000 年。我们假设这种时间分离反映了语言和视觉操纵背后的不同神经认知机制的顺序进化。基于我们之前识别出不同的表达和接受语言机制的分类框架，我们检查了它们与神经发育障碍个体的绘画能力的共现情况。结果揭示了特定的分离：比喻绘画与句法机制（负责句法理解）同时出现。相比之下，非具象艺术与修饰语机制（调解名词与形容词的整合）相关。
- Keywords: mechanism, figurative, non-figurative, syntactic, drawing

### 2. [用于预测精神分裂症现实世界功能的结构知情认知表征](https://www.medrxiv.org/content/10.64898/2026.06.25.26356524v2)
- Original title: Structure-Informed Cognitive Representation for Predicting Real-World Functioning in Schizophrenia
- Authors: Chen, C.
- Meta: 2026-07-09 | psychiatry and clinical psychology | DOI: 10.64898/2026.06.25.26356524
- 中文摘要: 预测精神分裂症（SCZ）的现实世界功能仍然是临床优先事项，但现有模型受到方法学限制和缺乏既定的临床实用性的限制。认知是一种常用的预测因子，其表示方式可能会影响预测性能。规范潜在认知结构（N-LCS）方法提供了一种结构知情的表示，可以解决传统领域级别分数的局限性。来自 COBRE 队列（163 个 SCZ、180 个健康对照）的数据用于开发和内部验证经济 (EF)、职业 (OF) 和社会 (SF) 功能的岭回归模型，使用 N-LCS 偏差指标以及完全嵌套的乐观校正引导框架内的先验选择的人口和临床预测因子。开发了使用 MCCB 域 T 分数的基于分数的模型进行比较。
- Abstract: Predicting real-world functioning in schizophrenia (SCZ) remains a clinical priority, but existing models are limited by methodological constraints and a lack of established clinical utility. Cognition is a commonly used predictor and how it is represented may affect predictive performance. The Normative Latent Cognitive Structure (N-LCS) approach provides a structure- informed representation that may address limita...
- Summary (fallback): 机器翻译摘要显示：预测精神分裂症（SCZ）的现实世界功能仍然是临床优先事项，但现有模型受到方法学限制和缺乏既定的临床实用性的限制。认知是一种常用的预测因子，其表示方式可能会影响预测性能。规范潜在认知结构（N-LCS）方法提供了一种结构知情的表示，可以解决传统领域级别分数的局限性。来自 COBRE 队列（163 个 SCZ、180 个健康对照）的数据用于开发和内部验证经济 (EF)、职业 (OF) 和社会 (SF) 功能的岭回归模型，使用 N-LCS 偏差指标以及完全嵌套的乐观校正引导框架内的先验选择的人口和临床预测因子。开发了使用 MCCB 域 T 分数的基于分数的模型进行比较。
- Keywords: models, performance, clinical, functioning, used

### 3. [用于无出血分析人体内脏器官的体内空间转录组学](https://www.medrxiv.org/content/10.64898/2026.07.06.26357355v1)
- Original title: In Vivo Spatial Transcriptomics for Bleeding-free Profiling Human Internal Organs
- Authors: Sun, H., Guo, F., Zhao, X., Wan, Y., Zhang, X. et al.
- Meta: 2026-07-09 | genetic and genomic medicine | DOI: 10.64898/2026.07.06.26357355
- 中文摘要: 尽管空间转录组学在技术上取得了重大进步，但其临床应用在很大程度上尚未开发。在这里，我们开发了一个集成系统 ENDO-Genome，用于微创体内转录本采样，以促进人体内部器官的实时空间转录组分析。这是通过将纳米阵列生物芯片与现有内窥镜集成，直接从人体内脏（包括高度血管化的肝脏或肾脏）进行压力传感器校准的“Touch & Go”RNA提取来实现的，无需进行组织活检，从而避免任何出血风险。通过胃肠内窥镜的演示，在常规检查中，通过 5 分钟的操作，从人体肠道的多个位置获得了 55 个 mRNA 转录本的多重景观。受益于免测序方法，每次检测的成本不到 10 美元。
- Abstract: Despite the significant technical advancement in spatial transcriptomics, its clinical usage is largely untapped. Here, we develop an integrated system, ENDO-Genome, for minimally invasive in-body transcript sampling to facilitate live spatial transcriptomic analysis of human internal organs. This is achieved by integrating a nanoarrayed biochip with existing endoscope to perform pressure-sensor-calibrated "Touch &...
- Summary (fallback): 机器翻译摘要显示：尽管空间转录组学在技术上取得了重大进步，但其临床应用在很大程度上尚未开发。在这里，我们开发了一个集成系统 ENDO-Genome，用于微创体内转录本采样，以促进人体内部器官的实时空间转录组分析。这是通过将纳米阵列生物芯片与现有内窥镜集成，直接从人体内脏（包括高度血管化的肝脏或肾脏）进行压力传感器校准的“Touch & Go”RNA提取来实现的，无需进行组织活检，从而避免任何出血风险。通过胃肠内窥镜的演示，在常规检查中，通过 5 分钟的操作，从人体肠道的多个位置获得了 55 个 mRNA 转录本的多重景观。受益于免测序方法，每次检测的成本不到 10 美元。
- Keywords: spatial, human, transcriptomics, internal, organs

### 4. [使用开放大语言模型从芬兰电子病历中提取临床结果的不确定性](https://www.medrxiv.org/content/10.64898/2026.07.07.26355248v1)
- Original title: Uncertainty-aware extraction of clinical findings from Finnish EHRs using open large language models
- Authors: Leinonen, J. V., Knuutila, J., Kurki, S., Pamilo, S., Koskinen, M.
- Meta: 2026-07-09 | health informatics | DOI: 10.64898/2026.07.07.26355248
- 中文摘要: 客观的。评估开放权重大语言模型 (LLM) 是否能够从芬兰语儿科记录中准确提取临床结果，以及预测不确定性是否可用于对病例进行分类以供专家审查，以最大限度地减少体力工作。材料和方法。来自赫尔辛基大学医院（2010 年 - 2023 年）的 97 名儿童缺血性中风患者（1 个月 - 17 岁）的回顾性队列。三个开放的法学硕士（gpt-oss-20b、DeepSeek-R1-Distill-Qwen-32B 和 medgemma-27b-text-it）以英语提示，从每位患者的完整自由文本记录中检测四个提取目标（偏瘫、头痛、癫痫发作和中风作为阳性对照）。每个组合收到 15 个呼叫（五个温度 x​​ 三个重复）。性能根据临床医生参考（准确度、召回率、精确度、F1）进行基准测试。
- Abstract: Objective. To evaluate whether open-weight large language models (LLMs) can accurately extract clinical findings from Finnish-language pediatric records, and whether prediction uncertainty can be used to triage cases for expert review to minimize manual work. Materials and Methods. Retrospective cohort of 97 pediatric ischaemic stroke patients (1 month - 17 years) from Helsinki University Hospital (2010 - 2023). Thr...
- Summary (fallback): 机器翻译摘要显示：客观的。评估开放权重大语言模型 (LLM) 是否能够从芬兰语儿科记录中准确提取临床结果，以及预测不确定性是否可用于对病例进行分类以供专家审查，以最大限度地减少体力工作。材料和方法。来自赫尔辛基大学医院（2010 年 - 2023 年）的 97 名儿童缺血性中风患者（1 个月 - 17 岁）的回顾性队列。三个开放的法学硕士（gpt-oss-20b、DeepSeek-R1-Distill-Qwen-32B 和 medgemma-27b-text-it）以英语提示，从每位患者的完整自由文本记录中检测四个提取目标（偏瘫、头痛、癫痫发作和中风作为阳性对照）。每个组合收到 15 个呼叫（五个温度 x​​ 三个重复）。性能根据临床医生参考（准确度、召回率、精确度、F1）进行基准测试。
- Keywords: clinical, findings, extraction, open, llms

### 5. [南非住院儿童中 SARS-CoV-2 变体的儿科 COVID-19 严重程度：一项回顾性队列研究](https://www.medrxiv.org/content/10.64898/2026.07.06.26357377v1)
- Original title: Paediatric COVID-19 severity across SARS-CoV-2 variants in hospitalised children in South Africa: a retrospective cohort study
- Authors: Fiandrino, S., Di Chiara, C., Dona, D., Dunbar, R., Goussard, P. et al.
- Meta: 2026-07-09 | epidemiology | DOI: 10.64898/2026.07.06.26357377
- 中文摘要: 在连续的 SARS-CoV-2 相关变体 (VOC) 的推动下，COVID-19 的流行病学不断发展，促使人们不断评估其对儿童疾病严重程度的影响。在低收入和中等收入国家（LMIC），由于营养不良、免疫不完全、艾滋病毒暴露或感染、结核病以及获得医疗服务的差距等因素，儿童承受着更高的严重呼吸道疾病和肺炎相关死亡率的负担。因此，需要中低收入国家进行医院儿科研究，以了解 COVID-19 的流行病学和严重程度在大流行浪潮中如何变化。这项研究在南非开普敦 Tygerberg 医院检查了 354 名在 Omicron 早期（Beta 和 Delta）和 Omicron 波期间感染 SARS-CoV-2 的住院儿童。
- Abstract: The evolving epidemiology of COVID-19, driven by successive SARS-CoV-2 variants of concern (VOCs), has prompted ongoing evaluation of their impact on disease severity in children. In low- and middle-income countries (LMICs), children experience a higher burden of severe respiratory illness and pneumonia-related mortality due to factors such as malnutrition, incomplete immunisation, HIV exposure or infection, tubercu...
- Summary (fallback): 机器翻译摘要显示：在连续的 SARS-CoV-2 相关变体 (VOC) 的推动下，COVID-19 的流行病学不断发展，促使人们不断评估其对儿童疾病严重程度的影响。在低收入和中等收入国家（LMIC），由于营养不良、免疫不完全、艾滋病毒暴露或感染、结核病以及获得医疗服务的差距等因素，儿童承受着更高的严重呼吸道疾病和肺炎相关死亡率的负担。因此，需要中低收入国家进行医院儿科研究，以了解 COVID-19 的流行病学和严重程度在大流行浪潮中如何变化。这项研究在南非开普敦 Tygerberg 医院检查了 354 名在 Omicron 早期（Beta 和 Delta）和 Omicron 波期间感染 SARS-CoV-2 的住院儿童。
- Keywords: severity, covid-19, children, across, disease
