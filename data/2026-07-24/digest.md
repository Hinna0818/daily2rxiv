# daily2rxiv Digest - 2026-07-24

共收录 64 篇论文。

## arxiv

### 1. [具有隐式和显式几何形状的 3D 感知 VLM](https://arxiv.org/abs/2607.21595v1)
- Original title: 3D-Aware VLMs with Implicit and Explicit Geometries
- Authors: Wenhao Li, Xueying Jiang, Quanhao Qian, Deli Zhao, Ran Xu et al.
- Meta: 2026-07-23 | cs.CV
- 中文摘要: 尽管进展迅速，但大多数现有的基于 2D 视觉输入构建的视觉语言模型 (VLM) 在处理需要细粒度空间理解和推理的各种 3D 任务时常常遇到困难。为了弥补这一差距，我们提出了 VLM-IE3D，这是一个统一的框架，通过为 VLM 配备从 RGB 视频中学习到的隐式和显式 3D 几何图形来增强 VLM 的 3D 空间感知。我们的 VLM-IE3D 引入了隐式几何标记 (IGT)，可从输入视频中捕获高级几何先验；以及互补的显式几何标记 (EGT)，可根据重建的 3D 属性对详细几何结构进行编码。最重要的是，VLM-IE3D 配备了 3D 感知适配器，可有效地将两种类型的几何表示与 2D 视觉提示融合在一起。
- Abstract: Despite rapid progress, most existing vision-language models (VLMs) built from 2D visual inputs often struggle when handling various 3D tasks that require fine-grained spatial understanding and reasoning. To bridge this gap, we present VLM-IE3D, a unified framework that enhances the 3D spatial awareness of VLMs by equipping them with both implicit and explicit 3D geometries learned from RGB videos. Our VLM-IE3D intr...
- Summary (fallback): 机器翻译摘要显示：尽管进展迅速，但大多数现有的基于 2D 视觉输入构建的视觉语言模型 (VLM) 在处理需要细粒度空间理解和推理的各种 3D 任务时常常遇到困难。为了弥补这一差距，我们提出了 VLM-IE3D，这是一个统一的框架，通过为 VLM 配备从 RGB 视频中学习到的隐式和显式 3D 几何图形来增强 VLM 的 3D 空间感知。我们的 VLM-IE3D 引入了隐式几何标记 (IGT)，可从输入视频中捕获高级几何先验；以及互补的显式几何标记 (EGT)，可根据重建的 3D 属性对详细几何结构进行编码。最重要的是，VLM-IE3D 配备了 3D 感知适配器，可有效地将两种类型的几何表示与 2D 视觉提示融合在一起。
- Keywords: vlm-ie3d, spatial, vlms, implicit, explicit

### 2. [扩展流程图](https://arxiv.org/abs/2607.21585v1)
- Original title: Expanding Flow Maps
- Authors: Sophia Tang, Pranam Chatterjee
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 基于流的生成模型在连续和离散状态空间的快速、可控生成方面取得了显着进展，但现有的参数化仅限于固定维度或固定序列长度。在这里，我们引入扩展生成流（EFlows），它定义沿着扩展插值的维度增加的分布之间的流，该插值通过用条件噪声增强状态来增长状态。在此结构的基础上，我们提出了扩展流图（EFM），这是一类新的流图，它将扩展插值提炼成高效的少步生成模型。
- Abstract: Flow-based generative models have enabled remarkable progress in fast and controllable generation across continuous and discrete state spaces, yet existing parameterizations are constrained to fixed dimensions or fixed sequence lengths. Here, we introduce Expanding Generative Flows (EFlows), which define flows between distributions of increasing dimensionality along an expanding interpolant that grows the state by a...
- Summary (fallback): 机器翻译摘要显示：基于流的生成模型在连续和离散状态空间的快速、可控生成方面取得了显着进展，但现有的参数化仅限于固定维度或固定序列长度。在这里，我们引入扩展生成流（EFlows），它定义沿着扩展插值的维度增加的分布之间的流，该插值通过用条件噪声增强状态来增长状态。在此结构的基础上，我们提出了扩展流图（EFM），这是一类新的流图，它将扩展插值提炼成高效的少步生成模型。
- Keywords: state, expanding, which, flow, maps

### 3. [Barzilai-Borwein 在每维 $n\geq 4$ 的开二次方程组上超线性收敛失败](https://arxiv.org/abs/2607.21579v1)
- Original title: Barzilai-Borwein Fails Superlinear Convergence on an Open Set of Quadratics for Every Dimension $n\geq 4$
- Authors: Dawei Li, Xiaotian Jiang, Mingyi Hong
- Meta: 2026-07-23 | math.OC
- 中文摘要: Barzilai--Borwein (BB) 方法在连续优化方面表现出了很强的实用性能，但其收敛动力学仍然知之甚少。特别是，一个未解决的核心问题是 BB 是否对于几乎每个严格凸二次问题和初始化都超线性收敛。我们对这个问题给出否定的答案。具体来说，对于每个有限维度 $n\geq4$，我们构造一个非空开集，即正勒贝格测度，严格凸二次问题族和长 Barzilai-Borwein 方法 (BB1) 收敛但不能收敛根超线性的初始点。更准确地说，使用显式常数 $ρ_{\min}=10^{-6},ρ_{\max}=0.61$，梯度的每个谱分量都以相应的几何序列上下为界。
- Abstract: Barzilai--Borwein (BB) method has shown strong practical performance in continuous optimization, yet its convergence dynamics remains poorly understood. In particular, a central unresolved question is whether BB converges superlinearly for almost every strictly convex quadratic problem and initialization. We provide a negative answer to this question. Specifically, for every finite dimension $n\geq4$, we construct a...
- Summary (fallback): 机器翻译摘要显示：Barzilai--Borwein (BB) 方法在连续优化方面表现出了很强的实用性能，但其收敛动力学仍然知之甚少。特别是，一个未解决的核心问题是 BB 是否对于几乎每个严格凸二次问题和初始化都超线性收敛。我们对这个问题给出否定的答案。具体来说，对于每个有限维度 $n\geq4$，我们构造一个非空开集，即正勒贝格测度，严格凸二次问题族和长 Barzilai-Borwein 方法 (BB1) 收敛但不能收敛根超线性的初始点。更准确地说，使用显式常数 $ρ_{\min}=10^{-6},ρ_{\max}=0.61$，梯度的每个谱分量都以相应的几何序列上下为界。
- Keywords: every, convergence, dimension, geometric, superlinear

### 4. [用于凹版印刷质量控制自动化的综合数据生成框架](https://arxiv.org/abs/2607.21577v1)
- Original title: Synthetic data generation framework for quality control automation in gravure printing
- Authors: Korota Arsène Coulibaly, Mohamed Hamlich, Khalid Hmali, Andrea Trombin
- Meta: 2026-07-23 | cs.CV
- 中文摘要: 印刷中的质量控制，特别是凹版印刷中的质量控制，仍然依赖于缓慢、昂贵且主观的手动检查。自动表面缺陷检测对于维持凹版印刷的高质量标准至关重要。深度学习模型为自动化带来了前景。然而，训练强大的深度学习模型（例如 YOLO 或 Vision Transformers）却因现实世界工业缺陷图像的极度稀缺而受到严重阻碍。为了克服这一限制，本文介绍了一种专为凹版印刷质量控制而定制的新型合成数据生成框架。所提出的管道自动生成特定印刷缺陷（折痕、条纹、套准不准等）的高保真图像，并输出相应的边界框和注释。
- Abstract: Quality control in printing, particularly in rotogravure printing, still depends on slow, costly, and subjective manual inspection. Automated surface defect detection is critical for maintaining high-quality standards in rotogravure printing. Deep learning models give prospects for automation. However, training robust deep learning models, such as YOLO or Vision Transformers, is heavily hindered by the extreme scarc...
- Summary (fallback): 机器翻译摘要显示：印刷中的质量控制，特别是凹版印刷中的质量控制，仍然依赖于缓慢、昂贵且主观的手动检查。自动表面缺陷检测对于维持凹版印刷的高质量标准至关重要。深度学习模型为自动化带来了前景。然而，训练强大的深度学习模型（例如 YOLO 或 Vision Transformers）却因现实世界工业缺陷图像的极度稀缺而受到严重阻碍。为了克服这一限制，本文介绍了一种专为凹版印刷质量控制而定制的新型合成数据生成框架。所提出的管道自动生成特定印刷缺陷（折痕、条纹、套准不准等）的高保真图像，并输出相应的边界框和注释。
- Keywords: printing, synthetic, framework, quality, control

### 5. [超越充分性：具有反事实必要性的时间序列解释](https://arxiv.org/abs/2607.21573v1)
- Original title: Beyond Sufficiency: Time Series Explanation with Counterfactual Necessity
- Authors: Hongnan Ma, Yiwei Shi, Mengyue Yang, Weiru Liu
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 对时间序列分类器的忠实解释应该确定子序列，这些子序列不仅足以保留黑盒模型的预测，而且对于维护它也是必要的。然而，现有的面向充分性的方法可以高度重视支持预测的虚假子序列，但对模型的决策来说并不重要。我们引入 \textbf{TimePNS}，一个用于时间序列解释的必要性感知框架。受 Pearl 的反事实必要性概念的启发，TimePNS 通过干预时间因素并测量原始预测是否被破坏来评估时间因素是否必要。该框架采用两阶段设计。第一阶段学习可识别的因果生成过程以及面向充分性的解释面具。
- Abstract: Faithful explanations of time-series classifiers should identify subsequences that are not only sufficient to preserve a black-box model's prediction, but also necessary for maintaining it. However, existing sufficiency-oriented methods can assign high importance to spurious subsequences that support the prediction without being essential to the model's decision. We introduce \textbf{TimePNS}, a necessity-aware fram...
- Summary (fallback): 机器翻译摘要显示：对时间序列分类器的忠实解释应该确定子序列，这些子序列不仅足以保留黑盒模型的预测，而且对于维护它也是必要的。然而，现有的面向充分性的方法可以高度重视支持预测的虚假子序列，但对模型的决策来说并不重要。我们引入 \textbf{TimePNS}，一个用于时间序列解释的必要性感知框架。受 Pearl 的反事实必要性概念的启发，TimePNS 通过干预时间因素并测量原始预测是否被破坏来评估时间因素是否必要。该框架采用两阶段设计。第一阶段学习可识别的因果生成过程以及面向充分性的解释面具。
- Keywords: explanation, counterfactual, necessity, time-series, subsequences

### 6. [MedGame：医学教育大型语言模型支持的讲故事游戏化](https://arxiv.org/abs/2607.21570v1)
- Original title: MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education
- Authors: Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao et al.
- Meta: 2026-07-23 | cs.CL
- 中文摘要: 大型语言模型（LLM）显示出医学教育的前景，但大多数现有系统侧重于本地化交互，例如问答或单轮反馈，而不是将整个临床案例组织成以决策为中心的学习轨迹。我们引入了 \textit{MedGame}，一个将静态临床案例转化为结构化、可执行的讲故事游戏的框架。 MedGame 采用双引擎设计：医学叙事设计师将基于案例的临床故事情节与状态和决策节点综合起来，而故事导演将它们转换为由我们发布的交互式平台呈现的依赖关系感知的多模式编排计划。我们构建了 MedGame Bench，这是一个用于医学叙事生成和故事指导的 5,000 个案例基准和评估协议。
- Abstract: Large Language Models (LLMs) show promise for medical education, but most existing systems focus on localized interactions such as question answering or single-turn feedback, rather than organizing an entire clinical case into a decision-centered learning trajectory. We introduce \textit{MedGame}, a framework that transforms static clinical cases into structured, executable storytelling games. MedGame uses a dual-en...
- Summary (fallback): 机器翻译摘要显示：大型语言模型（LLM）显示出医学教育的前景，但大多数现有系统侧重于本地化交互，例如问答或单轮反馈，而不是将整个临床案例组织成以决策为中心的学习轨迹。我们引入了 \textit{MedGame}，一个将静态临床案例转化为结构化、可执行的讲故事游戏的框架。 MedGame 采用双引擎设计：医学叙事设计师将基于案例的临床故事情节与状态和决策节点综合起来，而故事导演将它们转换为由我们发布的交互式平台呈现的依赖关系感知的多模式编排计划。我们构建了 MedGame Bench，这是一个用于医学叙事生成和故事指导的 5,000 个案例基准和评估协议。
- Keywords: medgame, medical, models, clinical, storytelling

### 7. [环肽系综的图学习：分子系综建模的研究](https://arxiv.org/abs/2607.21561v1)
- Original title: Graph Learning on Ensembles of Cyclic Peptides: An Investigation of Molecular Ensemble Modeling
- Authors: Aaron Feller, Kris Deibler, Maxim Secor
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 从结构预测分子性质通常使用单个代表性构象，即使许多分子在溶液中作为构象集合存在。我们引入了 EnsembleEGNN，这是一种分子集成基础模型，它通过首先使用共享等变图神经网络 (EGNN) 层对每个构象异构体进行编码，然后将所得的构象异构体表示与设置注意力块进行池化来对集成进行编码。我们使用结合了掩蔽标记恢复、噪声坐标重建和成对距离重建的多任务自监督目标，在 CREMP（一个环肽集成数据集）上对模型进行预训练。在 CREMP-CycPeptMPDB 数据集上，从头开始训练 EnsembleEGNN 完全失败 ($R^2=0.005$)。然而，预训练模型达到 $R^2=0.477$ 和 Pearson $r=0.699$，优于仅序列 BERT 基线（$R^2=0.439$，Pearson $r=0.667$）。
- Abstract: Molecular property prediction from structure often uses a single representative conformation, even though many molecules exist as conformational ensembles in solution. We introduce EnsembleEGNN, a molecular ensemble foundation model that encodes an ensemble by first encoding each conformer with shared Equivariant Graph Neural Network (EGNN) layers, then pooling the resulting conformer representations with a Set Atte...
- Summary (fallback): 机器翻译摘要显示：从结构预测分子性质通常使用单个代表性构象，即使许多分子在溶液中作为构象集合存在。我们引入了 EnsembleEGNN，这是一种分子集成基础模型，它通过首先使用共享等变图神经网络 (EGNN) 层对每个构象异构体进行编码，然后将所得的构象异构体表示与设置注意力块进行池化来对集成进行编码。我们使用结合了掩蔽标记恢复、噪声坐标重建和成对距离重建的多任务自监督目标，在 CREMP（一个环肽集成数据集）上对模型进行预训练。在 CREMP-CycPeptMPDB 数据集上，从头开始训练 EnsembleEGNN 完全失败 ($R^2=0.005$)。然而，预训练模型达到 $R^2=0.477$ 和 Pearson $r=0.699$，优于仅序列 BERT 基线（$R^2=0.439$，Pearson $r=0.667$）。
- Keywords: ensemble, model, ensembles, molecular, ensembleegnn

### 8. [加纳时空疟疾发病率的无监督共识异常检测](https://arxiv.org/abs/2607.21559v1)
- Original title: Unsupervised Consensus-Based Anomaly Detection for Spatiotemporal Malaria Incidence in Ghana
- Authors: T. Ansah-Narh, Y. Asare Afrane
- Meta: 2026-07-23 | cs.AI
- 中文摘要: 将共识异常检测框架应用于加纳（2014-2023）的每月疟疾监测数据，以识别非典型传播模式。异常在空间和时间上是高度结构化的。阿散蒂和北部地区是最经常发生异常的地区，其中塔马利、库马西和阿克拉的热点地区持续存在。一个关键发现是异常负担（异常期间的累积病例）和异常频率（异常行为的持续存在）之间的空间区别。异常期间，玉米粉蒸肉的负担最高，而异常发生率最高的地区集中在阿散蒂地区，这表明高负担地区不一定是异常传播最频繁的地区。异常月份形成了一个统计上不同的群体，与正常月份相比，病例数要高得多（Cohen $d = 3.252$），并且季节性偏差较大（$d > 1.2$）。
- Abstract: A consensus anomaly detection framework was applied to monthly malaria surveillance data from Ghana (2014-2023) to identify atypical transmission patterns. Anomalies were highly structured in space and time. Ashanti and Northern Regions accounted for most recurrent anomalies, with persistent hotspots at Tamale, Kumasi, and Accra. A key finding was the spatial distinction between anomaly burden (cumulative cases duri...
- Summary (fallback): 机器翻译摘要显示：将共识异常检测框架应用于加纳（2014-2023）的每月疟疾监测数据，以识别非典型传播模式。异常在空间和时间上是高度结构化的。阿散蒂和北部地区是最经常发生异常的地区，其中塔马利、库马西和阿克拉的热点地区持续存在。一个关键发现是异常负担（异常期间的累积病例）和异常频率（异常行为的持续存在）之间的空间区别。异常期间，玉米粉蒸肉的负担最高，而异常发生率最高的地区集中在阿散蒂地区，这表明高负担地区不一定是异常传播最频繁的地区。异常月份形成了一个统计上不同的群体，与正常月份相比，病例数要高得多（Cohen $d = 3.252$），并且季节性偏差较大（$d > 1.2$）。
- Keywords: anomaly, malaria, transmission, anomalies, burden

### 9. [MIRROR：从其他视角学习多模态推理](https://arxiv.org/abs/2607.21552v1)
- Original title: MIRROR: Learning from the Other View for Multi-Modal Reasoning
- Authors: Wen Ye, Yuxiao Qu, Aviral Kumar, Xuezhe Ma
- Meta: 2026-07-23 | cs.AI
- 中文摘要: 与表现出强大推理能力的大型语言模型 (LLM) 不同，视觉语言模型 (VLM) 很难进行视觉推理，即使是在允许等效文本、图表以及图表+文本组合视图的几何问题上也是如此。我们表明，这些视图通常会引发不同的行为：模型可能从文本解决问题，但在相应的图表上失败，或者在视觉上成功，但在文本上失败。这种不一致表明，不同的观点暴露了标准多模式后训练没有充分利用的互补推理路径和故障模式。为了研究和利用这种现象，我们构建了 ODA-Data，这是一个高质量的配对多模态几何数据集，具有相同问题的文本主导、图像主导和组合图像+文本视图，以及用于训练和评估模态依赖推理行为的分割。
- Abstract: Unlike large language models (LLMs) that exhibit strong reasoning capabilities, vision-language models (VLMs) struggle with visual reasoning, even on geometry problems that admit equivalent text, diagram, and combined diagram+text views. We show that these views often elicit different behaviors: a model may solve a problem from text but fail on the corresponding diagram, or succeed visually while failing textually....
- Summary (fallback): 机器翻译摘要显示：与表现出强大推理能力的大型语言模型 (LLM) 不同，视觉语言模型 (VLM) 很难进行视觉推理，即使是在允许等效文本、图表以及图表+文本组合视图的几何问题上也是如此。我们表明，这些视图通常会引发不同的行为：模型可能从文本解决问题，但在相应的图表上失败，或者在视觉上成功，但在文本上失败。这种不一致表明，不同的观点暴露了标准多模式后训练没有充分利用的互补推理路径和故障模式。为了研究和利用这种现象，我们构建了 ODA-Data，这是一个高质量的配对多模态几何数据集，具有相同问题的文本主导、图像主导和组合图像+文本视图，以及用于训练和评估模态依赖推理行为的分割。
- Keywords: reasoning, views, mirror, text, geometry

### 10. [X$^3$-OPD：通过策略对齐将推理提炼为大型音频语言模型](https://arxiv.org/abs/2607.21550v1)
- Original title: X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment
- Authors: Dongjie Fu, Di Cao, Xize Cheng, Zihan Zhang, Wenxu Jia et al.
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 虽然大型音频语言模型在听觉感知方面取得了显着的进步，但在深度逻辑推理方面仍然落后于基于文本的大型语言模型，这主要是由于高质量音频推理数据的稀缺。为了弥补这一差距，我们提出了 X$^3$-OPD，这是一种跨模式的策略蒸馏框架，可将推理能力从强大的文本教师转移到音频语言学生。在训练过程中，学生根据自己的声学感知生成推理轨迹，而教师则使用匹配的文本输入和经过验证的答案提供标记级指导。我们进一步构建了一个三层对称语料库，涵盖渲染为语音的文本推理、基于复杂声学场景的音频事件推理以及涉及副语言线索的口语对话推理。
- Abstract: While large audio-language models have achieved remarkable progress in auditory perception, they still lag behind text-based large language models in deep logical reasoning, primarily due to the scarcity of high-quality audio reasoning data. To bridge this gap, we propose X$^3$-OPD, a cross-modal on-policy distillation framework that transfers reasoning capabilities from a powerful text teacher to an audio-language...
- Summary (fallback): 机器翻译摘要显示：虽然大型音频语言模型在听觉感知方面取得了显着的进步，但在深度逻辑推理方面仍然落后于基于文本的大型语言模型，这主要是由于高质量音频推理数据的稀缺。为了弥补这一差距，我们提出了 X$^3$-OPD，这是一种跨模式的策略蒸馏框架，可将推理能力从强大的文本教师转移到音频语言学生。在训练过程中，学生根据自己的声学感知生成推理轨迹，而教师则使用匹配的文本输入和经过验证的答案提供标记级指导。我们进一步构建了一个三层对称语料库，涵盖渲染为语音的文本推理、基于复杂声学场景的音频事件推理以及涉及副语言线索的口语对话推理。
- Keywords: reasoning, large, audio-language, models, while

### 11. [鬼胶子耦合戴森--兰道规范中施温格方程的神经解](https://arxiv.org/abs/2607.21548v1)
- Original title: Neural solutions of coupled ghost and gluon Dyson--Schwinger equations in Landau gauge
- Authors: Rodrigo Carmo Terin
- Meta: 2026-07-23 | hep-ph
- 中文摘要: 四维朗道规范杨-米尔斯 (YM) 理论的耦合鬼和胶子 Dyson-Schwinger 方程 (DSE) 通过仅根据重正化方程残差训练的神经表示来求解。神经解和定点解在百分比水平上一致，并且在初始化、网络大小、积分网格和红外边界条件的变化下保持稳定。三胶子顶点模型的变化产生的影响比神经误差大得多。 MiniMOM 紫外运行和胶子施温格函数的符号变化也在截断的限制内再现。
- Abstract: The coupled ghost and gluon Dyson--Schwinger equations (DSEs) of four-dimensional Landau-gauge Yang--Mills (YM) theory are solved with a neural representation trained only from renormalized equation residuals. The neural and fixed-point solutions agree at the percent level and remain stable under changes of initialization, network size, integration grid, and infrared boundary condition. Variations of the three-gluon...
- Summary (fallback): 机器翻译摘要显示：四维朗道规范杨-米尔斯 (YM) 理论的耦合鬼和胶子 Dyson-Schwinger 方程 (DSE) 通过仅根据重正化方程残差训练的神经表示来求解。神经解和定点解在百分比水平上一致，并且在初始化、网络大小、积分网格和红外边界条件的变化下保持稳定。三胶子顶点模型的变化产生的影响比神经误差大得多。 MiniMOM 紫外运行和胶子施温格函数的符号变化也在截断的限制内再现。
- Keywords: neural, gluon, solutions, coupled, ghost

### 12. [自动化的边界：人类持续参与的理论](https://arxiv.org/abs/2607.21547v1)
- Original title: The Boundaries of Automation: A Theory of Persistent Human Participation
- Authors: Fares Fourati, Hinrich Schütze, Eyke Hüllermeier, Iryna Gurevych
- Meta: 2026-07-23 | cs.AI
- 中文摘要: 人工智能的快速进步强化了人们长期以来对自动化的追求：尽可能用算法代替人类参与。这种追求隐含着这样的假设：人类之所以留在循环中，只是因为当前的人工智能系统还没有足够的能力。本文挑战了这一假设。我们不是问自动化可以延伸多远，而是问它的概念限制在哪里，并认为即使使用高性能的人工智能系统，人类的参与也可能持续存在，原因有三个。当人类贡献人工智能无法提供的能力或观点时，技术或互补性就会出现。当参与本身对人类能动性或学习有价值时，就会出现规范或发展的基础。
- Abstract: The rapid progress of AI has intensified the long-standing pursuit of automation: replacing human participation with algorithms wherever possible. Implicit in this pursuit is the assumption that humans remain in the loop only because current AI systems are not yet sufficiently capable. This paper challenges that assumption. Rather than asking how far automation can extend, we ask where its conceptual limits lie and...
- Summary (fallback): 机器翻译摘要显示：人工智能的快速进步强化了人们长期以来对自动化的追求：尽可能用算法代替人类参与。这种追求隐含着这样的假设：人类之所以留在循环中，只是因为当前的人工智能系统还没有足够的能力。本文挑战了这一假设。我们不是问自动化可以延伸多远，而是问它的概念限制在哪里，并认为即使使用高性能的人工智能系统，人类的参与也可能持续存在，原因有三个。当人类贡献人工智能无法提供的能力或观点时，技术或互补性就会出现。当参与本身对人类能动性或学习有价值时，就会出现规范或发展的基础。
- Keywords: participation, human, automation, systems, humans

### 13. [UnDA：医学成像中跨模态知识转移的不成对域对齐](https://arxiv.org/abs/2607.21546v1)
- Original title: UnDA: Unpaired Domain Alignment for Cross-Modal Knowledge Transfer in Medical Imaging
- Authors: Rafsan Jany, Shadab Tanjeed Ahmad, Ahsan Bulbul, Tahsinul Islam, Md Azam Hossain et al.
- Meta: 2026-07-23 | cs.CV
- 中文摘要: 基于多模态的方法在下游任务中通常优于单一模态方法，因为不同的模态提供了互补的信息，但获取配对的临床数据在现实世界中仍然是一个重大挑战。虽然跨模态知识蒸馏解决了这个问题，但现有的方法常常面临较大的模态差距和来自不确定源域预测的噪声传播的问题。为了克服这些挑战，我们提出了 UnDA，一种用于不配对跨模式蒸馏的锚引导框架。我们的方法引入了一个与主干网无关的对齐模块，该模块通过基于注意力的池机制提取语义结构的类标记。
- Abstract: Multimodal based approaches often outperform single modality approaches in downstream tasks as the different modalities provide complementary information, yet acquiring paired clinical data remains a significant challenge in real world scenarios. While cross-modal knowledge distillation addresses this, existing methods often struggle with large modality gaps and the propagation of noise from uncertain source-domain...
- Summary (fallback): 机器翻译摘要显示：基于多模态的方法在下游任务中通常优于单一模态方法，因为不同的模态提供了互补的信息，但获取配对的临床数据在现实世界中仍然是一个重大挑战。虽然跨模态知识蒸馏解决了这个问题，但现有的方法常常面临较大的模态差距和来自不确定源域预测的噪声传播的问题。为了克服这些挑战，我们提出了 UnDA，一种用于不配对跨模式蒸馏的锚引导框架。我们的方法引入了一个与主干网无关的对齐模块，该模块通过基于注意力的池机制提取语义结构的类标记。
- Keywords: unpaired, knowledge, alignment, cross-modal, modality

### 14. [零流量双样本测试](https://arxiv.org/abs/2607.21542v1)
- Original title: Zero-Flow Two-Sample Tests
- Authors: Yakun Wang, Leyang Wang, Song Liu, Taiji Suzuki
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 我们提出了一种新的双样本测试方法，用于确定两组样本是否来自同一分布。该测试建立在基于零流量标准的统计差异之上，称为零流量差异 (ZFD)。我们证明了 ZFD 的有效性，并提出了一种实用的测试程序，称为零流量双样本测试（ZF2ST）。关键思想是了解两个分布的样本如何局部未对齐，并使用所得的方向模式作为分布差异的证据。通过将见证学习与假设评估分开，ZF2ST 可以使用灵活的神经网络，同时保持有效的统计校准。我们开发了基于回归和功率最大化的方法来学习证人。
- Abstract: We propose a new approach to two-sample testing for deciding whether two sets of samples are drawn from the same distribution. The test is built on a statistical discrepancy based on the zero-flow criterion, termed zero-flow discrepancy (ZFD). We prove the validity of ZFD and propose a practical testing procedure, termed the zero-flow two-sample test (ZF2ST). The key idea is to learn how samples from the two distrib...
- Summary (fallback): 机器翻译摘要显示：我们提出了一种新的双样本测试方法，用于确定两组样本是否来自同一分布。该测试建立在基于零流量标准的统计差异之上，称为零流量差异 (ZFD)。我们证明了 ZFD 的有效性，并提出了一种实用的测试程序，称为零流量双样本测试（ZF2ST）。关键思想是了解两个分布的样本如何局部未对齐，并使用所得的方向模式作为分布差异的证据。通过将见证学习与假设评估分开，ZF2ST 可以使用灵活的神经网络，同时保持有效的统计校准。我们开发了基于回归和功率最大化的方法来学习证人。
- Keywords: zero-flow, two-sample, testing, zf2st, propose

### 15. [半参数估计中黑盒学习器的优化使用](https://arxiv.org/abs/2607.21541v1)
- Original title: Optimal use of a black-box learner in semiparametric estimation
- Authors: Yihong Gu
- Meta: 2026-07-23 | math.ST
- 中文摘要: 考虑结构不可知设置中的部分线性模型 $Y = μ_0(X) + β_0 \cdot T + \varepsilon$ 和 $T = π_0(X) + u$，其中我们对结构 $μ_0$ 和 $π_0$ 视而不见，并通过黑盒假设类估计麻烦。该类的可学习性的特征是在没有模型错误指定的情况下的估计误差 $δ_s$ 以及分别针对 $μ_0$ 和 $π_0$ 的 $L_2$ 错误指定错误 $δ_{a, μ}$ 和 $δ_{a, π}$。我们提出了一种新的目标线性系数 $θ_0 = β_0$ 估计器，其错误率为 \[ \frac{1}{\sqrt{n}} + δ_{a, μ} \cdot δ_{a, π} + [δ_s]^2。 \] 还建立了匹配的下限，这意味着该速率是不可改进的。与双重机器学习 (DML) 产生的产品率相比，我们的估计器无需额外成本或假设即可删除次优项 $\max(δ_{a, μ}, δ_{a, π})\cdot δ_s$。
- Abstract: Consider the partial linear model $Y = μ_0(X) + β_0 \cdot T + \varepsilon$ and $T = π_0(X) + u$ in the structure-agnostic setting, where we are blind to the structure $μ_0$ and $π_0$ and estimate the nuisances by a black-box hypothesis class. The learnability of the class is characterized by the estimation error $δ_s$ in the absence of model misspecification and its $L_2$ mis-specification error $δ_{a, μ}$ and $δ_{a...
- Summary (fallback): 机器翻译摘要显示：考虑结构不可知设置中的部分线性模型 $Y = μ_0(X) + β_0 \cdot T + \varepsilon$ 和 $T = π_0(X) + u$，其中我们对结构 $μ_0$ 和 $π_0$ 视而不见，并通过黑盒假设类估计麻烦。该类的可学习性的特征是在没有模型错误指定的情况下的估计误差 $δ_s$ 以及分别针对 $μ_0$ 和 $π_0$ 的 $L_2$ 错误指定错误 $δ_{a, μ}$ 和 $δ_{a, π}$。我们提出了一种新的目标线性系数 $θ_0 = β_0$ 估计器，其错误率为 \[ \frac{1}{\sqrt{n}} + δ_{a, μ} \cdot δ_{a, π} + [δ_s]^2。 \] 还建立了匹配的下限，这意味着该速率是不可改进的。与双重机器学习 (DML) 产生的产品率相...
- Keywords: black-box, linear, model, estimation, cdot

### 16. [Windowed-MTP：取消百万代币上下文中的全上下文 Draft-KV 税](https://arxiv.org/abs/2607.21535v1)
- Original title: Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context
- Authors: Alagappan Valliappan
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 推测性解码通过目标并行验证的廉价草稿提议令牌来加速自回归生成。前沿模型越来越多地提供内置的多令牌预测 (MTP/NEXTN) 选秀头，假设选秀的成本可以忽略不计。在百万个令牌的上下文中，这种情况会被打破：MTP 草稿头通常会在每个草稿步骤中对整个 KV 缓存进行全面关注，因此它的读取会随着上下文线性增长，并开始主导草稿成本——这正是推测最有价值的地方。这种效果与草稿长度相结合（深度的原生草稿可能会变成净负值，比没有推测要慢），并在混合/线性注意力目标下变得锐利，在这种情况下，更便宜的验证会使草稿的全注意力阅读暴露出来。
- Abstract: Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel. Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap. At million-token context this breaks: an MTP draft head typically runs full attention over the entire KV cache at every draft step, so it...
- Summary (fallback): 机器翻译摘要显示：推测性解码通过目标并行验证的廉价草稿提议令牌来加速自回归生成。前沿模型越来越多地提供内置的多令牌预测 (MTP/NEXTN) 选秀头，假设选秀的成本可以忽略不计。在百万个令牌的上下文中，这种情况会被打破：MTP 草稿头通常会在每个草稿步骤中对整个 KV 缓存进行全面关注，因此它的读取会随着上下文线性增长，并开始主导草稿成本——这正是推测最有价值的地方。这种效果与草稿长度相结合（深度的原生草稿可能会变成净负值，比没有推测要慢），并在混合/线性注意力目标下变得锐利，在这种情况下，更便宜的验证会使草稿的全注意力阅读暴露出来。
- Keywords: draft, context, cost, acceptance, target

### 17. [使用基于语音的多模态大语言模型进行广义认知障碍检测](https://arxiv.org/abs/2607.21496v1)
- Original title: Toward Generalizable Cognitive Impairment Detection with Speech-Based Multimodal Large Language Models
- Authors: Yingchao Huang, Xin Wang, Yuhan Su, Shanshan Yao
- Meta: 2026-07-23 | eess.SP
- 中文摘要: 认知障碍（CI）是一个日益严重的公共卫生问题。早期准确的诊断对于及时干预和改善患者治疗效果至关重要。基于语音的 CI 检测已成为一种有前途的非侵入性方法，因为语音信号编码与认知衰退相关的语言和声学标记。大语言模型 (LLM) 的最新进展通过实现更具表现力的表征学习和改进跨不同说话者、录音设备和临床环境的泛化，进一步增强了基于语音的评估的潜力。此外，通过联合建模语言和声学特征的多模态学习可以更全面地表征与 CI 相关的认知和行为变化，从而实现更可靠的检测。
- Abstract: Cognitive impairment (CI) is a growing public health concern. Early and accurate diagnosis is critical for enabling timely intervention and improving patient outcomes. Speech-based CI detection has emerged as a promising non-invasive approach, as speech signals encode both linguistic and acoustic markers associated with cognitive decline. Recent advances in large language models (LLMs) further strengthen the potenti...
- Summary (fallback): 机器翻译摘要显示：认知障碍（CI）是一个日益严重的公共卫生问题。早期准确的诊断对于及时干预和改善患者治疗效果至关重要。基于语音的 CI 检测已成为一种有前途的非侵入性方法，因为语音信号编码与认知衰退相关的语言和声学标记。大语言模型 (LLM) 的最新进展通过实现更具表现力的表征学习和改进跨不同说话者、录音设备和临床环境的泛化，进一步增强了基于语音的评估的潜力。此外，通过联合建模语言和声学特征的多模态学习可以更全面地表征与 CI 相关的认知和行为变化，从而实现更可靠的检测。
- Keywords: multimodal, cognitive, detection, speech, acoustic

### 18. [什么、在哪里以及如何：理清任务、语言和模型在代码模型表示中的角色](https://arxiv.org/abs/2607.21491v1)
- Original title: What, Where, and How: Disentangling the Roles of Task, Language, and Model in Code Model Representations
- Authors: Piotr Wilam
- Meta: 2026-07-23 | cs.CL
- 中文摘要: 独立训练的语言模型是否会以相同的方式表示相同的事物？我们回答代码，将最近引入的概念电路提取方法扩展到 2x2 设计（Python 和 Rust 与 Qwen2.5-Coder-7B 和 DeepSeek-Coder-V1-6.7B 交叉），并在所有四个单元中以相同的方式测量语法概念的完整清单（58 个 Python，57 个 Rust）：最小的设计，将取决于任务、语言和模型的内容分开。答案分为三个部分。获得专用电路的内容由任务决定：模型就哪些概念接收电路达成一致（Python 的 Spearman $ρ$ = 0.638，Rust 的 0.673，两者 p < $10^{-7}$）。这些电路的位置由模型设定：对于两种语言，Qwen 处理后期频段 (~L17-19) 中的概念，DeepSeek 处理 L6-7 中的概念。
- Abstract: Do independently trained language models come to represent the same thing in the same way? We answer for code, extending a recently introduced concept-circuit extraction method to a 2x2 design -- Python and Rust crossed with Qwen2.5-Coder-7B and DeepSeek-Coder-V1-6.7B -- and measuring a complete inventory of grammatical concepts (58 Python, 57 Rust) identically in all four cells: the smallest design that separates w...
- Summary (fallback): 机器翻译摘要显示：独立训练的语言模型是否会以相同的方式表示相同的事物？我们回答代码，将最近引入的概念电路提取方法扩展到 2x2 设计（Python 和 Rust 与 Qwen2.5-Coder-7B 和 DeepSeek-Coder-V1-6.7B 交叉），并在所有四个单元中以相同的方式测量语法概念的完整清单（58 个 Python，57 个 Rust）：最小的设计，将取决于任务、语言和模型的内容分开。答案分为三个部分。获得专用电路的内容由任务决定：模型就哪些概念接收电路达成一致（Python 的 Spearman $ρ$ = 0.638，Rust 的 0.673，两者 p < $10^{-7}$）。这些电路的位置由模型设定：对于两种语言，Qwen 处理后期频段 (~L17-19) 中的概念，DeepSeek 处理 L6-7...
- Keywords: model, rust, circuits, what, models

### 19. [无信号交叉口自动驾驶车辆的紧凑型潜在协调](https://arxiv.org/abs/2607.21488v1)
- Original title: Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections
- Authors: Gil Lifshits, Igal Bilik, Gilad Katz
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 在无信号交叉口协调自动驾驶车辆仍然是多智能体强化学习（MARL）系统的一个关键挑战，该系统通常会与组合动作空间、对特权信息的依赖或严格的智能体设计作斗争。我们提出了主代理原型计划系统（MAPS），这是一种分层深度强化学习（DRL）架构，其中集中式主代理生成紧凑、连续的嵌入，表示为原型计划，编码全局协调策略。去中心化工作代理将这种嵌入与本地观察相结合，以执行特定于车辆的控制，将战略意图与战术执行分离，并实现每个模块的独立优化。作为此协调机制的概念验证评估，我们在 HighwayEnv 中的 72 个交叉路口配置中测试了 MAPS。
- Abstract: Coordinating autonomous vehicles at unsignalized intersections remains a critical challenge for multi-agent reinforcement learning (MARL) systems, which typically struggle with combinatorial action spaces, reliance on privileged information, or rigid agent designs. We propose Master-Agent Proto-plan System (MAPS), a hierarchical deep reinforcement learning (DRL) architecture in which a centralized Master agent gener...
- Summary (fallback): 机器翻译摘要显示：在无信号交叉口协调自动驾驶车辆仍然是多智能体强化学习（MARL）系统的一个关键挑战，该系统通常会与组合动作空间、对特权信息的依赖或严格的智能体设计作斗争。我们提出了主代理原型计划系统（MAPS），这是一种分层深度强化学习（DRL）架构，其中集中式主代理生成紧凑、连续的嵌入，表示为原型计划，编码全局协调策略。去中心化工作代理将这种嵌入与本地观察相结合，以执行特定于车辆的控制，将战略意图与战术执行分离，并实现每个模块的独立优化。作为此协调机制的概念验证评估，我们在 HighwayEnv 中的 72 个交叉路口配置中测试了 MAPS。
- Keywords: coordination, learning, maps, compact, autonomous

### 20. [高召回率候选生成的有限样本覆盖率审核：认证和学习理论设计](https://arxiv.org/abs/2607.21480v1)
- Original title: Finite-Sample Coverage Audits for High-Recall Candidate Generation: Certification and Learning-Theoretic Design
- Authors: Martin Anthony, Kaveh Salehzadeh Nobari
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 经验管道中的初始高召回阶段决定哪些项目传递到以后的审查、标记或建模，而它错过的相关项目将在每个后续阶段中丢失。我们研究需要多少个审核标签来证明，在有限样本有效性的情况下，这个缺失的相关质量很小，我们的主要结果描述了这个问题的标签复杂性。我们首先表明，仅使用候选集内部标签的程序无法证明遗漏质量的任何非平凡界限：审计必须对排除池进行采样，这是未恢复的相关项目可能存在的唯一区域。然后我们证明一个匹配的有限语料库下界。任何证明少于 $m$ 的有效审计在不存在相关项目的情况下很有可能错过相关项目，即使是自适应的并允许标记整个包含池，也必须按照 $N_0/m$ 排除池 la 的顺序进行检查...
- Abstract: An initial high-recall stage in an empirical pipeline decides which items pass to later review, labelling, or modelling, and relevant items it misses are lost to every subsequent stage. We study how many audit labels are needed to certify, with finite-sample validity, that this missed relevant mass is small, and our main results characterise the label complexity of this problem. We first show that no procedure using...
- Summary (fallback): 机器翻译摘要显示：经验管道中的初始高召回阶段决定哪些项目传递到以后的审查、标记或建模，而它错过的相关项目将在每个后续阶段中丢失。我们研究需要多少个审核标签来证明，在有限样本有效性的情况下，这个缺失的相关质量很小，我们的主要结果描述了这个问题的标签复杂性。我们首先表明，仅使用候选集内部标签的程序无法证明遗漏质量的任何非平凡界限：审计必须对排除池进行采样，这是未恢复的相关项目可能存在的唯一区域。然后我们证明一个匹配的有限语料库下界。任何证明少于 $m$ 的有效审计在不存在相关项目的情况下很有可能错过相关项目，即使是自适应的并允许标记整个包含池，也必须按照 $N_0/m$ 排除池 la 的顺序进行检查...
- Keywords: candidate, items, relevant, audit, labels

### 21. [通过随机设计进行 KV 缓存驱逐的错误证书](https://arxiv.org/abs/2607.21475v1)
- Original title: Error Certificates for KV-Cache Eviction via Randomized Design
- Authors: Peng Xie
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 确定性 KV 缓存驱逐将前 $k$ 令牌保持在重要性分数之下，并删除其余令牌。我们证明这种设计无法知道它破坏了什么：被驱逐的值可以改变，以便服务系统保留的所有内容都不变，而真正的注意力输出误差任意增长，因此该误差的服务时间估计器是一致的。随机驱逐恢复了可识别性。使用已知包含概率的泊松采样尾部，一个 Logit 偏移量在 Softmax 内执行 Hájek 校正，并且保留集上的调查采样方差估计器成为每步误差证书，经验覆盖率为 0.97，且没有准确性成本。
- Abstract: Deterministic KV-cache eviction keeps the top-$k$ tokens under an importance score and deletes the rest. We prove that this design cannot know what it destroyed: evicted values can be altered so that everything the serving system retains is unchanged while the true attention-output error grows arbitrarily, so no serving-time estimator of that error is consistent. Randomized eviction restores identifiability. With a...
- Summary (fallback): 机器翻译摘要显示：确定性 KV 缓存驱逐将前 $k$ 令牌保持在重要性分数之下，并删除其余令牌。我们证明这种设计无法知道它破坏了什么：被驱逐的值可以改变，以便服务系统保留的所有内容都不变，而真正的注意力输出误差任意增长，因此该误差的服务时间估计器是一致的。随机驱逐恢复了可识别性。使用已知包含概率的泊松采样尾部，一个 Logit 偏移量在 Softmax 内执行 Hájek 校正，并且保留集上的调查采样方差估计器成为每步误差证书，经验覆盖率为 0.97，且没有准确性成本。
- Keywords: error, eviction, certificate, kv-cache, randomized

### 22. [通过错误定位调整测试时间](https://arxiv.org/abs/2607.21453v1)
- Original title: Test-Time Scaling via Error Localization
- Authors: Rajiv Shailesh Chitale, Rahul Madhavan, Taneesh Gupta, Deepanway Ghosal, Aravindan Raghuveer
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 扩展推理时间计算已成为提高大型语言模型在复杂推理和编程任务上的性能的可靠方法。然而，独立采样和顺序多轮细化等标准方法在没有令牌级信用分配的情况下运行，导致计算效率低下，因为有效的推理前缀经常被丢弃。在这项工作中，我们引入了通过错误定位进行测试时间缩放（TTEL），这是一种推理时间算法，利用固定或环境反馈来执行令牌级错误定位。通过将知情反馈下的条件概率与空上下文基线进行比较，TTEL 可以隔离发生错误的步骤。然后，该算法截断轨迹并分支新一代，最大限度地重用有效前缀。
- Abstract: Scaling inference-time computation has emerged as a reliable method to improve the performance of large language models on complex reasoning and programming tasks. However, standard approaches such as independent sampling and sequential multi-turn refinement operate without token-level credit assignment, resulting in computational inefficiency, since valid reasoning prefixes are frequently discarded. In this work, w...
- Summary (fallback): 机器翻译摘要显示：扩展推理时间计算已成为提高大型语言模型在复杂推理和编程任务上的性能的可靠方法。然而，独立采样和顺序多轮细化等标准方法在没有令牌级信用分配的情况下运行，导致计算效率低下，因为有效的推理前缀经常被丢弃。在这项工作中，我们引入了通过错误定位进行测试时间缩放（TTEL），这是一种推理时间算法，利用固定或环境反馈来执行令牌级错误定位。通过将知情反馈下的条件概率与空上下文基线进行比较，TTEL 可以隔离发生错误的步骤。然后，该算法截断轨迹并分支新一代，最大限度地重用有效前缀。
- Keywords: ttel, error, test-time, scaling, localization

### 23. [KroQuant：用于扩散变压器高效训练后量化的克罗内克结构块变换](https://arxiv.org/abs/2607.21446v1)
- Original title: KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers
- Authors: Yann Bouquet, Alireza Khodamoradi, Kristof Denolf, Mathieu Salzmann
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 扩散变换器 (DiT) 到 W4A4 的训练后量化 (PTQ) 会严重降低输出质量，因为进入每个线性层的激活包含 4 位格式无法表示的异常值。标准修复对激活值应用可逆线性变换，并在量化两者之前对权重应用其逆线性变换。块之间的归一化层迫使该转换在每个去噪步骤中在线运行，使其推理计算成本成为绑定设计约束。
- Abstract: Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot represent. The standard fix applies an invertible linear transform to the activations and its inverse to the weights before quantizing both. Normalization layers between blocks force this transform to run online at every...
- Summary (fallback): 机器翻译摘要显示：扩散变换器 (DiT) 到 W4A4 的训练后量化 (PTQ) 会严重降低输出质量，因为进入每个线性层的激活包含 4 位格式无法表示的异常值。标准修复对激活值应用可逆线性变换，并在量化两者之前对权重应用其逆线性变换。块之间的归一化层迫使该转换在每个去噪步骤中在线运行，使其推理计算成本成为绑定设计约束。
- Keywords: quantization, kroquant, block, transforms, quality

### 24. [可持续城市的气候适应型电动汽车充电基础设施：预防性维护和低碳出行的可解释因果整体框架](https://arxiv.org/abs/2607.21444v1)
- Original title: Climate-resilient electric vehicle charging infrastructure for sustainable cities: An interpretable causal-ensemble framework for preventive maintenance and low-carbon mobility
- Authors: Cande Lian, Wentao Zeng, Jiabin Wu, Yiming Bie, Wei Zhou
- Meta: 2026-07-23 | math.OC
- 中文摘要: 可靠的电动汽车（EV）充电基础设施是可持续低碳城市的基石，但极端高温、强降水和潮湿等城市气候压力日益增加设备故障风险，并损害城市能源和出行服务的弹性。将操作从反应性维修转变为预防性维护取决于准确、前瞻性的故障风险预测，这项任务因物理、行为、背景和历史信号的异构时间尺度以及数周范围内的预测而变得复杂。我们开发了 FGDSE，这是一种特征控制的动态堆叠集成，它形成了一个可解释的决策支持系统，用于适应气候变化的充电资产管理。
- Abstract: Reliable electric vehicle (EV) charging infrastructure is a cornerstone of sustainable, low-carbon cities, yet urban climate stress such as extreme heat, heavy precipitation, and humidity increasingly raises equipment fault risk and undermines the resilience of urban energy and mobility services. Shifting operation from reactive repair to preventive maintenance depends on accurate, forward-looking fault-risk predict...
- Summary (fallback): 机器翻译摘要显示：可靠的电动汽车（EV）充电基础设施是可持续低碳城市的基石，但极端高温、强降水和潮湿等城市气候压力日益增加设备故障风险，并损害城市能源和出行服务的弹性。将操作从反应性维修转变为预防性维护取决于准确、前瞻性的故障风险预测，这项任务因物理、行为、背景和历史信号的异构时间尺度以及数周范围内的预测而变得复杂。我们开发了 FGDSE，这是一种特征控制的动态堆叠集成，它形成了一个可解释的决策支持系统，用于适应气候变化的充电资产管理。
- Keywords: maintenance, low-carbon, mobility, urban, fault

### 25. [局部细胞间耦合足以进行长程钙信号传导](https://arxiv.org/abs/2607.21442v1)
- Original title: Local intercellular coupling is sufficient for long-range calcium signaling
- Authors: Benjamin M. Goykadosh, Vasuretha Chandar, Harikrishnan Parameswaran
- Meta: 2026-07-23 | q-bio.CB
- 中文摘要: 长程细胞间钙 (Ca2+) 信号传导协调从受精到收缩和细胞死亡的生物过程。经典模型将这种长距离传播归因于肌醇 1,4,5-三磷酸 (IP3) 通过间隙连接的快速扩散。然而，最近的证据表明，IP3 的扩散速度比之前认为的要慢得多，并且即使间隙连接被拆卸，Ca2+ 振荡仍然持续，这表明必须有一种替代机制来维持长距离通信。在这里，我们开发了一个计算模型，表明相邻细胞之间的局部耦合足以在细胞群中产生和传播再生 Ca2+ 振荡，而无需快速分子扩散。
- Abstract: Long-range intercellular calcium (Ca2+) signaling coordinates biological processes ranging from fertilization to contraction and cell death. The classical model attributes this long-range propagation to rapid diffusion of inositol 1,4,5-trisphosphate (IP3) through gap junctions. However, recent evidence that IP3 diffuses far more slowly than previously believed, and that Ca2+ oscillations persist even when gap junct...
- Summary (fallback): 机器翻译摘要显示：长程细胞间钙 (Ca2+) 信号传导协调从受精到收缩和细胞死亡的生物过程。经典模型将这种长距离传播归因于肌醇 1,4,5-三磷酸 (IP3) 通过间隙连接的快速扩散。然而，最近的证据表明，IP3 的扩散速度比之前认为的要慢得多，并且即使间隙连接被拆卸，Ca2+ 振荡仍然持续，这表明必须有一种替代机制来维持长距离通信。在这里，我们开发了一个计算模型，表明相邻细胞之间的局部耦合足以在细胞群中产生和传播再生 Ca2+ 振荡，而无需快速分子扩散。
- Keywords: long-range, local, cell, intercellular, coupling

### 26. [代理引导的关系概念发现：走向可解释的手术边缘评估](https://arxiv.org/abs/2607.21437v1)
- Original title: Agent-Guided Relational Concept Discovery: Toward Interpretable Surgical Margin Assessment
- Authors: Nooshin Maghsoodi, Amoon Jamzad, Robert Policelli, Mohammad Farahmand, Dilakshan Srikanthan et al.
- Meta: 2026-07-23 | cs.AI
- 中文摘要: 深度学习模型可以有效地利用快速蒸发电离质谱（REIMS）数据进行手术切缘评估。然而，由于对手术室条件的推广有限，它们的临床应用仍然具有挑战性。之所以出现这种困难，是因为模型通常是根据从切除的组织样本收集的标记光谱进行训练的，而它们必须对手术期间直接获取的嘈杂、未标记的数据进行操作。此外，深度学习模型的黑盒性质使得理解和系统地改进其行为变得困难。基于概念的学习通过将原始测量结果映射到人类可理解的概念，提供了一种解决这些挑战的有前途的方法。然而，基于概念的监督方法依赖于概念注释，这在复杂的质谱工作流程中很难获得。
- Abstract: Deep learning models can effectively use Rapid Evaporative Ionization Mass Spectrometry (REIMS) data for surgical margin assessment. However, their clinical adoption remains challenging due to limited generalization to operating room conditions. This difficulty arises because models are typically trained on labeled spectra collected from resected tissue samples, while they must operate on noisy, unlabeled data acqui...
- Summary (fallback): 机器翻译摘要显示：深度学习模型可以有效地利用快速蒸发电离质谱（REIMS）数据进行手术切缘评估。然而，由于对手术室条件的推广有限，它们的临床应用仍然具有挑战性。之所以出现这种困难，是因为模型通常是根据从切除的组织样本收集的标记光谱进行训练的，而它们必须对手术期间直接获取的嘈杂、未标记的数据进行操作。此外，深度学习模型的黑盒性质使得理解和系统地改进其行为变得困难。基于概念的学习通过将原始测量结果映射到人类可理解的概念，提供了一种解决这些挑战的有前途的方法。然而，基于概念的监督方法依赖于概念注释，这在复杂的质谱工作流程中很难获得。
- Keywords: concept, concepts, surgical, learning, models

### 27. [思想链模型中的代币预算饱和和推理不收敛的机制早期检测](https://arxiv.org/abs/2607.21433v1)
- Original title: Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models
- Authors: Renuka Oladri, Niveda Jawahar, Abdirisak Mohamed
- Meta: 2026-07-23 | cs.CL
- 中文摘要: DeepSeek-R1-Distill-Qwen-7B 等思想链推理模型表现出双峰收敛模式：生成要么在代币预算内终止（收敛），要么耗尽代币预算但未得出结论（非收敛）。我们对这一现象进行了实证表征，结果表明，融合代在 AIME 1983-2024 上实现了 90.3% 的准确率，而非融合代仅实现了 6.6%，总体收敛率为 62.0%。然后我们询问这个结果是否可以在思维链的早期使用内部模型表示来检测到。在令牌位置 50-300 处的隐藏状态激活上训练线性探针，我们发现令牌 150 处的第 20 层激活达到了 AUC 0.608（+-0.080，5 倍 CV），即使在令牌 50 处也可靠地高于机会。激活探针始终优于从令牌熵和重复统计数据导出的行为基线。
- Abstract: Chain-of-thought reasoning models such as DeepSeek-R1-Distill-Qwen-7B exhibit a bimodal convergence pattern: generations either terminate within a token budget (converged) or exhaust it without reaching a conclusion (non-converged). We characterize this phenomenon empirically, showing that converged generations achieve 90.3% accuracy on AIME 1983-2024 while non-converged ones achieve only 6.6%, with an overall conve...
- Summary (fallback): 机器翻译摘要显示：DeepSeek-R1-Distill-Qwen-7B 等思想链推理模型表现出双峰收敛模式：生成要么在代币预算内终止（收敛），要么耗尽代币预算但未得出结论（非收敛）。我们对这一现象进行了实证表征，结果表明，融合代在 AIME 1983-2024 上实现了 90.3% 的准确率，而非融合代仅实现了 6.6%，总体收敛率为 62.0%。然后我们询问这个结果是否可以在思维链的早期使用内部模型表示来检测到。在令牌位置 50-300 处的隐藏状态激活上训练线性探针，我们发现令牌 150 处的第 20 层激活达到了 AUC 0.608（+-0.080，5 倍 CV），即使在令牌 50 处也可靠地高于机会。激活探针始终优于从令牌熵和重复统计数据导出的行为基线。
- Keywords: token, convergence, achieve, budget, early

### 28. [上下文加权离散流匹配](https://arxiv.org/abs/2607.21427v1)
- Original title: Context-weighted Discrete Flow Matching
- Authors: Daniil Cherniavskii, Daniel Severo, Karen Ullrich
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 离散流匹配为离散结构的生成建模提供了灵活的框架。然而，标准分解训练目标使模型暴露于不同难度的目标，将条件良好的、可预测的标记与模糊的、高熵的标记混合在一起。我们凭经验证明，每个令牌价值的不确定性与其邻域可用上下文的密度密切相关。受这一观察的启发，我们提出了对底层连续时间马尔可夫链（CTMC）的简单修改，其中包含了本地上下文信息。我们的上下文加权采样器以可忽略的计算开销提高了生成质量，而我们的缩放交叉熵损失函数重新加权了来自不同标记的训练信号，并将 OpenWebText 上的生成困惑度降低了高达 63%。
- Abstract: Discrete flow matching provides a flexible framework for generative modeling on discrete structures. However, the standard factorized training objective exposes the model to targets of varying difficulty, mixing well-conditioned, predictable tokens with ambiguous, high-entropy ones. We empirically demonstrate that the uncertainty over the value of each token is closely related to the density of available context in...
- Summary (fallback): 机器翻译摘要显示：离散流匹配为离散结构的生成建模提供了灵活的框架。然而，标准分解训练目标使模型暴露于不同难度的目标，将条件良好的、可预测的标记与模糊的、高熵的标记混合在一起。我们凭经验证明，每个令牌价值的不确定性与其邻域可用上下文的密度密切相关。受这一观察的启发，我们提出了对底层连续时间马尔可夫链（CTMC）的简单修改，其中包含了本地上下文信息。我们的上下文加权采样器以可忽略的计算开销提高了生成质量，而我们的缩放交叉熵损失函数重新加权了来自不同标记的训练信号，并将 OpenWebText 上的生成困惑度降低了高达 63%。
- Keywords: discrete, generative, training, context, context-weighted

### 29. [用于建设性和协作性多任务的语义感知任务集群](https://arxiv.org/abs/2607.21426v1)
- Original title: Semantic-Aware Task Clustering for Constructive and Cooperative Multi-Tasking
- Authors: Ahmad Halimi Razlighi, Maximilian H. V. Tillmann, Edgar Beck, Bho Matthiesen, Armin Dekorsy
- Meta: 2026-07-23 | cs.LG
- 中文摘要: 协作多任务语义通信（CMT-SemCom）通过利用共享表示来提高任务执行性能。然而，正如我们在[1]中所演示的，协作多任务处理可以是建设性的，也可以是破坏性的，具体取决于任务之间的语义关系。为了确保建设性合作，我们为 CMT-SemCom 提出了一种语义感知任务聚类方法。我们制定了一个顺序多阶段优化问题，其中语义对齐的任务在短暂的初始训练阶段后聚集一次，然后专门在发现的组内进行端到端（E2E）联合训练。具体来说，该问题分解为两个阶段：(i) 利用基于分层密度的空间聚类的语义聚类问题，以及 (ii) 集群内 E2E CMT-SemCom 学习问题。
- Abstract: Cooperative multi-task semantic communication (CMT-SemCom) improves task execution performance by leveraging shared representations. However, as we demonstrated in [1], cooperative multi-tasking can be either constructive or destructive, depending on the semantic relationships among tasks. To ensure constructive cooperation, we propose a semantic-aware task clustering method for CMT-SemCom. We have formulated a sequ...
- Summary (fallback): 机器翻译摘要显示：协作多任务语义通信（CMT-SemCom）通过利用共享表示来提高任务执行性能。然而，正如我们在[1]中所演示的，协作多任务处理可以是建设性的，也可以是破坏性的，具体取决于任务之间的语义关系。为了确保建设性合作，我们为 CMT-SemCom 提出了一种语义感知任务聚类方法。我们制定了一个顺序多阶段优化问题，其中语义对齐的任务在短暂的初始训练阶段后聚集一次，然后专门在发现的组内进行端到端（E2E）联合训练。具体来说，该问题分解为两个阶段：(i) 利用基于分层密度的空间聚类的语义聚类问题，以及 (ii) 集群内 E2E CMT-SemCom 学习问题。
- Keywords: clustering, problem, task, constructive, cooperative

### 30. [对深度参数化量子电路持谨慎乐观态度](https://arxiv.org/abs/2607.21409v1)
- Original title: Cautious optimism for deep parameterized quantum circuits
- Authors: Marie Kempkes, Elies Gil-Fuster, Carlos Bravo-Prieto, Aroosa Ijaz, Alissa Wilms et al.
- Meta: 2026-07-23 | quant-ph
- 中文摘要: 量子机器学习的一个核心挑战是理解参数化量子电路（PQC）的缩放行为。特别是，随着可训练参数数量的增加，它们在未见过的数据上的性能如何变化仍不清楚。先前的工作已经为量子模型得出了形式化的泛化保证，但众所周知，许多此类结果并不能完全表征实践中的泛化行为。在这项工作中，我们表明，随着模型大小的增加，基于梯度的 PQC 可以在未见过的数据上表现出更好的性能，显示出双下降现象。这与传统观点形成鲜明对比，传统观点认为较大的模型会导致泛化能力下降。我们通过利用附加扰动技术和随机矩阵的谱特性，提供严格支持这种行为的分析结果。
- Abstract: A central challenge in quantum machine learning is understanding the scaling behavior of parameterized quantum circuits (PQCs). In particular, it remains unclear how their performance on unseen data changes as the number of trainable parameters increases. Prior works have derived formal generalization guarantees for quantum models, but it is well-known that many such results do not fully characterize generalization...
- Summary (fallback): 机器翻译摘要显示：量子机器学习的一个核心挑战是理解参数化量子电路（PQC）的缩放行为。特别是，随着可训练参数数量的增加，它们在未见过的数据上的性能如何变化仍不清楚。先前的工作已经为量子模型得出了形式化的泛化保证，但众所周知，许多此类结果并不能完全表征实践中的泛化行为。在这项工作中，我们表明，随着模型大小的增加，基于梯度的 PQC 可以在未见过的数据上表现出更好的性能，显示出双下降现象。这与传统观点形成鲜明对比，传统观点认为较大的模型会导致泛化能力下降。我们通过利用附加扰动技术和随机矩阵的谱特性，提供严格支持这种行为的分析结果。
- Keywords: quantum, behavior, parameterized, circuits, pqcs

## biorxiv

### 1. [在早期急性肝损伤中，中区肝细胞通过 Atf4-Chop 轴以增殖换生存](https://www.biorxiv.org/content/10.1101/2025.08.21.671501v3)
- Original title: Mid-zone hepatocytes trade proliferation for survival via Atf4-Chop axis in early acute liver injury
- Authors: Zhu, Y., Deng, C., Chen, B., He, J., Liu, Y. et al.
- Meta: 2026-07-24 | pharmacology and toxicology | DOI: 10.1101/2025.08.21.671501
- 中文摘要: 肝细胞经历广泛的增殖以促进损伤后的肝脏修复，但增殖前的早期适应性变化仍不清楚。在此，我们报告在早期对乙酰氨基酚 (APAP) 诱导的肝损伤期间，肝细胞表现出短暂的增殖抑制，这在中区肝细胞中最为明显，这与带状 APAP 代谢一致。虽然空间转录组学（ST）为中间区的这种停滞提供了强有力的证据，但对中央周围肝细胞中类似停滞的支持是有限的。将 ST 与免疫组织化学和功能研究相结合，我们确定了一个以 Atf4-Chop 轴为中心的独特的中区应激反应程序，该程序通过细胞周期抑制剂 Btg2 抑制增殖。
- Abstract: Hepatocytes undergo extensive proliferation to facilitate liver repair after injury, yet early adaptive changes prior to proliferation remain unclear. Here, we report that during early acetaminophen (APAP)-induced liver injury, hepatocytes exhibit transient proliferation suppression that is most pronounced in mid-zone hepatocytes, consistent with zonal APAP metabolism. While spatial transcriptomics (ST) provided rob...
- Summary (fallback): 机器翻译摘要显示：肝细胞经历广泛的增殖以促进损伤后的肝脏修复，但增殖前的早期适应性变化仍不清楚。在此，我们报告在早期对乙酰氨基酚 (APAP) 诱导的肝损伤期间，肝细胞表现出短暂的增殖抑制，这在中区肝细胞中最为明显，这与带状 APAP 代谢一致。虽然空间转录组学（ST）为中间区的这种停滞提供了强有力的证据，但对中央周围肝细胞中类似停滞的支持是有限的。将 ST 与免疫组织化学和功能研究相结合，我们确定了一个以 Atf4-Chop 轴为中心的独特的中区应激反应程序，该程序通过细胞周期抑制剂 Btg2 抑制增殖。
- Keywords: hepatocytes, proliferation, mid-zone, liver, early

### 2. [D-柠檬烯对马铃薯干腐病菌尖孢镰刀菌的抗真菌活性及机制](https://www.biorxiv.org/content/10.1101/2025.10.06.675995v2)
- Original title: Antifungal activity and mechanisms of D-limonene against Fusarium oxysporum, a pathogen of potato dry rot
- Authors: Xia, Q., Dong, P.
- Meta: 2026-07-24 | plant biology | DOI: 10.1101/2025.10.06.675995
- 中文摘要: 背景：马铃薯干腐病（PDR）是由镰刀菌引起的，严重威胁马铃薯生产和采后质量。尽管柠檬烯已表现出抗真菌活性，但之前的研究主要集中在含柠檬烯的精油或表型生长抑制上，而其针对 PDR 的细胞和分子机制以及应用潜力仍不清楚。结果：D-柠檬烯对尖孢镰刀菌的生长具有浓度依赖性抑制作用，半数抑制浓度（IC）为8.32 L/mL。它还改变了菌丝形态，降低了致病性和孢子萌发，降低了孢子活力，并改变了几丁质相关荧光增白剂 28 染色模式。转录组分析鉴定出 1,884 个差异表达基因，其中 1,027 个下调基因和 857 个上调基因。
- Abstract: BACKGROUND: Potato dry rot (PDR), caused by Fusarium species, seriously threatens potato production and postharvest quality. Although limonene has demonstrated antifungal activity, previous studies have mainly focused on limonene-containing essential oils or phe-notypic growth inhibition, while its cellular and molecular mechanisms and application potential against PDR remain insufficiently understood. RESULTS: D-li...
- Summary (fallback): 机器翻译摘要显示：背景：马铃薯干腐病（PDR）是由镰刀菌引起的，严重威胁马铃薯生产和采后质量。尽管柠檬烯已表现出抗真菌活性，但之前的研究主要集中在含柠檬烯的精油或表型生长抑制上，而其针对 PDR 的细胞和分子机制以及应用潜力仍不清楚。结果：D-柠檬烯对尖孢镰刀菌的生长具有浓度依赖性抑制作用，半数抑制浓度（IC）为8.32 L/mL。它还改变了菌丝形态，降低了致病性和孢子萌发，降低了孢子活力，并改变了几丁质相关荧光增白剂 28 染色模式。转录组分析鉴定出 1,884 个差异表达基因，其中 1,027 个下调基因和 857 个上调基因。
- Keywords: d-limonene, fusarium, potato, analysis, genes

### 3. [生命早期内侧丘脑破坏导致灵长类动物出现精神分裂症相关的前额叶抑制和认知缺陷](https://www.biorxiv.org/content/10.64898/2026.07.23.740162v1)
- Original title: Early-life medial pulvinar disruption drives schizophrenia-relevant prefrontal inhibitory and cognitive deficits in primates
- Authors: Scott, J. T., Fin, S., Caccavano, A. P., Walker, M., Szczupak, D. et al.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.23.740162
- 中文摘要: 精神分裂症被认为是由出生后前额叶回路成熟中断引起的，但将早期脆弱性与成人皮质功能障碍联系起来的发育事件仍不清楚。在这里，我们测试了灵长类动物内侧丘脑核（与前额叶皮层互连的高阶丘脑核）是否有助于前额叶成熟。新生狨猴的双侧内侧枕状病变改变了青少年前额叶扩散轨迹并产生了成年工作记忆缺陷，后者在成年后并没有出现类似的病变。生命早期的病变动物表现出丘脑皮质对第 3 层小白蛋白中间神经元的输入减少、前额叶伽马功率减弱、小白蛋白表达减少以及快速尖峰中间神经元的不成熟样生理学。
- Abstract: Schizophrenia is thought to arise from disrupted postnatal maturation of prefrontal circuits, but the developmental events linking early vulnerability to adult cortical dysfunction remain unclear. Here, we tested whether the primate medial pulvinar, a higher-order thalamic nucleus interconnected with prefrontal cortex, contributes to prefrontal maturation. Bilateral medial pulvinar lesions in neonatal marmosets alte...
- Summary (fallback): 机器翻译摘要显示：精神分裂症被认为是由出生后前额叶回路成熟中断引起的，但将早期脆弱性与成人皮质功能障碍联系起来的发育事件仍不清楚。在这里，我们测试了灵长类动物内侧丘脑核（与前额叶皮层互连的高阶丘脑核）是否有助于前额叶成熟。新生狨猴的双侧内侧枕状病变改变了青少年前额叶扩散轨迹并产生了成年工作记忆缺陷，后者在成年后并没有出现类似的病变。生命早期的病变动物表现出丘脑皮质对第 3 层小白蛋白中间神经元的输入减少、前额叶伽马功率减弱、小白蛋白表达减少以及快速尖峰中间神经元的不成熟样生理学。
- Keywords: prefrontal, medial, pulvinar, maturation, thalamic

### 4. [纹状体投射神经元模型中两个钙阈值诱导 LTP 和 LTD 的相反和互补作用](https://www.biorxiv.org/content/10.1101/2025.11.17.688856v2)
- Original title: Opposite and complementary roles of the two calcium thresholds for inducing LTP and LTD in models of striatal projection neurons
- Authors: Trpevski, D.
- Meta: 2026-07-24 | neuroscience | DOI: 10.1101/2025.11.17.688856
- 中文摘要: 当钙因传入刺激流入突触超过阈值水平时，突触可塑性就会发生。该阈值水平可以通过称为化塑性的过程进行修改。一些神经元，例如纹状体投射神经元，使用不同来源的钙作为突触增强（长期增强，LTP）或减弱（长期抑制，LTD）的信号，导致它们具有两个诱导可塑性的阈值。在这项研究中，我们表明，化塑性使得在学习过程中经历 LTP 和 LTD 的突触能够选择性地表达一种形式的可塑性（LTP 或 LTD）。为了证明这一点，我们使用线性和非线性特征绑定问题（FBP 和 NFBP），因为它们的输入模式共享特征，将突触暴露于此类竞争的 LTP 和 LTD 过程。
- Abstract: Synaptic plasticity has been shown to occur when calcium, flowing into the synapse due to incoming stimuli, surpasses a threshold level. This threshold level is modifiable through a process called metaplasticity. Some neurons, such as the striatal projection neurons, use different sources of calcium as the signal for synaptic strengthening (long-term potentiation, LTP) or weakening (long-term depression, LTD), resul...
- Summary (fallback): 机器翻译摘要显示：当钙因传入刺激流入突触超过阈值水平时，突触可塑性就会发生。该阈值水平可以通过称为化塑性的过程进行修改。一些神经元，例如纹状体投射神经元，使用不同来源的钙作为突触增强（长期增强，LTP）或减弱（长期抑制，LTD）的信号，导致它们具有两个诱导可塑性的阈值。在这项研究中，我们表明，化塑性使得在学习过程中经历 LTP 和 LTD 的突触能够选择性地表达一种形式的可塑性（LTP 或 LTD）。为了证明这一点，我们使用线性和非线性特征绑定问题（FBP 和 NFBP），因为它们的输入模式共享特征，将突触暴露于此类竞争的 LTP 和 LTD 过程。
- Keywords: metaplasticity, calcium, threshold, thresholds, plasticity

### 5. [感知较少或感知不可靠？解开衰老和神经病变背景下的热感觉敏感性和精确度](https://www.biorxiv.org/content/10.1101/2025.09.22.677851v3)
- Original title: Perceiving less or perceiving unreliably? Disentangling thermosensory sensitivity and precision in the contexts of ageing and neuropathy
- Authors: Courtin, A. S., Kraenge, C. E., Mitchell, A. G., Ehmsen, J. F., Brask-Thomsen, P. K. et al.
- Meta: 2026-07-24 | neuroscience | DOI: 10.1101/2025.09.22.677851
- 中文摘要: 热感知不仅取决于灵敏度，还取决于精度。然而，后者在热感觉和疼痛研究中经常被忽视。这项研究探讨了衰老和糖尿病多发性神经病 (DPN) 如何影响这些参数，以及评估敏感性和精确度是否有助于区分患者和健康对照。我们使用贝叶斯分层模型，在 75 名健康成年人（21-80 岁）和 33 名 DPN 患者的横截面样本中，估计了在前臂掌侧传递的冷检测、温检测、冷痛和热痛刺激的心理测量功能阈值（灵敏度）和斜率（精度）。我们还分别估计了每个参与者的这些参数，并将所得估计值用于分类分析。
- Abstract: Thermal perception is determined not only by sensitivity but also by precision. Yet, the latter is often overlooked in thermosensation and pain research. This study examined how ageing and diabetic polyneuropathy (DPN) affect these parameters and whether assessing both sensitivity and precision can aid in distinguishing patients from healthy controls. Using Bayesian hierarchical models, we estimated psychometric fun...
- Summary (fallback): 机器翻译摘要显示：热感知不仅取决于灵敏度，还取决于精度。然而，后者在热感觉和疼痛研究中经常被忽视。这项研究探讨了衰老和糖尿病多发性神经病 (DPN) 如何影响这些参数，以及评估敏感性和精确度是否有助于区分患者和健康对照。我们使用贝叶斯分层模型，在 75 名健康成年人（21-80 岁）和 33 名 DPN 患者的横截面样本中，估计了在前臂掌侧传递的冷检测、温检测、冷痛和热痛刺激的心理测量功能阈值（灵敏度）和斜率（精度）。我们还分别估计了每个参与者的这些参数，并将所得估计值用于分类分析。
- Keywords: detection, cold, parameters, pain, thresholds

### 6. [电惊厥刺激驱动小鼠皮质扩散抑制依赖的早期基因表达](https://www.biorxiv.org/content/10.64898/2026.04.14.718362v3)
- Original title: Electroconvulsive stimulation drives cortical spreading depression dependent immediate early gene expression in mice
- Authors: Ladret, H. J., Lupori, L., Sieni, L., Stroukov, E., Kanamori, T. et al.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.04.14.718362
- 中文摘要: 电休克疗法（ECT）是治疗多种精神疾病的一种高效方法，但其生物学机制仍不清楚。传统上，其治疗作用归因于 ECT 诱发的全身性癫痫发作。然而，这一观点受到最近发现的挑战，即电惊厥刺激（ECS）可以引发皮质扩散性抑制（CSD）。由于 CSD 引发大量细胞内分子变化，我们假设它可能是 ECT 治疗、可塑性诱导作用的关键介质。我们在接受 ECT 的小鼠和患者中观察到 ECS 后类似的神经元振荡。我们发现，CSD 会促进即早期基因 Fos 的表达增加，Fos 是神经元可塑性的关键标志物，并且与预测 ECT 积极治疗结果的因素相关。
- Abstract: Electroconvulsive therapy (ECT) is a highly effective treatment for several psychiatric disorders, though its biological mechanisms remain unclear. Its therapeutic action has traditionally been attributed to the generalized seizure ECT induces. However, this view is challenged by the recent finding that electroconvulsive stimulation (ECS) can trigger a cortical spreading depression (CSD). Because CSD triggers massiv...
- Summary (fallback): 机器翻译摘要显示：电休克疗法（ECT）是治疗多种精神疾病的一种高效方法，但其生物学机制仍不清楚。传统上，其治疗作用归因于 ECT 诱发的全身性癫痫发作。然而，这一观点受到最近发现的挑战，即电惊厥刺激（ECS）可以引发皮质扩散性抑制（CSD）。由于 CSD 引发大量细胞内分子变化，我们假设它可能是 ECT 治疗、可塑性诱导作用的关键介质。我们在接受 ECT 的小鼠和患者中观察到 ECS 后类似的神经元振荡。我们发现，CSD 会促进即早期基因 Fos 的表达增加，Fos 是神经元可塑性的关键标志物，并且与预测 ECT 积极治疗结果的因素相关。
- Keywords: therapeutic, electroconvulsive, stimulation, drives, cortical

### 7. [大鼠丘脑内侧分区通过不同的前额叶通路差异调节疼痛的感觉和情感成分。](https://www.biorxiv.org/content/10.64898/2026.07.17.739109v2)
- Original title: Rat mediodorsal thalamic subdivisions differentially modulate the sensory and affective components of pain through distinct prefrontal pathways.
- Authors: Iben-Daoudi, H., Ba-Mhamed, S., Moubarrad, F.-Z. L., Bennis, M., LANDRY, M. et al.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.17.739109
- 中文摘要: 丘脑内侧 (MD) 通过丘脑皮质调节 mPFC 来调节疼痛。然而，尽管 MD 具有明显的内部异质性，但通常被视为单一的解剖学和功能实体。在这里，我们测试了内侧-中央MD（MDmc）和外侧MD（MDl）细分是否通过前扣带皮层（ACC）和前边缘皮层（PrL）对疼痛的感觉辨别和情感动机成分发挥可分离的控制。利用大鼠的细分选择性兴奋性毒性损伤，结合顺行追踪、层流活动映射和 ACC 或 PrL 中 MDmc 和 MDl 末端的投影特异性光遗传学操作，我们确定了每个细分的贡献和潜在的 MD-PFC 回路机制。
- Abstract: The mediodorsal thalamus (MD) modulates pain through thalamocortical regulation of the mPFC. Yet, MD is often treated as a single anatomical and functional entity despite marked internal heterogeneity. Here, we tested whether medial-central MD (MDmc) and lateral MD (MDl) subdivisions exert dissociable control over sensory-discriminative and affective-motivational components of pain by engaging the anterior cingulate...
- Summary (fallback): 机器翻译摘要显示：丘脑内侧 (MD) 通过丘脑皮质调节 mPFC 来调节疼痛。然而，尽管 MD 具有明显的内部异质性，但通常被视为单一的解剖学和功能实体。在这里，我们测试了内侧-中央MD（MDmc）和外侧MD（MDl）细分是否通过前扣带皮层（ACC）和前边缘皮层（PrL）对疼痛的感觉辨别和情感动机成分发挥可分离的控制。利用大鼠的细分选择性兴奋性毒性损伤，结合顺行追踪、层流活动映射和 ACC 或 PrL 中 MDmc 和 MDl 末端的投影特异性光遗传学操作，我们确定了每个细分的贡献和潜在的 MD-PFC 回路机制。
- Keywords: mdmc, pain, lesions, avoidance, components

### 8. [小胶质细胞通过孔胞作用提取神经元蛋白水解细胞器](https://www.biorxiv.org/content/10.64898/2026.07.22.740182v1)
- Original title: Microglia extract neuronal proteolytic organelles via skoupocytosis
- Authors: Pepper, R., Griswold, J. M., Middleton-Davis, F., Syed, S., Imoto, Y. et al.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.22.740182
- 中文摘要: 由于其曲折的形态和延伸的过程，神经元在维持蛋白质稳态方面面临着独特的挑战。蛋白水解细胞器通常逆行运输至溶酶体富集的胞体进行降解，但一些细胞器比这些神经元过程更大，质疑这些细胞器是如何降解的。在这里，我们展示了小胶质细胞（大脑的常驻免疫细胞）在体外和体内从神经元中提取蛋白水解细胞器。小胶质细胞与神经元膜短暂接触，神经元膜下方有蛋白水解细胞器。在这些相互作用的位点，小胶质细胞夹断含有细胞器的神经元过程的一小部分，使过程的其余部分保持完整。我们将这个过程称为“skoupocytosis”，源自希腊语中的“垃圾”一词。
- Abstract: Neurons face unique challenges in maintaining protein homeostasis due to their tortuous morphology and extended processes. Proteolytic organelles are typically transported retrogradely towards their soma for degradation where lysosomes are enriched, but some organelles are larger than these neuronal processes, questioning how these organelles are degraded. Here we show that microglia, the resident immune cells of th...
- Summary (fallback): 机器翻译摘要显示：由于其曲折的形态和延伸的过程，神经元在维持蛋白质稳态方面面临着独特的挑战。蛋白水解细胞器通常逆行运输至溶酶体富集的胞体进行降解，但一些细胞器比这些神经元过程更大，质疑这些细胞器是如何降解的。在这里，我们展示了小胶质细胞（大脑的常驻免疫细胞）在体外和体内从神经元中提取蛋白水解细胞器。小胶质细胞与神经元膜短暂接触，神经元膜下方有蛋白水解细胞器。在这些相互作用的位点，小胶质细胞夹断含有细胞器的神经元过程的一小部分，使过程的其余部分保持完整。我们将这个过程称为“skoupocytosis”，源自希腊语中的“垃圾”一词。
- Keywords: organelles, proteolytic, microglia, neuronal, skoupocytosis

### 9. [侧链-侧链相互作用的重新分布控制错义 Shank1 PDZ 突变体中配体特异性结合亲和力的变化](https://www.biorxiv.org/content/10.1101/2025.07.03.662971v3)
- Original title: Redistribution of sidechain-sidechain interactions govern ligand-specific binding affinity changes in missense Shank1 PDZ mutants
- Authors: Santa, A., Kalman, Z. E. E., Nagy-Kanta, E., Jakab, B., Gaspari, Z. et al.
- Meta: 2026-07-24 | molecular biology | DOI: 10.1101/2025.07.03.662971
- 中文摘要: 柄蛋白代表突触后密度中丰富的支架家族。他们的功能障碍已被确定为自闭症谱系障碍和各种癌症背后的可能原因。 Shank 家族的 PDZ 结构域非常混杂，在同种型中高度保守，并且包含一个独特的动态片段，即 {β}2-{β}3 环，它可能在配体选择性中发挥重要作用。我们使用 Shank1 PDZ 作为模型系统来分析五种疾病相关错义突变对不同伴侣肽结合的干扰影响。使用实验方法和分子动力学模拟，我们详细描述了相互作用，重点关注其动态方面。
- Abstract: Shank proteins represent a family of abundant scaffolds in the postsynaptic density. Their dysfunctions had been identified as possible causes behind autism spectrum disorders and various types of cancer. The remarkably promiscuous PDZ domain of the Shank family is highly conserved through isoforms, and contains a unique dynamic segment, the {beta}2-{beta}3 loop, which is likely to play an important role in ligand s...
- Summary (fallback): 机器翻译摘要显示：柄蛋白代表突触后密度中丰富的支架家族。他们的功能障碍已被确定为自闭症谱系障碍和各种癌症背后的可能原因。 Shank 家族的 PDZ 结构域非常混杂，在同种型中高度保守，并且包含一个独特的动态片段，即 {β}2-{β}3 环，它可能在配体选择性中发挥重要作用。我们使用 Shank1 PDZ 作为模型系统来分析五种疾病相关错义突变对不同伴侣肽结合的干扰影响。使用实验方法和分子动力学模拟，我们详细描述了相互作用，重点关注其动态方面。
- Keywords: interactions, dynamic, mutations, ligand-specific, binding

### 10. [后期促进复合物针对有毒蛋白早老蛋白，通过自噬进行泛素依赖性降解](https://www.biorxiv.org/content/10.64898/2026.07.23.740245v1)
- Original title: The Anaphase Promoting Complex targets the toxic protein Progerin for ubiquitin-dependent degradation via autophagy
- Authors: Eskiw, C. H., Martinez, V., Lubachowski, M., Gillespie, Z. E., Fleming, M. et al.
- Meta: 2026-07-24 | cell biology | DOI: 10.64898/2026.07.23.740245
- 中文摘要: 早衰疾病哈钦森-吉尔福德早衰综合症 (HGPS) 是由于核纤层中早老蛋白的积累引起的，早老蛋白是一种细胞毒性蛋白，由核纤层蛋白 A/C 基因的点突变产生。在适当的刺激下，细胞会降解早老素，逆转细胞 HGPS 表型；然而，我们对哪些途径介导早老素降解的了解仍然存在差距。先前的数据表明，后期促进复合物（APC）是一种多亚基泛素连接酶，可降解目标蛋白，并且 APC 功能的下降与细胞衰老有关。为了确定 APC 是否与 HGPS 疾病表型相关，我们对从 HGPS 患者分离的皮肤样本中提取的 RNA 序列数据进行了荟萃分析，并确定了编码 APC 亚基和底物的几个基因的失调。
- Abstract: The premature aging disease Hutchinson-Gilford Progeria Syndrome (HGPS) results from the accumulation of progerin, a cytotoxic protein generated from a point mutation in the Lamin A/C gene, in the nuclear lamina. Upon the proper stimulation, cells degrade progerin, reversing cellular HGPS phenotypes; however, there is still a gap in our knowledge concerning which pathways are mediating progerin degradation. Previous...
- Summary (fallback): 机器翻译摘要显示：早衰疾病哈钦森-吉尔福德早衰综合症 (HGPS) 是由于核纤层中早老蛋白的积累引起的，早老蛋白是一种细胞毒性蛋白，由核纤层蛋白 A/C 基因的点突变产生。在适当的刺激下，细胞会降解早老素，逆转细胞 HGPS 表型；然而，我们对哪些途径介导早老素降解的了解仍然存在差距。先前的数据表明，后期促进复合物（APC）是一种多亚基泛素连接酶，可降解目标蛋白，并且 APC 功能的下降与细胞衰老有关。为了确定 APC 是否与 HGPS 疾病表型相关，我们对从 HGPS 患者分离的皮肤样本中提取的 RNA 序列数据进行了荟萃分析，并确定了编码 APC 亚基和底物的几个基因的失调。
- Keywords: progerin, degradation, hgps, cells, protein

### 11. [NDUFV2P1 驱动的线粒体和神经元活动调节；对精神分裂症的影响](https://www.biorxiv.org/content/10.64898/2026.07.23.740347v1)
- Original title: NDUFV2P1-driven modulation of mitochondrial and neuronal activities; implications to schizophrenia
- Authors: Ben-Shachar, D., Lapiro, Y., Karry, R., Binah, O.
- Meta: 2026-07-24 | cell biology | DOI: 10.64898/2026.07.23.740347
- 中文摘要: 精神分裂症（SZ）是一种严重的精神障碍，影响情绪、认知和社会功能。线粒体对于神经元功能、突触可塑性和行为至关重要，而这些在 SZ 中都会受到损害。 SZ 线粒体功能障碍的主要驱动因素是复合物 I，特别是其 NDUFV2 核心亚基。我们发现 NDUFV2 假基因（NDUFV2P1；PG）在 SZ 患者的脑和外周细胞中表达上调，并且与 Epstein-Barr 病毒转化的淋巴细胞系（LCL）中的 NDUFV2 表达和线粒体呼吸呈负相关。计算机分析排除了 NDUFV2 的小 RNA 干扰，而是暗示了 PG。为了研究 PG 对 NDUFV2 表达、线粒体功能和神经元活动的影响，我们调节了 LCL 中的 PG 丰度。
- Abstract: Schizophrenia (SZ) is a severe mental disorder affecting emotion, cognitive and social functioning. Mitochondria are essential for neuronal function, synaptic plasticity, and behavior, all impaired in SZ. A major driver of mitochondrial dysfunction in SZ is Complex I, particularly its NDUFV2 core-subunit. We showed that NDUFV2 pseudogene (NDUFV2P1; PG) is upregulated in brain and peripheral cells of SZ patients and...
- Summary (fallback): 机器翻译摘要显示：精神分裂症（SZ）是一种严重的精神障碍，影响情绪、认知和社会功能。线粒体对于神经元功能、突触可塑性和行为至关重要，而这些在 SZ 中都会受到损害。 SZ 线粒体功能障碍的主要驱动因素是复合物 I，特别是其 NDUFV2 核心亚基。我们发现 NDUFV2 假基因（NDUFV2P1；PG）在 SZ 患者的脑和外周细胞中表达上调，并且与 Epstein-Barr 病毒转化的淋巴细胞系（LCL）中的 NDUFV2 表达和线粒体呼吸呈负相关。计算机分析排除了 NDUFV2 的小 RNA 干扰，而是暗示了 PG。为了研究 PG 对 NDUFV2 表达、线粒体功能和神经元活动的影响，我们调节了 LCL 中的 PG 丰度。
- Keywords: mitochondrial, ndufv2, neuronal, lcls, impaired

### 12. [hAMH 驱动的 SOX17 异位表达诱导小鼠睾丸增生性支持阀形成](https://www.biorxiv.org/content/10.64898/2026.05.08.723552v2)
- Original title: Ectopic hAMH-driven SOX17 expression induces hyperplastic Sertoli valve formation in mouse testes
- Authors: Han, X., Uchida, A., Lee, S., Nakamura, K., Takahashi, K. et al.
- Meta: 2026-07-24 | developmental biology | DOI: 10.64898/2026.05.08.723552
- 中文摘要: RT 特异性 Sox17 条件性敲除 (cKO) 小鼠睾丸的表型分析表明，在生精小管终末段，睾丸网 (RT) 上皮细胞中的 SOX17 表达在支持瓣 (SV) 的形成中发挥着至关重要的作用。在这些 RT 特异性 Sox17 cKO 睾丸中，SV 破坏导致 RT 液体回流到生精小管中，导致精子发生缺陷和男性不育。尽管Sox17 cKO睾丸中的瓣膜变形可能是由R​​T中Sox17下游作用受损间接引起的，但RT中SOX17影响生精小管中SV形成的机制仍不清楚。为了解决这个问题，我们构建了一种新型 AMH-Sox17 转基因 (Tg) 小鼠系，其携带人类 AMH 启动子驱动的 Sox17 cDNA 盒。
- Abstract: In the terminal segment of the seminiferous tubules, SOX17 expression in the rete testis (RT) epithelium plays a crucial role in the formation of the Sertoli valve (SV), as revealed by phenotypic analyses of RT-specific Sox17 conditional knockout (cKO) mouse testes. In these RT-specific Sox17 cKO testes, SV disruption leads to the backflow of RT fluid into the seminiferous tubules, resulting in defective spermiogene...
- Summary (fallback): 机器翻译摘要显示：RT 特异性 Sox17 条件性敲除 (cKO) 小鼠睾丸的表型分析表明，在生精小管终末段，睾丸网 (RT) 上皮细胞中的 SOX17 表达在支持瓣 (SV) 的形成中发挥着至关重要的作用。在这些 RT 特异性 Sox17 cKO 睾丸中，SV 破坏导致 RT 液体回流到生精小管中，导致精子发生缺陷和男性不育。尽管Sox17 cKO睾丸中的瓣膜变形可能是由R​​T中Sox17下游作用受损间接引起的，但RT中SOX17影响生精小管中SV形成的机制仍不清楚。为了解决这个问题，我们构建了一种新型 AMH-Sox17 转基因 (Tg) 小鼠系，其携带人类 AMH 启动子驱动的 Sox17 cDNA 盒。
- Keywords: sox17, sertoli, valve, formation, testes

### 13. [鱼精蛋白快速进化抑制果蝇减数分裂驱动](https://www.biorxiv.org/content/10.1101/2025.09.03.674087v2)
- Original title: Rapid protamine evolution suppresses meiotic drive in Drosophila
- Authors: Chang, C.-H., de la Cruz, A. F., Lai, H.-Y., Natividad, I. M., Noyola, A. et al.
- Meta: 2026-07-24 | evolutionary biology | DOI: 10.1101/2025.09.03.674087
- 中文摘要: 许多动物物种在精子发生过程中用鱼精蛋白取代组蛋白。尽管鱼精蛋白对精子功能很重要，但它在许多物种中都迅速进化。它们快速进化背后的生物学原因仍然未知。在这里，我们利用体内基因替换，研究了鱼精蛋白 Mst77F 快速进化的原因和后果，鱼精蛋白 Mst77F 对于黑腹果蝇的雄性生育力至关重要。与携带 Y 染色体的精子相比，Mst77F 直系同源替换导致在精子发生过程中携带 X 染色体的精子的 DNA 压缩存在缺陷，从而导致携带 X 染色体的成熟精子和偏雄性后代的数量减少。与黑腹果蝇不同，Mst77F对于黑腹果蝇的雄性生育能力不是必需的，但仍然是抑制性别比例扭曲所必需的。
- Abstract: Many animal species replace histones with protamines during spermatogenesis. Despite their importance for sperm function, protamines rapidly evolve in many species; the biological causes behind their rapid evolution remain unknown. Here, using in vivo gene replacement, we investigated the causes and consequences underlying the rapid evolution of protamine Mst77F, which is essential for male fertility in D. melanogas...
- Summary (fallback): 机器翻译摘要显示：许多动物物种在精子发生过程中用鱼精蛋白取代组蛋白。尽管鱼精蛋白对精子功能很重要，但它在许多物种中都迅速进化。它们快速进化背后的生物学原因仍然未知。在这里，我们利用体内基因替换，研究了鱼精蛋白 Mst77F 快速进化的原因和后果，鱼精蛋白 Mst77F 对于黑腹果蝇的雄性生育力至关重要。与携带 Y 染色体的精子相比，Mst77F 直系同源替换导致在精子发生过程中携带 X 染色体的精子的 DNA 压缩存在缺陷，从而导致携带 X 染色体的成熟精子和偏雄性后代的数量减少。与黑腹果蝇不同，Mst77F对于黑腹果蝇的雄性生育能力不是必需的，但仍然是抑制性别比例扭曲所必需的。
- Keywords: rapid, evolution, sperm, protamines, mst77f

### 14. [1/e 定律预测跨类群最佳繁殖时机的证据](https://www.biorxiv.org/content/10.64898/2026.06.30.733937v2)
- Original title: Evidence for the 1/e-law predicting optimal timing of reproduction across taxa
- Authors: Froese, T., Froese, R., Bruss, T.
- Meta: 2026-07-24 | evolutionary biology | DOI: 10.64898/2026.06.30.733937
- 中文摘要: 生殖成功需要在整个生命周期中分配精力，平衡早期死亡的风险与随着体型或年龄而增加的更高繁殖力或父母专业知识的好处。在此，我们报告了对植物、动物和人类生殖时间表的跨分类学分析，结果表明，生殖努力峰值始终发生在物种特定最大寿命的约 1/e（~37%）处。该模式在主要系统发育群体中都很稳健，并且与绝对寿命无关。这种收敛在逻辑上和数值上都与最佳选择的 1/e 定律（Bruss 1984）的最佳停止分数 (1/e) 一致，该定律通过延迟承诺直到检查了 1/e 的可用选项，最大化了在不确定性下选择更好选项的概率。
- Abstract: Reproductive success requires allocating effort across lifespan in a manner that balances the risk of early mortality against the benefit of higher fecundity or parental expertise that increase with body size or age. Here we report a cross-taxonomic analysis of reproductive schedules in plants, animals, and humans, showing that peak reproductive effort consistently occurs at approximately 1/e (~37%) of species-speci...
- Summary (fallback): 机器翻译摘要显示：生殖成功需要在整个生命周期中分配精力，平衡早期死亡的风险与随着体型或年龄而增加的更高繁殖力或父母专业知识的好处。在此，我们报告了对植物、动物和人类生殖时间表的跨分类学分析，结果表明，生殖努力峰值始终发生在物种特定最大寿命的约 1/e（~37%）处。该模式在主要系统发育群体中都很稳健，并且与绝对寿命无关。这种收敛在逻辑上和数值上都与最佳选择的 1/e 定律（Bruss 1984）的最佳停止分数 (1/e) 一致，该定律通过延迟承诺直到检查了 1/e 的可用选项，最大化了在不确定性下选择更好选项的概率。
- Keywords: reproductive, lifespan, e-law, timing, across

### 15. [8000 个完整人类着丝粒的多维变异和群体分层](https://www.biorxiv.org/content/10.64898/2026.07.22.740206v1)
- Original title: Multidimensional variation and population stratification across 8000 complete human centromeres
- Authors: Sun, Y., Wan, S., Nie, L., Yu, D., Zhou, F. et al.
- Meta: 2026-07-24 | genomics | DOI: 10.64898/2026.07.22.740206
- 中文摘要: 人类着丝粒对于细胞分裂过程中染色体的忠实分离是不可或缺的，但其高度重复的性质历来妨碍了全面的表征，从而导致有关其序列多样性、进化轨迹和功能动力学的基本问题尚未解决。在这里，我们从亚洲泛基因组计划第一阶段的 320 个分阶段基因组组装中生成了 6,312 个完整的人类着丝粒序列。通过整合人类泛基因组参考联盟 (HPRC) 和人类基因组结构变异联盟 (HGSVC) 的组装，我们构建了包含 8,000 多个无间隙着丝粒的多维遗传变异图谱。着丝粒卫星阵列占整个基因组的 4.19% 至 6.01%，不同染色体的大小和结构存在很大差异。
- Abstract: Human centromeres are indispensable for the faithful segregation of chromosomes during cell division, yet their highly repetitive nature has historically precluded comprehensive characterization, leaving fundamental questions about their sequence diversity, evolution trajectories and function dynamics unresolved. Here, we generated 6,312 complete human centromere sequences from 320 phased genome assemblies in Asian...
- Summary (fallback): 机器翻译摘要显示：人类着丝粒对于细胞分裂过程中染色体的忠实分离是不可或缺的，但其高度重复的性质历来妨碍了全面的表征，从而导致有关其序列多样性、进化轨迹和功能动力学的基本问题尚未解决。在这里，我们从亚洲泛基因组计划第一阶段的 320 个分阶段基因组组装中生成了 6,312 个完整的人类着丝粒序列。通过整合人类泛基因组参考联盟 (HPRC) 和人类基因组结构变异联盟 (HGSVC) 的组装，我们构建了包含 8,000 多个无间隙着丝粒的多维遗传变异图谱。着丝粒卫星阵列占整个基因组的 4.19% 至 6.01%，不同染色体的大小和结构存在很大差异。
- Keywords: centromeres, human, centromere, across, chromosomes

### 16. [生成机器学习和微流体 uHTS：酶工程的高效合作伙伴](https://www.biorxiv.org/content/10.1101/2025.11.02.685536v3)
- Original title: Generative Machine Learning and Microfluidics uHTS: An Efficient Partnership for Enzyme Engineering
- Authors: Nair, P. M., Steinberg, D. M., Resende, T., Suarez, A. F., Power, H. et al.
- Meta: 2026-07-24 | bioengineering | DOI: 10.1101/2025.11.02.685536
- 中文摘要: 酶工程在调整生物催化剂性能以满足目标应用的需求方面发挥着至关重要的作用。然而，单个野生型酶序列可能产生的序列轨迹数量太大，无法通过实验进行遍历。在这里，我们提出了一种新颖的方法，首先使用超高通量筛选（uHTS）扩展实验可访问的序列空间，然后使用间接和低保真度测定数据为目标酶类别创建“指纹”。提取来自微流体 uHTS 的实验数据，并用于将特异性改造为来自巴西曲霉 (AbrUPO) 的非特异性过氧合酶 (UPO)。我们创建了一个包含超过 500 万个用 Komagataella phaffii（毕赤酵母）表达的不同变体的文库。然后使用微流控液滴分选生成超过 30,000 个与功能数据配对的独特序列的数据集。
- Abstract: Enzyme engineering plays a vital role in tailoring biocatalyst performance to meet the needs of target applications. However, the number of sequence trajectories possible from a single wildtype enzyme sequence is too vast to traverse experimentally. Here we present a novel approach that first expands the experimentally accessible sequence space using ultrahigh throughput screening (uHTS), and then uses indirect and...
- Summary (fallback): 机器翻译摘要显示：酶工程在调整生物催化剂性能以满足目标应用的需求方面发挥着至关重要的作用。然而，单个野生型酶序列可能产生的序列轨迹数量太大，无法通过实验进行遍历。在这里，我们提出了一种新颖的方法，首先使用超高通量筛选（uHTS）扩展实验可访问的序列空间，然后使用间接和低保真度测定数据为目标酶类别创建“指纹”。提取来自微流体 uHTS 的实验数据，并用于将特异性改造为来自巴西曲霉 (AbrUPO) 的非特异性过氧合酶 (UPO)。我们创建了一个包含超过 500 万个用 Komagataella phaffii（毕赤酵母）表达的不同变体的文库。然后使用微流控液滴分选生成超过 30,000 个与功能数据配对的独特序列的数据集。
- Keywords: enzyme, generative, uhts, variants, series

### 17. [STAR Suite：一个开源的单一可执行转录组学引擎，用于可重复的人工智能代理辅助处理](https://www.biorxiv.org/content/10.64898/2026.03.09.710580v5)
- Original title: STAR Suite: an open-source single-executable transcriptomics engine for reproducible, AI agent-assisted processing
- Authors: Hung, L.-H., Baker, D., Flynn, B., Huangfu, D., Luo, R. et al.
- Meta: 2026-07-24 | bioinformatics | DOI: 10.64898/2026.03.09.710580
- 中文摘要: 处理测序数据意味着链接许多专用工具，这对实验室生物学家和越来越多地用于运行分析的人工智能代理来说是一个障碍。开放、集成的管道仍然不完整：事实上的单单元标准 Cell Ranger 是专有的 - 其许可证禁止重新分发、修改和非 10x 使用 - 因此它不能充当可共享、AI 可发现的层，并且不存在适用于 10x Flex 的生产就绪的开源管道。在这里，我们推出了 STAR Suite，它将 STAR 对齐器扩展为用于转录组处理的单个可执行文件。适配器处理、特征条形码分配、Flex 探针处理、SLAM-seq 分析、排序和质量控制直接集成到 28,228 行 STAR 代码库中，无需额外的外部依赖项，添加了 132,226 行 C/C++ 代码，通过人工指导的 AI 软件工程使其易于处理。
- Abstract: Processing sequencing data means chaining many specialized tools, a barrier for bench biologists and for the AI agents increasingly used to run analyses. Open, integrated pipelines remain incomplete: the de facto single-cell standard, Cell Ranger, is proprietary - its license bars redistribution, modification, and non-10x use - so it cannot serve as a shareable, AI-discoverable layer, and no production-ready open-so...
- Summary (fallback): 机器翻译摘要显示：处理测序数据意味着链接许多专用工具，这对实验室生物学家和越来越多地用于运行分析的人工智能代理来说是一个障碍。开放、集成的管道仍然不完整：事实上的单单元标准 Cell Ranger 是专有的 - 其许可证禁止重新分发、修改和非 10x 使用 - 因此它不能充当可共享、AI 可发现的层，并且不存在适用于 10x Flex 的生产就绪的开源管道。在这里，我们推出了 STAR Suite，它将 STAR 对齐器扩展为用于转录组处理的单个可执行文件。适配器处理、特征条形码分配、Flex 探针处理、SLAM-seq 分析、排序和质量控制直接集成到 28,228 行 STAR 代码库中，无需额外的外部依赖项，添加了 132,226 行 C/C++ 代码，通过人工指导的 AI 软件工程使其易于处理。
- Keywords: star, processing, suite, open-source, transcriptomics

### 18. [双层不对称性导致ESCRT-III依赖性膜弯曲方向](https://www.biorxiv.org/content/10.64898/2026.07.23.740341v1)
- Original title: Direction of ESCRT-III-dependent membrane bending emerges from bilayer asymmetry
- Authors: Tran, J., Roux, A.
- Meta: 2026-07-24 | biophysics | DOI: 10.64898/2026.07.23.740341
- 中文摘要: 在细胞中，ESCRT-III 在从内部介导膜颈裂变方面具有独特性，这一过程称为逆拓扑裂变。然而，在体外，该复合物主要在膜颈外组装并以正常拓扑介导裂变。在这里，我们表明 ESCRT 介导的膜变形的方向是由双层不对称性产生的，而不是仅由 ESCRT 机制内在编码。利用芽殖酵母中的遗传扰动，我们发现磷脂不对称性和鞘脂稳态的破坏并不能消除ESCRT依赖性运输，而是使ILV形成对膜物理状态高度敏感，导致低效的货物分类和停滞的内体中间体的积累。
- Abstract: In cells, ESCRT-III is unique in mediating fission of membrane necks from inside, a process called reverse-topology fission. Yet, in vitro, the complex primarily assembles outside membrane necks and mediates fission with normal topology. Here, we show that the direction of ESCRT-mediated membrane deformation emerges from bilayer asymmetry rather than being intrinsically encoded by the ESCRT machinery alone. Using ge...
- Summary (fallback): 机器翻译摘要显示：在细胞中，ESCRT-III 在从内部介导膜颈裂变方面具有独特性，这一过程称为逆拓扑裂变。然而，在体外，该复合物主要在膜颈外组装并以正常拓扑介导裂变。在这里，我们表明 ESCRT 介导的膜变形的方向是由双层不对称性产生的，而不是仅由 ESCRT 机制内在编码。利用芽殖酵母中的遗传扰动，我们发现磷脂不对称性和鞘脂稳态的破坏并不能消除ESCRT依赖性运输，而是使ILV形成对膜物理状态高度敏感，导致低效的货物分类和停滞的内体中间体的积累。
- Keywords: membrane, bilayer, emerges, asymmetry, fission

### 19. [印记调控网络揭示了拟南芥胚乳中父本和母本基因组之间的分子串扰](https://www.biorxiv.org/content/10.64898/2026.07.23.740329v1)
- Original title: Imprinted regulatory networks reveal the molecular cross-talk between paternal and maternal genomes in the endosperm of Arabidopsis arenosa
- Authors: Budinsky, T., Kovacik, M., Cermak, V., Pribylova, A., Salony, S. et al.
- Meta: 2026-07-24 | plant biology | DOI: 10.64898/2026.07.23.740329
- 中文摘要: 印记基因并不单独影响种子发育，而是作为一个复杂的网络——就像任何其他基因一样。然而，它们所嵌入的分子背景，即它们的基因网络，在很大程度上仍未得到充分研究。为了解决这一知识差距，我们在物种水平上描述了拟南芥的印记组，并使用基因调控网络分析。我们表明，基因组印记仅优先影响少数途径，为剂量敏感过程和亲本冲突的分子领域提供了候选者。在这些途径中，一些印记基因充当枢纽基因，其中NRPE1突出了表观遗传学在胚乳发育中的重要性。亲代基因组之间的相互作用是相当片面的：父系表达的调节因子优先针对 PEG，而母系表达的调节因子不加区别地针对 PEG 和 MEG。
- Abstract: Imprinted genes do not act alone to shape seed development, but as a complex network - just like any other gene. Yet, the molecular context in which they are embedded, i.e. their gene network, remains largely understudied. To address this knowledge gap, we characterized the imprintome of Arabidopsis arenosa at the species-level and used gene regulatory network analyses. We show that genomic imprinting preferentially...
- Summary (fallback): 机器翻译摘要显示：印记基因并不单独影响种子发育，而是作为一个复杂的网络——就像任何其他基因一样。然而，它们所嵌入的分子背景，即它们的基因网络，在很大程度上仍未得到充分研究。为了解决这一知识差距，我们在物种水平上描述了拟南芥的印记组，并使用基因调控网络分析。我们表明，基因组印记仅优先影响少数途径，为剂量敏感过程和亲本冲突的分子领域提供了候选者。在这些途径中，一些印记基因充当枢纽基因，其中NRPE1突出了表观遗传学在胚乳发育中的重要性。亲代基因组之间的相互作用是相当片面的：父系表达的调节因子优先针对 PEG，而母系表达的调节因子不加区别地针对 PEG 和 MEG。
- Keywords: molecular, parental, imprinted, paternal, maternal

### 20. [衣藻乙醇酸脱氢酶的叶绿体表达改善光呼吸旁路](https://www.biorxiv.org/content/10.64898/2026.07.23.739952v1)
- Original title: Chloroplast expression of Chlamydomonas glycolate dehydrogenase en route to an improved photorespiratory bypass
- Authors: Jeong, J., Baek, K., Thomas, S., Stutz, S. S., Staub, J. M. et al.
- Meta: 2026-07-24 | plant biology | DOI: 10.64898/2026.07.23.739952
- 中文摘要: 光呼吸旁路途径工程的成功依赖于核转化，需要亚细胞靶向和蛋白质定位于光呼吸的目标细胞器中。在当前的研究中，线粒体衣藻乙醇酸脱氢酶（CrGDH）直接在衣藻和烟草的叶绿体中表达，作为光呼吸旁路的第一个酶促步骤。随后在衣藻中进行了概念验证实验，转基因烟草品系证实了活性 CrGDH 蛋白叶绿体的积累。在测试条件下，光合速率和生物量与野生型植物相当或更低，表明单独 CrGDH 的叶绿体表达不足以改善植物性能。
- Abstract: Successes with photorespiratory bypass pathway engineering have relied on nuclear transformation, requiring subcellular targeting and protein localization in the target organelles for photorespiration. In the current study, mitochondrial Chlamydomonas glycolate dehydrogenase (CrGDH) was directly expressed in chloroplasts of Chlamydomonas and tobacco, as the first enzymatic step for a photorespiratory bypass. Proof-o...
- Summary (fallback): 机器翻译摘要显示：光呼吸旁路途径工程的成功依赖于核转化，需要亚细胞靶向和蛋白质定位于光呼吸的目标细胞器中。在当前的研究中，线粒体衣藻乙醇酸脱氢酶（CrGDH）直接在衣藻和烟草的叶绿体中表达，作为光呼吸旁路的第一个酶促步骤。随后在衣藻中进行了概念验证实验，转基因烟草品系证实了活性 CrGDH 蛋白叶绿体的积累。在测试条件下，光合速率和生物量与野生型植物相当或更低，表明单独 CrGDH 的叶绿体表达不足以改善植物性能。
- Keywords: photorespiratory, bypass, crgdh, chloroplast, chlamydomonas

### 21. [植物病毒选择性地重新利用真核 DNA 复制机制](https://www.biorxiv.org/content/10.64898/2026.07.23.740281v1)
- Original title: Selective repurposing of the eukaryotic DNA replication machinery by a plant virus
- Authors: Shi, C., Medina-Puche, L., Pott, D. M., Wei, H., Acatay, S. et al.
- Meta: 2026-07-24 | plant biology | DOI: 10.64898/2026.07.23.740281
- 中文摘要: 在细胞核中复制的真核 DNA 病毒通常利用宿主 DNA 复制机制的组件进行基因组复制。双生病毒是世界范围内毁灭性农作物病害的病原体，严格依赖宿主因素来复制其环状单链 (ss) DNA 基因组，此过程只需要一个病毒编码蛋白 Rep。 Rep 将宿主复制蛋白招募到病毒基因组中，并在滚环复制的起始和终止位点催化切口和连接。尽管双生病毒复制依赖于植物蛋白，但病毒复制体的组成仍然很大程度上未知。在这里，我们使用基于 TurboID 的邻近标记来识别感染过程中双生病毒番茄黄曲叶病毒 (TYLCV) 和苘麻花叶病毒 (AbMV) 的 Rep 蛋白附近的植物蛋白。
- Abstract: Eukaryotic DNA viruses that replicate in the nucleus often exploit components of the host DNA replication machinery for genome replication. Geminiviruses, causal agents of devastating crop diseases worldwide, strictly depend on host factors to replicate their circular single-stranded (ss) DNA genomes, with only a single virus-encoded protein, Rep, required for this process. Rep recruits host replication proteins to...
- Summary (fallback): 机器翻译摘要显示：在细胞核中复制的真核 DNA 病毒通常利用宿主 DNA 复制机制的组件进行基因组复制。双生病毒是世界范围内毁灭性农作物病害的病原体，严格依赖宿主因素来复制其环状单链 (ss) DNA 基因组，此过程只需要一个病毒编码蛋白 Rep。 Rep 将宿主复制蛋白招募到病毒基因组中，并在滚环复制的起始和终止位点催化切口和连接。尽管双生病毒复制依赖于植物蛋白，但病毒复制体的组成仍然很大程度上未知。在这里，我们使用基于 TurboID 的邻近标记来识别感染过程中双生病毒番茄黄曲叶病毒 (TYLCV) 和苘麻花叶病毒 (AbMV) 的 Rep 蛋白附近的植物蛋白。
- Keywords: replication, eukaryotic, host, proteins, viral

### 22. [人脑类器官细胞命运调节组揭示了 Kruppel 样因子 KLF5 和 KLF8 成为阿尔茨海默病的主要转录调节因子](https://www.biorxiv.org/content/10.64898/2026.07.23.740401v1)
- Original title: Kruppel-like factors KLF5 & KLF8 emerge as master transcriptional regulators of Alzheimers disease, as revealed on cell fate regulomes in human brain organoids
- Authors: Aubert, A., Comby, A.-C., Bramoulle, A., Mendoza-Ferri, M.-G., Azzolin, P. et al.
- Meta: 2026-07-24 | systems biology | DOI: 10.64898/2026.07.23.740401
- 中文摘要: 除了充分描述的 β-淀粉样蛋白板积累和 tau 过度磷酸化之外，阿尔茨海默病 (AD) 还伴随着基因表达的重大变化。在此，我们的目的是揭示在 AD 进展过程中负责基因表达变化的主转录因子 (TF)。为此，我们使用了含有 AD 相关基因突变（APP-Swedish、PSEN1-M146V）的人脑类器官 (BORG)，通过批量和空间分辨转录组学在多个时间点对这些突变进行了追踪。通过重建概括 BORG 发育的基因调控网络 (GRN)，我们鉴定了 110 个 AD 特异性主 TF 的子集，并且对于其中 75 个，我们在其启动子内检索了 KLF5 和/或 KLF8 结合基序。
- Abstract: In addition to the well described beta-amyloid plates accumulation and tau hyper-phosphorylation, Alzheimers disease (AD) is accompanied by major changes in gene expression. Herein, we aimed at revealing master transcription factors (TFs) responsible for gene expression changes during AD progression. For this, we have used human brain organoids (BORGs) harbouring AD-related genetic mutations (APP-Swedish, PSEN1-M146...
- Summary (fallback): 机器翻译摘要显示：除了充分描述的 β-淀粉样蛋白板积累和 tau 过度磷酸化之外，阿尔茨海默病 (AD) 还伴随着基因表达的重大变化。在此，我们的目的是揭示在 AD 进展过程中负责基因表达变化的主转录因子 (TF)。为此，我们使用了含有 AD 相关基因突变（APP-Swedish、PSEN1-M146V）的人脑类器官 (BORG)，通过批量和空间分辨转录组学在多个时间点对这些突变进行了追踪。通过重建概括 BORG 发育的基因调控网络 (GRN)，我们鉴定了 110 个 AD 特异性主 TF 的子集，并且对于其中 75 个，我们在其启动子内检索了 KLF5 和/或 KLF8 结合基序。
- Keywords: factors, master, disease, human, gene

### 23. [扩展的杏仁核协调社交孤立小鼠的社会动机](https://www.biorxiv.org/content/10.64898/2026.07.23.739873v1)
- Original title: Extended amygdala orchestrates social motivation in socially isolated mice
- Authors: Grammer, J., Dryer, A., Tweed, C., Conoscenti, M., Zelikowsky, M.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.23.739873
- 中文摘要: 长期被剥夺社会接触的青少年会对行为产生广泛的不利影响，包括社交厌恶感增加。采用我们最近开发的综合分析来评估社交厌恶，我们发现社交隔离足以导致社交动机下降以及社交恐惧和犹豫增加。无监督的行为分析表明，孤立小鼠的社交厌恶很大程度上是由一种僵化的、类似焦虑的状态驱动的，其特征是高度的社交警惕性。使用交叉的、投射特异性的神经回路扰动和体内成像，我们发现隔离引起的社交动机下降是由从终纹前背床核（adBNST）到伏隔核（NAc）的尚未充分探索的投射控制的。
- Abstract: Juveniles deprived of social contact for an extended period of time demonstrate a broad range of adverse effects on behavior, including increased social aversion. Employing our recently developed integrative assay to assess social aversion, we discovered that social isolation is sufficient to induce decreases in social motivation and increases in social fear and hesitancy. Unsupervised behavioral analyses revealed t...
- Summary (fallback): 机器翻译摘要显示：长期被剥夺社会接触的青少年会对行为产生广泛的不利影响，包括社交厌恶感增加。采用我们最近开发的综合分析来评估社交厌恶，我们发现社交隔离足以导致社交动机下降以及社交恐惧和犹豫增加。无监督的行为分析表明，孤立小鼠的社交厌恶很大程度上是由一种僵化的、类似焦虑的状态驱动的，其特征是高度的社交警惕性。使用交叉的、投射特异性的神经回路扰动和体内成像，我们发现隔离引起的社交动机下降是由从终纹前背床核（adBNST）到伏隔核（NAc）的尚未充分探索的投射控制的。
- Keywords: social, motivation, aversion, extended, isolated

### 24. [因果网络结构预测跨事件的记忆组织和神经恢复](https://www.biorxiv.org/content/10.64898/2026.07.22.740141v1)
- Original title: Causal network structure predicts memory organization and neural reinstatement across events
- Authors: Antony, J. W., Abbas, S., Babb, M. S., Reagh, Z., Ranganath, C.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.22.740141
- 中文摘要: 因果关系似乎在叙事中发挥着核心作用，但它如何影响后来的记忆以及大脑如何创建因果结构尚不清楚。在这里，参与者在功能磁共振成像期间观看并回忆了一个具有五个时间交错的故事情节的电视节目，不同的参与者确定了每对事件之间的因果关系。在行为上，因果关系显着影响回忆组织，在几个预测因素中，最重要的因果关系最能预测回忆的转变。在神经上，默认模式网络（DMN）区域中的跨事件模式反映了因果结构，而事件边界处的 DMN 模式专门重新激活了先前的因果相关事件，这表明因果关系预测了我们将跨时间间隙的相关事件缝合在一起的能力。
- Abstract: Causality appears to play a central role in narratives, but how it influences later memory and how the brain creates causal structure is unclear. Here, participants watched and recalled a TV show featuring five temporally interleaved storylines during fMRI, and different participants determined cause-effect relationships between each pair of events. Behaviorally, causality significantly influenced recall organizatio...
- Summary (fallback): 机器翻译摘要显示：因果关系似乎在叙事中发挥着核心作用，但它如何影响后来的记忆以及大脑如何创建因果结构尚不清楚。在这里，参与者在功能磁共振成像期间观看并回忆了一个具有五个时间交错的故事情节的电视节目，不同的参与者确定了每对事件之间的因果关系。在行为上，因果关系显着影响回忆组织，在几个预测因素中，最重要的因果关系最能预测回忆的转变。在神经上，默认模式网络（DMN）区域中的跨事件模式反映了因果结构，而事件边界处的 DMN 模式专门重新激活了先前的因果相关事件，这表明因果关系预测了我们将跨时间间隙的相关事件缝合在一起的能力。
- Keywords: events, causal, network, causality, structure

### 25. [学习可以稳定时间活动，但不能稳定前额皮质的神经元选择性](https://www.biorxiv.org/content/10.64898/2026.07.23.740357v1)
- Original title: Learning stabilizes temporal activity but not neuronal selectivity in prefrontal cortex
- Authors: Huang, Y.-Y., Mehrke, L. S., Bernklau, T. W., Busse, L., Jacob, S. N.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.23.740357
- 中文摘要: 智能行为需要神经表征随着新的需求而变化，同时保留学习的结构。前额叶皮层是这种能力的核心，但其机制尚不清楚。在这里，我们跟踪内侧前额叶神经元数月，因为小鼠学习了与连续规则切换的关联任务。当试验期间单个神经元活跃时，学习逐渐稳定，但它们对哪些任务变量做出反应却不稳定。即使神经元的活动状况稳定后，也会反复获得、失去或改变选择性。我们开发了稀疏张量分量分析，以表明动态单神经元选择性不是反映随机漂移，而是通过一组固定任务表示的规则依赖重组产生的。
- Abstract: Intelligent behavior requires neural representations to change with new demands while preserving learned structure. The prefrontal cortex is central to this ability, but the mechanisms are unclear. Here, we tracked medial prefrontal neurons for months as mice learned an association task with successive rule switches. Learning progressively stabilized when individual neurons were active during a trial, but not what t...
- Summary (fallback): 机器翻译摘要显示：智能行为需要神经表征随着新的需求而变化，同时保留学习的结构。前额叶皮层是这种能力的核心，但其机制尚不清楚。在这里，我们跟踪内侧前额叶神经元数月，因为小鼠学习了与连续规则切换的关联任务。当试验期间单个神经元活跃时，学习逐渐稳定，但它们对哪些任务变量做出反应却不稳定。即使神经元的活动状况稳定后，也会反复获得、失去或改变选择性。我们开发了稀疏张量分量分析，以表明动态单神经元选择性不是反映随机漂移，而是通过一组固定任务表示的规则依赖重组产生的。
- Keywords: prefrontal, neurons, learning, selectivity, cortex

### 26. [大规模功能耦合和计算建模揭示了工作记忆识别、编码和检索过程中分布式网络连接中的额颞热点](https://www.biorxiv.org/content/10.64898/2026.07.23.740204v1)
- Original title: Large-scale functional coupling and computational modelling reveal frontotemporal hotspots in distributed network connectivity during working memory recognition, encoding, and retrieval
- Authors: Zhang, W., Zhang, H., Deng, Y., Deng, X., Ji, Y. et al.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.23.740204
- 中文摘要: 工作记忆取决于分布式大脑网络的协调活动，但这些相互作用如何支持识别、编码和检索仍不清楚。在这里，我们分析了 36 名癫痫患者执行自然卡片匹配任务时 1,652 个部位的颅内局部场电位。相位-幅度和相位-相位耦合揭示了广泛的条件依赖性相互作用，额叶和颞叶区域成为循环网络枢纽。事件相关分析显示参与者之间可重复的试验内耦合动态。定向相转移熵进一步识别了频率特定的信息流，包括充当 θ 波段源和 alpha 波段接收器的额叶区域。
- Abstract: Working memory depends on coordinated activity across distributed brain networks, but how these interactions support recognition, encoding, and retrieval remains unclear. Here, we analyzed intracranial local field potentials from 1,652 sites in 36 epilepsy patients performing a naturalistic card-matching task. Phase-amplitude and phase-phase coupling revealed widespread condition-dependent interactions, with frontal...
- Summary (fallback): 机器翻译摘要显示：工作记忆取决于分布式大脑网络的协调活动，但这些相互作用如何支持识别、编码和检索仍不清楚。在这里，我们分析了 36 名癫痫患者执行自然卡片匹配任务时 1,652 个部位的颅内局部场电位。相位-幅度和相位-相位耦合揭示了广泛的条件依赖性相互作用，额叶和颞叶区域成为循环网络枢纽。事件相关分析显示参与者之间可重复的试验内耦合动态。定向相转移熵进一步识别了频率特定的信息流，包括充当 θ 波段源和 alpha 波段接收器的额叶区域。
- Keywords: coupling, distributed, working, memory, large-scale

### 27. [Dlx5/6 调节神经周围网络突触耦合并稳定成人皮质小清蛋白神经元网络](https://www.biorxiv.org/content/10.64898/2026.07.23.740286v1)
- Original title: Dlx5/6 regulate perineuronal net-synapse coupling and stabilize adult cortical Parvalbumin neurons networks
- Authors: Belz, L., Aouci, R., Allain, B., Henderson, F., Fontaine, A. et al.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.23.740286
- 中文摘要: 维持成人小白蛋白（PV）中间神经元功能和皮质网络稳定性的转录机制仍知之甚少。我们之前表明，编码转录因子的 Dlx5/6 GABA 能神经元失活会扰乱社交互动并降低前额皮质中的 PV 中间神经元密度。在这里，将转录和组织学分析与离体电生理学和体内脑电图 (EEG) 记录相结合，我们发现 Dlx5/6 调节控制成人皮质中神经周围网 (PNN) 稳态的分子程序。 Dlx5/6 失活导致多个 PNN 相关基因的表达失调，并诱导前额叶和体感皮质中 PNN 网状结构的区域特异性重塑。
- Abstract: The transcriptional mechanisms that maintain adult Parvalbumin (PV) interneuron function and cortical network stability remain poorly understood. We previously showed that the inactivation in GABAergic neurons of Dlx5/6, coding for transcription factors, disrupts social interaction and reduces PV interneuron density in the prefrontal cortex. Here, combining transcriptional and histological analyses with ex vivo elec...
- Summary (fallback): 机器翻译摘要显示：维持成人小白蛋白（PV）中间神经元功能和皮质网络稳定性的转录机制仍知之甚少。我们之前表明，编码转录因子的 Dlx5/6 GABA 能神经元失活会扰乱社交互动并降低前额皮质中的 PV 中间神经元密度。在这里，将转录和组织学分析与离体电生理学和体内脑电图 (EEG) 记录相结合，我们发现 Dlx5/6 调节控制成人皮质中神经周围网 (PNN) 稳态的分子程序。 Dlx5/6 失活导致多个 PNN 相关基因的表达失调，并诱导前额叶和体感皮质中 PNN 网状结构的区域特异性重塑。
- Keywords: dlx5, adult, synaptic, cortical, interneuron

### 28. [CNIH3 是慢 AMPA 受体的分子特征](https://www.biorxiv.org/content/10.64898/2026.07.22.739851v1)
- Original title: CNIH3 is a molecular signature of slow AMPA receptors
- Authors: Boutonnet, M., Noonan, J. D., Pampaloni, N. P., Plested, A.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.22.739851
- 中文摘要: 在兴奋性突触处，谷氨酸激活突触后膜中的受体，包括 AMPA 受体。 AMPA 受体通常被认为是大脑中最快的受体，它可以产生模仿尖峰时间的毫秒突触电位。然而，我们在 CA1 锥体细胞中发现了大量缓慢的 AMPA 反应。这些缓慢的反应显示出单个细胞甚至单个树突中的马赛克分布（Pampaloni 等人，2021）。一项文献调查揭示了小脑、纹状体和其他大脑区域类似缓慢反应的神秘报道（Pampaloni 和 Plested，2022）。这些惊人的观察结果为大脑中 AMPA 受体多样性开辟了新的视角。为了详细研究大脑中这些慢速 AMPA 受体，我们试图确定它们的分子基础。
- Abstract: At excitatory synapses, glutamate activates receptors in the postsynaptic membrane including the AMPA receptor. Usually considered to be the fastest receptor in the brain, AMPA receptors can produce millisecond synaptic potentials that mimic the timing of spikes. However, we found abundant slow AMPA responses in CA1 pyramidal cells. These slow responses show a mosaic distribution in individual cells and even in sing...
- Summary (fallback): 机器翻译摘要显示：在兴奋性突触处，谷氨酸激活突触后膜中的受体，包括 AMPA 受体。 AMPA 受体通常被认为是大脑中最快的受体，它可以产生模仿尖峰时间的毫秒突触电位。然而，我们在 CA1 锥体细胞中发现了大量缓慢的 AMPA 反应。这些缓慢的反应显示出单个细胞甚至单个树突中的马赛克分布（Pampaloni 等人，2021）。一项文献调查揭示了小脑、纹状体和其他大脑区域类似缓慢反应的神秘报道（Pampaloni 和 Plested，2022）。这些惊人的观察结果为大脑中 AMPA 受体多样性开辟了新的视角。为了详细研究大脑中这些慢速 AMPA 受体，我们试图确定它们的分子基础。
- Keywords: ampa, slow, responses, cnih3, brain

### 29. [人类神经元的神经元自噬需要 KIF1A 介导的转运](https://www.biorxiv.org/content/10.64898/2026.07.22.740140v1)
- Original title: KIF1A-mediated trafficking is required for neuronal autophagy in human neurons
- Authors: Borland, C. T., Popolow, J., Holzbaur, E.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.22.740140
- 中文摘要: 分子运动蛋白 KIF1A 的突变会导致一系列神经发育和神经退行性疾病，称为 KIF1A 相关神经障碍 (KAND)。 KIF1A 突变会不同程度地破坏突触小泡运输，但 KIF1A 突变对其他运输途径的影响仍未被探索。自噬是神经元稳态所需的保守途径。我们使用基因编辑的人类 IPSC 衍生神经元研究了 KIF1A 在自噬中的作用。 KIF1A 缺失抑制了 ATG9 的运输，ATG9 是自噬体生物发生所必需的跨膜脂质扰乱酶。这种缺陷显着降低了自噬体的生物发生和轴突自噬体的密度。 KIF1A 缺失还会耗尽轴突中的溶酶体，抑制自噬体成熟。
- Abstract: Mutations in the molecular motor protein KIF1A result in a spectrum of neurodevelopmental and neurodegenerative disorders termed KIF1A-Associated Neurological Disorder (KAND). KIF1A mutations variably disrupt synaptic vesicle trafficking, but the effects of KIF1A mutations on other trafficking pathways remain unexplored. Autophagy is a conserved pathway required for neuronal homeostasis. We investigated the role of...
- Summary (fallback): 机器翻译摘要显示：分子运动蛋白 KIF1A 的突变会导致一系列神经发育和神经退行性疾病，称为 KIF1A 相关神经障碍 (KAND)。 KIF1A 突变会不同程度地破坏突触小泡运输，但 KIF1A 突变对其他运输途径的影响仍未被探索。自噬是神经元稳态所需的保守途径。我们使用基因编辑的人类 IPSC 衍生神经元研究了 KIF1A 在自噬中的作用。 KIF1A 缺失抑制了 ATG9 的运输，ATG9 是自噬体生物发生所必需的跨膜脂质扰乱酶。这种缺陷显着降低了自噬体的生物发生和轴突自噬体的密度。 KIF1A 缺失还会耗尽轴突中的溶酶体，抑制自噬体成熟。
- Keywords: autophagy, kif1a, trafficking, neuronal, neurons

### 30. [自定时运动启动需要前额皮质和小脑中电路的快速顺序协调](https://www.biorxiv.org/content/10.64898/2026.07.23.739940v1)
- Original title: Self-timed movement initiation requires rapid sequential coordination of circuits in prefrontal cortex and cerebellum
- Authors: Monakhov, M. V., Wojaczynski, G. J., Medina, J. F.
- Meta: 2026-07-24 | neuroscience | DOI: 10.64898/2026.07.23.739940
- 中文摘要: 人们对运动启动所需的神经“事件链”知之甚少，特别是对于自定时的内源性动作。在这里，我们引入了一项新任务，要求小鼠在没有外部“开始”信号的情况下以高时间精度自行发起运动。短暂、精确定时的光遗传学光抑制闪光表明，运动的启动是由前额皮质和小脑外侧神经元的快速顺序募集所驱动的。
- Abstract: The neural 'chain of events' necessary for movement initiation is poorly understood, particularly for endogenous actions that are self-timed. Here, we introduce a new task that requires mice to self-initiate a movement with high temporal precision in the absence of external 'go' signals. Brief, precisely timed flashes of optogenetic photoinhibition reveal that movement initiation is causally driven by rapid sequenti...
- Summary (fallback): 机器翻译摘要显示：人们对运动启动所需的神经“事件链”知之甚少，特别是对于自定时的内源性动作。在这里，我们引入了一项新任务，要求小鼠在没有外部“开始”信号的情况下以高时间精度自行发起运动。短暂、精确定时的光遗传学光抑制闪光表明，运动的启动是由前额皮质和小脑外侧神经元的快速顺序募集所驱动的。
- Keywords: movement, initiation, self-timed, requires, rapid

## medrxiv

### 1. [孟加拉国已婚女性青少年生育力的决定因素：2022 年孟加拉国人口和健康调查分析](https://www.medrxiv.org/content/10.64898/2026.07.21.26358612v2)
- Original title: Determinants of adolescent fertility among ever-married women in Bangladesh: an analysis of the 2022 Bangladesh Demographic and Health Survey
- Authors: Khan, M. I. H., Jahan, I., Islam, M. A., Karim, M.
- Meta: 2026-07-24 | sexual and reproductive health | DOI: 10.64898/2026.07.21.26358612
- 中文摘要: 孟加拉国仍然是南亚青少年生育率最高的国家之一，但大多数先前的国家分析并未充分考虑人口和健康调查的复杂调查设计，也没有评估调查结果对缺失数据的稳健性。本研究利用最新的全国代表性数据，研究了孟加拉国 15-19 岁已婚少女中与青春期生育力相关的因素。我们分析了 2022 年孟加拉国人口和健康调查的数据。青少年生育力的定义是当前怀孕或至少生育过一次活产。在 2,449 名 15-19 岁的符合条件的已婚女性中，1,601 名拥有所有模型变量的完整信息被纳入主要完整病例分析。
- Abstract: Bangladesh continues to report one of the highest adolescent fertility rates in South Asia, yet most prior national analyses have not fully accounted for the complex survey design of the Demographic and Health Surveys or assessed the robustness of findings to missing data. Using the most recent nationally representative data, this study examined factors associated with adolescent fertility among ever-married adolesc...
- Summary (fallback): 机器翻译摘要显示：孟加拉国仍然是南亚青少年生育率最高的国家之一，但大多数先前的国家分析并未充分考虑人口和健康调查的复杂调查设计，也没有评估调查结果对缺失数据的稳健性。本研究利用最新的全国代表性数据，研究了孟加拉国 15-19 岁已婚少女中与青春期生育力相关的因素。我们分析了 2022 年孟加拉国人口和健康调查的数据。青少年生育力的定义是当前怀孕或至少生育过一次活产。在 2,449 名 15-19 岁的符合条件的已婚女性中，1,601 名拥有所有模型变量的完整信息被纳入主要完整病例分析。
- Keywords: adolescent, fertility, bangladesh, years, women

### 2. [膝关节或髋关节置换术后住院患者阿片类药物剂量的多祖先全基因组关联研究](https://www.medrxiv.org/content/10.1101/2025.07.23.25331996v2)
- Original title: Multi-ancestry Genome-wide Association Study of Inpatient Opioid Dosing Following Knee or Hip Arthroplasty
- Authors: Jinwala, Z., Davis, C. N., SooHoo, J. F., Million Veteran Program,, Gelernter, J. et al.
- Meta: 2026-07-24 | genetic and genomic medicine | DOI: 10.1101/2025.07.23.25331996
- 中文摘要: 阿片类药物通常用于治疗术后急性疼痛。然而，阿片类药物的给药模式和实践存在相当大的差异，这部分归因于患者的特征。我们使用电子健康记录 (EHR) 和百万退伍军人计划样本的基因型数据来研究膝关节或髋关节置换术后住院患者阿片类镇痛药物暴露个体差异的遗传预测因素 (n = 27,896)。我们从住院患者服用阿片类药物的药房记录中提取数据，以得出住院患者术后期间平均​​每日阿片类药物暴露量的指标。
- Abstract: Opioids are commonly prescribed to manage acute postoperative pain. However, there is considerable variability in opioid administration patterns and practices, which is partially attributable to patient characteristics. We used electronic health record (EHR) and genotype data from the Million Veteran Program sample to investigate genetic predictors of individual differences in inpatient opioid analgesic exposure fol...
- Summary (fallback): 机器翻译摘要显示：阿片类药物通常用于治疗术后急性疼痛。然而，阿片类药物的给药模式和实践存在相当大的差异，这部分归因于患者的特征。我们使用电子健康记录 (EHR) 和百万退伍军人计划样本的基因型数据来研究膝关节或髋关节置换术后住院患者阿片类镇痛药物暴露个体差异的遗传预测因素 (n = 27,896)。我们从住院患者服用阿片类药物的药房记录中提取数据，以得出住院患者术后期间平均​​每日阿片类药物暴露量的指标。
- Keywords: gwas, opioid, inpatient, genetic, genome-wide

### 3. [1 型糖尿病患者连续餐后血糖监测的因果中介途径](https://www.medrxiv.org/content/10.64898/2026.03.16.26348520v3)
- Original title: Causal Mediation Pathways in Continuous Postprandial Glucose Monitoring for Type 1 Diabetes Patients
- Authors: Hilligoss, S., Qu, A.
- Meta: 2026-07-24 | endocrinology | DOI: 10.64898/2026.03.16.26348520
- 中文摘要: 管理 1 型糖尿病 (T1DM) 的餐后血糖需要了解碳水化合物摄入如何通过直接途径和胰岛素介导的补偿影响血糖。标准分析将胰岛素视为混杂因素而不是中介因素，从而掩盖了碳水化合物反应中这些不同的因果通道和患者水平的异质性。使用俄亥俄州 T1DM 队列中 12 名成年人以膳食为中心的连续血糖监测窗口，我们应用因果中介分析，按膳食类型和结果分位数将碳水化合物摄入对血糖变化的总效应分解为平均直接效应 (ADE)、胰岛素介导效应 (ACME) 和总效应。为了调整餐前混杂，我们引入了一种因果约束线性自动编码器，它可以学习低维表示，从而改善对测量的餐前状态的调整。
- Abstract: Managing postprandial glucose in Type 1 Diabetes Mellitus (T1DM) requires understanding how carbohydrate intake affects glucose through both direct pathways and insulin-mediated compensation. Standard analyses treat insulin as a confounder rather than a mediator, obscuring these distinct causal channels and patient-level heterogeneity in carbohydrate response. Using meal-centered continuous glucose monitoring window...
- Summary (fallback): 机器翻译摘要显示：管理 1 型糖尿病 (T1DM) 的餐后血糖需要了解碳水化合物摄入如何通过直接途径和胰岛素介导的补偿影响血糖。标准分析将胰岛素视为混杂因素而不是中介因素，从而掩盖了碳水化合物反应中这些不同的因果通道和患者水平的异质性。使用俄亥俄州 T1DM 队列中 12 名成年人以膳食为中心的连续血糖监测窗口，我们应用因果中介分析，按膳食类型和结果分位数将碳水化合物摄入对血糖变化的总效应分解为平均直接效应 (ADE)、胰岛素介导效应 (ACME) 和总效应。为了调整餐前混杂，我们引入了一种因果约束线性自动编码器，它可以学习低维表示，从而改善对测量的餐前状态的调整。
- Keywords: glucose, postprandial, carbohydrate, causal, type

### 4. [用于本迪布焦埃博拉病毒爆发应对的环形和社区疫苗接种：随机网络建模研究](https://www.medrxiv.org/content/10.64898/2026.07.09.26357654v2)
- Original title: Ring and community vaccination for Bundibugyo ebolavirus outbreak response: a stochastic network modelling study
- Authors: Andrews, J. R., Placide, M., MUKADI, P., Kindrachuk, J., Hoff, N. A. et al.
- Meta: 2026-07-24 | public and global health | DOI: 10.64898/2026.07.09.26357654
- 中文摘要: 背景：rVSV-ZEBOV 疫苗对扎伊尔埃博拉病毒非常有效，但对本迪布焦埃博拉病毒 (BDBV) 的保护作用尚未得到证实。我们评估了 BDBV 爆发期间在实际操作限制下部分交叉保护性假设疫苗的相对人群影响和剂量效率。方法：我们在两层家庭-社区联系网络上开发了一个随机传播模型，并根据 2026 年刚果民主共和国 BDBV 疫情数据进行了校准。使用贝叶斯更新模型估计随时间变化的有效繁殖数。我们评估了病例检测、隔离、接触者追踪、反应环疫苗接种和社区疫苗接种（覆盖率 20-80%）。基本情况疫苗功效为 45%，包括针对疾病和死亡的暴露后保护。
- Abstract: Background: Vaccination with rVSV-ZEBOV is highly effective against Zaire ebolavirus, but protection against Bundibugyo ebolavirus (BDBV) is unproven. We evaluated the relative population impact and dose efficiency of a partially cross-protective hypothetical vaccine under operationally realistic constraints during a BDBV outbreak. Methods: We developed a stochastic transmission model on a two-layer household-commun...
- Summary (fallback): 机器翻译摘要显示：背景：rVSV-ZEBOV 疫苗对扎伊尔埃博拉病毒非常有效，但对本迪布焦埃博拉病毒 (BDBV) 的保护作用尚未得到证实。我们评估了 BDBV 爆发期间在实际操作限制下部分交叉保护性假设疫苗的相对人群影响和剂量效率。方法：我们在两层家庭-社区联系网络上开发了一个随机传播模型，并根据 2026 年刚果民主共和国 BDBV 疫情数据进行了校准。使用贝叶斯更新模型估计随时间变化的有效繁殖数。我们评估了病例检测、隔离、接触者追踪、反应环疫苗接种和社区疫苗接种（覆盖率 20-80%）。基本情况疫苗功效为 45%，包括针对疾病和死亡的暴露后保护。
- Keywords: vaccination, mortality, operations, ring, doses
