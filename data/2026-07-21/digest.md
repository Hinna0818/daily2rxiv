# daily2rxiv Digest - 2026-07-21

共收录 68 篇论文。

## arxiv

### 1. [视觉相似性的多种感觉：文本提示的图像感知度量](https://arxiv.org/abs/2607.18237v1)
- Original title: The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric
- Authors: Sheng-Yu Wang, Yotam Nitzan, Aaron Hertzmann, Jun-Yan Zhu, Eli Shechtman et al.
- Meta: 2026-07-20 | cs.CV
- 中文摘要: 人类视觉相似性判断是依赖于上下文的。例如，两个图像可能形状相似但颜色不同。然而，现有的感知相似性度量将这些细微差别压缩为单个标量值，没有提供针对特定方面的条件的机制。为了弥补这一差距，我们引入了人类对图像三元组相似性判断的大规模数据集，其中每个三元组都在相似性的多个自由形式语义方面进行了注释。对广泛的前沿视觉语言模型（VLM）进行基准测试表明，与人类注释者的共识相比，存在相当大的性能差距。利用我们的数据，我们微调 VLM 以生成文本提示图像感知相似度 (TPIPS) 指标，根据指定的文本提示捕获视觉相似度的多种感觉。
- Abstract: Human visual similarity judgments are context-dependent. For example, two images may be similar in shape but distinct in color. Existing perceptual similarity metrics, however, collapse these nuances into a single scalar value, offering no mechanism to condition on specific aspects. To bridge this gap, we introduce a large-scale dataset of human similarity judgments over image triplets, where each triplet is annotat...
- Summary (fallback): 机器翻译摘要显示：人类视觉相似性判断是依赖于上下文的。例如，两个图像可能形状相似但颜色不同。然而，现有的感知相似性度量将这些细微差别压缩为单个标量值，没有提供针对特定方面的条件的机制。为了弥补这一差距，我们引入了人类对图像三元组相似性判断的大规模数据集，其中每个三元组都在相似性的多个自由形式语义方面进行了注释。对广泛的前沿视觉语言模型（VLM）进行基准测试表明，与人类注释者的共识相比，存在相当大的性能差距。利用我们的数据，我们微调 VLM 以生成文本提示图像感知相似度 (TPIPS) 指标，根据指定的文本提示捕获视觉相似度的多种感觉。
- Keywords: similarity, human, tpips, visual, image

### 2. [补丁策略：通过密集的视觉表示进行有效的具体控制](https://arxiv.org/abs/2607.18236v1)
- Original title: Patch Policy: Efficient Embodied Control via Dense Visual Representations
- Authors: Gaoyue Zhou, Zichen Jeff Cui, Ada Langford, Bowen Tan, Yann LeCun et al.
- Meta: 2026-07-20 | cs.RO
- 中文摘要: 视觉变压器 (ViT) 的预训练密集视觉特征功能强大，但在机器人学习中尚未得到充分利用。现代机器人策略要么将每个观察结果压缩为单个全局标记，要么依赖于从头开始训练的视觉主干，从而牺牲了细粒度的空间细节和大规模视觉预训练的好处。虽然存在确实对大型视觉语言动作模型（VLA）等密集补丁特征进行操作的策略，但它们往往笨重且缓慢，继承了十亿参数视觉语言模型（VLM）主干的全部成本。我们通过补丁策略缩小了这一差距，这是一种最小的架构扩展，使基于变压器的策略能够直接使用密集的预训练补丁令牌，而无需完整 VLM 的计算开销。
- Abstract: Pretrained dense visual features from Vision Transformers (ViTs) are powerful yet have been underutilized in robot learning. Modern robot policies either compress each observation into a single global token, or rely on visual backbones trained from scratch, sacrificing both fine-grained spatial detail and the benefits of large-scale visual pre-training. While there exist policies that do operate on dense patch featu...
- Summary (fallback): 机器翻译摘要显示：视觉变压器 (ViT) 的预训练密集视觉特征功能强大，但在机器人学习中尚未得到充分利用。现代机器人策略要么将每个观察结果压缩为单个全局标记，要么依赖于从头开始训练的视觉主干，从而牺牲了细粒度的空间细节和大规模视觉预训练的好处。虽然存在确实对大型视觉语言动作模型（VLA）等密集补丁特征进行操作的策略，但它们往往笨重且缓慢，继承了十亿参数视觉语言模型（VLM）主干的全部成本。我们通过补丁策略缩小了这一差距，这是一种最小的架构扩展，使基于变压器的策略能够直接使用密集的预训练补丁令牌，而无需完整 VLM 的计算开销。
- Keywords: patch, visual, policies, policy, dense

### 3. [不规则时间序列的因果发现](https://arxiv.org/abs/2607.18226v1)
- Original title: Causal Discovery on Irregular Time Series
- Authors: Martim Penim, Ricardo Ribeiro Pereira, Jacopo Bono, Hugo Ferreira, Mário A. T. Figueiredo et al.
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 因果发现方法在时间系统中表现出了强大的性能，但它们通常依赖于规则和离散的滞后结构，限制了它们对规则采样数据的适用性。然而，许多现实世界的任务需要处理不规则采样的事件流，例如传感器流、医疗数据和金融交易。在这项工作中，我们提出了 PCMCI+ 的扩展，这是一种在规则多元时间序列上进行因果发现的最先进方法，以允许处理不规则时间序列。我们的方法不是通过固定滞后依赖性来建模因果关系，而是聚合预定义时间窗口上的因果影响。
- Abstract: Causal discovery methods have shown strong performance in temporal systems, but they typically rely on regular and discrete lag structures, limiting their applicability to regularly sampled data. However, many real-world tasks require dealing with irregularly sampled streams of events, such as sensor streams, healthcare data, and financial transactions. In this work, we propose an extension of PCMCI+, a state-of-the...
- Summary (fallback): 机器翻译摘要显示：因果发现方法在时间系统中表现出了强大的性能，但它们通常依赖于规则和离散的滞后结构，限制了它们对规则采样数据的适用性。然而，许多现实世界的任务需要处理不规则采样的事件流，例如传感器流、医疗数据和金融交易。在这项工作中，我们提出了 PCMCI+ 的扩展，这是一种在规则多元时间序列上进行因果发现的最先进方法，以允许处理不规则时间序列。我们的方法不是通过固定滞后依赖性来建模因果关系，而是聚合预定义时间窗口上的因果影响。
- Keywords: causal, discovery, irregular, time, series

### 4. [向量搜索作为最近邻匹配：因果推理中基于 RAG 的策略学习](https://arxiv.org/abs/2607.18225v1)
- Original title: Vector Search As Nearest Neighbor Matching: RAG-based Policy Learning in Causal Inference
- Authors: Masahiro Kato, Taka Kato
- Meta: 2026-07-20 | econ.EM
- 中文摘要: 我们提出了利用检索增强生成（RAG）进行策略学习的一步法和两步法。我们在潜在结果框架下制定基于 RAG 的行动选择。在两步方法中，向量搜索在嵌入空间中检索特定于动作的相邻证据，生成器估计条件预期结果或其对比，并且插件规则选择动作。该公式将特定动作向量搜索与因果推理中的最近邻匹配联系起来。我们将两步方法的遗憾分解为候选生成遗憾和候选内选择遗憾，并使用最近邻估计器和变换器的预测误差保证来限制后者。我们直接将一步法作为一种策略进行评估，因为它的中间计算是不可观察的。
- Abstract: We propose one-step and two-step methods for policy learning with retrieval-augmented generation (RAG). We formulate RAG-based action selection under the potential outcome framework. In the two-step method, vector search retrieves action-specific neighboring evidence in an embedding space, the generator estimates conditional expected outcomes or their contrasts, and a plug-in rule selects an action. This formulation...
- Summary (fallback): 机器翻译摘要显示：我们提出了利用检索增强生成（RAG）进行策略学习的一步法和两步法。我们在潜在结果框架下制定基于 RAG 的行动选择。在两步方法中，向量搜索在嵌入空间中检索特定于动作的相邻证据，生成器估计条件预期结果或其对比，并且插件规则选择动作。该公式将特定动作向量搜索与因果推理中的最近邻匹配联系起来。我们将两步方法的遗憾分解为候选生成遗憾和候选内选择遗憾，并使用最近邻估计器和变换器的预测误差保证来限制后者。我们直接将一步法作为一种策略进行评估，因为它的中间计算是不可观察的。
- Keywords: vector, search, policy, two-step, method

### 5. [GigaPath-Flash 和 GigaTIME-Flash：用于全玻片和肿瘤微环境分析的高效病理学基础模型](https://arxiv.org/abs/2607.18218v1)
- Original title: GigaPath-Flash and GigaTIME-Flash: Efficient Pathology Foundation Models for Whole-Slide and Tumor Microenvironment Analysis
- Authors: Naoto Usuyama, Jeya Maria Jose Valanarasu, Sicong Yao, Hanwen Xu, Jaspreet Bagga et al.
- Meta: 2026-07-20 | cs.CV
- 中文摘要: 基础模型已成为计算病理学的驱动力，有可能通过从大规模组织病理学数据中学习可转移的表示来改变癌症诊断、预后和治疗选择。病理学基础模型的不断发展现在涵盖了不同的数据源、架构和下游应用程序。然而，大多数预训练模型仅在图像图块级别运行，使用限制性许可，并且计算成本仍然很高，限制了大规模幻灯片级别的临床和研究使用。在这里，我们介绍 GigaPath-Flash 和 GigaTIME-Flash，这是用于全玻片病理学 AI 和空间蛋白质组学预测的高效模型。 GigaPath-Flash 将 22M 参数的 ViT-S 平铺编码器与 21M 参数的 LongNet 滑动编码器相结合，两者都经过大规模真实世界组织病理学数据的预训练。
- Abstract: Foundation models have emerged as a driving force in computational pathology, with the potential to transform cancer diagnosis, prognosis, and treatment selection by learning transferable representations from large-scale histopathology data. A growing landscape of pathology foundation models now spans diverse data sources, architectures, and downstream applications. However, most pretrained models operate only at th...
- Summary (fallback): 机器翻译摘要显示：基础模型已成为计算病理学的驱动力，有可能通过从大规模组织病理学数据中学习可转移的表示来改变癌症诊断、预后和治疗选择。病理学基础模型的不断发展现在涵盖了不同的数据源、架构和下游应用程序。然而，大多数预训练模型仅在图像图块级别运行，使用限制性许可，并且计算成本仍然很高，限制了大规模幻灯片级别的临床和研究使用。在这里，我们介绍 GigaPath-Flash 和 GigaTIME-Flash，这是用于全玻片病理学 AI 和空间蛋白质组学预测的高效模型。 GigaPath-Flash 将 22M 参数的 ViT-S 平铺编码器与 21M 参数的 LongNet 滑动编码器相结合，两者都经过大规模真实世界组织病理学数据的预训练。
- Keywords: models, pathology, gigapath-flash, large-scale, gigatime-flash

### 6. [通过 ATLAS 揭示异构环境中不变和可转移的潜在因子](https://arxiv.org/abs/2607.18209v1)
- Original title: Unveiling Invariant and Transferable Latent Factors Across Heterogeneous Environments via ATLAS
- Authors: Yihong Gu, Katherine Liao, Tianxi Cai
- Meta: 2026-07-20 | math.ST
- 中文摘要: 本文考虑了一种多环境因素模型，其中从异构环境中收集高维协变量，并在这些环境的子集中提供辅助标签。协变量的联合分布可能因环境而异，而潜在结构被分解为具有共享载荷的不变因子和具有环境特定载荷的异质因子。这样的模型是由迁移学习和潜在因子回归驱动的，其中人们寻求稳定的低维表示来解释和响应 $Y$ 的稳健样本外预测。利用不变性原理，我们证明了不变性和异质性因素在最小结构条件下是解开的。
- Abstract: This paper considers a multi-environment factor model in which high-dimensional covariates are collected from heterogeneous environments, with auxiliary labels available in a subset of these environments. The joint distribution of the covariates may vary across environments, whereas the latent structure is decomposed into invariant factors with shared loadings and heterogeneous factors with environment-specific load...
- Summary (fallback): 机器翻译摘要显示：本文考虑了一种多环境因素模型，其中从异构环境中收集高维协变量，并在这些环境的子集中提供辅助标签。协变量的联合分布可能因环境而异，而潜在结构被分解为具有共享载荷的不变因子和具有环境特定载荷的异质因子。这样的模型是由迁移学习和潜在因子回归驱动的，其中人们寻求稳定的低维表示来解释和响应 $Y$ 的稳健样本外预测。利用不变性原理，我们证明了不变性和异质性因素在最小结构条件下是解开的。
- Keywords: factors, heterogeneous, invariant, latent, environments

### 7. [PPL-Factory：从语言建模到推理的任务感知和预算感知数据选择](https://arxiv.org/abs/2607.18199v1)
- Original title: PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning
- Authors: Hang Zhang, Warren J. Gross
- Meta: 2026-07-20 | cs.CL
- 中文摘要: 并非所有训练样本对大型语言模型微调的贡献都相同。选择信息丰富的训练样本可以降低计算成本，同时保持下游性能。许多现有的数据选择方法依赖于间接启发法，例如数据质量、多样性或推理轨迹长度。然而，这些固定标准的有效性取决于任务，并且难以在不同的下游任务中推广。基于困惑度的数据选择提供了一种简单且模型感知的解决方案来估计样本难度，但现有方法通常对整个训练序列进行评分，并忽略语言建模和推理任务的学习目标的差异。在本文中，我们提出了 PPL-Factory，这是一种简单且可解释的数据选择框架，它结合了任务感知的基于困惑的分数和数据预算感知的选择标准......
- Abstract: Not all training samples contribute equally to large language model fine-tuning. Selecting informative training samples can reduce the computational cost while preserving downstream performance. Many existing data selection methods rely on indirect heuristics, such as data quality, diversity or reasoning trace length. However, the effectiveness of these fixed criteria is task-dependent and difficult to generalize ac...
- Summary (fallback): 机器翻译摘要显示：并非所有训练样本对大型语言模型微调的贡献都相同。选择信息丰富的训练样本可以降低计算成本，同时保持下游性能。许多现有的数据选择方法依赖于间接启发法，例如数据质量、多样性或推理轨迹长度。然而，这些固定标准的有效性取决于任务，并且难以在不同的下游任务中推广。基于困惑度的数据选择提供了一种简单且模型感知的解决方案来估计样本难度，但现有方法通常对整个训练序列进行评分，并忽略语言建模和推理任务的学习目标的差异。在本文中，我们提出了 PPL-Factory，这是一种简单且可解释的数据选择框架，它结合了任务感知的基于困惑的分数和数据预算感知的选择标准......
- Keywords: selection, ppl-factory, training, task-aware, budget-aware

### 8. [用于生成建模的三体散射](https://arxiv.org/abs/2607.18198v1)
- Original title: Three-Body Scattering for Generative Modeling
- Authors: Peng Sun, Zhenglin Cheng, Deyuan Liu, Jun Xie, Xinyi Shang et al.
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 现代生成模型通常依赖于对抗性批评家、规定的噪声到数据路径或自回归分解。相反，我们证明适当的分布能量可以引起样本级运动，并为一步生成器提供直接回归监督。用于生成的三体散射建模 (TBSM) 将能量距离转化为恒定大小的每个射弹相互作用：每个射弹被一个真实源吸引，并被一个独立生成的源排斥。以射弹及其条件为条件，其期望等于 $\frac12D_E^2(P_θ,Q)$ 的 $2$-Wasserstein 梯度流速。一批 $B$ 冻结目标事件会产生 $O(B)$ 样本级损失，每个损失都使用一个参考作为其条件，而不是漂移模型等方法使用的小批量范围的全对字段。
- Abstract: Modern generative models typically rely on an adversarial critic, a prescribed noise-to-data path, or an autoregressive factorization. Instead, we show that a proper distributional energy can induce sample-level motion and provide direct regression supervision for a one-step generator. Three-Body Scattering Modeling (TBSM) for generation turns the energy distance into a constant-size per-projectile interaction: each...
- Summary (fallback): 机器翻译摘要显示：现代生成模型通常依赖于对抗性批评家、规定的噪声到数据路径或自回归分解。相反，我们证明适当的分布能量可以引起样本级运动，并为一步生成器提供直接回归监督。用于生成的三体散射建模 (TBSM) 将能量距离转化为恒定大小的每个射弹相互作用：每个射弹被一个真实源吸引，并被一个独立生成的源排斥。以射弹及其条件为条件，其期望等于 $\frac12D_E^2(P_θ,Q)$ 的 $2$-Wasserstein 梯度流速。一批 $B$ 冻结目标事件会产生 $O(B)$ 样本级损失，每个损失都使用一个参考作为其条件，而不是漂移模型等方法使用的小批量范围的全对字段。
- Keywords: scattering, one-step, tbsm, three-body, generative

### 9. [卷积扰动认证培训](https://arxiv.org/abs/2607.18195v1)
- Original title: Certified Training for Convolutional Perturbations
- Authors: Benedikt Brückner, Alessio Lomuscio
- Meta: 2026-07-20 | cs.CV
- 中文摘要: 人们发现视觉模型很容易受到扰动，例如运行时由晃动的相机引起的运动模糊。这阻碍了它们在关键应用中的部署，因为视觉轻微模糊等现象可能会导致故障，例如物体检测器丢失物体。虽然数据增强或对抗训练等方法可以提高经验稳健性，但它们缺乏正式的安全保证，因此很难识别和缓解隐藏的漏洞。我们引入了一种新颖的认证训练方法，该方法利用卷积扰动的有效编码来训练可证明稳健的模型。我们的方法显着优于对抗训练，例如，在 CIFAR10 上针对合理强度的运动模糊实现了超过 80% 的鲁棒精度，同时保持了可比较的标准精度。
- Abstract: Vision models have been found to be susceptible to perturbations such as motion blur induced at runtime by a shaking camera. This impedes their deployment in critical applications since phenomena such as slightly blurred vision might lead to failures, for example an object detector missing objects. While methods such as data augmentation or Adversarial Training can improve empirical robustness, they lack formal safe...
- Summary (fallback): 机器翻译摘要显示：人们发现视觉模型很容易受到扰动，例如运行时由晃动的相机引起的运动模糊。这阻碍了它们在关键应用中的部署，因为视觉轻微模糊等现象可能会导致故障，例如物体检测器丢失物体。虽然数据增强或对抗训练等方法可以提高经验稳健性，但它们缺乏正式的安全保证，因此很难识别和缓解隐藏的漏洞。我们引入了一种新颖的认证训练方法，该方法利用卷积扰动的有效编码来训练可证明稳健的模型。我们的方法显着优于对抗训练，例如，在 CIFAR10 上针对合理强度的运动模糊实现了超过 80% 的鲁棒精度，同时保持了可比较的标准精度。
- Keywords: training, perturbations, such, certified, convolutional

### 10. [EVOLVE：在跨域数据库上使用可变速率编码进行高效的学习卷压缩](https://arxiv.org/abs/2607.18187v1)
- Original title: EVOLVE: Efficient Learned Volume Compression with Variable-Rate Encoding on a Cross-Domain Database
- Authors: Kaiyuan Tang, Maizhe Yang, Chaoli Wang
- Meta: 2026-07-20 | cs.GR
- 中文摘要: 大规模科学模拟生成体积数据的速度远远超过存储和网络带宽的进步，这使得有效的有损压缩变得越来越重要。然而，传统的压缩器通常很难在高压缩比 (CR) 下保留精细的结构细节，而隐式神经表示 (INR) 需要昂贵的每卷优化并生成具有固定 CR 的模型。为此，我们推出了 EVOLVE，这是一种基于自动编码器 (AE) 的体积压缩框架，旨在实现离线压缩的高 CR，具有三个关键贡献。首先，我们构建了一个包含来自 21 个科学模拟的 6,376 卷的大型跨域数据库，通过感知哈希进行整理以确保多样性，使优化的模型能够提取在所覆盖的科学模拟领域内跨卷进行泛化的特征。
- Abstract: Large-scale scientific simulations generate volumetric data at rates that far outpace advances in storage and network bandwidth, making effective lossy compression increasingly critical. However, conventional compressors often struggle to preserve fine structural details at high compression ratios (CRs), and implicit neural representations (INRs) require costly per-volume optimization and produce models with fixed C...
- Summary (fallback): 机器翻译摘要显示：大规模科学模拟生成体积数据的速度远远超过存储和网络带宽的进步，这使得有效的有损压缩变得越来越重要。然而，传统的压缩器通常很难在高压缩比 (CR) 下保留精细的结构细节，而隐式神经表示 (INR) 需要昂贵的每卷优化并生成具有固定 CR 的模型。为此，我们推出了 EVOLVE，这是一种基于自动编码器 (AE) 的体积压缩框架，旨在实现离线压缩的高 CR，具有三个关键贡献。首先，我们构建了一个包含来自 21 个科学模拟的 6,376 卷的大型跨域数据库，通过感知哈希进行整理以确保多样性，使优化的模型能够提取在所覆盖的科学模拟领域内跨卷进行泛化的特征。
- Keywords: compression, scientific, evolve, compressors, model

### 11. [BCover：基于电子结构的反应感知共价对接评分套件](https://arxiv.org/abs/2607.18177v1)
- Original title: BCover: An Electronic Structure-Based Scoring Suite for Reaction-Aware Covalent Docking
- Authors: Emil Zak, Michał Szczepanik
- Meta: 2026-07-20 | physics.chem-ph
- 中文摘要: 共价虚拟筛选需要根据非共价识别及其采用具有适当反应性弹头的反应能力几何结构的能力对化合物进行排序。在这里，我们介绍了 BCover，一种反应感知评分套件，它将预反应对接与量子化学衍生的配体反应性描述符（蛋白质口袋的静电特性）相结合。使用基于非线性树的评分模型聚合量子化学描述符。 BCover 在 COValid 基准上进行回顾性评估，包括 9 个目标和 10 个反应位点，并与 AutoDock、DOCK6、DOCKovalent、带有 Rosetta 重新评分的 AlphaFold3 以及 AlphaFold3 基于置信度的排名进行比较。 BCover 的平均调整 LogAUC 为 31%（最大值 57%），平均 ROC-AUC 为 0.88（最大值 0.96），平均 EF1 为 18（最大值 33）。
- Abstract: Covalent virtual screening requires ranking compounds according to both noncovalent recognition and their ability to adopt a reaction-competent geometry with an appropriately reactive warhead. Here, we introduce BCover, a reaction-aware scoring suite that combines pre-reactive docking with quantum-chemistry-derived ligand reactivity descriptors, the electrostatic properties of the protein pocket. Quantum-chemical de...
- Summary (fallback): 机器翻译摘要显示：共价虚拟筛选需要根据非共价识别及其采用具有适当反应性弹头的反应能力几何结构的能力对化合物进行排序。在这里，我们介绍了 BCover，一种反应感知评分套件，它将预反应对接与量子化学衍生的配体反应性描述符（蛋白质口袋的静电特性）相结合。使用基于非线性树的评分模型聚合量子化学描述符。 BCover 在 COValid 基准上进行回顾性评估，包括 9 个目标和 10 个反应位点，并与 AutoDock、DOCK6、DOCKovalent、带有 Rosetta 重新评分的 AlphaFold3 以及 AlphaFold3 基于置信度的排名进行比较。 BCover 的平均调整 LogAUC 为 31%（最大值 57%），平均 ROC-AUC 为 0.88（最大值 0.96），平均 EF1 为 18（最大值 33）。
- Keywords: bcover, average, ligand, scoring, covalent

### 12. [FlashRT：用于指导代理部署实时多模式应用程序的代理线束](https://arxiv.org/abs/2607.18171v1)
- Original title: FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications
- Authors: Krish Agarwal, Zhuoming Chen, Yanyuan Qin, Zhenyu Gu, Atri Rudra et al.
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 实时多模式应用程序（包括语音代理和交互式视频生成）将异构模型组合成管道，其有效部署需要有关放置、流式传输和模型内并行性的特定于应用程序的决策。现有的服务系统和自动并行编译器致力于有限的转换和固定的工作负载假设，因此在新应用程序上实现高性能需要手工设计高效的实现。我们推出了 FlashRT，这是一种代理工具，可指导编码代理将简单的开发人员编写的参考实现提升为优化的多 GPU 部署，从而灵活权衡延迟和吞吐量等目标指标。
- Abstract: Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a ne...
- Summary (fallback): 机器翻译摘要显示：实时多模式应用程序（包括语音代理和交互式视频生成）将异构模型组合成管道，其有效部署需要有关放置、流式传输和模型内并行性的特定于应用程序的决策。现有的服务系统和自动并行编译器致力于有限的转换和固定的工作负载假设，因此在新应用程序上实现高性能需要手工设计高效的实现。我们推出了 FlashRT，这是一种代理工具，可指导编码代理将简单的开发人员编写的参考实现提升为优化的多 GPU 部署，从而灵活权衡延迟和吞吐量等目标指标。
- Keywords: flashrt, agent, latency, agents, multimodal

### 13. [通过鲁棒模型预测控制实现自适应数字孪生的持续验证、更新和决策框架：增材制造案例研究](https://arxiv.org/abs/2607.18164v1)
- Original title: A Continual Validation, Updating, and Decision-Making Framework for Self-Adaptive Digital Twins via Robust Model Predictive Control: A Case Study in Additive Manufacturing
- Authors: Yi-Ping Chen, Ying-Kuan Tsai, Vispi Karkaria, Seul Lee, Daniel Apley et al.
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 数字孪生依靠代理模型来实时反映物理系统，但这些模型可能会随着操作条件的变化而退化，这种现象称为概念漂移。在漂移下保持代理保真度，特别是当模型还必须捕获任意不确定性时，仍然是一个开放的挑战。现有的自适应框架缺乏原则性的机制来检测何时需要更新、根据有限的流数据有效地调整模型以及证明更新确实可以提高预测性能。在这里，我们提出了一个自适应数字孪生框架，它集成了基于 Fisher 评分的多元漂移检测器、用于参数高效持续学习的低秩适应 (LoRA) 以及用于在线统计验证的 Mann-Whitney $U$ 测试。
- Abstract: Digital Twins rely on surrogate models to mirror physical systems in real time, yet these models can degrade as operating conditions evolve, a phenomenon known as concept drift. Maintaining surrogate fidelity under drift, particularly when models must also capture aleatoric uncertainty, remains an open challenge. Existing adaptive frameworks lack principled mechanisms for detecting when updates are needed, for effic...
- Summary (fallback): 机器翻译摘要显示：数字孪生依靠代理模型来实时反映物理系统，但这些模型可能会随着操作条件的变化而退化，这种现象称为概念漂移。在漂移下保持代理保真度，特别是当模型还必须捕获任意不确定性时，仍然是一个开放的挑战。现有的自适应框架缺乏原则性的机制来检测何时需要更新、根据有限的流数据有效地调整模型以及证明更新确实可以提高预测性能。在这里，我们提出了一个自适应数字孪生框架，它集成了基于 Fisher 评分的多元漂移检测器、用于参数高效持续学习的低秩适应 (LoRA) 以及用于在线统计验证的 Mann-Whitney $U$ 测试。
- Keywords: drift, framework, digital, predictive, models

### 14. [或者：用于策略优化的可微信任区域](https://arxiv.org/abs/2607.18163v1)
- Original title: OR Else: A Differentiable Trust Region for Policy Optimization
- Authors: Chinmay Rane, Kanishka Tyagi, Michael Manry
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 这里研究的 PPO 和 GRPO 基线使用修剪的代理目标，其有利方向饱和会导致标量目标导数的突然变化。我们询问输出重置（OR）这种平滑的单边饱和规则是否为大型语言模型训练后提供了一种有用的替代方案。 PPO-OR 和 GRPO-OR 将截断的策略术语替换为推出相对代币对数比率空间中的 OR 平方利润损失；优势符号决定更新方向，并且代币在跨越有利边际后贡献零直接或残差。我们在广义优势估计（GAE）下比较 PPO-clip 与 PPO-OR，以及在群体相对优势下比较 GRPO 与 GRPO-OR，在人类 \texttt{hh-rlhf} 上使用 \texttt{Llama-3.2-1B-Instruct}，每个方法有一个共享奖励模型和三个种子。
- Abstract: PPO and the GRPO baseline studied here use clipped surrogate objectives whose favorable-direction saturation introduces an abrupt change in the scalar objective's derivative. We ask whether Output Reset (OR), a smooth one-sided saturation rule, offers a useful alternative for large language model post-training. PPO-OR and GRPO-OR replace the clipped policy term with an OR squared-margin loss in rollout-relative toke...
- Summary (fallback): 机器翻译摘要显示：这里研究的 PPO 和 GRPO 基线使用修剪的代理目标，其有利方向饱和会导致标量目标导数的突然变化。我们询问输出重置（OR）这种平滑的单边饱和规则是否为大型语言模型训练后提供了一种有用的替代方案。 PPO-OR 和 GRPO-OR 将截断的策略术语替换为推出相对代币对数比率空间中的 OR 平方利润损失；优势符号决定更新方向，并且代币在跨越有利边际后贡献零直接或残差。我们在广义优势估计（GAE）下比较 PPO-clip 与 PPO-OR，以及在群体相对优势下比较 GRPO 与 GRPO-OR，在人类 \texttt{hh-rlhf} 上使用 \texttt{Llama-3.2-1B-Instruct}，每个方法有一个共享奖励模型和三个种子。
- Keywords: grpo-or, under, grpo, ppo-or, group-relative

### 15. [校准通道确定贝叶斯误差代理：温度引起的失真的精确定律](https://arxiv.org/abs/2607.18162v1)
- Original title: The Calibration Channel Determines the Bayes-Error Proxy: An Exact Law for Temperature-Induced Distortion
- Authors: Shreyas Pradeepkumar Khandale
- Meta: 2026-07-20 | cs.LG
- 中文摘要: Ishida 等人的软标签贝叶斯误差估计 beta(z) = E[min(z, 1-z)]。直接从概率值标签估计二元任务的不可约误差。 Ushio 等人的最新工作。表明当概率不是真正的后验时，该估计器是脆弱的：即使完美校准的软标签也可能产生基本上不准确的估计，并且他们提出等渗校准作为一致的补救措施。我们通过准确描述最广泛使用的事后校准图（温度缩放）如何扭曲代理来补充这一工作。
- Abstract: The soft-label Bayes-error estimator beta(z) = E[min(z, 1-z)] of Ishida et al. estimates the irreducible error of a binary task directly from probability-valued labels. Recent work by Ushio et al. showed that this estimator is fragile when the probabilities are not the true posterior: even perfectly calibrated soft labels can yield a substantially inaccurate estimate, and they propose isotonic calibration as a consi...
- Summary (fallback): 机器翻译摘要显示：Ishida 等人的软标签贝叶斯误差估计 beta(z) = E[min(z, 1-z)]。直接从概率值标签估计二元任务的不可约误差。 Ushio 等人的最新工作。表明当概率不是真正的后验时，该估计器是脆弱的：即使完美校准的软标签也可能产生基本上不准确的估计，并且他们提出等渗校准作为一致的补救措施。我们通过准确描述最广泛使用的事后校准图（温度缩放）如何扭曲代理来补充这一工作。
- Keywords: proxy, calibration, error, temperature, fixed

### 16. [测试具有块覆盖的检索增强生成系统](https://arxiv.org/abs/2607.18155v1)
- Original title: Testing Retrieval-Augmented Generation Systems with Chunk Coverage
- Authors: Jinhan Kim, Samuele Pasini, Paolo Tonella
- Meta: 2026-07-20 | cs.SE
- 中文摘要: 基于检索增强生成（RAG）的系统\脚注{为了简洁起见，基于 RAG 的系统在本文中被称为 RAG 系统。}越来越多地部署在高风险环境中，其中正确的行为不仅取决于语言模型，还取决于在推理时选择外部文档的检索组件。虽然现有的 RAG 评估指标在每个查询的基础上评估检索和生成质量，通常依赖于查询级测试预言，例如参考答案或相关性注释，但它们对测试套件是否充分执行整个系统的检索行为提供的了解有限。在本文中，我们介绍了块覆盖率（CC），这是一种独立于预言机的测试充分性标准，用于测试 RAG 系统的检索组件。
- Abstract: Retrieval-Augmented Generation (RAG)-based systems\footnote{For brevity, RAG-based systems are referred to as RAG systems throughout this paper.} are increasingly deployed in high-stakes settings where correct behaviour depends not only on the language model but also on the retrieval component that selects external documents at inference time. While existing RAG evaluation metrics assess retrieval and generation qua...
- Summary (fallback): 机器翻译摘要显示：基于检索增强生成（RAG）的系统\脚注{为了简洁起见，基于 RAG 的系统在本文中被称为 RAG 系统。}越来越多地部署在高风险环境中，其中正确的行为不仅取决于语言模型，还取决于在推理时选择外部文档的检索组件。虽然现有的 RAG 评估指标在每个查询的基础上评估检索和生成质量，通常依赖于查询级测试预言，例如参考答案或相关性注释，但它们对测试套件是否充分执行整个系统的检索行为提供的了解有限。在本文中，我们介绍了块覆盖率（CC），这是一种独立于预言机的测试充分性标准，用于测试 RAG 系统的检索组件。
- Keywords: retrieval, test, systems, testing, generation

### 17. [用于边缘设备上低延迟 EEG 分类的可微分逻辑门网络](https://arxiv.org/abs/2607.18149v1)
- Original title: Differentiable Logic Gate Networks for Low-Latency EEG Classification on Edge Devices
- Authors: Shyamal Y. Dharia, Stephen D. Smith, Camilo E. Valderrama
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 边缘设备上的实时脑电图分类受到传统神经网络浮点运算的瓶颈。我们研究了可微分逻辑门网络 (Diff-Logic)，将其作为硬件本机替代方案，将模型编译成可通过按位 CPU 运算执行的纯布尔电路。通过跨越两个分类任务、二元痴呆检测和三类情感识别的四个脑电图数据集的严格等参数实验，我们在四个复杂度层（50k-500k 参数）将 Diff-Logic 与匹配容量的多层感知器 (MLP) 和二值化神经网络 (BNN) 基线进行了比较。在痴呆症筛查中，Diff-Logic 的 Macro F1 达到 80.2%，比 MLP 基线高出 6.8%。
- Abstract: Real-time EEG classification on edge devices is bottlenecked by the floating-point arithmetic of conventional neural networks. We investigated Differentiable Logic Gate Networks (Diff-Logic) as a hardware-native alternative that compiles models into pure Boolean circuits executable via bitwise CPU operations. Through rigorous iso-parameter experiments across four EEG datasets spanning two classification tasks, binar...
- Summary (fallback): 机器翻译摘要显示：边缘设备上的实时脑电图分类受到传统神经网络浮点运算的瓶颈。我们研究了可微分逻辑门网络 (Diff-Logic)，将其作为硬件本机替代方案，将模型编译成可通过按位 CPU 运算执行的纯布尔电路。通过跨越两个分类任务、二元痴呆检测和三类情感识别的四个脑电图数据集的严格等参数实验，我们在四个复杂度层（50k-500k 参数）将 Diff-Logic 与匹配容量的多层感知器 (MLP) 和二值化神经网络 (BNN) 基线进行了比较。在痴呆症筛查中，Diff-Logic 的 Macro F1 达到 80.2%，比 MLP 基线高出 6.8%。
- Keywords: diff-logic, times, networks, classification, edge

### 18. [全正矩阵与特征多项式的最高阶系数](https://arxiv.org/abs/2607.18148v1)
- Original title: Totally Positive Matrices and the Highest-Order Coefficients of the Characteristic Polynomial
- Authors: Tiago Closs, Leandro Farina
- Meta: 2026-07-20 | cs.LG | DOI: 10.1016/j.laa.2026.07.003
- 中文摘要: 我们研究了通过特征多项式的最高阶系数可以在多大程度上区分全正矩阵。为了识别信息最丰富的系数，我们还采用了神经网络分类器和特征归因方法。使用由几个结构化全正族（包括正双对角矩阵、范德蒙德矩阵和柯西矩阵的乘积）构建的数据集，我们发现系数 (a_{n-1}、a_{n-2}、a_{n-3}) 已经包含强大的区分信息，用于在维度 5、10 和 30 中区分全正矩阵和非全正矩阵。所得分离明显是非线性的，并且允许利用马哈拉诺比斯椭球体在相应的三维系数空间中进行自然几何描述。
- Abstract: We investigate the extent to which totally positive matrices can be distinguished through the highest-order coefficients of their characteristic polynomials. To identify the most informative coefficients, we also employed neural-network classifiers together with feature-attribution methods. Using datasets built from several structured totally positive families, including products of positive bidiagonal matrices, Van...
- Summary (fallback): 机器翻译摘要显示：我们研究了通过特征多项式的最高阶系数可以在多大程度上区分全正矩阵。为了识别信息最丰富的系数，我们还采用了神经网络分类器和特征归因方法。使用由几个结构化全正族（包括正双对角矩阵、范德蒙德矩阵和柯西矩阵的乘积）构建的数据集，我们发现系数 (a_{n-1}、a_{n-2}、a_{n-3}) 已经包含强大的区分信息，用于在维度 5、10 和 30 中区分全正矩阵和非全正矩阵。所得分离明显是非线性的，并且允许利用马哈拉诺比斯椭球体在相应的三维系数空间中进行自然几何描述。
- Keywords: positive, totally, matrices, coefficients, highest-order

### 19. [语言模型是否梦想着结合分子？空间限制下法学硕士的基准测试](https://arxiv.org/abs/2607.18144v1)
- Original title: Do Language Models Dream of Binding Molecules? Benchmarking LLMs under Spatial Constraints
- Authors: Thomas MacDougall, Maksim Kuznetsov, Roman Schutski, Rim Shayakhmetov, Maxim Malkov et al.
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 基于结构的药物设计 (SBDD) 利用蛋白质靶点的 3D 结构（通常辅以其他空间限制）来生成候选结合分子。虽然扩散模型已成为高质量 3D 分子生成的领先范例，但基于 LLM 的方法正在分子设计中迅速兴起，并在口袋条件分子生成中显示出具有竞争力的性能。然而，它们推理物理和 3D 空间环境的能力在很大程度上尚未得到充分开发。在这项工作中，我们系统地分析了当前的通用法学硕士与已建立的基线（例如专门的扩散模型）相比是否能够应对复杂的 3D 约束。
- Abstract: Structure-based drug design (SBDD) leverages the 3D structure of protein targets, often complemented by other spatial constraints, to generate candidate binding molecules. While diffusion models have dominated as a leading paradigm for high-quality 3D molecule generation, LLM-based methods are rapidly emerging in molecular design and have shown competitive performance in pocket-conditioned molecular generation. Howe...
- Summary (fallback): 机器翻译摘要显示：基于结构的药物设计 (SBDD) 利用蛋白质靶点的 3D 结构（通常辅以其他空间限制）来生成候选结合分子。虽然扩散模型已成为高质量 3D 分子生成的领先范例，但基于 LLM 的方法正在分子设计中迅速兴起，并在口袋条件分子生成中显示出具有竞争力的性能。然而，它们推理物理和 3D 空间环境的能力在很大程度上尚未得到充分开发。在这项工作中，我们系统地分析了当前的通用法学硕士与已建立的基线（例如专门的扩散模型）相比是否能够应对复杂的 3D 约束。
- Keywords: spatial, constraints, generation, models, binding

### 20. [结合医院能力和基于阈值的雾化干预措施的登革热传播数学模型](https://arxiv.org/abs/2607.18140v1)
- Original title: A Mathematical Model of Dengue Transmission Incorporating Hospital Capacity and Threshold-Based Fogging Interventions
- Authors: Dipo Aldila, Joseph Páez Chávez, Aytül Gökçe, Thomas Götz, Burcu Gürbüz
- Meta: 2026-07-20 | math.DS
- 中文摘要: 登革热仍然是热带地区的一个重大公共卫生挑战，反复爆发表明当前的干预策略尚未完全有效。现有的数学模型通常假设医院容量不受限制并持续应用雾化，忽略了强烈影响疾病控制的实际限制。我们开发了一种登革热传播的非光滑常微分方程模型，该模型结合了有限的医院容量和当报告的感染超过可用容量的规定分数时激活的阈值触发雾化策略。该模型展示了三种与流行病学相关的操作制度，反映了随着疫情的发展住院治疗和病媒控制政策的变化。我们建立了无病和地方性平衡的存在和局部稳定性。
- Abstract: Dengue remains a major public health challenge in tropical regions, and recurring outbreaks suggest that current intervention strategies are not yet fully effective. Existing mathematical models typically assume unlimited hospital capacity and continuously applied fogging, neglecting practical constraints that strongly influence disease control. We develop a non-smooth ordinary differential equation model of dengue...
- Summary (fallback): 机器翻译摘要显示：登革热仍然是热带地区的一个重大公共卫生挑战，反复爆发表明当前的干预策略尚未完全有效。现有的数学模型通常假设医院容量不受限制并持续应用雾化，忽略了强烈影响疾病控制的实际限制。我们开发了一种登革热传播的非光滑常微分方程模型，该模型结合了有限的医院容量和当报告的感染超过可用容量的规定分数时激活的阈值触发雾化策略。该模型展示了三种与流行病学相关的操作制度，反映了随着疫情的发展住院治疗和病媒控制政策的变化。我们建立了无病和地方性平衡的存在和局部稳定性。
- Keywords: capacity, hospital, fogging, dengue, model

### 21. [用于参数高效微调的流形约束超连接](https://arxiv.org/abs/2607.18130v1)
- Original title: Manifold-Constrained Hyper-Connections for Parameter-Efficient Finetuning
- Authors: Valentijn Oldenburg, Floris de Kam, Bente Zuijdam, Lieve Eberson, Nicky van Zutphen et al.
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 大多数参数高效微调（PEFT）方法都会调整权重或激活，从而使 Transformer 的关键组件之一保持不变：残差连接。本文研究了流形约束超连接 (mHC)，这是一种残差连接的推广，作为一种新颖的 PEFT 方法，用学习的残差路由模块包裹冻结的 OLMo-2 主干网。我们发现 mHC 可以对冻结的 Transformer 进行微调，但其作用与原始的预训练设置有根本不同：在微调中，将残差混合矩阵固定为同一性通常可以提高性能。作为一种独立的 PEFT 方法，mHC 的性能并不总是优于 LoRA。然而，在匹配的可训练参数预算下，mHC+LoRA 组合改善了语言建模损失，并在 1B 和 7B 规模上显示出任务相关的基准增益。
- Abstract: Most parameter-efficient finetuning (PEFT) methods adapt weights or activations, thus leaving one of the key Transformer components unchanged: residual connections. This paper investigates Manifold-Constrained Hyper-Connections (mHC), a generalisation of residual connections, as a novel PEFT approach, wrapping frozen OLMo-2 backbones with learned residual routing modules. We find that mHC can finetune frozen Transfo...
- Summary (fallback): 机器翻译摘要显示：大多数参数高效微调（PEFT）方法都会调整权重或激活，从而使 Transformer 的关键组件之一保持不变：残差连接。本文研究了流形约束超连接 (mHC)，这是一种残差连接的推广，作为一种新颖的 PEFT 方法，用学习的残差路由模块包裹冻结的 OLMo-2 主干网。我们发现 mHC 可以对冻结的 Transformer 进行微调，但其作用与原始的预训练设置有根本不同：在微调中，将残差混合矩阵固定为同一性通常可以提高性能。作为一种独立的 PEFT 方法，mHC 的性能并不总是优于 LoRA。然而，在匹配的可训练参数预算下，mHC+LoRA 组合改善了语言建模损失，并在 1B 和 7B 规模上显示出任务相关的基准增益。
- Keywords: residual, peft, finetuning, manifold-constrained, hyper-connections

### 22. [ClouDens：用于大规模云系统监控的操作上下文感知异常检测](https://arxiv.org/abs/2607.18127v1)
- Original title: ClouDens: Operational Context-Aware Anomaly Detection for Large-scale Cloud System Monitoring
- Authors: Thu T. H. Doan, Mohammad Saiful Islam, Andriy Miranskyy, Ngoc-Thanh Nguyen, Rogardt Heldal et al.
- Meta: 2026-07-20 | cs.NI
- 中文摘要: 随着云计算基础设施规模和复杂性的快速增长，大规模云系统 (LCS) 的网络监控变得越来越具有挑战性，需要自动化、可靠的异常检测来维持服务可用性。现代濒海战斗舰不断从分布式云服务生成遥测日志，生成捕获系统操作的高维多元时间序列。由于极端的维度、分布式组件之间的复杂依赖关系以及间歇性活动服务的严重稀疏性，在这种情况下检测异常非常困难。
- Abstract: With the rapid growth of cloud computing infrastructures in scale and complexity, network monitoring for Large-scale Cloud Systems (LCSs) has become increasingly challenging, requiring automated and reliable anomaly detection to maintain service availability. Modern LCSs continuously generate telemetry logs from distributed cloud services, producing high-dimensional multivariate time series that capture system opera...
- Summary (fallback): 机器翻译摘要显示：随着云计算基础设施规模和复杂性的快速增长，大规模云系统 (LCS) 的网络监控变得越来越具有挑战性，需要自动化、可靠的异常检测来维持服务可用性。现代濒海战斗舰不断从分布式云服务生成遥测日志，生成捕获系统操作的高维多元时间序列。由于极端的维度、分布式组件之间的复杂依赖关系以及间歇性活动服务的严重稀疏性，在这种情况下检测异常非常困难。
- Keywords: detection, anomaly, telemetry, cloud, cloudens

### 23. [COVAriance 引起的子组公平聚类的公平差距惩罚](https://arxiv.org/abs/2607.18119v1)
- Original title: COVAriance-Induced Fairness Gap Penalty for Subgroup-Fair Clustering
- Authors: Kyungseon Lee, Hankyo Jeong, Kunwoong Kim, Kwanho Lee, Yongdai Kim
- Meta: 2026-07-20 | stat.ML
- 中文摘要: 公平聚类的目的是使聚类分配独立于敏感属性，但是当多个敏感属性共同定义许多子组时，这个目标就变得具有挑战性。在这样的设置中，直接扩展现有的公平聚类算法在计算上是昂贵的或在数值上不稳定，特别是当子组的数量呈指数增长并且某些子组仅包含几个实例时。为了解决这些挑战，我们定义了一个用于聚类的子组公平差距，并导出了一个与该差距完全匹配的基于协方差的代理。然后，我们引入代理的连续松弛，从而实现高效的基于梯度的优化并产生我们提出的算法 COVA-FC。我们还表明，仅子群体公平并不意味着边际公平，并扩展了我们的框架以捕获子群体边际公平差距。
- Abstract: Fair clustering aims to make cluster assignments independent of sensitive attributes, but this goal becomes challenging when multiple sensitive attributes jointly define many subgroups. In such settings, directly extending existing fair clustering algorithms is computationally expensive or numerically unstable, especially when the number of subgroups grows exponentially and some subgroups contain only a few instance...
- Summary (fallback): 机器翻译摘要显示：公平聚类的目的是使聚类分配独立于敏感属性，但是当多个敏感属性共同定义许多子组时，这个目标就变得具有挑战性。在这样的设置中，直接扩展现有的公平聚类算法在计算上是昂贵的或在数值上不稳定，特别是当子组的数量呈指数增长并且某些子组仅包含几个实例时。为了解决这些挑战，我们定义了一个用于聚类的子组公平差距，并导出了一个与该差距完全匹配的基于协方差的代理。然后，我们引入代理的连续松弛，从而实现高效的基于梯度的优化并产生我们提出的算法 COVA-FC。我们还表明，仅子群体公平并不意味着边际公平，并扩展了我们的框架以捕获子群体边际公平差距。
- Keywords: clustering, fairness, subgroups, fair, sensitive

### 24. [对齐调整如何塑造法学硕士中阿谀奉承和相关提示引起的偏差的表示？](https://arxiv.org/abs/2607.18114v1)
- Original title: How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?
- Authors: Prakhar Gupta, Terry Jingchen Zhang, Florent Draye, Bernhard Schölkopf, Zhijing Jin
- Meta: 2026-07-20 | cs.CL
- 中文摘要: 现代法学硕士非常容易受到输入提示的简单非实质性变化的影响：一个随意的提示、一个错误标记的少数例子，或者一个虚假的先前助理轮流经常会翻转原来正确的答案。我们研究了这种敏感性（涵盖阿谀奉承和相关线索引起的偏见）存在于模型内部的何处。在五个模型系列和七种 BCT 偏差类型中，我们从隐藏状态中提取每个偏差方向，并通过三种措施对其进行三角测量：探测、留一数据集转移和因果干预。敏感性很大程度上是通过对齐调整而不是预训练来设置的：预训练的基础模型几乎不会屈服于这些偏差，并且它们的激活除了问题内容之外不携带特定于提示的信号。
- Abstract: Modern LLMs are alarmingly susceptible to surprisingly simple immaterial changes of input prompts: a casual hint, an incorrectly labeled few-shot example, or a fake prior assistant turn often flips an originally correct answer. We study where this susceptibility, spanning sycophancy and related cue-induced biases, lives inside the model. Across five model families and seven BCT bias types, we extract a per-bias dire...
- Summary (fallback): 机器翻译摘要显示：现代法学硕士非常容易受到输入提示的简单非实质性变化的影响：一个随意的提示、一个错误标记的少数例子，或者一个虚假的先前助理轮流经常会翻转原来正确的答案。我们研究了这种敏感性（涵盖阿谀奉承和相关线索引起的偏见）存在于模型内部的何处。在五个模型系列和七种 BCT 偏差类型中，我们从隐藏状态中提取每个偏差方向，并通过三种措施对其进行三角测量：探测、留一数据集转移和因果干预。敏感性很大程度上是通过对齐调整而不是预训练来设置的：预训练的基础模型几乎不会屈服于这些偏差，并且它们的激活除了问题内容之外不携带特定于提示的信号。
- Keywords: biases, bias, alignment, tuning, cue-induced

### 25. [法学硕士作为教练：针对不可验证任务的体验式学习](https://arxiv.org/abs/2607.18110v1)
- Original title: LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks
- Authors: Tianzhu Ye, Li Dong, Guanheng Chen, He Zhu, Xun Wu et al.
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 开放式任务的强化学习 (RL) 将法学硕士基于标准的评估压缩为标量奖励，丢弃丰富的文本反馈并将响应与不同的质量概况混为一谈。我们提出体验式学习（EL），它将反馈模型从法学硕士作为法官重新调整为法学硕士作为教练。教练将其对每个政策响应的评估提炼为可转移的经验知识，这些知识以教师模型为条件，并通过政策背景提炼被政策内化。与标量奖励相比，这种更高带宽的反馈通道提供了密集的监督，并保留了高质量响应中的细粒度偏好。在两个策略系列中，借助策略本身或专有模型的反馈，EL 在保留和未见的开放式任务上始终优于基于规则的强化学习。
- Abstract: Reinforcement learning (RL) on open-ended tasks compresses an LLM's rubric-based evaluation into a scalar reward, discarding rich textual feedback and conflating responses with distinct quality profiles. We propose Experiential Learning (EL), which repurposes the feedback model from an LLM-as-a-Judge into an LLM-as-a-Coach. The coach distills its assessment of each on-policy response into transferable experiential k...
- Summary (fallback): 机器翻译摘要显示：开放式任务的强化学习 (RL) 将法学硕士基于标准的评估压缩为标量奖励，丢弃丰富的文本反馈并将响应与不同的质量概况混为一谈。我们提出体验式学习（EL），它将反馈模型从法学硕士作为法官重新调整为法学硕士作为教练。教练将其对每个政策响应的评估提炼为可转移的经验知识，这些知识以教师模型为条件，并通过政策背景提炼被政策内化。与标量奖励相比，这种更高带宽的反馈通道提供了密集的监督，并保留了高质量响应中的细粒度偏好。在两个策略系列中，借助策略本身或专有模型的反馈，EL 在保留和未见的开放式任务上始终优于基于规则的强化学习。
- Keywords: experiential, learning, tasks, feedback, model

### 26. [射频电容耦合等离子体模拟的隐式时域谐波平衡方法](https://arxiv.org/abs/2607.18103v1)
- Original title: An Implicit Time-Domain Harmonic Balance Method for Radio-Frequency Capacitively Coupled Plasma Simulations
- Authors: Yuze Zhu, Yufeng Wei, Yue Zhang, Kun Xu
- Meta: 2026-07-20 | physics.plasm-ph
- 中文摘要: 射频电容耦合等离子体（RF CCP）的快速准确的流体模拟对于现代等离子体反应器的迭代设计和参数优化具有重要意义。这项研究首次成功地将时域谐波平衡 (HB) 方法扩展到完全耦合的漂移扩散泊松系统，并具有用于射频等离子体模拟的完整电子能量传输。为了解决高度非线性能量相关动力学和密集相位耦合引起的严重数值刚度，采用了高效的时空算子分裂策略。通过顺序执行空间隐式松弛和单元局部时间反演，该策略完全避免了全局雅克比行列式的内存密集型组装，同时保持了鲁棒的数值稳定性。
- Abstract: Fast and accurate fluid simulation of radio-frequency capacitively coupled plasmas (RF CCPs) is of great importance for the iterative design and parameter optimization of modern plasma reactors. This study presents the first successful extension of the time-domain harmonic balance (HB) method to a fully coupled drift-diffusion-Poisson system with complete electron-energy transport for RF plasma simulations. To resol...
- Summary (fallback): 机器翻译摘要显示：射频电容耦合等离子体（RF CCP）的快速准确的流体模拟对于现代等离子体反应器的迭代设计和参数优化具有重要意义。这项研究首次成功地将时域谐波平衡 (HB) 方法扩展到完全耦合的漂移扩散泊松系统，并具有用于射频等离子体模拟的完整电子能量传输。为了解决高度非线性能量相关动力学和密集相位耦合引起的严重数值刚度，采用了高效的时空算子分裂策略。通过顺序执行空间隐式松弛和单元局部时间反演，该策略完全避免了全局雅克比行列式的内存密集型组装，同时保持了鲁棒的数值稳定性。
- Keywords: method, plasma, time-domain, highly, coupled

### 27. [使用边缘 AI 推理加速器增强设备上模型适应能力](https://arxiv.org/abs/2607.18101v1)
- Original title: Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator
- Authors: Mateusz Piechocki, Alessandro Capotondi, Marek Kraft
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 设备上的模型自适应对于在资源受限的硬件上实现终身个性化至关重要，但此类设备的计算、功率和内存限制使得端到端反向传播对于现代深度神经网络来说不切实际。这项工作提出了一种异构适应管道，重新利用商业边缘 AI 推理加速器 Hailo-8L，用于设备上训练期间的冻结骨干特征提取。计算图被分区，以便预训练的主干被量化为 INT8 并在加速器上运行，而只有轻量级 FP32 分类头在主机 CPU 上进行微调，从而实现频繁、节能的现场更新，同时大多数权重保持固定。
- Abstract: On-device model adaptation is essential to enable lifelong personalization on resource-constrained hardware, but compute, power, and memory limitations of such devices make end-to-end backpropagation impractical for modern deep neural networks. This work proposes a heterogeneous adaptation pipeline that repurposes a commercial edge AI inference accelerator, Hailo-8L, for frozen-backbone feature extraction during on-...
- Summary (fallback): 机器翻译摘要显示：设备上的模型自适应对于在资源受限的硬件上实现终身个性化至关重要，但此类设备的计算、功率和内存限制使得端到端反向传播对于现代深度神经网络来说不切实际。这项工作提出了一种异构适应管道，重新利用商业边缘 AI 推理加速器 Hailo-8L，用于设备上训练期间的冻结骨干特征提取。计算图被分区，以便预训练的主干被量化为 INT8 并在加速器上运行，而只有轻量级 FP32 分类头在主机 CPU 上进行微调，从而实现频繁、节能的现场更新，同时大多数权重保持固定。
- Keywords: on-device, adaptation, edge, accelerator, model

### 28. [SciForma：结构忠实地生成科学图表](https://arxiv.org/abs/2607.18091v1)
- Original title: SciForma: Structure-Faithful Generation of Scientific Diagrams
- Authors: Yuxuan Luo, Peng Zhang, Xinjie Zhang, Xun Guo, Zhouhui Lian et al.
- Meta: 2026-07-20 | cs.CV
- 中文摘要: 结构保真度对于科学方法图至关重要。为了传达研究逻辑，这些图表必须忠实地呈现组件、方向关系和文本注释。由于单个错误（例如反向箭头或不可读的方程）可能会使整个图形无效，因此结构保真度本质上是结合性的：一个轴上的正确性无法补偿另一轴上的错误。当前的开源模型无法满足这一标准。有监督微调（SFT）学习合理的布局，但无法可靠地确保结构正确性，而基于标量奖励的后训练则掩盖了哪个结构维度失败了。为了解决这个问题，我们引入了 SciForma，一个用于结构忠实地生成科学方法图的框架。
- Abstract: Structural fidelity is essential to scientific methodology diagrams. To communicate research logic, these diagrams must faithfully render components, directional relations, and textual annotations. Since a single error, such as a reversed arrow or an unreadable equation, can invalidate the entire figure, structural fidelity is inherently conjunctive: correctness on one axis cannot compensate for failure on another....
- Summary (fallback): 机器翻译摘要显示：结构保真度对于科学方法图至关重要。为了传达研究逻辑，这些图表必须忠实地呈现组件、方向关系和文本注释。由于单个错误（例如反向箭头或不可读的方程）可能会使整个图形无效，因此结构保真度本质上是结合性的：一个轴上的正确性无法补偿另一轴上的错误。当前的开源模型无法满足这一标准。有监督微调（SFT）学习合理的布局，但无法可靠地确保结构正确性，而基于标量奖励的后训练则掩盖了哪个结构维度失败了。为了解决这个问题，我们引入了 SciForma，一个用于结构忠实地生成科学方法图的框架。
- Keywords: structural, sciforma, scientific, diagrams, generation

### 29. [分布偏移下类条件覆盖的标签复杂度](https://arxiv.org/abs/2607.18088v1)
- Original title: The Label Complexity of Class-Conditional Coverage under Distribution Shift
- Authors: Weijia Han, Lisha Qu
- Meta: 2026-07-20 | cs.LG
- 中文摘要: 许多识别系统的标准评估包含构造上的分布偏移，因为基准在训练和测试分割中放置了不相交的条件。在这种转变下，分离共形预测使边际覆盖率保持在名义水平附近，而每个类别的覆盖率却默默地失败：在真正的跨主题骨架基准上，边际覆盖率保持在 90% 附近，最差的行动类别在大约 70% 的时间内被覆盖，而 60 个类别中的 10 个类别的覆盖率低于 80%。我们描述了恢复每类有效性的成本。首先，这是不可能的：一旦转变联合作用于协变量和标签，目标类条件评分法则就无法从源标签和未标记的目标样本中识别出来，因此没有无标签方法能够同时获得有效且高效的每类覆盖率。
- Abstract: Standard evaluation of many recognition systems contains distribution shift by construction, since benchmarks place disjoint conditions in the training and test splits. Under such a shift, split conformal prediction keeps marginal coverage near the nominal level while per-class coverage fails silently: on a real cross-subject skeleton benchmark, marginal coverage stays near ninety percent, the worst action class is...
- Summary (fallback): 机器翻译摘要显示：许多识别系统的标准评估包含构造上的分布偏移，因为基准在训练和测试分割中放置了不相交的条件。在这种转变下，分离共形预测使边际覆盖率保持在名义水平附近，而每个类别的覆盖率却默默地失败：在真正的跨主题骨架基准上，边际覆盖率保持在 90% 附近，最差的行动类别在大约 70% 的时间内被覆盖，而 60 个类别中的 10 个类别的覆盖率低于 80%。我们描述了恢复每类有效性的成本。首先，这是不可能的：一旦转变联合作用于协变量和标签，目标类条件评分法则就无法从源标签和未标记的目标样本中识别出来，因此没有无标签方法能够同时获得有效且高效的每类覆盖率。
- Keywords: coverage, per-class, shift, marginal, labels

### 30. [临床法学硕士中证据充分性提示的依赖于法官的安全收益和模型特定的帮助成本](https://arxiv.org/abs/2607.18086v1)
- Original title: Judge-dependent safety gains and model-specific helpfulness costs of evidence-sufficiency prompting in clinical LLMs
- Authors: Koyar Afrasyab
- Meta: 2026-07-20 | cs.AI
- 中文摘要: 背景：法学硕士越来越多地评估临床语言模型是否在证据不完整的情况下给出过于自信的答案，但测量的“安全增益”是否反映了真实的行为变化或法官的校准尚未解决。使用结构化证据充分性提示作为测试用例，我们询问它是否减少了不安全的过度自信的答案，这种影响在多大程度上取决于评分法官，以及它的帮助成本是多少。方法：在回顾性公共数据基准（Real-POCQi、HealthBench、MedRBench）中，四种模型（GPT-5.5、Claude Opus 4.8、Gemini 3.5 Flash、Grok 4.3）使用标准提示和包装器回答了完全配对的通用面板（1,200 个单元）。
- Abstract: Background: LLM judges increasingly score whether clinical language models give overconfident answers under incomplete evidence, yet whether a measured "safety gain" reflects real behavior change or the judge's calibration is unresolved. Using a structured evidence-sufficiency prompt as a test case, we asked whether it reduces unsafe overconfident answers, how far that effect depends on the scoring judge, and what i...
- Summary (fallback): 机器翻译摘要显示：背景：法学硕士越来越多地评估临床语言模型是否在证据不完整的情况下给出过于自信的答案，但测量的“安全增益”是否反映了真实的行为变化或法官的校准尚未解决。使用结构化证据充分性提示作为测试用例，我们询问它是否减少了不安全的过度自信的答案，这种影响在多大程度上取决于评分法官，以及它的帮助成本是多少。方法：在回顾性公共数据基准（Real-POCQi、HealthBench、MedRBench）中，四种模型（GPT-5.5、Claude Opus 4.8、Gemini 3.5 Flash、Grok 4.3）使用标准提示和包装器回答了完全配对的通用面板（1,200 个单元）。
- Keywords: judge, helpfulness, clinical, safety, whether

## biorxiv

### 1. [用于蛋白质组重新分配从头预测的混合机器学习和酶约束代谢模型](https://www.biorxiv.org/content/10.64898/2026.07.20.739489v1)
- Original title: A hybrid machine learning and enzyme-constrained metabolic model for ab initio prediction of proteome reallocation
- Authors: Motamedian, E., Nikoloski, Z.
- Meta: 2026-07-21 | systems biology | DOI: 10.64898/2026.07.20.739489
- 中文摘要: 由于有限的细胞蛋白质组的重新分配，微生物细胞工厂中异源蛋白质的高表达经常引发严重的负担。传统的基于约束的模型很难在不依赖特定条件的组学数据的情况下从头开始预测这些资源转移。为了弥补这一差距，我们开发了混合转录-翻译 (HyTT) 框架，通过强制执行 80S 核糖体完整性约束，将多元自适应回归样条 (MARS) 与酶约束代谢模型相结合。 HyTT 作为一个混合整数线性规划问题，基于二分搜索，在数学上将宏观空间边界与微观、序列导出的平移成本耦合起来。
- Abstract: High expression of heterologous proteins in microbial cell factories frequently triggers a severe burden due to reallocation of finite cellular proteome. Conventional constraint-based models struggle to predict these resource shifts ab initio without relying on condition-specific omics data. To bridge this gap, we developed the Hybrid Transcription-Translation (HyTT) framework, combining multivariate adaptive regres...
- Summary (fallback): 机器翻译摘要显示：由于有限的细胞蛋白质组的重新分配，微生物细胞工厂中异源蛋白质的高表达经常引发严重的负担。传统的基于约束的模型很难在不依赖特定条件的组学数据的情况下从头开始预测这些资源转移。为了弥补这一差距，我们开发了混合转录-翻译 (HyTT) 框架，通过强制执行 80S 核糖体完整性约束，将多元自适应回归样条 (MARS) 与酶约束代谢模型相结合。 HyTT 作为一个混合整数线性规划问题，基于二分搜索，在数学上将宏观空间边界与微观、序列导出的平移成本耦合起来。
- Keywords: metabolic, hytt, proteome, initio, reallocation

### 2. [线粒体功能的光遗传学调控调节细胞死亡](https://www.biorxiv.org/content/10.64898/2026.07.19.739443v1)
- Original title: Optogenetic Regulation of Mitochondrial Function to Modulate Cell Death
- Authors: Yang, R.-Z., Wang, D.-D., Li, S.-M., Liu, D.-H., Liu, P.-P. et al.
- Meta: 2026-07-21 | cell biology | DOI: 10.64898/2026.07.19.739443
- 中文摘要: 细胞死亡是生理和病理条件（包括神经退行性疾病和癌症）中涉及的关键过程。这项研究探索了利用光遗传学技术通过光敏蛋白诱导细胞死亡。通过用光敏蛋白操纵线粒体功能，我们研究了三种不同的策略：1）通过胶杆菌视紫红质介导的碱化抑制氧化磷酸化，2）用反向质子泵视紫红质（RPPR）和阴离子传导通道视紫红质诱导线粒体去极化，3）使用靶向线粒体的miniSOG产生活性氧（ROS）。我们的研究结果强调了光遗传学方法诱导细胞死亡的潜力，为以异常细胞存活为特征的疾病的治疗干预提供了有希望的途径。
- Abstract: Cell death is a critical process involved in physiological and pathological conditions, including neurodegenerative diseases and cancer. This study explores the use of optogenetic techniques to induce cell death by employing light sensitive proteins. By manipulating mitochondrial function with light-sensitive proteins, we investigated three distinct strategies: 1) inhibiting oxidative phosphorylation through Gloeoba...
- Summary (fallback): 机器翻译摘要显示：细胞死亡是生理和病理条件（包括神经退行性疾病和癌症）中涉及的关键过程。这项研究探索了利用光遗传学技术通过光敏蛋白诱导细胞死亡。通过用光敏蛋白操纵线粒体功能，我们研究了三种不同的策略：1）通过胶杆菌视紫红质介导的碱化抑制氧化磷酸化，2）用反向质子泵视紫红质（RPPR）和阴离子传导通道视紫红质诱导线粒体去极化，3）使用靶向线粒体的miniSOG产生活性氧（ROS）。我们的研究结果强调了光遗传学方法诱导细胞死亡的潜力，为以异常细胞存活为特征的疾病的治疗干预提供了有希望的途径。
- Keywords: cell, death, optogenetic, mitochondrial, function

### 3. [通过摄影测量引导采样揭示了优势珊瑚单特异性群内的空间基因型模式。](https://www.biorxiv.org/content/10.64898/2026.07.19.739434v1)
- Original title: Spatial genotypic patterns within monospecific stands of a dominant coral revealed through photogrammetry-guided sampling.
- Authors: van Hulten, D., Liggins, L., Yuval, M., Sewell, M. A., Bongaerts, P.
- Meta: 2026-07-21 | ecology | DOI: 10.64898/2026.07.19.739434
- 中文摘要: 当地和全球的压力因素正在推动造礁珊瑚的竞争性下降，并有利于耐压的杂草物种。在许多这些类群中，快速无性繁殖策略促进了现有基因型在小空间尺度上的增殖，可能导致单特异性林分（“地毯”）的形成。这种繁殖策略引起了人们对未来珊瑚礁的种内多样性和恢复力的担忧。这些空间占主导地位的杂草珊瑚的遗传结构仍然知之甚少，部分原因是密集聚集的珊瑚群缺乏明显的边界，阻碍了标准抽样设计的使用。我们采用摄影测量引导的、空间明确的采样方法来评估库拉索岛三个珊瑚礁点日益占主导地位的造石珊瑚 Madracis auretenra 的基因型多样性和基因分布。 M的封面。
- Abstract: Local and global stressors are driving declines in competitive reef-building corals and favouring stress-tolerant, weedy species. In many of these taxa, rapid asexual reproductive strategies promote the proliferation of existing genotypes at small spatial scales, potentially leading to the formation of monospecific stands ("carpets"). Such reproductive strategies raise concerns for the intraspecific diversity and re...
- Summary (fallback): 机器翻译摘要显示：当地和全球的压力因素正在推动造礁珊瑚的竞争性下降，并有利于耐压的杂草物种。在许多这些类群中，快速无性繁殖策略促进了现有基因型在小空间尺度上的增殖，可能导致单特异性林分（“地毯”）的形成。这种繁殖策略引起了人们对未来珊瑚礁的种内多样性和恢复力的担忧。这些空间占主导地位的杂草珊瑚的遗传结构仍然知之甚少，部分原因是密集聚集的珊瑚群缺乏明显的边界，阻碍了标准抽样设计的使用。我们采用摄影测量引导的、空间明确的采样方法来评估库拉索岛三个珊瑚礁点日益占主导地位的造石珊瑚 Madracis auretenra 的基因型多样性和基因分布。 M的封面。
- Keywords: genotypic, sampling, diversity, dominant, monospecific

### 4. [追踪“海洋熊猫”：珠江口极度濒危的太平斑鳢 eDNA 监测的物种特异性 qPCR 检测](https://www.biorxiv.org/content/10.64898/2026.07.20.739478v1)
- Original title: Tracing the 'Panda of the Sea': Species-Specific qPCR Assays for eDNA Monitoring of Critically Endangered Bahaba taipingensis in the Pearl River Estuary
- Authors: Liao, Y., Szeto, B. C.-F., Zhao, H., Lin, H., Chen, G. et al.
- Meta: 2026-07-21 | ecology | DOI: 10.64898/2026.07.20.739478
- 中文摘要: 太平鲳鱼（Bahaba taipingensis，石首鱼科）是我国极危、国家一级保护海洋鱼类。迫切需要可靠、非侵入性的监测工具来为保护和放养工作提供信息。我们开发并验证了三种基于 TaqMan 探针的 qPCR 检测，针对线粒体 12S rRNA、ND5 和控制区 (D 环) 位点，用于太平芽孢杆菌的物种特异性检测。引物-探针组是根据完整的线粒体基因组设计的，并根据 GenBank 进行计算机模拟评估，并根据 B. taipingensis 和密切相关的 sciaenids 的组织 DNA 以及阳性 eDNA 样本进行体外评估；使用合成靶 DNA 的连续稀释来量化灵敏度。所有三种检测均显示出高特异性和一致的扩增；基于卓越的低拷贝灵敏度和最小的产品差异，选择 12S rRNA 测定 (Bhb-12S) 进行现场筛选。
- Abstract: Chinese Bahaba (Bahaba taipingensis, Sciaenidae) is a Critically Endangered, Grade I state protected marine fish in China. Reliable, non invasive monitoring tools are urgently needed to inform conservation and restocking efforts. We developed and validated three TaqMan probe-based qPCR assays targeting mitochondrial 12S rRNA, ND5, and control region (D-loop) loci for species specific detection of B. taipingensis. Pr...
- Summary (fallback): 机器翻译摘要显示：太平鲳鱼（Bahaba taipingensis，石首鱼科）是我国极危、国家一级保护海洋鱼类。迫切需要可靠、非侵入性的监测工具来为保护和放养工作提供信息。我们开发并验证了三种基于 TaqMan 探针的 qPCR 检测，针对线粒体 12S rRNA、ND5 和控制区 (D 环) 位点，用于太平芽孢杆菌的物种特异性检测。引物-探针组是根据完整的线粒体基因组设计的，并根据 GenBank 进行计算机模拟评估，并根据 B.
- Keywords: taipingensis, assays, qpcr, edna, monitoring

### 5. [印度动物群的大规模众包注释声学数据集](https://www.biorxiv.org/content/10.64898/2026.07.20.739496v1)
- Original title: A large-scale crowd-sourced annotated acoustic dataset of Indian fauna
- Authors: Ramesh, V., Singh, S., Pop, P., Choksi, P., Singh, P. et al.
- Meta: 2026-07-21 | ecology | DOI: 10.64898/2026.07.20.739496
- 中文摘要: 全球生物多样性丧失速度需要在大地理范围内采取保护行动和监测。声音监测等保护技术与深度学习相结合，现在使我们能够跨空间和时间同时监测野生动物。然而，对于热带地区很大一部分生物多样性，我们还不能依赖自动识别方法，因为我们缺乏声学模板来稳健地训练深度学习算法。在本文中，我们依靠一种新颖的参与方法，招募研究人员、保护从业者和自然爱好者，创建了一个独特的众包、开放获取的印度生物多样性分类组的声学注释数据集。
- Abstract: Global rates of biodiversity loss warrant conservation action and monitoring at large geographic scales. Conservation technologies such as acoustic monitoring in conjunction with deep learning now enable us to monitor wildlife simultaneously across space and time. However, for a significant proportion of biodiversity in tropical regions, we cannot yet rely on automated recognition approaches because we lack acoustic...
- Summary (fallback): 机器翻译摘要显示：全球生物多样性丧失速度需要在大地理范围内采取保护行动和监测。声音监测等保护技术与深度学习相结合，现在使我们能够跨空间和时间同时监测野生动物。然而，对于热带地区很大一部分生物多样性，我们还不能依赖自动识别方法，因为我们缺乏声学模板来稳健地训练深度学习算法。在本文中，我们依靠一种新颖的参与方法，招募研究人员、保护从业者和自然爱好者，创建了一个独特的众包、开放获取的印度生物多样性分类组的声学注释数据集。
- Keywords: acoustic, biodiversity, dataset, conservation, monitoring

### 6. [<em>白色念珠菌 TLO</em> 基因家族的旁系同源物形成具有不完全冗余的互连功能网络](https://www.biorxiv.org/content/10.64898/2026.06.29.735307v2)
- Original title: Paralogs of the <em>Candida albicans TLO</em> gene family form interconnected functional networks with incomplete redundancy
- Authors: Simonton, E., Cangelosi, N., Zhou, M., Hendricks, P. S., Woodruff, A. L. et al.
- Meta: 2026-07-21 | genetics | DOI: 10.64898/2026.06.29.735307
- 中文摘要: 基因复制通常无法赋予生物体选择性优势，从而促使它们从群体中消失。在极少数情况下，复制不会产生适应性成本或增强适应性，基因家族可以通过重复复制过程形成。虽然基因重复的功能已被详细研究，但很少有人探讨重复重复如何影响旁系同源物冗余并可能限制新旁系同源物或新功能的出现。在这里，我们为白色念珠菌端粒相关 (TLO) 基因家族的 14 个成员中的每一个构建了一组单缺失突变体，以测试来自谱系特异性扩展的旁系同源物之间分子和生物学功能的冗余性。
- Abstract: Gene duplication typically fails to confer a selective advantage to an organism, prompting their removal from a population. In the rare instance that duplication either does not incur a fitness cost or it enhances fitness, gene families can form through repeating the duplication process. While the function of gene duplicates has been studied in detail, little work has explored how repeated duplication impacts paralo...
- Summary (fallback): 机器翻译摘要显示：基因复制通常无法赋予生物体选择性优势，从而促使它们从群体中消失。在极少数情况下，复制不会产生适应性成本或增强适应性，基因家族可以通过重复复制过程形成。虽然基因重复的功能已被详细研究，但很少有人探讨重复重复如何影响旁系同源物冗余并可能限制新旁系同源物或新功能的出现。在这里，我们为白色念珠菌端粒相关 (TLO) 基因家族的 14 个成员中的每一个构建了一组单缺失突变体，以测试来自谱系特异性扩展的旁系同源物之间分子和生物学功能的冗余性。
- Keywords: gene, paralogs, redundancy, function, single

### 7. [Legumain（天冬酰胺酰内肽酶）调节肺纤维化中的细胞外基质动力学](https://www.biorxiv.org/content/10.64898/2026.07.20.739492v1)
- Original title: Legumain (asparaginyl endopeptidase) modulates extracellular matrix dynamics in pulmonary fibrosis
- Authors: SAIDI, A., RIGOUX, B., DAVID, A., SIZARET, D., ALLOUCHE, R. et al.
- Meta: 2026-07-21 | biochemistry | DOI: 10.64898/2026.07.20.739492
- 中文摘要: 肺纤维化的特征是由成纤维细胞向肌成纤维细胞转变（FMT）驱动的细胞外基质（ECM）沉积以及蛋白水解平衡的改变。虽然几种半胱氨酸蛋白酶的作用已被记录，但组织蛋白酶 V (CatV) 和 legumain (LGMN) 的具体贡献仍鲜有探讨。 LGMN、CatV 及其双重抑制剂半胱氨酸蛋白酶抑制剂 M/E (CysM/E) 在特发性肺纤维化患者的肺标本和支气管肺泡灌洗液中显着升高。 TGF {β}1 通过 Smad 3 途径触发 CysM/E 表达和 LGMN 转录、细胞内成熟、酶活性和前 LGMN 分泌，而 CatV 在经历肌分化的人肺成纤维细胞（CCD 19Lu 和原代 HPF 细胞）中下调。
- Abstract: Pulmonary fibrosis is characterized by extracellular matrix (ECM) deposition driven by fibroblast to myofibroblast transition (FMT) and by an altered proteolytic balance. While the roles of several cysteine proteases have been documented, the specific contribution of cathepsin V (CatV) and legumain (LGMN) remains poorly explored. LGMN, CatV and their dual inhibitor cystatin M/E (CysM/E) are significantly increased i...
- Summary (fallback): 机器翻译摘要显示：肺纤维化的特征是由成纤维细胞向肌成纤维细胞转变（FMT）驱动的细胞外基质（ECM）沉积以及蛋白水解平衡的改变。虽然几种半胱氨酸蛋白酶的作用已被记录，但组织蛋白酶 V (CatV) 和 legumain (LGMN) 的具体贡献仍鲜有探讨。 LGMN、CatV 及其双重抑制剂半胱氨酸蛋白酶抑制剂 M/E (CysM/E) 在特发性肺纤维化患者的肺标本和支气管肺泡灌洗液中显着升高。 TGF {β}1 通过 Smad 3 途径触发 CysM/E 表达和 LGMN 转录、细胞内成熟、酶活性和前 LGMN 分泌，而 CatV 在经历肌分化的人肺成纤维细胞（CCD 19Lu 和原代 HPF 细胞）中下调。
- Keywords: lgmn, catv, fibrosis, fibronectin, elastin

### 8. [临床级血小板衍生生物材料可减轻神经元损伤临床前模型中的线粒体功能障碍](https://www.biorxiv.org/content/10.1101/2025.09.11.675564v2)
- Original title: Clinical-grade platelet-derived biomaterials mitigate mitochondrial dysfunction in preclinical models of neuronal injury
- Authors: Gupta, K., Delila, L., Chou, M.- L., Ngoc Le, N. T., Wu, H.- Y. et al.
- Meta: 2026-07-21 | bioengineering | DOI: 10.1101/2025.09.11.675564
- 中文摘要: 血小板衍生的生物材料正在成为再生医学和神经恢复的有前景的无细胞治疗平台。其中，由临床级同种异体血小板浓缩物制备的人血小板颗粒裂解物（HPPL）和血小板衍生的细胞外囊泡（PEV）提供两种互补的生物材料形式：富含可溶性营养因子的裂解物和富含生物活性物质的囊泡制剂。由于线粒体功能障碍和氧化还原失衡是神经退行性变的标志，因此我们研究了这些血小板衍生的生物材料是否可以防止鱼藤酮诱导的线粒体损伤。 HPPL 和 PEV 由临床级血小板浓缩物进行生物加工，并对其蛋白质含量、抗氧化能力、囊泡形态、大小分布、浓度以及血小板和 EV 标记物进行表征。
- Abstract: Platelet-derived biomaterials are emerging as promising cell-free therapeutic platforms for regenerative medicine and neurorestoration. Among them, human platelet pellet lysates (HPPL) and platelet-derived extracellular vesicles (PEVs), prepared from clinical-grade allogeneic platelet concentrates, provide two complementary biomaterial formats: a soluble trophic factor-rich lysate and a vesicular formulation enriche...
- Summary (fallback): 机器翻译摘要显示：血小板衍生的生物材料正在成为再生医学和神经恢复的有前景的无细胞治疗平台。其中，由临床级同种异体血小板浓缩物制备的人血小板颗粒裂解物（HPPL）和血小板衍生的细胞外囊泡（PEV）提供两种互补的生物材料形式：富含可溶性营养因子的裂解物和富含生物活性物质的囊泡制剂。由于线粒体功能障碍和氧化还原失衡是神经退行性变的标志，因此我们研究了这些血小板衍生的生物材料是否可以防止鱼藤酮诱导的线粒体损伤。 HPPL 和 PEV 由临床级血小板浓缩物进行生物加工，并对其蛋白质含量、抗氧化能力、囊泡形态、大小分布、浓度以及血小板和 EV 标记物进行表征。
- Keywords: mitochondrial, biomaterials, hppl, pevs, platelet-derived

### 9. [用于组织重塑多参数分析的高通量 3D 微组织平台。](https://www.biorxiv.org/content/10.64898/2026.07.15.738540v2)
- Original title: A high-throughput, 3D microtissue platform for multiparametric analysis of tissue remodeling.
- Authors: Vasan, A., Nguyen, Q., Davis, E., Karakan, M. C., Westphal, E. et al.
- Meta: 2026-07-21 | bioengineering | DOI: 10.64898/2026.07.15.738540
- 中文摘要: 细胞外基质（ECM）重塑和力产生是组织形态发生和修复的基本驱动因素，但定量研究这些动态机械过程的可扩展方法仍然有限。在这里，我们提出了一个高通量筛选平台，该平台将工程三维 (3D) 微组织集成在标准化 96 孔格式中。我们引入了强大的模具铸造制造工艺和逐层表面改性策略，可确保长期组织稳定性并防止脱离（95% 组织形成成功；在培养物中稳定超过 10 天）。该系统能够通过相差成像方式同时纵向量化组织闭合、组织收缩性和组织压实。
- Abstract: Extracellular matrix (ECM) remodeling and force generation are fundamental drivers of tissue morphogenesis and repair, yet scalable methods to quantitatively interrogate these dynamic mechanical processes remain limited. Here, we present a high-throughput screening platform that integrates engineered three-dimensional (3D) microtissues within a standardized 96-well format. We introduce a robust mold-casting fabricat...
- Summary (fallback): 机器翻译摘要显示：细胞外基质（ECM）重塑和力产生是组织形态发生和修复的基本驱动因素，但定量研究这些动态机械过程的可扩展方法仍然有限。在这里，我们提出了一个高通量筛选平台，该平台将工程三维 (3D) 微组织集成在标准化 96 孔格式中。我们引入了强大的模具铸造制造工艺和逐层表面改性策略，可确保长期组织稳定性并防止脱离（95% 组织形成成功；在培养物中稳定超过 10 天）。该系统能够通过相差成像方式同时纵向量化组织闭合、组织收缩性和组织压实。
- Keywords: tissue, remodeling, platform, high-throughput, analysis

### 10. [ProtSyntax：用于解码翻译后修饰语法和功能的蛋白质大语言模型](https://www.biorxiv.org/content/10.64898/2026.07.18.739331v1)
- Original title: ProtSyntax: a protein large language model for decoding post-translational modification syntax and function
- Authors: Lin, Y.
- Meta: 2026-07-21 | bioinformatics | DOI: 10.64898/2026.07.18.739331
- 中文摘要: 翻译后修饰 (PTM) 通过残基化学、序列背景、三维微环境和修饰状态之间的依赖性来调节蛋白质功能，但大多数预测因子独立地对位点进行建模，并且不会将修饰倾向与功能后果联系起来。在这里，我们介绍了 ProtSyntax，这是一种以 PTM 为中心的蛋白质语言模型，经过 40 个 PTM 类别的 425 万个示例的训练，并针对激酶特异性、PTM 串扰和酶动力学进行监督。 ProtSyntax 将双向远程建模与几何门控注意力集成在稀疏专家混合架构中，并使用自适应多目标学习将残基级 PTM 语法与蛋白质级函数耦合。在 40 个 PTM 站点基准测试中，相对于表现最佳的基准，ProtSyntax 将平均 MCC 和 AP 分别提高了 12.7% 和 10.7%。
- Abstract: Post-translational modifications (PTMs) regulate protein function through dependencies among residue chemistry, sequence context, three-dimensional microenvironments and modification states, yet most predictors model sites independently and do not connect modification propensity to functional consequences. Here we present ProtSyntax, a PTM-centered protein language model trained on 4.25 million examples spanning 40...
- Summary (fallback): 机器翻译摘要显示：翻译后修饰 (PTM) 通过残基化学、序列背景、三维微环境和修饰状态之间的依赖性来调节蛋白质功能，但大多数预测因子独立地对位点进行建模，并且不会将修饰倾向与功能后果联系起来。在这里，我们介绍了 ProtSyntax，这是一种以 PTM 为中心的蛋白质语言模型，经过 40 个 PTM 类别的 425 万个示例的训练，并针对激酶特异性、PTM 串扰和酶动力学进行监督。 ProtSyntax 将双向远程建模与几何门控注意力集成在稀疏专家混合架构中，并使用自适应多目标学习将残基级 PTM 语法与蛋白质级函数耦合。在 40 个 PTM 站点基准测试中，相对于表现最佳的基准，ProtSyntax 将平均 MCC 和 AP 分别提高了 12.7% 和 10.7%。
- Keywords: protsyntax, protein, model, modification, function

### 11. [拷贝数特征簇和基因组不稳定性的泛癌症多组学分析](https://www.biorxiv.org/content/10.64898/2026.07.20.739333v1)
- Original title: A Pan-Cancer Multi-Omic Analysis of Copy Number Signature Clusters and Genomic Instability
- Authors: Rota Negroni, M., Billato, I., Romualdi, C.
- Meta: 2026-07-21 | cancer biology | DOI: 10.64898/2026.07.20.739333
- 中文摘要: 拷贝数改变 (CNA) 是癌症基因组不稳定的主要原因，而拷贝数特征 (CNS) 提供了塑造 CNA 景观的过程的紧凑表示。然而，现有中枢神经系统框架之间的关系及其从全基因组测序以外的分子数据的可预测性仍不清楚。在这里，我们比较了 5,800 多个 TCGA 癌症样本中的三个主要 CNS 概要，评估了它们的重叠性、互补性、生物学相关性和预后关联。个体特征显示出有限的交叉研究一致性，而特征衍生的簇识别了生物学上不同的患者群体，包括在所有框架中观察到的有利结果簇。
- Abstract: Copy number alterations (CNAs) are major contributors to genomic instability in cancer, and copy number signatures (CNS) provide a compact representation of the processes shaping CNA landscapes. However, the relationships among existing CNS frameworks and their predictability from molecular data other than whole-genome sequencing remain unclear. Here, we compare three major CNS compendia across more than 5,800 TCGA...
- Summary (fallback): 机器翻译摘要显示：拷贝数改变 (CNA) 是癌症基因组不稳定的主要原因，而拷贝数特征 (CNS) 提供了塑造 CNA 景观的过程的紧凑表示。然而，现有中枢神经系统框架之间的关系及其从全基因组测序以外的分子数据的可预测性仍不清楚。在这里，我们比较了 5,800 多个 TCGA 癌症样本中的三个主要 CNS 概要，评估了它们的重叠性、互补性、生物学相关性和预后关联。个体特征显示出有限的交叉研究一致性，而特征衍生的簇识别了生物学上不同的患者群体，包括在所有框架中观察到的有利结果簇。
- Keywords: instability, copy, number, clusters, genomic

### 12. [使用体内 CRISPR 筛选和扰动测序绘制食管腺癌中的功能性肿瘤抑制网络](https://www.biorxiv.org/content/10.64898/2026.07.19.739473v1)
- Original title: Mapping Functional Tumor Suppressor Networks in Esophageal Adenocarcinoma Using In Vivo CRISPR Screening and Perturb-sequencing
- Authors: Mustafa, E. H., Papastratos, K., Wu, K., Thio, N., Milne, J. V. et al.
- Meta: 2026-07-21 | cancer biology | DOI: 10.64898/2026.07.19.739473
- 中文摘要: 食管腺癌（EAC）是一种遗传异质性恶性肿瘤，很少有复发驱动因素，限制了有效的靶向治疗。尽管 EAC 起源于巴雷特食管 (BE)，但驱动从癌前状态进展为侵袭性癌症的机制仍不清楚。我们结合了 CRISPR-Cas9 功能丧失筛选、体内致瘤性测定和 Perturb-seq 分析来定义 BE 转化的功能驱动因素。我们鉴定了 37 个肿瘤抑制因子，它们的缺失会促进 EAC 的进展，从而定义了肿瘤起始的功能景观。尽管存在遗传多样性，但这些损失集中在四个转录程序上，涉及代谢重编程、细胞周期进程、RNA 加工和细胞运动。此外，我们发现 NIPBL、TGFBR2 和 RPL22 的缺失是铂类和紫杉烷类化疗耐药的关键介质。
- Abstract: Esophageal adenocarcinoma (EAC) is a genetically heterogeneous malignancy with few recurrent drivers, limiting effective targeted therapies. Although EAC arises from Barrett's esophagus (BE), mechanisms driving progression from this premalignant state to invasive cancer remain unclear. We combined pooled CRISPR-Cas9 loss-of-function screening, in vivo tumorigenicity assays, and Perturb-seq profiling to define functi...
- Summary (fallback): 机器翻译摘要显示：食管腺癌（EAC）是一种遗传异质性恶性肿瘤，很少有复发驱动因素，限制了有效的靶向治疗。尽管 EAC 起源于巴雷特食管 (BE)，但驱动从癌前状态进展为侵袭性癌症的机制仍不清楚。我们结合了 CRISPR-Cas9 功能丧失筛选、体内致瘤性测定和 Perturb-seq 分析来定义 BE 转化的功能驱动因素。我们鉴定了 37 个肿瘤抑制因子，它们的缺失会促进 EAC 的进展，从而定义了肿瘤起始的功能景观。尽管存在遗传多样性，但这些损失集中在四个转录程序上，涉及代谢重编程、细胞周期进程、RNA 加工和细胞运动。此外，我们发现 NIPBL、TGFBR2 和 RPL22 的缺失是铂类和紫杉烷类化疗耐药的关键介质。
- Keywords: tumor, functional, progression, suppressor, esophageal

### 13. [染色质复合体依赖性的系统多变量分析揭示 Set1C/COMPASS 是富含黑色素瘤的表观遗传脆弱性](https://www.biorxiv.org/content/10.64898/2026.02.13.705694v2)
- Original title: Systematic multivariate analysis of chromatin complex dependencies reveals Set1C/COMPASS as a melanoma-enriched epigenetic vulnerability
- Authors: Camacho, L. Q., Fallahi-Sichani, M.
- Meta: 2026-07-21 | cancer biology | DOI: 10.64898/2026.02.13.705694
- 中文摘要: 表观遗传失调是癌症的一个常见特征。由于对维持恶性转录状态的基于染色质的机制的日益依赖，它造成了脆弱性。虽然细胞活力广泛需要许多染色质调节因子，但其他调节因子在不同的致癌环境、组织谱系和分化状态中以上下文相关的方式发挥作用。此外，染色质调节因子通常在多亚基复合体中发挥作用。因此，表观遗传脆弱性是由协调的复杂活动产生的。在这里，我们将人类癌细胞系的大规模遗传依赖性图谱与精心设计的表观遗传复杂注释相结合，对跨癌症谱系的复杂水平表观遗传依赖性进行系统的多变量分析。
- Abstract: Epigenetic dysregulation is a common feature of cancer. It creates vulnerabilities arising from an increased reliance on chromatin-based mechanisms that sustain malignant transcriptional states. While many chromatin regulators are broadly required for cellular viability, others function in a context-dependent manner across distinct oncogenic settings, tissue lineages, and differentiation states. Moreover, chromatin...
- Summary (fallback): 机器翻译摘要显示：表观遗传失调是癌症的一个常见特征。由于对维持恶性转录状态的基于染色质的机制的日益依赖，它造成了脆弱性。虽然细胞活力广泛需要许多染色质调节因子，但其他调节因子在不同的致癌环境、组织谱系和分化状态中以上下文相关的方式发挥作用。此外，染色质调节因子通常在多亚基复合体中发挥作用。因此，表观遗传脆弱性是由协调的复杂活动产生的。在这里，我们将人类癌细胞系的大规模遗传依赖性图谱与精心设计的表观遗传复杂注释相结合，对跨癌症谱系的复杂水平表观遗传依赖性进行系统的多变量分析。
- Keywords: epigenetic, complex, analysis, dependencies, set1c

### 14. [用于从现场图像中概率信息检测香蕉病害的视觉归一化流程](https://www.biorxiv.org/content/10.64898/2026.07.19.739426v1)
- Original title: Vision Normalizing Flows for the probability-informed detection of banana diseases from in-field images
- Authors: Prusokiene, A., Prusokas, A., Retkute, R.
- Meta: 2026-07-21 | plant biology | DOI: 10.64898/2026.07.19.739426
- 中文摘要: 香蕉病害给热带小农耕作系统造成严重的生产损失，但准确的田间视觉诊断仍然很困难：不同品种和生长阶段的症状表现各不相同，并且几种病害会产生形态重叠的叶征。我们开发了一个概率图像识别框架，用于从现场照片中检测五种经济上重要的香蕉病害——黄单胞菌枯萎病、香蕉束顶病、镰刀菌枯萎病（巴拿马病）、黄叶斑病和黑叶斑病——无需对视觉主干进行任何特定疾病的微调。该方法从 DINOv3 视觉基础模型中提取冻结的 1,152 维嵌入，并将它们与条件归一化流耦合，并在四个公开可用的数据集（涵盖患病香蕉植物、健康组织、非香蕉植被和一般自然图像）上进行训练。
- Abstract: Banana diseases impose severe production losses in tropical smallholder farming systems, yet accurate in-field visual diagnosis remains difficult: symptom expression varies across cultivars and growth stages, and several diseases produce morphologically overlapping foliar signs. We developed a probabilistic image-recognition framework for detecting five economically important banana diseases - Xanthomonas Wilt, Bana...
- Summary (fallback): 机器翻译摘要显示：香蕉病害给热带小农耕作系统造成严重的生产损失，但准确的田间视觉诊断仍然很困难：不同品种和生长阶段的症状表现各不相同，并且几种病害会产生形态重叠的叶征。我们开发了一个概率图像识别框架，用于从现场照片中检测五种经济上重要的香蕉病害——黄单胞菌枯萎病、香蕉束顶病、镰刀菌枯萎病（巴拿马病）、黄叶斑病和黑叶斑病——无需对视觉主干进行任何特定疾病的微调。该方法从 DINOv3 视觉基础模型中提取冻结的 1,152 维嵌入，并将它们与条件归一化流耦合，并在四个公开可用的数据集（涵盖患病香蕉植物、健康组织、非香蕉植被和一般自然图像）上进行训练。
- Keywords: banana, disease, diseases, sigatoka, vision

### 15. [瞳孔直径作为蓝斑活动模式代理的局限性](https://www.biorxiv.org/content/10.64898/2026.07.14.738598v1)
- Original title: Limitations of pupil diameter as a proxy for modes of locus coeruleus activity
- Authors: Thompson, L. W., Gold, J. I.
- Meta: 2026-07-21 | neuroscience | DOI: 10.64898/2026.07.14.738598
- 中文摘要: 蓝斑-去甲肾上腺素 (LC-NE) 系统在高级大脑功能中发挥着多种作用，这些作用被认为取决于其激活模式，反映了基线和诱发激活水平之间的关系。这些关系在单单位 LC 活性和拟议的 LC-NE 活性生理指标（例如瞳孔大小）中都很明显。在这里，我们使用清醒猴子的测量来表明，这两种不同测量中明显的基线诱发关系在它们之间不可靠地耦合：瞳孔的基线诱发关系不能预测 LC 中的基线诱发关系，反之亦然。
- Abstract: The locus coeruleus-norepinephrine (LC-NE) system plays multiple roles in higher brain function that are thought to depend on its mode of activation, which reflects relationships between baseline and evoked activation levels. These relationships are evident in both single-unit LC activity and proposed physiological proxies of LC-NE activity, such as pupil size. Here we used measurements in awake monkeys to show that...
- Summary (fallback): 机器翻译摘要显示：蓝斑-去甲肾上腺素 (LC-NE) 系统在高级大脑功能中发挥着多种作用，这些作用被认为取决于其激活模式，反映了基线和诱发激活水平之间的关系。这些关系在单单位 LC 活性和拟议的 LC-NE 活性生理指标（例如瞳孔大小）中都很明显。在这里，我们使用清醒猴子的测量来表明，这两种不同测量中明显的基线诱发关系在它们之间不可靠地耦合：瞳孔的基线诱发关系不能预测 LC 中的基线诱发关系，反之亦然。
- Keywords: activity, pupil, lc-ne, relationships, baseline

### 16. [血清素在麻醉小鼠前脑中诱导下调状态](https://www.biorxiv.org/content/10.64898/2026.07.14.738517v2)
- Original title: Serotonin induces DOWN states across the anesthetized mouse forebrain
- Authors: Grossmann, R., Meijas, J. F., International Brain Laboratory,, Mainen, Z. F., Meijer, G. T.
- Meta: 2026-07-21 | neuroscience | DOI: 10.64898/2026.07.14.738517
- 中文摘要: 中缝背核（DRN）中的血清素能神经元广泛投射到整个前脑，但它们对整体网络状态的影响仍然存在争议。血清素参与调节缓慢振荡，即所谓的向上和向下状态，这种状态发生在睡眠和轻度麻醉期间。虽然光遗传学功能磁共振成像表明血清素 (5-HT) 会抑制全脑活动，但经典的电刺激研究报告了皮质 UP 状态的诱导。为了解决这一差异，我们将光遗传学 5-HT 刺激与轻麻醉小鼠前脑的大规模神经像素记录相结合。我们证明，选择性 5-HT 释放持续诱导皮层和纹状体的 DOWN 状态，而中脑动力学基本上不受影响。
- Abstract: Serotonergic neurons in the dorsal raphe nucleus (DRN) project extensively throughout the forebrain, yet their influence on global network states remains controversial. Serotonin is implicated in regulating slow-oscillations, so-called UP and DOWN states, which occur during sleep and light anesthesia. While optogenetic fMRI suggests that serotonin (5-HT) suppresses brain-wide activity, classical electrical stimulati...
- Summary (fallback): 机器翻译摘要显示：中缝背核（DRN）中的血清素能神经元广泛投射到整个前脑，但它们对整体网络状态的影响仍然存在争议。血清素参与调节缓慢振荡，即所谓的向上和向下状态，这种状态发生在睡眠和轻度麻醉期间。虽然光遗传学功能磁共振成像表明血清素 (5-HT) 会抑制全脑活动，但经典的电刺激研究报告了皮质 UP 状态的诱导。为了解决这一差异，我们将光遗传学 5-HT 刺激与轻麻醉小鼠前脑的大规模神经像素记录相结合。我们证明，选择性 5-HT 释放持续诱导皮层和纹状体的 DOWN 状态，而中脑动力学基本上不受影响。
- Keywords: states, serotonin, down, across, forebrain

### 17. [人类海马体中的正负视网膜专题代码](https://www.biorxiv.org/content/10.1101/2024.09.27.615397v4)
- Original title: Positive and Negative Retinotopic Codes in the Human Hippocampus
- Authors: Angeli, P. A., Steel, A., Robertson, C. E.
- Meta: 2026-07-21 | neuroscience | DOI: 10.1101/2024.09.27.615397
- 中文摘要: 海马体被认为协调大脑中的感觉记忆信息流，代表视觉处理层次的顶点和记忆处理的中心枢纽。然而，人们对海马体感觉记忆相互作用的机制知之甚少。最近在皮质方面的研究表明，视网膜专题代码（通常被认为是视觉区域独有的）可能有助于通过对手的相互作用来组织皮质顶点的内部和外部信息。在这里，我们利用高分辨率 7T 功能 MRI 来测试二价视网膜专题代码是否在人类海马体内构建活动并介导海马-皮质相互作用。
- Abstract: The hippocampus is thought to coordinate sensory-mnemonic information streams in the brain, representing both the apex of the visual processing hierarchy and the central hub of mnemonic processing. Yet, the mechanisms underlying sensory-mnemonic interactions in the hippocampus are poorly understood. Recent work in cortex suggests that a retinotopic code - typically thought to be exclusive to visual areas - may help...
- Summary (fallback): 机器翻译摘要显示：海马体被认为协调大脑中的感觉记忆信息流，代表视觉处理层次的顶点和记忆处理的中心枢纽。然而，人们对海马体感觉记忆相互作用的机制知之甚少。最近在皮质方面的研究表明，视网膜专题代码（通常被认为是视觉区域独有的）可能有助于通过对手的相互作用来组织皮质顶点的内部和外部信息。在这里，我们利用高分辨率 7T 功能 MRI 来测试二价视网膜专题代码是否在人类海马体内构建活动并介导海马-皮质相互作用。
- Keywords: retinotopic, hippocampus, visual, processing, interactions

### 18. [杜氏利什曼原虫感染期间，与塞莫里细单胞菌共同感染可增强巨噬细胞的存活并促进细胞内寄生虫的持续存在](https://www.biorxiv.org/content/10.64898/2026.02.23.707439v3)
- Original title: Co-infection with Leptomonas seymouri enhances macrophage survival and promotes intracellular parasite persistence during Leishmania donovani infection
- Authors: Das, S., Sarkar, P. D., Biswas, S.
- Meta: 2026-07-21 | microbiology | DOI: 10.64898/2026.02.23.707439
- 中文摘要: 背景杜氏利什曼原虫（LD）是一种专性细胞内寄生虫，在巨噬细胞内存活和复制。塞摩利细单胞菌 (LS) 是一种传统的单性锥虫动物，在印度黑热病病例中多次与 LD 一起分离，通常与塞摩利细单胞菌 narna 样病毒 1 (Lepsey NLV1) 一起分离。 LS 是否能够在哺乳动物巨噬细胞内存活和复制，以及联合感染如何影响寄生虫和病毒动力学，这些问题仍然悬而未决。方法和结果 使用鼠巨噬细胞 (RAW 264.7) 和人巨噬细胞 (THP-1) 系统评估了单独 LS 以及与 LD 共感染期间 LS 的细胞内存活、复制和复活。定量 ITS1 PCR 表明，感染后 48-168 小时 (h.p.i) 内细胞内寄生虫 DNA 显着增加，表明复制活跃而不是持续存在。
- Abstract: Background Leishmania donovani (LD) is an obligate intracellular parasite that survives and replicates within macrophages. Leptomonas seymouri (LS), a traditionally monoxenous trypanosomatid, has been repeatedly co-isolated with LD from kala-azar cases in India, often together with Leptomonas seymouri narna-like virus 1 (Lepsey NLV1). Whether LS can survive and replicate within mammalian macrophages, and how co-infe...
- Summary (fallback): 机器翻译摘要显示：背景杜氏利什曼原虫（LD）是一种专性细胞内寄生虫，在巨噬细胞内存活和复制。塞摩利细单胞菌 (LS) 是一种传统的单性锥虫动物，在印度黑热病病例中多次与 LD 一起分离，通常与塞摩利细单胞菌 narna 样病毒 1 (Lepsey NLV1) 一起分离。 LS 是否能够在哺乳动物巨噬细胞内存活和复制，以及联合感染如何影响寄生虫和病毒动力学，这些问题仍然悬而未决。方法和结果 使用鼠巨噬细胞 (RAW 264.7) 和人巨噬细胞 (THP-1) 系统评估了单独 LS 以及与 LD 共感染期间 LS 的细胞内存活、复制和复活。定量 ITS1 PCR 表明，感染后 48-168 小时 (h.p.i) 内细胞内寄生虫 DNA 显着增加，表明复制活跃而不是持续存在。
- Keywords: co-infection, intracellular, macrophages, macrophage, survival

### 19. [hnRNPA1 和 hnRNPH1 对 HBZ 剪接的拮抗调节驱动 HTLV-1 白血病发生。](https://www.biorxiv.org/content/10.64898/2026.07.20.739521v1)
- Original title: Antagonistic regulation of HBZ splicing by hnRNPA1 and hnRNPH1 drives HTLV-1 leukemogenesis.
- Authors: Tram, J., Mourouvin, C., Marty, L., Marie-Delkasse, A., Lecante, A. et al.
- Meta: 2026-07-21 | molecular biology | DOI: 10.64898/2026.07.20.739521
- 中文摘要: 成人 T 细胞白血病/淋巴瘤 (ATL) 是一种由人类 T 细胞白血病病毒 1 型 (HTLV-1) 驱动的高度侵袭性白血病，目前的治疗方法在很大程度上仍然难以治愈。尽管 hbz 是急性 ATL 中唯一一致表达的病毒转录本，但其选择性剪接在多大程度上影响疾病生物学仍不清楚。在这里，我们证明了 hbz 剪接在驱动 ATL 癌症发展中发挥着关键作用。对 HTLV-1 感染的细胞系和原代样本的定量分析显示，ATL 患者的 CD4 T 细胞中剪接亚型 HBZ_SP1 显着富集（超过 200 倍），而未剪接转录本 (usHBZ) 在 CD8 T 细胞中占主导地位。尽管转录强劲，但 usHBZ 蛋白无法检测到，而 HBZ_SP1 快速积累，将其确定为 ATL 患者 CD4 T 细胞中的主要亚型。
- Abstract: Adult T-cell leukemia/lymphoma (ATL) is a highly aggressive leukemia driven by Human T-cell Leukemia Virus type 1 (HTLV-1) and remains largely refractory to current therapies. Although hbz is the only viral transcript consistently expressed in acute ATL, the extent to which its alternative splicing shapes disease biology remains unknown. Here, we demonstrate that the splicing of hbz plays a key role in driving cance...
- Summary (fallback): 机器翻译摘要显示：成人 T 细胞白血病/淋巴瘤 (ATL) 是一种由人类 T 细胞白血病病毒 1 型 (HTLV-1) 驱动的高度侵袭性白血病，目前的治疗方法在很大程度上仍然难以治愈。尽管 hbz 是急性 ATL 中唯一一致表达的病毒转录本，但其选择性剪接在多大程度上影响疾病生物学仍不清楚。在这里，我们证明了 hbz 剪接在驱动 ATL 癌症发展中发挥着关键作用。对 HTLV-1 感染的细胞系和原代样本的定量分析显示，ATL 患者的 CD4 T 细胞中剪接亚型 HBZ_SP1 显着富集（超过 200 倍），而未剪接转录本 (usHBZ) 在 CD8 T 细胞中占主导地位。尽管转录强劲，但 usHBZ 蛋白无法检测到，而 HBZ_SP1 快速积累，将其确定为 ATL 患者 CD4 T 细胞中的主要亚型。
- Keywords: splicing, isoform, hnrnpa1, hnrnph1, htlv-1

### 20. [利用胶原蛋白无创精密分子 MRI 揭示多囊肾病的早期肾纤维化](https://www.biorxiv.org/content/10.64898/2026.07.19.739445v1)
- Original title: Unmasking Early Renal Fibrosis in Polycystic Kidney Disease Using Noninvasive Precision Molecular MRI of Collagen
- Authors: Bamishaye, O. S., Akinlotan, F., Qiao, J., Chumley, P. H., Dorabadizare, F. et al.
- Meta: 2026-07-21 | molecular biology | DOI: 10.64898/2026.07.19.739445
- 中文摘要: 细胞外基质的纤维化重塑是常染色体显性多囊肾病（ADPKD）从疾病早期阶段开始进展的核心驱动因素。不幸的是，在不可逆转的结构和功能衰退之前，无法使用现有的方法对其进行评估，从而造成诊断盲点，阻碍准确的早期风险分层和管理。在这里，我们报告 Gd-hProCA32 的开发。 Collagen 是一种胶原蛋白靶向蛋白 MRI 造影剂，可在传统实验室和成像方法检测 Pkhd1PCK/PCK (PCK) 大鼠和 Pkd2 突变小鼠的肾脏和肝脏变化之前，通过直接对体内 I 型胶原沉积进行成像，实现早期纤维化的精确分子 MRI (pMRI)。 Gd-hProCA32。
- Abstract: Fibrotic remodeling of extracellular matrix is a central driver of autosomal dominant polycystic kidney disease (ADPKD) progression since early stages of the disease. Unfortunately, it cannot be assessed with currently available methodologies before irreversible structural and functional decline, creating a diagnostic blind spot that hinders accurate early risk stratification and management. Here, we report the deve...
- Summary (fallback): 机器翻译摘要显示：细胞外基质的纤维化重塑是常染色体显性多囊肾病（ADPKD）从疾病早期阶段开始进展的核心驱动因素。不幸的是，在不可逆转的结构和功能衰退之前，无法使用现有的方法对其进行评估，从而造成诊断盲点，阻碍准确的早期风险分层和管理。在这里，我们报告 Gd-hProCA32 的开发。 Collagen 是一种胶原蛋白靶向蛋白 MRI 造影剂，可在传统实验室和成像方法检测 Pkhd1PCK/PCK (PCK) 大鼠和 Pkd2 突变小鼠的肾脏和肝脏变化之前，通过直接对体内 I 型胶原沉积进行成像，实现早期纤维化的精确分子 MRI (pMRI)。 Gd-hProCA32。
- Keywords: collagen, early, kidney, disease, gd-hproca32

### 21. [致病性 MYBPC3 错义变异改变肌节内蛋白质-蛋白质相互作用](https://www.biorxiv.org/content/10.64898/2026.05.27.727676v3)
- Original title: Pathogenic MYBPC3 missense variants alter protein-protein interactions within the sarcomere
- Authors: Thompson, A. D., Pankiewicz, C., Plenge, L. S., Lilienthal, U., Kotaru, S. et al.
- Meta: 2026-07-21 | cell biology | DOI: 10.64898/2026.05.27.727676
- 中文摘要: 背景：肥厚性心肌病（HCM）是一种遗传性心脏病，可导致左心室肥厚、心力衰竭和心律失常。肌球蛋白结合蛋白 C (MYBPC3) 基因的致病性错义变异聚集在其内部子域 C3 和 C6 内。携带这些错义变异的蛋白质 (MyBP-C) 通常定位于肌丝，因此导致 HCM 的机制存在不确定性。
- Abstract: Background: Hypertrophic cardiomyopathy (HCM) is a genetic heart disease that leads to left ventricular hypertrophy, heart failure, and arrhythmias. Pathogenic missense variants in the gene myosin binding protein C (MYBPC3) cluster within its internal subdomains C3 and C6. The protein (MyBP-C), carrying these missense variants, localizes normally to the myofilaments, leaving uncertainty regarding the mechanism(s) by...
- Summary (fallback): 机器翻译摘要显示：背景：肥厚性心肌病（HCM）是一种遗传性心脏病，可导致左心室肥厚、心力衰竭和心律失常。肌球蛋白结合蛋白 C (MYBPC3) 基因的致病性错义变异聚集在其内部子域 C3 和 C6 内。携带这些错义变异的蛋白质 (MyBP-C) 通常定位于肌丝，因此导致 HCM 的机制存在不确定性。
- Keywords: mybp-c, variants, missense, pathogenic, proximity

### 22. [海藻与珊瑚全生物的基于接触和扩散的化感相互作用](https://www.biorxiv.org/content/10.64898/2026.07.20.739502v1)
- Original title: Contact- and diffusion-based allelopathic interaction of a seaweed with coral holobionts
- Authors: Tang, P. Y. P., Pereyra, J. P. A., Lee, L. K., McDougald, D., Rice, S. A. et al.
- Meta: 2026-07-21 | ecology | DOI: 10.64898/2026.07.20.739502
- 中文摘要: 在全球许多沿海地区，从珊瑚为主的珊瑚礁系统向大型藻类为主的珊瑚礁系统的转变变得越来越普遍。珊瑚与巨藻的相互作用已被证明对珊瑚健康普遍有害，巨藻化感化合物能够对处于不同生长和发育阶段的珊瑚产生严重甚至致命的影响。先前的研究表明，与珊瑚相关的微生物群落在珊瑚健康和减轻外部环境压力（包括巨藻接触压力）方面发挥着重要作用。然而，目前尚不清楚珊瑚微生物组的变化是否会对共生科群落组成产生影响，以及这些变化是否会随后影响珊瑚的健康。
- Abstract: Shifts from coral-dominated to macroalgal-dominated reef systems have become increasingly common in many coastal regions worldwide. Coral-macroalgal interactions have been shown to be generally detrimental to coral health, with macroalgal allelopathic compounds able to exert serious and even lethal effects on coral at various stages of growth and development. Previous studies have shown that the coral-associated mic...
- Summary (fallback): 机器翻译摘要显示：在全球许多沿海地区，从珊瑚为主的珊瑚礁系统向大型藻类为主的珊瑚礁系统的转变变得越来越普遍。珊瑚与巨藻的相互作用已被证明对珊瑚健康普遍有害，巨藻化感化合物能够对处于不同生长和发育阶段的珊瑚产生严重甚至致命的影响。先前的研究表明，与珊瑚相关的微生物群落在珊瑚健康和减轻外部环境压力（包括巨藻接触压力）方面发挥着重要作用。然而，目前尚不清楚珊瑚微生物组的变化是否会对共生科群落组成产生影响，以及这些变化是否会随后影响珊瑚的健康。
- Keywords: coral, macroalgal, communities, contact, symbiodiniaceae

### 23. [禽类疟疾寄生虫 Haemoproteus Majoris（WW2 谱系）的基因组及其与其他疟原虫物种的关系](https://www.biorxiv.org/content/10.64898/2026.07.13.738139v2)
- Original title: The genome of the avian malaria parasite Haemoproteus majoris (lineage WW2) and its relationship to other Plasmodium species
- Authors: Bardil, A., Berthomieu, A., Dainat, J., Fontaine, M. C., Hellgren, O. et al.
- Meta: 2026-07-21 | genomics | DOI: 10.64898/2026.07.13.738139
- 中文摘要: 禽疟原虫在血孢子虫中形成了一个高度流行且遗传多样性的群体，但相对于感染人类和啮齿动物的同类，它们长期以来一直被忽视。其中，血变形虫属（Haemosporidae、Haemoproteidae）寄生虫是鸟类广泛流行的血液寄生虫，由虱蝇（Hippoboscidae）和叮蠓（Ceratopogonidae）传播。最近的系统发育学分析将血变形菌属寄生虫置于血孢子虫树的根部，使得这些类群的基因组数据对于了解疟疾寄生虫的进化起源至关重要。迄今为止，仅对两种禽类疟原虫和一种禽类嗜血变形菌基因组进行了测序。我们展示了第一个组装的大型嗜血变形菌（WW2 谱系）基因组，这是雀形目鸟类常见的血液寄生虫。
- Abstract: Avian malaria parasites form a highly prevalent and genetically diverse group within the haemosporidians, yet they have long been overlooked relative to their human- and rodent-infecting counterparts. Among these, parasites of the genus Haemoproteus (Haemosporida, Haemoproteidae) are widespread and prevalent blood parasites of birds, transmitted by louse flies (Hippoboscidae) and biting midges (Ceratopogonidae). Rec...
- Summary (fallback): 机器翻译摘要显示：禽疟原虫在血孢子虫中形成了一个高度流行且遗传多样性的群体，但相对于感染人类和啮齿动物的同类，它们长期以来一直被忽视。其中，血变形虫属（Haemosporidae、Haemoproteidae）寄生虫是鸟类广泛流行的血液寄生虫，由虱蝇（Hippoboscidae）和叮蠓（Ceratopogonidae）传播。最近的系统发育学分析将血变形菌属寄生虫置于血孢子虫树的根部，使得这些类群的基因组数据对于了解疟疾寄生虫的进化起源至关重要。迄今为止，仅对两种禽类疟原虫和一种禽类嗜血变形菌基因组进行了测序。我们展示了第一个组装的大型嗜血变形菌（WW2 谱系）基因组，这是雀形目鸟类常见的血液寄生虫。
- Keywords: avian, parasites, haemoproteus, genome, malaria

### 24. [从精原细胞角度观察哺乳动物大脑的扩张](https://www.biorxiv.org/content/10.1101/2025.09.15.676184v3)
- Original title: A spermatogonial perspective on the expansion of the mammalian brain
- Authors: Bush, S. J., Goriely, A.
- Meta: 2026-07-21 | genomics | DOI: 10.1101/2025.09.15.676184
- 中文摘要: 大脑和睾丸有许多分子相似之处，但这种重叠的进化意义仍不清楚。我们之前假设，在整个进化过程中，一些有助于大脑尺寸扩张的遗传变异首先出现在精原细胞中，它们通过“自私的精原细胞选择”（类似于肿瘤发生的过程）赋予雄性生殖干细胞选择性优势。一旦传递到下一代，这些自私的变异就成为组成型的，不成比例地积累在活跃于精子发生和神经发生并调节干细胞增殖的信号通路中。然而，检验这一假设受到了精原细胞相对稀缺和单细胞转录组分析固有的随机性的阻碍。
- Abstract: The brain and testis share many molecular similarities, yet the evolutionary implications of this overlap remain unclear. We have previously hypothesised that, throughout evolution, some genetic variants contributing to brain size expansion first arose in spermatogonia where they conferred a selective advantage to the male germline stem cells via 'selfish spermatogonial selection', a process analogous to oncogenesis...
- Summary (fallback): 机器翻译摘要显示：大脑和睾丸有许多分子相似之处，但这种重叠的进化意义仍不清楚。我们之前假设，在整个进化过程中，一些有助于大脑尺寸扩张的遗传变异首先出现在精原细胞中，它们通过“自私的精原细胞选择”（类似于肿瘤发生的过程）赋予雄性生殖干细胞选择性优势。一旦传递到下一代，这些自私的变异就成为组成型的，不成比例地积累在活跃于精子发生和神经发生并调节干细胞增殖的信号通路中。然而，检验这一假设受到了精原细胞相对稀缺和单细胞转录组分析固有的随机性的阻碍。
- Keywords: brain, spermatogonia, evolutionary, spermatogonial, expansion

### 25. [超分子水凝胶粘弹性调节原位三级淋巴新生](https://www.biorxiv.org/content/10.64898/2026.07.20.739456v1)
- Original title: Supramolecular hydrogel viscoelasticity regulates in situ tertiary lymphoid neogenesis
- Authors: Hosn, R. R., Marrone Mantovani, O., Margaronis, A., Wang, J. S., Kriss, E. et al.
- Meta: 2026-07-21 | bioengineering | DOI: 10.64898/2026.07.20.739456
- 中文摘要: 三级淋巴结构（TLS）是有组织的三维免疫生态位，与改善的抗肿瘤免疫力相关，这促使人们努力使用生物材料人工诱导它们。然而，这些策略主要集中在可溶性线索传递上，而对支架物理性质的作用知之甚少。在这里，我们开发了可注射的脂质体交联超分子水凝胶，涵盖柔软和坚硬的配方，以确定支架机械性能如何调节原位三级淋巴新生。这些制剂的粘弹性特性有所不同，同时卵清蛋白和 LIGHT 的释放量保持大致可比。
- Abstract: Tertiary lymphoid structures (TLSs) are organized three-dimensional immune niches associated with improved antitumor immunity, which has galvanized efforts to induce them artificially using biomaterials. However, these strategies have largely focused on soluble cue delivery, leaving the role of scaffold physical properties poorly understood. Here, we developed injectable, liposome-crosslinked supramolecular hydrogel...
- Summary (fallback): 机器翻译摘要显示：三级淋巴结构（TLS）是有组织的三维免疫生态位，与改善的抗肿瘤免疫力相关，这促使人们努力使用生物材料人工诱导它们。然而，这些策略主要集中在可溶性线索传递上，而对支架物理性质的作用知之甚少。在这里，我们开发了可注射的脂质体交联超分子水凝胶，涵盖柔软和坚硬的配方，以确定支架机械性能如何调节原位三级淋巴新生。这些制剂的粘弹性特性有所不同，同时卵清蛋白和 LIGHT 的释放量保持大致可比。
- Keywords: lymphoid, hydrogels, tertiary, scaffold, properties

### 26. [使用消费类智能手表进行边缘优先地面反作用力估计](https://www.biorxiv.org/content/10.64898/2026.07.18.739307v1)
- Original title: Edge-First Ground Reaction Force Estimation with Consumer Smartwatches
- Authors: Ghaffarzadeh, P., Chakraborty, D., Aslansefat, K., Dostan, A., Papadopoulos, Y.
- Meta: 2026-07-21 | bioengineering | DOI: 10.64898/2026.07.18.739307
- 中文摘要: 地面反作用力（GRF）测量仍然主要局限于仪器实验室，限制了日常生活中的纵向监测。本文介绍了一种边缘优先的可穿戴系统，用于估算消费类智能手表的垂直 GRF。佩戴在手腕和腰部的两个 Apple Watch Series 6 设备以 100 Hz 的频率将 12 通道惯性数据传输到 iPhone，其中预处理、存储和推理在本地进行，无需依赖云。所提出的 GRFNet-MultiScale 模型是一个紧凑的时间卷积网络，具有四个扩张的残差块和一个全局上下文分支。在对 10 名健康参与者的 539 个姿势窗口进行留一主题评估时，双传感器系统的平均 Pearson 相关性为 0.798，RMSE 为 257 N，而仅手腕配置保留了 82.5% 的双传感器相关性。
- Abstract: Ground reaction force (GRF) measurement remains largely confined to instrumented laboratories, limiting longitudinal monitoring in daily life. This article presents an edge-first wearable system for estimating vertical GRF from consumer smartwatches. Two Apple Watch Series 6 devices worn at the wrist and waist stream 12-channel inertial data at 100 Hz to an iPhone, where preprocessing, storage, and inference occur l...
- Summary (fallback): 机器翻译摘要显示：地面反作用力（GRF）测量仍然主要局限于仪器实验室，限制了日常生活中的纵向监测。本文介绍了一种边缘优先的可穿戴系统，用于估算消费类智能手表的垂直 GRF。佩戴在手腕和腰部的两个 Apple Watch Series 6 设备以 100 Hz 的频率将 12 通道惯性数据传输到 iPhone，其中预处理、存储和推理在本地进行，无需依赖云。所提出的 GRFNet-MultiScale 模型是一个紧凑的时间卷积网络，具有四个扩张的残差块和一个全局上下文分支。在对 10 名健康参与者的 539 个姿势窗口进行留一主题评估时，双传感器系统的平均 Pearson 相关性为 0.798，RMSE 为 257 N，而仅手腕配置保留了 82.5% 的双传感器相关性。
- Keywords: system, edge-first, ground, reaction, force

### 27. [人类基因组中的一组新的 DNA 甲基化变异显示出主要的组织特异性和对重编程的敏感性，并具有潜在的疾病易感性。](https://www.biorxiv.org/content/10.64898/2026.07.18.738653v1)
- Original title: A new set of DNA methylation variants in the human genome show predominant tissue specificity and sensitivity to reprogramming with a potential for disease susceptibility.
- Authors: Anne, A., Kumar, L., Singh, M., Choudhury, S., Das, S. et al.
- Meta: 2026-07-21 | bioinformatics | DOI: 10.64898/2026.07.18.738653
- 中文摘要: 对 3,370 个外胚层、内胚层和中胚层来源的正常人体组织进行分析，确定了 12,587 个平均约 585 bp 的区域，相同组织内 DNA 甲基化水平存在显着差异。这些甲基化变异 (MeVars) 存在于富含神经系统疾病和癌症的 8,037 个基因中，其中大多数是组织特异性的，而不是系统性的。通过在体外重新编程为 iPSC 以及在体内在精子发生过程中重新编程，可以减少这种体细胞变异。前额皮质分析显示，对照组候选基因中 MeVar 的发生率高于精神分裂症患者，其中一部分患者的转录水平显着改变。口腔组织和皮肤成纤维细胞也观察到类似的效果。
- Abstract: Analyses of 3,370 normal human tissues of ectodermal, endodermal and mesodermal origins identified 12,587 regions averaging ~585 bp with significant differences in DNA methylation levels within identical tissues. These methylation variants (MeVars) occurred in 8,037 genes enriched in neurological disorders and cancers of which, majority were tissue-specific rather than being systemic. This somatic variation was redu...
- Summary (fallback): 机器翻译摘要显示：对 3,370 个外胚层、内胚层和中胚层来源的正常人体组织进行分析，确定了 12,587 个平均约 585 bp 的区域，相同组织内 DNA 甲基化水平存在显着差异。这些甲基化变异 (MeVars) 存在于富含神经系统疾病和癌症的 8,037 个基因中，其中大多数是组织特异性的，而不是系统性的。通过在体外重新编程为 iPSC 以及在体内在精子发生过程中重新编程，可以减少这种体细胞变异。前额皮质分析显示，对照组候选基因中 MeVar 的发生率高于精神分裂症患者，其中一部分患者的转录水平显着改变。口腔组织和皮肤成纤维细胞也观察到类似的效果。
- Keywords: mevars, methylation, reprogramming, tissues, showed

### 28. [缺氧反应通过生物胺能和肽能神经回路延长寿命。](https://www.biorxiv.org/content/10.1101/2025.05.04.652087v2)
- Original title: The hypoxic response extends lifespan through a bioaminergic and peptidergic neural circuit.
- Authors: Kitto, E. S., Huang, S., Bhandari, M., Tian, C., Cox, R. L. et al.
- Meta: 2026-07-21 | physiology | DOI: 10.1101/2025.05.04.652087
- 中文摘要: 对压力的协调反应对于促进有机体的短期和长期健康至关重要。通常通过神经系统对压力的感知会导致生理变化，而这对于维持体内平衡至关重要。激活对低氧或缺氧的反应可以延长线虫的健康寿命和寿命。然而，尽管有一些积极的影响，但特定组织中缺氧反应的负面影响阻碍了它们在哺乳动物中的益处。因此，必须确定这种反应的哪些成分可以促进长寿。在这里，我们探讨了缺氧反应基因激活下游的细胞非自主信号通路。我们发现 ADF 血清素能神经元中 HIF-1 介导的信号传导对于延长寿命来说既是必要的也是充分的。
- Abstract: A coordinated response to stress is crucial for promoting the short- and long-term health of an organism. The perception of stress, frequently through the nervous system, can lead to physiological changes that are fundamental to maintaining homeostasis. Activating the response to low oxygen, or hypoxia, extends healthspan and lifespan in C. elegans. However, despite some positive impacts, negative effects of the hyp...
- Summary (fallback): 机器翻译摘要显示：对压力的协调反应对于促进有机体的短期和长期健康至关重要。通常通过神经系统对压力的感知会导致生理变化，而这对于维持体内平衡至关重要。激活对低氧或缺氧的反应可以延长线虫的健康寿命和寿命。然而，尽管有一些积极的影响，但特定组织中缺氧反应的负面影响阻碍了它们在哺乳动物中的益处。因此，必须确定这种反应的哪些成分可以促进长寿。在这里，我们探讨了缺氧反应基因激活下游的细胞非自主信号通路。我们发现 ADF 血清素能神经元中 HIF-1 介导的信号传导对于延长寿命来说既是必要的也是充分的。
- Keywords: response, hypoxic, signaling, lifespan, through

### 29. [母亲缺铁会重塑心脏线粒体并改变高血压妊娠的应激反应](https://www.biorxiv.org/content/10.64898/2026.05.12.724698v2)
- Original title: Maternal iron deficiency remodels cardiac mitochondria and alters stress responses in hypertensive pregnancy
- Authors: Rachid, J.-J. R., Holody, C. D., Liu, S. N., Roshmi, R. R., Badhan, N. S. et al.
- Meta: 2026-07-21 | physiology | DOI: 10.64898/2026.05.12.724698
- 中文摘要: 怀孕期间母亲缺铁（ID）与心血管适应有关，包括高血压妊娠期间血压降低和心脏效率提高。然而，这些明显的功能增益是否伴随着心脏线粒体功能的保留仍不清楚。鉴于母体心脏的高代谢需求和铁在氧化代谢中的核心作用，我们研究了母体 ID 如何影响妊娠自发性高血压大鼠 (SHR) 和正常血压 Wistar-Kyoto (WKY) 大鼠的心脏线粒体超微结构、呼吸、动力学和氧化还原状态。雌性 SHR 和 WKY 大鼠在妊娠前和整个妊娠期间接受铁充足或铁限制饮食。
- Abstract: Maternal iron deficiency (ID) during pregnancy is associated with cardiovascular adaptations, including reduced blood pressure and improved cardiac efficiency in hypertensive pregnancy. However, whether these apparent functional gains are accompanied by preserved cardiac mitochondrial function remains unclear. Given the high metabolic demands of the maternal heart and irons central role in oxidative metabolism, we e...
- Summary (fallback): 机器翻译摘要显示：怀孕期间母亲缺铁（ID）与心血管适应有关，包括高血压妊娠期间血压降低和心脏效率提高。然而，这些明显的功能增益是否伴随着心脏线粒体功能的保留仍不清楚。鉴于母体心脏的高代谢需求和铁在氧化代谢中的核心作用，我们研究了母体 ID 如何影响妊娠自发性高血压大鼠 (SHR) 和正常血压 Wistar-Kyoto (WKY) 大鼠的心脏线粒体超微结构、呼吸、动力学和氧化还原状态。雌性 SHR 和 WKY 大鼠在妊娠前和整个妊娠期间接受铁充足或铁限制饮食。
- Keywords: maternal, cardiac, mitochondrial, iron, hypertensive

### 30. [从头整合域的计算设计能够合理控制植物 NLR 免疫受体中病原体效应子的识别。](https://www.biorxiv.org/content/10.64898/2026.07.10.737686v2)
- Original title: Computational design of de novo integrated domains enables rational control of pathogen effector recognition in plant NLR immune receptors.
- Authors: Xi, Y., Bucknell, A. H., Watson, J. L., Maqbool, A., Bennett, J. W. et al.
- Meta: 2026-07-21 | plant biology | DOI: 10.64898/2026.07.10.737686
- 中文摘要: 植物病原体的快速进化对全球农业的可持续发展构成了持续的威胁，其速度往往超过了自然抗病基因的发现和部署。虽然植物细胞内免疫受体（NLR）的生物工程提供了一种潜在的解决方案，但开发定制的免疫识别仍然受到天然受体和植物-病原体相互作用的费力表征的限制。在这里，我们描述了一个可编程框架，该框架利用生成式 AI 蛋白质设计工具 RFdiffusion 和 ProteinMPNN，来设计针对不同病原体效应子的从头集成域 (ID)。通过将这些定制的结合剂集成到模块化稻瘟病 Pik-1/Pik-2 NLR 受体底盘中，我们成功地识别了巴拿马疾病病原体尖孢镰刀菌 (Fusarium oxysporum f) 的非同源毒力因子（效应子）。 sp。 cubense 热带种族 4。
- Abstract: The rapid evolution of plant pathogens poses a persistent threat to global agricultural sustainability, often outpacing the discovery and deployment of natural disease resistance genes. While bioengineering of plant intracellular immune receptors (NLRs) offers a potential solution, developing bespoke immune recognition remains constrained by the laborious characterisation of natural receptors and plant-pathogen inte...
- Summary (fallback): 机器翻译摘要显示：植物病原体的快速进化对全球农业的可持续发展构成了持续的威胁，其速度往往超过了自然抗病基因的发现和部署。虽然植物细胞内免疫受体（NLR）的生物工程提供了一种潜在的解决方案，但开发定制的免疫识别仍然受到天然受体和植物-病原体相互作用的费力表征的限制。在这里，我们描述了一个可编程框架，该框架利用生成式 AI 蛋白质设计工具 RFdiffusion 和 ProteinMPNN，来设计针对不同病原体效应子的从头集成域 (ID)。通过将这些定制的结合剂集成到模块化稻瘟病 Pik-1/Pik-2 NLR 受体底盘中，我们成功地识别了巴拿马疾病病原体尖孢镰刀菌 (Fusarium oxysporum f) 的非同源毒力因子（效应子）。 sp。 cubense 热带种族 4。
- Keywords: domains, immune, novo, integrated, plant

## medrxiv

### 1. [更年期的血液蛋白质组学与大脑衰老和痴呆风险相关](https://www.medrxiv.org/content/10.64898/2026.02.09.26345907v2)
- Original title: Blood proteomics of menopause map to brain aging and dementia risk
- Authors: Wood Alexander, M., Rabin, J. S., Caunca, M., Iadipaolo, A., Cornelis, L. et al.
- Meta: 2026-07-21 | neurology | DOI: 10.64898/2026.02.09.26345907
- 中文摘要: 更年期是生物衰老的一个标志性过程，与后来的神经退行性风险有关。我们利用来自多个队列的蛋白质组学数据来确定更年期潜在的生物学变化及其与大脑衰老的联系。在 N = 80 名经过严格分期 (STRAW+10) 的绝经前、围绝经期和绝经后女性中，通过血清 NULISAseq 蛋白质组学发现，自发绝经的特点是炎症、突触、代谢和阿尔茨海默氏病生物过程的失调，与激素的关系比年龄的关系更强烈。对年龄匹配的绝经前/围绝经期与绝经后女性进行血浆 Olink 蛋白质组学 (N=2,814) 的验证分析重复了观察到的蛋白质组变化，并揭示了更广泛的与更年期相关的炎症和分解代谢过程的上调，以及加速的器官和细胞衰老，包括大脑衰老。
- Abstract: Menopause is a hallmark process in biological aging that has been implicated in later neurodegenerative risk. We leveraged proteomics data from multiple cohorts to identify biological changes underlying menopause and its links to brain aging. In N=80 rigorously staged (STRAW+10) pre-, peri-, and postmenopausal women with serum NULISAseq proteomics, spontaneous menopause was characterized by dysregulation in inflamma...
- Summary (fallback): 机器翻译摘要显示：更年期是生物衰老的一个标志性过程，与后来的神经退行性风险有关。我们利用来自多个队列的蛋白质组学数据来确定更年期潜在的生物学变化及其与大脑衰老的联系。在 N = 80 名经过严格分期 (STRAW+10) 的绝经前、围绝经期和绝经后女性中，通过血清 NULISAseq 蛋白质组学发现，自发绝经的特点是炎症、突触、代谢和阿尔茨海默氏病生物过程的失调，与激素的关系比年龄的关系更强烈。对年龄匹配的绝经前/围绝经期与绝经后女性进行血浆 Olink 蛋白质组学 (N=2,814) 的验证分析重复了观察到的蛋白质组变化，并揭示了更广泛的与更年期相关的炎症和分解代谢过程的上调，以及加速的器官和细胞衰老，包括大脑衰老。
- Keywords: menopause, aging, proteomics, brain, women

### 2. [超越强度：疼痛分布影响有或没有临床疼痛的个体寻求医疗保健和治疗的信念](https://www.medrxiv.org/content/10.64898/2026.04.02.26349577v2)
- Original title: Beyond intensity: Pain distribution shapes healthcare- and treatment-seeking beliefs in individuals with and without clinical pain
- Authors: Frankenstein, T., Intert, S., Szikszay, T. M., Katra, M., Elsner, B. et al.
- Meta: 2026-07-21 | pain medicine | DOI: 10.64898/2026.04.02.26349577
- 中文摘要: 疼痛通常用感觉术语来描述，但其空间特征（定位和分布）很少被量化。我们调查了关于疼痛分布的非专业信念是否影响寻求护理和治疗偏好的理论决策。在一项横断面调查中（N=503；49% 的人报告疼痛），参与者完成了思想实验，其中视觉呈现的疼痛分布模式（小、中或大）和疼痛强度（数字评定量表分数：2、5、8/10）都有系统性的变化。对于每种情况，他们评估了 (i) 寻求专业帮助 (LoSH) 和 (ii) 服用镇痛药物 (LoTM) 的可能性。参与者还完成了一项空间强度权衡任务，其中他们在固定的强度减少 20% 和疼痛分布的可变减少 (20-80%) 之间进行选择。
- Abstract: Pain is commonly described in sensory terms, yet its spatial characteristics-localization and distribution-are rarely quantified. We investigated whether lay beliefs about pain distribution influence theoretical decisions to seek care and treatment preferences. In a cross-sectional survey (N=503; 49% reporting pain), participants completed thought experiments in which both visually presented pain distribution patter...
- Summary (fallback): 机器翻译摘要显示：疼痛通常用感觉术语来描述，但其空间特征（定位和分布）很少被量化。我们调查了关于疼痛分布的非专业信念是否影响寻求护理和治疗偏好的理论决策。在一项横断面调查中（N=503；49% 的人报告疼痛），参与者完成了思想实验，其中视觉呈现的疼痛分布模式（小、中或大）和疼痛强度（数字评定量表分数：2、5、8/10）都有系统性的变化。对于每种情况，他们评估了 (i) 寻求专业帮助 (LoSH) 和 (ii) 服用镇痛药物 (LoTM) 的可能性。参与者还完成了一项空间强度权衡任务，其中他们在固定的强度减少 20% 和疼痛分布的可变减少 (20-80%) 之间进行选择。
- Keywords: pain, distribution, intensity, individuals, reduction

### 3. [急诊科成人菌血症多变量回归模型的开发和外部验证](https://www.medrxiv.org/content/10.64898/2026.07.17.26358264v2)
- Original title: Development and external validation of a multivariable regression model for bacteraemia in adults presenting to emergency departments
- Authors: Samuels, T. H., Forrest-Hammond, R., Stockford, C., Harris, S. K., Eyre, D. W. et al.
- Meta: 2026-07-21 | infectious diseases | DOI: 10.64898/2026.07.17.26358264
- 中文摘要: 背景：菌血症与不良预后相关，但诊断金标准（外周血培养）需要长达 24 小时才能在临床上采取行动，这阻碍了疑似感染的早期管理决策。单一预测因子​​和现有脓毒症风险评分的区分效果较差，并且很少有多变量菌血症模型在英国人群中得到充分验证。方法：我们开发了一个逻辑回归模型，在 2019 年至 2024 年间伦敦大学学院医院 (UCLH) 33,874 例医院就诊的回顾性队列中，使用基于 AIC 的向后选择预定义候选预测因子，这些预测因子通常在就诊后数小时内可用。使用限制三次样条对连续预测因子进行建模，并使用多重插补处理缺失数据。
- Abstract: Background: Bacteraemia is associated with poor outcomes but the diagnostic gold standard, peripheral blood culture, takes up to 24 hours to become clinically actionable, hampering early management decisions in suspected infection. Single predictors and existing sepsis risk scores discriminate poorly, and few multivariable bacteraemia models have been adequately validated in UK populations. Methods: We developed a l...
- Summary (fallback): 机器翻译摘要显示：背景：菌血症与不良预后相关，但诊断金标准（外周血培养）需要长达 24 小时才能在临床上采取行动，这阻碍了疑似感染的早期管理决策。单一预测因子​​和现有脓毒症风险评分的区分效果较差，并且很少有多变量菌血症模型在英国人群中得到充分验证。方法：我们开发了一个逻辑回归模型，在 2019 年至 2024 年间伦敦大学学院医院 (UCLH) 33,874 例医院就诊的回顾性队列中，使用基于 AIC 的向后选择预定义候选预测因子，这些预测因子通常在就诊后数小时内可用。使用限制三次样条对连续预测因子进行建模，并使用多重插补处理缺失数据。
- Keywords: validation, external, model, bacteraemia, predictors

### 4. [体力活动和 2 型糖尿病风险：肥胖和年龄的剂量反应异质性](https://www.medrxiv.org/content/10.1101/2025.10.19.25338324v2)
- Original title: Physical Activity and Type 2 Diabetes Risk: Heterogeneity in the Dose-Response by Obesity and Age
- Authors: liu, j., zeng, q.
- Meta: 2026-07-21 | geriatric medicine | DOI: 10.1101/2025.10.19.25338324
- 中文摘要: 背景 患有严重精神障碍的人是糖尿病及其并发症的高危人群。缺乏身体活动和久坐行为是 2 型糖尿病 (T2DM) 合并症的共同行为风险因素。然而，体力活动（PA）对 T2DM 的保护作用是否会因肥胖和年龄而改变，及其具体的剂量反应关系仍不清楚。方法 本研究利用了 2017-2020 年国家健康和营养检查调查 (NHANES) 中 5,042 名成年人的横断面数据。采用加权多变量逻辑回归和限制三次样条 (RCS) 模型来分析 PA 和 T2DM 风险之间的关联，并评估 BMI 和年龄的潜在影响修正。结果调整混杂因素后，较高水平的 PA 与较低的糖尿病风险独立相关。
- Abstract: Background Individuals with severe mental disorders represent a very high-risk population for diabetes and its complications. Physical inactivity and sedentary behavior are shared behavioral risk factors for type 2 diabetes (T2DM) comorbidity. However, whether the protective effect of physical activity (PA) on T2DM is modified by obesity and age, and its specific dose-response relationship, remain unclear. Methods T...
- Summary (fallback): 机器翻译摘要显示：背景 患有严重精神障碍的人是糖尿病及其并发症的高危人群。缺乏身体活动和久坐行为是 2 型糖尿病 (T2DM) 合并症的共同行为风险因素。然而，体力活动（PA）对 T2DM 的保护作用是否会因肥胖和年龄而改变，及其具体的剂量反应关系仍不清楚。方法 本研究利用了 2017-2020 年国家健康和营养检查调查 (NHANES) 中 5,042 名成年人的横断面数据。采用加权多变量逻辑回归和限制三次样条 (RCS) 模型来分析 PA 和 T2DM 风险之间的关联，并评估 BMI 和年龄的潜在影响修正。结果调整混杂因素后，较高水平的 PA 与较低的糖尿病风险独立相关。
- Keywords: effect, diabetes, risk, obesity, t2dm

### 5. [索马里与疟疾诊断和青蒿素部分耐药相关的基因突变的出现：基因组监测研究](https://www.medrxiv.org/content/10.64898/2026.07.19.26357122v1)
- Original title: Emergence of Genetic Mutations associated with Malaria Diagnostic and Artemisinin Partial Resistance in Somalia: A Genomic Surveillance Study
- Authors: Arale, A. M., Hassan, A. H., Mahmoud, A. I., Rey, J., la Fuente, I. M.-d. et al.
- Meta: 2026-07-21 | infectious diseases | DOI: 10.64898/2026.07.19.26357122
- 中文摘要: 基于富含组氨酸蛋白 2 (HRP2) 的快速诊断测试 (RDT) 是非洲疟疾病例管理的核心，但当恶性疟原虫寄生虫缺乏 pfhrp2 或 pfhrp3 基因时，就会失败。厄立特里亚、埃塞俄比亚和吉布提报告了广泛的删除情况，但索马里尚未提供系统数据。 2023 年 5 月至 10 月期间，我们从索马里 7 个地区的 8 个医疗机构就诊的疑似疟疾患者收集了 7148 份干血斑 (DBS) 样本。进行了现场 HRP2/泛乳酸脱氢酶 (LDH) RDT 和显微镜检查，并从 301 个 RDT 阳性和 173 个 RDT 阴性 DBS 样本中提取了 DNA。
- Abstract: Histidine-rich protein 2 (HRP2)-based rapid diagnostic tests (RDTs) are central to malaria case management in Africa but fail when Plasmodium falciparum parasites lack the pfhrp2 or pfhrp3 genes. Widespread deletions have been reported in Eritrea, Ethiopia, and Djibouti, yet no systematic data have been available from Somalia. Between May and October 2023, we collected 7148 dried blood spot (DBS) samples from patien...
- Summary (fallback): 机器翻译摘要显示：基于富含组氨酸蛋白 2 (HRP2) 的快速诊断测试 (RDT) 是非洲疟疾病例管理的核心，但当恶性疟原虫寄生虫缺乏 pfhrp2 或 pfhrp3 基因时，就会失败。厄立特里亚、埃塞俄比亚和吉布提报告了广泛的删除情况，但索马里尚未提供系统数据。 2023 年 5 月至 10 月期间，我们从索马里 7 个地区的 8 个医疗机构就诊的疑似疟疾患者收集了 7148 份干血斑 (DBS) 样本。进行了现场 HRP2/泛乳酸脱氢酶 (LDH) RDT 和显微镜检查，并从 301 个 RDT 阳性和 173 个 RDT 阴性 DBS 样本中提取了 DNA。
- Keywords: deletions, somalia, pfhrp2, pfhrp3, malaria

### 6. [多组学分析揭示了虚弱、慢性疼痛和类风湿关节炎之间的双向遗传联系和趋同的炎症神经元特征](https://www.medrxiv.org/content/10.64898/2026.06.30.26356940v2)
- Original title: Multi-Omic Analyses Reveal Bidirectional Genetic Links and Convergent Inflammatory-Neuronal Signatures Between Frailty, Chronic Pain, and Rheumatoid Arthritis
- Authors: Flint, J. P., Mitchell, B. L., Heyworth, S. M., Smith, H. M., Foote, I. F. et al.
- Meta: 2026-07-21 | epidemiology | DOI: 10.64898/2026.06.30.26356940
- 中文摘要: 摘要背景：虚弱反映了生理弹性的降低和对压力源的脆弱性增加，是衰老的一个关键生物学标志。然而，将虚弱与慢性炎症联系起来的分子和因果机制仍不清楚。方法：我们整合孟德尔随机化（MR）、成对全基因组关联（PW-GWAS）和表观遗传蛋白预测来剖析虚弱、慢性疼痛（CP）和类风湿性关节炎（RA）之间的双向生物学途径。结果：在九个基因定义的衰弱表型中——六个特定领域因素、一个一般衰弱因子 (GF) 和两个累积指数（衰弱指数 - FI、Fried 衰弱评分 - FFS）——MR 揭示了 CP 和 RA 对衰弱的广泛因果影响。
- Abstract: Abstract Background: Frailty reflects reduced physiological resilience and increased vulnerability to stressors, functioning as a key biological marker of ageing. Yet, the molecular and causal mechanisms linking frailty to chronic inflammatory conditions remain unclear. Methods: We integrate Mendelian randomisation (MR), pairwise genome-wide association (PW-GWAS), and epigenetic-protein prediction to dissect bidirec...
- Summary (fallback): 机器翻译摘要显示：摘要背景：虚弱反映了生理弹性的降低和对压力源的脆弱性增加，是衰老的一个关键生物学标志。然而，将虚弱与慢性炎症联系起来的分子和因果机制仍不清楚。方法：我们整合孟德尔随机化（MR）、成对全基因组关联（PW-GWAS）和表观遗传蛋白预测来剖析虚弱、慢性疼痛（CP）和类风湿性关节炎（RA）之间的双向生物学途径。结果：在九个基因定义的衰弱表型中——六个特定领域因素、一个一般衰弱因子 (GF) 和两个累积指数（衰弱指数 - FI、Fried 衰弱评分 - FFS）——MR 揭示了 CP 和 RA 对衰弱的广泛因果影响。
- Keywords: frailty, chronic, pain, pathways, cumulative

### 7. [在糖尿病预防计划成果研究中实施国家阿尔茨海默病协调中心统一数据集 (v3)](https://www.medrxiv.org/content/10.64898/2026.07.17.26357765v1)
- Original title: Implementing the National Alzheimer's Coordinating Center Uniform Data Set (v3) within the Diabetes Prevention Program Outcomes Study
- Authors: Doherty, L., Dechiario, I., Sherif, H., Bowers, A., Martinez, D. et al.
- Meta: 2026-07-21 | epidemiology | DOI: 10.64898/2026.07.17.26357765
- 中文摘要: 简介：糖尿病预防计划 (DPP) 是一项随机临床试验，旨在预防患有前驱糖尿病的成人患 2 型糖尿病 (T2D)。 DPP 结果研究 (DPPOS) 是对该队列的 30 年随访，重点关注 T2D、糖尿病前期和相关并发症。认知评估于 2009 年开始，并于 2022 年扩大范围，以检查幸存队列中的认知障碍，包括阿尔茨海默病 (AD) 和 AD 相关痴呆 (ADRD)。为了支持这些目标，国家阿尔茨海默病协调中心统一数据集版本 3 (NACC-UDSv3)（阿尔茨海默病研究中心使用的标准化框架）于 2022 年在 DPPOS 中实施，以便与 NACC 共享数据。 DPPOS 中进行的认知测试对这些表格进行了补充。
- Abstract: INTRODUCTION: The Diabetes Prevention Program (DPP) was a randomized clinical trial designed to prevent type 2 diabetes (T2D) in adults with prediabetes. The DPP Outcomes Study (DPPOS) is the 30-year follow-up of this cohort, focusing on T2D, prediabetes, and related complications. Cognitive assessments began in 2009 and expanded in 2022 to examine cognitive impairment, including Alzheimer's disease (AD) and AD rela...
- Summary (fallback): 机器翻译摘要显示：简介：糖尿病预防计划 (DPP) 是一项随机临床试验，旨在预防患有前驱糖尿病的成人患 2 型糖尿病 (T2D)。 DPP 结果研究 (DPPOS) 是对该队列的 30 年随访，重点关注 T2D、糖尿病前期和相关并发症。认知评估于 2009 年开始，并于 2022 年扩大范围，以检查幸存队列中的认知障碍，包括阿尔茨海默病 (AD) 和 AD 相关痴呆 (ADRD)。为了支持这些目标，国家阿尔茨海默病协调中心统一数据集版本 3 (NACC-UDSv3)（阿尔茨海默病研究中心使用的标准化框架）于 2022 年在 DPPOS 中实施，以便与 NACC 共享数据。 DPPOS 中进行的认知测试对这些表格进行了补充。
- Keywords: nacc-udsv3, dppos, cognitive, adrd, alzheimer

### 8. [孟德尔随机研究中暴露和结果的遗传性混杂](https://www.medrxiv.org/content/10.1101/2024.09.05.24312293v5)
- Original title: Heritable confounding of exposure and outcome in Mendelian randomization studies
- Authors: Sanderson, E., Rosoff, D., Vitt, N., Palmer, T., Tilling, K. et al.
- Meta: 2026-07-21 | epidemiology | DOI: 10.1101/2024.09.05.24312293
- 中文摘要: 孟德尔随机化 (MR) 利用遗传变异来推断暴露对结果的因果影响，假设这些变异仅通过暴露影响结果。然而，与暴露和结果的遗传混杂因素相关的遗传仪器可能违反这一假设，破坏基因-环境等效性并使 MR 效应估计产生偏差。随着全基因组关联研究中样本量的增加，效应量较小的遗传仪器被识别为与性状相关。在这里，我们使用模拟和应用示例来估计 C 反应蛋白对 2 型糖尿病的影响，以证明效应量较小的变异更容易出现遗传混杂，从而导致常见 MR 方法的因果估计存在偏差。
- Abstract: Mendelian randomization (MR) leverages genetic variants to infer causal effects of exposures on outcomes, assuming these variants influence outcomes solely through the exposure. However, genetic instruments associated with heritable confounders of the exposure and outcome can violate this assumption, undermining gene-environment equivalence and biasing MR effect estimates. With increasing sample sizes in genome-wide...
- Summary (fallback): 机器翻译摘要显示：孟德尔随机化 (MR) 利用遗传变异来推断暴露对结果的因果影响，假设这些变异仅通过暴露影响结果。然而，与暴露和结果的遗传混杂因素相关的遗传仪器可能违反这一假设，破坏基因-环境等效性并使 MR 效应估计产生偏差。随着全基因组关联研究中样本量的增加，效应量较小的遗传仪器被识别为与性状相关。在这里，我们使用模拟和应用示例来估计 C 反应蛋白对 2 型糖尿病的影响，以证明效应量较小的变异更容易出现遗传混杂，从而导致常见 MR 方法的因果估计存在偏差。
- Keywords: heritable, exposure, effect, confounding, outcome
