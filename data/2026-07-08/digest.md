# daily2rxiv Digest - 2026-07-08

共收录 68 篇论文。

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
- 中文摘要: 视觉-语言-动作（VLA）模型已成为通用机器人操作的一种有前景的方法。特别是，基于流匹配的 VLA 模型由于能够生成精确且平滑的动作序列并捕获多模态分布而取得了显着的成功。然而，动作头中的迭代去噪过程是主要的计算瓶颈，对实时部署提出了严峻的挑战。为了应对这一挑战，我们提出了 ActionCache，这是一种即插即用的外部缓存，它可以机会性地重用过去的中间操作，以从目标操作附近热启动生成，从而大大减少推理延迟。具体来说，ActionCache 使用紧凑的多模式键存储中间操作，这使得可以从不同情节甚至不同任务的类似过去​​上下文中进行检索。
- Abstract: Vision-Language-Action (VLA) models have emerged as a promising approach for generalizable robotic manipulations. In particular, flow matching-based VLA models have shown remarkable success due to their capability to generate precise and smooth action sequences and capture multimodal distributions. However, the iterative denoising process in the action head acts as a major computational bottleneck, posing a critical...
- Summary (fallback): 机器翻译摘要显示：视觉-语言-动作（VLA）模型已成为通用机器人操作的一种有前景的方法。特别是，基于流匹配的 VLA 模型由于能够生成精确且平滑的动作序列并捕获多模态分布而取得了显着的成功。然而，动作头中的迭代去噪过程是主要的计算瓶颈，对实时部署提出了严峻的挑战。为了应对这一挑战，我们提出了 ActionCache，这是一种即插即用的外部缓存，它可以机会性地重用过去的中间操作，以从目标操作附近热启动生成，从而大大减少推理延迟。具体来说，ActionCache 使用紧凑的多模式键存储中间操作，这使得可以从不同情节甚至不同任务的类似过去​​上下文中进行检索。
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

### 1. [晚期糖基化终末产物 (AGE) 对人类神经肌肉接头共培养模型的有害影响](https://www.biorxiv.org/content/10.64898/2026.07.07.736594v1)
- Original title: Detrimental effects of advanced glycation end-products (AGEs) on a human neuromuscular junction co-culture model
- Authors: Alomosh, R., Bateman, A., Mamchaoui, K., Mouly, V., Lightfoot, A. P. et al.
- Meta: 2026-07-08 | cell biology | DOI: 10.64898/2026.07.07.736594
- 中文摘要: 神经肌肉接头（NMJ）是运动神经元和骨骼肌之间的特殊突触，其逐渐恶化会导致与年龄相关和代谢疾病相关的肌肉功能下降。晚期糖基化终产物 (AGE) 在衰老、糖尿病和慢性代谢功能障碍期间在组织中积累，并与神经肌肉变性有关，但它们对完整 NMJ 的影响此前尚未在人体模型系统中进行过研究。本研究采用完全人源、无血清、无神经生长因子的 NMJ 共培养系统，将神经祖细胞与来自 83 岁捐赠者的永生化人成肌细胞相结合，以研究 AGE 暴露对神经肌肉完整性在结构、代谢、功能和分泌结果方面的影响。
- Abstract: The neuromuscular junction (NMJ) is a specialised synapse between motor neurons and skeletal muscle, and its progressive deterioration contributes to age-related and metabolic disease-associated declines in muscle function. Advanced glycation end-products (AGEs) accumulate in tissues during ageing, diabetes, and chronic metabolic dysfunction and have been implicated in neuromuscular degeneration, yet their effects o...
- Summary (fallback): 机器翻译摘要显示：神经肌肉接头（NMJ）是运动神经元和骨骼肌之间的特殊突触，其逐渐恶化会导致与年龄相关和代谢疾病相关的肌肉功能下降。晚期糖基化终产物 (AGE) 在衰老、糖尿病和慢性代谢功能障碍期间在组织中积累，并与神经肌肉变性有关，但它们对完整 NMJ 的影响此前尚未在人体模型系统中进行过研究。本研究采用完全人源、无血清、无神经生长因子的 NMJ 共培养系统，将神经祖细胞与来自 83 岁捐赠者的永生化人成肌细胞相结合，以研究 AGE 暴露对神经肌肉完整性在结构、代谢、功能和分泌结果方面的影响。
- Keywords: human, neuromuscular, effects, glycation, co-culture

### 2. [Nuclear-BRITE：用于核 RNA 活细胞成像的增强型 MS2 系统](https://www.biorxiv.org/content/10.64898/2026.07.07.736975v1)
- Original title: Nuclear-BRITE: an enhanced MS2 system for live-cell imaging of nuclear RNAs
- Authors: Cawte, A. D., Cihlova, B., Brockdorff, N.
- Meta: 2026-07-08 | cell biology | DOI: 10.64898/2026.07.07.736975
- 中文摘要: MS2 系统已广泛用于 mRNA 的活细胞单分子成像，但由于过量的核定位荧光衣壳蛋白，其对细胞核中存在的 RNA 的适用性有限。在这里，我们描述了 Nuclear-BRITE，这是一种减少核背景信号的改进方法，能够以单分子分辨率对各种内源标记核 RNA 进行快速活细胞成像，而不干扰其丰度、定位或功能。
- Abstract: The MS2 system has been widely adopted for live-cell single molecule imaging of mRNA, but is of limited applicability for RNAs present in the cell nucleus due to excess nuclear-localised fluorescent capsid protein. Here we describe Nuclear-BRITE, an improved methodology that reduces nuclear background signal, enabling fast live-cell imaging of a wide range of endogenously tagged nuclear RNAs at single-molecule resol...
- Summary (fallback): 机器翻译摘要显示：MS2 系统已广泛用于 mRNA 的活细胞单分子成像，但由于过量的核定位荧光衣壳蛋白，其对细胞核中存在的 RNA 的适用性有限。在这里，我们描述了 Nuclear-BRITE，这是一种减少核背景信号的改进方法，能够以单分子分辨率对各种内源标记核 RNA 进行快速活细胞成像，而不干扰其丰度、定位或功能。
- Keywords: live-cell, imaging, nuclear, rnas, nuclear-brite

### 3. [对全基因组加倍的直接细胞反应在多倍体环境中是保守的](https://www.biorxiv.org/content/10.64898/2026.07.07.736946v1)
- Original title: The immediate cellular response to whole-genome doubling is conserved across polyploid contexts
- Authors: Geerlings, C., Darmasaputra, G., Jordan Ortiz, C., Chuva de Sousa Lopes, S. M., Clevers, H. M. et al.
- Meta: 2026-07-08 | cell biology | DOI: 10.64898/2026.07.07.736946
- 中文摘要: 多倍体细胞含有两个以上基因组拷贝，广泛存在于植物和动物中，通常存在于具有高生物合成和代谢需求的组织中，例如哺乳动物的肝脏和胎盘。虽然体细胞多倍体通常与细胞生长和生物合成能力的增加有关，但通常不被编程为多倍体的细胞类型中的计划外多倍化通常与细胞适应性降低和基因组不稳定有关。为了了解这些不同的结果是否源于细胞对倍性增加的不同直接反应，我们系统地比较了自然发生的和实验诱导的系统中多倍化的早期后果。
- Abstract: Polyploid cells, which contain more than two copies of the genome, are widely present across plants and animals, where they are often found in tissues with high biosynthetic and metabolic demands, such as the mammalian liver and placenta. While somatic polyploidy is frequently associated with increased cell growth and biosynthetic capacity, unscheduled polyploidization in cell types that are not normally programmed...
- Summary (fallback): 机器翻译摘要显示：多倍体细胞含有两个以上基因组拷贝，广泛存在于植物和动物中，通常存在于具有高生物合成和代谢需求的组织中，例如哺乳动物的肝脏和胎盘。虽然体细胞多倍体通常与细胞生长和生物合成能力的增加有关，但通常不被编程为多倍体的细胞类型中的计划外多倍化通常与细胞适应性降低和基因组不稳定有关。为了了解这些不同的结果是否源于细胞对倍性增加的不同直接反应，我们系统地比较了自然发生的和实验诱导的系统中多倍化的早期后果。
- Keywords: polyploid, across, cells, cell, polyploidization

### 4. [北极浮游植物和浮游霉菌的种群动态揭示了壶菌介导的硅藻水华终止](https://www.biorxiv.org/content/10.64898/2026.07.07.736921v1)
- Original title: Population dynamics of Arctic phytoplankton and mycoplankton reveal chytrid-mediated diatom bloom termination
- Authors: Thome, P. C., Oldenburg, E., Hörstmann, C., Strassert, J. F.
- Meta: 2026-07-08 | ecology | DOI: 10.64898/2026.07.07.736921
- 中文摘要: 壶菌是单细胞真菌，作为寄生虫或腐生菌感染并降解浮游植物。它们不仅影响地表水的粮食供应和质量，还影响碳循环和封存。到目前为止，它们的生态意义主要是在淡水环境中进行的研究，而对海洋环境的观测却很少——尽管壶菌在那里也非常丰富（如北冰洋所示）。为了测试壶菌控制北冰洋浮游植物动态的潜力，我们分析了塔拉极地圈和 MOSAiC 两次探险的元条形码和光合色素数据；后者提供了一年内冰下水柱和海冰样本的密集采样样线。
- Abstract: Chytrids are unicellular fungi that infect and degrade phytoplankton as parasites or saprotrophs. They impact not only food availability and quality in surface waters but also carbon cycling and sequestration. So far, their ecological significance has mostly been investigated for freshwater environments, whereas observations for marine environments are scarce -- even though chytrids can be highly abundant there, too...
- Summary (fallback): 机器翻译摘要显示：壶菌是单细胞真菌，作为寄生虫或腐生菌感染并降解浮游植物。它们不仅影响地表水的粮食供应和质量，还影响碳循环和封存。到目前为止，它们的生态意义主要是在淡水环境中进行的研究，而对海洋环境的观测却很少——尽管壶菌在那里也非常丰富（如北冰洋所示）。为了测试壶菌控制北冰洋浮游植物动态的潜力，我们分析了塔拉极地圈和 MOSAiC 两次探险的元条形码和光合色素数据；后者提供了一年内冰下水柱和海冰样本的密集采样样线。
- Keywords: chytrids, phytoplankton, diatom, environments, abundant

### 5. [食草动物和病原体可以调节植物种群对未来气候条件的反应](https://www.biorxiv.org/content/10.64898/2026.07.07.736959v1)
- Original title: Herbivores and pathogens can modulate plant population responses to future climate conditions
- Authors: Andrzejak, M., Knight, T., Korell, L.
- Meta: 2026-07-08 | ecology | DOI: 10.64898/2026.07.07.736959
- 中文摘要: 气候变化预计不仅会通过直接的环境变化，还会通过生物相互作用的变化，例如与食草动物和病原体的相互作用来改变植物种群。由于植物物种对气候和拮抗物的反应也各不相同，因此植物对这两个因素的反应预计是可变的且具有物种特异性。为了评估气候和拮抗剂对植物种群动态的相互作用影响是否常见，以及植物反应的强度和方向是否因物种而异，我们进行了一项多年的田间实验，操纵现实的气候变化，并通过实验减少昆虫食草动物和真菌病原体。我们测量了植物生命率的反应，例如六个草原物种的存活率、生长率和繁殖率。
- Abstract: Climate change is expected to alter plant populations not only through direct environmental shifts but also via changes in biotic interactions, such as with herbivores and pathogens. As plant species are also expected to differ in their responses to both climate and antagonists, plant responses to both factors are expected to be variable and species-specific. To assess whether interactive effects of climate and anta...
- Summary (fallback): 机器翻译摘要显示：气候变化预计不仅会通过直接的环境变化，还会通过生物相互作用的变化，例如与食草动物和病原体的相互作用来改变植物种群。由于植物物种对气候和拮抗物的反应也各不相同，因此植物对这两个因素的反应预计是可变的且具有物种特异性。为了评估气候和拮抗剂对植物种群动态的相互作用影响是否常见，以及植物反应的强度和方向是否因物种而异，我们进行了一项多年的田间实验，操纵现实的气候变化，并通过实验减少昆虫食草动物和真菌病原体。我们测量了植物生命率的反应，例如六个草原物种的存活率、生长率和繁殖率。
- Keywords: plant, climate, responses, population, species

### 6. [对亲脂性染料标记的严格重新评估表明，与无血清培养细胞衍生的小细胞外囊泡的结合可以忽略不计](https://www.biorxiv.org/content/10.64898/2026.07.04.722344v1)
- Original title: Critical reassessment of lipophilic dye labeling reveals negligible incorporation into small extracellular vesicles derived form serum-free cultured cells
- Authors: Ji, Y., Ji, Q., Ji, J., Shentu, Y., Zhou, l. et al.
- Meta: 2026-07-08 | bioengineering | DOI: 10.64898/2026.07.04.722344
- 中文摘要: 亲脂性染料广泛用于追踪细胞外囊泡 (EV)，但其对真正的小型 EV (sEV) 的标记效率仍不清楚。在这里，我们使用无血清 HEK293F 系统批判性地重新评估这种效率，该系统生成内源性荧光蛋白标记的 sEV（sEVs-FPT）作为明确的阳性参考，从而最大限度地减少来自共分离的、可染料标记的非囊泡细胞外颗粒（NVEP）的干扰。采用纳米流式细胞术和荧光显微镜这两种正交方法进行交叉验证。我们发现 PKH26、PKH67 和 DiD 标记的 sEVs-FPT <0.5%，无论囊泡异质性如何。体内追踪证实，染料衍生的信号远弱于 FPT 信号，并且明显无法与它们共定位。
- Abstract: Lipophilic dyes are widely used to track extracellular vesicles (EVs), yet their labeling efficiency toward bona fide small EVs (sEVs) remains poorly defined. Here, we critically reassess this efficiency using a serum-free HEK293F system that generates endogenously fluorescent protein-tagged sEVs (sEVs-FPT) as an unambiguous positive reference, thereby minimizing interference from co-isolated, dye-labelable non-vesi...
- Summary (fallback): 机器翻译摘要显示：亲脂性染料广泛用于追踪细胞外囊泡 (EV)，但其对真正的小型 EV (sEV) 的标记效率仍不清楚。在这里，我们使用无血清 HEK293F 系统批判性地重新评估这种效率，该系统生成内源性荧光蛋白标记的 sEV（sEVs-FPT）作为明确的阳性参考，从而最大限度地减少来自共分离的、可染料标记的非囊泡细胞外颗粒（NVEP）的干扰。采用纳米流式细胞术和荧光显微镜这两种正交方法进行交叉验证。我们发现 PKH26、PKH67 和 DiD 标记的 sEVs-FPT <0.5%，无论囊泡异质性如何。体内追踪证实，染料衍生的信号远弱于 FPT 信号，并且明显无法与它们共定位。
- Keywords: lipophilic, extracellular, sevs, critical, labeling

### 7. [针对鼻疽伯克霍尔德氏菌外膜 β 桶蛋白的人鼻疽多表位疫苗的设计](https://www.biorxiv.org/content/10.64898/2026.05.25.727591v2)
- Original title: Design of a Multi-epitope Vaccine Against Human Glanders Targeting Outer Membrane β-barrel Proteins of Burkholderia mallei
- Authors: Kapoor, J., Panda, A., Kumar, S., Bandyopadhyay, A.
- Meta: 2026-07-08 | bioinformatics | DOI: 10.64898/2026.05.25.727591
- 中文摘要: 鼻疽伯克霍尔德氏菌（Burkholderia mallei）是一种兼性细胞内革兰氏阴性病原体，是鼻疽病的病原体，主要影响单足类动物，并偶尔传播给人类。目前的干预措施主要依靠抗生素；然而，耐药性的增加和缺乏许可的疫苗使疾病管理进一步复杂化。在本研究中，对 B. mallei turkey2 蛋白质组采用了基于共识的计算框架。总共 59 种蛋白质 - 包括孔蛋白、TonB 受体、自转运蛋白和外排成分 - 被鉴定为表面暴露的外膜 {β}-桶 (OMBB) 蛋白质，用于设计多表位疫苗 (MEV) 构建体。
- Abstract: Burkholderia mallei, a facultative intracellular Gram-negative pathogen, is the causative agent of glanders that primarily affects solipeds and sporadically transmitted to humans. Current interventions mainly rely on antibiotics; however, increasing resistance and the lack of a licensed vaccine further complicate disease management. In the present study, a consensus-based computational framework was employed on the...
- Summary (fallback): 机器翻译摘要显示：鼻疽伯克霍尔德氏菌（Burkholderia mallei）是一种兼性细胞内革兰氏阴性病原体，是鼻疽病的病原体，主要影响单足类动物，并偶尔传播给人类。目前的干预措施主要依靠抗生素；然而，耐药性的增加和缺乏许可的疫苗使疾病管理进一步复杂化。在本研究中，对 B. mallei turkey2 蛋白质组采用了基于共识的计算框架。总共 59 种蛋白质 - 包括孔蛋白、TonB 受体、自转运蛋白和外排成分 - 被鉴定为表面暴露的外膜 {β}-桶 (OMBB) 蛋白质，用于设计多表位疫苗 (MEV) 构建体。
- Keywords: proteins, mallei, vaccine, surface, construct

### 8. [单物种单资源环境下微生物生态动力学的最小随机模型](https://www.biorxiv.org/content/10.64898/2026.07.01.735782v2)
- Original title: A Minimal Stochastic Model of Microbial Ecological Dynamics in a Single-Species-Single-Resource Setting
- Authors: Leung, C. F. A., Kolomeisky, A.
- Meta: 2026-07-08 | biophysics | DOI: 10.64898/2026.07.01.735782
- 中文摘要: 由于大量的生化过程、时空相互作用、环境变化和进化压力，微生物表现出复杂的动态行为。尽管在理解微生物生态动力学方面取得了重大进展，但仍然存在多个悬而未决的问题，包括生长的微观机制以及营养物和随机性的作用。在这项工作中，我们提出了一种最小的理论方法来阐明微生物资源消耗与其生长之间的联系。通过分析和蒙特卡罗计算机模拟研究了一个随机模型，该模型解释了单一微生物物种在通过细胞分裂生长时消耗单一类型资源的情况。
- Abstract: Microbes exhibit complex dynamic behavior as the result of a large number of biochemical processes, spatial and temporal interactions, environmental variations, and evolutionary pressure. Although significant progress has been achieved in understanding microbial ecological dynamics, multiple open questions remain, including the microscopic mechanisms of growth and the roles of nutrients and stochasticity. In this wo...
- Summary (fallback): 机器翻译摘要显示：由于大量的生化过程、时空相互作用、环境变化和进化压力，微生物表现出复杂的动态行为。尽管在理解微生物生态动力学方面取得了重大进展，但仍然存在多个悬而未决的问题，包括生长的微观机制以及营养物和随机性的作用。在这项工作中，我们提出了一种最小的理论方法来阐明微生物资源消耗与其生长之间的联系。通过分析和蒙特卡罗计算机模拟研究了一个随机模型，该模型解释了单一微生物物种在通过细胞分裂生长时消耗单一类型资源的情况。
- Keywords: microbial, growth, highwire, dtlvardef, model

### 9. [骨髓增生异常综合征中阿扎胞苷的反应以 NK 样 CD8 T 细胞扩增和 CXCL12+ 网状细胞重塑为标志](https://www.biorxiv.org/content/10.64898/2026.07.07.736922v1)
- Original title: Azacitidine Response in Myelodysplastic Syndromes is Marked by NK-like CD8 T-Cell Expansion and CXCL12+ Reticular Cell Remodeling
- Authors: Hampton, H. R., Pan, A., Carnell, M., Wang, B., Shinko, D. et al.
- Meta: 2026-07-08 | cancer biology | DOI: 10.64898/2026.07.07.736922
- 中文摘要: 骨髓增生异常综合征 (MDS) 由造血干细胞和祖细胞 (HSPC) 的体细胞突变驱动，导致克隆扩张和无效造血。低甲基化药物（HMA；阿扎胞苷或地西他滨）是高危 MDS 的标准治疗方法。然而，它们对骨髓（BM）微环境的影响以及这些变化与临床反应的相关程度仍然知之甚少。我们对临床试验 (NCT03493646) 中接受阿扎胞苷治疗的 MDS 患者的 BM 抽吸物、环钻活检和外周血样本进行了纵向分析，整合了 CyTOF、5' 单细胞 RNA 和 TCR 测序、血浆蛋白质组学和多重免疫荧光显微镜来表征与阿扎胞苷反应相关的变化。
- Abstract: Myelodysplastic syndromes (MDS) are driven by somatic mutations in hematopoietic stem and progenitor cells (HSPCs), leading to clonal expansion and ineffective hematopoiesis. Hypomethylating agents (HMAs; azacitidine or decitabine) are the standard of care for higher-risk MDS. However, their effects on the bone marrow (BM) microenvironment, and the extent to which these changes correlate with clinical response, rema...
- Summary (fallback): 机器翻译摘要显示：骨髓增生异常综合征 (MDS) 由造血干细胞和祖细胞 (HSPC) 的体细胞突变驱动，导致克隆扩张和无效造血。低甲基化药物（HMA；阿扎胞苷或地西他滨）是高危 MDS 的标准治疗方法。然而，它们对骨髓（BM）微环境的影响以及这些变化与临床反应的相关程度仍然知之甚少。我们对临床试验 (NCT03493646) 中接受阿扎胞苷治疗的 MDS 患者的 BM 抽吸物、环钻活检和外周血样本进行了纵向分析，整合了 CyTOF、5' 单细胞 RNA 和 TCR 测序、血浆蛋白质组学和多重免疫荧光显微镜来表征与阿扎胞苷反应相关的变化。
- Keywords: azacitidine, cells, response, expansion, clinical

### 10. [重新编程蛋白质连接酶以扩展遗传密码](https://www.biorxiv.org/content/10.64898/2026.07.07.736966v1)
- Original title: Reprogramming a Protein Ligase for Genetic Code Expansion
- Authors: Gallo, G., Sieber, A., Hellwig, M., Fuerst, M. J. L. J., Lassak, J. M.
- Meta: 2026-07-08 | synthetic biology | DOI: 10.64898/2026.07.07.736966
- 中文摘要: 核糖体的 DNA 编码产生的确定的聚合物序列自然限于 22 个氨基酸。尽管翻译机器具有聚合骨架修饰底物（包括 {β}-氨基酸）的潜在能力，但这种潜力受到天然氨酰基-tRNA 合成酶的内在选择性的限制。在这里，我们通过“逆向工程”大肠杆菌蛋白连接酶 EpmA 来解决这一限制。 EpmA 天然激活 (R)-{β}-赖氨酸，并进化为丢弃其 tRNA 结合域以利于蛋白质识别。通过将经典赖氨酰-tRNA 合成酶 LysRS 的反密码子结合域移植到 EpmA 上，我们创建了嵌合酶 chEpmA。据我们所知，这代表了蛋白质连接酶首次成功重编程为功能性氨酰-tRNA 合成酶。
- Abstract: The ribosome's DNA-encoded production of defined polymer sequences is naturally limited to 22 amino acids. Although the translation machinery has the latent capacity to polymerize backbone-modified substrates, including {beta}-amino acids, this potential is constrained by the intrinsic -selectivity of native aminoacyl-tRNA synthetases. Here, we address this limitation by "reverse engineering" the Escherichia coli pr...
- Summary (fallback): 机器翻译摘要显示：核糖体的 DNA 编码产生的确定的聚合物序列自然限于 22 个氨基酸。尽管翻译机器具有聚合骨架修饰底物（包括 {β}-氨基酸）的潜在能力，但这种潜力受到天然氨酰基-tRNA 合成酶的内在选择性的限制。在这里，我们通过“逆向工程”大肠杆菌蛋白连接酶 EpmA 来解决这一限制。 EpmA 天然激活 (R)-{β}-赖氨酸，并进化为丢弃其 tRNA 结合域以利于蛋白质识别。通过将经典赖氨酰-tRNA 合成酶 LysRS 的反密码子结合域移植到 EpmA 上，我们创建了嵌合酶 chEpmA。据我们所知，这代表了蛋白质连接酶首次成功重编程为功能性氨酰-tRNA 合成酶。
- Keywords: protein, lysine, ligase, substrates, beta

### 11. [核光研究的五年：对趋势、偏见和未来方向的系统回顾](https://www.biorxiv.org/content/10.64898/2026.07.07.736978v1)
- Original title: Five Decades of Rariphotic Research: A Systematic Reviewof Trends, Biases, and Future Directions
- Authors: Haim, A., Eyal, G.
- Meta: 2026-07-08 | zoology | DOI: 10.64898/2026.07.07.736978
- 中文摘要: 缺光区通常跨越约 130 至 300 米的深度，代表依赖光的珊瑚礁生态系统和无光深海之间的关键过渡。尽管其具有潜在的生态重要性，包括其作为遭受气候驱动压力的物种避难所的作用，但人们对松果生态系统仍然知之甚少。在这项研究中，我们对 1970 年至 2025 年有关这些栖息地的科学文献进行了系统回顾和综合。
- Abstract: The rariphotic zone, typically spanning depths of approximately 130 to 300 meters, represents a key transition between light-dependent coral reef ecosystems and the aphotic deep sea. Despite its potential ecological importance, including its proposed role as a refuge for species exposed to climate-driven stress, rariphotic ecosystems remain poorly understood. In this study, we conducted a systematic review and synth...
- Summary (fallback): 机器翻译摘要显示：缺光区通常跨越约 130 至 300 米的深度，代表依赖光的珊瑚礁生态系统和无光深海之间的关键过渡。尽管其具有潜在的生态重要性，包括其作为遭受气候驱动压力的物种避难所的作用，但人们对松果生态系统仍然知之甚少。在这项研究中，我们对 1970 年至 2025 年有关这些栖息地的科学文献进行了系统回顾和综合。
- Keywords: research, rariphotic, biases, zone, five

### 12. [右背外侧前额叶和后顶叶皮质对自动酒精接近倾向的可分离贡献](https://www.biorxiv.org/content/10.64898/2026.04.19.719365v3)
- Original title: Dissociable Contributions of the Right Dorsolateral Prefrontal and Posterior Parietal Cortices to Automatic Alcohol Approach Tendencies
- Authors: Verma, A. K., Kumar, A. D., Chivukula, U., Kumar, N.
- Meta: 2026-07-08 | neuroscience | DOI: 10.64898/2026.04.19.719365
- 中文摘要: 强迫性饮酒通常是通过接近倾向来维持的，这种接近倾向会自动将个人导向与酒精相关的线索，即使他们打算避免这些线索。越来越多的证据表明，额顶叶区域参与调节这种自动行为。然而，右背外侧前额叶皮层（rDLPFC）和右后顶叶皮层（rPPC）的具体贡献以及潜在的神经认知机制仍不清楚。为了确定这些区域的具体贡献，我们使用受试者内的主动假平衡设计，对不同组的非临床酒精使用者（rDLPFC：n = 29；rPPC：n = 28）的rDLPFC或rPPC应用连续θ爆发刺激（cTBS）。在基线和主动刺激和假刺激后使用酒精接近避免任务评估酒精接近倾向。
- Abstract: Compulsive alcohol intake is often sustained by approach tendencies that automatically orient individuals toward alcohol-related cues, even when they intend to avoid them. Converging evidence implicates the frontoparietal regions in regulating such automatic behavior; however, the specific contributions of the right dorsolateral prefrontal cortex (rDLPFC) and right posterior parietal cortex (rPPC), and the underlyin...
- Summary (fallback): 机器翻译摘要显示：强迫性饮酒通常是通过接近倾向来维持的，这种接近倾向会自动将个人导向与酒精相关的线索，即使他们打算避免这些线索。越来越多的证据表明，额顶叶区域参与调节这种自动行为。然而，右背外侧前额叶皮层（rDLPFC）和右后顶叶皮层（rPPC）的具体贡献以及潜在的神经认知机制仍不清楚。为了确定这些区域的具体贡献，我们使用受试者内的主动假平衡设计，对不同组的非临床酒精使用者（rDLPFC：n = 29；rPPC：n = 28）的rDLPFC或rPPC应用连续θ爆发刺激（cTBS）。在基线和主动刺激和假刺激后使用酒精接近避免任务评估酒精接近倾向。
- Keywords: alcohol, approach, rdlpfc, rppc, responses

### 13. [使用银屑病关节炎滑液作为工具来捕获患者对治疗的特异性反应的关节组织外植体模型](https://www.biorxiv.org/content/10.64898/2026.07.05.736607v1)
- Original title: Joint tissue explant model using psoriatic arthritis synovial fluid as a tool to capture patient-specific responses to treatments
- Authors: Ziyaeyan, A., Rasti, M., Gandhi, R., Oikonomopoulou, K., Chandran, V. et al.
- Meta: 2026-07-08 | immunology | DOI: 10.64898/2026.07.05.736607
- 中文摘要: 目的 我们开发了一种患者和关节特异性外植体共培养系统，用于模拟活动性银屑病关节炎 (PsA) 并捕获供体特异性组织对治疗干预的反应。方法 根据终末期骨关节炎（OA）和 PsA 之间的趋同性关节病理学，将来自关节置换术患者的 OA 软骨骨和滑膜组织暴露于从 PsA 和 OA 患者获得的滑液（SF）。在 7-21 天内评估组织学结果（滑膜炎、蛋白多糖分布）、策划的基因表达、可溶性介质和蛋白酶活性。评估了模型对地塞米松 (DEX) 和抗肿瘤坏死因子抗体阿达木单抗 (ADA) 的反应。
- Abstract: Objective We developed a patient- and joint-specific explant co-culture system to model active psoriatic arthritis (PsA) and capture donor-specific tissue responses to therapeutic interventions. Methods Based on convergent joint pathology between end-stage osteoarthritis (OA) and PsA, OA cartilage-bone and synovium tissues from arthroplasty patients were exposed to synovial fluid (SF) obtained from PsA and OA patien...
- Summary (fallback): 机器翻译摘要显示：目的 我们开发了一种患者和关节特异性外植体共培养系统，用于模拟活动性银屑病关节炎 (PsA) 并捕获供体特异性组织对治疗干预的反应。方法 根据终末期骨关节炎（OA）和 PsA 之间的趋同性关节病理学，将来自关节置换术患者的 OA 软骨骨和滑膜组织暴露于从 PsA 和 OA 患者获得的滑液（SF）。在 7-21 天内评估组织学结果（滑膜炎、蛋白多糖分布）、策划的基因表达、可溶性介质和蛋白酶活性。评估了模型对地塞米松 (DEX) 和抗肿瘤坏死因子抗体阿达木单抗 (ADA) 的反应。
- Keywords: responses, model, synovial, synovitis, joint

### 14. [SELECT-seq 允许在一锅单细胞全转录组测序中对 SNP 编辑进行预测序富集](https://www.biorxiv.org/content/10.64898/2026.07.07.736965v1)
- Original title: SELECT-seq allows Pre-Sequencing Enrichment of SNP Edits in One-Pot Single-Cell Whole-Transcriptome Sequencing
- Authors: Iwama, S., Gitterman, D., Brendler-Spaeth, T., Waters, A. J., Robertson, H. et al.
- Meta: 2026-07-08 | molecular biology | DOI: 10.64898/2026.07.07.736965
- 中文摘要: 高通量测序的进步将数百万个假定的遗传变异与疾病联系起来。然而，建立遗传变异和下游转录结果之间因果关系的可扩展实验方法仍然是一个重大挑战。将基因分型与转录组分析相结合的单细胞方法提供了一种解决此问题的方法，但无法对正确编辑的细胞进行预测序富集，从而限制了规模。我们提出了 SELECT-seq（利用 Cas12a 靶向的 SNP 富集），这是一种快速方法，可以在全转录组扩增的同时进行 SNP 特异性 PCR 扩增和 Cas12a 介导的荧光检测。
- Abstract: Advances in high-throughput sequencing have associated millions of putative genetic variants with disease. However, scalable experimental methods to establish causal relationships between genetic variants and downstream transcriptional outcomes remain a major challenge. Single-cell methods that integrate genotyping with transcriptomic profiling provide a way to address this, but do not enable pre-sequencing enrichme...
- Summary (fallback): 机器翻译摘要显示：高通量测序的进步将数百万个假定的遗传变异与疾病联系起来。然而，建立遗传变异和下游转录结果之间因果关系的可扩展实验方法仍然是一个重大挑战。将基因分型与转录组分析相结合的单细胞方法提供了一种解决此问题的方法，但无法对正确编辑的细胞进行预测序富集，从而限制了规模。我们提出了 SELECT-seq（利用 Cas12a 靶向的 SNP 富集），这是一种快速方法，可以在全转录组扩增的同时进行 SNP 特异性 PCR 扩增和 Cas12a 介导的荧光检测。
- Keywords: select-seq, enrichment, single-cell, scalable, cells

### 15. [在非模型动物中缺乏参考基因组的情况下对 Iso-Seq 数据的聚类和组装策略进行评估](https://www.biorxiv.org/content/10.1101/2025.09.18.677004v2)
- Original title: An evaluation of clustering and assembly strategies from Iso-Seq data in the absence of reference genomes in non-model animals
- Authors: Eleftheriadi, K., Vazquez-Valls, M., Fernandez, R.
- Meta: 2026-07-08 | evolutionary biology | DOI: 10.1101/2025.09.18.677004
- 中文摘要: 转录组组装能够恢复表达的基因和亚型，但从长读长测序中重建转录组的最佳策略仍未解决。特别是，建立生成准确基因模型和选择代表性同种型的最佳实践对于比较基因组学至关重要，因为对于直系同源推断，通常仅包括每个基因模型的最长同种型。在这里，我们使用来自跨越七个门的 17 个动物谱系（其中大多数是非模型物种）的 PacBio Iso-Seq 数据系统地比较聚类和从头组装方法，目的是研究在缺乏特定管道的情况下哪种方法更适合为每个基因模型选择一种异构体。我们评估了四种方法：isoseq cluster、CD-HIT、RNA-Bloom2 和 isONform。
- Abstract: Transcriptome assembly enables the recovery of expressed genes and isoforms, but the optimal strategy for reconstructing transcriptomes from long-read sequencing remains unresolved. In particular, establishing best practices for generating accurate gene models and selecting representative isoforms is essential for comparative genomics, as for orthology inference typically only the longest isoform per gene model is i...
- Summary (fallback): 机器翻译摘要显示：转录组组装能够恢复表达的基因和亚型，但从长读长测序中重建转录组的最佳策略仍未解决。特别是，建立生成准确基因模型和选择代表性同种型的最佳实践对于比较基因组学至关重要，因为对于直系同源推断，通常仅包括每个基因模型的最长同种型。在这里，我们使用来自跨越七个门的 17 个动物谱系（其中大多数是非模型物种）的 PacBio Iso-Seq 数据系统地比较聚类和从头组装方法，目的是研究在缺乏特定管道的情况下哪种方法更适合为每个基因模型选择一种异构体。我们评估了四种方法：isoseq cluster、CD-HIT、RNA-Bloom2 和 isONform。
- Keywords: assembly, long-read, gene, clustering, absence

### 16. [功能代孕可以在缺乏 COL3A1 直向同源物的情况下对斑马鱼进行血管埃勒斯-当洛斯综合征建模](https://www.biorxiv.org/content/10.64898/2026.07.03.736265v1)
- Original title: Functional surrogacy enables Vascular Ehlers-Danlos Syndrome modelling in zebrafish in the absence of a COL3A1 ortholog
- Authors: Baird, D. A., Pidlisnyuk, N., Matischen, A., Matelowska, Z., Seo, S. et al.
- Meta: 2026-07-08 | genetics | DOI: 10.64898/2026.07.03.736265
- 中文摘要: COL3A1 的致病变异会导致血管埃勒斯-当洛斯综合征 (vEDS)，这是一种罕见的结缔组织疾病，其特征是血管脆性，增加动脉破裂/夹层的风险。基因组测序的进步导致 COL3A1 变异数量不断增加，其临床意义尚不清楚，这些变异被称为意义不确定的变异 (VUS)。 VUS 给诊断和临床管理带来了挑战。因此，人们做出了重大努力，将这些变异重新分类为疾病因果关系中的致病变异或良性变异。来自模型系统的功能数据可以为临床医生提供有关变异致病性的重要证据。
- Abstract: Pathogenic variants in COL3A1 cause Vascular Ehlers-Danlos syndrome (vEDS), a rare connective tissue disorder characterised by vascular fragility, increasing the risk of arterial ruptures/dissection. Advances in genomic sequencing have led to an increasing number of COL3A1 variants where the clinical significance is unclear, with these being termed variants of uncertain significance (VUS). VUS creates challenges for...
- Summary (fallback): 机器翻译摘要显示：COL3A1 的致病变异会导致血管埃勒斯-当洛斯综合征 (vEDS)，这是一种罕见的结缔组织疾病，其特征是血管脆性，增加动脉破裂/夹层的风险。基因组测序的进步导致 COL3A1 变异数量不断增加，其临床意义尚不清楚，这些变异被称为意义不确定的变异 (VUS)。 VUS 给诊断和临床管理带来了挑战。因此，人们做出了重大努力，将这些变异重新分类为疾病因果关系中的致病变异或良性变异。来自模型系统的功能数据可以为临床医生提供有关变异致病性的重要证据。
- Keywords: col3a1, functional, zebrafish, variants, vascular

### 17. [元条形码复制检测频率跟踪古代海洋沉积物中鳕鱼和鲱鱼 eDNA 的 ddPCR 拷贝数](https://www.biorxiv.org/content/10.64898/2026.07.03.736335v1)
- Original title: Metabarcoding replicate detection frequency tracks ddPCR copy number for cod and herring eDNA in ancient marine sediments
- Authors: Banos Lara, E., Holman, L. E., Knudsen, S. W., Bohmann, K.
- Meta: 2026-07-08 | genetics | DOI: 10.64898/2026.07.03.736335
- 中文摘要: 1. 检测稀有或低丰度水生物种的环境 DNA (eDNA) 仍然是一项重大挑战，特别是当它高度降解、浓度较低且以非目标类群 DNA 为主时。这些挑战在沉积古 DNA (sedaDNA) 研究中进一步放大，数千年的时间可以进一步降解 eDNA，使得微弱生物信号的检测和定量解释变得困难。 2. 元条形码通常用于从 eDNA 生成高通量群落级数据，但其本质上是组合性的，并受到扩增偏差的影响。尽管如此，元条形码读取丰度或 PCR 复制检测频率越来越多地用作相对 DNA 浓度的代理，但它们的定量解释很少根据绝对 DNA 丰度的独立测量进行评估。 3.
- Abstract: 1. Detecting environmental DNA (eDNA) from rare or low-abundance aquatic species remains a major challenge, particularly when it is highly degraded, present at low concentrations, and dominated by DNA from non-target taxa. These challenges are further amplified in sedimentary ancient DNA (sedaDNA) studies, where thousands of years can degrade eDNA further, making the detection and quantitative interpretation of weak...
- Summary (fallback): 机器翻译摘要显示：1. 检测稀有或低丰度水生物种的环境 DNA (eDNA) 仍然是一项重大挑战，特别是当它高度降解、浓度较低且以非目标类群 DNA 为主时。这些挑战在沉积古 DNA (sedaDNA) 研究中进一步放大，数千年的时间可以进一步降解 eDNA，使得微弱生物信号的检测和定量解释变得困难。 2. 元条形码通常用于从 eDNA 生成高通量群落级数据，但其本质上是组合性的，并受到扩增偏差的影响。尽管如此，元条形码读取丰度或 PCR 复制检测频率越来越多地用作相对 DNA 浓度的代理，但它们的定量解释很少根据绝对 DNA 丰度的独立测量进行评估。 3.
- Keywords: metabarcoding, detection, frequency, edna, abundance

### 18. [基因调控共表达网络破译潜在的 lncRNA-miRNA-mRNA 相互作用调节神经退行性疾病中的转录调控](https://www.biorxiv.org/content/10.64898/2026.07.03.736295v1)
- Original title: Gene regulatory co-expression networks decipher potential lncRNA-miRNA-mRNA interactions modulating transcription regulation in neurodegeneration
- Authors: Venkatesan, A., Sinha, P., Basak, J., Bahadur, R.
- Meta: 2026-07-08 | bioinformatics | DOI: 10.64898/2026.07.03.736295
- 中文摘要: 神经退行性疾病是一种复杂的疾病，其特征是进行性神经元丢失和广泛的转录组失调；然而，编码和非编码 RNA 之间导致疾病进展的协调相互作用仍不完全清楚。在这项研究中，使用基于网络的综合框架分析了代表阿尔茨海默病 (AD)、帕金森病 (PD) 和肌萎缩侧索硬化症 (ALS) 的疾病相关神经元群体和大脑区域的 RNA-seq 数据集。差异表达分析与加权基因共表达网络分析相结合，确定了与疾病显着相关的模块，并优先考虑了高度连接的中心基因。这些枢纽基因与精心策划的 RNA 相互作用数据库的整合能够构建候选 lncRNA-miRNA-mRNA 调控网络。
- Abstract: Neurodegenerative diseases are complex disorders characterised by progressive neuronal loss and widespread transcriptomic dysregulation; however, the coordinated interactions among coding and non-coding RNAs that contribute to disease progression remain incompletely understood. In this study, RNA-seq datasets from disease-relevant neuronal populations and brain regions representing Alzheimer's disease (AD), Parkinso...
- Summary (fallback): 机器翻译摘要显示：神经退行性疾病是一种复杂的疾病，其特征是进行性神经元丢失和广泛的转录组失调；然而，编码和非编码 RNA 之间导致疾病进展的协调相互作用仍不完全清楚。在这项研究中，使用基于网络的综合框架分析了代表阿尔茨海默病 (AD)、帕金森病 (PD) 和肌萎缩侧索硬化症 (ALS) 的疾病相关神经元群体和大脑区域的 RNA-seq 数据集。差异表达分析与加权基因共表达网络分析相结合，确定了与疾病显着相关的模块，并优先考虑了高度连接的中心基因。这些枢纽基因与精心策划的 RNA 相互作用数据库的整合能够构建候选 lncRNA-miRNA-mRNA 调控网络。
- Keywords: regulatory, disease, genes, gene, networks

### 19. [肿瘤栓子相关的适应性应激反应特征识别炎症性乳腺癌的侵袭性疾病特征](https://www.biorxiv.org/content/10.64898/2026.07.06.734332v1)
- Original title: Tumor emboli-associated adaptive stress response signatures identify aggressive disease features in inflammatory breast cancer
- Authors: PAI, P., Hsu, H., Manyam, G. C., Laere, S. V., Mysona, D. P. et al.
- Meta: 2026-07-08 | cancer biology | DOI: 10.64898/2026.07.06.734332
- 中文摘要: 炎性乳腺癌（IBC）是一种侵袭性乳腺癌亚型，其特征为肿瘤栓塞、淋巴血管侵犯（LVI）和早期播散。在此，我们将适应性应激反应（ASR）建立为一种生物学特征，将应激适应与肿瘤栓子存活、淋巴传播、治疗反应和差异联系起来。使用先前定义的 226 个 ASR 相关基因、肿瘤栓子和淋巴循环细胞簇的互补临床前模型以及独立的患者队列，我们​​确定了富含 XIAP-NF{kappa}B、氧化应激反应、炎症和免疫途径的 ASR 基因。
- Abstract: Inflammatory breast cancer (IBC) is an aggressive breast cancer subtype characterized by tumor emboli, lymphovascular invasion (LVI), and early dissemination. Herein, we establish adaptive stress response (ASR) as a biologic feature linking stress adaptation to tumor emboli survival, lymphatic dissemination, therapeutic response, and disparities. Using a previously defined 226 ASR-related genes, complementary precli...
- Summary (fallback): 机器翻译摘要显示：炎性乳腺癌（IBC）是一种侵袭性乳腺癌亚型，其特征为肿瘤栓塞、淋巴血管侵犯（LVI）和早期播散。在此，我们将适应性应激反应（ASR）建立为一种生物学特征，将应激适应与肿瘤栓子存活、淋巴传播、治疗反应和差异联系起来。使用先前定义的 226 个 ASR 相关基因、肿瘤栓子和淋巴循环细胞簇的互补临床前模型以及独立的患者队列，我们​​确定了富含 XIAP-NF{kappa}B、氧化应激反应、炎症和免疫途径的 ASR 基因。
- Keywords: tumor, stress, emboli, response, dissemination

### 20. [PTPRJ 推动 CEBPA 突变 AML 的克隆选择](https://www.biorxiv.org/content/10.64898/2026.07.07.736996v1)
- Original title: PTPRJ Drives Clonal Selection in CEBPA mutated AML
- Authors: Lubin, A., Hockings, C., Hoade, Y., Copper, L., Dace, P. et al.
- Meta: 2026-07-08 | cancer biology | DOI: 10.64898/2026.07.07.736996
- 中文摘要: 10-15% 的急性髓系白血病 (AML) 中转录因子 CEBPA 发生突变，这是一种死亡率很高的造血系统恶性肿瘤。 CEBPA 突变表现出独特的模式，大多数患者是双等位基因，在相反的等位基因上同时携带符合读码框的 C 端突变和移码 N 端突变。罕见的 N 端种系病例对 AML 具有 100% 的外显率，所有病例均具有获得性 C 端突变。这表明来自一种 CEBPA 突变的选择性压力会导致另一种突变的发生。我们的斑马鱼模型忠实地再现了人类疾病。所有双等位基因突变体组合均在 4-6 周龄时死亡，并伴有白血病前造血干细胞 (HSC) 扩增。 C 端和 N 端突变体在髓系引发的 HSC 中表现出表型差异，并且在髓系分化块中表现出差异。 RNA-Seq 鉴定了相反载体中差异表达的基因。
- Abstract: Transcription factor CEBPA is mutated in 10-15% of acute myeloid leukaemia (AML), a haematopoietic malignancy with high mortality. CEBPA mutations show a distinct pattern, and most patients are biallelic, carrying both an in frame C-terminal mutation and a frameshift N-terminal mutation on opposing alleles. Rare N-terminal germline cases have 100% penetrance to AML, all with an acquired a C-terminal mutation. This s...
- Summary (fallback): 机器翻译摘要显示：10-15% 的急性髓系白血病 (AML) 中转录因子 CEBPA 发生突变，这是一种死亡率很高的造血系统恶性肿瘤。 CEBPA 突变表现出独特的模式，大多数患者是双等位基因，在相反的等位基因上同时携带符合读码框的 C 端突变和移码 N 端突变。罕见的 N 端种系病例对 AML 具有 100% 的外显率，所有病例均具有获得性 C 端突变。这表明来自一种 CEBPA 突变的选择性压力会导致另一种突变的发生。我们的斑马鱼模型忠实地再现了人类疾病。所有双等位基因突变体组合均在 4-6 周龄时死亡，并伴有白血病前造血干细胞 (HSC) 扩增。 C 端和 N 端突变体在髓系引发的 HSC 中表现出表型差异，并且在髓系分化块中表现出差异。 RNA-Seq 鉴定了相反载体中差异表达的基因。
- Keywords: cebpa, mutation, ptprj, c-terminal, n-terminal

### 21. [与环境相关的贫铀暴露会损害线粒体，降低细胞质还原能力，并通过涉及弹弓蛋白磷酸酶 1b 富集的 ROS 独立机制增加整体 DNA 损伤积累。](https://www.biorxiv.org/content/10.64898/2026.07.02.736169v1)
- Original title: Environmentally relevant depleted uranium exposure damages mitochondria, decreases cytosolic reductive capacity, and increases global DNA damage accumulation through a ROS-independent mechanism involving slingshot protein phosphatase 1b enrichment.
- Authors: Kalaniopio, P. H., Gibbons, L. B., Allen, R. S., Matthews, S. M., Lujan, O. R. et al.
- Meta: 2026-07-08 | pharmacology and toxicology | DOI: 10.64898/2026.07.02.736169
- 中文摘要: 贫铀 (DU) 是一种环境污染物，EPA 饮用水最高污染水平 (MCL) 为 30 g/L（ppb；十亿分之一）。铀矿开采和现代武器中贫铀的使用导致人类接触铀，这对美国的军事和部落社区造成了不成比例的影响。铀的放射性毒性特性已为人所知，但其化学危害却远非如此。在斑马鱼 (Danio rerio) 和人类细胞培养物中，我们测试了这样的假设：接触 DU 通过破坏线粒体代谢对细胞功能和发育产生负面影响。使用 TEM/SEM+EDS 的新型弹片模型，我们发现铀微粒会导致邻近依赖性线粒体破坏。
- Abstract: Depleted uranium (DU) is an environmental contaminant with a 30 g/L (ppb; parts per billion) EPA maximum contaminant level (MCL) for drinking water. The mining of uranium and use of DU in modern weapons underly human exposure that disproportionally impacts military and tribal communities in the United States. Uranium's radiotoxic characteristics are understood, but its chemical hazards much less so. In zebrafish (Da...
- Summary (fallback): 机器翻译摘要显示：贫铀 (DU) 是一种环境污染物，EPA 饮用水最高污染水平 (MCL) 为 30 g/L（ppb；十亿分之一）。铀矿开采和现代武器中贫铀的使用导致人类接触铀，这对美国的军事和部落社区造成了不成比例的影响。铀的放射性毒性特性已为人所知，但其化学危害却远非如此。在斑马鱼 (Danio rerio) 和人类细胞培养物中，我们测试了这样的假设：接触 DU 通过破坏线粒体代谢对细胞功能和发育产生负面影响。使用 TEM/SEM+EDS 的新型弹片模型，我们发现铀微粒会导致邻近依赖性线粒体破坏。
- Keywords: exposure, mitochondrial, uranium, damage, reductive

### 22. [CqFT1A 和 CqFT1B-1 是藜麦的主要开花激活剂](https://www.biorxiv.org/content/10.64898/2026.07.07.736970v1)
- Original title: CqFT1A and CqFT1B-1 are major flowering activators in quinoa
- Authors: Ogata, T., Fujita, Y.
- Meta: 2026-07-08 | plant biology | DOI: 10.64898/2026.07.07.736970
- 中文摘要: 开花时间强烈影响作物适应、植物结构、世代更替和育种效率，但在许多多倍体孤儿作物中，成花基因的功能组织仍然很难解决。藜麦 (Chenopodium quinoa) 是一种气候适应性强的异源四倍体作物，其开花行为存在广泛差异，基因组分析已鉴定出多个类似 FLOWERING LOCUS T (FT) 的同源物。然而，仅靠基因组序列和表达信息无法确定哪些同源物在植物中提供有效的成花输出。在这里，我们将藜麦中苹果潜伏球形病毒介导的过表达（VOX）和病毒诱导的基因沉默（VIGS）与拟南芥中的异源表达、结构域交换分析和跨种质验证相结合，以功能性剖析藜麦 FT 活性。
- Abstract: Flowering time strongly influences crop adaptation, plant architecture, generation turnover, and breeding efficiency, but the functional organization of florigen genes remains poorly resolved in many polyploid orphan crops. Quinoa (Chenopodium quinoa) is a climate-resilient allotetraploid crop with extensive variation in flowering behavior, and genome analyses have identified multiple FLOWERING LOCUS T (FT)-like hom...
- Summary (fallback): 机器翻译摘要显示：开花时间强烈影响作物适应、植物结构、世代更替和育种效率，但在许多多倍体孤儿作物中，成花基因的功能组织仍然很难解决。藜麦 (Chenopodium quinoa) 是一种气候适应性强的异源四倍体作物，其开花行为存在广泛差异，基因组分析已鉴定出多个类似 FLOWERING LOCUS T (FT) 的同源物。然而，仅靠基因组序列和表达信息无法确定哪些同源物在植物中提供有效的成花输出。在这里，我们将藜麦中苹果潜伏球形病毒介导的过表达（VOX）和病毒诱导的基因沉默（VIGS）与拟南芥中的异源表达、结构域交换分析和跨种质验证相结合，以功能性剖析藜麦 FT 活性。
- Keywords: flowering, quinoa, functional, homologs, induced

### 23. [有丝分裂前极性程序图案化草叶表皮](https://www.biorxiv.org/content/10.64898/2026.07.07.736711v1)
- Original title: A premitotic polarity program patterns the grass leaf epidermis
- Authors: Korosteleva, A. L., Janssen, K. N., Zhang, D., Ruiz Duarte, P., Polat, I. et al.
- Meta: 2026-07-08 | plant biology | DOI: 10.64898/2026.07.07.736711
- 中文摘要: 草叶表皮发育中的横向不对称细胞分裂（ACD）产生大的基底铺面细胞和小的顶端特化细胞。这些“图案分裂”产生了草类特有的长短表皮细胞图案。在这里，我们表明，模式分裂需要模型草二穗短柄草中 BdPOLAR-LIKE1 (BdPL1) 的有丝分裂前基底极化。 BdPL1 的缺失会破坏所有细胞文件中的分裂平面方向和有丝分裂后细胞大小不对称性，从而导致表皮图案缺陷。异位表达分析表明，BdPL1 极化独立于细胞环境，足以促进多余的横分裂。此外，发育调节因子 BdBREVIS RADIX-solo 和 BdYODA1 形成了一个分裂后极性域，独立于 BdPL1 强制执行细胞命运不对称。
- Abstract: Transverse asymmetric cell divisions (ACDs) in grass leaf epidermal development produce large basal pavement cells and small apical specialised cells. These "patterning divisions" generate the long-short epidermal cell pattern that is distinctive of grasses. Here, we show that patterning divisions require premitotic basal polarisation of BdPOLAR-LIKE1 (BdPL1) in the model grass Brachypodium distachyon. Loss of BdPL1...
- Summary (fallback): 机器翻译摘要显示：草叶表皮发育中的横向不对称细胞分裂（ACD）产生大的基底铺面细胞和小的顶端特化细胞。这些“图案分裂”产生了草类特有的长短表皮细胞图案。在这里，我们表明，模式分裂需要模型草二穗短柄草中 BdPOLAR-LIKE1 (BdPL1) 的有丝分裂前基底极化。 BdPL1 的缺失会破坏所有细胞文件中的分裂平面方向和有丝分裂后细胞大小不对称性，从而导致表皮图案缺陷。异位表达分析表明，BdPL1 极化独立于细胞环境，足以促进多余的横分裂。此外，发育调节因子 BdBREVIS RADIX-solo 和 BdYODA1 形成了一个分裂后极性域，独立于 BdPL1 强制执行细胞命运不对称。
- Keywords: cell, bdpl1, grass, divisions, patterning

### 24. [重金属 ATP 酶家族的泛基因组和泛转录组分析揭示了大麦中的不同表达模式和功能作用](https://www.biorxiv.org/content/10.64898/2026.07.07.736986v1)
- Original title: Pan-genomic and pan-transcriptomic analysis of the Heavy Metal ATPase family reveals diverse expression patterns and functional roles in barley
- Authors: Shadbolt, J., Schreiber, M., Russell, J., Waugh, R., Houston, K.
- Meta: 2026-07-08 | plant biology | DOI: 10.64898/2026.07.07.736986
- 中文摘要: 重金属在许多生理过程中充当必需金属蛋白辅因子，但当非必需金属积累或必需金属过量时，重金属会变得有毒。当植物通过根不断接触重金属时，它们进化出了复杂的稳态机制来调节金属的吸收和分布。重金属 ATP 酶 (HMA) 基因家族编码一组重金属转运 P 型 ATP 酶，这些酶与抗逆性和营养供应有关。在这里，我们使用生物信息学方法来识别和表征大麦 Morex V3 参考基因组中含有特征性 P1B 型 ATP 酶结构域和基序的 13 个 HMA 基因。这些基因位于大麦七个染色体中的五个上。系统发育分析表明，它们分为五个亚支，其中一个是大麦特有的支。
- Abstract: Heavy metals act as essential metalloprotein cofactors in numerous physiological processes but can become toxic when non-essential metals accumulate or when essential metals are in excess. As plants continuously encounter heavy metals through their roots, they have evolved complex homeostatic mechanisms to regulate metal uptake and distribution. The Heavy Metal ATPase (HMA) gene family encodes a group of heavy metal...
- Summary (fallback): 机器翻译摘要显示：重金属在许多生理过程中充当必需金属蛋白辅因子，但当非必需金属积累或必需金属过量时，重金属会变得有毒。当植物通过根不断接触重金属时，它们进化出了复杂的稳态机制来调节金属的吸收和分布。重金属 ATP 酶 (HMA) 基因家族编码一组重金属转运 P 型 ATP 酶，这些酶与抗逆性和营养供应有关。在这里，我们使用生物信息学方法来识别和表征大麦 Morex V3 参考基因组中含有特征性 P1B 型 ATP 酶结构域和基序的 13 个 HMA 基因。这些基因位于大麦七个染色体中的五个上。系统发育分析表明，它们分为五个亚支，其中一个是大麦特有的支。
- Keywords: heavy, metal, barley, metals, atpase

### 25. [用于记录细胞谱系树的条码质粒 DNA 文库构建，由基于 Biofoundry 的可扩展和模块化自动化机器人管道实现](https://www.biorxiv.org/content/10.64898/2026.07.07.736956v1)
- Original title: Barcoded-Plasmid DNA library construction for recording cell lineage trees enabled by a Scalable and modular Biofoundry-based Automated Robotic Pipeline
- Authors: Tassinari, E., Ives, L., Hawkins, E., Annese, D., Fonseca, S. et al.
- Meta: 2026-07-08 | synthetic biology | DOI: 10.64898/2026.07.07.736956
- 中文摘要: 高通量的高质量质粒 DNA 纯化仍然是分子生物学和生物工程的一个重要瓶颈。目前的方法常常无法提供哺乳动物细胞基因工程应用所需的足够产量的纯转染级 DNA。在这里，我们提出了一种基于 Biofoundry 的自动化管道，使用 CyBio FeliX 机器人液体处理平台，以最少的手动干预快速纯化质粒 DNA。该协议利用基于固相可逆固定 (SPRI) 的磁珠技术来确保适合下游病毒颗粒生产和哺乳动物细胞转染的一致性、可扩展性和 DNA 纯度。该管道支持每次运行灵活处理 8 至 96 个样本，使其能够适应广泛的实验规模。
- Abstract: High-quality plasmid DNA purification at high throughput remains a significant bottleneck in molecular biology and bioengineering. Current methods frequently fail to deliver sufficient yields of pure, transfection-grade DNA required for genetic engineering applications in mammalian cells. Here, we present a Biofoundry-based automated pipeline using the CyBio FeliX robotic liquid handling platform to rapidly purify p...
- Summary (fallback): 机器翻译摘要显示：高通量的高质量质粒 DNA 纯化仍然是分子生物学和生物工程的一个重要瓶颈。目前的方法常常无法提供哺乳动物细胞基因工程应用所需的足够产量的纯转染级 DNA。在这里，我们提出了一种基于 Biofoundry 的自动化管道，使用 CyBio FeliX 机器人液体处理平台，以最少的手动干预快速纯化质粒 DNA。该协议利用基于固相可逆固定 (SPRI) 的磁珠技术来确保适合下游病毒颗粒生产和哺乳动物细胞转染的一致性、可扩展性和 DNA 纯度。该管道支持每次运行灵活处理 8 至 96 个样本，使其能够适应广泛的实验规模。
- Keywords: pipeline, library, cell, robotic, plasmid

### 26. [虚拟儿童大脑：神经成熟轨迹建模](https://www.biorxiv.org/content/10.64898/2026.07.07.737052v1)
- Original title: The Virtual Child Brain: Modeling Neuromaturational Trajectories
- Authors: Westin, K. M., Martin, L. K., Pille, M., Schirner, M., Ritter, P.
- Meta: 2026-07-08 | neuroscience | DOI: 10.64898/2026.07.07.737052
- 中文摘要: 简介 了解人类神经成熟的机制是神经科学的基本问题之一。虽然有充分的描述，大规模的大脑成熟是在感觉运动大脑区域内启动并进展到联想皮层，但潜在的发育神经生物学仍有待充分表征。动物模型表明，皮质抑制上调可能是神经发育的驱动因素。为了研究皮质抑制上调在人类神经成熟中发挥类似作用的假设，我们开发了基于虚拟大脑（TVB）的计算模型（TVB-Child）来探索人类神经发育的潜在机制。
- Abstract: Introduction Understanding the mechanisms of human neuromaturation constitutes one of the fundamental questions of neuroscience. While it is well described that large-scale brain maturation is initiated within sensorimotor brain regions and progresses to associative cortex, the underlying developmental neurobiology remains to be fully characterized. Animal models have indicated that cortical inhibitory upregulation...
- Summary (fallback): 机器翻译摘要显示：简介 了解人类神经成熟的机制是神经科学的基本问题之一。虽然有充分的描述，大规模的大脑成熟是在感觉运动大脑区域内启动并进展到联想皮层，但潜在的发育神经生物学仍有待充分表征。动物模型表明，皮质抑制上调可能是神经发育的驱动因素。为了研究皮质抑制上调在人类神经成熟中发挥类似作用的假设，我们开发了基于虚拟大脑（TVB）的计算模型（TVB-Child）来探索人类神经发育的潜在机制。
- Keywords: brain, network, networks, trajectories, models

### 27. [源自患者的 tau 种子人类神经元嵌合体重现了成熟的阿尔茨海默病 tau 病理学并揭示了人类特有的神经元脆弱性](https://www.biorxiv.org/content/10.64898/2026.07.06.736894v1)
- Original title: Patient-derived tau-seeded human neuronal chimeras recapitulate mature Alzheimer's tau pathology and uncover human-specific neuronal vulnerability
- Authors: Xu, R.
- Meta: 2026-07-08 | neuroscience | DOI: 10.64898/2026.07.06.736894
- 中文摘要: Tau 病理学是阿尔茨海默病 (AD) 的核心标志，与认知能力下降密切相关，但由于现有模型无法捕获人类特异性疾病特征，特别是 AD tau 病理学的成熟形式，因此 tau 靶向疗法的发展受到阻碍。此外，tau 病理学的物种特异性机制仍然知之甚少。在这里，我们通过将人类多能干细胞（hPSC）来源的神经祖细胞移植到新生小鼠大脑中，然后脑内注射来自死后 AD 大脑的病理性 tau 种子，建立了患者来源的 tau 种子人类神经元嵌合体模型。人类神经元在体内成熟并重现了成人 tau 特征，包括所有六种亚型，3R:4R 比例约为 1:1。
- Abstract: Tau pathology is a central hallmark of Alzheimer's disease (AD) and strongly correlates with cognitive decline, yet the development of tau-targeted therapies has been hindered by the inability of existing models to capture human-specific disease features, particularly the mature forms of AD tau pathology. Moreover, species-specific mechanisms underlying tau pathology remain poorly understood. Here, we establish a pa...
- Summary (fallback): 机器翻译摘要显示：Tau 病理学是阿尔茨海默病 (AD) 的核心标志，与认知能力下降密切相关，但由于现有模型无法捕获人类特异性疾病特征，特别是 AD tau 病理学的成熟形式，因此 tau 靶向疗法的发展受到阻碍。此外，tau 病理学的物种特异性机制仍然知之甚少。在这里，我们通过将人类多能干细胞（hPSC）来源的神经祖细胞移植到新生小鼠大脑中，然后脑内注射来自死后 AD 大脑的病理性 tau 种子，建立了患者来源的 tau 种子人类神经元嵌合体模型。人类神经元在体内成熟并重现了成人 tau 特征，包括所有六种亚型，3R:4R 比例约为 1:1。
- Keywords: human, pathology, neurons, mature, neuronal

### 28. [节奏对新生儿听觉节律神经处理的影响：对韵律结构敏感的出现](https://www.biorxiv.org/content/10.64898/2026.07.07.736947v1)
- Original title: Effect of tempo on newborns' neural processing of auditory rhythm: Emergence of sensitivity to metrical structure
- Authors: Edalati, M., Psaris, M., Gallard, A., Foulon, A., Wallois, F. et al.
- Meta: 2026-07-08 | neuroscience | DOI: 10.64898/2026.07.07.736947
- 中文摘要: 节奏感知能力是音乐和语言处理的基础，其发展起源可以追溯到生命的最早时期。虽然大多数节奏模式包含各种起始间隔，但听众通常会提取稳定的基础节拍周期性以及节拍分组周期性（两个或三个节拍的组将分别处于主要节拍频率的 1/2 或 1/3），形成韵律层次结构。虽然发育中的大脑可以在出生前追踪听觉节律，但之前的一项研究发现，对较快节拍相关周期性的神经敏感性在妊娠晚期早期出现，而对较慢韵律结构周期性的编码仅在接近足月出生时出现。
- Abstract: Rhythm perception ability underpins music and language processing, and its developmental origins trace back to the earliest periods of life. While most rhythm patterns contain a variety of inter-onset intervals, listeners typically extract a steady underlying beat periodicity, as well as beat grouping periodicities (groups of two or three beats will be at frequencies 1/2 or 1/3, respectively, of that of the primary...
- Summary (fallback): 机器翻译摘要显示：节奏感知能力是音乐和语言处理的基础，其发展起源可以追溯到生命的最早时期。虽然大多数节奏模式包含各种起始间隔，但听众通常会提取稳定的基础节拍周期性以及节拍分组周期性（两个或三个节拍的组将分别处于主要节拍频率的 1/2 或 1/3），形成韵律层次结构。虽然发育中的大脑可以在出生前追踪听觉节律，但之前的一项研究发现，对较快节拍相关周期性的神经敏感性在妊娠晚期早期出现，而对较慢韵律结构周期性的编码仅在接近足月出生时出现。
- Keywords: metrical, tempo, neural, rhythm, sensitivity

### 29. [简单的过度学习时间期望的神经特征类似于情景检索](https://www.biorxiv.org/content/10.64898/2026.07.07.737020v1)
- Original title: The neural signature of simple overlearned temporal expectations resembles episodic retrieval
- Authors: Sempf, L., Vavra, P., Noesselt, T.
- Meta: 2026-07-08 | neuroscience | DOI: 10.64898/2026.07.07.737020
- 中文摘要: 时间期望对于对可预测事件的适应性响应至关重要。以前的大多数成像研究都集中在意外事件而不是预期的神经基础上，没有考虑到与时间预期相关的神经反应可能会被并行学习过程所混淆。为了通过功能磁共振成像确定过度学习预期的神经基础，我们采用了多日检测范例，在可能和不太可能的时间点，听觉线索先于视觉目标。训练后，左下顶叶皮层与压后皮层和前额叶皮层一起处理过度学习的时间期望。值得注意的是，与未经训练的对照组相比，我们观察到反向的大脑反应是刺激可能性和训练状态的函数。
- Abstract: Temporal expectations are crucial for adaptive responding to predictable events. Most previous imaging studies have focused on the neural underpinnings of unexpectedness rather than expectedness, without considering that neural responses related to temporal expectations may be confounded by parallel learning processes. To identify the neural basis of overlearned expectancy with fMRI, we employed a multi-day detectio...
- Summary (fallback): 机器翻译摘要显示：时间期望对于对可预测事件的适应性响应至关重要。以前的大多数成像研究都集中在意外事件而不是预期的神经基础上，没有考虑到与时间预期相关的神经反应可能会被并行学习过程所混淆。为了通过功能磁共振成像确定过度学习预期的神经基础，我们采用了多日检测范例，在可能和不太可能的时间点，听觉线索先于视觉目标。训练后，左下顶叶皮层与压后皮层和前额叶皮层一起处理过度学习的时间期望。值得注意的是，与未经训练的对照组相比，我们观察到反向的大脑反应是刺激可能性和训练状态的函数。
- Keywords: temporal, expectations, neural, overlearned, episodic

## medrxiv

### 1. [患有儿科发作的强迫症的儿童和青少年的抑制控制 - 一项功能磁共振成像研究](https://www.medrxiv.org/content/10.1101/2025.05.09.25327300v2)
- Original title: Inhibitory control in children and adolescents with paediatric-onset obsessive-compulsive disorder - An fMRI study
- Authors: Larsen, K. M. M., Uhre, V., Labanauskas, V., Madsen, K., Nejad, A. et al.
- Meta: 2026-07-08 | psychiatry and clinical psychology | DOI: 10.1101/2025.05.09.25327300
- 中文摘要: 背景：强迫症（OCD）的病理生理学似乎涉及感觉运动、认知、情感和动机过程的大脑回路功能障碍。观察到的功能障碍之一是抑制性运动控制的破坏。虽然功能磁共振成像 (fMRI) 揭示了成人大脑网络水平的相关改变，但针对儿童强迫症的研究却得出了不一致的结果。方法：这项基于任务的功能磁共振成像研究检查了 65 名未接受药物治疗的儿童强迫症患者和 58 名年龄和性别匹配的健康对照者的执行运动控制。参与者年龄为 8 至 17 岁，并在全脑 3 Tesla fMRI 期间执行停止信号任务。除了全脑分析之外，我们还进行了兴趣区域分析，重点关注在停止信号任务期间促进抑制性运动控制的大脑区域。
- Abstract: Background: The pathophysiology of obsessive-compulsive disorder (OCD) appears to involve dysfunctions in brain circuits underlying sensorimotor, cognitive, affective, and motivational processes. One area of dysfunction observed is disruption in inhibitory motor control. While functional magnetic resonance imaging (fMRI) has revealed associated alterations at the brain network level in adults, studies in pediatric O...
- Summary (fallback): 机器翻译摘要显示：背景：强迫症（OCD）的病理生理学似乎涉及感觉运动、认知、情感和动机过程的大脑回路功能障碍。观察到的功能障碍之一是抑制性运动控制的破坏。虽然功能磁共振成像 (fMRI) 揭示了成人大脑网络水平的相关改变，但针对儿童强迫症的研究却得出了不一致的结果。方法：这项基于任务的功能磁共振成像研究检查了 65 名未接受药物治疗的儿童强迫症患者和 58 名年龄和性别匹配的健康对照者的执行运动控制。参与者年龄为 8 至 17 岁，并在全脑 3 Tesla fMRI 期间执行停止信号任务。除了全脑分析之外，我们还进行了兴趣区域分析，重点关注在停止信号任务期间促进抑制性运动控制的大脑区域。
- Keywords: control, inhibitory, fmri, brain, motor

### 2. [数据驱动的萎缩轨迹解释了路易体疾病的临床异质性](https://www.medrxiv.org/content/10.64898/2026.01.29.26344990v2)
- Original title: Data-driven trajectories of atrophy explain clinical heterogeneity across Lewy body diseases
- Authors: Konuri, A., Castro Leal, G., Zebarjadi, N., Habich, A., Castellanos-Perilla, N. et al.
- Meta: 2026-07-08 | neurology | DOI: 10.64898/2026.01.29.26344990
- 中文摘要: 背景：路易体疾病（LBD）共同具有α-突触核蛋白路易体病理学，但呈现出广泛的临床异质性，具有重叠的运动和非运动特征以及挑战传统诊断界限的进展模式。方法：为了在生物学水平上解决这种时空异质性，我们使用亚型和阶段推断 (SuStaIn) 算法，将数据驱动的萎缩进展框架应用于 833 名帕金森病 (PD)、路易体痴呆 (DLB) 和前驱特发性快速眼动睡眠行为障碍 (iRBD) 个体的 MRI 数据。
- Abstract: Background: Lewy body diseases (LBD) collectively share alpha-synuclein Lewy pathology, yet present wide clinical heterogeneity, with overlapping motor and non-motor features and progression patterns that challenge traditional diagnostic boundaries. Methods: To resolve this spatiotemporal heterogeneity at the biological level, we applied a data-driven atrophy progression framework to MRI data from 833 individuals ac...
- Summary (fallback): 机器翻译摘要显示：背景：路易体疾病（LBD）共同具有α-突触核蛋白路易体病理学，但呈现出广泛的临床异质性，具有重叠的运动和非运动特征以及挑战传统诊断界限的进展模式。方法：为了在生物学水平上解决这种时空异质性，我们使用亚型和阶段推断 (SuStaIn) 算法，将数据驱动的萎缩进展框架应用于 833 名帕金森病 (PD)、路易体痴呆 (DLB) 和前驱特发性快速眼动睡眠行为障碍 (iRBD) 个体的 MRI 数据。
- Keywords: lewy, early, late, basal, atrophy

### 3. [人工智能衍生的心电图年龄差距作为心血管风险的数字生物标志物：在医院和社区前瞻性队列中的外部验证](https://www.medrxiv.org/content/10.64898/2026.03.24.26349186v3)
- Original title: AI-Derived ECG Age Gap as a Digital Biomarker for Cardiovascular Risk: External Validation in Hospital and Community-Based Prospective Cohorts
- Authors: Huang, S., Nie, G., Liu, H., Xie, D., Li, J. et al.
- Meta: 2026-07-08 | health informatics | DOI: 10.64898/2026.03.24.26349186
- 中文摘要: 心血管疾病仍然是全球死亡的主要原因，早期风险分层对于改善预后至关重要。人工智能衍生的心电图（AI-ECG）提供了一种有前途的方法来推导心脏生物学年龄作为非侵入性数字生物标记。本研究基于 ECGFounder 基础模型开发了一个 AI-ECG 框架，用于量化心脏生物衰老并预测心血管风险。总共包含来自 63,512 名英国生物银行参与者的 67,824 份心电图。该模型在健康个体的发育队列（n = 26,871）上进行训练，并在独立的临床评估队列（n = 40,953）中进行评估。 Cox比例风险模型用于评估AI-ECG年龄差距与主要不良心脑血管事件（MACCE）以及其他次要结局之间的关联。
- Abstract: Cardiovascular diseases remain the leading cause of global mortality, and early risk stratification is critical for improving prognosis. Artificial intelligence-derived electrocardiography (AI-ECG) provides a promising approach to deriving cardiac biological age as a non-invasive digital biomarker. This study developed an AI-ECG framework based on the ECGFounder foundation model to quantify cardiac biological aging...
- Summary (fallback): 机器翻译摘要显示：心血管疾病仍然是全球死亡的主要原因，早期风险分层对于改善预后至关重要。人工智能衍生的心电图（AI-ECG）提供了一种有前途的方法来推导心脏生物学年龄作为非侵入性数字生物标记。本研究基于 ECGFounder 基础模型开发了一个 AI-ECG 框架，用于量化心脏生物衰老并预测心血管风险。总共包含来自 63,512 名英国生物银行参与者的 67,824 份心电图。该模型在健康个体的发育队列（n = 26,871）上进行训练，并在独立的临床评估队列（n = 40,953）中进行评估。 Cox比例风险模型用于评估AI-ECG年龄差距与主要不良心脑血管事件（MACCE）以及其他次要结局之间的关联。
- Keywords: cardiovascular, cohort, risk, ai-ecg, macce

### 4. [2 岁时年龄和阶段问卷 3 评估的表现是否可以估计对 5 岁时早期基础阶段的影响？使用常规数据的纵向观察研究。](https://www.medrxiv.org/content/10.64898/2026.02.27.26347090v2)
- Original title: Does performance on the Ages and Stages Questionnaire-3 assessment at age 2 estimate the effect on the Early Years Foundation Stage at age 5? A longitudinal observational study using routine data.
- Authors: Dickerson, J., Xu, Y., Shore, R., Henderson, H., Lee, D. et al.
- Meta: 2026-07-08 | public and global health | DOI: 10.64898/2026.02.27.26347090
- 中文摘要: 简介 到 2025 年，提高 5 岁儿童在早期基础阶段概况 (EYFSP) 中达到良好发展水平 (GLD) 的比例成为英格兰的国家优先事项。本研究检验了 2 岁年龄和阶段问卷 3 (ASQ-3) 的表现是否可以评估对 EYFSP 的影响。方法 使用链接的互联约克郡（布拉德福德）数据创建纵向数据集。多元回归分析估计了 ​​ASQ-3 对 EYFSP 的影响，描述性分析探讨了 GLD 之间的重叠。结果 在 2013 年 9 月至 2023 年 5 月期间出生的 98,851 名儿童中，47,046 名 (48%) 拥有 ASQ-3 记录，6,021 名已关联 EYFSP 数据。在 ASQ-3 中获得 GLD 的儿童在 EYFSP 中获得 GLD 的几率是其三倍以上（OR 3.18，95% CI 2.70-3.75）。
- Abstract: Introduction Improving the proportion of children achieving a good level of development (GLD) on the Early Years Foundation Stage Profile (EYFSP) aged five became a national priority in England in 2025. This study examined whether performance on the Ages and Stages Questionnaire-3 (ASQ-3) aged two can estimate the effect on the EYFSP. Methods A longitudinal dataset was created using linked Connected Yorkshire (Bradf...
- Summary (fallback): 机器翻译摘要显示：简介 到 2025 年，提高 5 岁儿童在早期基础阶段概况 (EYFSP) 中达到良好发展水平 (GLD) 的比例成为英格兰的国家优先事项。本研究检验了 2 岁年龄和阶段问卷 3 (ASQ-3) 的表现是否可以评估对 EYFSP 的影响。方法 使用链接的互联约克郡（布拉德福德）数据创建纵向数据集。多元回归分析估计了 ​​ASQ-3 对 EYFSP 的影响，描述性分析探讨了 GLD 之间的重叠。结果 在 2013 年 9 月至 2023 年 5 月期间出生的 98,851 名儿童中，47,046 名 (48%) 拥有 ASQ-3 记录，6,021 名已关联 EYFSP 数据。在 ASQ-3 中获得 GLD 的儿童在 EYFSP 中获得 GLD 的几率是其三倍以上（OR 3.18，95% CI 2.70-3.75...
- Keywords: eyfsp, asq-3, children, achieve, early

### 5. [后来被诊断为自闭症的儿童在婴儿期早期阿尔法波段连接性发生了变化](https://www.medrxiv.org/content/10.64898/2026.06.25.26353501v1)
- Original title: Alterations in Early Alpha-band Connectivity emerge in Infancy among children later diagnosed with Autism
- Authors: Chung, H., An, W. W., Wilkinson, C. L., Davila Mejia, G., Tager-Flusberg, H. et al.
- Meta: 2026-07-08 | neurology | DOI: 10.64898/2026.06.25.26353501
- 中文摘要: 自闭症是一种异质性神经发育疾病，通常伴随着语言和认知发展的挑战。尽管非典型功能连接（FC）在自闭症中已有报道，但其首次出现的时间及其与以后行为的相关性仍然知之甚少。在这项研究中，我们研究了生命前三年 α 波段 FC 和网络组织的发展轨迹。我们计算了全局 α 波段测量值，包括峰值 α 连接频率 (PACF)、平均 FC、聚类系数和模块性，以表征从 238 名自闭症儿童（3 至 36 个月大）和非自闭症儿童（LL-noAutism；n=180）收集的纵向脑电图的非线性发育轨迹。基于网络的统计数据（NBS-预测）确定了导致每个年龄段群体差异的子网络。
- Abstract: Autism is a heterogeneous neurodevelopmental condition, often accompanied by challenges in language and cognitive development. Although atypical functional connectivity (FC) has been reported in autism, the timing of when it first emerges and its relevance for later behavior remain poorly understood. In this study, we examined developmental trajectories of alpha-band FC and network organization across the first thre...
- Summary (fallback): 机器翻译摘要显示：自闭症是一种异质性神经发育疾病，通常伴随着语言和认知发展的挑战。尽管非典型功能连接（FC）在自闭症中已有报道，但其首次出现的时间及其与以后行为的相关性仍然知之甚少。在这项研究中，我们研究了生命前三年 α 波段 FC 和网络组织的发展轨迹。我们计算了全局 α 波段测量值，包括峰值 α 连接频率 (PACF)、平均 FC、聚类系数和模块性，以表征从 238 名自闭症儿童（3 至 36 个月大）和非自闭症儿童（LL-noAutism；n=180）收集的纵向脑电图的非线性发育轨迹。基于网络的统计数据（NBS-预测）确定了导致每个年龄段群体差异的子网络。
- Keywords: autism, alpha-band, connectivity, later, developmental

### 6. [大型语言模型辅助工作流程，用于生成气候敏感食源性疾病的活证据库](https://www.medrxiv.org/content/10.64898/2026.07.04.26357263v1)
- Original title: A large language model-assisted workflow for generating a living evidence base for climate-sensitive foodborne disease
- Authors: Elson, R., McIntyre, K. M., Hardingham, M. B., Luechtefeld, T., Lake, I. R.
- Meta: 2026-07-08 | health informatics | DOI: 10.64898/2026.07.04.26357263
- 中文摘要: 摘要 气候变化正在改变影响食源性疾病传播的环境条件，但传统的系统评价无法跟上不断扩大的证据的步伐。我们评估了法学硕士辅助的工作流程是否可以为气候敏感的食源性疾病生成快速、可重复且与政策相关的活证据基础。我们在 SysRev 平台内结合了结构化 PubMed 搜索（2010-2023）、黄金标准人类标签以及基于 GPT?4?Turbo? 的自动贴标机的迭代细化。对英国公共卫生具有重要意义的病原体是预先选择的。使用召回率、精确度、特异性、准确度和平衡准确度来针对人类评审员评估模型性能。
- Abstract: Abstract Climate change is altering environmental conditions that influence foodborne disease transmission, yet traditional systematic reviews cannot keep pace with expanding evidence. We assessed whether an LLM-assisted workflow could generate a rapid, repeatable, and policy-relevant living evidence base for climate-sensitive foodborne disease. We combined structured PubMed searches (2010-2023), gold-standard human...
- Summary (fallback): 机器翻译摘要显示：摘要 气候变化正在改变影响食源性疾病传播的环境条件，但传统的系统评价无法跟上不断扩大的证据的步伐。我们评估了法学硕士辅助的工作流程是否可以为气候敏感的食源性疾病生成快速、可重复且与政策相关的活证据基础。我们在 SysRev 平台内结合了结构化 PubMed 搜索（2010-2023）、黄金标准人类标签以及基于 GPT?4?Turbo? 的自动贴标机的迭代细化。对英国公共卫生具有重要意义的病原体是预先选择的。使用召回率、精确度、特异性、准确度和平衡准确度来针对人类评审员评估模型性能。
- Keywords: evidence, foodborne, disease, middle, workflow

### 7. [伊朗德黑兰城市居民预防德国小蠊感染的行为决定因素](https://www.medrxiv.org/content/10.64898/2026.07.04.26357085v1)
- Original title: Behavioral determinants of preventive practices against German cockroach infestation among urban residents in Tehran, Iran
- Authors: Moshavernia, S., Azarm, A., Bagherzade, S., Karimi, M., Ghaem Maralani, H. et al.
- Meta: 2026-07-08 | health informatics | DOI: 10.64898/2026.07.04.26357085
- 中文摘要: 背景德国小蠊（Blattella germanica）侵扰是一种重要的城市环境健康威胁，与食品污染、过敏性疾病和生活质量下降有关。长期防治不仅取决于专业的害虫管理，还取决于居民的知识和预防行为。本研究评估了伊朗德黑兰城市居民与德国小蠊感染相关的知识、健康信念模型 (HBM) 构建、自我效能和预防实践。方法 在这项横断面研究中，从德黑兰有执照的害虫防治公司招募了 120 名经专业证实患有家庭德国小蠊感染的成年人。使用包含 39 项 HBM 的问卷整理数据，评估知识、感知易感性、感知严重性、感知益处、感知障碍、自我效能和预防实践……
- Abstract: Background German cockroach (Blattella germanica) infestation is an important urban environmental health menace associated with food contamination, allergic disease, and reduced quality of life. Long-term control depends not only on professional pest management, but also on residents knowledge and preventive behaviors. This study assessed the knowledge, Health belief model (HBM) constructs, self-efficacy, and preven...
- Summary (fallback): 机器翻译摘要显示：背景德国小蠊（Blattella germanica）侵扰是一种重要的城市环境健康威胁，与食品污染、过敏性疾病和生活质量下降有关。长期防治不仅取决于专业的害虫管理，还取决于居民的知识和预防行为。本研究评估了伊朗德黑兰城市居民与德国小蠊感染相关的知识、健康信念模型 (HBM) 构建、自我效能和预防实践。方法 在这项横断面研究中，从德黑兰有执照的害虫防治公司招募了 120 名经专业证实患有家庭德国小蠊感染的成年人。使用包含 39 项 HBM 的问卷整理数据，评估知识、感知易感性、感知严重性、感知益处、感知障碍、自我效能和预防实践……
- Keywords: preventive, knowledge, practices, cockroach, perceived

### 8. [咖啡摄入量与改善胰岛素敏感性和降低内脏肥胖有关：来自生物标志物和遗传分析的证据](https://www.medrxiv.org/content/10.64898/2026.06.25.26356610v1)
- Original title: Coffee Intake is Associated with Improved Insulin Sensitivity and Lower Visceral Adiposity: Evidence from Biomarker and Genetic Analysis
- Authors: Sevilla-Gonzalez, M., Wang, X., Yun, H., Mei, Z., Hsu, S. et al.
- Meta: 2026-07-08 | endocrinology | DOI: 10.64898/2026.06.25.26356610
- 中文摘要: 重要性：较高的咖啡摄入量与较低的 2 型糖尿病 (T2D) 风险相关，但其潜在的生物学途径仍不完全清楚。目的：研究咖啡摄入量与胰岛素敏感性、肥胖和 T2D 风险之间的关联，并评估咖啡摄入量是否改变途径特异性遗传易感性与 T2D 事件之间的关联。设计、背景和参与者：对维生素 D 和 OmegA-3 TriaL (VITAL) 临床亚队列中 806 名无 T2D 的参与者进行横断面分析，这些参与者在基线和第 2 年接受了重复的饮食评估、临床表型分析和双能 X 射线吸收测量成像。对 333,053 名基线时没有 T2D 的英国生物银行参与者进行前瞻性分析，他们有饮食和遗传数据，随访时间中位数为 13.3 年。
- Abstract: Importance: Higher coffee intake has been associated with lower risk of type 2 diabetes (T2D), but the underlying biological pathways remain incompletely understood. Objective: To examine associations of coffee intake with insulin sensitivity, adiposity, and T2D risk, and assess whether coffee intake modifies associations between pathway-specific genetic susceptibility and incident T2D. Design, Setting, and Particip...
- Summary (fallback): 机器翻译摘要显示：重要性：较高的咖啡摄入量与较低的 2 型糖尿病 (T2D) 风险相关，但其潜在的生物学途径仍不完全清楚。目的：研究咖啡摄入量与胰岛素敏感性、肥胖和 T2D 风险之间的关联，并评估咖啡摄入量是否改变途径特异性遗传易感性与 T2D 事件之间的关联。设计、背景和参与者：对维生素 D 和 OmegA-3 TriaL (VITAL) 临床亚队列中 806 名无 T2D 的参与者进行横断面分析，这些参与者在基线和第 2 年接受了重复的饮食评估、临床表型分析和双能 X 射线吸收测量成像。对 333,053 名基线时没有 T2D 的英国生物银行参与者进行前瞻性分析，他们有饮食和遗传数据，随访时间中位数为 13.3 年。
- Keywords: coffee, intake, lower, insulin, higher

### 9. [美国学术牙科护理中与艰难梭菌感染相关的抗生素暴露的种族和民族差异](https://www.medrxiv.org/content/10.64898/2026.06.25.26356622v1)
- Original title: Racial and Ethnic Differences in Exposure to Antibiotics Associated with Clostridioides difficile Infection in US Academic Dental Care
- Authors: Gladden, A. D., Westgard, L. K., Tam, R. A., Ugbala, M. C., Foong, K. S. et al.
- Meta: 2026-07-08 | epidemiology | DOI: 10.64898/2026.06.25.26356622
- 中文摘要: 背景 严重艰难梭菌感染 (CDI) 的发病率和死亡率对美国黑人和西班牙裔患者影响尤为严重。抗生素暴露是 CDI 的主要可改变危险因素，而克林霉素是与相关危害最密切相关的药物之一。描述处方中的不平等现象至关重要。牙科是克林霉素处方的主要来源。学术牙科诊所为不同的患者群体提供服务，并为评估跨种族和族裔群体的处方提供了理想的环境。因此，我们检查了抗生素使用和累积克林霉素暴露作为 CDI 相关风险的衡量标准。方法 我们对 2021 年至 2023 年 5 家美国学术牙科机构的电子健康记录进行了回顾性研究。
- Abstract: Background Severe Clostridioides difficile infection (CDI) morbidity and mortality disproportionately affect Black and Hispanic patients in the United States. Antibiotic exposure is the primary modifiable risk factor for CDI, and clindamycin is among the agents most strongly associated with related harm. Characterizing inequities in prescribing is critical. Dentistry is a major source of clindamycin prescriptions. A...
- Summary (fallback): 机器翻译摘要显示：背景 严重艰难梭菌感染 (CDI) 的发病率和死亡率对美国黑人和西班牙裔患者影响尤为严重。抗生素暴露是 CDI 的主要可改变危险因素，而克林霉素是与相关危害最密切相关的药物之一。描述处方中的不平等现象至关重要。牙科是克林霉素处方的主要来源。学术牙科诊所为不同的患者群体提供服务，并为评估跨种族和族裔群体的处方提供了理想的环境。因此，我们检查了抗生素使用和累积克林霉素暴露作为 CDI 相关风险的衡量标准。方法 我们对 2021 年至 2023 年 5 家美国学术牙科机构的电子健康记录进行了回顾性研究。
- Keywords: antibiotic, clindamycin, exposure, dental, patients
