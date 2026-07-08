# daily2rxiv Digest - 2026-07-08

共收录 90 篇论文。

## arxiv

### 1. [ELSA3D：用于统一 3D 理解和生成的弹性语义锚定](https://arxiv.org/abs/2607.06565v1)
- Original title: ELSA3D: Elastic Semantic Anchoring for Unified 3D Understanding and Generation
- Authors: Tianjiao Yu, Xinzhuo Li, Yifan Shen, Onkar Susladkar, Yuanzhe Liu et al.
- Meta: 2026-07-07 | cs.CV
- 中文摘要: 统一的 3D 基础模型渴望生成 3D 资产并在单个主干中用语言对其进行推理，但它们的文本-3D 交互在很大程度上仍然是隐式的。现有方法将文本和 3D 标记连接成一个平面序列，并依赖自注意力，将粗糙的结构线索和精细的几何细节折叠成一个无差别的表示。我们引入了 ELSA3D，这是一种统一的 3D 模型，它通过弹性语义锚定、结构化语言和几何推理沿着匹配的抽象尺度共同解决这个问题。 ELSA3D 使用尺度感知八叉树分词器来表示几何，并引入锚标记，即选择语义线索的稀疏跨模态单元，将它们路由到最相关的 3D 尺度，检索特定于尺度的几何证据，并将融合信号写回到统一表示中，从而保持交互稀疏而精确。
- Abstract: Unified 3D foundation models aspire to generate 3D assets and reason about them in language within a single backbone, but their text-3D interaction remains largely implicit. Existing methods concatenate text and 3D tokens into a flat sequence and rely on self-attention, collapsing coarse structural cues and fine geometric details into one undifferentiated representation. We introduce ELSA3D, a unified 3D model that...
- Summary (fallback): 机器翻译摘要显示：统一的 3D 基础模型渴望生成 3D 资产并在单个主干中用语言对其进行推理，但它们的文本-3D 交互在很大程度上仍然是隐式的。现有方法将文本和 3D 标记连接成一个平面序列，并依赖自注意力，将粗糙的结构线索和精细的几何细节折叠成一个无差别的表示。我们引入了 ELSA3D，这是一种统一的 3D 模型，它通过弹性语义锚定、结构化语言和几何推理沿着匹配的抽象尺度共同解决这个问题。 ELSA3D 使用尺度感知八叉树分词器来表示几何，并引入锚标记，即选择语义线索的稀疏跨模态单元，将它们路由到最相关的 3D 尺度，检索特定于尺度的几何证据，并将融合信号写回到统一表示中，从而保持交互稀疏而精确。
- Keywords: unified, elsa3d, geometric, elastic, semantic

### 2. [图卷积注意力：图去噪和扩散的光谱视角](https://arxiv.org/abs/2607.06546v1)
- Original title: Graph Convolutional Attention: A Spectral Perspective on Graph Denoising and Diffusion
- Authors: Shervin Khalafi, Igor Krawczuk, Sergio Rozada, Charilaos Kanatsoulis, Antonio G Marques et al.
- Meta: 2026-07-07 | cs.LG
- 中文摘要: 图去噪是图学习中的一个基本问题，也是图扩散模型的核心运算。像图转换器这样的基于注意力的架构最近在图去噪方面显示出了希望。然而，我们对基于注意力的图去噪的原则性理解仍然有限，因此尚不清楚标准注意力是否是该任务的正确机制。在这里，我们表明，在去噪目标下，线性注意力不是最优的，并且只能在训练分布上学习平均谱去噪滤波器。这造成了一个基本的限制，因为图表通常在整个分布范围内变化。为了克服这一限制，我们引入了频谱注意力，它直接利用输入图频谱，并证明其性能优于线性注意力，其幅度由分布的频谱多样性决定。
- Abstract: Denoising graphs is a fundamental problem in graph learning and the core operation of graph diffusion models. Attention-based architectures like graph transformers have recently shown promise in denoising graphs. However, our principled understanding of attention-based graph denoising remains limited, making it unclear whether standard attention is the right mechanism for this task. Here we show that, under a denois...
- Summary (fallback): 机器翻译摘要显示：图去噪是图学习中的一个基本问题，也是图扩散模型的核心运算。像图转换器这样的基于注意力的架构最近在图去噪方面显示出了希望。然而，我们对基于注意力的图去噪的原则性理解仍然有限，因此尚不清楚标准注意力是否是该任务的正确机制。在这里，我们表明，在去噪目标下，线性注意力不是最优的，并且只能在训练分布上学习平均谱去噪滤波器。这造成了一个基本的限制，因为图表通常在整个分布范围内变化。为了克服这一限制，我们引入了频谱注意力，它直接利用输入图频谱，并证明其性能优于线性注意力，其幅度由分布的频谱多样性决定。
- Keywords: graph, attention, denoising, spectral, diffusion

### 3. [GraphBU：使用图本机块单元生成 MILP 实例](https://arxiv.org/abs/2607.06532v1)
- Original title: GraphBU: MILP Instance Generation with Graph-Native Block Units
- Authors: Xiaolei Guo, Chenyu Zhou, Jianghao Lin, Dongdong Ge
- Meta: 2026-07-07 | cs.LG
- 中文摘要: 当模型来自私有或特定于应用程序的管道时，很难获得用于求解器开发的混合整数线性规划 (MILP) 实例。生成器必须保留求解器和学习策略所依赖的结构。现有的通用生成器通常从公式模板、汇总统计、本地图形编辑或重组后找到的块中选择其生成单元。这些单元没有明确记录 MILP 的本地部分如何与实例的其余部分耦合。我们提出了 GraphBU，一种图原生生成器，其基本单元是局部子问题及其接口。该方法将耦合节点提升为主约束或边界变量，并使用生成的块单元进行兼容性检查替换。
- Abstract: Mixed-integer linear programming (MILP) instances used for solver development are hard to obtain when models come from private or application-specific pipelines. A generator must keep the structure that solvers and learned policies rely on. Existing general generators usually choose their generation unit from a formulation template, summary statistics, local graph edits, or blocks found after recombination. These un...
- Summary (fallback): 机器翻译摘要显示：当模型来自私有或特定于应用程序的管道时，很难获得用于求解器开发的混合整数线性规划 (MILP) 实例。生成器必须保留求解器和学习策略所依赖的结构。现有的通用生成器通常从公式模板、汇总统计、本地图形编辑或重组后找到的块中选择其生成单元。这些单元没有明确记录 MILP 的本地部分如何与实例的其余部分耦合。我们提出了 GraphBU，一种图原生生成器，其基本单元是局部子问题及其接口。该方法将耦合节点提升为主约束或边界变量，并使用生成的块单元进行兼容性检查替换。
- Keywords: milp, graphbu, generation, units, unit

### 4. [大型癌症助手 (LCA)：用于肿瘤学可扩展临床决策支持的模型不可知的编排框架](https://arxiv.org/abs/2607.06531v1)
- Original title: The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology
- Authors: Ghassen Marrakchi, Basarab Matei
- Meta: 2026-07-07 | cs.AI
- 中文摘要: - 目标：肿瘤学中的多模态深度学习模型目前受到严格耦合数据摄取、临床路由和人工智能 (AI) 推理的整体设计的限制。为了解决这种不灵活性问题，我们提出了大型癌症助手 (LCA)，这是一种与模型无关的事后编排框架，专为可扩展的临床决策支持而设计。 - 方法：LCA 在数学上形式化为基于算法不可渗透性原则的 7 元组架构，确保编排逻辑严格独立于底层黑盒 AI 模型。我们引入了进入理论，利用几何深度学习 (GDL) 沿着不同的结构和医疗轴标准化多模式患者数据。
- Abstract: - Objective: Multimodal deep learning models in oncology are currently limited by monolithic designs that rigidly couple data ingestion, clinical routing, and artificial intelligence (AI) inference. To address this inflexibility, we propose the Large Cancer Assistant (LCA), a model-agnostic, post-hoc orchestration framework designed for scalable clinical decision support. - Methods: The LCA is mathematically formali...
- Summary (fallback): 机器翻译摘要显示：- 目标：肿瘤学中的多模态深度学习模型目前受到严格耦合数据摄取、临床路由和人工智能 (AI) 推理的整体设计的限制。为了解决这种不灵活性问题，我们提出了大型癌症助手 (LCA)，这是一种与模型无关的事后编排框架，专为可扩展的临床决策支持而设计。 - 方法：LCA 在数学上形式化为基于算法不可渗透性原则的 7 元组架构，确保编排逻辑严格独立于底层黑盒 AI 模型。我们引入了进入理论，利用几何深度学习 (GDL) 沿着不同的结构和医疗轴标准化多模式患者数据。
- Keywords: orchestration, cancer, framework, clinical, multimodal

### 5. [EntroPath：用于流形学习的最大熵路径集成嵌入](https://arxiv.org/abs/2607.06497v1)
- Original title: EntroPath: Maximum Entropy Path Ensemble Embedding for Manifold Learning
- Authors: Przemysław Rola
- Meta: 2026-07-07 | cs.LG
- 中文摘要: 我们引入了 EntroPath，一种流形学习方法，通过扩散路径集合从数据图中恢复测地几何。许多现有的基于图的嵌入依赖于局部归一化随机游走或最短路径距离。前者可以将扩散集中在密集采样区域，而后者对图中的虚假快捷边敏感。相反，EntroPath 从最大熵随机游走 (MERW) 中构建其差异，它聚合了点之间 k 步路径的完整集合，而不是依赖于任何单个轨迹。我们通过 Varadhan 的热核公式证明，由此产生的自由能差异在短时间内收敛到平方测地距离。
- Abstract: We introduce EntroPath, a manifold learning method that recovers geodesic geometry from data graphs through ensembles of diffusion paths. Many existing graph-based embeddings rely either on locally normalised random walks or on shortest-path distances. The former can concentrate diffusion in densely sampled regions, while the latter are sensitive to spurious shortcut edges in the graph. EntroPath instead builds its...
- Summary (fallback): 机器翻译摘要显示：我们引入了 EntroPath，一种流形学习方法，通过扩散路径集合从数据图中恢复测地几何。许多现有的基于图的嵌入依赖于局部归一化随机游走或最短路径距离。前者可以将扩散集中在密集采样区域，而后者对图中的虚假快捷边敏感。相反，EntroPath 从最大熵随机游走 (MERW) 中构建其差异，它聚合了点之间 k 步路径的完整集合，而不是依赖于任何单个轨迹。我们通过 Varadhan 的热核公式证明，由此产生的自由能差异在短时间内收敛到平方测地距离。
- Keywords: entropath, diffusion, manifold, geodesic, geometry

### 6. [Pitwall：来自经过校准的实时蒙特卡罗引擎的忠实自然语言竞赛策略简报](https://arxiv.org/abs/2607.06495v1)
- Original title: Pitwall: Faithful Natural-Language Race-Strategy Briefings from a Calibrated Real-Time Monte Carlo Engine
- Authors: Juan S. Santillana
- Meta: 2026-07-07 | cs.CL
- 中文摘要: 现场体育评论是在截止日期内接地生成的：声明涉及真实的、命名的运动员，接地状态每隔几秒就会改变，并且在生成时不存在参考文本。我们推出了 Pitwall，这是一个生成系统，可以生成英语、西班牙语和葡萄牙语的自然语言一级方程式策略简报，将忠诚度视为一种建筑属性而不是一种愿望：每个发布的句子都被分解为类型化的事实主张（位置、差距、轮胎、配速、超车、比赛控制），并且每个主张都根据引发它的概率种族状态进行验证。同一个验证者控制微调数据：在 3,045 个模型编写的目标中，只有 81.9% 的每项声明都得到国家支持的目标被保留，其余的则回落到可证明忠实的模板，因此生成器永远不会看到不接地气的目标。
- Abstract: Live sports commentary is grounded generation under a deadline: statements concern real, named athletes, the grounding state changes every few seconds, and no reference text exists at generation time. We present Pitwall, a production system that generates natural-language Formula 1 strategy briefings in English, Spanish, and Portuguese, treating faithfulness as an architectural property rather than an aspiration: ev...
- Summary (fallback): 机器翻译摘要显示：现场体育评论是在截止日期内接地生成的：声明涉及真实的、命名的运动员，接地状态每隔几秒就会改变，并且在生成时不存在参考文本。我们推出了 Pitwall，这是一个生成系统，可以生成英语、西班牙语和葡萄牙语的自然语言一级方程式策略简报，将忠诚度视为一种建筑属性而不是一种愿望：每个发布的句子都被分解为类型化的事实主张（位置、差距、轮胎、配速、超车、比赛控制），并且每个主张都根据引发它的概率种族状态进行验证。同一个验证者控制微调数据：在 3,045 个模型编写的目标中，只有 81.9% 的每项声明都得到国家支持的目标被保留，其余的则回落到可证明忠实的模板，因此生成器永远不会看到不接地气的目标。
- Keywords: briefings, live, generation, grounding, state

### 7. [评估针对互联和自动驾驶车辆的增强 3D 点云公共数据集的中毒攻击的运营影响](https://arxiv.org/abs/2607.06484v1)
- Original title: Assessing the Operational Impact of Poisoning Attacks over Augmented 3D Point Cloud Public Datasets for Connected and Autonomous Vehicles
- Authors: Marwan Lazrag, Badis Hammi, Lorena Gonzalez-Manzano, Joaquin Garcia-Alfaro
- Meta: 2026-07-07 | cs.CR
- 中文摘要: 针对公共数据集的中毒攻击会导致重大问题，例如（i）当中毒数据用于训练时感知对象的错误分类，以及（ii）当系统中的特定条件适用于学习模型时最终可能触发的后门嵌入。它对数据增强模型的影响尚不清楚。虽然数据增强降低了中毒攻击成功的可能性，但仍然存在一些有效的问题。数据增强是否会影响中毒攻击的影响？是否会增加中毒样本或注入后门的数量？我们在本文中探讨了其中一些问题。
- Abstract: Poisoning attacks against public datasets lead to major concerns, such as (i) misclassification of perceived objects when the poisoned data is used for training and (ii) embedding of backdoors that may eventually be triggered later on, when specific conditions in the system apply over the learned models. Its impact over data augmentation models is unclear. While data augmentation reduces the likelihood of poisoning...
- Summary (fallback): 机器翻译摘要显示：针对公共数据集的中毒攻击会导致重大问题，例如（i）当中毒数据用于训练时感知对象的错误分类，以及（ii）当系统中的特定条件适用于学习模型时最终可能触发的后门嵌入。它对数据增强模型的影响尚不清楚。虽然数据增强降低了中毒攻击成功的可能性，但仍然存在一些有效的问题。数据增强是否会影响中毒攻击的影响？是否会增加中毒样本或注入后门的数量？我们在本文中探讨了其中一些问题。
- Keywords: poisoning, datasets, augmentation, over, impact

### 8. [周期性层状结构散射 T 矩阵的 Trefftz DG 近似](https://arxiv.org/abs/2607.06475v1)
- Original title: Trefftz DG Approximation of the T-Matrix for Scattering by Periodic Layered Structures
- Authors: Armando Maria Monforte, Andrea Moiola, Simone Zanotto
- Meta: 2026-07-07 | math.NA
- 中文摘要: 我们研究周期性分层光栅对时谐电磁波的散射，由二维亥姆霍兹方程建模。周期性障碍物可以包括可穿透和不可穿透的区域，并且由有限数量的堆叠层组成。使用准周期边界条件在单个周期单元上制定边界值问题。垂直方向的辐射条件是通过狄利克雷到诺依曼 (DtN) 算子施加的。为了有效地处理多层结构，我们采用了基于 T 矩阵方法的公式。全局散射问题被分解为各个层上提出的边值问题。在层边界上，场以准周期模态展开形式表示，层 T 矩阵描述了传入波模和传出波模之间的映射。
- Abstract: We study the scattering of time-harmonic electromagnetic waves by periodic layered gratings, modelled by the 2D Helmholtz equation. The periodic obstacle may include penetrable and impenetrable regions, and consists of a finite number of stacked layers. The boundary value problem is formulated on a single periodic cell using quasi-periodic boundary conditions. The radiation condition in the vertical directions is im...
- Summary (fallback): 机器翻译摘要显示：我们研究周期性分层光栅对时谐电磁波的散射，由二维亥姆霍兹方程建模。周期性障碍物可以包括可穿透和不可穿透的区域，并且由有限数量的堆叠层组成。使用准周期边界条件在单个周期单元上制定边界值问题。垂直方向的辐射条件是通过狄利克雷到诺依曼 (DtN) 算子施加的。为了有效地处理多层结构，我们采用了基于 T 矩阵方法的公式。全局散射问题被分解为各个层上提出的边值问题。在层边界上，场以准周期模态展开形式表示，层 T 矩阵描述了传入波模和传出波模之间的映射。
- Keywords: t-matrix, scattering, periodic, layers, boundary

### 9. [用于预测量子多体系统时间演化的可证明学习分离](https://arxiv.org/abs/2607.06472v1)
- Original title: Provable learning separation for predicting time-evolution of quantum many-body systems
- Authors: Rahul Bandyopadhyay, Riccardo Molteni, Jens Eisert, Vedran Dunjko, Sofiene Jerbi
- Meta: 2026-07-07 | quant-ph
- 中文摘要: 鉴于量子计算机天生适合模拟量子多体系统的行为，一个直接的问题出现了：能否制定表现出学习分离的物理驱动的量子机器学习（QML）任务？我们通过从可能近似正确（PAC）学习的角度研究量子多体动力学的可学习性来解决这个问题。具体来说，我们设计了一个监督学习问题，其中训练集由随机稳定器探针状态的规范、从多项式大时间间隔 $[0,T]$ 均匀采样的演化时间以及在未知哈密顿量下根据所得时间演化状态评估的某些可观测值的期望值组成。
- Abstract: Given that quantum computers are naturally suited to simulate the behavior of quantum many-body systems, an immediate question arises: can one formulate physically motivated quantum machine learning (QML) tasks that exhibit learning separations? We address this problem by studying the learnability of quantum many-body dynamics from the perspective of probably approximately correct (PAC)-learning. Concretely, we devi...
- Summary (fallback): 机器翻译摘要显示：鉴于量子计算机天生适合模拟量子多体系统的行为，一个直接的问题出现了：能否制定表现出学习分离的物理驱动的量子机器学习（QML）任务？我们通过从可能近似正确（PAC）学习的角度研究量子多体动力学的可学习性来解决这个问题。具体来说，我们设计了一个监督学习问题，其中训练集由随机稳定器探针状态的规范、从多项式大时间间隔 $[0,T]$ 均匀采样的演化时间以及在未知哈密顿量下根据所得时间演化状态评估的某些可观测值的期望值组成。
- Keywords: quantum, learning, hamiltonian, mathsf, many-body

### 10. [TILDE：基于 TILt 的分布式擦除用于概念遗忘](https://arxiv.org/abs/2607.06432v1)
- Original title: TILDE: TILt-based Distributional Erasure for Concept Unlearning
- Authors: Naveen George, Naoki Murata, Yuhta Takida, Konda Reddy Mopuri, Yuki Mitsufuji
- Meta: 2026-07-07 | cs.LG
- 中文摘要: 文本到图像扩散模型中的概念遗忘对于安全和实际部署至关重要：随着隐私问题、版权纠纷、商标限制和安全法规的不断增加，部署的系统必须能够在训练后抑制不需要的概念。现有的方法通常会有效地去除目标概念，但实际的遗忘还需要一个同样基本的属性：遗忘的模型应该保留良性生成的质量、多样性和语义覆盖。黄金标准是从头开始训练的仅保留模型，没有不需要的数据。然而，常见的擦除目标并未指定哪种遗忘后分布应近似该参考，从而使保留成为更新规则的隐含结果。
- Abstract: Concept unlearning in text-to-image diffusion models is critical for safe and practical deployment: with rising privacy concerns, copyright disputes, trademark constraints, and safety regulations, deployed systems must be able to suppress unwanted concepts after training. Existing methods often remove the target concept effectively, but practical unlearning also requires an equally fundamental property: the unlearne...
- Summary (fallback): 机器翻译摘要显示：文本到图像扩散模型中的概念遗忘对于安全和实际部署至关重要：随着隐私问题、版权纠纷、商标限制和安全法规的不断增加，部署的系统必须能够在训练后抑制不需要的概念。现有的方法通常会有效地去除目标概念，但实际的遗忘还需要一个同样基本的属性：遗忘的模型应该保留良性生成的质量、多样性和语义覆盖。黄金标准是从头开始训练的仅保留模型，没有不需要的数据。然而，常见的擦除目标并未指定哪种遗忘后分布应近似该参考，从而使保留成为更新规则的隐含结果。
- Keywords: distributional, concept, unlearning, model, tilde

### 11. [图像不能表达的东西：语言引导的嗅觉表征学习](https://arxiv.org/abs/2607.06402v1)
- Original title: What Images Cannot Say: Language-Guided Olfactory Representation Learning
- Authors: Eleftherios Tsonis, Xi Wang, Vicky Kalogeiton
- Meta: 2026-07-07 | cs.CV
- 中文摘要: 图像告诉我们场景是什么样子，但很少告诉我们身临其境的感觉。虽然最近的数据集将视觉场景与电子鼻测量配对，但将气味信号与图像对齐仍然具有挑战性，因为许多嗅觉线索来自于像素中不直接可见的上下文环境因素。我们介绍 SCENT，这是一个多模态框架，它使用语言指导作为视觉和嗅觉之间的语义桥梁。我们的方法利用视觉语言模型（VLM）生成场景描述符，捕获视觉场景所建议的对象、环境背景和合理的环境气味线索。这些描述符为学习嗅觉表征提供语义指导。
- Abstract: Images tell us what a scene looks like, but rarely what it would feel like to be there. While recent datasets pair visual scenes with electronic-nose measurements, aligning smell signals with images remains challenging because many olfactory cues arise from contextual environmental factors that are not directly visible in pixels. We introduce SCENT, a multimodal framework that uses language guidance as a semantic br...
- Summary (fallback): 机器翻译摘要显示：图像告诉我们场景是什么样子，但很少告诉我们身临其境的感觉。虽然最近的数据集将视觉场景与电子鼻测量配对，但将气味信号与图像对齐仍然具有挑战性，因为许多嗅觉线索来自于像素中不直接可见的上下文环境因素。我们介绍 SCENT，这是一个多模态框架，它使用语言指导作为视觉和嗅觉之间的语义桥梁。我们的方法利用视觉语言模型（VLM）生成场景描述符，捕获视觉场景所建议的对象、环境背景和合理的环境气味线索。这些描述符为学习嗅觉表征提供语义指导。
- Keywords: olfactory, smell, what, images, learning

### 12. [学习在多障碍环境中安全投掷物体](https://arxiv.org/abs/2607.06388v1)
- Original title: Learning to Throw Objects Safely in Multi-Obstacle Environments
- Authors: Mohammadreza Kasaei, Klemen Voncina, Hamidreza Kasaei
- Meta: 2026-07-07 | cs.RO
- 中文摘要: 机器人投掷可以将物体快速有效地放置在机器人的直接工作空间之外，但在杂乱环境中可靠的投掷仍然没有得到充分探索。现有的方法，例如 TossingBot，从视觉输入中学习投掷策略，但假设无障碍设置。在本文中，我们解决了将物体扔进目标篮子同时避开场景中随机放置的障碍物的问题。我们引入了一种势场状态表示，它在固定大小的网格上紧凑地编码了篮子吸引力和障碍物排斥力，使强化学习（RL）策略能够泛化到任意数量和配置的障碍物。该策略从动觉演示中初始化，并使用三种最先进的 RL 算法（SAC、DDPG、TD3）在模拟中进行优化。
- Abstract: Robotic throwing enables fast and efficient object placement beyond the robot's immediate workspace, but reliable throwing in cluttered environments remains underexplored. Existing approaches, such as TossingBot, learn throwing strategies from visual input but assume obstacle-free settings. In this paper, we address the problem of throwing objects into a target basket while avoiding obstacles placed randomly in the...
- Summary (fallback): 机器翻译摘要显示：机器人投掷可以将物体快速有效地放置在机器人的直接工作空间之外，但在杂乱环境中可靠的投掷仍然没有得到充分探索。现有的方法，例如 TossingBot，从视觉输入中学习投掷策略，但假设无障碍设置。在本文中，我们解决了将物体扔进目标篮子同时避开场景中随机放置的障碍物的问题。我们引入了一种势场状态表示，它在固定大小的网格上紧凑地编码了篮子吸引力和障碍物排斥力，使强化学习（RL）策略能够泛化到任意数量和配置的障碍物。该策略从动觉演示中初始化，并使用三种最先进的 RL 算法（SAC、DDPG、TD3）在模拟中进行优化。
- Keywords: throwing, objects, environments, representation, learning

### 13. [组合学习的函数空间二分法：神经正切核的指数次优性](https://arxiv.org/abs/2607.06382v1)
- Original title: A Function-Space Dichotomy for Compositional Learning: Exponential Sub-Optimality of the Neural Tangent Kernel
- Authors: Arkaprabha Ganguli, Emil Constantinescu
- Meta: 2026-07-07 | stat.ML
- 中文摘要: 持续的经验观察表明，经过训练的神经网络在具有组合结构的任务上超越了其神经正切内核（NTK）的限制，但缺乏对 $\textbf{when}$ 和 $\textbf{by how much}$ 的定量说明。在单位圆上，我们通过目标的两个复杂性度量之间的二分法给出这样的解释：它的$\textbf{傅里叶复杂度}$，它控制NTK核回归，它的$\textbf{架构复杂度}$，它控制深度$L$、宽度$w$ReLU网络的学习，权重的变化范数以$R$为界。我们首先描述架构类 $\mathcal{C}_{L,w,R}$ 的极小极大速率，将其固定为 $L$ 的单个因子：在 $Ω(Lw^2R^2/n)$ 和 $\tilde{O}(L^2w^2R^2/n)$ 之间。
- Abstract: A persistent empirical observation is that trained neural networks outperform their neural tangent kernel (NTK) limit on tasks with compositional structure, yet a quantitative account of $\textbf{when}$ and $\textbf{by how much}$ has been lacking. Working on the unit circle, we give such an account through a dichotomy between two complexity measures of the target: its $\textbf{Fourier complexity}$, which controls NT...
- Summary (fallback): 机器翻译摘要显示：持续的经验观察表明，经过训练的神经网络在具有组合结构的任务上超越了其神经正切内核（NTK）的限制，但缺乏对 $\textbf{when}$ 和 $\textbf{by how much}$ 的定量说明。在单位圆上，我们通过目标的两个复杂性度量之间的二分法给出这样的解释：它的$\textbf{傅里叶复杂度}$，它控制NTK核回归，它的$\textbf{架构复杂度}$，它控制深度$L$、宽度$w$ReLU网络的学习，权重的变化范数以$R$为界。我们首先描述架构类 $\mathcal{C}_{L,w,R}$ 的极小极大速率，将其固定为 $L$ 的单个因子：在 $Ω(Lw^2R^2/n)$ 和 $\tilde{O}(L^2w^2R^2/n)$ 之间。
- Keywords: textbf, kernel, compositional, neural, complexity

### 14. [柔性蛋白质组件膜弯曲的动态模拟](https://arxiv.org/abs/2607.06378v1)
- Original title: Dynamical Simulation of Membrane Bending by Flexible Protein Assemblies
- Authors: Samuel L. Foley, Margaret E. Johnson
- Meta: 2026-07-07 | cond-mat.soft
- 中文摘要: 膜变形蛋白晶格在基本和致病的生物过程中发挥着关键作用，包括内吞作用和病毒出芽。对于如此大规模的膜重塑事件来说，在模拟中获得必要的长度和时间尺度可能很困难。我们提出了一个柔性蛋白质晶格模型，该模型与赫尔弗里希膜耦合，在过阻尼状态下在傅立叶空间中传播。我们主要关注膜结合网格蛋白晶格，它是内吞机制的重要组成部分。我们使用屈曲方法来量化网格蛋白模型晶格的材料特性，以测量弯曲刚度，因为它随粗粒势能函数的力常数而变化。
- Abstract: Membrane-deforming protein lattices play a key role in essential and pathogenic biological processes, including endocytosis and viral budding. Attaining the necessary length- and time-scales in simulation can be difficult for such large-scale membrane remodeling events. We present a model of a flexible protein lattice coupled to a Helfrich membrane propagated in Fourier space in the over-damped regime. We focus prim...
- Summary (fallback): 机器翻译摘要显示：膜变形蛋白晶格在基本和致病的生物过程中发挥着关键作用，包括内吞作用和病毒出芽。对于如此大规模的膜重塑事件来说，在模拟中获得必要的长度和时间尺度可能很困难。我们提出了一个柔性蛋白质晶格模型，该模型与赫尔弗里希膜耦合，在过阻尼状态下在傅立叶空间中传播。我们主要关注膜结合网格蛋白晶格，它是内吞机制的重要组成部分。我们使用屈曲方法来量化网格蛋白模型晶格的材料特性，以测量弯曲刚度，因为它随粗粒势能函数的力常数而变化。
- Keywords: membrane, bending, protein, lattices, clathrin

### 15. [具有动作缓存和细化的视觉-语言-动作模型的免训练加速](https://arxiv.org/abs/2607.06370v1)
- Original title: Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement
- Authors: Ryuji Oi, Hikari Otsuka, Kosuke Matsushima, Yuki Ichikawa, Masato Motomura et al.
- Meta: 2026-07-07 | cs.RO
- 中文摘要: 视觉-语言-动作（VLA）模型已成为通用机器人操作的一种有前途的方法。特别是，基于流匹配的 VLA 模型由于能够生成精确且平滑的动作序列并捕获多模态分布而取得了显着的成功。然而，动作头中的迭代去噪过程是主要的计算瓶颈，对实时部署提出了严峻的挑战。为了应对这一挑战，我们提出了 ActionCache，这是一种即插即用的外部缓存，它可以机会性地重用过去的中间操作，以从目标操作附近热启动生成，从而大大减少推理延迟。具体来说，ActionCache 使用紧凑的多模式键存储中间操作，这使得可以从不同情节甚至不同任务的类似过去​​上下文中进行检索。
- Abstract: Vision-Language-Action (VLA) models have emerged as a promising approach for generalizable robotic manipulations. In particular, flow matching-based VLA models have shown remarkable success due to their capability to generate precise and smooth action sequences and capture multimodal distributions. However, the iterative denoising process in the action head acts as a major computational bottleneck, posing a critical...
- Summary (fallback): 机器翻译摘要显示：视觉-语言-动作（VLA）模型已成为通用机器人操作的一种有前途的方法。特别是，基于流匹配的 VLA 模型由于能够生成精确且平滑的动作序列并捕获多模态分布而取得了显着的成功。然而，动作头中的迭代去噪过程是主要的计算瓶颈，对实时部署提出了严峻的挑战。为了应对这一挑战，我们提出了 ActionCache，这是一种即插即用的外部缓存，它可以机会性地重用过去的中间操作，以从目标操作附近热启动生成，从而大大减少推理延迟。具体来说，ActionCache 使用紧凑的多模式键存储中间操作，这使得可以从不同情节甚至不同任务的类似过去​​上下文中进行检索。
- Keywords: models, action, actioncache, actions, acceleration

### 16. [基于 Deep Ritz 方法的高维稳态薛定谔方程的特征学习](https://arxiv.org/abs/2607.06369v1)
- Original title: Feature Learning for the High Dimensional Stationary Schödinger Equation with Deep Ritz Method
- Authors: Yao Yao, Yulong Lu, Gilad Lerman
- Meta: 2026-07-07 | math.OC
- 中文摘要: 本文研究了深度 Ritz 方法框架内的特征学习，用于求解具有诺伊曼边界条件的平稳薛定谔方程。我们首先分析黎曼梯度下降在不可知环境中的收敛性，其中假设函数仅限于单指标模型，而偏微分方程解是任意的。我们证明梯度下降达到近似全局最小值：经过 T = O(log(1/ε)) 次迭代后，损失在最优损失的常数倍的 ε 范围内。然后，我们检查当偏微分方程本身的源项遵循单指数模型时的损失情况，并考虑由单指数模型或两神经元多指数模型给出的假设函数。在单索引情况下，我们表明在与源项的特征向量对齐的特征向量处获得了最小 Ritz 能量。
- Abstract: This paper investigates feature learning within the framework of the deep Ritz method for solving the stationary Schrödinger equation with Neumann boundary conditions. We first analyze the convergence of Riemannian gradient descent in an agnostic setting, where the hypothesis function is restricted to a single-index model while the PDE solution is arbitrary. We prove that gradient descent reaches an approximate glob...
- Summary (fallback): 机器翻译摘要显示：本文研究了深度 Ritz 方法框架内的特征学习，用于求解具有诺伊曼边界条件的平稳薛定谔方程。我们首先分析黎曼梯度下降在不可知环境中的收敛性，其中假设函数仅限于单指标模型，而偏微分方程解是任意的。我们证明梯度下降达到近似全局最小值：经过 T = O(log(1/ε)) 次迭代后，损失在最优损失的常数倍的 ε 范围内。然后，我们检查当偏微分方程本身的源项遵循单指数模型时的损失情况，并考虑由单指数模型或两神经元多指数模型给出的假设函数。在单索引情况下，我们表明在与源项的特征向量对齐的特征向量处获得了最小 Ritz 能量。
- Keywords: feature, ritz, single-index, model, loss

### 17. [因子增强机器学习面板回归](https://arxiv.org/abs/2607.06368v1)
- Original title: Factor-Augmented Machine Learning Panel Regressions
- Authors: Andrii Babii, Luca Barbaglia, Eric Ghysels, Jonas Striaukas
- Meta: 2026-07-07 | econ.EM
- 中文摘要: 本文发展了在由常见冲击驱动的横截面相关误差的情况下进行高维面板数据回归的渐近理论。我们考虑将 MIDAS 聚合与潜在因子相结合的因子增强稀疏组 LASSO 估计器。估计器可以利用时间序列维度中的混合频率组结构。理论表明，它在预测和估计方面都优于标准 LASSO 估计器，同时允许横截面依赖性。
- Abstract: This paper develops the asymptotic theory for high-dimensional panel data regressions in settings with cross-sectionally dependent errors driven by common shocks. We consider a factor-augmented sparse-group LASSO estimator that combines MIDAS aggregation with latent factors. The estimator can take advantage of the mixed-frequency group structure in the time-series dimension. Theory shows that it can outperform the s...
- Summary (fallback): 机器翻译摘要显示：本文发展了在由常见冲击驱动的横截面相关误差的情况下进行高维面板数据回归的渐近理论。我们考虑将 MIDAS 聚合与潜在因子相结合的因子增强稀疏组 LASSO 估计器。估计器可以利用时间序列维度中的混合频率组结构。理论表明，它在预测和估计方面都优于标准 LASSO 估计器，同时允许横截面依赖性。
- Keywords: estimator, factor-augmented, panel, regressions, theory

### 18. [正态均值估计中收缩阈值规则的近似风险最小化](https://arxiv.org/abs/2607.06367v1)
- Original title: Approximate Risk Minimization Over Shrinking-Thresholding Rules in Normal Mean Estimation
- Authors: Wei Jiang
- Meta: 2026-07-07 | math.ST
- 中文摘要: 我们开发了一个近似风险最小化框架，用于正常均值问题中的收缩阈值估计。在规范多元正态均值模型中，我们引入了通用函数类估计器，其中包含经典收缩和阈值行为，包括 James-Stein 型和套索型规则。我们将二次风险表示为此类的函数，推导出预言风险和数据驱动的近似风险最小化的最优条件，并在预言风险不可用时从观察到的数据构建可行的近似风险准则。由此产生的估计量 NOMAD 是通过最小化建议类别的近似风险而获得的。
- Abstract: We develop an approximate risk minimization framework for shrinkage-thresholding estimation in normal mean problems. In the canonical multivariate normal mean model, we introduce a general functional class of estimators that contains classical shrinkage and thresholding behavior, including James-Stein-type and lasso-type rules. We express quadratic risk as a functional over this class, derive optimality conditions f...
- Summary (fallback): 机器翻译摘要显示：我们开发了一个近似风险最小化框架，用于正常均值问题中的收缩阈值估计。在规范多元正态均值模型中，我们引入了通用函数类估计器，其中包含经典收缩和阈值行为，包括 James-Stein 型和套索型规则。我们将二次风险表示为此类的函数，推导出预言风险和数据驱动的近似风险最小化的最优条件，并在预言风险不可用时从观察到的数据构建可行的近似风险准则。由此产生的估计量 NOMAD 是通过最小化建议类别的近似风险而获得的。
- Keywords: risk, approximate, normal, mean, minimization

### 19. [用于甲烷生物特征预测的广义微生物细胞模型](https://arxiv.org/abs/2607.06366v1)
- Original title: A generalised microbial cell model for methane biosignature predictions
- Authors: Arwen E. Nicholson, Nathan J. Mayne
- Meta: 2026-07-07 | astro-ph.EP
- 中文摘要: 迄今为止检测到的大多数潜在宜居行星可能与地球有很大不同，例如，半径和质量更大，自转速度不同，并且主星光谱与太阳不同。因此，第一个被发现的外星生命可能生活在我们星球上不存在的条件下。这就需要一种通用的生物学建模方法，该方法可以应用于多种行星场景，建立在地球生命的基础知识的基础上，但不仅限于此。在这里，我们探索了微生物细胞的广义模型，其代谢率受热力学和跨细胞壁的底物扩散控制。我们模拟了一个由产生甲烷的微生物组成的单一物种生物圈，并确定了细胞大小、细胞死亡率和生物质合成成本的变化如何影响地球上的生物特征——在本例中是甲烷。
- Abstract: The majority of potentially habitable planets detected to date are likely quite different to Earth, for example, being larger in radius and mass, differing rotation rates and with host star spectra unlike the Sun. Therefore the first alien life detected will potentially be living in conditions not found on our planet. This necessitates a generalised approach to modelling biology that can be applied to numerous plane...
- Summary (fallback): 机器翻译摘要显示：迄今为止检测到的大多数潜在宜居行星可能与地球有很大不同，例如，半径和质量更大，自转速度不同，并且主星光谱与太阳不同。因此，第一个被发现的外星生命可能生活在我们星球上不存在的条件下。这就需要一种通用的生物学建模方法，该方法可以应用于多种行星场景，建立在地球生命的基础知识的基础上，但不仅限于此。在这里，我们探索了微生物细胞的广义模型，其代谢率受热力学和跨细胞壁的底物扩散控制。我们模拟了一个由产生甲烷的微生物组成的单一物种生物圈，并确定了细胞大小、细胞死亡率和生物质合成成本的变化如何影响地球上的生物特征——在本例中是甲烷。
- Keywords: cell, model, generalised, methane, biosignature

### 20. [TMF-RSE：具有区域语义和证据不确定性的三模态融合，用于肺部严重程度评分](https://arxiv.org/abs/2607.06356v1)
- Original title: TMF-RSE: Tri-Modal Fusion with Regional Semantics and Evidential Uncertainty for Lung Severity Scoring
- Authors: Fadi Abdeladhim Zidi, Salah Eddine Bekhouche, Abdellah Zakaria Sellam, Gaby Maroun, Fadi Dornaika et al.
- Meta: 2026-07-07 | eess.IV
- 中文摘要: 通过胸部影像准确量化肺部疾病的严重程度对于临床决策和资源分配至关重要。我们提出了一种三模态深度学习框架 TMF-RSE（具有区域语义和证据不确定性的三模态融合），该框架结合了二维胸部输入的外观特征、肺分割掩模的结构特征以及视觉语言模型（VLM）的语义特征以进行严重程度量化。我们的方法采用互补的融合机制，集成了语义指导、结构先验和跨模态的分层交互。该模型采用证据回归来提供严重性预测和不确定性估计。
- Abstract: Accurate quantification of lung disease severity from chest imaging is critical for clinical decision-making and resource allocation. We propose a tri-modal deep learning framework, TMF-RSE (Tri-Modal Fusion with Regional Semantics and Evidential Uncertainty), that combines appearance features from two-dimensional chest inputs, structural features from lung segmentation masks, and semantic features from vision-langu...
- Summary (fallback): 机器翻译摘要显示：通过胸部影像准确量化肺部疾病的严重程度对于临床决策和资源分配至关重要。我们提出了一种三模态深度学习框架 TMF-RSE（具有区域语义和证据不确定性的三模态融合），该框架结合了二维胸部输入的外观特征、肺分割掩模的结构特征以及视觉语言模型（VLM）的语义特征以进行严重程度量化。我们的方法采用互补的融合机制，集成了语义指导、结构先验和跨模态的分层交互。该模型采用证据回归来提供严重性预测和不确定性估计。
- Keywords: severity, tmf-rse, tri-modal, fusion, evidential

### 21. [PDE 解决方案系列的物理信息神经嵌入](https://arxiv.org/abs/2607.06348v1)
- Original title: Physics-Informed Neural Embeddings of PDE Solution Families
- Authors: Raul Jimenez, Svitlana Mayboroda, Pavlos Protopapas, Leonid Sarieddine, David N. Spergel et al.
- Meta: 2026-07-07 | cs.LG
- 中文摘要: 我们引入了一个基于物理的框架，用于学习偏微分方程解族的有限维嵌入。该方法使用多头物理信息神经网络，其中共享体学习表示解空间的潜在流形，而线性头重建与不同初始条件相关的单独解。头部正交化惩罚消除了潜在表示的简并性，并稳定了训练实现中的主成分谱。由于初始条件是通过构建构建到网络输出中的，因此这些主成分衡量的是网络在初始配置文件之上学习的额外可变性，而不是完整的解决方案本身。我们将该方法应用于一维粘性 Burgers 方程，并用热方程和波动方程作为鲁棒性检查。
- Abstract: We introduce a physics-informed framework for learning finite-dimensional embeddings of solution families of partial differential equations. The method uses a multihead Physics-Informed Neural Network in which a shared body learns a latent manifold representing the solution space, while linear heads reconstruct individual solutions associated with different initial conditions. A head-orthogonalization penalty remove...
- Summary (fallback): 机器翻译摘要显示：我们引入了一个基于物理的框架，用于学习偏微分方程解族的有限维嵌入。该方法使用多头物理信息神经网络，其中共享体学习表示解空间的潜在流形，而线性头重建与不同初始条件相关的单独解。头部正交化惩罚消除了潜在表示的简并性，并稳定了训练实现中的主成分谱。由于初始条件是通过构建构建到网络输出中的，因此这些主成分衡量的是网络在初始配置文件之上学习的额外可变性，而不是完整的解决方案本身。我们将该方法应用于一维粘性 Burgers 方程，并用热方程和波动方程作为鲁棒性检查。
- Keywords: solution, latent, principal, physics-informed, equations

### 22. [随机高效差分隐私的抖动高斯机制](https://arxiv.org/abs/2607.06320v1)
- Original title: Dithered Gaussian Mechanism for Randomness-Efficient Differential Privacy
- Authors: Nikita P. Kalinin, Rasmus Pagh
- Meta: 2026-07-07 | cs.CR
- 中文摘要: 我们提出了抖动高斯机制，这是差分隐私离散高斯机制的一种新颖替代方案，它离散化私人输出而不是噪声分布本身。通过将这种离散化解释为高斯机制的后处理，我们的构造直接继承了标准高斯机制的隐私保证，同时避免了有限精度浮点输出导致的漏洞。我们证明该机制是随机有效的：通过直接对离散输出值进行采样，可以显着减少隐私所需的高质量随机位的数量，并且使其与噪声水平无关。
- Abstract: We present the dithered Gaussian mechanism, a novel alternative to the discrete Gaussian mechanism for differential privacy that discretizes the private output rather than the noise distribution itself. By interpreting this discretization as post-processing of the Gaussian mechanism, our construction directly inherits the privacy guarantees of the standard Gaussian mechanism while avoiding vulnerabilities caused by...
- Summary (fallback): 机器翻译摘要显示：我们提出了抖动高斯机制，这是差分隐私离散高斯机制的一种新颖替代方案，它离散化私人输出而不是噪声分布本身。通过将这种离散化解释为高斯机制的后处理，我们的构造直接继承了标准高斯机制的隐私保证，同时避免了有限精度浮点输出导致的漏洞。我们证明该机制是随机有效的：通过直接对离散输出值进行采样，可以显着减少隐私所需的高质量随机位的数量，并且使其与噪声水平无关。
- Keywords: mechanism, gaussian, privacy, noise, randomness

### 23. [微分方程高斯过程逼近的统一视角](https://arxiv.org/abs/2607.06292v1)
- Original title: A unified perspective of Gaussian process approximation for differential equations
- Authors: Mengwu Guo
- Meta: 2026-07-07 | math.NA
- 中文摘要: 高斯过程用于逼近微分方程的应用迅速扩展，导致数值方法不断增长、多样化且分散。我们提出了一个统一的贝叶斯观点，将这些技术置于一个共同的概率框架内，基于将微分方程约束纳入可能性的导数匹配解释。这种统一的视角支持参数估计和解近似，并展示了如何在其中理解一系列现有方法。这项工作旨在巩固当前的发展并为未来的研究奠定基础。
- Abstract: The use of Gaussian processes for approximating differential equations has expanded rapidly, leading to a growing, diverse, and fragmented body of numerical methods. We present a unified Bayesian perspective that places these techniques within a common probabilistic framework, based on a derivative matching interpretation for incorporating differential equation constraints into likelihood. This unified perspective s...
- Summary (fallback): 机器翻译摘要显示：高斯过程用于逼近微分方程的应用迅速扩展，导致数值方法不断增长、多样化且分散。我们提出了一个统一的贝叶斯观点，将这些技术置于一个共同的概率框架内，基于将微分方程约束纳入可能性的导数匹配解释。这种统一的视角支持参数估计和解近似，并展示了如何在其中理解一系列现有方法。这项工作旨在巩固当前的发展并为未来的研究奠定基础。
- Keywords: unified, perspective, differential, gaussian, approximation

### 24. [张量程序的定量高斯过程极限](https://arxiv.org/abs/2607.06290v1)
- Original title: Quantitative Gaussian-Process limits of Tensor Programs
- Authors: Andrea Agazzi, Eloy Mosig García, Dario Trevisan
- Meta: 2026-07-07 | cs.LG
- 中文摘要: 我们通过张量程序的视角研究了随机神经网络的无限宽度高斯过程极限，并提供了 Wasserstein 距离的定量收敛理论。我们的主要结果给出了明确的有限宽度误差界限，其阶数为有限网络执行与其高斯过程极限之间的宽度的倒数平方根。该框架与架构无关，涵盖前馈模型以及与循环和变压器型架构相关的权重共享方案。
- Abstract: We study the infinite-width Gaussian-process limit of random neural networks through the lens of tensor programs, and we provide a quantitative convergence theory in Wasserstein distance. Our main result gives explicit finite-width error bounds, of order inverse square-root of the widths between finite-network executions and their Gaussian-process limits. The framework is architecture-agnostic and covers feed-forwar...
- Summary (fallback): 机器翻译摘要显示：我们通过张量程序的视角研究了随机神经网络的无限宽度高斯过程极限，并提供了 Wasserstein 距离的定量收敛理论。我们的主要结果给出了明确的有限宽度误差界限，其阶数为有限网络执行与其高斯过程极限之间的宽度的倒数平方根。该框架与架构无关，涵盖前馈模型以及与循环和变压器型架构相关的权重共享方案。
- Keywords: gaussian-process, quantitative, limits, tensor, programs

### 25. [基于内核的算子学习：误差分析、预算分配和物理信息扩展](https://arxiv.org/abs/2607.06287v1)
- Original title: Kernel-based Operator Learning: Error Analysis, Budget Allocation, and a Physics-Informed Extension
- Authors: Rüdiger Kempf
- Meta: 2026-07-07 | math.NA
- 中文摘要: 我们在两阶段采样框架中研究基于核的算子学习，其中离线核回归算子从输入输出对中学习目标算子的离散化表示，在线核重建算子从预测观测中恢复输出函数。我们的主要理论贡献是与训练对的数量 $N$、输入观测的数量 $n$ 以及输出分辨率 $m$ 相关的明确预算分配条件。该条件源自耦合误差分析，该分析将替代项解释为近似数据的重建。这会将总误差分解为可以独立分析的重建和学习贡献。
- Abstract: We study kernel-based operator learning in a two-stage sampling framework, where an offline kernel regression operator learns a discretized representation of the target operator from input-output pairs and an online kernel reconstruction operator recovers the output function from predicted observations. Our main theoretical contribution is an explicit budget allocation condition relating the number $N$ of training p...
- Summary (fallback): 机器翻译摘要显示：我们在两阶段采样框架中研究基于核的算子学习，其中离线核回归算子从输入输出对中学习目标算子的离散化表示，在线核重建算子从预测观测中恢复输出函数。我们的主要理论贡献是与训练对的数量 $N$、输入观测的数量 $n$ 以及输出分辨率 $m$ 相关的明确预算分配条件。该条件源自耦合误差分析，该分析将替代项解释为近似数据的重建。这会将总误差分解为可以独立分析的重建和学习贡献。
- Keywords: operator, reconstruction, learning, kernel-based, error

### 26. [量化夹带证据：信息处理路径图的频率论和贝叶斯方法的比较](https://arxiv.org/abs/2607.06284v1)
- Original title: Quantifying Entrainment Evidence: A Comparison of Frequentist and Bayesian Approaches for Information Processing Pathway Maps
- Authors: Kaibo Zhang, Ji Wu, Chao Zhang, Andrew Thwaites
- Meta: 2026-07-07 | q-bio.NC
- 中文摘要: 信息处理路径图 (IPPM) 提供了一个可扩展的框架，用于形式化应用于感官刺激的复杂数学变换序列。这些图描绘了计算步骤的延迟和皮质表达，依靠统计推断将模型输出与观察到的神经活动联系起来。传统上，这种映射依赖于频率假设检验。然而，确定几种竞争计算模型中的哪一种最能解释神经数据是模型裁决的问题，可以说更适合概率推理。在这里，我们对已建立的频率论方法和用于映射皮质夹带的新颖贝叶斯框架进行了直接比较。
- Abstract: Information Processing Pathway Maps (IPPMs) offer a scalable framework for formalizing the complex sequence of mathematical transformations applied to sensory stimuli. These maps chart the latency and cortical expression of computational steps, relying on statistical inference to link model outputs with observed neural activity. Traditionally, this mapping has relied on frequentist hypothesis testing. However, deter...
- Summary (fallback): 机器翻译摘要显示：信息处理路径图 (IPPM) 提供了一个可扩展的框架，用于形式化应用于感官刺激的复杂数学变换序列。这些图描绘了计算步骤的延迟和皮质表达，依靠统计推断将模型输出与观察到的神经活动联系起来。传统上，这种映射依赖于频率假设检验。然而，确定几种竞争计算模型中的哪一种最能解释神经数据是模型裁决的问题，可以说更适合概率推理。在这里，我们对已建立的频率论方法和用于映射皮质夹带的新颖贝叶斯框架进行了直接比较。
- Keywords: evidence, frequentist, bayesian, pathway, maps

### 27. [揭示铁电向列液晶巨介电响应背后的集体模式](https://arxiv.org/abs/2607.06257v1)
- Original title: Uncovering Collective Modes Underlying the Giant Dielectric Response of Ferroelectric Nematic Liquid Crystals
- Authors: Kazuma Nakajima, Hirokazu Kamifuji, Masanori Ozaki, Hirotsugu Kikuchi, Kenjiro Fukuda
- Meta: 2026-07-07 | cond-mat.soft
- 中文摘要: 铁电向列液晶（FNLC）是一种极性流体，其中自发极化与向列取向顺序共存，从而产生不寻常的介电和机电响应。然而，其巨大介电响应背后的集体模式仍不清楚。在这里，我们证明这种响应源自两种不同松弛模式的叠加，而不是单个过程。介电谱表明，低频模式表现出与短轴分子旋转相关的类似软模式的行为，而高频模式对应于围绕指向矢旋转的有效横向偏振分量的类似戈德斯通的相移。这些任务得到了对温度、电场、单元厚度和对准层依赖性的系统分析的支持。
- Abstract: Ferroelectric nematic liquid crystals (FNLCs) are polar fluids in which spontaneous polarization coexists with nematic orientational order, giving rise to unusual dielectric and electromechanical responses. However, the collective modes underlying their giant dielectric response remain unclear. Here, we show that this response originates from the superposition of two distinct relaxation modes rather than a single pr...
- Summary (fallback): 机器翻译摘要显示：铁电向列液晶（FNLC）是一种极性流体，其中自发极化与向列取向顺序共存，从而产生不寻常的介电和机电响应。然而，其巨大介电响应背后的集体模式仍不清楚。在这里，我们证明这种响应源自两种不同松弛模式的叠加，而不是单个过程。介电谱表明，低频模式表现出与短轴分子旋转相关的类似软模式的行为，而高频模式对应于围绕指向矢旋转的有效横向偏振分量的类似戈德斯通的相移。这些任务得到了对温度、电场、单元厚度和对准层依赖性的系统分析的支持。
- Keywords: dielectric, response, nematic, collective, modes

### 28. [基于神经似然的贝叶斯逆问题的凸逼近框架](https://arxiv.org/abs/2607.06252v1)
- Original title: A Convex Approximation Framework for Neural Likelihood-Based Bayesian Inverse Problems
- Authors: Fabian Schneider, Tapio Helin, Leila Taghizadeh
- Meta: 2026-07-07 | stat.ML
- 中文摘要: 科学和工程中的许多问题难以准确建模，这要么是由于未知的物理机制、量化的测量不确定性较差，要么是由于高保真模拟的计算成本过高。这些挑战限制了马尔可夫链蒙特卡罗等经典概率推理方法的适用性，特别是在高维贝叶斯逆问题中。随着科学实验数据变得越来越可用，机器学习方法为显式参数建模提供了灵活的替代方案。我们研究神经似然近似，其目标是直接从数据中学习似然函数，而不需要明确了解底层数据生成过程。
- Abstract: Many problems in science and engineering are difficult to model accurately, either due to unknown physical mechanisms, poorly quantified measurement uncertainty, or prohibitive computational costs of high-fidelity simulations. These challenges limit the applicability of classical probabilistic inference methods such as Markov chain Monte Carlo, especially in high-dimensional Bayesian inverse problems. As data from s...
- Summary (fallback): 机器翻译摘要显示：科学和工程中的许多问题难以准确建模，这要么是由于未知的物理机制、量化的测量不确定性较差，要么是由于高保真模拟的计算成本过高。这些挑战限制了马尔可夫链蒙特卡罗等经典概率推理方法的适用性，特别是在高维贝叶斯逆问题中。随着科学实验数据变得越来越可用，机器学习方法为显式参数建模提供了灵活的替代方案。我们研究神经似然近似，其目标是直接从数据中学习似然函数，而不需要明确了解底层数据生成过程。
- Keywords: likelihood, approximation, neural, problems, convex

### 29. [PhyMRI-SR：迈向物理感知 MRI 图像超分辨率](https://arxiv.org/abs/2607.06238v1)
- Original title: PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution
- Authors: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li et al.
- Meta: 2026-07-07 | cs.CV
- 中文摘要: 磁共振成像 (MRI) 超分辨率对于提高诊断可及性至关重要，但大多数方法将其视为从固定低分辨率输入到高分辨率目标的确定性映射。这忽视了 MRI 采集物理的一个关键属性：空间分辨率和信噪比 (SNR) 本质上是耦合的，使得任何给定的低分辨率扫描只是在不同采集权衡下的许多可能实现之一。我们将 MRI 超分辨率重新视为物理感知重建问题，其目标是确定最佳分辨率-SNR 配置，然后对其进行超分辨率以获得高质量的 MRI 结果。这个公式的一个关键含义是 MRI 分辨率变得动态而不是固定的。
- Abstract: Magnetic resonance imaging (MRI) super-resolution is vital for improving diagnostic accessibility, yet most methods treat it as a deterministic mapping from a fixed low-resolution input to a high-resolution target. This overlooks a key property of MRI acquisition physics: spatial resolution and signal-to-noise ratio (SNR) are inherently coupled, making any given low-resolution scan merely one of many possible realiz...
- Summary (fallback): 机器翻译摘要显示：磁共振成像 (MRI) 超分辨率对于提高诊断可及性至关重要，但大多数方法将其视为从固定低分辨率输入到高分辨率目标的确定性映射。这忽视了 MRI 采集物理的一个关键属性：空间分辨率和信噪比 (SNR) 本质上是耦合的，使得任何给定的低分辨率扫描只是在不同采集权衡下的许多可能实现之一。我们将 MRI 超分辨率重新视为物理感知重建问题，其目标是确定最佳分辨率-SNR 配置，然后对其进行超分辨率以获得高质量的 MRI 结果。这个公式的一个关键含义是 MRI 分辨率变得动态而不是固定的。
- Keywords: super-resolution, physics-aware, imaging, fixed, low-resolution

### 30. [模拟免疫增强对人群疫苗有效性的影响](https://arxiv.org/abs/2607.06235v1)
- Original title: Modeling the Impact of Immune Boosting on Population-Level Vaccine Effectiveness
- Authors: Nir Gavish, Guy Katriel, Zohar Rom-Ramon
- Meta: 2026-07-07 | q-bio.PE
- 中文摘要: 我们扩展了标准的易感者感染恢复框架，以在短期爆发期间纳入自然免疫增强。通过推导封闭式最终规模关系，我们分析地将总发病率与提高动态和疫苗覆盖率联系起来。该框架确定了一个关键的加强阈值：高于该阈值，更高的疫苗覆盖率反而会降低相对疫苗有效性。发生这种情况是因为成功的流行病抑制剥夺了接种疫苗的个体维持其相对免疫优势所需的沉默病原体暴露。至关重要的是，总体人口层面的影响仍然是有益的，持续减少绝对疾病负担。对于高度传播的变体，渐近分析表明，相对疫苗有效性收敛到完全独立于覆盖范围的正极限。
- Abstract: We extend the standard susceptible-infected-recovered framework to incorporate natural immune boosting during a short-scale outbreak. By deriving closed-form final size relations, we analytically link total attack rates to boosting dynamics and vaccine coverage. This framework identifies a critical boosting threshold: above it, higher vaccine coverage paradoxically decreases relative vaccine effectiveness. This occu...
- Summary (fallback): 机器翻译摘要显示：我们扩展了标准的易感者感染恢复框架，以在短期爆发期间纳入自然免疫增强。通过推导封闭式最终规模关系，我们分析地将总发病率与提高动态和疫苗覆盖率联系起来。该框架确定了一个关键的加强阈值：高于该阈值，更高的疫苗覆盖率反而会降低相对疫苗有效性。发生这种情况是因为成功的流行病抑制剥夺了接种疫苗的个体维持其相对免疫优势所需的沉默病原体暴露。至关重要的是，总体人口层面的影响仍然是有益的，持续减少绝对疾病负担。对于高度传播的变体，渐近分析表明，相对疫苗有效性收敛到完全独立于覆盖范围的正极限。
- Keywords: vaccine, boosting, effectiveness, coverage, relative

## biorxiv

### 1. [PEPstrMOD2：化学修饰和非天然肽的下一代三级结构预测](https://www.biorxiv.org/content/10.64898/2026.06.22.733733v2)
- Original title: PEPstrMOD2: Next-generation tertiary structure prediction of chemically modified and non-natural peptides
- Authors: Jain, S., Mehta, N. K., Raina, S., Kumar, P., Varun, V. et al.
- Meta: 2026-07-07 | bioinformatics | DOI: 10.64898/2026.06.22.733733
- 中文摘要: 虽然大多数现有方法仅限于预测仅包含规范残基的蛋白质的三级结构，但 PEPstrMOD 服务器（2015 年开发）开创了化学修饰和非天然肽的结构预测。尽管其广泛使用，但最初的框架仅限于 7 至 25 个残基的肽，并且依赖于较旧的主干预测算法。为了解决这些限制，我们推出了 PEPstrMOD2，它比其前身引入了三项重大进步。首先，它用最先进的深度学习 (DL) 算法取代了原来的内部坐标生成，利用 AlphaFold2 和 ESMFold 进行高精度的初始结构预测。
- Abstract: While most existing methods are limited to predicting the tertiary structures of proteins containing only canonical residues, the PEPstrMOD server (developed in 2015) pioneered structure prediction for chemically modified and non-natural peptides. Despite its widespread use, the original framework was restricted to peptides of 7 to 25 residues and relied on older backbone-prediction algorithms. To address these limi...
- Summary (fallback): 机器翻译摘要显示：虽然大多数现有方法仅限于预测仅包含规范残基的蛋白质的三级结构，但 PEPstrMOD 服务器（2015 年开发）开创了化学修饰和非天然肽的结构预测。尽管其广泛使用，但最初的框架仅限于 7 至 25 个残基的肽，并且依赖于较旧的主干预测算法。为了解决这些限制，我们推出了 PEPstrMOD2，它比其前身引入了三项重大进步。首先，它用最先进的深度学习 (DL) 算法取代了原来的内部坐标生成，利用 AlphaFold2 和 ESMFold 进行高精度的初始结构预测。
- Keywords: pepstrmod2, angstroms, peptides, original, pepstrmod

### 2. [MDL-001：一种口服、直接作用的通用抗病毒药物，用于治疗流感样疾病 (ILI) 和慢性肝炎](https://www.biorxiv.org/content/10.1101/2025.01.13.632836v5)
- Original title: MDL-001: an Oral, Direct-Acting Universal Antiviral for Influenza-Like Illness (ILI) and Chronic Hepatitis
- Authors: Woods, V., Umansky, T., Russell, S. M., Goodman, A., Bobardt, M. et al.
- Meta: 2026-07-07 | pharmacology and toxicology | DOI: 10.1101/2025.01.13.632836
- 中文摘要: 由流感、呼吸道合胞病毒和冠状病毒引起的地方性病毒性呼吸道疾病每年给全球造成数亿人感染和数十万人死亡的疾病负担。全球分别有 2.54 亿和 5800 万人患有慢性乙型肝炎和丙型肝炎感染。没有批准的治疗方法可以针对一种以上的病毒。 MDL-001 是一种口服、直接作用、广谱抗病毒药物，针对病毒聚合酶的 Thumb-1 变构位点。在这里，我们报告 MDL-001 在体外以纳摩尔 EC90 效力抑制甲型/乙型流感、RSV、SARS-CoV-2、地方性人类冠状病毒和乙型/丙型/丁型肝炎病毒。 MDL-001 在体内对抗小鼠致死性甲型流感的功效与奥司他韦相当，可将肺部病毒载量降低 2.6 log10，并防止体重减轻和死亡。 MDL-001 在 SARS-CoV 中表现出与皮下注射瑞德西韦相同的症状减轻作用...
- Abstract: Endemic viral respiratory illnesses caused by influenza, RSV, and coronaviruses impose a global disease burden of hundreds of millions of infections and hundreds of thousands of deaths annually. Chronic hepatitis B and C infections persist in 254 million and 58 million people worldwide, respectively. No approved therapy addresses more than one virus. MDL-001 is an oral, direct-acting, broad-spectrum antiviral target...
- Summary (fallback): 机器翻译摘要显示：由流感、呼吸道合胞病毒和冠状病毒引起的地方性病毒性呼吸道疾病每年给全球造成数亿人感染和数十万人死亡的疾病负担。全球分别有 2.54 亿和 5800 万人患有慢性乙型肝炎和丙型肝炎感染。没有批准的治疗方法可以针对一种以上的病毒。 MDL-001 是一种口服、直接作用、广谱抗病毒药物，针对病毒聚合酶的 Thumb-1 变构位点。在这里，我们报告 MDL-001 在体外以纳摩尔 EC90 效力抑制甲型/乙型流感、RSV、SARS-CoV-2、地方性人类冠状病毒和乙型/丙型/丁型肝炎病毒。 MDL-001 在体内对抗小鼠致死性甲型流感的功效与奥司他韦相当，可将肺部病毒载量降低 2.6 log10，并防止体重减轻和死亡。 MDL-001 在 SARS-CoV 中表现出与皮下注射瑞德西韦相同的症状减轻作用...
- Keywords: mdl-001, oral, sars-cov-2, log10, viral

### 3. [雄性小鼠的催产素受体阻断改变了性别偏好并破坏了中间社会等级的稳定，但不影响一般社会偏好](https://www.biorxiv.org/content/10.1101/2022.07.23.501222v3)
- Original title: Oxytocin receptor blockade in male mice alters sex preference and destabilizes intermediate social ranks without affecting general social preference
- Authors: Nasukawa, D., Matsushima, S., Yamada, K., Ujihara, Y., Hirakata, H. et al.
- Meta: 2026-07-07 | neuroscience | DOI: 10.1101/2022.07.23.501222
- 中文摘要: 群体内的社会等级对于许多动物的生存至关重要。在社区中的排名有助于避免不必要的冲突并与他人建立稳定的关系。催产素因其在社会行为中的作用而受到越来越多的关注。然而，催产素受体信号传导与社会等级之间的因果关系仍不清楚。在这里，我们研究了腹膜内施用血脑屏障穿透性催产素受体拮抗剂 L-368-899 对雄性小鼠的（1）社会等级、（2）性别偏好、（3）社会偏好和（4）二元相互作用的影响。在试管测试中，催产素受体阻断对第一等级小鼠没有影响，但增加了第二等级小鼠的等级波动，表明催产素受体信号传导有助于中间社会等级的稳定性。
- Abstract: Social rank within a group is essential for survival in many animals. Rank in the community helps to avoid unnecessary conflicts and establish stable relationships with others. Oxytocin has received increasing attention for its function in social behavior. However, the causal relationship between oxytocin receptor signaling and social rank remains unclear. Here, we examined the effects of intraperitoneal administrat...
- Summary (fallback): 机器翻译摘要显示：群体内的社会等级对于许多动物的生存至关重要。在社区中的排名有助于避免不必要的冲突并与他人建立稳定的关系。催产素因其在社会行为中的作用而受到越来越多的关注。然而，催产素受体信号传导与社会等级之间的因果关系仍不清楚。在这里，我们研究了腹膜内施用血脑屏障穿透性催产素受体拮抗剂 L-368-899 对雄性小鼠的（1）社会等级、（2）性别偏好、（3）社会偏好和（4）二元相互作用的影响。在试管测试中，催产素受体阻断对第一等级小鼠没有影响，但增加了第二等级小鼠的等级波动，表明催产素受体信号传导有助于中间社会等级的稳定性。
- Keywords: social, oxytocin, receptor, mice, preference

### 4. [动态乐观和悲观状态塑造猴子的冒险行为](https://www.biorxiv.org/content/10.64898/2026.05.01.722186v3)
- Original title: Dynamic optimism and pessimism states shape risk-taking behavior in monkeys
- Authors: Higashino, I., Ito, R., Okochi, Y., Inutsuka, K., Yokoyama, H. et al.
- Meta: 2026-07-07 | neuroscience | DOI: 10.64898/2026.05.01.722186
- 中文摘要: 人类和动物经常面临需要做出决策的危险情况。此类决策有时可能是高风险、高回报，有时可能是低风险、低回报，具体取决于乐观与悲观之间的平衡。然而，这种乐观-悲观主义偏见如何在不同背景下进行调节仍不清楚。在这里，我们引入了一种基于自由能原理的冒险任务决策计算模型，以及一个机器学习框架，该框架可以根据行为数据反向估计认知更新和乐观悲观偏差。将这个框架应用于猴子的行为数据，我们发现猴子可以快速准确地识别风险程度，同时在任务过程中频繁地在乐观和悲观之间切换。
- Abstract: Humans and animals often face risky situations that require decision-making. Such decisions can be high-risk, high-return at some times, and low-risk, low-return at other times, depending on the balance between optimism and pessimism. However, how this optimism-pessimism bias is regulated across contexts remains unclear. Here, we introduced a computational model of decision-making in a risk-taking task based on the...
- Summary (fallback): 机器翻译摘要显示：人类和动物经常面临需要做出决策的危险情况。此类决策有时可能是高风险、高回报，有时可能是低风险、低回报，具体取决于乐观与悲观之间的平衡。然而，这种乐观-悲观主义偏见如何在不同背景下进行调节仍不清楚。在这里，我们引入了一种基于自由能原理的冒险任务决策计算模型，以及一个机器学习框架，该框架可以根据行为数据反向估计认知更新和乐观悲观偏差。将这个框架应用于猴子的行为数据，我们发现猴子可以快速准确地识别风险程度，同时在任务过程中频繁地在乐观和悲观之间切换。
- Keywords: optimism, pessimism, decision-making, optimism-pessimism, bias

### 5. [衰老增强的成纤维细胞积累排除了脱髓鞘病变中的少突胶质细胞](https://www.biorxiv.org/content/10.1101/2025.07.27.667059v3)
- Original title: Aging-enhanced accumulation of fibroblasts excludes oligodendrocytes in demyelinated lesions
- Authors: Lozinski, B. M., Melchor, G. S., D'Mello, C., Gorter, R., Dong, Y. et al.
- Meta: 2026-07-07 | neuroscience | DOI: 10.1101/2025.07.27.667059
- 中文摘要: 成纤维细胞失调导致病理性纤维化和异常修复。新的证据表明，成纤维细胞在中枢神经系统损伤后的病变中积聚，但它们是否以及如何影响少突胶质细胞的修复反应（包括衰老过程）尚不确定。在这里，我们报道了溶血卵磷脂诱导脱髓鞘后，成纤维细胞在 6 至 10 周龄幼鼠的脊髓白质病变实质中积聚。这是首先通过免疫荧光显微镜观察到的，该显微镜采用了几种归因于成纤维细胞的标记物，包括血小板衍生生长因子β、1型胶原、α平滑肌肌动蛋白、骨膜蛋白和纤连蛋白；以及使用血小板衍生生长因子β； TdTomato 报告基因转基因小鼠。
- Abstract: Fibroblast dysregulation contributes to pathological fibrosis and aberrant repair. Emerging evidence suggest that fibroblasts accumulate in lesions following central nervous system injury, but whether and how they influence oligodendrocyte repair responses, including in aging, is uncertain. Here we report that fibroblasts accumulate in the parenchyma of spinal cord white matter lesions of 6 to 10 week old young mice...
- Summary (fallback): 机器翻译摘要显示：成纤维细胞失调导致病理性纤维化和异常修复。新的证据表明，成纤维细胞在中枢神经系统损伤后的病变中积聚，但它们是否以及如何影响少突胶质细胞的修复反应（包括衰老过程）尚不确定。在这里，我们报道了溶血卵磷脂诱导脱髓鞘后，成纤维细胞在 6 至 10 周龄幼鼠的脊髓白质病变实质中积聚。这是首先通过免疫荧光显微镜观察到的，该显微镜采用了几种归因于成纤维细胞的标记物，包括血小板衍生生长因子β、1型胶原、α平滑肌肌动蛋白、骨膜蛋白和纤连蛋白；以及使用血小板衍生生长因子β； TdTomato 报告基因转基因小鼠。
- Keywords: fibroblasts, lesions, lysolecithin, oligodendrocyte, fibroblast

### 6. [TDP-43 相变和细胞质聚集的细胞修饰剂](https://www.biorxiv.org/content/10.64898/2025.12.16.694670v3)
- Original title: Cellular modifiers of TDP-43 phase transition and cytoplasmic aggregation
- Authors: Chin, N., Zhang, Q., Zou, J., Cheng, K. C.-C., Zheng, W. et al.
- Meta: 2026-07-07 | cell biology | DOI: 10.64898/2025.12.16.694670
- 中文摘要: RNA 结合蛋白 TAR DNA 结合蛋白 43 (TDP-43) 可以形成液体样核组件，其相行为被认为影响其聚集倾向和神经毒性活性。控制 TDP-43 液-固相变的机制尚不清楚。在这里，我们结合化学和全基因组遗传筛选来鉴定调节 RNA 结合缺陷 TDP-43 突变体相行为的细胞因子。我们的筛选发现了多种细胞过程，包括 RNA 剪接、蛋白质翻译、蛋白质稳态失衡和作为 TDP-43 相调节剂的核输出。
- Abstract: RNA-binding protein TAR DNA-binding protein 43 (TDP-43) can form liquid-like, nuclear assemblies whose phase behavior is thought to influence its aggregation propensity and neurotoxic activity. The mechanism(s) that governs the liquid-to-solid phase transition of TDP-43 is poorly defined. Here we combined chemical and genome-wide genetic screenings to identify cellular factors that modulate the phase behavior of an...
- Summary (fallback): 机器翻译摘要显示：RNA 结合蛋白 TAR DNA 结合蛋白 43 (TDP-43) 可以形成液体样核组件，其相行为被认为影响其聚集倾向和神经毒性活性。控制 TDP-43 液-固相变的机制尚不清楚。在这里，我们结合化学和全基因组遗传筛选来鉴定调节 RNA 结合缺陷 TDP-43 突变体相行为的细胞因子。我们的筛选发现了多种细胞过程，包括 RNA 剪接、蛋白质翻译、蛋白质稳态失衡和作为 TDP-43 相调节剂的核输出。
- Keywords: tdp-43, phase, nuclear, cellular, transition

### 7. [FIND：用于识别 gnomAD 中人群丰富的致病变异的软件工具](https://www.biorxiv.org/content/10.64898/2026.06.05.730273v2)
- Original title: FIND: a software tool for identifying population-enriched pathogenic variants in gnomAD
- Authors: Horowitz, A. L., Liebman, A. Z., Liebman, S. W.
- Meta: 2026-07-07 | genomics | DOI: 10.64898/2026.06.05.730273
- 中文摘要: 创始人突变是在单一祖先中出现并通过瓶颈和内婚在后代群体中丰富的变体。致病性始祖突变的鉴定促进了有效的靶向筛查。更广泛地说，即使没有确认创始人身份，识别特定人群中丰富的致病变异也可以揭示特定人群的疾病负担。然而，许多此类变体仍然隐藏在现有数据集中的显而​​易见的地方。为了解决这一差距，我们开发了 FIND（隐藏在数据中的创始人候选者），这是一种网络工具，可识别 gnomAD 中的变体，其在一个祖先群体中频率 >0.00008，并且比所有其他群体至少高出十倍（在对少于 5 个观察到的等位基因的群体进行归零之后）。搜索仅限于致病性、可能致病性和预测的功能丧失变异。
- Abstract: Founder mutations are variants that arose in a single ancestor and became enriched in a descendant population through a bottleneck and endogamy. Identification of pathogenic founder mutations has facilitated efficient targeted screening. More broadly, even without confirmed founder status, identifying pathogenic variants that are enriched within specific populations reveals population-specific disease burden. Howeve...
- Summary (fallback): 机器翻译摘要显示：创始人突变是在单一祖先中出现并通过瓶颈和内婚在后代群体中丰富的变体。致病性始祖突变的鉴定促进了有效的靶向筛查。更广泛地说，即使没有确认创始人身份，识别特定人群中丰富的致病变异也可以揭示特定人群的疾病负担。然而，许多此类变体仍然隐藏在现有数据集中的显而​​易见的地方。为了解决这一差距，我们开发了 FIND（隐藏在数据中的创始人候选者），这是一种网络工具，可识别 gnomAD 中的变体，其在一个祖先群体中频率 >0.00008，并且比所有其他群体至少高出十倍（在对少于 5 个观察到的等位基因的群体进行归零之后）。搜索仅限于致病性、可能致病性和预测的功能丧失变异。
- Keywords: variants, founder, pathogenic, populations, find

### 8. [RdRp Thumb-1 Pocket 是广谱抗病毒药物开发的保守靶标](https://www.biorxiv.org/content/10.1101/2024.03.29.587401v6)
- Original title: The RdRp Thumb-1 Pocket is a Conserved Target for Broad-Spectrum Antiviral Development
- Authors: Woods, V., Umansky, T., Russell, S. M., Gallay, P., Smith, D. et al.
- Meta: 2026-07-07 | bioinformatics | DOI: 10.1101/2024.03.29.587401
- 中文摘要: 单链 RNA (ssRNA) 病毒会导致人类疾病，从轻度感冒到致命的流行病。广谱非核苷抗病毒药物被认为不可能开发，因为变构结合位点保守性差。 HCV 的 RNA 依赖性 RNA 聚合酶 (RdRp) 中鉴定的 Thumb-1 变构位点控制着聚合酶启动所需的 {Lambda}1 环中的重要构象变化。唯一批准的 Thumb-1 抑制剂贝拉布韦已被证明对多种非 HCV 病毒无效，包括脊髓灰质炎病毒、鼻病毒、冠状病毒、柯萨奇病毒、流感病毒和 HIV。尽管对接预测良好，但它随后未能抑制 SARS-CoV-2。 RdRp 上跨多个病毒家族的保守同源变构位点尚未报道。
- Abstract: Single-stranded RNA (ssRNA) viruses cause human diseases ranging from mild colds to deadly pandemics. Broad-spectrum non-nucleoside antivirals have been characterized as impossible to develop because allosteric binding sites are poorly conserved. The Thumb-1 allosteric site identified in HCV's RNA-dependent RNA polymerase (RdRp) governs an essential conformational change in the {Lambda}1-loop required for polymerase...
- Summary (fallback): 机器翻译摘要显示：单链 RNA (ssRNA) 病毒会导致人类疾病，从轻度感冒到致命的流行病。广谱非核苷抗病毒药物被认为不可能开发，因为变构结合位点保守性差。 HCV 的 RNA 依赖性 RNA 聚合酶 (RdRp) 中鉴定的 Thumb-1 变构位点控制着聚合酶启动所需的 {Lambda}1 环中的重要构象变化。唯一批准的 Thumb-1 抑制剂贝拉布韦已被证明对多种非 HCV 病毒无效，包括脊髓灰质炎病毒、鼻病毒、冠状病毒、柯萨奇病毒、流感病毒和 HIV。尽管对接预测良好，但它随后未能抑制 SARS-CoV-2。 RdRp 上跨多个病毒家族的保守同源变构位点尚未报道。
- Keywords: thumb-1, conserved, rdrp, broad-spectrum, allosteric

### 9. [PHI：基于 Galaxy 的工作流程，用于可重复的原噬菌体-宿主相互作用分析和标准化病毒基因组报告](https://www.biorxiv.org/content/10.64898/2025.12.02.691814v2)
- Original title: PHI: A Galaxy-based workflow for reproducible prophage-host interaction analysis and standardized viral-genomics reporting
- Authors: Saraiva, J. P., Borim Correa, F., Bernt, M., Ghanem, N., Nieto, E. et al.
- Meta: 2026-07-07 | bioinformatics | DOI: 10.64898/2025.12.02.691814
- 中文摘要: 背景：感染细菌的病毒，称为噬菌体或噬菌体，在自然界中广泛存在，在塑造微生物群落和生态系统功能方面发挥着重要作用。一些噬菌体可以作为“原噬菌体”整合到细菌基因组中，它们可以通过携带影响新陈代谢、毒力或环境适应的基因来影响宿主的生物学。尽管它们很重要，但研究原噬菌体及其与细菌宿主的相互作用仍然具有挑战性，因为它通常需要结合许多复杂的计算工具并且可能是资源密集型的。结果：在这项研究中，我们介绍了 Prophage-Host Interaction Toolkit (PHI)，这是一种通过 Galaxy 平台提供的用户友好且自动化的工作流程。
- Abstract: Background: Viruses that infect bacteria, known as bacteriophages or phages, are widespread in nature and play important roles in shaping microbial communities and ecosystem functions. Some phages can integrate into bacterial genomes as "prophages", where they may influence the biology of their host by carrying genes that affect metabolism, virulence, or environmental adaptation. Despite their importance, studying p...
- Summary (fallback): 机器翻译摘要显示：背景：感染细菌的病毒，称为噬菌体或噬菌体，在自然界中广泛存在，在塑造微生物群落和生态系统功能方面发挥着重要作用。一些噬菌体可以作为“原噬菌体”整合到细菌基因组中，它们可以通过携带影响新陈代谢、毒力或环境适应的基因来影响宿主的生物学。尽管它们很重要，但研究原噬菌体及其与细菌宿主的相互作用仍然具有挑战性，因为它通常需要结合许多复杂的计算工具并且可能是资源密集型的。结果：在这项研究中，我们介绍了 Prophage-Host Interaction Toolkit (PHI)，这是一种通过 Galaxy 平台提供的用户友好且自动化的工作流程。
- Keywords: prophages, workflow, genomes, host, tools

### 10. [患者来源的类器官在功能上将上皮性卵巢癌分层为临床相关的化疗反应表型](https://www.biorxiv.org/content/10.64898/2026.06.10.731260v3)
- Original title: Patient-Derived Organoids Functionally Stratify Epithelial Ovarian Cancer into Clinically Relevant Chemotherapy Response Phenotypes
- Authors: Ragothaman, S., Reddy, R., Sajan, S. C., John, L. A., Biju, V. et al.
- Meta: 2026-07-07 | cancer biology | DOI: 10.64898/2026.06.10.731260
- 中文摘要: 背景：卵巢癌（OC）对铂类化疗的反应表现出显着的异质性，导致临床结果变化和频繁复发。目前的生物标志物，包括血清 CA-125 动力学和 BRCA 突变状态，不能完全预测治疗反应。我们研究了患者来源的类器官（PDO）是否可以在功能上对化疗敏感性进行分层并更好地反映患者特异性的临床行为。方法：纳入2024年1月至2026年5月期间治疗的20例OC患者，成功建立14个PDO系。八个具有强大低通道扩增和全面纵向随访的 PDO 接受了针对卡铂、紫杉醇、奥拉帕尼和阿霉素的功能分析。
- Abstract: Background: Ovarian cancer (OC) exhibits substantial heterogeneity in response to platinum-based chemotherapy, resulting in variable clinical outcomes and frequent recurrence. Current biomarkers, including serum CA-125 kinetics and BRCA mutational status, incompletely predict therapeutic response. We investigated whether patient-derived organoids (PDOs) could functionally stratify chemotherapy sensitivity and better...
- Summary (fallback): 机器翻译摘要显示：背景：卵巢癌（OC）对铂类化疗的反应表现出显着的异质性，导致临床结果变化和频繁复发。目前的生物标志物，包括血清 CA-125 动力学和 BRCA 突变状态，不能完全预测治疗反应。我们研究了患者来源的类器官（PDO）是否可以在功能上对化疗敏感性进行分层并更好地反映患者特异性的临床行为。方法：纳入2024年1月至2026年5月期间治疗的20例OC患者，成功建立14个PDO系。八个具有强大低通道扩增和全面纵向随访的 PDO 接受了针对卡铂、紫杉醇、奥拉帕尼和阿霉素的功能分析。
- Keywords: response, ca-125, functional, clinical, therapeutic

### 11. [番茄 MIK2 进化枝受体参与镰刀菌衍生诱导子的感知](https://www.biorxiv.org/content/10.1101/2025.05.22.655486v2)
- Original title: A tomato MIK2-clade receptor is involved in the perception of a Fusarium-derived elicitor
- Authors: Maroschek, J., Roesgen, Y., Roessner, C., Snoeck, S., Schwechheimer, C. et al.
- Meta: 2026-07-07 | plant biology | DOI: 10.1101/2025.05.22.655486
- 中文摘要: - 植物不断监测其环境，以适应影响健康和健身的威胁。细胞表面受体检测保守的微生物相关分子模式 (MAMP) 或内源性免疫原性信号，以激活诱导广谱抗病性的信号通路，称为模式触发免疫 (PTI)。 - 在拟南芥中，富含亮氨酸的重复受体激酶 MIK2 作为一种多功能受体出现，参与感知内源性 SCOOP 肽以及源自镰刀菌和相关真菌的潜在 MAMP。虽然 SCOOP 感知似乎仅限于芸苔目，但镰刀菌衍生的激发子会触发不同植物谱系的 PTI 反应。 - 在这里，我们证明镰刀菌激发子响应性和 MIK2 进化枝蛋白在种子植物中是保守的。
- Abstract: - Plants continuously monitor their environment to adapt to threats affecting health and fitness. Cell-surface receptors detect conserved microbe-associated molecular patterns (MAMPs) or endogenous immunogenic signals to activate signaling pathways that induce broad-spectrum disease resistance, known as pattern-triggered immunity (PTI). - In Arabidopsis thaliana, the leucine-rich repeat receptor kinase MIK2 emerged...
- Summary (fallback): 机器翻译摘要显示：- 植物不断监测其环境，以适应影响健康和健身的威胁。细胞表面受体检测保守的微生物相关分子模式 (MAMP) 或内源性免疫原性信号，以激活诱导广谱抗病性的信号通路，称为模式触发免疫 (PTI)。 - 在拟南芥中，富含亮氨酸的重复受体激酶 MIK2 作为一种多功能受体出现，参与感知内源性 SCOOP 肽以及源自镰刀菌和相关真菌的潜在 MAMP。虽然 SCOOP 感知似乎仅限于芸苔目，但镰刀菌衍生的激发子会触发不同植物谱系的 PTI 反应。 - 在这里，我们证明镰刀菌激发子响应性和 MIK2 进化枝蛋白在种子植物中是保守的。
- Keywords: mik2-clade, receptor, tomato, elicitor, fusarium

### 12. [明显的视觉注意力调节额叶皮层中与决策相关的信号](https://www.biorxiv.org/content/10.1101/2024.10.25.620227v3)
- Original title: Overt visual attention modulates decision-related signals in the frontal cortex
- Authors: Shevlin, B. R. K., Gwinn, R. E., Makwana, A., Krajbich, I.
- Meta: 2026-07-07 | neuroscience | DOI: 10.1101/2024.10.25.620227
- 中文摘要: 当表明两个选项之间的偏好时，决策者被认为是在注意力引导的过程中比较和积累证据。人们对这一过程的神经基础或视觉注意力如何影响积累的证据的表征知之甚少。我们同时进行了眼球追踪和功能磁共振成像实验，在实验中，人类受试者逐渐了解了两张食物彩票的价值。通过这种设计，我们能够在较长的时间过程中扩展决策，操纵证据的时间开始，从而分离采样和积累的证据。
- Abstract: When indicating a preference between two options, decision makers are thought to compare and accumulate evidence in an attention-guided process. Little is known about this process's neural substrates or how visual attention affects the representations of accumulated evidence. We conducted a simultaneous eye-tracking and fMRI experiment in which human subjects gradually learned about the value of two food-lotteries....
- Summary (fallback): 机器翻译摘要显示：当表明两个选项之间的偏好时，决策者被认为是在注意力引导的过程中比较和积累证据。人们对这一过程的神经基础或视觉注意力如何影响积累的证据的表征知之甚少。我们同时进行了眼球追踪和功能磁共振成像实验，在实验中，人类受试者逐渐了解了两张食物彩票的价值。通过这种设计，我们能够在较长的时间过程中扩展决策，操纵证据的时间开始，从而分离采样和积累的证据。
- Keywords: evidence, accumulated, visual, attention, signals

### 13. [水温升高对代间和跨代可塑性的影响揭示了水生植物物种的短期代谢和表型记忆](https://www.biorxiv.org/content/10.64898/2026.07.06.736556v1)
- Original title: Effects of an increase in water temperature on inter- and transgenerational plasticity reveal a short-term metabolic and phenotypic memory in an aquatic plant species
- Authors: Loupit, G., Sancharme, M., Petriacq, P., Valls Fonayet, J., Bittebiere, A.-K.
- Meta: 2026-07-07 | plant biology | DOI: 10.64898/2026.07.06.736556
- 中文摘要: 跨代可塑性可以塑造植物表型，并影响植物对与当前条件相互作用的环境变化的反应。虽然过去的胁迫如何与当前的最佳或胁迫条件相互作用在单个植物中被越来越多地记录，但跨代可塑性仍然知之甚少，尤其是在代谢组水平上。在我们的研究中，我们研究了热应激是否会诱导亚南极水生植物澳大利亚利莫氏菌（Limosella australis）连续两个克隆分株世代的跨代代谢和表型修饰。我们进行了非靶向代谢组学方法并测量了形态和性能特征，以评估代谢组和表型的跨代可塑性。
- Abstract: Transgenerational plasticity can shape plant phenotype and influence plant response to environmental changes in interaction with the current conditions. While how past stress interact with either current optimal or stress conditions is increasingly documented within a single plant, transgenerational plasticity remains particularly poorly understood especially at the metabolome level. In our study, we investigated wh...
- Summary (fallback): 机器翻译摘要显示：跨代可塑性可以塑造植物表型，并影响植物对与当前条件相互作用的环境变化的反应。虽然过去的胁迫如何与当前的最佳或胁迫条件相互作用在单个植物中被越来越多地记录，但跨代可塑性仍然知之甚少，尤其是在代谢组水平上。在我们的研究中，我们研究了热应激是否会诱导亚南极水生植物澳大利亚利莫氏菌（Limosella australis）连续两个克隆分株世代的跨代代谢和表型修饰。我们进行了非靶向代谢组学方法并测量了形态和性能特征，以评估代谢组和表型的跨代可塑性。
- Keywords: plant, stress, transgenerational, metabolic, heat

### 14. [比较代谢组学分析揭示了水稻渗入系的盐度耐受机制](https://www.biorxiv.org/content/10.64898/2026.07.06.736799v1)
- Original title: Comparative Metabolomic Profiling Reveals Salinity Tolerance Mechanisms in a Rice Introgression Line
- Authors: Chaudhary, C., Guttula, P., Agrawal, K., Subudhi, P. K., Gartia, M. R.
- Meta: 2026-07-07 | plant biology | DOI: 10.64898/2026.07.06.736799
- 中文摘要: 水稻（Oryza sativa）对盐度高度敏感，但耐盐性背后的代谢机制仍不完全清楚。在这项研究中，我们对耐盐渗入系 JN100 (JN)、其供体亲本 Nona Bokra (NB) 及其轮回亲本 Jupiter (JU) 进行了叶组织特异性非靶向代谢组学分析，以表征对盐胁迫的代谢反应。比较分析确定了跨越不同化学类别的差异累积代谢物 (DAM)，包括氨基酸、糖和碳水化合物、脂质、有机酸、辅因子、电子载体和核苷酸。在盐胁迫 (SS) 下，相对于 JU，JN 中检测到 201 个 DAM（89 个上调，112 个下调）。
- Abstract: Rice (Oryza sativa) is highly sensitive to salinity, yet the metabolic mechanisms underlying salt tolerance remains incompletely understood. In this study, we performed leaf tissue-specific untargeted metabolomic profiling of the salt-tolerant introgression line JN100 (JN), its donor parent Nona Bokra (NB), and its recurrent parent Jupiter (JU) to characterize metabolic responses to salt stress. Comparative analysis...
- Summary (fallback): 机器翻译摘要显示：水稻（Oryza sativa）对盐度高度敏感，但耐盐性背后的代谢机制仍不完全清楚。在这项研究中，我们对耐盐渗入系 JN100 (JN)、其供体亲本 Nona Bokra (NB) 及其轮回亲本 Jupiter (JU) 进行了叶组织特异性非靶向代谢组学分析，以表征对盐胁迫的代谢反应。比较分析确定了跨越不同化学类别的差异累积代谢物 (DAM)，包括氨基酸、糖和碳水化合物、脂质、有机酸、辅因子、电子载体和核苷酸。在盐胁迫 (SS) 下，相对于 JU，JN 中检测到 201 个 DAM（89 个上调，112 个下调）。
- Keywords: stress, salinity, metabolic, metabolomic, tolerance

### 15. [代谢组学特征支持使用广义线性模型对腹膜子宫内膜异位症的诊断。](https://www.biorxiv.org/content/10.64898/2026.07.05.736551v2)
- Original title: Metabolomic signatures support the diagnostics of peritoneal endometriosis using generalised linear models.
- Authors: Cecil, A., Vouk, K., Novak Pusic, M., Vogler, A., Wenzl, R. et al.
- Meta: 2026-07-07 | systems biology | DOI: 10.64898/2026.07.05.736551
- 中文摘要: 子宫内膜异位症是一种常见的炎症性妇科疾病，影响全世界多达 10% 的女性，其特征是子宫外存在子宫内膜样组织。目前的诊断方法，例如超声和 MRI，可以有效检测卵巢和深部子宫内膜异位症，但无法检测更常见的腹膜类型。目前诊断腹膜子宫内膜异位症需要侵入性腹腔镜检查和组织学确认。尽管付出了很多努力，但还没有新的可靠生物标志物成功转化为常规临床应用。本研究旨在研究利用靶向代谢组学来发现能够识别血浆样本中子宫内膜异位症的代谢物比率。我们分析了 235 名患者的发现人群和 278 名患者的验证人群。两个人群中的所有病例和对照均通过腹腔镜检查诊断。
- Abstract: Endometriosis, a common inflammatory gynecological disorder affecting up to 10% of women worldwide, is characterized by the presence of endometrium-like tissue outside the uterus. Current diagnostic methods, such as ultrasound and MRI, effectively detect ovarian and deep endometriosis but fail to detect more common peritoneal type. Diagnosing peritoneal endometriosis currently necessitates invasive laparoscopy and h...
- Summary (fallback): 机器翻译摘要显示：子宫内膜异位症是一种常见的炎症性妇科疾病，影响全世界多达 10% 的女性，其特征是子宫外存在子宫内膜样组织。目前的诊断方法，例如超声和 MRI，可以有效检测卵巢和深部子宫内膜异位症，但无法检测更常见的腹膜类型。目前诊断腹膜子宫内膜异位症需要侵入性腹腔镜检查和组织学确认。尽管付出了很多努力，但还没有新的可靠生物标志物成功转化为常规临床应用。本研究旨在研究利用靶向代谢组学来发现能够识别血浆样本中子宫内膜异位症的代谢物比率。我们分析了 235 名患者的发现人群和 278 名患者的验证人群。两个人群中的所有病例和对照均通过腹腔镜检查诊断。
- Keywords: endometriosis, peritoneal, ratios, diagnostics, linear

### 16. [雄性和雌性铃木果蝇在离散的阳光刺激下保持长时间、稳定的飞行方向。](https://www.biorxiv.org/content/10.64898/2026.07.06.736788v1)
- Original title: Male and female Drosophila suzukii maintain extended, stable flight headings to a discrete sun stimulus.
- Authors: Horikawa, K., Savkin, K., Rower, L., Hodge, L., Warren, T. L.
- Meta: 2026-07-07 | zoology | DOI: 10.64898/2026.07.06.736788
- 中文摘要: 昆虫的长距离移动对农业、人类健康和生物多样性具有至关重要的影响。尽管长期以来人们一直认为只有大型专业昆虫才有支持长距离扩散的导航能力，但最近的研究表明，较小的昆虫，例如微小的果蝇果蝇，可以在飞行或行走时保持延伸、笔直的路径。这就提出了一个问题：其他果蝇物种是否具有支持长期扩散的导航能力。解决这个问题对于铃木果蝇（斑翅果蝇）来说尤其重要，铃木果蝇是一种强效害虫，对全世界成熟的水果和浆果造成巨大损害。斑翅果蝇被认为缺乏长距离扩散的能力，因为之前的研究估计每日最大扩散距离小于 90 m。
- Abstract: Long-distance movement in insects has crucial impacts on agriculture, human health, and biodiversity. Although it was long assumed that only large, specialist insects had the navigation capacity to support long-distance dispersal, recent studies have demonstrated that smaller insects, such as the tiny fruit fly Drosophila melanogaster, can maintain extended, straight paths while flying or walking. This raises the qu...
- Summary (fallback): 机器翻译摘要显示：昆虫的长距离移动对农业、人类健康和生物多样性具有至关重要的影响。尽管长期以来人们一直认为只有大型专业昆虫才有支持长距离扩散的导航能力，但最近的研究表明，较小的昆虫，例如微小的果蝇果蝇，可以在飞行或行走时保持延伸、笔直的路径。这就提出了一个问题：其他果蝇物种是否具有支持长期扩散的导航能力。解决这个问题对于铃木果蝇（斑翅果蝇）来说尤其重要，铃木果蝇是一种强效害虫，对全世界成熟的水果和浆果造成巨大损害。斑翅果蝇被认为缺乏长距离扩散的能力，因为之前的研究估计每日最大扩散距离小于 90 m。
- Keywords: drosophila, capacity, suzukii, dispersal, maintain

### 17. [语境单词学习过程中的纹状体活动受到儿童阅读能力的影响](https://www.biorxiv.org/content/10.64898/2026.07.06.736136v1)
- Original title: Striatal activity during contextual word learning is influenced by children's reading ability
- Authors: Bahar, N., Arabadzhiyska, D., Jones, H., Singh, S., Davis, M. et al.
- Meta: 2026-07-07 | neuroscience | DOI: 10.64898/2026.07.06.736136
- 中文摘要: 语境单词学习是儿童时期词汇习得的基本机制。对于成年人来说，从上下文中成功推断单词含义本质上是有益的，并且与奖励相关大脑区域的更大享受和更活跃有关。类似的奖励机制是否支持儿童的单词学习，以及它们是否因能力而异，仍然未知。我们使用功能磁共振成像 (fMRI) 来检查 25 名具有典型阅读技能的 11-13 岁儿童和 20 名年龄匹配的患有阅读障碍的儿童在上下文单词学习过程中的神经反应。当成功学习新单词的含义时，神经典型读者表现出核心奖励处理区域（包括腹侧纹状体）的激活增强。
- Abstract: Contextual word learning is a fundamental mechanism for vocabulary acquisition during childhood. In adults, successful inference of word meaning from context is intrinsically rewarding, and is associated with greater enjoyment and greater activity in reward-related brain regions. Whether similar reward mechanisms support word learning in children, and whether they differ as a function of ability, remains unknown. We...
- Summary (fallback): 机器翻译摘要显示：语境单词学习是儿童时期词汇习得的基本机制。对于成年人来说，从上下文中成功推断单词含义本质上是有益的，并且与奖励相关大脑区域的更大享受和更活跃有关。类似的奖励机制是否支持儿童的单词学习，以及它们是否因能力而异，仍然未知。我们使用功能磁共振成像 (fMRI) 来检查 25 名具有典型阅读技能的 11-13 岁儿童和 20 名年龄匹配的患有阅读障碍的儿童在上下文单词学习过程中的神经反应。当成功学习新单词的含义时，神经典型读者表现出核心奖励处理区域（包括腹侧纹状体）的激活增强。
- Keywords: learning, word, during, children, reading

### 18. [海马印迹配置前额叶上下文表征来指导灵活的决策](https://www.biorxiv.org/content/10.64898/2026.07.06.732916v1)
- Original title: Hippocampal engrams configure prefrontal context representations to guide flexible decisions
- Authors: Julian, J. B., Kaminsky, J. C., Tank, D. W., Brody, C.
- Meta: 2026-07-07 | neuroscience | DOI: 10.64898/2026.07.06.732916
- 中文摘要: 灵活的行为需要使用过去的经验来配置皮质计算以满足当前的任务需求。神经科学的一个中心问题是记忆表征如何控制这种重新配置。尽管海马（HPC）印迹可以驱动学习行为，但先前的研究很大程度上仅限于固定的刺激反应计算。因此，印迹是否可以驱动一组刺激-反应映射的检索，而不是特定反应本身，仍然悬而未决。此外，印迹如何影响皮质任务表征和动态从而产生印迹一致的行为仍有待研究。在这里，我们通过在小鼠上下文依赖的任务切换范例中将 HPC 印迹的标记和重新激活与内侧前额叶皮层 (mPFC) 的同步大规模记录相结合来解决这两个问题。
- Abstract: Flexible behavior requires using past experiences to configure cortical computations to suit current task demands. A central question in neuroscience is how memory representations control such reconfigurations. Although hippocampal (HPC) engrams can drive learned behaviors, prior studies have been largely limited to a fixed stimulus-response computation. Thus, whether engrams can drive retrieval of a set of stimulus...
- Summary (fallback): 机器翻译摘要显示：灵活的行为需要使用过去的经验来配置皮质计算以满足当前的任务需求。神经科学的一个中心问题是记忆表征如何控制这种重新配置。尽管海马（HPC）印迹可以驱动学习行为，但先前的研究很大程度上仅限于固定的刺激反应计算。因此，印迹是否可以驱动一组刺激-反应映射的检索，而不是特定反应本身，仍然悬而未决。此外，印迹如何影响皮质任务表征和动态从而产生印迹一致的行为仍有待研究。在这里，我们通过在小鼠上下文依赖的任务切换范例中将 HPC 印迹的标记和重新激活与内侧前额叶皮层 (mPFC) 的同步大规模记录相结合来解决这两个问题。
- Keywords: engrams, behavior, mpfc, configure, context

### 19. [在视野范围内有意识和无意识的目光接触](https://www.biorxiv.org/content/10.64898/2026.07.06.736643v1)
- Original title: Conscious and unconscious eye contact at the limits of vision
- Authors: Lanfranco, R. C., Guterstam, A., Cleeremans, A.
- Meta: 2026-07-07 | neuroscience | DOI: 10.64898/2026.07.06.736643
- 中文摘要: 眼神接触是最有效的社交信号之一，但目前尚不清楚多少视觉输入足以记录直接凝视，以及这种记录是否需要有意识的意识。在这里，我们使用定制的测速仪来呈现仅 1-5 毫秒的脸部，询问注视方向是否可以在视觉极限下塑造感知。与回避目光的面部相比，直视面部需要更少的视觉输入来定位，并且从 3 毫秒开始产生更高的定位灵敏度。至关重要的是，这种优势在参与者能够明确地对注视方向进行分类之前就出现了，并且在感知意识评级显示对驱动本地化的信息的元认知访问之前，这两者都只在 4-5 毫秒时出现。
- Abstract: Eye contact is one of the most potent social signals, but it remains unclear how little visual input is sufficient to register direct gaze, and whether such registration requires conscious awareness. Here, we used a custom tachistoscope to present faces for only 1-5 ms, asking whether gaze direction can shape perception at the very limits of vision. Direct-gaze faces required less visual input to localise than avert...
- Summary (fallback): 机器翻译摘要显示：眼神接触是最有效的社交信号之一，但目前尚不清楚多少视觉输入足以记录直接凝视，以及这种记录是否需要有意识的意识。在这里，我们使用定制的测速仪来呈现仅 1-5 毫秒的脸部，询问注视方向是否可以在视觉极限下塑造感知。与回避目光的面部相比，直视面部需要更少的视觉输入来定位，并且从 3 毫秒开始产生更高的定位灵敏度。至关重要的是，这种优势在参与者能够明确地对注视方向进行分类之前就出现了，并且在感知意识评级显示对驱动本地化的信息的元认知访问之前，这两者都只在 4-5 毫秒时出现。
- Keywords: gaze, visual, localisation, conscious, contact

### 20. [内在终止子的系统工程和机器学习分析揭示了终止子发夹直接上游的关键核苷酸。](https://www.biorxiv.org/content/10.64898/2026.07.06.736697v1)
- Original title: Systematic engineering and machine learning analysis of intrinsic terminators reveal crucial nucleotides directly upstream of the terminator hairpin.
- Authors: Koster, C. C., Terlouw, B., Nieuwkoop, T., Creutzburg, S. C. A., Martin-Pascual, M. et al.
- Meta: 2026-07-07 | molecular biology | DOI: 10.64898/2026.07.06.736697
- 中文摘要: 转录终止效率被认为是微调细菌基因表达的重要参数。尽管如此，决定转录终止效率的设计原理仍然知之甚少。在本研究中，我们旨在研究 3' 非翻译区 (3'UTR) 对大肠杆菌和其他细菌基因表达的影响。首先，生成 3'UTR 变体序列，在终止密码子和内在终止子之间插入随机的 30 bp 序列，由富含 GC 的发夹和下游聚 (U) 尾组成。使用三个报告基因，发现不同的 3'UTR 序列导致蛋白质产量差异高达五倍，与上游编码序列无关。当腺苷直接存在于终止子发夹上游时，可获得最高的蛋白质产量。
- Abstract: Transcriptional termination efficiency is considered an important parameter for fine tuning bacterial gene expression. Still, the design principles that determine transcription termination efficiency remain poorly understood. In this study, we aimed to investigate the impact of the 3' untranslated region (3'UTR) on gene expression in Escherichia coli and other bacteria. First, 3'UTR variant sequences were generated,...
- Summary (fallback): 机器翻译摘要显示：转录终止效率被认为是微调细菌基因表达的重要参数。尽管如此，决定转录终止效率的设计原理仍然知之甚少。在本研究中，我们旨在研究 3' 非翻译区 (3'UTR) 对大肠杆菌和其他细菌基因表达的影响。首先，生成 3'UTR 变体序列，在终止密码子和内在终止子之间插入随机的 30 bp 序列，由富含 GC 的发夹和下游聚 (U) 尾组成。使用三个报告基因，发现不同的 3'UTR 序列导致蛋白质产量差异高达五倍，与上游编码序列无关。当腺苷直接存在于终止子发夹上游时，可获得最高的蛋白质产量。
- Keywords: terminator, upstream, hairpin, sequences, protein

### 21. [大肠杆菌 MscL 的结构及其在纳米圆盘中的二聚体形成](https://www.biorxiv.org/content/10.64898/2026.07.06.736777v1)
- Original title: The Structure of Escherichia coli MscL and its dimer formation in Nanodiscs
- Authors: Rasmussen, T., Bahner, J. I., Flegler, V. J., Hove, T. T., Kraft, C. et al.
- Meta: 2026-07-07 | molecular biology | DOI: 10.64898/2026.07.06.736777
- 中文摘要: 大电导机械敏感通道 (MscL) 是重要的细菌安全阀，可通过响应膜张力释放溶质来防止渗透裂解。尽管对大肠杆菌 MscL (EcMscL) 进行了广泛的功能研究，但其高分辨率结构仍然未知。使用冷冻电子显微镜，我们展示了在纳米圆盘中以 3.1 [A] 分辨率重建的 EcMscL 实验结构。该结构揭示了一个五聚体组装体，在胞质侧有一个狭窄的疏水门和一个周质空腔，与典型的 MscL 折叠一致。与早期发表的来自其他生物体的 MscL 晶体结构的差异在于不太保守的周质环。我们观察到先前未报道的 EcMscL 五聚体的二聚体关联，由周质环中的残基 61-63 介导。
- Abstract: Mechanosensitive channels of large conductance (MscL) are essential bacterial safety valves that prevent osmotic lysis by releasing solutes in response to membrane tension. Despite extensive functional studies on Escherichia coli MscL (EcMscL), its high-resolution structure remained unknown. Using cryo-electron microscopy, we present an experimental structure of EcMscL reconstituted in nanodiscs at 3.1 [A] resolutio...
- Summary (fallback): 机器翻译摘要显示：大电导机械敏感通道 (MscL) 是重要的细菌安全阀，可通过响应膜张力释放溶质来防止渗透裂解。尽管对大肠杆菌 MscL (EcMscL) 进行了广泛的功能研究，但其高分辨率结构仍然未知。使用冷冻电子显微镜，我们展示了在纳米圆盘中以 3.1 [A] 分辨率重建的 EcMscL 实验结构。该结构揭示了一个五聚体组装体，在胞质侧有一个狭窄的疏水门和一个周质空腔，与典型的 MscL 折叠一致。与早期发表的来自其他生物体的 MscL 晶体结构的差异在于不太保守的周质环。我们观察到先前未报道的 EcMscL 五聚体的二聚体关联，由周质环中的残基 61-63 介导。
- Keywords: structure, mscl, ecmscl, periplasmic, escherichia

### 22. [M-MLV 逆转录酶的饱和诱变筛选可识别增强引物编辑效率的变体](https://www.biorxiv.org/content/10.64898/2026.07.06.736660v1)
- Original title: Saturated mutagenesis screen of M-MLV reverse transcriptase identifies variants enhancing prime editing efficiency
- Authors: Li, H., Wang, Y., Zhang, C., Tun, T. T., Yu, S. et al.
- Meta: 2026-07-07 | molecular biology | DOI: 10.64898/2026.07.06.736660
- 中文摘要: Prime编辑能够对基因组进行精确修饰，从而在治疗遗传疾病方面具有巨大潜力。尽管主要编辑技术取得了实质性进展，并且启动了第一个治疗慢性肉芽肿性疾病的临床试验，但仍然迫切需要进一步提高跨编辑类型的编辑效率。在这里，我们通过删除 MMLV 逆转录酶 (MMLV-RT) 的 RNase H 结构域开发了一个紧凑的 Prime 编辑器 PE2{Delta}R。然后，我们针对 PE2{Delta}R-RT Fingers 结构域内的两个 DNA 相互作用区域进行了饱和诱变筛选。通过将三个高效突变（I61R、V101R、S67W）整合到缺乏 RNase H 结构域的 PEmax（称为 PEmax{Delta}RM3）中，与 PEmax 相比，我们实现了跨编辑类型的编辑效率高达 90% 的提高。
- Abstract: Prime editing enables the precise modification of genomes, thereby holding great potential for the treatment of genetic diseases. Despite substantial advancements in prime editing technology and the initiation of the first clinical trial for treating chronic granulomatous disease, further enhancement of editing efficiency across edit types is still urgently needed. Here, we developed a compact prime editor, PE2{Delt...
- Summary (fallback): 机器翻译摘要显示：Prime编辑能够对基因组进行精确修饰，从而在治疗遗传疾病方面具有巨大潜力。尽管主要编辑技术取得了实质性进展，并且启动了第一个治疗慢性肉芽肿性疾病的临床试验，但仍然迫切需要进一步提高跨编辑类型的编辑效率。在这里，我们通过删除 MMLV 逆转录酶 (MMLV-RT) 的 RNase H 结构域开发了一个紧凑的 Prime 编辑器 PE2{Delta}R。然后，我们针对 PE2{Delta}R-RT Fingers 结构域内的两个 DNA 相互作用区域进行了饱和诱变筛选。通过将三个高效突变（I61R、V101R、S67W）整合到缺乏 RNase H 结构域的 PEmax（称为 PEmax{Delta}RM3）中，与 PEmax 相比，我们实现了跨编辑类型的编辑效率高达 90% 的提高。
- Keywords: editing, prime, efficiency, pemax, mutagenesis

### 23. [SYT1 相互作用组学和双定位蛋白质组学的整合将 ER-PM 接触与木质素沉积联系起来](https://www.biorxiv.org/content/10.64898/2026.07.06.736826v1)
- Original title: Integration of SYT1 Interactomics and Dual-Localization Proteomics Links ER-PM Contacts to Lignin Deposition
- Authors: Morello-Lopez, J., Galvan, U., Benitez-Fuente, F., Markovic, V., Parsons, H. T. et al.
- Meta: 2026-07-07 | molecular biology | DOI: 10.64898/2026.07.06.736826
- 中文摘要: 膜接触位点 (MCS) 是进化上保守的细胞内纳米结构域，可物理桥接相对的脂质双层，以促进非囊泡通讯并维持细胞稳态。在植物中，内质网-质膜 (ER-PM) 接触位点在环境适应中发挥着重要作用，并且由充当系链的特殊蛋白质组成，例如突触结合蛋白 1 (SYT1)。然而，仍然需要对这些连接处控制过程的分子机制有一个全面的了解。在这项工作中，我们整合了亲和纯化质谱、TurboID 邻近标记和 HyperLOPIT 空间蛋白质组学的双定位再分析，以功能性地绘制 ER-PM 接触位点蛋白质 SYT1 的蛋白质相互作用图谱。
- Abstract: Membrane contact sites (MCSs) are evolutionarily conserved intracellular nanodomains that physically bridge opposing lipid bilayers to facilitate non-vesicular communication and maintain cellular homeostasis. In plants, endoplasmic reticulum-plasma membrane (ER-PM) contact sites play fundamental roles in environmental adaptation, and are populated by specialized proteins which act as tethers such as Synaptotagmin 1...
- Summary (fallback): 机器翻译摘要显示：膜接触位点 (MCS) 是进化上保守的细胞内纳米结构域，可物理桥接相对的脂质双层，以促进非囊泡通讯并维持细胞稳态。在植物中，内质网-质膜 (ER-PM) 接触位点在环境适应中发挥着重要作用，并且由充当系链的特殊蛋白质组成，例如突触结合蛋白 1 (SYT1)。然而，仍然需要对这些连接处控制过程的分子机制有一个全面的了解。在这项工作中，我们整合了亲和纯化质谱、TurboID 邻近标记和 HyperLOPIT 空间蛋白质组学的双定位再分析，以功能性地绘制 ER-PM 接触位点蛋白质 SYT1 的蛋白质相互作用图谱。
- Keywords: er-pm, contact, sites, syt1, membrane

### 24. [非裂解膜透化程序可驱动体内上皮细胞更新](https://www.biorxiv.org/content/10.64898/2026.07.06.736761v1)
- Original title: A non-lytic membrane permeabilization program drives epithelial cell turnover in vivo
- Authors: Morikawa, M., Yoo, S. K.
- Meta: 2026-07-07 | cell biology | DOI: 10.64898/2026.07.06.736761
- 中文摘要: 上皮细胞更新的核心困境是消除和替换细胞，同时保留组织结构和屏障功能。传统上，凋亡或非凋亡细胞的排出与肠上皮更新有关。在这里，我们确定了一种非裂解膜透化程序，可驱动体内生理性肠上皮细胞更新。在果蝇肠道中，肠上皮细胞经历细胞死亡，这是一种非凋亡形式的细胞死亡，其特征是细胞质蛋白的消耗。我们发现这个过程是由估计直径为 16-50 nm 的瞬时质膜孔介导的，允许细胞外蛋白质流入和细胞质内容物的损失。成孔蛋白 Ninjurin A (NijA) 在 erebosis 过程中积累为点，对于驱动这一过程是必要且充分的。
- Abstract: A central dilemma of epithelial cell turnover is eliminating and replacing cells while simultaneously preserving tissue architecture and barrier function. Conventionally, apoptotic or non-apoptotic cell extrusion has been implicated in the intestinal epithelial turnover. Here, we identify a non-lytic membrane permeabilization program that drives physiological enterocyte turnover in vivo. In the Drosophila intestine,...
- Summary (fallback): 机器翻译摘要显示：上皮细胞更新的核心困境是消除和替换细胞，同时保留组织结构和屏障功能。传统上，凋亡或非凋亡细胞的排出与肠上皮更新有关。在这里，我们确定了一种非裂解膜透化程序，可驱动体内生理性肠上皮细胞更新。在果蝇肠道中，肠上皮细胞经历细胞死亡，这是一种非凋亡形式的细胞死亡，其特征是细胞质蛋白的消耗。我们发现这个过程是由估计直径为 16-50 nm 的瞬时质膜孔介导的，允许细胞外蛋白质流入和细胞质内容物的损失。成孔蛋白 Ninjurin A (NijA) 在 erebosis 过程中积累为点，对于驱动这一过程是必要且充分的。
- Keywords: membrane, epithelial, cell, turnover, permeabilization

### 25. [Tetherin 加强免疫代谢检查点，协调脂肪细胞中的糖酵解和干扰素信号传导](https://www.biorxiv.org/content/10.64898/2026.07.06.735062v1)
- Original title: Tetherin enforces an immunometabolic checkpoint that coordinates glycolytic and interferon signaling in adipocytes
- Authors: Cho, C. H., Jang, Y., Warnock, A., Yildiz, R., Jhang, J. et al.
- Meta: 2026-07-07 | cell biology | DOI: 10.64898/2026.07.06.735062
- 中文摘要: 先天免疫信号和葡萄糖代谢之间的协调是机体稳态的基础，然而，尽管数十年来将免疫和代谢联系起来的研究，代谢细胞抑制抗病毒先天信号同时在营养过剩期间保持糖酵解能力的机制仍然不明确。在这里，我们将 Tetherin (BST2) 确定为一种独特的细胞固有免疫代谢检查点，它将 I 型干扰素 (IFN-I) 信号传导的抑制与脂肪细胞中糖酵解能力的保存结合起来。 Tetherin 定位于内质网，并组织一个富含抗病毒传感调节因子和脂肪细胞中糖酵解控制节点的相互作用组。
- Abstract: Coordination between innate immune signaling and glucose metabolism is fundamental to organismal homeostasis, yet despite decades of study linking immunity and metabolism, the mechanisms by which metabolic cells restrain antiviral innate signaling while preserving glycolytic competence during overnutrition remain poorly defined. Here we identify Tetherin (BST2) as a unique cell-intrinsic immunometabolic checkpoint t...
- Summary (fallback): 机器翻译摘要显示：先天免疫信号和葡萄糖代谢之间的协调是机体稳态的基础，然而，尽管数十年来将免疫和代谢联系起来的研究，代谢细胞抑制抗病毒先天信号同时在营养过剩期间保持糖酵解能力的机制仍然不明确。在这里，我们将 Tetherin (BST2) 确定为一种独特的细胞固有免疫代谢检查点，它将 I 型干扰素 (IFN-I) 信号传导的抑制与脂肪细胞中糖酵解能力的保存结合起来。 Tetherin 定位于内质网，并组织一个富含抗病毒传感调节因子和脂肪细胞中糖酵解控制节点的相互作用组。
- Keywords: tetherin, glycolytic, signaling, immunometabolic, adipocytes

### 26. [使用 CRISPR/Cas9 介导的分裂荧光蛋白敲入，对海胆 Lytechinus pictus 进行有效的内源标记](https://www.biorxiv.org/content/10.64898/2026.07.06.736833v1)
- Original title: Efficient Endogenous Tagging in the Sea Urchin, Lytechinus pictus, Using CRISPR/Cas9-mediated Split-Fluorescent Protein Knock-In
- Authors: Lee, Y., Jenniches, C., Tjeerdema, E., Jackson, E., Paix, A. et al.
- Meta: 2026-07-07 | developmental biology | DOI: 10.64898/2026.07.06.736833
- 中文摘要: 荧光报告基因的精确敲入是研究胚胎发生的动态细胞和分子过程的有力工具。然而，大插入片段（例如全长荧光蛋白）的传统 CRISPR-Cas9 敲入效率低下。这限制了它在许多新兴模型系统中的应用，包括海胆。在这里，我们使用转基因 Lytechinus pictus 系克服了这一障碍，该系普遍表达 mNeonGreen (mNG3K1-10) 大片段。在该品系中，只有当 CRISPR 介导的敲入传递 mNG211（荧光蛋白的第 11 条 β 链）以补充组成型表达片段时，荧光才会重建。
- Abstract: Precise knock-in of fluorescent reporters is a powerful tool for studying the dynamic cellular and molecular processes of embryogenesis. However, conventional CRISPR-Cas9 knock-in of large inserts, such as full-length fluorescent proteins, is inefficient. This has limited its application in many emerging model systems, including sea urchins. Here, we overcome this barrier using a transgenic Lytechinus pictus line th...
- Summary (fallback): 机器翻译摘要显示：荧光报告基因的精确敲入是研究胚胎发生的动态细胞和分子过程的有力工具。然而，大插入片段（例如全长荧光蛋白）的传统 CRISPR-Cas9 敲入效率低下。这限制了它在许多新兴模型系统中的应用，包括海胆。在这里，我们使用转基因 Lytechinus pictus 系克服了这一障碍，该系普遍表达 mNeonGreen (mNG3K1-10) 大片段。在该品系中，只有当 CRISPR 介导的敲入传递 mNG211（荧光蛋白的第 11 条 β 链）以补充组成型表达片段时，荧光才会重建。
- Keywords: protein, knock-in, fluorescent, full-length, endogenous

### 27. [整个大陆范围内相机陷阱指标的校准揭示了欧洲野猫的人口密度较低](https://www.biorxiv.org/content/10.64898/2026.07.06.734798v1)
- Original title: Continent-wide calibration of camera-trap metrics reveals low population densities in the European wildcat
- Authors: Nogueira, C., Alves, B. S. G., Anile, S., Barona, J., Bastianelli, M. L. et al.
- Meta: 2026-07-07 | ecology | DOI: 10.64898/2026.07.06.734798
- 中文摘要: 有效的保护取决于可靠反映物种状况的人口统计指标，特别是种群丰度。然而，对于低密度出现的难以捉摸的物种，这样的指标仍然很难获得。空间捕获-再捕获（SCR）模型是估计标记群体密度的标准化方法，但其数据要求，特别是跨个体的多次空间重新捕获的需要，通常限制了在小群体或数据匮乏群体中的适用性。这种限制导致了一些最脆弱物种的知识差距，破坏了基于证据的保护规划和管理。
- Abstract: Effective conservation depends on demographic metrics that reliably reflect species status, particularly population abundance. For elusive species occurring at low densities, however, such metrics remain difficult to obtain. Spatial capture-recapture (SCR) models are the standardized approach for estimating density in marked populations, but their data requirements, especially the need for multiple spatial recapture...
- Summary (fallback): 机器翻译摘要显示：有效的保护取决于可靠反映物种状况的人口统计指标，特别是种群丰度。然而，对于低密度出现的难以捉摸的物种，这样的指标仍然很难获得。空间捕获-再捕获（SCR）模型是估计标记群体密度的标准化方法，但其数据要求，特别是跨个体的多次空间重新捕获的需要，通常限制了在小群体或数据匮乏群体中的适用性。这种限制导致了一些最脆弱物种的知识差距，破坏了基于证据的保护规划和管理。
- Keywords: density, populations, metrics, species, densities

### 28. [为什么连锁不平衡测量不一致：稀有常见单倍型结构的费舍尔几何](https://www.biorxiv.org/content/10.64898/2026.07.02.736022v1)
- Original title: Why linkage disequilibrium measures disagree: Fisher geometry of rare common haplotype structure
- Authors: Ichikawa, Y.
- Meta: 2026-07-07 | genetics | DOI: 10.64898/2026.07.02.736022
- 中文摘要: 传统的 LD 测量（例如 r2）在罕见的常见区域中表现不佳，特别是在不对称配置（例如嵌套单倍型结构）中。由于 r2 是对称且二次的，因此它以两种方式删除方向结构：平方丢弃由带符号的 LD 系数 D 保留的符号或相位，而对称归一化则隐藏条件概率 P(A|B) 和 P(B|A) 之间的不对称性。虽然 D 恢复了相位，但它是轨迹对称且未归一化的；它的大小很难在频率范围内进行比较，并且它本身并不能表达不对称性的运行方式。因此，我们将条件概率不对称性 {Delta} = P(A|B) - P(B|A) 以及 r2 和 D 分析为费希尔信息度量下单倍型单纯形上的不同标量函数。
- Abstract: Conventional LD measures such as r2 perform poorly in the rare common regime, particularly in asymmetric configurations such as nested haplotype structure. Because r2 is symmetric and quadratic, it removes directional structure in two ways: squaring discards the sign, or phase, retained by the signed LD coefficient D, while symmetric normalization hides the asymmetry between the conditional probabilities P(A|B) and...
- Summary (fallback): 机器翻译摘要显示：传统的 LD 测量（例如 r2）在罕见的常见区域中表现不佳，特别是在不对称配置（例如嵌套单倍型结构）中。由于 r2 是对称且二次的，因此它以两种方式删除方向结构：平方丢弃由带符号的 LD 系数 D 保留的符号或相位，而对称归一化则隐藏条件概率 P(A|B) 和 P(B|A) 之间的不对称性。虽然 D 恢复了相位，但它是轨迹对称且未归一化的；它的大小很难在频率范围内进行比较，并且它本身并不能表达不对称性的运行方式。因此，我们将条件概率不对称性 {Delta} = P(A|B) - P(B|A) 以及 r2 和 D 分析为费希尔信息度量下单倍型单纯形上的不同标量函数。
- Keywords: fisher, haplotype, structure, rare, symmetric

### 29. [基于片段的氨基甲酸酯水解酶活性位点探索揭示了氨基甲酸酯结合模式的多样性](https://www.biorxiv.org/content/10.64898/2026.07.06.734427v1)
- Original title: Fragment Based Active Site Exploration of Urethane Hydrolases Reveals a Diversity of Urethane Binding Modes
- Authors: Bicer, D., Kochubei, D., Graham, R., Pena-Diaz, S., Rotilio, L. et al.
- Meta: 2026-07-07 | biochemistry | DOI: 10.64898/2026.07.06.734427
- 中文摘要: 氨基甲酸酯酶的发现、表征和工程的最新进展为聚氨酯废物的可持续生物催化降解提供了新的机遇。对酶-塑性相互作用的机制理解对于基于结构的工程增强氨基甲酸酯酶活性至关重要。然而，聚氨酯极其复杂和疏水的性质使得阐明酶-塑料相互作用的结构基础具有挑战性。在这里，我们使用基于片段的方法来表征两种具有不同催化支架的新型氨基甲酸酯酶的活性位点，同时采用晶体片段筛选（FASE）活动和模拟底物、过渡态或产物的塑料类似物的可溶性片段。
- Abstract: Recent advances in the discovery, characterisation, and engineering of urethanases provide new opportunities for the sustainable biocatalytic degradation of polyurethane waste. A mechanistic understanding of enzyme-plastic interactions is essential for structure-based engineering to enhance urethanase activity. However, the extremely complex and hydrophobic nature of polyurethane makes it challenging to elucidate th...
- Summary (fallback): 机器翻译摘要显示：氨基甲酸酯酶的发现、表征和工程的最新进展为聚氨酯废物的可持续生物催化降解提供了新的机遇。对酶-塑性相互作用的机制理解对于基于结构的工程增强氨基甲酸酯酶活性至关重要。然而，聚氨酯极其复杂和疏水的性质使得阐明酶-塑料相互作用的结构基础具有挑战性。在这里，我们使用基于片段的方法来表征两种具有不同催化支架的新型氨基甲酸酯酶的活性位点，同时采用晶体片段筛选（FASE）活动和模拟底物、过渡态或产物的塑料类似物的可溶性片段。
- Keywords: polyurethane, active, binding, urethanases, interactions

### 30. [来自莱姆病病原体的辅因子混杂 HMGR 阐明了细菌类异戊二烯生物合成的多样性](https://www.biorxiv.org/content/10.64898/2026.07.06.735745v1)
- Original title: A cofactor-promiscuous HMGR from the Lyme disease pathogen illuminates diversity in bacterial isoprenoid biosynthesis
- Authors: Paady, I., McCausland, J., Frazier, M., Chatterjee, P., Setegne, M. et al.
- Meta: 2026-07-07 | biochemistry | DOI: 10.64898/2026.07.06.735745
- 中文摘要: 莱姆病病原体伯氏疏螺旋体含有高度减少的基因组，缺乏许多主要代谢途径。然而，伯氏疏螺旋体保留了合成异戊烯焦磷酸 (IPP) 的甲羟戊酸途径，异戊烯焦磷酸是肽聚糖载体脂质的前体。虽然甲羟戊酸途径和催化其限速步骤的酶（3-羟基-3-甲基戊二酰辅酶 A 还原酶，HMGR）在脊椎动物中得到了充分研究，但人们对伯氏疏螺旋体和许多病原菌中的途径知之甚少。在这项工作中，我们揭示了 HMGR 是伯氏疏螺旋体中的一种关键代谢酶。我们证明 HMGR 的缺失会导致形态缺陷和肽聚糖的从头合成减弱；这些缺陷可通过外源性甲羟戊酸和 IPP 得到改善。
- Abstract: The Lyme disease pathogen Borrelia burgdorferi contains a highly reduced genome lacking many primary metabolic pathways. However, B. burgdorferi retains the mevalonate pathway that synthesizes isopentenyl pyrophosphate (IPP), the precursor to the peptidoglycan carrier lipid. While the mevalonate pathway and the enzyme that catalyzes its rate-limiting step (3-hydroxy-3-methyl glutaryl coenzyme A reductase, HMGR) are...
- Summary (fallback): 机器翻译摘要显示：莱姆病病原体伯氏疏螺旋体含有高度减少的基因组，缺乏许多主要代谢途径。然而，伯氏疏螺旋体保留了合成异戊烯焦磷酸 (IPP) 的甲羟戊酸途径，异戊烯焦磷酸是肽聚糖载体脂质的前体。虽然甲羟戊酸途径和催化其限速步骤的酶（3-羟基-3-甲基戊二酰辅酶 A 还原酶，HMGR）在脊椎动物中得到了充分研究，但人们对伯氏疏螺旋体和许多病原菌中的途径知之甚少。在这项工作中，我们揭示了 HMGR 是伯氏疏螺旋体中的一种关键代谢酶。我们证明 HMGR 的缺失会导致形态缺陷和肽聚糖的从头合成减弱；这些缺陷可通过外源性甲羟戊酸和 IPP 得到改善。
- Keywords: hmgr, burgdorferi, pathogen, highly, mevalonate

## medrxiv

### 1. [使用位移跟踪矩阵流数据和非药物干预合规场景对本迪布焦埃博拉病毒病在乌干达的输入和传播进行基于网络的建模](https://www.medrxiv.org/content/10.64898/2026.06.22.26356210v2)
- Original title: Network-based modelling of Bundibugyo Ebola virus disease importation and spread in Uganda using Displacement Tracking Matrix flow data and non-pharmaceutical intervention compliance scenarios
- Authors: Walekhwa, A. W., Mbaka, P., Nannyonga, B. K., Silal, S. P., Bbuye, M. et al.
- Meta: 2026-07-07 | infectious diseases | DOI: 10.64898/2026.06.22.26356210
- 中文摘要: 背景：2026 年乌干达爆发的本迪布焦埃博拉疫情与刚果民主共和国 (DRC) 持续流行的疫情有关，通过人员流动跨境和在国内传播。我们的目的是量化进口和传播模式，为国家以下各级的有针对性的干预措施提供信息。方法：我们使用 2026 年 5 月 15 日至 24 日收集的 IOM 位移跟踪矩阵 (DTM) 流（观察到的 11,245 次移动）和 2024 年乌干达人口普查（4590 万人）构建了一个数据驱动的定向加权移动网络。在 90 天内，对乌干达 135 个地区和刚果民主共和国的两个省份模拟了一个随机集合群体 SEIR 模型，该模型纳入了症状前传播以及接触者和感染者的移动。 7 1 7 敏捷响应是通过动态接触者追踪覆盖率（40%、70%、85%）明确建模的。
- Abstract: Background: The 2026 Bundibugyo Ebola outbreak in Uganda, linked to the ongoing epidemic in the Democratic Republic of the Congo (DRC), spread through human mobility across borders and within the country. We aimed to quantify importation and spread patterns to inform targeted interventions at subnational level. Methods: We constructed a data-driven directed weighted mobility network using IOM Displacement Tracking M...
- Summary (fallback): 机器翻译摘要显示：背景：2026 年乌干达爆发的本迪布焦埃博拉疫情与刚果民主共和国 (DRC) 持续流行的疫情有关，通过人员流动跨境和在国内传播。我们的目的是量化进口和传播模式，为国家以下各级的有针对性的干预措施提供信息。方法：我们使用 2026 年 5 月 15 日至 24 日收集的 IOM 位移跟踪矩阵 (DTM) 流（观察到的 11,245 次移动）和 2024 年乌干达人口普查（4590 万人）构建了一个数据驱动的定向加权移动网络。在 90 天内，对乌干达 135 个地区和刚果民主共和国的两个省份模拟了一个随机集合群体 SEIR 模型，该模型纳入了症状前传播以及接触者和感染者的移动。 7 1 7 敏捷响应是通过动态接触者追踪覆盖率（40%、70%、85%）明确建模的。
- Keywords: interventions, cases, non-pharmaceutical, parameters, kampala

### 2. [青少年自杀患者危险行为增加的情绪计算机制](https://www.medrxiv.org/content/10.1101/2023.10.31.23297870v6)
- Original title: Mood computational mechanisms underlying increased risk behavior in adolescent suicidal patients
- Authors: Wang, Z., Nan, T., Lu, F., Yu, Y., Cai, X. et al.
- Meta: 2026-07-07 | psychiatry and clinical psychology | DOI: 10.1101/2023.10.31.23297870
- 中文摘要: 自杀念头和行为（STB）是全世界死亡的主要原因之一。尽管之前的研究一致记录了 STB 患者冒险行为的增加，并将情绪障碍确定为自杀的核心特征，但这种危险行为增加背后的精确认知和情感计算机制仍然知之甚少。在这里，83 名患有情感障碍的青少年住院患者，包括 58 名 STB 患者 (S+) 和 25 名无 STB 患者 (S-)，以及 118 名年龄和性别匹配的健康对照 (HC) 完成了一项决策任务，涉及在某些选项和赌博选项之间进行选择，以及瞬时情绪评级。行为分析表明，S+ 比 S- 和 HC 表现出更大的冒险精神。
- Abstract: Suicidal thoughts and behaviors (STB) are among the leading causes of death worldwide. Although previous research has consistently documented elevated risk-taking in individuals with STB and identified mood disturbances as central features of suicidality, the precise cognitive and affective computational mechanisms underlying this increased risky behavior remain poorly understood. Here, 83 adolescent inpatients with...
- Summary (fallback): 机器翻译摘要显示：自杀念头和行为（STB）是全世界死亡的主要原因之一。尽管之前的研究一致记录了 STB 患者冒险行为的增加，并将情绪障碍确定为自杀的核心特征，但这种危险行为增加背后的精确认知和情感计算机制仍然知之甚少。在这里，83 名患有情感障碍的青少年住院患者，包括 58 名 STB 患者 (S+) 和 25 名无 STB 患者 (S-)，以及 118 名年龄和性别匹配的健康对照 (HC) 完成了一项决策任务，涉及在某些选项和赌博选项之间进行选择，以及瞬时情绪评级。行为分析表明，S+ 比 S- 和 HC 表现出更大的冒险精神。
- Keywords: computational, mood, behavior, risk-taking, affective

### 3. [阿司匹林-肠-脑-胶质瘤轴的多组学综合分析：转录组学、蛋白质组学、表观遗传学、孟德尔随机化和单细胞转录组学证据集中于 NEO1/Hepcidin 铁重编程和铁死亡漏洞](https://www.medrxiv.org/content/10.64898/2026.06.01.26354602v2)
- Original title: Multi-Omics Integrative Analysis of the Aspirin-Gut-Brain-Glioma Axis: Transcriptomic, Proteomic, Epigenetic, Mendelian Randomization, and Single-Cell Transcriptomic Evidence Converges on NEO1/Hepcidin Iron Reprogramming and Ferroptosis Vulnerability
- Authors: Ma, C., Zhang, F., Wu, F., Shi, C., Wu, X. et al.
- Meta: 2026-07-07 | oncology | DOI: 10.64898/2026.06.01.26354602
- 中文摘要: 背景：尽管流行病学对阿司匹林对神经胶质瘤的化学预防潜力感兴趣，但涵盖肠道微生物生态、COX-2/PGE2信号传导、通过NEO1/铁调素调节轴的器官间铁稳态、表观遗传重编程和铁死亡的潜在多层分子机制尚未在多组学水平上系统地表征。方法：我们利用 TCGA-GBM (n = 172) 和 TCGA-LGG (n = 534) 转录组、CPTAC GBM 蛋白质组学 (n = 99)、TCGA HM450K DNA 甲基化数据 (GBM n = 140、LGG n = 516)、GEO 阿司匹林扰动数据集、IEU OpenGWAS 摘要统计数据和独立数据进行综合多组学分析。单细胞 RNA-seq 数据（GSE131928，28 位 GBM 患者）。
- Abstract: Background: Despite epidemiological interest in aspirin's chemopreventive potential against glioma, the underlying multilayered molecular mechanisms spanning gut microbial ecology, COX-2/PGE2 signaling, inter-organ iron homeostasis via the NEO1/hepcidin regulatory axis, epigenetic reprogramming, and ferroptosis have not been systematically characterized at the multi-omics level. Methods: We conducted an integrative...
- Summary (fallback): 机器翻译摘要显示：背景：尽管流行病学对阿司匹林对神经胶质瘤的化学预防潜力感兴趣，但涵盖肠道微生物生态、COX-2/PGE2信号传导、通过NEO1/铁调素调节轴的器官间铁稳态、表观遗传重编程和铁死亡的潜在多层分子机制尚未在多组学水平上系统地表征。方法：我们利用 TCGA-GBM (n = 172) 和 TCGA-LGG (n = 534) 转录组、CPTAC GBM 蛋白质组学 (n = 99)、TCGA HM450K DNA 甲基化数据 (GBM n = 140、LGG n = 516)、GEO 阿司匹林扰动数据集、IEU OpenGWAS 摘要统计数据和独立数据进行综合多组学分析。单细胞 RNA-seq 数据（GSE131928，28 位 GBM 患者）。
- Keywords: analysis, neo1, iron, ferroptosis, axis

### 4. [乌干达裂谷热监测社区牲畜堕胎报告的促进因素和障碍：COM-B 分析](https://www.medrxiv.org/content/10.1101/2025.08.01.25332592v2)
- Original title: Facilitators and Barriers to Community-Based Livestock Abortion Reporting for Rift Valley Fever Surveillance in Uganda: A COM-B Analysis
- Authors: Walekhwa, A. W., Conlan, A. J., Namakula, L. N., Nakazibwe, B., Buchaki, S. A. et al.
- Meta: 2026-07-07 | epidemiology | DOI: 10.1101/2025.08.01.25332592
- 中文摘要: 裂谷热病 (RVFD) 通过牲畜流产风暴造成重大经济损失，但在流行地区，基于社区的流产早期预警报告仍然不够理想。本研究分析了牲畜流产报告的行为决定因素，为乌干达的裂谷热监测干预措施提供信息。我们在乌干达伊辛吉罗区采用定性数据收集方法，采用能力、机会、动机、行为 (COM-B) 框架进行了一项横断面研究。我们对国家/地区政策制定者和技术官员进行了 29 次关键知情人访谈，并进行了 17 次焦点小组讨论，涉及牲畜所有者、屠宰场经营者和地方领导人。使用 NVivo 12 对成绩单进行演绎主题分析，并进行独立的编码验证和成员检查。
- Abstract: Rift Valley Fever Disease (RVFD) causes substantial economic losses via livestock abortion storms, yet community based abortion reporting for early warning remains suboptimal in endemic settings. This study analysed the behavioural determinants of livestock abortion reporting to inform RVF surveillance interventions in Uganda. We conducted a cross sectional study using qualitative data collection methods in Isingiro...
- Summary (fallback): 机器翻译摘要显示：裂谷热病 (RVFD) 通过牲畜流产风暴造成重大经济损失，但在流行地区，基于社区的流产早期预警报告仍然不够理想。本研究分析了牲畜流产报告的行为决定因素，为乌干达的裂谷热监测干预措施提供信息。我们在乌干达伊辛吉罗区采用定性数据收集方法，采用能力、机会、动机、行为 (COM-B) 框架进行了一项横断面研究。我们对国家/地区政策制定者和技术官员进行了 29 次关键知情人访谈，并进行了 17 次焦点小组讨论，涉及牲畜所有者、屠宰场经营者和地方领导人。使用 NVivo 12 对成绩单进行演绎主题分析，并进行独立的编码验证和成员检查。
- Keywords: reporting, livestock, abortion, analysis, surveillance

### 5. [综合数据可降低快速诊断测试解释中公平人工智能的障碍](https://www.medrxiv.org/content/10.1101/2025.02.25.25322677v3)
- Original title: Synthetic Data to Lower Barriers Towards Equitable Artificial Intelligence in Rapid Diagnostic Test Interpretation
- Authors: Rogers, E., Turbe, V., Gareta, D., Herbst, C., McKendry, R. A. et al.
- Meta: 2026-07-07 | public and global health | DOI: 10.1101/2025.02.25.25322677
- 中文摘要: 快速诊断测试 (RDT) 支持经济实惠的疾病诊断。机器学习 (ML) 可以改进 RDT 解释，但通常依赖于大型、专有且昂贵的现实世界图像库。我们推出了 SynSight：一个支持 ML 的 RDT 分段和分类管道，在合成数据上进行训练。 SynSight 经过 HIV（98% 灵敏度、99% 特异性）和 COVID-19 RDT（准确度高达 99%）验证，无需真实训练图像即可实现快速 ML 训练，与新 RDT 开发保持同步。
- Abstract: Rapid diagnostic tests (RDTs) support affordable disease diagnosis. Machine learning (ML) can improve RDT interpretation but often relies on large, proprietary, and costly real-world image libraries. We present SynSight: a ML-enabled RDT segmentation and classification pipeline trained on synthetic data. Validated on HIV (98% sensitivity, 99% specificity) and COVID-19 RDTs (up to 99% accuracy), SynSight enables rapi...
- Summary (fallback): 机器翻译摘要显示：快速诊断测试 (RDT) 支持经济实惠的疾病诊断。机器学习 (ML) 可以改进 RDT 解释，但通常依赖于大型、专有且昂贵的现实世界图像库。我们推出了 SynSight：一个支持 ML 的 RDT 分段和分类管道，在合成数据上进行训练。 SynSight 经过 HIV（98% 灵敏度、99% 特异性）和 COVID-19 RDT（准确度高达 99%）验证，无需真实训练图像即可实现快速 ML 训练，与新 RDT 开发保持同步。
- Keywords: rapid, synthetic, diagnostic, interpretation, rdts

### 6. [现实分布变化下生物医学图像分类的故障检测：大规模评估的见解](https://www.medrxiv.org/content/10.64898/2026.05.04.26350496v2)
- Original title: Failure detection in biomedical image classification under realistic distribution shifts: insights from a large-scale evaluation
- Authors: Steinmetz, P., Frouin, F., Morard, V., Buvat, I.
- Meta: 2026-07-07 | radiology and imaging | DOI: 10.64898/2026.05.04.26350496
- 中文摘要: 由于不同的采集协议、设备和患者群体，生物医学图像 (BMI) 表现出变异性，因此推理时的故障检测对于临床分类器的可靠部署至关重要。由于现有的故障检测方法评估使用不同的设置，因此很难比较结果并确定最佳策略（如果有）。我们对八个 BMI 任务的八个置信评分函数和两个评分聚合策略进行了全面评估，涵盖不同的模式、骨干架构、训练设置和失败源。联合评估置信度排序能力和分类误差缓解。虽然没有任何一种方法能够系统地在各个设置中占主导地位，但置信度分数的汇总始终匹配或接近最佳的单独方法，并大大降低了静默故障率。
- Abstract: Biomedical images (BMI) exhibit variability due to different acquisition protocols, devices, and patient populations, making failure detection at inference time essential for reliable deployment of clinical classifiers. As existing evaluations of failure detection methods use different settings, it is difficult to compare results and identify the best strategy, if any. We present a comprehensive evaluation of eight...
- Summary (fallback): 机器翻译摘要显示：由于不同的采集协议、设备和患者群体，生物医学图像 (BMI) 表现出变异性，因此推理时的故障检测对于临床分类器的可靠部署至关重要。由于现有的故障检测方法评估使用不同的设置，因此很难比较结果并确定最佳策略（如果有）。我们对八个 BMI 任务的八个置信评分函数和两个评分聚合策略进行了全面评估，涵盖不同的模式、骨干架构、训练设置和失败源。联合评估置信度排序能力和分类误差缓解。虽然没有任何一种方法能够系统地在各个设置中占主导地位，但置信度分数的汇总始终匹配或接近最佳的单独方法，并大大降低了静默故障率。
- Keywords: failure, detection, confidence, settings, biomedical

### 7. [用于预测晚期非小细胞肺癌抗 PD-(L)1 治疗原发性耐药的多模式分析：前瞻性 PIONeeR 生物标志物研究](https://www.medrxiv.org/content/10.64898/2026.01.09.26343779v2)
- Original title: Multimodal profiling for prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer: the prospective PIONeeR biomarkers study
- Authors: Barlesi, F., Monville, F., Greillier, L., Ngoi, N., Ciccolini, J. et al.
- Meta: 2026-07-07 | oncology | DOI: 10.64898/2026.01.09.26343779
- 中文摘要: 背景 晚期非小细胞肺癌 (NSCLC) 抗 PD-(L)1 治疗原发性耐药的预处理预测仍然是一个未得到满足的临床需求。现有的生物标志物——包括 PD-L1 表达和肿瘤突变负荷 (TMB)——缺乏足够的辨别力，并且仍然缺乏针对原发性耐药的多模式预测模型来精确推动患者的治疗策略。方法 PIONeeR 是一项在 17 个中心进行的前瞻性、多中心生物标志物研究 (NCT03493581)。患有晚期 NSCLC 的成人患者开始标准护理一线铂类化疗加抗 PD-(L)1 治疗，或二线或后线抗 PD-(L)1 单药治疗。
- Abstract: Background Pretreatment prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer (NSCLC) remains an unmet clinical need. Existing biomarkers - including PD-L1 expression and tumour mutational burden (TMB) - are insufficiently discriminatory, and multimodal predictive models targeting primary resistance are still lacking to precisely drive patients treatment strategy. Methods PI...
- Summary (fallback): 机器翻译摘要显示：背景 晚期非小细胞肺癌 (NSCLC) 抗 PD-(L)1 治疗原发性耐药的预处理预测仍然是一个未得到满足的临床需求。现有的生物标志物——包括 PD-L1 表达和肿瘤突变负荷 (TMB)——缺乏足够的辨别力，并且仍然缺乏针对原发性耐药的多模式预测模型来精确推动患者的治疗策略。方法 PIONeeR 是一项在 17 个中心进行的前瞻性、多中心生物标志物研究 (NCT03493581)。患有晚期 NSCLC 的成人患者开始标准护理一线铂类化疗加抗 PD-(L)1 治疗，或二线或后线抗 PD-(L)1 单药治疗。
- Keywords: primary, multimodal, resistance, anti-pd-, therapy

### 8. [卧推训练可改善老年女性的楼梯行走动态：来自探索性非线性运动学分析的证据](https://www.medrxiv.org/content/10.64898/2026.07.02.26357116v1)
- Original title: Bench-stepping training improves stair-walking dynamics in older women: evidence from an exploratory nonlinear kinematic analysis
- Authors: Baggen, R. J., van Schooten, K. S., Van Roie, E., Verschueren, S. M., Delecluse, C. et al.
- Meta: 2026-07-07 | sports medicine | DOI: 10.64898/2026.07.02.26357116
- 中文摘要: 简介： 爬楼梯挑战老年人的平衡和协调性。卧推训练可以提高健康老年女性的爬楼梯速度。这项研究评估了卧推是否也可以改善楼梯行走过程中的动态平衡和运动复杂性。方法：楼梯行走数据取自之前一项涉及 45 名健康老年女性 (69 岁+/-4) 的研究，该研究评估了 12 周的卧凳行走干预与非训练对照的效果。在楼梯上升和下降过程中测量质心加速度。线性动力学包括时间、加速度大小和谐波比（HR；表示对称性）。使用非线性动力学来量化运动复杂性，包括样本熵 (SE)、递归量化分析 (RQA) 和分形维数 (FD)。
- Abstract: Introduction: Stair walking challenges balance and coordination in older people. Bench-stepping training improves stair climbing speed in healthy older women. This study assessed whether bench-stepping also improves dynamic balance and movement complexity during stair walking. Methods: Stair walking data were obtained from a previous study involving 45 healthy older women (69y+/-4) that assessed the effects of a 12-...
- Summary (fallback): 机器翻译摘要显示：简介： 爬楼梯挑战老年人的平衡和协调性。卧推训练可以提高健康老年女性的爬楼梯速度。这项研究评估了卧推是否也可以改善楼梯行走过程中的动态平衡和运动复杂性。方法：楼梯行走数据取自之前一项涉及 45 名健康老年女性 (69 岁+/-4) 的研究，该研究评估了 12 周的卧凳行走干预与非训练对照的效果。在楼梯上升和下降过程中测量质心加速度。线性动力学包括时间、加速度大小和谐波比（HR；表示对称性）。使用非线性动力学来量化运动复杂性，包括样本熵 (SE)、递归量化分析 (RQA) 和分形维数 (FD)。
- Keywords: stair, bench-stepping, dynamics, acceleration, r2partial

### 9. [宽度延迟指数：用于评估胰岛素抵抗的仅葡萄糖 OGTT 指标](https://www.medrxiv.org/content/10.64898/2026.07.05.26357315v1)
- Original title: The Width-Delay Index: a Glucose-Only OGTT Metric for Assessing Insulin Resistance
- Authors: Zhang, R.
- Meta: 2026-07-07 | endocrinology | DOI: 10.64898/2026.07.05.26357315
- 中文摘要: 背景：胰岛素抵抗是代谢性疾病的核心病理生理学特征，但通过稳态血浆葡萄糖（SSPG）测试对其进行参考标准评估的程序要求较高且劳动强度大，限制了其在常规临床护理和大规模研究中的使用。由于 OGTT 葡萄糖谱广泛可用，我们的目标是开发一种仅葡萄糖指标来表征动态葡萄糖反应并估计 SSPG 测量的胰岛素抵抗。方法：我们开发了宽度延迟指数 (WDI)，这是一种仅包含葡萄糖的 OGTT 指标，集成了相对暴露宽度、延迟暴露时间和血糖下限。在具有 16 点静脉 OGTT 概况和配对 SSPG 测量的 32 名受试者的数据集中，使用用于 SSPG 预测的留一交叉验证 (LOOCV) 以及胰岛素抵抗判别和稀疏采样稳健性分析来评估 WDI 表现...
- Abstract: Background: Insulin resistance is a core pathophysiologic feature of metabolic disease, but its reference-standard assessment by steady-state plasma glucose (SSPG) testing is procedurally demanding and labor-intensive, limiting use in routine clinical care and large-scale research. Because OGTT glucose profiles are widely available, we aimed to develop a glucose-only metric to characterize dynamic glucose responses...
- Summary (fallback): 机器翻译摘要显示：背景：胰岛素抵抗是代谢性疾病的核心病理生理学特征，但通过稳态血浆葡萄糖（SSPG）测试对其进行参考标准评估的程序要求较高且劳动强度大，限制了其在常规临床护理和大规模研究中的使用。由于 OGTT 葡萄糖谱广泛可用，我们的目标是开发一种仅葡萄糖指标来表征动态葡萄糖反应并估计 SSPG 测量的胰岛素抵抗。方法：我们开发了宽度延迟指数 (WDI)，这是一种仅包含葡萄糖的 OGTT 指标，集成了相对暴露宽度、延迟暴露时间和血糖下限。在具有 16 点静脉 OGTT 概况和配对 SSPG 测量的 32 名受试者的数据集中，使用用于 SSPG 预测的留一交叉验证 (LOOCV) 以及胰岛素抵抗判别和稀疏采样稳健性分析来评估 WDI 表现...
- Keywords: ogtt, glucose, index, glucose-only, insulin

### 10. [NIH 撤回文章的成本：实时分析](https://www.medrxiv.org/content/10.64898/2026.07.04.26357187v1)
- Original title: Cost of Retracted Articles to the NIH: a Living Analysis
- Authors: Sandoval-Lentisco, A., Ioannidis, J. P. A.
- Meta: 2026-07-07 | epidemiology | DOI: 10.64898/2026.07.04.26357187
- 中文摘要: 撤回引起了广泛关注，并且随着时间的推移变得越来越频繁。撤稿反映了科学的自我纠正性质，但也浪费了资源。撤回观察数据库 (RWD) 包含 60,000 多条记录。我们将 RWD 与 NIH 资助元数据（RePORTER 系统）集成。截至 2026 年 7 月，在 6,081 篇美国附属撤回文章中，1,725 篇 (28.4%) 与至少一项 NIH 资助相关。按 2026 年美元计算，每篇 NIH 资助的撤回文章的平均归属成本为 255,087 美元，按 2026 年美元计算，NIH 资助的撤回研究的归属总成本为 4.4 亿美元。与论文第一作者或最后作者为主要研究者的撤回论文相关的拨款，按 2026 年美元计算，将获得 40.3 亿美元。与其他美国文章相比，NIH 资助的文章需要更长的时间才能被撤回（平均 = 6.3 年），这可能会导致更大的下游影响……
- Abstract: Retractions attract substantial attention and have become more frequent over time. Retractions reflect the self-correcting nature of science but also wasted resources. The Retraction Watch Database (RWD) includes over 60,000 records. We integrated RWD with NIH funding metadata (RePORTER system). As of July 2026, of the 6,081 U.S. affiliated retracted articles, 1,725 (28.4%) were linked to at least one NIH grant. Wit...
- Summary (fallback): 机器翻译摘要显示：撤回引起了广泛关注，并且随着时间的推移变得越来越频繁。撤稿反映了科学的自我纠正性质，但也浪费了资源。撤回观察数据库 (RWD) 包含 60,000 多条记录。我们将 RWD 与 NIH 资助元数据（RePORTER 系统）集成。截至 2026 年 7 月，在 6,081 篇美国附属撤回文章中，1,725 篇 (28.4%) 与至少一项 NIH 资助相关。按 2026 年美元计算，每篇 NIH 资助的撤回文章的平均归属成本为 255,087 美元，按 2026 年美元计算，NIH 资助的撤回研究的归属总成本为 4.4 亿美元。与论文第一作者或最后作者为主要研究者的撤回论文相关的拨款，按 2026 年美元计算，将获得 40.3 亿美元。与其他美国文章相比，NIH 资助的文章需要更长的时间才能被撤回（平均 = 6....
- Keywords: retracted, cost, articles, retractions, nih-funded

### 11. [对接受医学辅助生殖治疗的妇女进行癌症筛查](https://www.medrxiv.org/content/10.64898/2026.07.05.26357336v1)
- Original title: Organised cancer screening among women who receive medically assisted reproduction treatments
- Authors: Walker, A. R., Odahl, S., Venetis, C., Jorm, L., Hacker, N. F. et al.
- Meta: 2026-07-07 | epidemiology | DOI: 10.64898/2026.07.05.26357336
- 中文摘要: 目前还没有关于女性使用医学辅助生殖 (MAR) 进行癌症筛查的公开数据。这些数据将有助于解释该群体的癌症发病率和风险状况。使用基于人口的澳大利亚健康登记和行政数据集，我们比较了 1991 年至 2016 年间接受三种类型 MAR 中的一种的有组织的公共资助的宫颈和乳腺癌筛查女性与未接受的女性的匹配情况。我们对第一次 MAR 治疗前后三年内接受筛查的女性比例进行了建模，并根据年龄、偏远地区、产次、社会经济劣势、癌症病史和其他筛查计划的采用情况进行了调整。
- Abstract: There are no published data on cancer screening by women using medically assisted reproduction (MAR). Such data would aid interpretation of the cancer incidence and risk profiles for this group. Using linked population-based Australian health registries and administrative datasets, we compared organised publicly funded cervical and breast screening episodes for women who received one of three types of MAR and matche...
- Summary (fallback): 机器翻译摘要显示：目前还没有关于女性使用医学辅助生殖 (MAR) 进行癌症筛查的公开数据。这些数据将有助于解释该群体的癌症发病率和风险状况。使用基于人口的澳大利亚健康登记和行政数据集，我们比较了 1991 年至 2016 年间接受三种类型 MAR 中的一种的有组织的公共资助的宫颈和乳腺癌筛查女性与未接受的女性的匹配情况。我们对第一次 MAR 治疗前后三年内接受筛查的女性比例进行了建模，并根据年龄、偏远地区、产次、社会经济劣势、癌症病史和其他筛查计划的采用情况进行了调整。
- Keywords: women, screening, cancer, before, organised

### 12. [SonoPatch：用于按需生理调节的可穿戴超声导入仪](https://www.medrxiv.org/content/10.64898/2026.07.03.26357138v1)
- Original title: SonoPatch: Wearable Sonophoresis for On-Demand Physiological Modulation
- Authors: Shimizu, K., Whitmore, N. W., Hossen, A., Zhang, Y., Maes, P.
- Meta: 2026-07-07 | pharmacology and therapeutics | DOI: 10.64898/2026.07.03.26357138
- 中文摘要: 现有的界面通过视觉、听觉和触觉通道调节用户体验，但以编程方式改变用户内部状态的直接生理调节在很大程度上仍未得到充分探索。我们提出了一种可穿戴超声导入贴片，它使用低频声刺激经皮输送精神活性物质，并评估其在人机交互中可编程生理调节的潜力。我们在一项双盲研究 (N=26) 中对此进行了测试，该研究提供 100 毫克咖啡因与假对照组，记录休息期间的生理信号和持续注意力任务 (SART)。休息期间心率标准差的计划比较是显着的（HR-SD p=0.025，d=1.48），咖啡因组显示出与交感神经激活一致的 HR~SD 抑制。
- Abstract: Existing interfaces modulate user experience through visual, auditory, and haptic channels, but direct physiological modulation, which programmatically alters a user's internal state, remains largely underexplored. We present a wearable sonophoresis patch that uses low-frequency acoustic stimulation to deliver psychoactive substances transdermally, and evaluate its potential for programmable physiological modulation...
- Summary (fallback): 机器翻译摘要显示：现有的界面通过视觉、听觉和触觉通道调节用户体验，但以编程方式改变用户内部状态的直接生理调节在很大程度上仍未得到充分探索。我们提出了一种可穿戴超声导入贴片，它使用低频声刺激经皮输送精神活性物质，并评估其在人机交互中可编程生理调节的潜力。我们在一项双盲研究 (N=26) 中对此进行了测试，该研究提供 100 毫克咖啡因与假对照组，记录休息期间的生理信号和持续注意力任务 (SART)。休息期间心率标准差的计划比较是显着的（HR-SD p=0.025，d=1.48），咖啡因组显示出与交感神经激活一致的 HR~SD 抑制。
- Keywords: physiological, user, heart, rate, wearable

### 13. [N-乙酰半胱氨酸可减少色氨酸引起的精神分裂症患者的异常](https://www.medrxiv.org/content/10.64898/2026.06.25.26356572v1)
- Original title: N-Acetylcysteine Reduces Tryptophan-induced Abnormalities in People with Schizophrenia
- Authors: Hare, S. M., Kelly, D. L., Pan, Y., Chen, S., Blatt, F. et al.
- Meta: 2026-07-07 | psychiatry and clinical psychology | DOI: 10.64898/2026.06.25.26356572
- 中文摘要: 目前的研究评估了抑制犬尿酸（KYNA）合成酶犬尿氨酸转氨酶（KAT）II的N-乙酰半胱氨酸（NAC）是否会影响色氨酸（TRYP）诱导的犬尿氨酸途径代谢物犬尿氨酸和KYNA的外周形成，并改善精神分裂症患者选定的功能结果指标。 58 名患有 DSM-5 精神分裂症或分裂情感障碍的参与者进入了一项双盲、安慰剂对照、随机交叉挑战研究，其中他们接受 NAC（最多 15 克）或安慰剂预处理，然后接受 6 克 TRYP。在接受研究药物之前和之后，参与者接受了实验室（血清犬尿氨酸和 KYNA）、症状（BPRS、SANS 和 CDS）、认知（6 项 MCCB 测试）和脑 MRI（ASL、DTI、1H-MRS）评估。
- Abstract: The current study assessed whether N-acetylcysteine (NAC), which inhibits the kynurenic acid (KYNA)-synthesizing enzyme kynurenine aminotransferase (KAT) II, affects tryptophan (TRYP)-induced peripheral formation of the kynurenine pathway metabolites kynurenine and KYNA and improves selected functional outcome measures in people with schizophrenia. Fifty-eight participants with DSM-5 schizophrenia or schizoaffective...
- Summary (fallback): 机器翻译摘要显示：目前的研究评估了抑制犬尿酸（KYNA）合成酶犬尿氨酸转氨酶（KAT）II的N-乙酰半胱氨酸（NAC）是否会影响色氨酸（TRYP）诱导的犬尿氨酸途径代谢物犬尿氨酸和KYNA的外周形成，并改善精神分裂症患者选定的功能结果指标。 58 名患有 DSM-5 精神分裂症或分裂情感障碍的参与者进入了一项双盲、安慰剂对照、随机交叉挑战研究，其中他们接受 NAC（最多 15 克）或安慰剂预处理，然后接受 6 克 TRYP。在接受研究药物之前和之后，参与者接受了实验室（血清犬尿氨酸和 KYNA）、症状（BPRS、SANS 和 CDS）、认知（6 项 MCCB 测试）和脑 MRI（ASL、DTI、1H-MRS）评估。
- Keywords: kyna, kynurenine, schizophrenia, people, tryp

### 14. [结构化闭塞揭示了急性和慢性精神病的状态依赖性平滑追踪缺陷](https://www.medrxiv.org/content/10.64898/2026.07.03.26357245v1)
- Original title: Structured Occlusion Reveals State-Dependent Smooth Pursuit Deficits Across Acute and Chronic Psychosis
- Authors: Simkovich, T., Segal, I., Bonneh, Y., Israeli, D.
- Meta: 2026-07-07 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.03.26357245
- 中文摘要: 平稳追踪眼动异常在精神病中已得到充分证实，但随临床状态和症状特征而变化的追踪表现的具体组成部分仍没有充分表征。在这里，我们使用快速平滑追踪范式，将标准线性跟踪（向不同方向移动的重复短期试验）与结构化目标遮挡相结合，以检查患有急性精神病、慢性精神病和健康对照的个体的动眼神经表现。当目标暂时隐藏并且凝视必须沿着预期轨迹保持时，遮挡条件允许评估跟踪。基本的动眼神经测量，包括完全追踪增益和初始追赶性扫视特性，在患者体内很大程度上保留了下来。相比之下，更具体的基于轨迹的测量显示出明显的异常。
- Abstract: Smooth pursuit eye movement abnormalities are well established in psychosis, but the specific components of pursuit performance that vary across clinical states and symptom profiles remain insufficiently characterized. Here, we used a rapid smooth pursuit paradigm combining standard linear tracking (repeated short trials moving in different directions) with structured target occlusion to examine oculomotor performan...
- Summary (fallback): 机器翻译摘要显示：平稳追踪眼动异常在精神病中已得到充分证实，但随临床状态和症状特征而变化的追踪表现的具体组成部分仍没有充分表征。在这里，我们使用快速平滑追踪范式，将标准线性跟踪（向不同方向移动的重复短期试验）与结构化目标遮挡相结合，以检查患有急性精神病、慢性精神病和健康对照的个体的动眼神经表现。当目标暂时隐藏并且凝视必须沿着预期轨迹保持时，遮挡条件允许评估跟踪。基本的动眼神经测量，包括完全追踪增益和初始追赶性扫视特性，在患者体内很大程度上保留了下来。相比之下，更具体的基于轨迹的测量显示出明显的异常。
- Keywords: pursuit, tracking, smooth, psychosis, occlusion

### 15. [哪些非洲国家面临无法实现可持续发展目标 3.2 的风险？使用联合国儿童基金会 2024 年数据绘制五岁以下死亡率的贝叶斯图](https://www.medrxiv.org/content/10.64898/2026.07.04.26357223v1)
- Original title: Which African Countries are at Risk of Missing SDG 3.2? Bayesian Mapping of Under-Five Mortality Using UNICEF 2024 Data
- Authors: Oladimeji, D. M., Mustapha, A. K., Ekop, E. E.
- Meta: 2026-07-07 | public and global health | DOI: 10.64898/2026.07.04.26357223
- 中文摘要: 摘要背景：尽管在千年发展目标时代，五岁以下儿童死亡率大幅下降，但整个非洲在实现可持续发展目标 (SDG) 3.2 方面的进展仍然不平衡。确定最有可能无法实现目标的国家对于确定干预措施和资源分配的优先顺序至关重要。方法：利用联合国儿童基金会获得的 49 个非洲国家 2024 年国家级数据进行贝叶斯空间预测生态研究。使用全局 Moran's I 和局部空间关联指标评估空间依赖性。使用集成嵌套拉普拉斯近似 (INLA) 拟合具有高斯、伽马和指数似然的贝叶斯结构化加性回归模型，并使用偏差信息准则 (DIC)、Watanabe-Akaike 信息准则 (WAIC) 和条件预测坐标进行比较。
- Abstract: Abstract Background: Despite considerable reductions in under-five mortality during the Millennium Development Goal era, progress towards Sustainable Development Goal (SDG) 3.2 remains uneven across Africa. Identifying countries at greatest risk of missing the target is essential for prioritizing interventions and resource allocation. Methods: A Bayesian spatial forecasting ecological study was conducted using 2024...
- Summary (fallback): 机器翻译摘要显示：摘要背景：尽管在千年发展目标时代，五岁以下儿童死亡率大幅下降，但整个非洲在实现可持续发展目标 (SDG) 3.2 方面的进展仍然不平衡。确定最有可能无法实现目标的国家对于确定干预措施和资源分配的优先顺序至关重要。方法：利用联合国儿童基金会获得的 49 个非洲国家 2024 年国家级数据进行贝叶斯空间预测生态研究。使用全局 Moran's I 和局部空间关联指标评估空间依赖性。使用集成嵌套拉普拉斯近似 (INLA) 拟合具有高斯、伽马和指数似然的贝叶斯结构化加性回归模型，并使用偏差信息准则 (DIC)、Watanabe-Akaike 信息准则 (WAIC) 和条件预测坐标进行比较。
- Keywords: countries, bayesian, mortality, under-five, africa

### 16. [入院时和入院后新生儿体温过低：与 NEST360 联盟实施的四个撒哈拉以南非洲国家的负担以及与室外气温和新生儿病房温度的关联](https://www.medrxiv.org/content/10.64898/2026.07.04.26357151v1)
- Original title: Neonatal Hypothermia at and after Admission: Burden and Associations with Outside Air Temperature and Neonatal Ward Temperature in Four Sub Saharan African Countries Implementing with the NEST360 Alliance
- Authors: Mar, M., Bohne, C. A., Wainaina, J., Johari, M. T., Okello, G. et al.
- Meta: 2026-07-07 | public and global health | DOI: 10.64898/2026.07.04.26357151
- 中文摘要: 背景：每年有 230 万新生儿死亡，大部分死于可预防的原因。新生儿体温过低是发病率和死亡率的一个重要因素，特别是在资源匮乏的环境中。这项研究量化了四个 NEST360 支持的国家入院时和入院后的低体温负担，并检查了室外气温、病房温度和新生儿低体温之间的关联。方法：我们对肯尼亚、马拉维、尼日利亚和坦桑尼亚 66 个新生儿科室的新生儿入院情况（2021 年 1 月至 2025 年 6 月）进行了回顾性分析。体温过低使用 WHO 阈值进行定义（轻度：36.0-36.4{度}C，中度：32.0-35.9{度}C，重度：<32.0{度}C）。从常规临床记录中提取新生儿入院体温和入院后最低体温。
- Abstract: Background: Annually, 2.3 million newborns die, largely from preventable causes. Neonatal hypothermia is an important contributor to morbidity and mortality, particularly in low-resource settings. This study quantified the burden of hypothermia at and after admission in four NEST360-supported countries and examined associations between outside air temperature, ward temperature, and neonatal hypothermia. Methods: We...
- Summary (fallback): 机器翻译摘要显示：背景：每年有 230 万新生儿死亡，大部分死于可预防的原因。新生儿体温过低是发病率和死亡率的一个重要因素，特别是在资源匮乏的环境中。这项研究量化了四个 NEST360 支持的国家入院时和入院后的低体温负担，并检查了室外气温、病房温度和新生儿低体温之间的关联。方法：我们对肯尼亚、马拉维、尼日利亚和坦桑尼亚 66 个新生儿科室的新生儿入院情况（2021 年 1 月至 2025 年 6 月）进行了回顾性分析。体温过低使用 WHO 阈值进行定义（轻度：36.0-36.4{度}C，中度：32.0-35.9{度}C，重度：<32.0{度}C）。从常规临床记录中提取新生儿入院体温和入院后最低体温。
- Keywords: admission, hypothermia, degrees, temperature, temperatures

### 17. [空气污染与整个生命过程中人口健康之间的延迟关联](https://www.medrxiv.org/content/10.64898/2026.06.25.26356581v1)
- Original title: Delayed associations between air pollution and population health across the life course
- Authors: Bentley, R. A., Ozeryansky, L.
- Meta: 2026-07-07 | public and global health | DOI: 10.64898/2026.06.25.26356581
- 中文摘要: 自 2000 年以来，美国的细颗粒空气污染 (PM2.5) 已下降约一半，但糖尿病和儿童多动症等相关健康结果却并未同步改善。一种可以调和的可能性是，生命早期接触污染会对健康产生影响，这种影响仅在几年或几十年后、污染本身下降后才出现。我们利用二十年的美国县级数据，将年度 PM2.5 估计值与出生结果、糖尿病患病率以及短期和长期范围内儿童注意力缺陷/多动症 (ADHD) 的小区域估计值联系起来。在县内，低出生体重率的变化与同年和出生前一年的 PM2.5 变化相关。
- Abstract: Fine particulate air pollution (PM2.5) in the United States has fallen by roughly half since 2000, yet linked health outcomes such as diabetes and childhood ADHD have not improved in parallel. One reconciling possibility is that pollution exposure in early life produces health effects that emerge only years or decades later, after pollution itself has declined. Using two decades of U.S. county-level data, we relate...
- Summary (fallback): 机器翻译摘要显示：自 2000 年以来，美国的细颗粒空气污染 (PM2.5) 已下降约一半，但糖尿病和儿童多动症等相关健康结果却并未同步改善。一种可以调和的可能性是，生命早期接触污染会对健康产生影响，这种影响仅在几年或几十年后、污染本身下降后才出现。我们利用二十年的美国县级数据，将年度 PM2.5 估计值与出生结果、糖尿病患病率以及短期和长期范围内儿童注意力缺陷/多动症 (ADHD) 的小区域估计值联系起来。在县内，低出生体重率的变化与同年和出生前一年的 PM2.5 变化相关。
- Keywords: pollution, health, diabetes, adhd, decades

### 18. [非洲和欧洲血统人群中性别和肥胖分层哮喘 GWAS](https://www.medrxiv.org/content/10.64898/2026.07.05.26357321v1)
- Original title: Sex and Obesity Stratified Asthma GWAS in African and European Ancestry Populations
- Authors: Qu, H.-Q., March, M., Mentch, F., Qiu, H., Connolly, J. J. et al.
- Meta: 2026-07-07 | respiratory medicine | DOI: 10.64898/2026.07.05.26357321
- 中文摘要: 背景：当作为单一表型进行分析时，生物学上不同的哮喘亚组可能会掩盖遗传效应。我们研究了哮喘易感性信号在不同血统、肥胖状况和性别之间是否具有共享性、异质性或阶层特异性。方法：我们对非洲血统参与者（9,965 例哮喘病例；37,391 名对照）和欧洲血统参与者（6,074 例；116,255 名对照）进行了血统特异性 GWAS 荟萃分析，然后进行肥胖和性别分层分析。分析使用了祖先内的推算剂量和固定效应荟萃分析。结果：分层检测到哮喘关联信号在组合表型中不太明显。共享的跨祖先位点涉及上皮抗病毒敏感性和免疫调节，以 CDHR3 和 FOXO1 附近的信号为代表。
- Abstract: Background: Biologically distinct asthma subgroups may obscure genetic effects when analyzed as a single phenotype. We examined whether asthma susceptibility signals are shared, heterogeneous, or stratum-specific across ancestry, obesity status, and sex. Methods: We performed ancestry-specific GWAS meta-analyses in African ancestry participants (9,965 asthma cases; 37,391 controls) and European ancestry participants...
- Summary (fallback): 机器翻译摘要显示：背景：当作为单一表型进行分析时，生物学上不同的哮喘亚组可能会掩盖遗传效应。我们研究了哮喘易感性信号在不同血统、肥胖状况和性别之间是否具有共享性、异质性或阶层特异性。方法：我们对非洲血统参与者（9,965 例哮喘病例；37,391 名对照）和欧洲血统参与者（6,074 例；116,255 名对照）进行了血统特异性 GWAS 荟萃分析，然后进行肥胖和性别分层分析。分析使用了祖先内的推算剂量和固定效应荟萃分析。结果：分层检测到哮喘关联信号在组合表型中不太明显。共享的跨祖先位点涉及上皮抗病毒敏感性和免疫调节，以 CDHR3 和 FOXO1 附近的信号为代表。
- Keywords: asthma, obesity, ancestry, signals, susceptibility

### 19. [抗 Ro-52 阳性与抗合成酶综合征患者心血管结局的关系](https://www.medrxiv.org/content/10.64898/2026.07.04.26357290v1)
- Original title: Association of anti-Ro-52 positivity with cardiovascular outcomes in patients with anti-synthetase syndrome
- Authors: Potharazu, A. V., Chung, J.-H., Yanek, L., Kelly, W., Gilotra, N. et al.
- Meta: 2026-07-07 | rheumatology | DOI: 10.64898/2026.07.04.26357290
- 中文摘要: 背景：抗合成酶综合征（ASyS）是特发性炎症性肌病的一个亚组，越来越多地被认为是一种具有肌炎、间质性肺疾病、炎症性关节炎和雷诺现象特征的独特实体。与抗 Ro-52（一种针对 Ro-52 E3 泛素连接酶的抗体）的共反应性已被证明与该患者群体中的进行性间质性肺疾病相关。然而，关于抗 Ro-52 阳性与心血管结局的关系知之甚少。
- Abstract: Background: Anti-synthetase syndrome (ASyS) is a subgroup of idiopathic inflammatory myopathies that is increasingly recognized as a distinct entity with features of myositis, interstitial lung disease, inflammatory arthritis, and Raynaud phenomenon. Co-reactivity with anti-Ro-52, an antibody directed against the Ro-52 E3 ubiquitin ligase, has been shown to be associated with progressive interstitial lung disease wi...
- Summary (fallback): 机器翻译摘要显示：背景：抗合成酶综合征（ASyS）是特发性炎症性肌病的一个亚组，越来越多地被认为是一种具有肌炎、间质性肺疾病、炎症性关节炎和雷诺现象特征的独特实体。与抗 Ro-52（一种针对 Ro-52 E3 泛素连接酶的抗体）的共反应性已被证明与该患者群体中的进行性间质性肺疾病相关。然而，关于抗 Ro-52 阳性与心血管结局的关系知之甚少。
- Keywords: anti-ro-52, positivity, outcomes, patients, cardiovascular

### 20. [老年男性内源性睾酮、C 反应蛋白和白细胞介素 6 之间的纵向关联：巴尔的摩衰老纵向研究的结果](https://www.medrxiv.org/content/10.64898/2026.06.25.26356580v1)
- Original title: Longitudinal Associations Between Endogenous Testosterone, C-Reactive Protein, and Interleukin-6 in Aging Men: Findings from the Baltimore Longitudinal Study of Aging
- Authors: Sureshkumar, K., Grewal, M. R., Gurayah, A., Williams, A., Dubin, J. et al.
- Meta: 2026-07-07 | sexual and reproductive health | DOI: 10.64898/2026.06.25.26356580
- 中文摘要: 背景：C反应蛋白（CRP）、白细胞介素6（IL-6）和睾酮缺乏升高与高龄和慢性炎症性疾病有关；而正常的睾酮水平已被证明可以通过多种机制减少炎症。横断面研究表明 CRP、IL-6 和总睾酮 (TT) 水平之间存在负相关关系，但当考虑代谢综合征的各个组成部分时，报告的结果不一。我们利用巴尔的摩纵向衰老研究评估了 2004 年至 2018 年男性 CRP、IL-6 和 TT 水平之间的关系，以确定低睾酮状态是否与高炎症状况相关。方法：参与者选自巴尔的摩老龄化纵向研究。我们的队列中包括至少 3 次就诊期间测量血清 TT 水平的男性参与者。
- Abstract: Background: Elevated C-Reactive Protein (CRP), interleukin-6 (IL-6) and testosterone deficiency are associated with advanced age and chronic inflammatory diseases; while normal testosterone levels have been shown to decrease inflammation through several mechanisms. Cross-sectional studies have shown an inverse relationship between CRP, IL-6 and total testosterone (TT) levels, yet mixed findings have been reported wh...
- Summary (fallback): 机器翻译摘要显示：背景：C反应蛋白（CRP）、白细胞介素6（IL-6）和睾酮缺乏升高与高龄和慢性炎症性疾病有关；而正常的睾酮水平已被证明可以通过多种机制减少炎症。横断面研究表明 CRP、IL-6 和总睾酮 (TT) 水平之间存在负相关关系，但当考虑代谢综合征的各个组成部分时，报告的结果不一。我们利用巴尔的摩纵向衰老研究评估了 2004 年至 2018 年男性 CRP、IL-6 和 TT 水平之间的关系，以确定低睾酮状态是否与高炎症状况相关。方法：参与者选自巴尔的摩老龄化纵向研究。我们的队列中包括至少 3 次就诊期间测量血清 TT 水平的男性参与者。
- Keywords: levels, associated, il-6, testosterone, inflammatory

### 21. [乌干达城市家庭性别暴力的发生率和预测因素及其对妇女生殖健康寻求行为的影响](https://www.medrxiv.org/content/10.64898/2026.07.05.26355955v1)
- Original title: Prevalence and Predictors of Domestic Gender-Based Violence and Its Impact on Women's Reproductive Health-Seeking Behavior in Urban Uganda
- Authors: SHARIF, K., Elizabeth, N.
- Meta: 2026-07-07 | sexual and reproductive health | DOI: 10.64898/2026.07.05.26355955
- 中文摘要: 家庭性别暴力（DGBV）仍然是一个主要的公共卫生问题，它损害了妇女的性健康和生殖健康（SRH）。本研究评估了 DGBV 对乌干达坎帕拉区 Lusaaze 地区育龄妇女寻求性健康和生殖健康行为的影响。通过系统随机抽样选取 383 名 15 至 49 岁的女性，采用定量横断面描述性相关设计。使用描述性统计、卡方检验和修正泊松回归对数据进行分析。 DGBV 的患病率很高，61.6% 的女性报告曾遭受过公开羞辱，60.0% 的女性报告过身体暴力，59.0% 的女性报告过强迫性交，45.1% 的女性报告遭受过经济排斥。接触过 DGBV 的女性报告伴侣预防艾滋病毒服务的可能性几乎是女性的两倍（66.8% vs. 35.2%；p < 0.001）。
- Abstract: Domestic gender-based violence (DGBV) remains a major public health concern that undermines womens sexual and reproductive health (SRH). This study assessed the influence of DGBV on SRH-seeking behavior among women of reproductive age in the Lusaaze Zone, Kampala District, Uganda. A quantitative cross-sectional descriptive-correlational design was employed among 383 women aged 15 to 49 years selected through systema...
- Summary (fallback): 机器翻译摘要显示：家庭性别暴力（DGBV）仍然是一个主要的公共卫生问题，它损害了妇女的性健康和生殖健康（SRH）。本研究评估了 DGBV 对乌干达坎帕拉区 Lusaaze 地区育龄妇女寻求性健康和生殖健康行为的影响。通过系统随机抽样选取 383 名 15 至 49 岁的女性，采用定量横断面描述性相关设计。使用描述性统计、卡方检验和修正泊松回归对数据进行分析。 DGBV 的患病率很高，61.6% 的女性报告曾遭受过公开羞辱，60.0% 的女性报告过身体暴力，59.0% 的女性报告过强迫性交，45.1% 的女性报告遭受过经济排斥。接触过 DGBV 的女性报告伴侣预防艾滋病毒服务的可能性几乎是女性的两倍（66.8% vs. 35.2%；p < 0.001）。
- Keywords: dgbv, women, violence, reporting, reproductive

### 22. [研究和指导研讨会强调对非洲医学生和早期职业医生的形成性反馈的教育影响](https://www.medrxiv.org/content/10.1101/2023.11.03.23298036v2)
- Original title: Educational Impact of a Research and Mentoring Symposium Emphasizing Formative Feedback for Medical Students and Early Career Doctors in Africa
- Authors: Nowbuth, A. A., Muwowo, M., Makashinyi, M., Kumwenda, A., Mwanamwampula, S. J. et al.
- Meta: 2026-07-07 | medical education | DOI: 10.1101/2023.11.03.23298036
- 中文摘要: 摘要 研究培训是医学教育的核心组成部分，但许多非洲医学院缺乏支持学生研究的资源，阻碍了全球卫生进步。会议提供了了解研究、建立人际网络和接收科学反馈的替代场所，但非洲学员参加会议的机会有限。我们假设为非洲医学实习生举办的研究和指导研讨会可以促进与会者的研究知识和兴趣。方法 我们共同组织了一次研讨会，由来自非洲机构的医学生和早期职业医生亲自（赞比亚卢萨卡）和虚拟参加。该项目以学员摘要演示、主题演讲和交流为特色。摘要收到书面评论，评委对演示提供实时形成性反馈。
- Abstract: Summary Research training is a core component of medical education, but many African medical schools lack resources to support student research, impeding global health progress. Conferences offer alternate venues to learn about research, network, and receive scientific feedback, but conference access for African trainees is limited. We hypothesized that a research and mentorship symposium for African medical trainee...
- Summary (fallback): 机器翻译摘要显示：摘要 研究培训是医学教育的核心组成部分，但许多非洲医学院缺乏支持学生研究的资源，阻碍了全球卫生进步。会议提供了了解研究、建立人际网络和接收科学反馈的替代场所，但非洲学员参加会议的机会有限。我们假设为非洲医学实习生举办的研究和指导研讨会可以促进与会者的研究知识和兴趣。方法 我们共同组织了一次研讨会，由来自非洲机构的医学生和早期职业医生亲自（赞比亚卢萨卡）和虚拟参加。该项目以学员摘要演示、主题演讲和交流为特色。摘要收到书面评论，评委对演示提供实时形成性反馈。
- Keywords: research, african, medical, symposium, trainees

### 23. [急诊科头痛治疗后记录的疼痛缓解结果不稳定：重新评估时间、缺失和评分选择](https://www.medrxiv.org/content/10.64898/2026.07.05.26357324v1)
- Original title: Documented Pain Relief After Emergency Department Headache Treatment Is Not a Stable Outcome: Reassessment Timing, Missingness, and Score Selection
- Authors: Gorenshtein, A., Adiniaev, Y., Liba, T., Klang, E., Daniel, O.
- Meta: 2026-07-07 | neurology | DOI: 10.64898/2026.07.05.26357324
- 中文摘要: 背景：从记录中读取急诊科 (ED) 治疗后患者的疼痛是否有所改善，以对 ED 进行基准测试、比较药物并标记研究结果。仅当治疗后评分被记录、适当计时并按固定规则选择时才可解释；其在这些选择中的稳定性尚不清楚。方法：在去识别的 ED 数据库（MIMIC-IV-ED，2011-2019）中对成人头痛就诊进行回顾性测量研究。在接受治疗的就诊中，我们按时间窗口量化了重新评估的完整性，根据评分选择规则和缺失数据假设估计了有意义的缓解（至少减少 2 分），测试了治疗时重新评估是否可预测，并将头痛与其他疼痛表现进行了比较。结果：在 19,501 次就诊（15,273 名患者）中，13,682 名患者（70.2%）接受了治疗。
- Abstract: Background: Whether a patient's pain improved after emergency department (ED) treatment is read from the record to benchmark EDs, compare drugs, and label research outcomes. It is interpretable only if a post-treatment score is recorded, appropriately timed, and chosen by a fixed rule; its stability across these choices is unknown. Methods: Retrospective measurement study of adult headache visits in a de-identified...
- Summary (fallback): 机器翻译摘要显示：背景：从记录中读取急诊科 (ED) 治疗后患者的疼痛是否有所改善，以对 ED 进行基准测试、比较药物并标记研究结果。仅当治疗后评分被记录、适当计时并按固定规则选择时才可解释；其在这些选择中的稳定性尚不清楚。方法：在去识别的 ED 数据库（MIMIC-IV-ED，2011-2019）中对成人头痛就诊进行回顾性测量研究。在接受治疗的就诊中，我们按时间窗口量化了重新评估的完整性，根据评分选择规则和缺失数据假设估计了有意义的缓解（至少减少 2 分），测试了治疗时重新评估是否可预测，并将头痛与其他疼痛表现进行了比较。结果：在 19,501 次就诊（15,273 名患者）中，13,682 名患者（70.2%）接受了治疗。
- Keywords: relief, reassessment, score, pain, headache

### 24. [罕见癌症的多时间点风险分层：根据已发表的尤文肉瘤试验数据进行验证的计算框架](https://www.medrxiv.org/content/10.64898/2026.07.03.26357236v1)
- Original title: Multi-Timepoint Risk Stratification in Rare Cancers: A Computational Framework Validated against Published Ewing Sarcoma Trial Data
- Authors: Kress, J.
- Meta: 2026-07-07 | oncology | DOI: 10.64898/2026.07.03.26357236
- 中文摘要: 三位观众——新诊断尤文肉瘤患者的家人、长期幸存者和合作组试验统计学家——收到了患者级别问题的队列平均答案，因为罕见癌症不存在机器学习所需的患者级别数据。我们提出了一个框架，可以根据已发布的汇总试验数据生成患者级别的预测。六阶段离散事件蒙特卡罗模拟将遗传风险因素、具有基因型条件加权的系列生物标志物动态、术后基于 ctDNA 的微小残留病 (ctDNA-MRD) 评估以及与治疗相关的死亡率作为可分离的竞争风险相结合。不良反应模块预测了化疗和放射暴露在五个器官系统中的 30 年发病率。
- Abstract: Three audiences -- the family of a newly diagnosed Ewing sarcoma patient, the long-term survivor, and the cooperative-group trial statistician -- receive cohort-mean answers to patient-level questions because the patient-level data machine learning requires do not exist for rare cancers. We present a framework producing patient-level predictions from published aggregate trial data. A six-stage discrete-event Monte C...
- Summary (fallback): 机器翻译摘要显示：三位观众——新诊断尤文肉瘤患者的家人、长期幸存者和合作组试验统计学家——收到了患者级别问题的队列平均答案，因为罕见癌症不存在机器学习所需的患者级别数据。我们提出了一个框架，可以根据已发布的汇总试验数据生成患者级别的预测。六阶段离散事件蒙特卡罗模拟将遗传风险因素、具有基因型条件加权的系列生物标志物动态、术后基于 ctDNA 的微小残留病 (ctDNA-MRD) 评估以及与治疗相关的死亡率作为可分离的竞争风险相结合。不良反应模块预测了化疗和放射暴露在五个器官系统中的 30 年发病率。
- Keywords: patient-level, risk, rare, framework, published

### 25. [Exportin 1 抑制剂 Selinexor 联合放化疗治疗新诊断胶质母细胞瘤患者的 I 期剂量递增](https://www.medrxiv.org/content/10.64898/2026.06.25.26356263v1)
- Original title: Phase I dose escalation of the Exportin 1 inhibitor, Selinexor, in combination with chemoradiation in patients with newly diagnosed glioblastoma
- Authors: Camphausen, K., Mathen, P., Chaudhry, H., Mackey, M., Cooley, T. et al.
- Meta: 2026-07-07 | oncology | DOI: 10.64898/2026.06.25.26356263
- 中文摘要: 目的：胶质母细胞瘤 (GBM) 仍然与不良预后相关，大多数复发发生在高剂量辐射场内，表明存在持续的放射抗性。 Selinexor 抑制输出蛋白 1 (XPO1) 已在临床前模型中证明具有放射增敏作用。我们进行了一项 I 期试验，以评估 Selinexor 联合标准放化疗治疗新诊断 GBM 的安全性、耐受性和初步疗效。方法：这项研究者发起的 I 期剂量递增试验（3+3 设计）招募了新诊断的 GBM 或神经胶质肉瘤的成人。患者接受标准放疗（60 Gy，分 30 次），同时使用替莫唑胺和递增剂量的 Selinexor。评估了三个剂量水平：每周 80 毫克（第 1、2、4、5 周）； 60 mg 每周两次（第 1、2、4、5 周）；放疗期间每周两次（第 1-6 周）60 毫克。
- Abstract: Purpose: Glioblastoma (GBM) remains associated with poor outcomes, with most recurrences occurring within the high-dose radiation field, suggesting persistent radioresistance. Exportin 1 (XPO1) inhibition with Selinexor has demonstrated radiosensitizing effects in preclinical models. We conducted a phase I trial to evaluate the safety, tolerability, and preliminary efficacy of Selinexor in combination with standard...
- Summary (fallback): 机器翻译摘要显示：目的：胶质母细胞瘤 (GBM) 仍然与不良预后相关，大多数复发发生在高剂量辐射场内，表明存在持续的放射抗性。 Selinexor 抑制输出蛋白 1 (XPO1) 已在临床前模型中证明具有放射增敏作用。我们进行了一项 I 期试验，以评估 Selinexor 联合标准放化疗治疗新诊断 GBM 的安全性、耐受性和初步疗效。方法：这项研究者发起的 I 期剂量递增试验（3+3 设计）招募了新诊断的 GBM 或神经胶质肉瘤的成人。患者接受标准放疗（60 Gy，分 30 次），同时使用替莫唑胺和递增剂量的 Selinexor。评估了三个剂量水平：每周 80 毫克（第 1、2、4、5 周）； 60 mg 每周两次（第 1、2、4、5 周）；放疗期间每周两次（第 1-6 周）60 毫克。
- Keywords: selinexor, patients, weekly, weeks, dose

### 26. [冈比亚城乡人群镰状细胞病人口统计学和临床​​流行病学回顾性分析](https://www.medrxiv.org/content/10.64898/2026.07.03.26357219v1)
- Original title: Sickle Cell Disease Demographics and Clinical Epidemiology in Gambian Urban and Rural Cohorts Retrospective Analysis
- Authors: Dibbasey, M., Esoh, K., Susso, B., Forrest, K., Sonko, B. et al.
- Meta: 2026-07-07 | genetic and genomic medicine | DOI: 10.64898/2026.07.03.26357219
- 中文摘要: 全球范围内，约 75% 的镰状细胞病 (SCD) 病例发生在撒哈拉以南非洲地区，但该地区有关其自然史、临床负担和修饰因素的经验数据仍然很少。这项回顾性研究描述了人口特征、并发症和常规护理，并研究了非遗传因素和血液标志物与疾病严重程度的关系。我们分析了在 MRCG Keneba 和 Fajara 诊所注册的 840 名确诊 HbSS 基因型的 SCD 患者的 8402 份医疗记录（NKeneba=148；NFajara=692）。采用广义线性模型来估计非遗传相关因素、血液生物标志物和常规护理药物与疾病严重程度的关联。在这里，我们显示 Keneba 队列中 67% 的患者和 Fajara 队列中 92% 的患者没有记录到的 SCD 相关慢性并发症。
- Abstract: Globally, approximately 75% of sickle cell disease (SCD) cases occur in sub-Saharan Africa, yet empirical data on its natural history, clinical burden, and modifiers remain scarce in the region. This retrospective study describes the demographic characteristics, complications, and routine care and examines how non-genetic factors and blood markers relate to disease severity. We analysed 8402 medical records from 840...
- Summary (fallback): 机器翻译摘要显示：全球范围内，约 75% 的镰状细胞病 (SCD) 病例发生在撒哈拉以南非洲地区，但该地区有关其自然史、临床负担和修饰因素的经验数据仍然很少。这项回顾性研究描述了人口特征、并发症和常规护理，并研究了非遗传因素和血液标志物与疾病严重程度的关系。我们分析了在 MRCG Keneba 和 Fajara 诊所注册的 840 名确诊 HbSS 基因型的 SCD 患者的 8402 份医疗记录（NKeneba=148；NFajara=692）。采用广义线性模型来估计非遗传相关因素、血液生物标志物和常规护理药物与疾病严重程度的关联。在这里，我们显示 Keneba 队列中 67% 的患者和 Fajara 队列中 92% 的患者没有记录到的 SCD 相关慢性并发症。
- Keywords: disease, clinical, keneba, fajara, crises

### 27. [在赢家诅咒、样本结构和多基因性下重新校准孟德尔随机化](https://www.medrxiv.org/content/10.64898/2026.06.25.26356593v1)
- Original title: Recalibrating Mendelian randomization under winner's curse, sample structure and polygenicity
- Authors: Yang, Y., Lin, Z., Xue, H., Zhu, X.
- Meta: 2026-07-07 | genetic and genomic medicine | DOI: 10.64898/2026.06.25.26356593
- 中文摘要: 最近，胡等人。 (2024) 进行的一项基准研究表明，大多数现有的孟德尔随机化 (MR) 方法在实际数据中表现出很大的偏差和夸大的 I 类错误率。他们将这些失败归因于两个很大程度上被忽视的偏见来源：赢家的诅咒和多基因引起的偏见。尽管已经开发了一些方法来解决其中一个或两个问题，但现有方法要么没有完全考虑这两种偏差，要么仅限于单变量设置。在本文中，我们提出了一种多变量 Rao-Blackwellization，它可以纠正赢家的诅咒，同时在统一框架中考虑多基因性和样本结构。
- Abstract: Recently, Hu et al. (2024) conducted a benchmarking study showing that most existing Mendelian randomization (MR) methods exhibit substantial bias and inflated type-I error rates in real data. They attributed these failures to two largely neglected sources of bias: winner's curse and polygenicity-induced bias. Although a few methods have been developed to address one or both of these issues, existing approaches eith...
- Summary (fallback): 机器翻译摘要显示：最近，胡等人。 (2024) 进行的一项基准研究表明，大多数现有的孟德尔随机化 (MR) 方法在实际数据中表现出很大的偏差和夸大的 I 类错误率。他们将这些失败归因于两个很大程度上被忽视的偏见来源：赢家的诅咒和多基因引起的偏见。尽管已经开发了一些方法来解决其中一个或两个问题，但现有方法要么没有完全考虑这两种偏差，要么仅限于单变量设置。在本文中，我们提出了一种多变量 Rao-Blackwellization，它可以纠正赢家的诅咒，同时在统一框架中考虑多基因性和样本结构。
- Keywords: methods, winner, curse, existing, bias

### 28. [围绝经期隐藏的生产力损失：女性黄金工作时期症状驱动的工作障碍](https://www.medrxiv.org/content/10.64898/2026.07.05.26357306v1)
- Original title: The hidden productivity toll of perimenopause: symptom-driven work impairment during women's prime working years
- Authors: Xu, Y., Prentice, C., Hewings-Martin, Y., Cunningham, A. C., Zhaunova, L. et al.
- Meta: 2026-07-07 | health economics | DOI: 10.64898/2026.07.05.26357306
- 中文摘要: 围绝经期女性通常处于职业生涯的黄金时期，在劳动力中占很大比例。之前的研究已经揭示了与围绝经期相关的显着症状负担，但其工作场所和经济后果仍然知之甚少。我们使用工作生产力和活动障碍问卷以及更年期评定量表，对 35-59 岁美国女性 (n=945) 进行了一项横断面调查，按症状严重程度和跨生育阶段检查了工作障碍。然后，我们使用人力资本方法估计了相关的生产力损失。围绝经期妇女与绝经前妇女一样有可能继续留在劳动力队伍中（76.6% vs. 78.0%），但报告的工作障碍要高得多（22.5% vs. 12.7%）。
- Abstract: Perimenopausal women, often in the prime of their careers, make up a significant proportion of the workforce. Previous studies have revealed the significant symptoms burden associated with perimenopause, yet its workplace and economic consequences remain poorly understood. We examined work impairment by symptom severity and across reproductive stages in a cross-sectional survey of U.S. women aged 35-59 (n=945), usin...
- Summary (fallback): 机器翻译摘要显示：围绝经期女性通常处于职业生涯的黄金时期，在劳动力中占很大比例。之前的研究已经揭示了与围绝经期相关的显着症状负担，但其工作场所和经济后果仍然知之甚少。我们使用工作生产力和活动障碍问卷以及更年期评定量表，对 35-59 岁美国女性 (n=945) 进行了一项横断面调查，按症状严重程度和跨生育阶段检查了工作障碍。然后，我们使用人力资本方法估计了相关的生产力损失。围绝经期妇女与绝经前妇女一样有可能继续留在劳动力队伍中（76.6% vs. 78.0%），但报告的工作障碍要高得多（22.5% vs. 12.7%）。
- Keywords: work, impairment, women, productivity, perimenopause

### 29. [相同的输入，不同的 EDSS：测量临床评分流程中的规范漂移](https://www.medrxiv.org/content/10.64898/2026.06.25.26356350v1)
- Original title: Same Inputs, Different EDSS: Measuring Specification Drift in Clinical Scoring Pipelines
- Authors: Hwang, S., Mowery, D. L., Thomas, S., Williams, H., Bar-Or, A. et al.
- Meta: 2026-07-07 | health informatics | DOI: 10.64898/2026.06.25.26356350
- 中文摘要: 临床信息学管道越来越多地从上游 NLP 输出计算经过验证的临床终点。即使端点是由既定的标准定义的，跨表示形式（自然语言指令、程序逻辑和参考实现）转换该标准也可能会引入规范漂移，其中表面上等效的计算器会产生有意义的不同分数。我们通过扩展残疾状态量表（EDSS）研究这种现象，这是多发性硬化症残疾的标准衡量标准。保持由大型语言模型 (LLM) 提取的共享功能系统 (FS) 子分数集不变，我们比较跨同一评分标准的三种表示计算的 EDSS 值：提示执行的自然语言、LLM 生成的代码和规范参考实现。
- Abstract: Clinical informatics pipelines increasingly compute validated clinical endpoints from upstream NLP outputs. Even when the endpoint is defined by an established rubric, translating that rubric across representations - natural language instructions, program logic, and reference implementations - can introduce specification drift, where ostensibly equivalent calculators yield meaningfully different scores. We study thi...
- Summary (fallback): 机器翻译摘要显示：临床信息学管道越来越多地从上游 NLP 输出计算经过验证的临床终点。即使端点是由既定的标准定义的，跨表示形式（自然语言指令、程序逻辑和参考实现）转换该标准也可能会引入规范漂移，其中表面上等效的计算器会产生有意义的不同分数。我们通过扩展残疾状态量表（EDSS）研究这种现象，这是多发性硬化症残疾的标准衡量标准。保持由大型语言模型 (LLM) 提取的共享功能系统 (FS) 子分数集不变，我们比较跨同一评分标准的三种表示计算的 EDSS 值：提示执行的自然语言、LLM 生成的代码和规范参考实现。
- Keywords: clinical, edss, rubric, language, same

### 30. [什么都看不见，什么都说：组织病理学双子座模型中缺乏视觉基础和虚构](https://www.medrxiv.org/content/10.64898/2026.07.04.26357257v1)
- Original title: Seeing Nothing, Saying Something: The Lack of Visual Grounding and Confabulation in Gemini Models for Histopathology
- Authors: Hasan, M. M., Tozal, M. E., Ayhan, M. S.
- Meta: 2026-07-07 | health informatics | DOI: 10.64898/2026.07.04.26357257
- 中文摘要: 大型视觉语言模型（VLM）在计算病理学基准上表现出了卓越的性能，但它们在对抗性或空洞输入下的可靠性仍然知之甚少。本文研究了两个 Gemini 模型 Gemini 3.0 Flash Preview (gemini-flash) 和 Gemini 3.1 Pro Preview (gemini-pro) 在一项众所周知的组织病理学分类任务上的视觉基础行为，并使用对抗性空白图像集探讨了混淆。在真实的组织病理学数据集上，两个模型在三个温度（0.0、0.5、1.0）和三个独立运行中均实现了近乎完美的准确度（98.75% - 100%）。然而，在一组被标记为良性或恶性的受控对抗性空白白色图像上，出现了明显的分歧。
- Abstract: Large vision-language models (VLMs) have demonstrated remarkable perfor- mance on computational pathology benchmarks, yet their reliability under adversarial or vacuous inputs remains poorly understood. This paper examines the visual grounding behaviour of two Gemini models Gemini 3.0 Flash Pre- view (gemini-flash) and Gemini 3.1 Pro Preview (gemini-pro) on a well known histopathology classification task, and probes...
- Summary (fallback): 机器翻译摘要显示：大型视觉语言模型（VLM）在计算病理学基准上表现出了卓越的性能，但它们在对抗性或空洞输入下的可靠性仍然知之甚少。本文研究了两个 Gemini 模型 Gemini 3.0 Flash Preview (gemini-flash) 和 Gemini 3.1 Pro Preview (gemini-pro) 在一项众所周知的组织病理学分类任务上的视觉基础行为，并使用对抗性空白图像集探讨了混淆。在真实的组织病理学数据集上，两个模型在三个温度（0.0、0.5、1.0）和三个独立运行中均实现了近乎完美的准确度（98.75% - 100%）。然而，在一组被标记为良性或恶性的受控对抗性空白白色图像上，出现了明显的分歧。
- Keywords: confabulation, gemini, models, visual, histopathology
