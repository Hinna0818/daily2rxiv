# daily2rxiv Digest - 2026-07-14

共收录 67 篇论文。

## arxiv

### 1. [顺序编码：利用自行生成的训练数据突破模型压缩的极限](https://arxiv.org/abs/2607.11883v1)
- Original title: Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data
- Authors: Shikai Qiu, Marc Finzi, Yujia Zheng, Kun Zhang, Andrew Gordon Wilson
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 压缩是智能的基础。可以将其训练数据表示为短代码的模型已经发现了能够进行泛化的规律。大型神经网络学习的函数可能比其参数计数所显示的简单得多，但构建实现这种简单性的代码具有挑战性。基于参数的方法（例如量化）产生的代码长度随模型大小而变化，对参数存储的信息量不敏感。前置编码通过压缩训练轨迹来绕过这个问题，但无论模型学习多少，都会对精确的数据序列进行编码，当数据具有高熵时会产生大代码。我们引入了顺序编码，其中教师模型从学生自己的分布中选择训练样本。
- Abstract: Compression is fundamental to intelligence. A model that can represent its training data as a short code has discovered regularities that enable generalization. Large neural networks may learn functions far simpler than their parameter counts suggest, but it is challenging to construct codes that realize this simplicity. Parameter-based methods such as quantization produce code lengths that scale with model size, in...
- Summary (fallback): 机器翻译摘要显示：压缩是智能的基础。可以将其训练数据表示为短代码的模型已经发现了能够进行泛化的规律。大型神经网络学习的函数可能比其参数计数所显示的简单得多，但构建实现这种简单性的代码具有挑战性。基于参数的方法（例如量化）产生的代码长度随模型大小而变化，对参数存储的信息量不敏感。前置编码通过压缩训练轨迹来绕过这个问题，但无论模型学习多少，都会对精确的数据序列进行编码，当数据具有高熵时会产生大代码。我们引入了顺序编码，其中教师模型从学生自己的分布中选择训练样本。
- Keywords: code, model, training, requential, coding

### 2. [归纳推理任务中 Transformers 的不变学习动态](https://arxiv.org/abs/2607.11875v1)
- Original title: Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks
- Authors: Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet, Thomas Hofmann
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 我们提出了一个理论框架来解释 Transformer 语言模型中归纳推理能力的出现。虽然迄今为止关于 Transformer 学习动态的工作大多与特定任务相关，但我们研究了一类归纳任务，它统一了文献中已知的几个合成任务，包括上下文 n 元语法和多跳推理。在本课程中，我们从理论上证明注意力模型的训练动态可以局限于高度可解释的低维不变流形。在这个流形上，学习动态是由少数可解释的坐标而不是数百万个参数捕获的，这使得理论和实证分析都更容易处理。
- Abstract: We present a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models. While previous works on Transformer learning dynamics have so far been mostly tied to specific tasks, we study a generalized class of inductive tasks that unifies several synthetic tasks known in the literature, including in-context n-grams and multi-hop reasoning. In this class, we theoretica...
- Summary (fallback): 机器翻译摘要显示：我们提出了一个理论框架来解释 Transformer 语言模型中归纳推理能力的出现。虽然迄今为止关于 Transformer 学习动态的工作大多与特定任务相关，但我们研究了一类归纳任务，它统一了文献中已知的几个合成任务，包括上下文 n 元语法和多跳推理。在本课程中，我们从理论上证明注意力模型的训练动态可以局限于高度可解释的低维不变流形。在这个流形上，学习动态是由少数可解释的坐标而不是数百万个参数捕获的，这使得理论和实证分析都更容易处理。
- Keywords: learning, dynamics, tasks, inductive, reasoning

### 3. [一种用于灵巧操作的极简重定向引导强化学习方法](https://arxiv.org/abs/2607.11874v1)
- Original title: A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation
- Authors: Yunhai Feng, Natalie Leung, Jiaxuan Wang, Lujie Yang, Haozhi Qi et al.
- Meta: 2026-07-13 | cs.RO
- 中文摘要: 最近在人形全身控制方面的工作通过一个简单的方法取得了成功：将人体运动重新定位到机器人运动学参考，然后通过强化学习（RL）训练策略来跟踪它们。但这个秘诀如何转化为灵巧的操作呢？答案并不明显，因为操纵涉及复杂的、接触丰富的动力学，并且需要对接触模式和力进行微妙的调节。我们推出了 REGRIND，这是一种极简主义的重定向引导的 RL 管道，可以从单个人类演示中学习灵巧的操纵策略。 REGRIND 将人类手部物体运动重新定位到保留手部物体空间和接触关系的机器人参考，在模拟中训练剩余强化学习策略以跟踪沿该参考的以物体为中心的关键点，并通过仔细的系统识别将生成的策略零样本传输到硬件。
- Abstract: Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires delicate regulation of contact modes and forces. We present...
- Summary (fallback): 机器翻译摘要显示：最近在人形全身控制方面的工作通过一个简单的方法取得了成功：将人体运动重新定位到机器人运动学参考，然后通过强化学习（RL）训练策略来跟踪它们。但这个秘诀如何转化为灵巧的操作呢？答案并不明显，因为操纵涉及复杂的、接触丰富的动力学，并且需要对接触模式和力进行微妙的调节。我们推出了 REGRIND，这是一种极简主义的重定向引导的 RL 管道，可以从单个人类演示中学习灵巧的操纵策略。 REGRIND 将人类手部物体运动重新定位到保留手部物体空间和接触关系的机器人参考，在模拟中训练剩余强化学习策略以跟踪沿该参考的以物体为中心的关键点，并通过仔细的系统识别将生成的策略零样本传输到硬件。
- Keywords: manipulation, dexterous, learning, recipe, human

### 4. [经过验证的教学反馈分类协议的耐用性和跨语言传输基准](https://arxiv.org/abs/2607.11873v1)
- Original title: A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol
- Authors: Esteban U. Vega Barajas
- Meta: 2026-07-13 | cs.CL
- 中文摘要: 机构收集的开放式教学评估反馈比他们阅读的要多得多。先前的一项研究引入了一种经过验证的协议，用于按主题类别和情感对此类评论进行分类，该协议是根据记录的注释指南、注释者内部可靠性测量、分层交叉验证以及对具有冻结编码器设计的西班牙机构语料库的保留评估构建的。有两个问题限制了它的重用：随着表示方法的进步，固定于 2019 年时代冻结嵌入的协议是否保持竞争力，以及它是否转移到第二语言。我们在三个表示代、稀疏词汇特征、冻结变压器嵌入和提示大型语言模型的原始西班牙语数据上重新运行它，并将其情感任务转移到英语，并根据方面标记的教育数据集检查了平衡的 45,000 条评论语料库。
- Abstract: Institutions collect far more open-ended teaching-evaluation feedback than they read. A prior study introduced a validated protocol for classifying such comments by thematic category and sentiment, built from a documented annotation guide, an intra-annotator reliability measurement, stratified cross-validation, and a held-out evaluation on a Spanish institutional corpus with a frozen-encoder design. Two questions li...
- Summary (fallback): 机器翻译摘要显示：机构收集的开放式教学评估反馈比他们阅读的要多得多。先前的一项研究引入了一种经过验证的协议，用于按主题类别和情感对此类评论进行分类，该协议是根据记录的注释指南、注释者内部可靠性测量、分层交叉验证以及对具有冻结编码器设计的西班牙机构语料库的保留评估构建的。有两个问题限制了它的重用：随着表示方法的进步，固定于 2019 年时代冻结嵌入的协议是否保持竞争力，以及它是否转移到第二语言。我们在三个表示代、稀疏词汇特征、冻结变压器嵌入和提示大型语言模型的原始西班牙语数据上重新运行它，并将其情感任务转移到英语，并根据方面标记的教育数据集检查了平衡的 45,000 条评论语料库。
- Keywords: protocol, sentiment, spanish, model, transfer

### 5. [不公平法官的内部：法学硕士法官偏见的机械解释](https://arxiv.org/abs/2607.11871v1)
- Original title: Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias
- Authors: Zixiang Xu, Sixian Li, Huaxing Liu, Xiang Wang, Shuai Li et al.
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 现有的关于法学硕士作为法官评分偏差的研究主要在输入输出层面进行：它们扰乱输入，测量分数增量，并提出即时级别的缓解措施。我们认为，同样的偏见承认法官隐藏状态中的表征水平帐户，与输入输出视图相补充，并且在操作上有用，但它无法提供。我们报告了针对七名法官、七种偏见类型和九个基准的三项调查结果。几何：基线判断输入占据一个紧密的激活流形，而有偏差的输入沿着低维、特定类型的子空间移位，该子空间随着深度而锐化，并由三个估计器系列一致地恢复。
- Abstract: Existing studies of LLM-as-judge scoring bias work predominantly at the input-output level: they perturb inputs, measure score deltas, and propose prompt-level mitigations. We argue that the same biases admit a representation-level account in the judge's hidden state, complementary to the input-output view and operationally useful in ways it does not afford. We report three findings, across seven judges, seven bias...
- Summary (fallback): 机器翻译摘要显示：现有的关于法学硕士作为法官评分偏差的研究主要在输入输出层面进行：它们扰乱输入，测量分数增量，并提出即时级别的缓解措施。我们认为，同样的偏见承认法官隐藏状态中的表征水平帐户，与输入输出视图相补充，并且在操作上有用，但它无法提供。我们报告了针对七名法官、七种偏见类型和九个基准的三项调查结果。几何：基线判断输入占据一个紧密的激活流形，而有偏差的输入沿着低维、特定类型的子空间移位，该子空间随着深度而锐化，并由三个估计器系列一致地恢复。
- Keywords: bias, scoring, inputs, judge, input-output

### 6. [针对量子神经网络的输入感知动态后门攻击](https://arxiv.org/abs/2607.11843v1)
- Original title: Input-Aware Dynamic Backdoor Attack Against Quantum Neural Networks
- Authors: Junrui Zhang, Zemin Chen, Lusi Li, Mohammad Ghasemigol, Daniel Takabi et al.
- Meta: 2026-07-13 | quant-ph
- 中文摘要: 量子神经网络（QNN）是近期量子设备上量子机器学习的一个有前途的框架，但它们的安全风险仍然没有得到充分的了解。研究表明，QNN 很容易受到后门攻击，但现有的量子后门大多依赖于所有中毒输入共享的固定触发器。这种固定触发设计是一个主要弱点，因为许多防御措施会检测或削弱此类触发在数据表示中留下的重复模式。尽管输入感知动态后门已经在经典神经网络中进行了研究，但将它们转移到 QNN 中很困难，因为量子学习引入了新的障碍。
- Abstract: Quantum Neural Networks (QNNs) are a promising framework for quantum machine learning on near-term quantum devices, but their security risks remain insufficiently understood. Studies have shown that QNNs are vulnerable to backdoor attacks, yet existing quantum backdoors mostly rely on a fixed trigger shared by all poisoned inputs. This fixed-trigger design is a major weakness because many defenses detect or weaken t...
- Summary (fallback): 机器翻译摘要显示：量子神经网络（QNN）是近期量子设备上量子机器学习的一个有前途的框架，但它们的安全风险仍然没有得到充分的了解。研究表明，QNN 很容易受到后门攻击，但现有的量子后门大多依赖于所有中毒输入共享的固定触发器。这种固定触发设计是一个主要弱点，因为许多防御措施会检测或削弱此类触发在数据表示中留下的重复模式。尽管输入感知动态后门已经在经典神经网络中进行了研究，但将它们转移到 QNN 中很困难，因为量子学习引入了新的障碍。
- Keywords: quantum, attack, input-aware, qnns, trigger

### 7. [用于节俭神经架构搜索的变压器引导群体智能](https://arxiv.org/abs/2607.11826v1)
- Original title: Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search
- Authors: Romain Amigon
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 神经架构搜索 (NAS) 实现了深度学习模型设计的自动化，但传统上需要大量计算资源，通常以数千个 GPU 天来衡量。在本文中，我们提出了一种节俭且模因的 NAS 框架，旨在实现消费级硬件架构设计的民主化。我们的方法结合了通过强化学习 (RL) 训练的自回归 Transformer 控制器的全局宏观搜索功能和人工蜂群 (ABC) 算法的局部微开发。为了防止 RL 阶段过早收敛，我们引入了动态熵机制，在检测到性能停滞时强制进行拓扑探索。在标准 GPU (NVIDIA RTX 3060) 上进行评估，我们的混合方法有效解决了元启发法固有的“冷启动”问题。
- Abstract: Neural Architecture Search (NAS) has automated the design of deep learning models but traditionally requires massive computational resources, often measured in thousands of GPU-days. In this paper, we propose a frugal and memetic NAS framework designed to democratize architecture design on consumer-grade hardware. Our approach combines the global macro-search capabilities of an autoregressive Transformer controller,...
- Summary (fallback): 机器翻译摘要显示：神经架构搜索 (NAS) 实现了深度学习模型设计的自动化，但传统上需要大量计算资源，通常以数千个 GPU 天来衡量。在本文中，我们提出了一种节俭且模因的 NAS 框架，旨在实现消费级硬件架构设计的民主化。我们的方法结合了通过强化学习 (RL) 训练的自回归 Transformer 控制器的全局宏观搜索功能和人工蜂群 (ABC) 算法的局部微开发。为了防止 RL 阶段过早收敛，我们引入了动态熵机制，在检测到性能停滞时强制进行拓扑探索。在标准 GPU (NVIDIA RTX 3060) 上进行评估，我们的混合方法有效解决了元启发法固有的“冷启动”问题。
- Keywords: architecture, search, learning, framework, frugal

### 8. [黑色素瘤 MITF 变阻器的新兴群体动态的定量模型](https://arxiv.org/abs/2607.11820v1)
- Original title: A quantitative model for the emergent population dynamics of the melanoma MITF rheostat
- Authors: Keith L. Chambers, Richard M. White, Colin R. Goding, Helen M. Byrne
- Meta: 2026-07-13 | q-bio.CB
- 中文摘要: 癌症进展是由具有相同驱动突变的细胞采用生物学上不同的适应性表型的能力驱动的。然而，肿瘤内表型异质性所暗示的群体动态却知之甚少。黑色素瘤是一种高度侵袭性的皮肤癌，是探索表型转换的绝佳模型，部分原因是表型身份是由黑素细胞相关转录因子 (MITF) 活性赋予的。在这里，我们开发并分析了表皮黑色素瘤细胞群的多尺度表型结构 PDE 模型，从亚细胞 MITF 动力学发展到充分混合和径向解析的群体模型。
- Abstract: Cancer progression is driven by the ability of cells with identical driver mutations to adopt biologically distinct adaptive phenotypes. Yet the population dynamics implied by intratumour phenotypic heterogeneity is poorly understood. Melanoma, a highly aggressive skin cancer, represents an excellent model to explore phenotype-switching, in part because phenotypic identity is conferred by melanocyte-associated trans...
- Summary (fallback): 机器翻译摘要显示：癌症进展是由具有相同驱动突变的细胞采用生物学上不同的适应性表型的能力驱动的。然而，肿瘤内表型异质性所暗示的群体动态却知之甚少。黑色素瘤是一种高度侵袭性的皮肤癌，是探索表型转换的绝佳模型，部分原因是表型身份是由黑素细胞相关转录因子 (MITF) 活性赋予的。在这里，我们开发并分析了表皮黑色素瘤细胞群的多尺度表型结构 PDE 模型，从亚细胞 MITF 动力学发展到充分混合和径向解析的群体模型。
- Keywords: melanoma, population, dynamics, model, cells

### 9. [通过仅干预的因果发现来放松忠诚度](https://arxiv.org/abs/2607.11816v1)
- Original title: Relaxing Faithfulness with Intervention-Only Causal Discovery
- Authors: Bijan Mazaheri, Jiaqi Zhang, Caroline Uhler
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 因果发现算法学习一个描述随机变量之间因果关系的网络。常见的工作流程首先利用观测数据的条件独立性来确定部分定向因果关系，然后应用干预措施来确定未知的因果方向。第一步的关键假设是忠实性：要求因果关联的变量表现出统计依赖性。许多自然系统都包含缓冲和稳定途径，这些途径相互抵消以实现系统的稳健性。这种路径的取消违反了忠实性，导致因果发现算法错误地消除了因果依赖性。在本文中，我们认为硬干预包含有关因果关系存在/不存在的信息，而这些信息在结构发现的第一阶段被忽视。
- Abstract: Causal discovery algorithms learn a network that describes the causal dependencies among random variables. A common workflow involves first utilizing conditional independence properties on observational data to determine partially directed causal relationships, then applying interventions to orient the unknown causal directions. A critical assumption for the first step is faithfulness: a requirement that causally li...
- Summary (fallback): 机器翻译摘要显示：因果发现算法学习一个描述随机变量之间因果关系的网络。常见的工作流程首先利用观测数据的条件独立性来确定部分定向因果关系，然后应用干预措施来确定未知的因果方向。第一步的关键假设是忠实性：要求因果关联的变量表现出统计依赖性。许多自然系统都包含缓冲和稳定途径，这些途径相互抵消以实现系统的稳健性。这种路径的取消违反了忠实性，导致因果发现算法错误地消除了因果依赖性。在本文中，我们认为硬干预包含有关因果关系存在/不存在的信息，而这些信息在结构发现的第一阶段被忽视。
- Keywords: causal, interventions, faithfulness, discovery, first

### 10. [选择性状态空间模型中状态使用的精确工具，以及它揭示的输入驱动迁移](https://arxiv.org/abs/2607.11796v1)
- Original title: An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals
- Authors: Raktim Bhattacharya
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 选择性状态空间模型（例如 Mamba）通过一组一阶模式传递信息，这些一阶模式的输入耦合由学习选择机制设置。我们提供了一种精确的工具来测量经过训练的模型如何使用这些模式。因为状态矩阵是对角矩阵，所以每个通道的输出精确地分解为每个模式的贡献，并且每个（层、通道、窗口）Gram 张量产生在任何预算下离线丢弃任何模式子集的精确输出误差。在 Mamba-1 系列上，根据参考实现的相对误差 $2.3\times10^{-7}$ 进行验证，该工具准确无误，预测层的部署修剪误差在 $4{,}464$ 配置上的中值相对偏差为 $5\times10^{-7}$，其下限由重建设置。
- Abstract: Selective state-space models such as Mamba route information through a bank of first-order modes whose input coupling is set by a learned selection mechanism. We give an exact instrument for measuring how a trained model uses these modes. Because the state matrix is diagonal, each channel's output decomposes exactly into per-mode contributions, and a per-(layer, channel, window) Gram tensor yields the exact output e...
- Summary (fallback): 机器翻译摘要显示：选择性状态空间模型（例如 Mamba）通过一组一阶模式传递信息，这些一阶模式的输入耦合由学习选择机制设置。我们提供了一种精确的工具来测量经过训练的模型如何使用这些模式。因为状态矩阵是对角矩阵，所以每个通道的输出精确地分解为每个模式的贡献，并且每个（层、通道、窗口）Gram 张量产生在任何预算下离线丢弃任何模式子集的精确输出误差。在 Mamba-1 系列上，根据参考实现的相对误差 $2.3\times10^{-7}$ 进行验证，该工具准确无误，预测层的部署修剪误差在 $4{,}464$ 配置上的中值相对偏差为 $5\times10^{-7}$，其下限由重建设置。
- Keywords: exact, instrument, state, modes, error

### 11. [用于血管内介入治疗的紧凑型顶部装载机器人：设计、控制和评估](https://arxiv.org/abs/2607.11779v1)
- Original title: A Compact Top-Loading Robot for Endovascular Interventions: Design, Control and Evaluation
- Authors: Jonas Fischer, Lennart Karstensen, Franziska Mathis-Ullrich
- Meta: 2026-07-13 | cs.RO
- 中文摘要: 机器人辅助血管内介入治疗可以潜在地减少辐射暴露，改善外科医生的人体工程学，实现远程手术，支持主动协助和自主性，并提高手术精度。然而，现有系统的程序覆盖范围往往有限，因为患者侧设置受限、灵活性有限以及复杂的仪器交换阻碍了临床工作流程集成。这项工作提出了一种用于血管内介入治疗的紧凑型机器人系统，可以对标准血管内器械进行连续平移和旋转操作。该系统由两个交替推车组成，其气动薄膜夹具集成到旋转夹具齿轮中。其顶部装载设计允许快速更换导丝和导管等器械，而无需改变机器人设置。
- Abstract: Robot-assisted endovascular intervention can potentially reduce radiation exposure, improve surgeon ergonomics, enable telesurgery, support active assistance and autonomy, and enhance procedural precision. However, existing systems often suffer from limited procedural coverage because constrained patient-side setups, restricted flexibility, and complex instrument exchange hinder clinical workflow integration. This w...
- Summary (fallback): 机器翻译摘要显示：机器人辅助血管内介入治疗可以潜在地减少辐射暴露，改善外科医生的人体工程学，实现远程手术，支持主动协助和自主性，并提高手术精度。然而，现有系统的程序覆盖范围往往有限，因为患者侧设置受限、灵活性有限以及复杂的仪器交换阻碍了临床工作流程集成。这项工作提出了一种用于血管内介入治疗的紧凑型机器人系统，可以对标准血管内器械进行连续平移和旋转操作。该系统由两个交替推车组成，其气动薄膜夹具集成到旋转夹具齿轮中。其顶部装载设计允许快速更换导丝和导管等器械，而无需改变机器人设置。
- Keywords: endovascular, system, motion, experiments, compact

### 12. [通过精密加权戴明回归进行多种仪器方法比较](https://arxiv.org/abs/2607.11776v1)
- Original title: Multiple Instrument Methods Comparison by Precision weighted Deming Regression
- Authors: Douglas M Hawkins, Jessica J Kraker
- Meta: 2026-07-13 | stat.AP
- 中文摘要: 在方法比较 (MC) 研究中，使用两种或多种仪器对样本进行测试，目的是建立不同仪器读数之间的统计关系。与常规回归不同，这是变量错误问题。关系可以参数化（Deming 回归）或非参数化（Passing Bablok 或 PB 回归）拟合。在临床化学环境中，测量变异性很少是恒定的，但通常随着分析物值的增加而增加。精度加权戴明回归对这种变异性进行建模并将其纳入拟合中。 (1) 中讨论了比较两种仪器的最简单设置，并在 R 包 (2) 中实现。 PB 做出最小的分布假设。其经典的两种仪器实施最近已扩展到多种仪器 (3)。
- Abstract: In methods comparison (MC) studies, specimens are tested using two or more instruments with the objective of establishing the statistical relationship between the different instruments readings. Unlike regular regression, this is an errors in variables problem. Relationships may be fitted parametrically (Deming regression) or non-parametrically (Passing Bablok or PB regression.) In clinical chemistry settings, the m...
- Summary (fallback): 机器翻译摘要显示：在方法比较 (MC) 研究中，使用两种或多种仪器对样本进行测试，目的是建立不同仪器读数之间的统计关系。与常规回归不同，这是变量错误问题。关系可以参数化（Deming 回归）或非参数化（Passing Bablok 或 PB 回归）拟合。在临床化学环境中，测量变异性很少是恒定的，但通常随着分析物值的增加而增加。精度加权戴明回归对这种变异性进行建模并将其纳入拟合中。 (1) 中讨论了比较两种仪器的最简单设置，并在 R 包 (2) 中实现。 PB 做出最小的分布假设。其经典的两种仪器实施最近已扩展到多种仪器 (3)。
- Keywords: regression, instruments, deming, multiple, methods

### 13. [从表现力到样本复杂性：通过 C-RASP 为 Transformers 提供狭隘的指导](https://arxiv.org/abs/2607.11760v1)
- Original title: From Expressivity to Sample Complexity: Narrow Teachers for Transformers via C-RASP
- Authors: Michael Rizvi-Martel, Satwik Bhattamishra, Guillaume Rabusseau, Michael Hahn
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 对 Transformer 的理论理解对于更好地理解大型语言模型 (LLM) 的能力和局限性至关重要。有很多工作分析基于注意力的模型的表达能力。通过提出手工权重或使用计算复杂性参数，过去的大量理论工作都试图描述哪些任务属于 Transformer 模型的假设类，哪些不属于 Transformer 模型的假设类。然而，很少有人研究此类解决方案的可学习性。在这项工作中，我们朝着这一目标取得了进展。受最近损失景观分析工作的启发，我们提出了使用 Transformer 学习 C-RASP 结构的初步样本复杂性界限。
- Abstract: A theoretical understanding of Transformers is crucial to better understand the capacities and limitations of large language models (LLMs). There is much work analyzing the expressivity of attention-based models. By proposing handcrafted weights or using computational complexity arguments, a large amount of past theoretical works have sought to characterize which tasks are and which are not in the hypothesis class o...
- Summary (fallback): 机器翻译摘要显示：对 Transformer 的理论理解对于更好地理解大型语言模型 (LLM) 的能力和局限性至关重要。有很多工作分析基于注意力的模型的表达能力。通过提出手工权重或使用计算复杂性参数，过去的大量理论工作都试图描述哪些任务属于 Transformer 模型的假设类，哪些不属于 Transformer 模型的假设类。然而，很少有人研究此类解决方案的可学习性。在这项工作中，我们朝着这一目标取得了进展。受最近损失景观分析工作的启发，我们提出了使用 Transformer 学习 C-RASP 结构的初步样本复杂性界限。
- Keywords: work, complexity, transformers, models, expressivity

### 14. [离散扩散模型中从全局到因子专家组合](https://arxiv.org/abs/2607.11758v1)
- Original title: From Global to Factor-Wise Expert Composition in Discrete Diffusion Models
- Authors: Haozhe Huang, Yudong Xu, Abhijoy Mandal, Alán Aspuru-Guzik
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 离散扩散模型为解决复杂的推理任务提供了强大的框架，特别是通过组合生成，它结合了多个预先训练的专家来概括超越他们的个人训练数据。最近的理论修正引入了与时间相关的混合权重，以更好地将组合扩散动力学与预期目标对齐。然而，这些方法从根本上受到限制，因为它们在每个样本的基础上工作，整体处理每个生成的状态并忽略不同专家的潜在空间或功能专业化。在这项工作中，我们通过提出 FactorDiff - 扩散模型的按因子组合框架来解决这一限制。我们假设样本可以进一步分解为更小的因素，并提出一种采样过程，将每个因素动态路由到最相关的专家。
- Abstract: Discrete diffusion models offer a powerful framework for solving complex reasoning tasks, particularly through compositional generation, which combines multiple pre-trained experts to generalize beyond their individual training data. Recent theoretical corrections introduce time-dependent mixing weights to better align composed diffusion dynamics with the intended target. However, these methods are fundamentally lim...
- Summary (fallback): 机器翻译摘要显示：离散扩散模型为解决复杂的推理任务提供了强大的框架，特别是通过组合生成，它结合了多个预先训练的专家来概括超越他们的个人训练数据。最近的理论修正引入了与时间相关的混合权重，以更好地将组合扩散动力学与预期目标对齐。然而，这些方法从根本上受到限制，因为它们在每个样本的基础上工作，整体处理每个生成的状态并忽略不同专家的潜在空间或功能专业化。在这项工作中，我们通过提出 FactorDiff - 扩散模型的按因子组合框架来解决这一限制。我们假设样本可以进一步分解为更小的因素，并提出一种采样过程，将每个因素动态路由到最相关的专家。
- Keywords: diffusion, models, framework, spatial, global

### 15. [博弈论均衡的悖论与无政府状态的代价](https://arxiv.org/abs/2607.11752v1)
- Original title: Paradoxes of Game Theoretic Equilibria and Price of Anarchy
- Authors: Georgios Piliouras, Ian Gemp, Siqi Liu, Luke Marris
- Meta: 2026-07-13 | cs.GT
- 中文摘要: 几十年来，静态解概念（纳什均衡、相关均衡和粗略相关均衡）和无政府状态的价格 (PoA) 已经构成了算法博弈论的基石，无悔学习证明可以快速收敛到这种博弈论均衡。我们表明，将多智能体学习简化为静态平衡和黑盒遗憾分析掩盖了潜在的动态不平衡和博弈论界限。首先，内部纳什均衡缺乏$C^1$向量场信息，这意味着代理无法区分对齐激励和严格相反的激励。继承这种几何结构，最坏情况的纯纳什均衡决定了稳健的 PoA 界限，表现为拓扑不稳定的严格鞍点，并且在规范拥塞博弈中，作为几乎所有严格支配策略都支持的全局排斥器。
- Abstract: For decades, static solution concepts (Nash, Correlated, and Coarse Correlated Equilibria) and the Price of Anarchy (PoA) have formed the bedrock of algorithmic game theory, with no-regret learning proving fast convergence to such game-theoretic equilibria. We show that reducing multi-agent learning to static equilibrium and black-box regret analysis obscures underlying dynamic disequilibrium and game theoretic boun...
- Summary (fallback): 机器翻译摘要显示：几十年来，静态解概念（纳什均衡、相关均衡和粗略相关均衡）和无政府状态的价格 (PoA) 已经构成了算法博弈论的基石，无悔学习证明可以快速收敛到这种博弈论均衡。我们表明，将多智能体学习简化为静态平衡和黑盒遗憾分析掩盖了潜在的动态不平衡和博弈论界限。首先，内部纳什均衡缺乏$C^1$向量场信息，这意味着代理无法区分对齐激励和严格相反的激励。继承这种几何结构，最坏情况的纯纳什均衡决定了稳健的 PoA 界限，表现为拓扑不稳定的严格鞍点，并且在规范拥塞博弈中，作为几乎所有严格支配策略都支持的全局排斥器。
- Keywords: equilibria, correlated, learning, strictly, game

### 16. [当本地监视器错过组合危害时：诊断多代理系统中的分布式后门](https://arxiv.org/abs/2607.11751v1)
- Original title: When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems
- Authors: Yibo Hu, Ren Wang
- Meta: 2026-07-13 | cs.CR
- 中文摘要: 当部署多代理、使用工具的 LLM 系统时，一个常见的安全网是一个运行时监视器，它会自行检查每条消息、工具调用或步骤。我们证明这个网有一个根本性的漏洞。分布式后门将有害负载分散到代理之间，因此每个本地检查都会通过，而组装的对象就是攻击。监视器可以准确地定位每一步，但仍然会错过攻击。问题不在于分裂本身：分裂的片段仍然可能泄漏可疑的令牌或来源边缘。困难的情况是\emph{局部良性}。没有片段会带来危害，剩下的看起来就像普通的良性流量。我们将其形式化为 \emph{可观察性边界}：监视器仅捕获其视图可以区分的良性流量。我们证明，一旦碎片在监控视图中看起来是良性的，该视图上的探测器就无法捕获它们，无论它们有多强。
- Abstract: As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own. We show this net has a fundamental hole. A distributed backdoor splits a harmful payload across agents, so every local check passes while the assembled object is the attack. The monitor can be right on every step and still miss the attack. The problem is not splitting...
- Summary (fallback): 机器翻译摘要显示：当部署多代理、使用工具的 LLM 系统时，一个常见的安全网是一个运行时监视器，它会自行检查每条消息、工具调用或步骤。我们证明这个网有一个根本性的漏洞。分布式后门将有害负载分散到代理之间，因此每个本地检查都会通过，而组装的对象就是攻击。监视器可以准确地定位每一步，但仍然会错过攻击。问题不在于分裂本身：分裂的片段仍然可能泄漏可疑的令牌或来源边缘。困难的情况是\emph{局部良性}。没有片段会带来危害，剩下的看起来就像普通的良性流量。我们将其形式化为 \emph{可观察性边界}：监视器仅捕获其视图可以区分的良性流量。我们证明，一旦碎片在监控视图中看起来是良性的，该视图上的探测器就无法捕获它们，无论它们有多强。
- Keywords: local, monitor, attack, benign, when

### 17. [HiFi-LLP：高保真、低成本延迟预测器，对强大的 HW-NAS 充满信心](https://arxiv.org/abs/2607.11746v1)
- Original title: HiFi-LLP: High-Fidelity, Low-Cost Latency Predictors with Confidence for Robust HW-NAS
- Authors: Shambhavi Balamuthu Sampath, Behzad Shomali, Nael Fasfous, Moritz Thoma, Judeson Anthony Fernando et al.
- Meta: 2026-07-13 | cs.LG | DOI: 10.1109/SOCC66126.2025.11235466
- 中文摘要: 随着深度神经网络 (DNN) 越来越多地部署在边缘设备上，硬件 (HW) 感知优化技术（例如硬件感知压缩和硬件感知神经架构搜索 (HW-NAS)）已变得至关重要。这些方法依赖于目标硬件的真实反馈来定制 DNN 架构以实现高效部署。虽然搜索可以并行化，但由于其顺序性质，通过硬件在环 (HIL) 进行的延迟测量仍然是一个瓶颈。最近的方法使用延迟预测器来取代昂贵的 HIL 反馈，但挑战仍然存在：(1) 特定于平台的预测器通常需要数万个样本，(2) 不准确的预测可能会误导 NAS 流程。为了解决这个问题，我们引入了 HiFi-LLP，这是一种基于图注意力网络的高保真、低成本延迟预测器，并通过置信度度量进行了增强。
- Abstract: With deep neural networks (DNNs) increasingly deployed on edge devices, hardware (HW)-aware optimization techniques--such as HW-aware compression and HW-aware neural architecture search (HW-NAS)--have become essential. These methods rely on real feedback from the target hardware to tailor DNN architectures for efficient deployment. While the search can be parallelized, latency measurements via hardware-in-the-loop (...
- Summary (fallback): 机器翻译摘要显示：随着深度神经网络 (DNN) 越来越多地部署在边缘设备上，硬件 (HW) 感知优化技术（例如硬件感知压缩和硬件感知神经架构搜索 (HW-NAS)）已变得至关重要。这些方法依赖于目标硬件的真实反馈来定制 DNN 架构以实现高效部署。虽然搜索可以并行化，但由于其顺序性质，通过硬件在环 (HIL) 进行的延迟测量仍然是一个瓶颈。最近的方法使用延迟预测器来取代昂贵的 HIL 反馈，但挑战仍然存在：(1) 特定于平台的预测器通常需要数万个样本，(2) 不准确的预测可能会误导 NAS 流程。为了解决这个问题，我们引入了 HiFi-LLP，这是一种基于图注意力网络的高保真、低成本延迟预测器，并通过置信度度量进行了增强。
- Keywords: latency, predictors, hifi-llp, high-fidelity, low-cost

### 18. [多尺度生物物理波 (MBW)：概念和理论框架](https://arxiv.org/abs/2607.11745v1)
- Original title: Multiscale Biophysical Waves (MBW): Conceptual and Theoretical Framework
- Authors: Samina S. Masood, Alishpa Masood, Robert L. Jones
- Meta: 2026-07-13 | physics.bio-ph
- 中文摘要: 本文为量子、分子、细胞、组织器官、全身和其他生物物理空间之间的多层次通信建立了概念和理论框架。电磁信号的波力学描述得到发展，详细描述了波如何穿过细胞结构并与周围的生物材料发生能量相互作用。这些区域在细胞、组织、器官和神经网络内部和之间传输和接收部分相干的生物分子信号，其中共振频率发生干扰、汇聚和响应。这些过程引入了非线性和随机延迟，影响了时序、相干性和网络级动态，并且可以集成到将物理状态的数学建模与体验结果联系起来的实用框架内。
- Abstract: This paper establishes a conceptual and theoretical framework for multilevel communication between quantum, molecular, cellular, tissue-organ, whole body, and other biophysical spaces. The wave-mechanical description of electromagnetic signaling is developed, detailing how waves move through cellular structures and interact energetically with surrounding biomaterials. These regions transmit and receive partially coh...
- Summary (fallback): 机器翻译摘要显示：本文为量子、分子、细胞、组织器官、全身和其他生物物理空间之间的多层次通信建立了概念和理论框架。电磁信号的波力学描述得到发展，详细描述了波如何穿过细胞结构并与周围的生物材料发生能量相互作用。这些区域在细胞、组织、器官和神经网络内部和之间传输和接收部分相干的生物分子信号，其中共振频率发生干扰、汇聚和响应。这些过程引入了非线性和随机延迟，影响了时序、相干性和网络级动态，并且可以集成到将物理状态的数学建模与体验结果联系起来的实用框架内。
- Keywords: framework, theoretical, biophysical, waves, conceptual

### 19. [NeuralActuator：机器人动力学和外力感知的神经驱动建模](https://arxiv.org/abs/2607.11734v1)
- Original title: NeuralActuator: Neural Actuation Modeling for Robot Dynamics and External Force Perception
- Authors: Zhiyang Dou, John U. Onyemelukwe, Hangxing Zhang, Heng Zhang, Minghao Guo et al.
- Meta: 2026-07-13 | cs.RO
- 中文摘要: 可微分模拟器具有先进的策略学习和基于模型的控制，但执行器动力学仍然是模拟到真实误差的重要来源。这在低成本平台上尤其严重，其中线性电流与扭矩关系 $τ= K_tI$ 在指令目标跟踪期间由于摩擦、迟滞、间隙和热效应而变得不可靠。我们提出了 NeuralActuator，一种神经执行器模型，它联合预测（i）模拟器等效的广义作用代理，用于低成本伺服平台上的轨迹传播，（ii）具有用于无传感器力感知的接触概率门的外力，以及（iii）受监督关节的运动状况得分。我们还介绍了神经驱动数据集（NAD），该数据集是通过双臂远程操作系统收集的，该系统记录机器人状态和执行器遥测以及外力标签。
- Abstract: Differentiable simulators have advanced policy learning and model-based control, yet actuator dynamics remain an important source of sim-to-real error. This is particularly acute on low-cost platforms, where the linear current-to-torque relation $τ= K_tI$ becomes unreliable during commanded-target tracking because of friction, hysteresis, backlash, and thermal effects. We present NeuralActuator, a neural actuator mo...
- Summary (fallback): 机器翻译摘要显示：可微分模拟器具有先进的策略学习和基于模型的控制，但执行器动力学仍然是模拟到真实误差的重要来源。这在低成本平台上尤其严重，其中线性电流与扭矩关系 $τ= K_tI$ 在指令目标跟踪期间由于摩擦、迟滞、间隙和热效应而变得不可靠。我们提出了 NeuralActuator，一种神经执行器模型，它联合预测（i）模拟器等效的广义作用代理，用于低成本伺服平台上的轨迹传播，（ii）具有用于无传感器力感知的接触概率门的外力，以及（iii）受监督关节的运动状况得分。我们还介绍了神经驱动数据集（NAD），该数据集是通过双臂远程操作系统收集的，该系统记录机器人状态和执行器遥测以及外力标签。
- Keywords: force, neuralactuator, actuator, platforms, neural

### 20. [铁素体和铬尖晶石的交换拓扑和临界性：统一的蒙特卡洛分析](https://arxiv.org/abs/2607.11729v1)
- Original title: Exchange topology and criticality in ferrite and chromium spinels: a unified Monte Carlo analysis
- Authors: Keltoum Khallouq, Ayoub El Maazouzi, Kamal Boumhara, Rachid Masrour
- Meta: 2026-07-13 | cond-mat.mtrl-sci
- 中文摘要: 我们报告了两个磁性尖晶石家族的 Metropolis Monte Carlo 结果的统一分析：反铁氧体 Fe$^{3+}_{A}$[M$^{2+}$Fe$^{3+}$]$_{B}$O$_4$ (M = Co, Cu, Fe, Ni)，其中超交换耦合两个化学上不同的亚晶格，以及铬尖晶石 $A$Cr$_2X_4$ ($A$ = Zn、Cd、Hg、$X$ = S、Se) 与呼吸晶格铬酸盐 Li$M$Cr$_4$O$_8$ ($M$ = Ga、In)，其中单个 Cr$^{3+}$ 物种占据共享角的四面体网络。将这些系统的交换常数、转变温度、临界指数、磁滞和磁热响应放在共同的基础上，我们引入了两个先前未报道的减少量：铁氧体的比率 $θ_{\mathrm{CW}}/T_C$ 和铬化合物的归一化排序尺度 $t^{*}=k_BT_C/[J_1S(S+1)]$。
- Abstract: We report a unified analysis of Metropolis Monte Carlo results for two families of magnetic spinels: inverse ferrites Fe$^{3+}_{A}$[M$^{2+}$Fe$^{3+}$]$_{B}$O$_4$ (M = Co, Cu, Fe, Ni), where superexchange couples two chemically distinct sublattices, and chromium spinels $A$Cr$_2X_4$ ($A$ = Zn, Cd, Hg, $X$ = S, Se) together with the breathing-lattice chromates Li$M$Cr$_4$O$_8$ ($M$ = Ga, In), where a single Cr$^{3+}$...
- Summary (fallback): 机器翻译摘要显示：我们报告了两个磁性尖晶石家族的 Metropolis Monte Carlo 结果的统一分析：反铁氧体 Fe$^{3+}_{A}$[M$^{2+}$Fe$^{3+}$]$_{B}$O$_4$ (M = Co, Cu, Fe, Ni)，其中超交换耦合两个化学上不同的亚晶格，以及铬尖晶石 $A$Cr$_2X_4$ ($A$ = Zn、Cd、Hg、$X$ = S、Se) 与呼吸晶格铬酸盐 Li$M$Cr$_4$O$_8$ ($M$ = Ga、In)，其中单个 Cr$^{3+}$ 物种占据共享角的四面体网络。将这些系统的交换常数、转变温度、临界指数、磁滞和磁热响应放在共同的基础上，我们引入了两个先前未报道的减少量：铁氧体的比率 $θ_{\mathrm{CW}}/T_C$ 和铬化合物的归一化排序尺度 $t^{*}=k_...
- Keywords: chromium, spinels, ferrites, approx, exchange

### 21. [用于 PPVC 模块工厂灵活作业车间调度的时滞感知深度强化学习](https://arxiv.org/abs/2607.11725v1)
- Original title: Time-Lag-Aware Deep Reinforcement Learning for Flexible Job-Shop Scheduling in PPVC Module Factories
- Authors: Ziheng Zhang, Wei Zhang
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 预制预制体积建筑将大部分建筑工作转移到模块工厂，其生产车间作为灵活的作业车间运行。一个主要的并发症是决定性的：由于混凝土固化、水密性积水测试和油漆干燥而导致操作后的长时间滞后，在此期间，模块被堵塞，而其工作站保持空闲。在以官方国家预制指南为基础的基准实例中，这些滞后甚至使最佳参考完工时间平均增加了约 67%，并且在决策时忽略它们，然后修复可行性，比每个调度规则都更糟糕。
- Abstract: Prefabricated prefinished volumetric construction moves most building work into module factories, whose production floor operates as a flexible job shop. A major complication is decisive: long post-operation time-lags caused by concrete curing, watertightness ponding tests, and paint drying, during which a module is blocked while its workstation stays free. On benchmark instances grounded in an official national pre...
- Summary (fallback): 机器翻译摘要显示：预制预制体积建筑将大部分建筑工作转移到模块工厂，其生产车间作为灵活的作业车间运行。一个主要的并发症是决定性的：由于混凝土固化、水密性积水测试和油漆干燥而导致操作后的长时间滞后，在此期间，模块被堵塞，而其工作站保持空闲。在以官方国家预制指南为基础的基准实例中，这些滞后甚至使最佳参考完工时间平均增加了约 67%，并且在决策时忽略它们，然后修复可行性，比每个调度规则都更糟糕。
- Keywords: solver, module, every, deep, reinforcement

### 22. [主动的线下到线上强化学习](https://arxiv.org/abs/2607.11720v1)
- Original title: Active Offline-to-Online Reinforcement Learning
- Authors: Alper Kamil Bozkurt, Shangtong Zhang, Yuichi Motai
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 背景：离线强化学习（RL）可以从先前收集的大型数据集中训练有效的策略，并随后通过有限的在线交互进行改进。这种离线到在线强化学习 (O2O-RL) 范式在互动成本高昂或存在潜在危险的非平稳领域特别有前景。标准的O2O-RL管道离线训练多个候选策略，使用离线策略或在线评估对其进行评估，然后部署和微调具有最高估计值的策略。然而，与离线预训练一样，微调性能对算法和超参数的选择高度敏感，因此采用单一策略存在风险。目标：我们研究 O2O-RL 设置中有限交互预算下的主动政策选择以进行微调。据我们所知，这是解决这个问题的第一个工作。
- Abstract: Background: Offline reinforcement learning (RL) enables effective policies to be trained from large, previously collected datasets and subsequently improved through limited online interaction. This offline-to-online RL (O2O-RL) paradigm is particularly promising in nonstationary domains where interaction is costly or potentially hazardous. Standard O2O-RL pipelines train multiple candidate policies offline, evaluate...
- Summary (fallback): 机器翻译摘要显示：背景：离线强化学习（RL）可以从先前收集的大型数据集中训练有效的策略，并随后通过有限的在线交互进行改进。这种离线到在线强化学习 (O2O-RL) 范式在互动成本高昂或存在潜在危险的非平稳领域特别有前景。标准的O2O-RL管道离线训练多个候选策略，使用离线策略或在线评估对其进行评估，然后部署和微调具有最高估计值的策略。然而，与离线预训练一样，微调性能对算法和超参数的选择高度敏感，因此采用单一策略存在风险。目标：我们研究 O2O-RL 设置中有限交互预算下的主动政策选择以进行微调。据我们所知，这是解决这个问题的第一个工作。
- Keywords: policies, online, policy, interaction, fine-tuning

### 23. [CatRetriever：生成催化剂发现中用于批量检索的对比表示学习](https://arxiv.org/abs/2607.11712v1)
- Original title: CatRetriever: Contrastive Representation Learning for Slab-to-Bulk Retrieval in Generative Catalyst Discovery
- Authors: Jungho Oh, Woosung Kim, Dong Hyeon Mok, Jonggeol Na, Seoin Back
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 逆向设计是一种新兴的数据驱动范例，用于有效地导航广阔的化学空间，发现具有目标特性的新材料，在多相催化的背景下，表面生成模型最近通过直接生成催化剂表面吸附物结构来推进这一目标。然而，这些模型通常在板层水平上运行，并且不提供相应的母体结构，因此很难评估与体相关的特性，例如形成能、表面能、晶体对称性和可合成性。在这里，我们将这种缺失的板片到块体连接作为检索问题来解决，并引入 CatRetriever，这是一种对比表示学习模型，可在共享潜在空间中对齐板片和块状晶体表示。
- Abstract: Inverse design is an emerging data-driven paradigm for efficiently navigating vast chemical spaces to discover new materials with targeted properties, and in the context of heterogeneous catalysis, surface generative models have recently advanced this goal by directly generating catalyst surface-adsorbate structures. However, these models typically operate at the slab level and do not provide the corresponding paren...
- Summary (fallback): 机器翻译摘要显示：逆向设计是一种新兴的数据驱动范例，用于有效地导航广阔的化学空间，发现具有目标特性的新材料，在多相催化的背景下，表面生成模型最近通过直接生成催化剂表面吸附物结构来推进这一目标。然而，这些模型通常在板层水平上运行，并且不提供相应的母体结构，因此很难评估与体相关的特性，例如形成能、表面能、晶体对称性和可合成性。在这里，我们将这种缺失的板片到块体连接作为检索问题来解决，并引入 CatRetriever，这是一种对比表示学习模型，可在共享潜在空间中对齐板片和块状晶体表示。
- Keywords: bulk, energy, catretriever, generative, catalyst

### 24. [$\mathtt{Q^2SAR}$：通过量子多核学习克服药物发现中的经典瓶颈](https://arxiv.org/abs/2607.11701v1)
- Original title: $\mathtt{Q^2SAR}$: overcoming classical bottlenecks in drug discovery via quantum multiple kernel learning
- Authors: Mariano Caruso, Daniel Ruiz, Alejandro Giraldo, Guido Bellomo
- Meta: 2026-07-13 | quant-ph
- 中文摘要: 定量构效关系 ($\mathtt{QSAR}$) 建模是早期药物发现的基础计算方法，在很大程度上依赖于预测化合物毒性、生物利用度和治疗潜力。然而，经典方法通常难以有效地绘制分子数据中固有的高度复杂、非线性和高维相互作用，从而导致预测准确性降低和代价高昂的后期临床失败。在本文中，我们提出了一种量子多核学习 ($\mathtt{QMKL}$) 框架，称为下一代 $\mathtt{Q^2SAR}$，它利用量子支持向量机 ($\mathtt{QSVMs}$) 来克服这些经典限制。通过将分子描述符编码到指数级大的量子希尔伯特空间中，我们的方法大大增强了非线性建模的表达能力。
- Abstract: Quantitative Structure-Activity Relationship ($\mathtt{QSAR}$) modeling is a foundational computational methodology in early-stage drug discovery, heavily relied upon for predicting compound toxicity, bioavailability, and therapeutic potential. However, classical methods often struggle to effectively map the highly complex, non-linear, and high-dimensional interactions inherent in molecular data, leading to reduced...
- Summary (fallback): 机器翻译摘要显示：定量构效关系 ($\mathtt{QSAR}$) 建模是早期药物发现的基础计算方法，在很大程度上依赖于预测化合物毒性、生物利用度和治疗潜力。然而，经典方法通常难以有效地绘制分子数据中固有的高度复杂、非线性和高维相互作用，从而导致预测准确性降低和代价高昂的后期临床失败。在本文中，我们提出了一种量子多核学习 ($\mathtt{QMKL}$) 框架，称为下一代 $\mathtt{Q^2SAR}$，它利用量子支持向量机 ($\mathtt{QSVMs}$) 来克服这些经典限制。通过将分子描述符编码到指数级大的量子希尔伯特空间中，我们的方法大大增强了非线性建模的表达能力。
- Keywords: mathtt, quantum, classical, drug, discovery

### 25. [靶向 DNA 甲基化：新范式和基因选择性工具的出现](https://arxiv.org/abs/2607.11697v1)
- Original title: Targeting DNA Methylation: New Paradigms and the Advent of Gene-Selective Tools
- Authors: Julie Gilbert, Francesco Calzaferri
- Meta: 2026-07-13 | q-bio.SC
- 中文摘要: DNA 甲基化可以作为有毒烷基化反应，被化疗药物利用来诱导癌细胞死亡。然而，精细调节的 DNA 甲基化在细胞生理学中发挥着重要作用，特别是在基因表达的表观遗传调控中。曾经被认为仅作为基因转录的抑制因子，其功能作用已被阐明为基因组位点特异性并与其他表观遗传因子密切相关。继阿扎胞苷和地西他滨等 DNA 甲基转移酶抑制剂用于治疗血液恶性肿瘤的临床批准后，人们投入了大量精力来开发调节表观遗传 DNA 甲基化的药理学工具。然而，这些药物缺乏基因选择性限制了它们的治疗功效并增加了脱靶毒性。
- Abstract: DNA methylation can function as a toxic alkylation reaction exploited by chemotherapeutic agents to induce cancer cell death. However, finely tuned DNA methylation plays a fundamental role in cellular physiology, particularly in the epigenetic regulation of gene expression. Once thought to act solely as a repressor of gene transcription, its functional role has since been elucidated as genomic locus-specific and dee...
- Summary (fallback): 机器翻译摘要显示：DNA 甲基化可以作为有毒烷基化反应，被化疗药物利用来诱导癌细胞死亡。然而，精细调节的 DNA 甲基化在细胞生理学中发挥着重要作用，特别是在基因表达的表观遗传调控中。曾经被认为仅作为基因转录的抑制因子，其功能作用已被阐明为基因组位点特异性并与其他表观遗传因子密切相关。继阿扎胞苷和地西他滨等 DNA 甲基转移酶抑制剂用于治疗血液恶性肿瘤的临床批准后，人们投入了大量精力来开发调节表观遗传 DNA 甲基化的药理学工具。然而，这些药物缺乏基因选择性限制了它们的治疗功效并增加了脱靶毒性。
- Keywords: methylation, epigenetic, tools, gene, agents

### 26. [使用仅摄像头视觉里程计的自主地面车辆的自我修复视觉恢复](https://arxiv.org/abs/2607.11686v1)
- Original title: Self-Healing Visual Recovery for Autonomous Ground Vehicles Using Camera-Only Visual Odometry
- Authors: Jakob Solberg Berntzen, Safia Fatima, Leon Moonen
- Meta: 2026-07-13 | cs.RO
- 中文摘要: 低成本的无人地面车辆通常用于仓库、检查走廊和农场等室内场所，在这些地方，涂漆的地板线引导机器人。巡线很有用，因为它只需要一个摄像头和很少的计算能力，但当线路被阻挡或急转弯并超出视野时，它可能会失败。传感器丰富的平台通过硬件冗余（LiDAR、GPS、多个摄像头）来容忍这种情况，但仅摄像头的系统必须在运行时恢复，而无需额外的基础设施。本文提出了一种轻量级的两阶段恢复方法，无需 LiDAR、GPS 或 GPU 即可恢复引导跟踪。当线路丢失时，机器人首先转向原位，同时缓慢放松其颜色检查并等待多个帧的确认（第一阶段）。
- Abstract: Low-cost unmanned ground vehicles are often used in indoor places like warehouses, inspection corridors, and farm rows, where painted floor lines guide the robot. Line following is useful because it only needs one camera and little computing power, but it can fail when the line is blocked or turns sharply and goes out of view. Sensor-rich platforms tolerate this through hardware redundancy (LiDAR, GPS, multiple came...
- Summary (fallback): 机器翻译摘要显示：低成本的无人地面车辆通常用于仓库、检查走廊和农场等室内场所，在这些地方，涂漆的地板线引导机器人。巡线很有用，因为它只需要一个摄像头和很少的计算能力，但当线路被阻挡或急转弯并超出视野时，它可能会失败。传感器丰富的平台通过硬件冗余（LiDAR、GPS、多个摄像头）来容忍这种情况，但仅摄像头的系统必须在运行时恢复，而无需额外的基础设施。本文提出了一种轻量级的两阶段恢复方法，无需 LiDAR、GPS 或 GPU 即可恢复引导跟踪。当线路丢失时，机器人首先转向原位，同时缓慢放松其颜色检查并等待多个帧的确认（第一阶段）。
- Keywords: visual, line, recovery, camera-only, odometry

### 27. [多样化多项 Logit 上下文强盗](https://arxiv.org/abs/2607.11684v1)
- Original title: Diversified Multinomial Logit Contextual Bandits
- Authors: Heesang Ann, Taehyun Hwang, Min-hwan Oh
- Meta: 2026-07-13 | stat.ML
- 中文摘要: 现有的上下文多项式 Logit (MNL) bandits 模型相关性驱动的选择，但忽略了分类内多样性的潜在好处，而子模块/组合 bandits 编码了奖励的多样性，但缺乏结构化的选择概率。我们用 $\textit{多样化多项式 logit}$ (DMNL) 上下文老虎机来弥补这一差距，它通过一般的子模多样性函数来增强 MNL 选择概率，从而在单个模型中形式化相关性-多样性权衡。纳入多样性使得精确的 MNL 分类优化变得棘手。我们提出了一种基于 UCB 的 $\textit{white-box}$ 算法，$\texttt{OFU-DMNL}$，该算法通过最大化乐观边际收益逐项构建分类，避免黑盒优化预言。
- Abstract: Existing contextual multinomial logit (MNL) bandits model relevance-driven choice but ignore the potential benefits of within-assortment diversity, while submodular/combinatorial bandits encode diversity in rewards but lack structured choice probabilities. We bridge this gap with the $\textit{diversified multinomial logit}$ (DMNL) contextual bandit, which augments MNL choice probabilities with a generally submodular...
- Summary (fallback): 机器翻译摘要显示：现有的上下文多项式 Logit (MNL) bandits 模型相关性驱动的选择，但忽略了分类内多样性的潜在好处，而子模块/组合 bandits 编码了奖励的多样性，但缺乏结构化的选择概率。我们用 $\textit{多样化多项式 logit}$ (DMNL) 上下文老虎机来弥补这一差距，它通过一般的子模多样性函数来增强 MNL 选择概率，从而在单个模型中形式化相关性-多样性权衡。纳入多样性使得精确的 MNL 分类优化变得棘手。我们提出了一种基于 UCB 的 $\textit{white-box}$ 算法，$\texttt{OFU-DMNL}$，该算法通过最大化乐观边际收益逐项构建分类，避免黑盒优化预言。
- Keywords: bandits, diversity, multinomial, logit, contextual

### 28. [用于复杂几何形状流体动力学预测的多尺度特征增强图神经网络](https://arxiv.org/abs/2607.11672v1)
- Original title: A multi-scale feature enhanced graph neural network for fluid dynamics prediction in complex geometries
- Authors: Li Xiao, Tianyu Li, Yiye Zou, Mingjie Zhang, Xiaogangd Deng
- Meta: 2026-07-13 | cs.LG
- 中文摘要: 车辆和航空航天工程等领域的工业设计通常依赖于大规模数值模拟来评估流体动力学性能，这可能会产生大量的计算成本。深度神经网络在提高模拟效率方面表现出了希望，尤其是图神经网络（GNN），由于其处理非结构化数据的灵活性而展现出巨大的潜力。然而，GNN 在处理涉及复杂几何形状和大规模网格的任务时面临挑战。在本文中，我们提出了多尺度特征增强图神经网络（ME-GNN）来应对这些挑战。 ME-GNN 采用具有两步消息传递机制的图神经网络来有效捕获详细的局部特征。此外，它将注意力 U-Net 与均匀网格离散化相结合，从而能够提取精细和粗略的特征。
- Abstract: Industrial design in fields such as vehicle and aerospace engineering often relies on large-scale numerical simulations to evaluate fluid dynamics performance, which can incur substantial computational costs. Deep neural networks have shown promise in improving simulation efficiency, especially graph neural networks (GNNs), which demonstrate great potential due to their flexibility with unstructured data. However, G...
- Summary (fallback): 机器翻译摘要显示：车辆和航空航天工程等领域的工业设计通常依赖于大规模数值模拟来评估流体动力学性能，这可能会产生大量的计算成本。深度神经网络在提高模拟效率方面表现出了希望，尤其是图神经网络（GNN），由于其处理非结构化数据的灵活性而展现出巨大的潜力。然而，GNN 在处理涉及复杂几何形状和大规模网格的任务时面临挑战。在本文中，我们提出了多尺度特征增强图神经网络（ME-GNN）来应对这些挑战。 ME-GNN 采用具有两步消息传递机制的图神经网络来有效捕获详细的局部特征。此外，它将注意力 U-Net 与均匀网格离散化相结合，从而能够提取精细和粗略的特征。
- Keywords: neural, graph, network, me-gnn, features

### 29. [如何驯服 Grokking：表示几何作为控制信号](https://arxiv.org/abs/2607.11666v1)
- Original title: How to Tame Grokking: Representation Geometry as a Control Signal
- Authors: Maksim A Kazanskii
- Meta: 2026-07-13 | cs.LG
- 中文摘要: Grokking 是一种神经网络最初记忆训练数据，经过长时间优化才表现出很强的泛化能力的现象。尽管最近进行了广泛的研究，但影响摸索出现和时间的因素仍然不完全清楚。我们研究了表示几何和延迟泛化之间的关系。我们发现，在所有评估的设置中，维度崩溃始终先于摸索的开始。受这些观察的启发，我们引入了几何维数正则化（GeomDR），这是一种简单的谱正则化器，可以在训练期间修改隐藏表示的有效维数。
- Abstract: Grokking is a phenomenon in which neural networks initially memorize training data and only later exhibit strong generalization after prolonged optimization. Despite extensive recent study, the factors influencing the emergence and timing of grokking remain incompletely understood. We investigate the relationship between representation geometry and delayed generalization. We find that dimensionality collapse consist...
- Summary (fallback): 机器翻译摘要显示：Grokking 是一种神经网络最初记忆训练数据，经过长时间优化才表现出很强的泛化能力的现象。尽管最近进行了广泛的研究，但影响摸索出现和时间的因素仍然不完全清楚。我们研究了表示几何和延迟泛化之间的关系。我们发现，在所有评估的设置中，维度崩溃始终先于摸索的开始。受这些观察的启发，我们引入了几何维数正则化（GeomDR），这是一种简单的谱正则化器，可以在训练期间修改隐藏表示的有效维数。
- Keywords: grokking, generalization, dimensionality, representation, geometry

### 30. [无插补变压器学习可实现稳健的阿尔茨海默病预测和跨异质临床队列的校准不确定性量化](https://arxiv.org/abs/2607.11656v1)
- Original title: Imputation-free transformer learning enables robust Alzheimer's disease prediction and calibrated uncertainty quantification across heterogeneous clinical cohorts
- Authors: Christelle Schneuwly Diaz, Narmina Baghirova, Duy-Thanh Vu, Duy-Cat Can, Gilles Allali et al.
- Meta: 2026-07-13 | q-bio.NC
- 中文摘要: 现实世界临床数据的不完整性和异质性阻碍了阿尔茨海默病的准确诊断分类和疾病严重程度预测。如果不加以解决，这些障碍将阻碍可靠的疾病建模并阻碍有效的临床评估。传统的插补策略会引入系统偏差，扭曲特征间关系，并产生过度自信的预测，这些限制在诊断环境中尤其严重。在这里，我们提出了 NITROGEN，一种无插补转换器，通过屏蔽和样本间注意力联合建模患者内部特征依赖性和患者之间的关系结构，从而直接从部分观察的记录中实现稳健的多模态学习。我们在 ADNI（N=7858 次扫描）上训练 NITROGEN，并在两个独立队列上进行评估：OASIS-3（N=2675 次扫描）和 AIBL（N=1286 次扫描）。
- Abstract: Accurate diagnostic classification and disease-severity prediction for Alzheimer's disease are hampered by the incompleteness and heterogeneity of real-world clinical data. Left unaddressed, these barriers prevent reliable disease modelling and hinder effective clinical evaluation. Conventional imputation strategies introduce systematic bias, distort inter-feature relationships, and yield overconfident predictions,...
- Summary (fallback): 机器翻译摘要显示：现实世界临床数据的不完整性和异质性阻碍了阿尔茨海默病的准确诊断分类和疾病严重程度预测。如果不加以解决，这些障碍将阻碍可靠的疾病建模并阻碍有效的临床评估。传统的插补策略会引入系统偏差，扭曲特征间关系，并产生过度自信的预测，这些限制在诊断环境中尤其严重。在这里，我们提出了 NITROGEN，一种无插补转换器，通过屏蔽和样本间注意力联合建模患者内部特征依赖性和患者之间的关系结构，从而直接从部分观察的记录中实现稳健的多模态学习。我们在 ADNI（N=7858 次扫描）上训练 NITROGEN，并在两个独立队列上进行评估：OASIS-3（N=2675 次扫描）和 AIBL（N=1286 次扫描）。
- Keywords: uncertainty, clinical, cohorts, diagnostic, imputation-free

## biorxiv

### 1. [知情的数据独立采集能够以单细胞分辨率对细胞命运决定中的关键调节蛋白进行有针对性的定量](https://www.biorxiv.org/content/10.1101/2025.05.30.656945v3)
- Original title: Informed Data-Independent Acquisition Enables Targeted Quantification of Key Regulatory Proteins in Cell Fate Decisions at Single-Cell Resolution
- Authors: Woessmann, J., Petrosius, V., Schovsbo, S., Furtwaengler, B., Arrey, T. N. et al.
- Meta: 2026-07-14 | systems biology | DOI: 10.1101/2025.05.30.656945
- 中文摘要: 尽管转录因子 (TF) 等低丰度调节蛋白在细胞状态转变中发挥着核心作用，但它们在很大程度上仍然无法在单细胞中直接定量。尽管单细胞蛋白质组学质谱 (scp-MS) 能够进行广泛的蛋白质组分析，但目前的方法通常缺乏在蛋白质水平上稳健量化这些调节因子所需的灵敏度。在这里，我们提出了知情数据独立采集（iDIA），这是一种跨仪器 MS 采集框架，将敏感的靶向测量与同一细胞的全局蛋白质组分析相结合。因此，iDIA 显着提高了预定义调节蛋白的灵敏度，同时保留了全局蛋白质组覆盖范围。
- Abstract: Low-abundance regulatory proteins, including transcription factors (TFs), remain largely inaccessible to direct quantification in single cells despite their central roles in cellular state transitions. Although single-cell proteomics by mass spectrometry (scp-MS) enables broad proteome profiling, current approaches often lack the sensitivity required to quantify these regulators at the protein level robustly. Here,...
- Summary (fallback): 机器翻译摘要显示：尽管转录因子 (TF) 等低丰度调节蛋白在细胞状态转变中发挥着核心作用，但它们在很大程度上仍然无法在单细胞中直接定量。尽管单细胞蛋白质组学质谱 (scp-MS) 能够进行广泛的蛋白质组分析，但目前的方法通常缺乏在蛋白质水平上稳健量化这些调节因子所需的灵敏度。在这里，我们提出了知情数据独立采集（iDIA），这是一种跨仪器 MS 采集框架，将敏感的靶向测量与同一细胞的全局蛋白质组分析相结合。因此，iDIA 显着提高了预定义调节蛋白的灵敏度，同时保留了全局蛋白质组覆盖范围。
- Keywords: regulatory, proteome, idia, acquisition, proteins

### 2. [沉默燕子中两性二态的前沿锯齿是随着精子竞争而进化的](https://www.biorxiv.org/content/10.1101/2023.08.12.552953v3)
- Original title: Sexually dimorphic leading-edge serrations evolved with sperm competition in silent swallows
- Authors: Hasegawa, M.
- Meta: 2026-07-14 | evolutionary biology | DOI: 10.1101/2023.08.12.552953
- 中文摘要: 前缘锯齿是特殊的羽毛结构，可减轻猫头鹰在觅食飞行期间的噪音，并已被广泛研究并应用于人造降噪结构。类似的结构也出现在燕子身上，尽管这些物种的锯齿的生态功能仍不清楚。我对水蛭（鸟纲：水蛭亚科）进行了宏观进化分析，研究它们的进化与生态环境的关系，其中前沿锯齿已经进化了多次。我发现沉默的水燕有更高的概率拥有前缘锯齿，这表明燕子的前缘锯齿具有与猫头鹰一样的声学功能。
- Abstract: Leading-edge serrations are specialized feather structures, mitigating acoustic noise during foraging flight in owls, and have been extensively studied and applied to man-made noise-reducing structures. Similar structures occur in swallows, although the ecological functions of the serrations in these species remain unclear. I conducted macroevolutionary analyses of hirundines (Aves: Hirundininae), in which leading-e...
- Summary (fallback): 机器翻译摘要显示：前缘锯齿是特殊的羽毛结构，可减轻猫头鹰在觅食飞行期间的噪音，并已被广泛研究并应用于人造降噪结构。类似的结构也出现在燕子身上，尽管这些物种的锯齿的生态功能仍不清楚。我对水蛭（鸟纲：水蛭亚科）进行了宏观进化分析，研究它们的进化与生态环境的关系，其中前沿锯齿已经进化了多次。我发现沉默的水燕有更高的概率拥有前缘锯齿，这表明燕子的前缘锯齿具有与猫头鹰一样的声学功能。
- Keywords: serrations, leading-edge, hirundines, sperm, competition

### 3. [使用 ESM3 推进打结蛋白质设计：引导生成和拓扑洞察](https://www.biorxiv.org/content/10.64898/2026.05.07.723606v2)
- Original title: Advancing Knotted Protein Design with ESM3: Guided Generation and Topological Insights
- Authors: Marsalkova, E., Simecek, P.
- Meta: 2026-07-14 | bioengineering | DOI: 10.64898/2026.05.07.723606
- 中文摘要: 多模式蛋白质语言模型已经改变了蛋白质设计，但它们捕获复杂拓扑特征的能力仍然知之甚少。我们使用打结的蛋白质（一种罕见的结构，其中主干形成一个不平凡的拓扑结）作为测试用例，以使用生成蛋白质语言模型 ESM3 来探测这种能力。 ESM3 的引导生成以 89% 的成功率（95% CI：81-94%）生成打结蛋白，而基于非引导扩散的方法的成功率约为 0.5%。结拓扑对于序列扰动非常稳健：在结断裂之前，平均 84% 的蛋白质序列必须被改变，并且损失遵循尖锐的阈值而不是逐渐降解。引人注目的是，结构漂移在拓扑破坏之前就已经积累，这表明拓扑比特定的三维排列更稳健。
- Abstract: Multimodal protein language models have transformed protein design, yet their capacity to capture complex topological features remains poorly understood. We use knotted proteins, rare structures in which the backbone forms a nontrivial topological knot, as a test case to probe this capacity using ESM3, a generative protein language model. ESM3's guided generation produces knotted proteins with an 89% success rate (9...
- Summary (fallback): 机器翻译摘要显示：多模式蛋白质语言模型已经改变了蛋白质设计，但它们捕获复杂拓扑特征的能力仍然知之甚少。我们使用打结的蛋白质（一种罕见的结构，其中主干形成一个不平凡的拓扑结）作为测试用例，以使用生成蛋白质语言模型 ESM3 来探测这种能力。 ESM3 的引导生成以 89% 的成功率（95% CI：81-94%）生成打结蛋白，而基于非引导扩散的方法的成功率约为 0.5%。结拓扑对于序列扰动非常稳健：在结断裂之前，平均 84% 的蛋白质序列必须被改变，并且损失遵循尖锐的阈值而不是逐渐降解。引人注目的是，结构漂移在拓扑破坏之前就已经积累，这表明拓扑比特定的三维排列更稳健。
- Keywords: protein, knotted, topological, proteins, esm3

### 4. [改进的 3D 径向叶序轨迹，实现读出方向的均匀密度分布和顺序分箱](https://www.biorxiv.org/content/10.64898/2026.07.06.736720v2)
- Original title: Improved 3D Radial Phyllotaxis Trajectories for Uniform Density Distribution of Readout Directions and Sequential Binning
- Authors: Leidi, M., Delitroz, J., Peper, E., Jia, Y., Barranco, J. et al.
- Meta: 2026-07-14 | bioinformatics | DOI: 10.64898/2026.07.06.736720
- 中文摘要: 目的：开发 3D 径向螺旋叶序轨迹，提供读出方向的均匀密度分布并支持回顾性顺序分箱，从而减少振铃伪影并提高图像质量。方法：UPhy轨迹重新定义极角以实现读出方向的均匀密度分布。 FlexiPhy 通过随机排列进一步解耦交错的方位角和极性排序，从而提高顺序分箱的鲁棒性。使用 3T MRI 扫描仪上的两个梯度回波序列对 10 名健康志愿者的体内评估轨迹进行了体内评估。使用结构相似性和相对 L2 误差度量将顺序时间重建与参考重建进行比较。结果：UPhy 通过分析证明了读出方向的均匀密度分布。
- Abstract: Purpose: To develop 3D radial spiral phyllotaxis trajectories that provide a uniform density distribution of readout directions and support retrospec- tive sequential binning, thereby reducing ringing artifacts and improving image quality. Methods: UPhy trajectory redefines the polar angle to achieve uni- form density distribution of readout directions. FlexiPhy further decouples the azimuthal and polar ordering of...
- Summary (fallback): 机器翻译摘要显示：目的：开发 3D 径向螺旋叶序轨迹，提供读出方向的均匀密度分布并支持回顾性顺序分箱，从而减少振铃伪影并提高图像质量。方法：UPhy轨迹重新定义极角以实现读出方向的均匀密度分布。 FlexiPhy 通过随机排列进一步解耦交错的方位角和极性排序，从而提高顺序分箱的鲁棒性。使用 3T MRI 扫描仪上的两个梯度回波序列对 10 名健康志愿者的体内评估轨迹进行了体内评估。使用结构相似性和相对 L2 误差度量将顺序时间重建与参考重建进行比较。结果：UPhy 通过分析证明了读出方向的均匀密度分布。
- Keywords: binning, sequential, trajectories, density, readout

### 5. [通过人类胼胝体的认知功能的功能投射](https://www.biorxiv.org/content/10.64898/2026.06.16.732587v2)
- Original title: Functional projection of cognitive functions through the human corpus callosum
- Authors: Bonandrini, R., Tettamanti, M., Luzzatti, C.
- Meta: 2026-07-14 | neuroscience | DOI: 10.64898/2026.06.16.732587
- 中文摘要: 自该领域研究开始以来，如何将人脑由两个不对称的半部组成的解剖学观察结果与精神的惊人统一相协调，一直是神经科学家面临的一个难题。胼胝体的白质连合纤维构成了解决这种解剖二元性功能的关键解剖基质。然而，迄今为止，胼胝体在不同认知领域的功能参与程度仍然是一个未知领域。在这里，我们提出了胼胝体参与一组认知功能的概率特征。特别是，我们通过将 Disconnectome 方法应用于健康参与者的参考样本，同时使用哈佛-牛津模板中包含的宏观解剖皮质区域作为种子来估计结构胼胝体连接。
- Abstract: Reconciling the anatomical observation that the human brain comprises two asymmetrical halves with the phenomenal unity of the mind is a puzzle that has challenged neuroscientists since the dawn of research in the field. White-matter commissural fibres of the corpus callosum constitute a critical anatomical substrate for the functional resolution of this anatomical duality. However, the extent of the functional invo...
- Summary (fallback): 机器翻译摘要显示：自该领域研究开始以来，如何将人脑由两个不对称的半部组成的解剖学观察结果与精神的惊人统一相协调，一直是神经科学家面临的一个难题。胼胝体的白质连合纤维构成了解决这种解剖二元性功能的关键解剖基质。然而，迄今为止，胼胝体在不同认知领域的功能参与程度仍然是一个未知领域。在这里，我们提出了胼胝体参与一组认知功能的概率特征。特别是，我们通过将 Disconnectome 方法应用于健康参与者的参考样本，同时使用哈佛-牛津模板中包含的宏观解剖皮质区域作为种子来估计结构胼胝体连接。
- Keywords: callosum, involvement, functional, functions, callosal

### 6. [海洋拟杆菌中β-葡聚糖的利用是由跨膜单组分系统控制的](https://www.biorxiv.org/content/10.64898/2026.01.10.698779v3)
- Original title: β-glucan utilization in marine Bacteroidota is controlled by a membrane-spanning one-component system
- Authors: Bartosik, D., Zuehlke, M. K., Welsch, N., THOMAS, F., Schweder, T.
- Meta: 2026-07-14 | microbiology | DOI: 10.64898/2026.01.10.698779
- 中文摘要: 海洋系统中最普遍和生物利用度最高的聚糖之一是{β}-葡聚糖昆布多糖。拟杆菌门的成员特别适合降解这种多糖和其他多糖。尽管最近的研究对该门对海洋聚糖的酶促分解提供了详细的见解，但控制其利用的调节机制在很大程度上仍未被探索。在这里，我们描述了一种调节海洋拟杆菌中昆布多糖利用的跨膜单组分系统。我们分析了海洋模型细菌 Formosa agariphila KMM3901T 中的这种 {β}-葡聚糖利用调节剂 (BguR) 类型。删除调节基因会消除昆布多糖的生长，而野生型则对相关基因组基因簇进行超过 80 倍的诱导，表明调节因子作为昆布多糖利用的转录激活剂的作用。
- Abstract: One of the most prevalent and bioavailable glycans in marine systems is the {beta}-glucan laminarin. Members of the phylum Bacteroidota are particularly well adapted to degrade this and other polysaccharides. Although recent research has provided detailed insights into the enzymatic breakdown of marine glycans by this phylum, the regulatory mechanisms that govern their utilization remain largely unexplored. Here, we...
- Summary (fallback): 机器翻译摘要显示：海洋系统中最普遍和生物利用度最高的聚糖之一是{β}-葡聚糖昆布多糖。拟杆菌门的成员特别适合降解这种多糖和其他多糖。尽管最近的研究对该门对海洋聚糖的酶促分解提供了详细的见解，但控制其利用的调节机制在很大程度上仍未被探索。在这里，我们描述了一种调节海洋拟杆菌中昆布多糖利用的跨膜单组分系统。我们分析了海洋模型细菌 Formosa agariphila KMM3901T 中的这种 {β}-葡聚糖利用调节剂 (BguR) 类型。删除调节基因会消除昆布多糖的生长，而野生型则对相关基因组基因簇进行超过 80 倍的诱导，表明调节因子作为昆布多糖利用的转录激活剂的作用。
- Keywords: marine, utilization, laminarin, bacteroidota, regulator

### 7. [衰老细胞更容易受到还原应激诱导的细胞死亡的影响：对衰老研究的影响。](https://www.biorxiv.org/content/10.64898/2026.07.10.737740v1)
- Original title: Senescent cells are more susceptible to reductive stress-induced cell death: implications for senolytic research.
- Authors: Belhac, V., Stolzing, A., Martin, N.
- Meta: 2026-07-14 | cell biology | DOI: 10.64898/2026.07.10.737740
- 中文摘要: 增殖细胞可以进入不可逆的细胞周期停滞状态，称为细胞衰老。衰老细胞的积累会导致机体衰老和与年龄相关的病理。因此，出现了选择性消除衰老细胞的治疗策略（senolytics）。我们之前的工作表明，衰老的小鼠成肌细胞比增殖细胞更容易受到还原应激诱导的细胞死亡的影响。在这里，我们在人类 LHCN-M2 成肌细胞中复制了这些发现，证明了与细胞死亡的双相剂量反应关系，其中低浓度与增殖和衰老细胞的细胞死亡减少相关，而较高浓度选择性诱导衰老细胞的细胞毒性。
- Abstract: Proliferating cells can enter an irreversible state of cell-cycle arrest known as cellular senescence. The accumulation of senescent cells contributes to organismal ageing and age-related pathologies. Consequently, therapeutic strategies have emerged to selectively eliminate senescent cells (senolytics). Our previous work suggested that senescent mouse myoblasts are more susceptible to reductive stress-induced cell...
- Summary (fallback): 机器翻译摘要显示：增殖细胞可以进入不可逆的细胞周期停滞状态，称为细胞衰老。衰老细胞的积累会导致机体衰老和与年龄相关的病理。因此，出现了选择性消除衰老细胞的治疗策略（senolytics）。我们之前的工作表明，衰老的小鼠成肌细胞比增殖细胞更容易受到还原应激诱导的细胞死亡的影响。在这里，我们在人类 LHCN-M2 成肌细胞中复制了这些发现，证明了与细胞死亡的双相剂量反应关系，其中低浓度与增殖和衰老细胞的细胞死亡减少相关，而较高浓度选择性诱导衰老细胞的细胞毒性。
- Keywords: cells, senescent, cell, death, reductive

### 8. [组成型巨胞饮作用维持衰老细胞的炎症表型](https://www.biorxiv.org/content/10.64898/2026.07.12.738086v1)
- Original title: Constitutive macropinocytosis sustains the inflammatory phenotype of senescent cells
- Authors: Kozik, K., Razali, N., Kono, K.
- Meta: 2026-07-14 | cell biology | DOI: 10.64898/2026.07.12.738086
- 中文摘要: 细胞衰老是一种稳定的细胞周期停滞，其特征是广泛的代谢重塑和促炎分泌组，称为衰老相关分泌表型（SASP）。虽然短暂的 SASP 支持组织修复和伤口愈合，但其持续激活会导致慢性炎症和与年龄相关的病理。尽管 SASP 的调控很复杂，但囊泡运输和内吞途径对其控制的贡献仍不清楚。在这里，我们将巨胞饮作用确定为多种细胞系和衰老亚型中的一种组成型活跃的内吞途径。通过药理学和遗传扰动，我们证明 PAK1 是衰老细胞巨胞饮作用的关键调节因子。此外，PAK1 依赖性巨胞饮作用通过 TGF{beta} 信号传导调节炎症 SASP 因子（例如 IL6 和 CCL2）的产生。
- Abstract: Cellular senescence is a stable cell cycle arrest characterized by extensive metabolic remodeling and a proinflammatory secretome known as senescence-associated secretory phenotype (SASP). While transient SASP supports tissue repair and wound healing, its persistent activation drives chronic inflammation and age-related pathology. Despite the complex regulation of SASP, the contribution of vesicle trafficking and en...
- Summary (fallback): 机器翻译摘要显示：细胞衰老是一种稳定的细胞周期停滞，其特征是广泛的代谢重塑和促炎分泌组，称为衰老相关分泌表型（SASP）。虽然短暂的 SASP 支持组织修复和伤口愈合，但其持续激活会导致慢性炎症和与年龄相关的病理。尽管 SASP 的调控很复杂，但囊泡运输和内吞途径对其控制的贡献仍不清楚。在这里，我们将巨胞饮作用确定为多种细胞系和衰老亚型中的一种组成型活跃的内吞途径。通过药理学和遗传扰动，我们证明 PAK1 是衰老细胞巨胞饮作用的关键调节因子。此外，PAK1 依赖性巨胞饮作用通过 TGF{beta} 信号传导调节炎症 SASP 因子（例如 IL6 和 CCL2）的产生。
- Keywords: macropinocytosis, sasp, phenotype, senescent, cells

### 9. [HiExM 实现细胞器形态和空间异质性的可扩展映射](https://www.biorxiv.org/content/10.64898/2026.07.12.738053v1)
- Original title: HiExM Enables Scalable Mapping of Organelle Morphology and Spatial Heterogeneity
- Authors: Day, J. H., Farrell, J. D., Yang, D., Neira, F. N., Allen, E. A. et al.
- Meta: 2026-07-14 | cell biology | DOI: 10.64898/2026.07.12.738053
- 中文摘要: 亚细胞组织的定量图像分析需要足够的空间分辨率来解析单个细胞器和样本大小，以捕获细胞内和细胞间的异质性。现有的成像方法通常迫使空间分辨率和通量之间进行权衡，限制了测量跨细胞群的细胞器水平表型的能力。在这里，我们建立了高通量扩展显微镜（HiExM）作为单细胞器分析的可扩展管道。作为基准，我们专注于绘制晚期内体和溶酶体（LEL），这是一种异质细胞器类别，其尺寸小、细胞内分布密集和功能多样性使得使用传统光学显微镜难以准确量化。
- Abstract: Quantitative image analysis of subcellular organization requires sufficient spatial resolution to resolve individual organelles and sample size to capture heterogeneity both within cells and between cells. Existing imaging approaches often force a tradeoff between spatial resolution and throughput, limiting the ability to measure organelle-level phenotypes across cell populations. Here, we establish high-throughputs...
- Summary (fallback): 机器翻译摘要显示：亚细胞组织的定量图像分析需要足够的空间分辨率来解析单个细胞器和样本大小，以捕获细胞内和细胞间的异质性。现有的成像方法通常迫使空间分辨率和通量之间进行权衡，限制了测量跨细胞群的细胞器水平表型的能力。在这里，我们建立了高通量扩展显微镜（HiExM）作为单细胞器分析的可扩展管道。作为基准，我们专注于绘制晚期内体和溶酶体（LEL），这是一种异质细胞器类别，其尺寸小、细胞内分布密集和功能多样性使得使用传统光学显微镜难以准确量化。
- Keywords: spatial, hiexm, scalable, analysis, resolution

### 10. [通过建立不对称细胞死亡形态将核材料划分成凋亡片段](https://www.biorxiv.org/content/10.64898/2026.07.13.738122v1)
- Original title: Partitioning of nuclear material into apoptotic fragments through establishment of asymmetric cell death morphology
- Authors: Santavanond, J. P., Jiang, L., Hodge, A. L., Ozkocak, D. C., Ceviker, A. et al.
- Meta: 2026-07-14 | cell biology | DOI: 10.64898/2026.07.13.738122
- 中文摘要: 凋亡细胞中的细胞物质必须被吞噬细胞有效地清除以维持组织稳态。此过程中的缺陷可能导致继发性坏死的发生和细胞内内容物的释放，例如损伤相关分子模式 (DAMP) 和通常源自细胞核的自身抗原。因此，适当处理和清除凋亡物质对于预防不需要的炎症反应和自身免疫性疾病的发生至关重要。然而，凋亡细胞如何包装核物质以供吞噬细胞有效清除的机制尚不清楚。通过利用细胞凋亡的小鼠模型，我们观察到由凋亡胸腺细胞产生的大细胞外囊泡的一个独特子集，称为凋亡小体（ApoBD），可以容纳大部分核内容物。
- Abstract: Cellular material in apoptotic cells must be efficiently cleared by phagocytes to maintain tissue homeostasis. Defects in this process can lead to the onset of secondary necrosis and the release of intracellular contents such as damage associated molecular patterns (DAMPs) and autoantigens that are often derived from the nucleus. Therefore, appropriate handling and clearance of apoptotic material is vital to prevent...
- Summary (fallback): 机器翻译摘要显示：凋亡细胞中的细胞物质必须被吞噬细胞有效地清除以维持组织稳态。此过程中的缺陷可能导致继发性坏死的发生和细胞内内容物的释放，例如损伤相关分子模式 (DAMP) 和通常源自细胞核的自身抗原。因此，适当处理和清除凋亡物质对于预防不需要的炎症反应和自身免疫性疾病的发生至关重要。然而，凋亡细胞如何包装核物质以供吞噬细胞有效清除的机制尚不清楚。通过利用细胞凋亡的小鼠模型，我们观察到由凋亡胸腺细胞产生的大细胞外囊泡的一个独特子集，称为凋亡小体（ApoBD），可以容纳大部分核内容物。
- Keywords: apoptotic, material, contents, nuclear, cell

### 11. [时间上不同的 CDX 程序预先配置迷走神经和躯干神经嵴](https://www.biorxiv.org/content/10.64898/2026.07.13.738216v1)
- Original title: Temporally distinct CDX programmes preconfigure vagal and trunk neural crest
- Authors: Amblard, I., Kalaitzis, C. M., Balaguer Balsells, I., Andrew, I., Choi, K. L. et al.
- Meta: 2026-07-14 | developmental biology | DOI: 10.64898/2026.07.13.738216
- 中文摘要: 神经嵴细胞（NCC）是祖细胞，对于脊椎动物胚胎的头部、心脏、肠道和周围神经系统的形成至关重要。 NCC 发育的中断是神经嵴病的基础，神经嵴病构成了一系列先天性异常。然而，NCC 如何获得明确的区域特征，使它们能够沿着身体轴生成不同的衍生物，目前仍不清楚。在这里，我们鉴定了小鼠胚胎中的外胚层祖细胞群，其短暂地促进迷走神经嵴细胞和躯干到尾部衍生物。利用神经嵴迁移连续阶段的单细胞空间转录组学，我们生成了颈胸细胞图谱，可以原位解析迷走神经和躯干神经嵴细胞。
- Abstract: Neural crest cells (NCCs) are progenitor cells vital in establishing the head, heart, gut and peripheral nervous system of vertebrate embryos. Disruptions to NCC development underlie neurocristopathies, which constitute a wide array of congenital anomalies. Yet how NCCs acquire defined regional identities that enable them to generate distinct derivatives along the body axis remains unclear. Here, we identify an epib...
- Summary (fallback): 机器翻译摘要显示：神经嵴细胞（NCC）是祖细胞，对于脊椎动物胚胎的头部、心脏、肠道和周围神经系统的形成至关重要。 NCC 发育的中断是神经嵴病的基础，神经嵴病构成了一系列先天性异常。然而，NCC 如何获得明确的区域特征，使它们能够沿着身体轴生成不同的衍生物，目前仍不清楚。在这里，我们鉴定了小鼠胚胎中的外胚层祖细胞群，其短暂地促进迷走神经嵴细胞和躯干到尾部衍生物。利用神经嵴迁移连续阶段的单细胞空间转录组学，我们生成了颈胸细胞图谱，可以原位解析迷走神经和躯干神经嵴细胞。
- Keywords: neural, crest, vagal, trunk, cells

### 12. [进食频率决定了海葵 Cylista elegans 无性繁殖的节奏](https://www.biorxiv.org/content/10.64898/2026.07.13.738267v1)
- Original title: Feeding frequency sets the rhythm of asexual reproduction in the sea anemone Cylista elegans
- Authors: Wells, C. D., Harris, L. G.
- Meta: 2026-07-14 | ecology | DOI: 10.64898/2026.07.13.738267
- 中文摘要: 许多海葵通过足裂伤进行无性繁殖，脱落的足盘碎片可再生为息肉。摄食如何影响这种繁殖的数量因物种而异，但摄食是否也决定其繁殖时间却很少被研究。我们每天、每两天、每四天或根本不喂食海葵 Cylista elegans（以前称为 Sagartia elegans），测量了 35 天的生长、撕裂和存活率，然后将海葵重新分配到新的时间表，以测试撕裂是否遵循当前或之前的时间表。生长随着喂养而增加，但饱和，每天喂养的动物和每隔一天以相似的速度生长。完全撕裂取决于海葵是否被喂食，而不是喂食的频率。每一次的喂食计划造成的撕裂伤比饥饿还多。相比之下，时间安排与时间表密切相关。
- Abstract: Many sea anemones reproduce asexually by pedal laceration, shedding fragments of the pedal disk that regenerate into polyps. How feeding affects the amount of this reproduction differs among species, but whether feeding also sets its timing has rarely been examined. We fed the sea anemone Cylista elegans (formerly Sagartia elegans) daily, every second day, every fourth day, or not at all, measured growth, laceration...
- Summary (fallback): 机器翻译摘要显示：许多海葵通过足裂伤进行无性繁殖，脱落的足盘碎片可再生为息肉。摄食如何影响这种繁殖的数量因物种而异，但摄食是否也决定其繁殖时间却很少被研究。我们每天、每两天、每四天或根本不喂食海葵 Cylista elegans（以前称为 Sagartia elegans），测量了 35 天的生长、撕裂和存活率，然后将海葵重新分配到新的时间表，以测试撕裂是否遵循当前或之前的时间表。生长随着喂养而增加，但饱和，每天喂养的动物和每隔一天以相似的速度生长。完全撕裂取决于海葵是否被喂食，而不是喂食的频率。每一次的喂食计划造成的撕裂伤比饥饿还多。相比之下，时间安排与时间表密切相关。
- Keywords: feeding, laceration, every, elegans, reproduction

### 13. [运动策略揭示了哺乳动物在城市地区的成功](https://www.biorxiv.org/content/10.64898/2026.07.13.738202v1)
- Original title: Movement strategies reveal the success of mammals in urban areas
- Authors: Grabow, M., Scholz, C., Roeleke, M., Stillfried, M., Kimmig, S. E. et al.
- Meta: 2026-07-14 | ecology | DOI: 10.64898/2026.07.13.738202
- 中文摘要: 人们提出了各种假设来解释为什么某些物种在城市地区持续存在甚至繁盛。然而，尽管运动行为在决定动物何时何地遇到资源、干扰和风险方面发挥着核心作用，但它仍然是城市成功的一个被忽视的机制。在城市地区，人类活动具有很强的周期性，即在空间和时间上是可预测的。这可能有利于物种能够根据可预测的资源周期和时空风险来调整自己的行为。在这里，我们测试了这一假设，并跟踪了三种具有不同城市成功率的哺乳动物物种沿着城市化梯度的运动行为：红狐（Vulpes vulpes），城市居民；浣熊（Procyon lotor），一种入侵性城市居民；以及城市使用者野猪（Sus scrofa）。
- Abstract: Various hypotheses have been proposed to explain why some species persist or even flourish in urban areas. Yet, despite its central role in determining when and where animals encounter resources, disturbance, and risk, movement behaviour remains an overlooked mechanism of urban success. In urban areas, human activities are strongly periodic, i.e. predictable in space and time. This may favour species able to adjust...
- Summary (fallback): 机器翻译摘要显示：人们提出了各种假设来解释为什么某些物种在城市地区持续存在甚至繁盛。然而，尽管运动行为在决定动物何时何地遇到资源、干扰和风险方面发挥着核心作用，但它仍然是城市成功的一个被忽视的机制。在城市地区，人类活动具有很强的周期性，即在空间和时间上是可预测的。这可能有利于物种能够根据可预测的资源周期和时空风险来调整自己的行为。在这里，我们测试了这一假设，并跟踪了三种具有不同城市成功率的哺乳动物物种沿着城市化梯度的运动行为：红狐（Vulpes vulpes），城市居民；浣熊（Procyon lotor），一种入侵性城市居民；以及城市使用者野猪（Sus scrofa）。
- Keywords: urban, movement, behaviour, urbanisation, success

### 14. [农村和发展中地区夜间人造光的生物足迹](https://www.biorxiv.org/content/10.64898/2026.07.13.737561v1)
- Original title: Biological Footprint of Artificial Light at Night in Rural and Developing Areas
- Authors: Boyles, J. G., Merritt, B. J., Koen, E., Minnaar, C.
- Meta: 2026-07-14 | ecology | DOI: 10.64898/2026.07.13.737561
- 中文摘要: 背景夜间人造光 (ALAN) 对个体生物体和整个群落有着深远的影响。尽管如此，人类还是倾向于低估 ALAN 的真实生物（空间）足迹，部分原因是与其他生物体相比，我们对光的敏感性有限。目标 我们试图利用基本物理定律（平方反比定律）证明 ALAN 能够深入黑暗空间多远，达到影响有机体行为和生理学的水平。方法我们创建了真实景观上的光传播的空间明确模型，使用日益可用的景观规模植被数据进行参数化，以解释森林的衰减和地形起伏的阻挡。结果 农村地区常见的照明类型可以在距光源 1 公里以上的范围内产生具有重要生物学意义的影响，而大型照明的影响可能会延伸 3 公里或更远。
- Abstract: Context Artificial light at night (ALAN) has profound impacts on individual organisms and entire communities. Still, humans tend to underestimate the true biological (spatial) footprint of ALAN, in part because of our limited sensitivity to light compared to other organisms. Objectives We sought to demonstrate how far ALAN can reach into dark spaces at levels that can impact organismal behavior and physiology using...
- Summary (fallback): 机器翻译摘要显示：背景夜间人造光 (ALAN) 对个体生物体和整个群落有着深远的影响。尽管如此，人类还是倾向于低估 ALAN 的真实生物（空间）足迹，部分原因是与其他生物体相比，我们对光的敏感性有限。目标 我们试图利用基本物理定律（平方反比定律）证明 ALAN 能够深入黑暗空间多远，达到影响有机体行为和生理学的水平。方法我们创建了真实景观上的光传播的空间明确模型，使用日益可用的景观规模植被数据进行参数化，以解释森林的衰减和地形起伏的阻挡。结果 农村地区常见的照明类型可以在距光源 1 公里以上的范围内产生具有重要生物学意义的影响，而大型照明的影响可能会延伸 3 公里或更远。
- Keywords: light, footprint, biological, alan, lighting

### 15. [无色网状植物 Ciliophrys sp。波罗的海其次缺乏质体，但拥有细菌内共生体](https://www.biorxiv.org/content/10.64898/2026.03.27.714854v2)
- Original title: The colourless dictyochophyte Ciliophrys sp. Baltic secondarily lacks a plastid but hosts a bacterial endosymbiont
- Authors: Barcyte, D., Husnik, F., Elias, M.
- Meta: 2026-07-14 | evolutionary biology | DOI: 10.64898/2026.03.27.714854
- 中文摘要: 细胞器的丧失代表了还原进化的极端情况。仅记录了少数质体丢失事件，并且它们在自由生活的祖先光合类群中似乎特别罕见。我们分离出一种新的吞噬性原生生物，Ciliophrys sp。波罗的海，代表原生藻藻类网藻纲中研究很少的非光合作用谱系。该生物体的基因组和转录组数据表明，它缺乏对质体生物发生至关重要的质体基因组和核基因。因此，质体细胞器很可能是从 Ciliophrys sp. 中其次缺失的。波罗的海，尽管一些最初针对质体的酶随着定位的改变而持续存在。出乎意料的是，Ciliophrys sp。波罗的海拥有一种细菌内共生体，Candidatus Penulousia baltica sp。十一月（立克次体目）。
- Abstract: The loss of an organelle represents an extreme case of reductive evolution. Only a few plastid loss events have been documented and they seem to be particularly rare in free-living ancestrally photosynthetic taxa. We isolated a new phagotrophic protist, Ciliophrys sp. Baltic, representing a poorly studied non-photosynthetic lineage in the stramenopile algal class Dictyochophyceae. Genomic and transcriptomic data fro...
- Summary (fallback): 机器翻译摘要显示：细胞器的丧失代表了还原进化的极端情况。仅记录了少数质体丢失事件，并且它们在自由生活的祖先光合类群中似乎特别罕见。我们分离出一种新的吞噬性原生生物，Ciliophrys sp。波罗的海，代表原生藻藻类网藻纲中研究很少的非光合作用谱系。该生物体的基因组和转录组数据表明，它缺乏对质体生物发生至关重要的质体基因组和核基因。因此，质体细胞器很可能是从 Ciliophrys sp. 中其次缺失的。波罗的海，尽管一些最初针对质体的酶随着定位的改变而持续存在。出乎意料的是，Ciliophrys sp。波罗的海拥有一种细菌内共生体，Candidatus Penulousia baltica sp。十一月（立克次体目）。
- Keywords: plastid, ciliophrys, baltic, loss, endosymbiont

### 16. [通过统一的潜在动力学生成全脑神经活动和行为](https://www.biorxiv.org/content/10.64898/2026.06.05.730482v2)
- Original title: Generating whole-brain neural activity and behavior through unified latent dynamics
- Authors: Nuzzi, D., Mattia, M., Pezzulo, G.
- Meta: 2026-07-14 | animal behavior and cognition | DOI: 10.64898/2026.06.05.730482
- 中文摘要: 了解高维神经活动和行为如何从共享的潜在动力学中产生仍然是神经科学的基本挑战。解决这个问题是使数字孪生能够忠实地再现和预测生命系统的多尺度大脑行为动态的关键。在这里，我们提出了 NEBULA（通过统一 LAtent 动力学进行神经和行为建模），这是一个联合建模全脑神经活动和行为的生成框架。该模型利用线虫的全脑记录，学习统一的潜在动态结构，支持神经和行为轨迹的长视野生成、行为的真实模拟和有针对性的虚拟干预。
- Abstract: Understanding how high-dimensional neural activity and behavior emerge from shared underlying dynamics remains a fundamental challenge in neuroscience. Addressing this problem is key to enabling digital twins that can faithfully reproduce and predict the multiscale brain-behavior dynamics of living systems. Here we present NEBULA (NEural and Behavioral modeling through Unified LAtent dynamics), a generative framewor...
- Summary (fallback): 机器翻译摘要显示：了解高维神经活动和行为如何从共享的潜在动力学中产生仍然是神经科学的基本挑战。解决这个问题是使数字孪生能够忠实地再现和预测生命系统的多尺度大脑行为动态的关键。在这里，我们提出了 NEBULA（通过统一 LAtent 动力学进行神经和行为建模），这是一个联合建模全脑神经活动和行为的生成框架。该模型利用线虫的全脑记录，学习统一的潜在动态结构，支持神经和行为轨迹的长视野生成、行为的真实模拟和有针对性的虚拟干预。
- Keywords: neural, dynamics, behavior, activity, unified

### 17. [以自我为中心的信念归因可以在群体互动中实现更高层次的心理理论计算。](https://www.biorxiv.org/content/10.64898/2026.03.27.714726v3)
- Original title: Egocentric belief attribution enables higher level Theory of Mind computation in group interactions.
- Authors: Zhang, S., Wang, H., Mendoza, R. B.
- Meta: 2026-07-14 | animal behavior and cognition | DOI: 10.64898/2026.03.27.714726
- 中文摘要: 准确地将信念归因于他人是社会认知的里程碑，也是完整认知功能的指标。然而，在复杂的社交互动中追踪所有其他人的信念往往效率低下，甚至是不可能的。我们建议，在这种情况下，将自己的信念归因于他人（即以自我为中心的信念归因）可以作为功能近似，使个人能够成功地与他人互动。在这项研究中，我们采用具有行为测量的计算模型来通过三个实验研究这种新型群体决策任务中的社会交换方法。我们发现，除了有据可查的互惠性之外，参与者还表现出一致的交替行为，其特点是潜在接受者之间的切换。
- Abstract: Accurately attributing belief to others is a milestone of social cognition and serves as an indicator of intact cognitive functioning. However, tracking all others' beliefs in complex social interactions is often inefficient or even impossible. We propose that in such cases, attributing one's own belief to others (i.e., egocentric belief attribution) may serve as a functional approximation, enabling individuals to i...
- Summary (fallback): 机器翻译摘要显示：准确地将信念归因于他人是社会认知的里程碑，也是完整认知功能的指标。然而，在复杂的社交互动中追踪所有其他人的信念往往效率低下，甚至是不可能的。我们建议，在这种情况下，将自己的信念归因于他人（即以自我为中心的信念归因）可以作为功能近似，使个人能够成功地与他人互动。在这项研究中，我们采用具有行为测量的计算模型来通过三个实验研究这种新型群体决策任务中的社会交换方法。我们发现，除了有据可查的互惠性之外，参与者还表现出一致的交替行为，其特点是潜在接受者之间的切换。
- Keywords: belief, egocentric, attribution, others, social

### 18. [hNav1.5α 形成反向平行的细胞内同二聚体，但作为单体掺入质膜中](https://www.biorxiv.org/content/10.64898/2026.07.12.738063v1)
- Original title: hNav1.5α forms an antiparallel intracellular homodimer but is incorporated into the plasma membrane as a monomer
- Authors: Schmalzing, G., Li, L.
- Meta: 2026-07-14 | biochemistry | DOI: 10.64898/2026.07.12.738063
- 中文摘要: 长期以来，电生理学研究一直将心脏电压门控钠通道 Nav1.5a (SCN5A) 视为单体成孔单元，与所有可用的冷冻电镜结构一致，仅显示单体结构。相比之下，生化研究——交联、单分子下拉和天然电泳——报道了具有耦合门控的 500 kDa Nav1.5a 同二聚体。为了调和这种明显的差异，我们将非洲爪蟾卵母细胞中 hNav1.5a 总池（代谢 35S-蛋氨酸）和质膜池（非膜渗透 IRDye 800CW）的选择性标记与高分辨率清晰天然电泳 (hrCNE) 结合起来。
- Abstract: Electrophysiological studies have long treated the cardiac voltage-gated sodium channel Nav1.5a (SCN5A) as a monomeric pore-forming unit, consistent with all available cryo-EM structures, which show only monomeric architectures. In contrast, biochemical studies - cross-linking, single-molecule pulldown, and native electrophoresis - have reported 500 kDa Nav1.5a homodimers with coupled gating. To reconcile this appar...
- Summary (fallback): 机器翻译摘要显示：长期以来，电生理学研究一直将心脏电压门控钠通道 Nav1.5a (SCN5A) 视为单体成孔单元，与所有可用的冷冻电镜结构一致，仅显示单体结构。相比之下，生化研究——交联、单分子下拉和天然电泳——报道了具有耦合门控的 500 kDa Nav1.5a 同二聚体。为了调和这种明显的差异，我们将非洲爪蟾卵母细胞中 hNav1.5a 总池（代谢 35S-蛋氨酸）和质膜池（非膜渗透 IRDye 800CW）的选择性标记与高分辨率清晰天然电泳 (hrCNE) 结合起来。
- Keywords: hnav1, homodimer, antiparallel, intracellular, monomer

### 19. [FAIM 通过非典型聚集途径抑制胰岛素淀粉样蛋白生成](https://www.biorxiv.org/content/10.64898/2026.07.13.738277v1)
- Original title: FAIM Inhibits Insulin Amyloidogenesis through a Noncanonical Aggregation Pathway
- Authors: Wolfe, D., Saha, J., Mitchell, J., McCalpin, S., Gutknecht, M. et al.
- Meta: 2026-07-14 | biochemistry | DOI: 10.64898/2026.07.13.738277
- 中文摘要: 胰岛素可以错误折叠并组装成淀粉样原纤维，这一过程不仅与胰岛素治疗的并发症有关，还与胰腺β细胞中的蛋白毒性应激有关。尽管人们对胰岛素聚集的病理后果越来越感兴趣，但由于对抵消胰岛素聚集的内源机制的不完全了解，预防工作受到限制。在这里，我们将 Fas 凋亡抑制分子 (FAIM) 确定为胰岛素淀粉样蛋白形成的内源性抑制剂。 FAIM 减少 β 折叠的形成，并将胰岛素重新定向到无序、生长无能的组装体上。此外，FAIM 还可减弱体外胰岛素聚集体的细胞毒性。我们假设这种效应是由于掩盖了胰岛素易于聚集的区域而产生的，并通过结构模型表明 FAIM 与两条胰岛素链相互作用。
- Abstract: Insulin can misfold and assemble into amyloid fibrils, a process linked not only to complications of insulin therapy but also to proteotoxic stress in pancreatic beta cells. Despite growing interest in the pathological consequences of insulin aggregation, prevention efforts are limited by an incomplete understanding of the endogenous mechanisms that counteract it. Here, we identify Fas apoptosis inhibitory molecule...
- Summary (fallback): 机器翻译摘要显示：胰岛素可以错误折叠并组装成淀粉样原纤维，这一过程不仅与胰岛素治疗的并发症有关，还与胰腺β细胞中的蛋白毒性应激有关。尽管人们对胰岛素聚集的病理后果越来越感兴趣，但由于对抵消胰岛素聚集的内源机制的不完全了解，预防工作受到限制。在这里，我们将 Fas 凋亡抑制分子 (FAIM) 确定为胰岛素淀粉样蛋白形成的内源性抑制剂。 FAIM 减少 β 折叠的形成，并将胰岛素重新定向到无序、生长无能的组装体上。此外，FAIM 还可减弱体外胰岛素聚集体的细胞毒性。我们假设这种效应是由于掩盖了胰岛素易于聚集的区域而产生的，并通过结构模型表明 FAIM 与两条胰岛素链相互作用。
- Keywords: insulin, faim, aggregation, amyloid, endogenous

### 20. [利福霉素 B 对抗利福平耐药 RNA 聚合酶的意外活性的结构基础](https://www.biorxiv.org/content/10.64898/2026.07.13.738162v1)
- Original title: Structural basis for the unexpected activity of rifamycin B against rifampicin-resistant RNA polymerase
- Authors: Mosaei, H., Shin, Y., Kozhevnikov, V. N., Waddell, P. G., Hall, M. J. et al.
- Meta: 2026-07-14 | biochemistry | DOI: 10.64898/2026.07.13.738162
- 中文摘要: 利福霉素通过靶向 RNA 聚合酶 (RNAP) 来抑制细菌转录，但其临床有效性因利福霉素结合袋内突变引起的耐药性的迅速出现而受到限制。利福霉素 B (Rif B) 是该抗生素家族中最早发现的成员之一，也是临床使用的衍生物的前体，但由于其化学不稳定和相对较弱的抗菌活性，其特征仍然很少。在这里，我们使用生化和结构方法重新审视 Rif B。我们表明，Rif B 在测定条件下保持足够稳定，并保留对携带临床相关利福平耐药突变的 RNAP 变体的抑制活性。我们报告了 Rif B 的第一个晶体结构，并确定了与细菌 RNAP 结合的 Rif B 的结构。
- Abstract: Rifamycins inhibit bacterial transcription by targeting RNA polymerase (RNAP), but their clinical effectiveness is limited by the rapid emergence of resistance caused by mutations within the rifamycin-binding pocket. Rifamycin B (Rif B), one of the earliest discovered members of this antibiotic family and a precursor of clinically used derivatives, has remained poorly characterized because of its chemical instabilit...
- Summary (fallback): 机器翻译摘要显示：利福霉素通过靶向 RNA 聚合酶 (RNAP) 来抑制细菌转录，但其临床有效性因利福霉素结合袋内突变引起的耐药性的迅速出现而受到限制。利福霉素 B (Rif B) 是该抗生素家族中最早发现的成员之一，也是临床使用的衍生物的前体，但由于其化学不稳定和相对较弱的抗菌活性，其特征仍然很少。在这里，我们使用生化和结构方法重新审视 Rif B。我们表明，Rif B 在测定条件下保持足够稳定，并保留对携带临床相关利福平耐药突变的 RNAP 变体的抑制活性。我们报告了 Rif B 的第一个晶体结构，并确定了与细菌 RNAP 结合的 Rif B 的结构。
- Keywords: rnap, rifamycin, activity, structural, against

### 21. [MolMAE：用于分子表示学习的以表面为中心的多模态掩蔽自动编码器](https://www.biorxiv.org/content/10.64898/2026.07.11.737987v1)
- Original title: MolMAE: A Surface-Centric Multimodal Masked Autoencoder for Molecular Representation Learning
- Authors: Li, J.
- Meta: 2026-07-14 | bioinformatics | DOI: 10.64898/2026.07.11.737987
- 中文摘要: 分子表示学习已成为现代计算药物发现的核心组成部分。现有的分子基础模型主要依赖于SMILES字符串、二维分子图或三维原子坐标。然而，许多分子特性最终由分子表面决定，分子间识别、溶剂化、静电互补和配体-蛋白质相互作用发生在分子表面。在这项工作中，我们提出了 MolMAE，一种用于分子表示学习的表面引导多模态掩码自动编码器。 MolMAE 将分子表面点云、三维分子图以及 SMILES 衍生的片段和功能组标记作为补充输入模态，并通过功能组对齐的掩码自动编码学习统一的多模态分子嵌入。
- Abstract: Molecular representation learning has become a central component of modern computational drug discovery. Existing molecular foundation models mainly rely on SMILES strings, two-dimensional molecular graphs, or three-dimensional atomic coordinates. However, many molecular properties are ultimately governed by the molecular surface, where intermolecular recognition, solvation, electrostatic complementarity, and ligand...
- Summary (fallback): 机器翻译摘要显示：分子表示学习已成为现代计算药物发现的核心组成部分。现有的分子基础模型主要依赖于SMILES字符串、二维分子图或三维原子坐标。然而，许多分子特性最终由分子表面决定，分子间识别、溶剂化、静电互补和配体-蛋白质相互作用发生在分子表面。在这项工作中，我们提出了 MolMAE，一种用于分子表示学习的表面引导多模态掩码自动编码器。 MolMAE 将分子表面点云、三维分子图以及 SMILES 衍生的片段和功能组标记作为补充输入模态，并通过功能组对齐的掩码自动编码学习统一的多模态分子嵌入。
- Keywords: molecular, surface, molmae, masked, multimodal

### 22. [移植代理：用于移植后风险预测和排斥生物标志物可重复性评估的多代理人工智能框架](https://www.biorxiv.org/content/10.1101/2025.07.10.664265v2)
- Original title: Transplant-Agents: A Multi-Agent Artificial Intelligence Framework for Reproducibility Assessment of Post-Transplant Risk Prediction and Rejection Biomarkers
- Authors: Ding, S., Bhattacharya, S., Sarwal, M. M., Sirota, M., Butte, A.
- Meta: 2026-07-14 | bioinformatics | DOI: 10.1101/2025.07.10.664265
- 中文摘要: 可重复的生物标志物识别和移植排斥风险预测仍然是移植医学中尚未解决的基本挑战。传统方法依赖于假设驱动的分析和领域专业知识，限制了不同人群的可扩展性和普遍性。我们推出了 Transplant-Agents，这是一种数据驱动的多代理 AI 框架，它将大型语言模型 (LLM) 与机器学习算法相结合，用于自动生物标志物识别和排斥风险预测。代理通过受预定义规则和标准控制的结构化迭代对话进行交互，收敛于可在多次迭代中重现的最佳生物标记集。我们评估了 ImmPort 的三个多中心临床试验移植数据集，其中包括肾脏、肝脏和心脏移植队列的 683 名患者。
- Abstract: Reproducible biomarker identification and transplant rejection risk prediction remain fundamental yet unsolved challenges in transplantation medicine. Traditional approaches rely on hypothesis-driven analyses and domain expertise, limiting scalability and generalizability across diverse populations. We introduce Transplant-Agents, a data-driven multi-agent AI framework integrating large language models (LLMs) with m...
- Summary (fallback): 机器翻译摘要显示：可重复的生物标志物识别和移植排斥风险预测仍然是移植医学中尚未解决的基本挑战。传统方法依赖于假设驱动的分析和领域专业知识，限制了不同人群的可扩展性和普遍性。我们推出了 Transplant-Agents，这是一种数据驱动的多代理 AI 框架，它将大型语言模型 (LLM) 与机器学习算法相结合，用于自动生物标志物识别和排斥风险预测。代理通过受预定义规则和标准控制的结构化迭代对话进行交互，收敛于可在多次迭代中重现的最佳生物标记集。我们评估了 ImmPort 的三个多中心临床试验移植数据集，其中包括肾脏、肝脏和心脏移植队列的 683 名患者。
- Keywords: risk, prediction, transplant, transplant-agents, rejection

### 23. [长读长多组学测序揭示复发性星形细胞瘤的 DNA 到 RNA 进化重塑轨迹](https://www.biorxiv.org/content/10.64898/2026.07.12.738108v1)
- Original title: Long read multi-omics sequencing reveals DNA-to-RNA evolutionary remodeling trajectories of recurrent astrocytoma
- Authors: Rashad, S., Ando, D., Yamashita, S., Shimoda, Y., Kanamori, M. et al.
- Meta: 2026-07-14 | cancer biology | DOI: 10.64898/2026.07.12.738108
- 中文摘要: 星形细胞瘤的复发是由遗传、表观遗传和转录进化决定的，但 DNA 重塑如何传播为全长 RNA 亚型和编码后果仍然没有得到很好的解决。在这里，我们应用配对的 PacBio HiFi 全基因组测序和 Kinnex 全长 RNA 测序来匹配来自 6 名患者的原发性和复发性星形细胞瘤，以及匹配的血液对照。复发性肿瘤保留了核心神经胶质瘤驱动因素的身份，同时获得了患者特异性的体细胞变异、拷贝数、结构变异、杂合性丧失、单倍型失衡和DNA甲基化的重塑。长读转录组学揭示了广泛的复发相关基因表达、亚型使用、差异转录本使用，并预测了基因水平表达之外的 ORF/蛋白质命运重塑。
- Abstract: Astrocytoma recurrence is shaped by genetic, epigenetic and transcriptional evolution, but how DNA remodeling is propagated into full-length RNA isoforms and coding consequences remains poorly resolved. Here we applied paired PacBio HiFi whole-genome sequencing and Kinnex full-length RNA sequencing to matched primary and recurrent astrocytoma from six patients, with matched blood controls. Recurrent tumors preserved...
- Summary (fallback): 机器翻译摘要显示：星形细胞瘤的复发是由遗传、表观遗传和转录进化决定的，但 DNA 重塑如何传播为全长 RNA 亚型和编码后果仍然没有得到很好的解决。在这里，我们应用配对的 PacBio HiFi 全基因组测序和 Kinnex 全长 RNA 测序来匹配来自 6 名患者的原发性和复发性星形细胞瘤，以及匹配的血液对照。复发性肿瘤保留了核心神经胶质瘤驱动因素的身份，同时获得了患者特异性的体细胞变异、拷贝数、结构变异、杂合性丧失、单倍型失衡和DNA甲基化的重塑。长读转录组学揭示了广泛的复发相关基因表达、亚型使用、差异转录本使用，并预测了基因水平表达之外的 ORF/蛋白质命运重塑。
- Keywords: remodeling, recurrent, astrocytoma, sequencing, variants

### 24. [癌症持续细胞激活 NMDAR 以在铁死亡中生存](https://www.biorxiv.org/content/10.64898/2026.07.13.738168v1)
- Original title: Cancer persister cells activate NMDARs to survive ferroptosis
- Authors: PUNZI, S., VILLANTI, I., GATTI, G., CITTARO, D., CRUPI, G. et al.
- Meta: 2026-07-14 | cancer biology | DOI: 10.64898/2026.07.13.738168
- 中文摘要: 治疗后，癌细胞会进行非遗传适应，包括耐受性和随后的持久性，以在治疗中生存。在这些持续细胞（PC）中引发程序性癌细胞死亡仍然是肿瘤学的主要目标。我们发现，铁死亡是持久性结直肠癌细胞中最不受控制的程序性细胞死亡机制，通过一些最广泛使用的治疗方案，包括基于铂的疗法，该疗法与铁死亡诱导剂相结合，可以消融持久性结直肠癌细胞。相反，拓扑异构酶抑制剂疗法中出现的持续细胞能够抵抗铁死亡和铁死亡诱导剂，反而增加细胞内铁浓度。我们发现拓扑异构酶抑制剂触发 Xc 逆向转运轴（通过 SLC7A11 和 CD44）增加细胞内胱氨酸以激活 GPX4 和细胞外谷氨酸。
- Abstract: Upon treatment, cancer cells engage non-genetic adaptations, including tolerance and subsequent persistence, to survive therapy. Eliciting programmed cancer cell death in these persister cells (PCs) remains a primary goal in oncology. We found that ferroptosis is the programmed cell death mechanism most deregulated in persisters by some of the most widely used therapeutic regimens, including platinum-based therapies...
- Summary (fallback): 机器翻译摘要显示：治疗后，癌细胞会进行非遗传适应，包括耐受性和随后的持久性，以在治疗中生存。在这些持续细胞（PC）中引发程序性癌细胞死亡仍然是肿瘤学的主要目标。我们发现，铁死亡是持久性结直肠癌细胞中最不受控制的程序性细胞死亡机制，通过一些最广泛使用的治疗方案，包括基于铂的疗法，该疗法与铁死亡诱导剂相结合，可以消融持久性结直肠癌细胞。相反，拓扑异构酶抑制剂疗法中出现的持续细胞能够抵抗铁死亡和铁死亡诱导剂，反而增加细胞内铁浓度。我们发现拓扑异构酶抑制剂触发 Xc 逆向转运轴（通过 SLC7A11 和 CD44）增加细胞内胱氨酸以激活 GPX4 和细胞外谷氨酸。
- Keywords: cancer, cells, ferroptosis, persister, nmdars

### 25. [破坏趋同乙酰化回路会破坏 AML 亚型的白血病特性](https://www.biorxiv.org/content/10.64898/2026.07.13.737885v1)
- Original title: Disrupting a Convergent Acetylation Circuit Collapses Leukemic Identity Across AML Subtypes
- Authors: Deshpande, A., Chiang, C.-Y., Perales Garcia, M., Niranjan, N., Sinha, N. et al.
- Meta: 2026-07-14 | cancer biology | DOI: 10.64898/2026.07.13.737885
- 中文摘要: 急性髓系白血病 (AML) 细胞依靠积极维持的染色质编码转录程序来维持其恶性身份，从而提​​供了潜在的治疗脆弱性。利用来自 1,000 多个癌细胞系的基因组规模依赖性数据，我们确定 SAGA 组蛋白乙酰转移酶复合物是 AML 和血液恶性肿瘤中的选择性染色质依赖性。我们表明，使用脑招募 PROTAC (GSK983/GSK699) 对 SAGA 催化亚基 KAT2A 和 KAT2B 进行药理学降解，可在遗传多样性的 AML 细胞系、原发性患者样本和具有协同致癌突变的同基因 KMT2A 重排模型中产生有效的广谱抗白血病活性。
- Abstract: Acute myeloid leukemia (AML) cells rely on an actively maintained, chromatin-encoded transcriptional program to sustain their malignant identity, offering a potential therapeutic vulnerability. Using genome-scale dependency data from over 1,000 cancer cell lines, we identify the SAGA histone acetyltransferase complex as a selective chromatin dependency in AML and hematological malignancies. We show that pharmacologi...
- Summary (fallback): 机器翻译摘要显示：急性髓系白血病 (AML) 细胞依靠积极维持的染色质编码转录程序来维持其恶性身份，从而提​​供了潜在的治疗脆弱性。利用来自 1,000 多个癌细胞系的基因组规模依赖性数据，我们确定 SAGA 组蛋白乙酰转移酶复合物是 AML 和血液恶性肿瘤中的选择性染色质依赖性。我们表明，使用脑招募 PROTAC (GSK983/GSK699) 对 SAGA 催化亚基 KAT2A 和 KAT2B 进行药理学降解，可在遗传多样性的 AML 细胞系、原发性患者样本和具有协同致癌突变的同基因 KMT2A 重排模型中产生有效的广谱抗白血病活性。
- Keywords: kat2a, transcriptional, acetylation, histone, degradation

### 26. [遗传增殖状态组织植物转录组](https://www.biorxiv.org/content/10.64898/2026.07.12.738078v1)
- Original title: Inherited proliferation states organize plant transcriptomes
- Authors: Lee, C., Lee, S., Gwon, D., Razzaque, S., Jeong, H. et al.
- Meta: 2026-07-14 | plant biology | DOI: 10.64898/2026.07.12.738078
- 中文摘要: 植物生物学的一个中心问题是自然转录组变异是否主要反映环境适应或内在遗传程序。使用 665 个天然拟南芥种质的转录组，我们发现遗传群体结构，而不是环境梯度，是全球转录组结构的主要组织者。基因组群体结构独特地解释了转录组广泛变异的 30.0%，而环境变量仅占 2.5%。该结构由单一共表达程序（增殖模块特征基因：prolifME）主导，富含细胞周期调节和核糖体生物发生，受二分转录因子结构调节，并在具有广泛反式调节作用的离散位点进行遗传编码。
- Abstract: A central question in plant biology is whether natural transcriptome variation primarily reflects environmental adaptation or intrinsic genetic programs. Using transcriptomes from 665 natural Arabidopsis thaliana accessions, we show that inherited population structure, not environmental gradients, is the primary organizer of global transcriptome architecture. Genomic population structure uniquely explains 30.0% of t...
- Summary (fallback): 机器翻译摘要显示：植物生物学的一个中心问题是自然转录组变异是否主要反映环境适应或内在遗传程序。使用 665 个天然拟南芥种质的转录组，我们发现遗传群体结构，而不是环境梯度，是全球转录组结构的主要组织者。基因组群体结构独特地解释了转录组广泛变异的 30.0%，而环境变量仅占 2.5%。该结构由单一共表达程序（增殖模块特征基因：prolifME）主导，富含细胞周期调节和核糖体生物发生，受二分转录因子结构调节，并在具有广泛反式调节作用的离散位点进行遗传编码。
- Keywords: proliferation, plant, program, transcriptomes, transcriptome

### 27. [合成细胞膜上的可编程和动态 DNA 定位](https://www.biorxiv.org/content/10.64898/2026.07.13.738173v1)
- Original title: Programmable and Dynamic DNA Localisation at Synthetic Cell Membranes
- Authors: Dack, C., Li, B., Newell, C., Booth, M. J.
- Meta: 2026-07-14 | synthetic biology | DOI: 10.64898/2026.07.13.738173
- 中文摘要: 膜相关成分的空间和时间组织是细胞信号传导的基础，但在最小的合成系统中仍然难以设计。在合成细胞中，DNA 和 RNA 纳米技术可在膜上提供可编程的分子组织，而体外转录 (IVT) 则可实现基因表达驱动的调节。然而，由于转录机制和核酸组装体之间存在不良相互作用，将这些系统整合到细胞样区室（例如巨型单层囊泡（GUV））中仍然具有挑战性。在这里，我们提出了一种模块化策略，将原位 RNA 生产与 GUV 合成细胞膜上的动态 DNA 定位相结合。在 GUV 内转录的 RNA 链充当连接子，将 DNA 缀合的货物招募到脂质膜上，从而实现可编程的空间组织。
- Abstract: Spatial and temporal organisation of membrane-associated components is fundamental to cellular signalling, yet remains difficult to engineer in minimal synthetic systems. In synthetic cells, DNA and RNA nanotechnology offer programmable molecular organisation at membranes, while in vitro transcription (IVT) enables gene expression-driven regulation. However, integrating these systems within cell-like compartments, s...
- Summary (fallback): 机器翻译摘要显示：膜相关成分的空间和时间组织是细胞信号传导的基础，但在最小的合成系统中仍然难以设计。在合成细胞中，DNA 和 RNA 纳米技术可在膜上提供可编程的分子组织，而体外转录 (IVT) 则可实现基因表达驱动的调节。然而，由于转录机制和核酸组装体之间存在不良相互作用，将这些系统整合到细胞样区室（例如巨型单层囊泡（GUV））中仍然具有挑战性。在这里，我们提出了一种模块化策略，将原位 RNA 生产与 GUV 合成细胞膜上的动态 DNA 定位相结合。在 GUV 内转录的 RNA 链充当连接子，将 DNA 缀合的货物招募到脂质膜上，从而实现可编程的空间组织。
- Keywords: synthetic, programmable, dynamic, membranes, localisation

### 28. [最少的数据，最大的洞察力（MDMI）：用于发现肽-蛋白质界面功能替代品的结构引导管道](https://www.biorxiv.org/content/10.64898/2026.07.13.737974v1)
- Original title: Minimal Data, Maximal Insight (MDMI): A Structure-guided Pipeline for Discovering Functional Alternatives in Peptide-Protein Interfaces
- Authors: Bayat, P., Perkins, S. J., Clancy, S., Patel, S. S., Yin, R. F. et al.
- Meta: 2026-07-14 | synthetic biology | DOI: 10.64898/2026.07.13.737974
- 中文摘要: 在巨大的序列空间中发现功能肽仍然是一项艰巨的挑战，特别是在实验训练数据稀缺的情况下。我们提出了最小数据最大洞察力（MDMI），这是一种两阶段结构引导的计算管道，仅使用小型带注释的数据集来设计功能性肽变体。 MDMI 不是仅仅依赖序列信息，而是将从预测的肽-蛋白质复合物衍生的三维结构特征集成到捕获界面几何形状和结合能量的机器学习模型中。
- Abstract: Discovering functional peptides across vast sequence space remains a formidable challenge, particularly when experimental training data is scarce. We present Minimal Data Maximal Insight (MDMI), a two-stage structure-guided computational pipeline that designs functional peptide variants using only a small, annotated dataset. Rather than relying on sequence information alone, MDMI integrates three-dimensional structu...
- Summary (fallback): 机器翻译摘要显示：在巨大的序列空间中发现功能肽仍然是一项艰巨的挑战，特别是在实验训练数据稀缺的情况下。我们提出了最小数据最大洞察力（MDMI），这是一种两阶段结构引导的计算管道，仅使用小型带注释的数据集来设计功能性肽变体。 MDMI 不是仅仅依赖序列信息，而是将从预测的肽-蛋白质复合物衍生的三维结构特征集成到捕获界面几何形状和结合能量的机器学习模型中。
- Keywords: functional, sequence, mdmi, minimal, peptide-protein

### 29. [自闭症谱系障碍患者节律同步期间保留的自发人际牵引](https://www.biorxiv.org/content/10.64898/2026.07.09.737537v1)
- Original title: Preserved Spontaneous Interpersonal Entrainment during Rhythmic Synchronization in Autism Spectrum Disorder
- Authors: Denis, M., Rosso, M., Da Fonseca, D., Schön, D.
- Meta: 2026-07-14 | neuroscience | DOI: 10.64898/2026.07.09.737537
- 中文摘要: 目的：人际夹带被定义为互动个体暂时调整其行为的倾向，被认为是通过预测和多感官过程支持社会互动的关键机制。自闭症谱系障碍（ASD）以社交和沟通困难为特征，与非典型的预测和多感觉整合过程有关，这可能会影响在有节奏的互动过程中自发地夹带他人的行为。方法：本研究使用 Rosso 等人开发的漂移节拍器范式的单向适应，调查了 24 名自闭症患者和 22 名神经正常年轻人的自发人际交往。 （2021）。
- Abstract: Purpose: Interpersonal entrainment, defined as the tendency of interacting individuals to temporally align their behaviours, is considered a key mechanism supporting social interactions through predictive and multisensory processes. Autism Spectrum Disorder (ASD), characterized by social and communication difficulties, has been associated with atypical predictive and multisensory integration processes, which may aff...
- Summary (fallback): 机器翻译摘要显示：目的：人际夹带被定义为互动个体暂时调整其行为的倾向，被认为是通过预测和多感官过程支持社会互动的关键机制。自闭症谱系障碍（ASD）以社交和沟通困难为特征，与非典型的预测和多感觉整合过程有关，这可能会影响在有节奏的互动过程中自发地夹带他人的行为。方法：本研究使用 Rosso 等人开发的漂移节拍器范式的单向适应，调查了 24 名自闭症患者和 22 名神经正常年轻人的自发人际交往。 （2021）。
- Keywords: interpersonal, entrainment, spontaneous, synchronization, predictive

### 30. [FLiPA：用于定量分析蛋白质-鞘糖脂相互作用的多功能平台](https://www.biorxiv.org/content/10.64898/2026.07.13.738194v1)
- Original title: FLiPA: A versatile platform for quantitative analysis of protein-glycosphingolipid interactions
- Authors: McKie, S. J., Deane, J. E., Bishop, E.
- Meta: 2026-07-14 | molecular biology | DOI: 10.64898/2026.07.13.738194
- 中文摘要: 蛋白质和鞘糖脂 (GSL) 之间的相互作用调节各种细胞过程，而 GSL 代谢的改变会导致多种疾病。 GSL 的不同聚糖头基和神经酰胺主链塑造膜组织、流动性、曲率和张力。由于蛋白质识别通常取决于聚糖特异性和膜内 GSL 的组织，因此这些相互作用在体外表征仍然具有挑战性。在这里，我们介绍 FLiPA（荧光脂质体板测定），这是一种利用荧光琼脂糖包埋的巨型脂质体对蛋白质-GSL 相互作用进行定量分析的多功能方法。
- Abstract: Interactions between proteins and glycosphingolipids (GSLs) regulate various cellular processes and altered GSL metabolism contributes to numerous diseases. The diverse glycan headgroups and ceramide backbones of GSLs shape membrane organisation, fluidity, curvature, and tension. As protein recognition frequently depends on both glycan specificity and the organisation of GSLs within the membrane, these interactions...
- Summary (fallback): 机器翻译摘要显示：蛋白质和鞘糖脂 (GSL) 之间的相互作用调节各种细胞过程，而 GSL 代谢的改变会导致多种疾病。 GSL 的不同聚糖头基和神经酰胺主链塑造膜组织、流动性、曲率和张力。由于蛋白质识别通常取决于聚糖特异性和膜内 GSL 的组织，因此这些相互作用在体外表征仍然具有挑战性。在这里，我们介绍 FLiPA（荧光脂质体板测定），这是一种利用荧光琼脂糖包埋的巨型脂质体对蛋白质-GSL 相互作用进行定量分析的多功能方法。
- Keywords: interactions, membrane, flipa, gsls, versatile

## medrxiv

### 1. [大规模功能测定的临床验证：来自 2,120 项基因真值测定评估的见解](https://www.medrxiv.org/content/10.64898/2026.07.10.26357766v1)
- Original title: Clinical validation of large-scale functional assays: insights from 2,120 gene-truthset-assay evaluations
- Authors: Allen, S., Rowlands, C. F., Kuzbari, Z., Garrett, A., Durkie, M. et al.
- Meta: 2026-07-14 | genetic and genomic medicine | DOI: 10.64898/2026.07.10.26357766
- 中文摘要: 背景：关于如何使用“真相集”变体进行功能测定的临床验证，即确定临床分类的可分配证据点（EP），缺乏明确的指导。有人认为，应该使用错义变体的真值集来验证测定，因为这是分类受功能数据影响最大的变体类型。 EP 将受到可用“真相集”变体的数量及其与测定读数的一致性的影响。方法：我们首先审查了 112 套 ClinGen 基因特异性分类规范 (CSPEC)，以评估他们应用于真值集组装和分析临床验证的方法。然后，我们提出了关于变异类型和分类严格性的不同规则，通过这些规则可以使用 ClinVar 提取的分类来组装真值集。
- Abstract: Background: Clear guidance is lacking regarding how 'truthset' variants should be used for clinical validation of functional assays, namely determining the allocatable evidence points (EPs) towards clinical classification. It is argued that assays should be validated using truthsets of missense variants, as this is the variant type for which classification is most impacted by functional data. EPs will be influenced...
- Summary (fallback): 机器翻译摘要显示：背景：关于如何使用“真相集”变体进行功能测定的临床验证，即确定临床分类的可分配证据点（EP），缺乏明确的指导。有人认为，应该使用错义变体的真值集来验证测定，因为这是分类受功能数据影响最大的变体类型。 EP 将受到可用“真相集”变体的数量及其与测定读数的一致性的影响。方法：我们首先审查了 112 套 ClinGen 基因特异性分类规范 (CSPEC)，以评估他们应用于真值集组装和分析临床验证的方法。然后，我们提出了关于变异类型和分类严格性的不同规则，通过这些规则可以使用 ClinVar 提取的分类来组装真值集。
- Keywords: clinical, truthsets, variants, validation, truthset

### 2. [内分泌-代谢网络结构揭示了多囊卵巢综合征的关键桥梁生物标志物](https://www.medrxiv.org/content/10.64898/2026.07.10.26357756v1)
- Original title: Endocrine - metabolic network architecture reveals key bridge biomarkers in polycystic ovary syndrome
- Authors: Piorkowska, N. J., Franik, G., Bizon, A.
- Meta: 2026-07-14 | endocrinology | DOI: 10.64898/2026.07.10.26357756
- 中文摘要: 背景：多囊卵巢综合征 (PCOS) 是一种异质性内分泌疾病，涉及内分泌、代谢、炎症和甲状腺途径之间复杂的相互作用。然而，这些交互的系统级组织仍然知之甚少。目的：重建 PCOS 女性的内分泌代谢生物标志物网络，并识别整合不同生理领域的桥接生物标志物。设计：回顾性横断面研究。设置：单一三级转诊中心。参与者：根据修订后的鹿特丹标准，共有 1,286 名被诊断患有 PCOS 的女性。方法：分析了代表内分泌、代谢、血液/炎症和甲状腺领域的 29 种常规测量的实验室生物标志物。使用具有扩展贝叶斯信息准则模型选择的图形 LASSO 来估计稀疏高斯图形模型...
- Abstract: Context: Polycystic ovary syndrome (PCOS) is a heterogeneous endocrine disorder involving complex interactions among endocrine, metabolic, inflammatory, and thyroid pathways. However, the systems-level organization of these interactions remains poorly understood. Objective: To reconstruct the endocrine-metabolic biomarker network in women with PCOS and identify bridge biomarkers integrating distinct physiological do...
- Summary (fallback): 机器翻译摘要显示：背景：多囊卵巢综合征 (PCOS) 是一种异质性内分泌疾病，涉及内分泌、代谢、炎症和甲状腺途径之间复杂的相互作用。然而，这些交互的系统级组织仍然知之甚少。目的：重建 PCOS 女性的内分泌代谢生物标志物网络，并识别整合不同生理领域的桥接生物标志物。设计：回顾性横断面研究。设置：单一三级转诊中心。参与者：根据修订后的鹿特丹标准，共有 1,286 名被诊断患有 PCOS 的女性。方法：分析了代表内分泌、代谢、血液/炎症和甲状腺领域的 29 种常规测量的实验室生物标志物。使用具有扩展贝叶斯信息准则模型选择的图形 LASSO 来估计稀疏高斯图形模型...
- Keywords: biomarkers, network, bridge, pcos, endocrine

### 3. [无家可归者旅馆流感疫苗接种的数学模型](https://www.medrxiv.org/content/10.64898/2026.07.10.26357528v1)
- Original title: Mathematical models for influenza vaccination in homeless hostels
- Authors: Xu, J., Hutchinson, N., House, T., Pellis, L., Hayward, A. et al.
- Meta: 2026-07-14 | epidemiology | DOI: 10.64898/2026.07.10.26357528
- 中文摘要: 本文的目的是对无家可归者的住宿环境进行建模，以调查疫苗接种如何缓解疫情，强调疫苗接种在脆弱环境中的重要性。我们估算了与更广泛社区的每日人均接触率、内部传播率以及所实现的疫苗覆盖率。我们对考虑内部和外部传播选择的疾病爆发的最终规模进行随机模拟。我们的结论是，有效减少传播的疫苗将减轻无家可归者旅馆的疫情爆发，但当家庭人口疫苗接种覆盖率较高时，效果会更好，从卫生经济角度来看，这可能会导致更多成本。
- Abstract: The aim of this paper is to model homeless accommodation settings to investigate how vaccination mitigates the outbreaks, highlighting the importance of vaccination in vulnerable settings. We estimate the daily per capita contact rate with wider community, the internal transmission rate, and the achieved vaccine coverage. We present stochastic simulation of the final size of disease outbreaks given choices of intern...
- Summary (fallback): 机器翻译摘要显示：本文的目的是对无家可归者的住宿环境进行建模，以调查疫苗接种如何缓解疫情，强调疫苗接种在脆弱环境中的重要性。我们估算了与更广泛社区的每日人均接触率、内部传播率以及所实现的疫苗覆盖率。我们对考虑内部和外部传播选择的疾病爆发的最终规模进行随机模拟。我们的结论是，有效减少传播的疫苗将减轻无家可归者旅馆的疫情爆发，但当家庭人口疫苗接种覆盖率较高时，效果会更好，从卫生经济角度来看，这可能会导致更多成本。
- Keywords: vaccination, homeless, transmission, hostels, settings

### 4. [设置和诊断算法对南非有症状和无症状结核病患者疾病严重程度的影响](https://www.medrxiv.org/content/10.64898/2026.07.10.26357755v1)
- Original title: Influence of setting and diagnostic algorithm on disease severity among people diagnosed with symptomatic and asymptomatic tuberculosis in South Africa
- Authors: McCreesh, N., Govender, I., Sithole, M., Wong, E. B., Buthelezi, I. et al.
- Meta: 2026-07-14 | epidemiology | DOI: 10.64898/2026.07.10.26357755
- 中文摘要: 背景 人们对结核病 (TB) 社区筛查和无症状结核病 (aTB) 检测越来越感兴趣。我们探讨了设置和筛查方法如何影响报告的症状与潜在疾病严重程度和传染性之间的关系。方法 我们比较了通过社区调查诊断为 aTB 或有症状结核病 (sTB) 的人群以及在同一南非社区诊所诊断为 aTB 或 sTB 的人群中的结核病严重程度和传染性标志物（计算机辅助检测 [CAD、CAD4TBv5] 评分，源自胸部 Xpert MTB/RIF Ultra 结果以及微量与超微量 Xpert MTB/RIF Ultra 结果）。我们评估了筛查算法的变化如何影响社区诊断的 aTB 与 sTB 的相对严重程度，并估计了不符合调查条件的人群（CAD 评分 <25 并且没有报告症状）的结核病患病率和严重程度。
- Abstract: Background There is growing interest in tuberculosis (TB) community screening and detection of asymptomatic TB (aTB). We explored how setting and screening approach influence the relationship between reported symptoms and underlying disease severity and infectiousness. Methods We compared markers of TB severity and infectiousness (computer-aided detection [CAD, CAD4TBv5] scores derived from chest radiographs and tra...
- Summary (fallback): 机器翻译摘要显示：背景 人们对结核病 (TB) 社区筛查和无症状结核病 (aTB) 检测越来越感兴趣。我们探讨了设置和筛查方法如何影响报告的症状与潜在疾病严重程度和传染性之间的关系。方法 我们比较了通过社区调查诊断为 aTB 或有症状结核病 (sTB) 的人群以及在同一南非社区诊所诊断为 aTB 或 sTB 的人群中的结核病严重程度和传染性标志物（计算机辅助检测 [CAD、CAD4TBv5] 评分，源自胸部 Xpert MTB/RIF Ultra 结果以及微量与超微量 Xpert MTB/RIF Ultra 结果）。我们评估了筛查算法的变化如何影响社区诊断的 aTB 与 sTB 的相对严重程度，并估计了不符合调查条件的人群（CAD 评分 <25 并且没有报告症状）的结核病患病率和严重程度。
- Keywords: people, severity, community, screening, influence

### 5. [人工智能聊天机器人在有生活经验的成年人中提供心理健康支持的使用和看法](https://www.medrxiv.org/content/10.64898/2026.07.11.26357785v1)
- Original title: Use and Perceptions of AI Chatbots for Mental Health Support Among Adults with Lived Experience
- Authors: Notsu, H., Nguyen, P. A., Flathers, M., Ryan, S. J., Noorily, J. et al.
- Meta: 2026-07-14 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.11.26357785
- 中文摘要: 重要性：人工智能聊天机器人越来越多地用于心理健康支持，但人们对有心理健康状况生活经验的成年人如何使用和感知这些工具知之甚少。目标：描述与美国大型心理健康组织有联系的成年人对人工智能聊天机器人的使用和感知，包括出于心理健康目的。设计：2026 年 3 月至 5 月进行的横断面在线调查。背景：通过美国最大的草根心理健康组织国家精神疾病联盟 (NAMI) 的电子邮件通讯招募的成年人。参与者：年满 18 岁、具有英语水平的成年人。不需要加入 NAMI 或诊断为精神健康障碍。结果：在 454 名参与者中，316 名 (69.6%) 表示曾使用过人工智能聊天机器人。
- Abstract: Importance: AI chatbots are increasingly used for mental health support, but little is known about how adults with lived experience of mental health condition use and perceive these tools. Objective: To characterize the use and perception of AI chatbots, including for mental health purposes, among adults connected to a large US mental health organization. Design: Cross-sectional online survey conducted from March to...
- Summary (fallback): 机器翻译摘要显示：重要性：人工智能聊天机器人越来越多地用于心理健康支持，但人们对有心理健康状况生活经验的成年人如何使用和感知这些工具知之甚少。目标：描述与美国大型心理健康组织有联系的成年人对人工智能聊天机器人的使用和感知，包括出于心理健康目的。设计：2026 年 3 月至 5 月进行的横断面在线调查。背景：通过美国最大的草根心理健康组织国家精神疾病联盟 (NAMI) 的电子邮件通讯招募的成年人。参与者：年满 18 岁、具有英语水平的成年人。不需要加入 NAMI 或诊断为精神健康障碍。结果：在 454 名参与者中，316 名 (69.6%) 表示曾使用过人工智能聊天机器人。
- Keywords: mental, health, adults, chatbots, participants

### 6. [相对于临床医生，对话轨迹降低了大语言模型对自杀意念的检测：一项预先注册的研究](https://www.medrxiv.org/content/10.64898/2026.07.10.26357132v1)
- Original title: Conversational trajectory degrades large language model detection of suicidal ideation relative to clinicians: a preregistered study
- Authors: Kalinich, M., Luccarelli, J., Santa Maria, J., Flathers, M., Nguyen, A. et al.
- Meta: 2026-07-14 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.10.26357132
- 中文摘要: 背景 通用大型语言模型越来越多地遇到情感和类似治疗的对话，但并未作为临床系统进行开发或评估。现有的安全评估在很大程度上依赖于简短的交流，尽管危害往往会在长期的互动中显现出来。随着对话积累上下文，模型是否保持安全相关的性能仍然未知。方法 在这项预先注册的研究中，在 5 个心理治疗和 3 个合成转录本中，在 0-200 个发言者轮流中插入了 400 份经过临床医生验证的陈述，无论是否有自杀意念。 49 名法学硕士和 8 名临床医生执行了相同的二元分类任务。混合效应模型估计了对话深度、模型规模和模型版本对 F1 的影响。在有或没有指令重述的情况下，对 12 个顶级模型进行了 1,500 次对话轨迹的测试。
- Abstract: Background General-purpose large language models increasingly encounter emotional and therapy-like conversation, yet are not developed or evaluated as clinical systems. Existing safety evaluations rely largely on brief exchanges, although harms often unfold over extended interactions. Whether models maintain safety-relevant performance as conversations accumulate context remains unknown. Methods In this preregistere...
- Summary (fallback): 机器翻译摘要显示：背景 通用大型语言模型越来越多地遇到情感和类似治疗的对话，但并未作为临床系统进行开发或评估。现有的安全评估在很大程度上依赖于简短的交流，尽管危害往往会在长期的互动中显现出来。随着对话积累上下文，模型是否保持安全相关的性能仍然未知。方法 在这项预先注册的研究中，在 5 个心理治疗和 3 个合成转录本中，在 0-200 个发言者轮流中插入了 400 份经过临床医生验证的陈述，无论是否有自杀意念。 49 名法学硕士和 8 名临床医生执行了相同的二元分类任务。混合效应模型估计了对话深度、模型规模和模型版本对 F1 的影响。在有或没有指令重述的情况下，对 12 个顶级模型进行了 1,500 次对话轨迹的测试。
- Keywords: models, conversational, performance, model, clinicians

### 7. [用于脊髓损伤个体局部骨刺激的可穿戴纳米振动传递装置的开发和初步临床可行性](https://www.medrxiv.org/content/10.64898/2026.07.09.26357644v1)
- Original title: Development and Preliminary Clinical Feasibility of a Wearable Nanovibration Delivery Device for Localised Bone Stimulation in Individuals with Spinal Cord Injury
- Authors: Williams, J., Gibson, R., Campsie, P., Dalby, M. J., Riddell, J. S. et al.
- Meta: 2026-07-14 | rehabilitation medicine and physical therapy | DOI: 10.64898/2026.07.09.26357644
- 中文摘要: 脊髓损伤 (SCI) 会导致瘫痪下肢快速而严重的骨质流失，尤其是股骨远端和胫骨近端，这些部位发生脆性骨折的风险很高。 1 kHz 的体外纳米级振动已被证明可以促进成骨分化并抑制破骨细胞生成，这表明具有作为有针对性的机械干预的潜力。本研究旨在开发和评估一种可穿戴设备，用于在 SCI 患者的股骨远端传递和监测局部纳米振动。该设备通过骨传导传感器以 1 kHz 的频率提供连续的正弦纳米级刺激，并使用反向加速度计来实时监测传输的振动。通过比较股骨远端、胫骨近端和胫骨远端的两项健康志愿者调查，改进了设计和目标部位选择。
- Abstract: Spinal cord injury (SCI) causes rapid and severe bone loss in the paralysed lower limbs, particularly at the distal femur and proximal tibia, where fragility fracture risk is high. In vitro nanoscale vibration at 1 kHz has been shown to promote osteogenic differentiation and inhibit osteoclastogenesis, suggesting potential as a targeted mechanical intervention. This study aimed to develop and evaluate a wearable dev...
- Summary (fallback): 机器翻译摘要显示：脊髓损伤 (SCI) 会导致瘫痪下肢快速而严重的骨质流失，尤其是股骨远端和胫骨近端，这些部位发生脆性骨折的风险很高。 1 kHz 的体外纳米级振动已被证明可以促进成骨分化并抑制破骨细胞生成，这表明具有作为有针对性的机械干预的潜力。本研究旨在开发和评估一种可穿戴设备，用于在 SCI 患者的股骨远端传递和监测局部纳米振动。该设备通过骨传导传感器以 1 kHz 的频率提供连续的正弦纳米级刺激，并使用反向加速度计来实时监测传输的振动。通过比较股骨远端、胫骨近端和胫骨远端的两项健康志愿者调查，改进了设计和目标部位选择。
- Keywords: femur, vibration, distal, feasibility, device
