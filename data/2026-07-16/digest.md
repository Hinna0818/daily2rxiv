# daily2rxiv Digest - 2026-07-16

共收录 61 篇论文。

## arxiv

### 1. [利用未标记数据进行可推广的神经群体解码](https://arxiv.org/abs/2607.14086v1)
- Original title: Leveraging unlabelled data for generalizable neural population decoding
- Authors: Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo, Matthew G. Perich, Guillaume Lajoie
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 强大而准确的神经解码器是脑机接口和闭环实验等神经技术不可或缺的一部分。最近的工作表明，在尖峰级别对神经数据进行标记有助于多会话预训练并提供最先进的解码性能。然而，当前基于尖峰的模型仅限于监督学习（SL），限制了对具有配对行为标签的数据集的训练。为了解决这个限制，我们引入了 MOJO（基于 Masked autOencoder 的联合训练），这是一种尖峰标记化模型的训练框架，通过 masked 自动编码和 SL 目标联合利用自监督学习（SSL）。
- Abstract: Robust and accurate neural decoders are integral to neurotechnologies such as brain-computer interfaces and closed-loop experiments. Recent work has shown that tokenizing neural data at the spike level facilitates multi-session pretraining and delivers state-of-the-art decoding performance. However, current spike-based models are restricted to supervised learning (SL), limiting training to datasets with paired behav...
- Summary (fallback): 机器翻译摘要显示：强大而准确的神经解码器是脑机接口和闭环实验等神经技术不可或缺的一部分。最近的工作表明，在尖峰级别对神经数据进行标记有助于多会话预训练并提供最先进的解码性能。然而，当前基于尖峰的模型仅限于监督学习（SL），限制了对具有配对行为标签的数据集的训练。为了解决这个限制，我们引入了 MOJO（基于 Masked autOencoder 的联合训练），这是一种尖峰标记化模型的训练框架，通过 masked 自动编码和 SL 目标联合利用自监督学习（SSL）。
- Keywords: models, performance, training, neural, tasks

### 2. [通过最佳传输进行线性独立分量分析](https://arxiv.org/abs/2607.14081v1)
- Original title: Linear Independent Component Analysis via Optimal Transport
- Authors: Ashutosh Jha, Michel Besserve, Simon Buchholz
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 线性独立分量分析 (ICA) 从线性混合中恢复联合独立的源信号。为了实现这一目标，经典 ICA 算法尝试最大化非高斯性（通过负熵来衡量），而负熵与信息论的独立性相关。由于精确的负熵优化很棘手，因此它们依赖于代理对比函数，例如四阶累积量和参数对数似然。我们建议使用与标准高斯的 Wasserstein 距离 $W_2^2$ 的平方来测量非高斯性。我们证明，当投影恢复独立分量时，标准正态分布与数据线性投影之间的 Wasserstein 距离最大化。基于这一观察，我们提出了 OT-ICA 算法，该算法通过基于梯度的优化来找到该投影。
- Abstract: Linear Independent Component Analysis (ICA) recovers jointly independent source signals from their linear mixtures. To achieve this, classical ICA algorithms attempt to maximize non-Gaussianity, measured by negentropy, which is linked to independence by information theory. Because exact negentropy optimization is intractable, they rely on proxy contrast functions, such as fourth-order cumulants, and parametric log-l...
- Summary (fallback): 机器翻译摘要显示：线性独立分量分析 (ICA) 从线性混合中恢复联合独立的源信号。为了实现这一目标，经典 ICA 算法尝试最大化非高斯性（通过负熵来衡量），而负熵与信息论的独立性相关。由于精确的负熵优化很棘手，因此它们依赖于代理对比函数，例如四阶累积量和参数对数似然。我们建议使用与标准高斯的 Wasserstein 距离 $W_2^2$ 的平方来测量非高斯性。我们证明，当投影恢复独立分量时，标准正态分布与数据线性投影之间的 Wasserstein 距离最大化。基于这一观察，我们提出了 OT-ICA 算法，该算法通过基于梯度的优化来找到该投影。
- Keywords: linear, independent, component, ot-ica, analysis

### 3. [人类感知、认知和决策动态的模块化状态空间模型](https://arxiv.org/abs/2607.14078v1)
- Original title: A modular state-space model of human perception, cognition, and decision dynamics
- Authors: Sven Schoonebeek, Anahita Jamshidnejad, Carlo Cenedese
- Meta: 2026-07-15 | eess.SY
- 中文摘要: 以人为中心的自适应系统需要既可以在心理上解释又可以在数学上分析的行为模型。许多现有的预测器要么作为黑盒输入输出映射运行，要么提供对潜在内部动态的有限访问。本文通过将行为建模为感知-认知-决策管道来解决这一差距。我们提出了一种模块化状态空间模型，其中注意力选择、预测推理、认知状态演化、意图形成和行动选择由耦合的数学映射表示。该模型通过潜在的内部状态将感觉输入与可观察的行为联系起来，同时保留与神经认知机制的可解释的联系。
- Abstract: Human-centered adaptive systems require behavioral models that are both psychologically interpretable and mathematically analyzable. Many existing predictors either operate as black-box input-output mappings or provide limited access to latent internal dynamics. This paper addresses this gap by modeling behavior as a perception-cognition-decision pipeline. We propose a modular state-space model in which attentional...
- Summary (fallback): 机器翻译摘要显示：以人为中心的自适应系统需要既可以在心理上解释又可以在数学上分析的行为模型。许多现有的预测器要么作为黑盒输入输出映射运行，要么提供对潜在内部动态的有限访问。本文通过将行为建模为感知-认知-决策管道来解决这一差距。我们提出了一种模块化状态空间模型，其中注意力选择、预测推理、认知状态演化、意图形成和行动选择由耦合的数学映射表示。该模型通过潜在的内部状态将感觉输入与可观察的行为联系起来，同时保留与神经认知机制的可解释的联系。
- Keywords: model, dynamics, interpretable, modular, state-space

### 4. [MetaPerch：从生物声学基础模型的元数据中学习](https://arxiv.org/abs/2607.14072v1)
- Original title: MetaPerch: Learning from metadata for bioacoustics foundation models
- Authors: Mustafa Chasmai, Vincent Dumoulin, Jenny Hamer
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 生物声学基础模型依赖于 Xeno-Canto 等大型公民科学平台来获取地理和生态多样性数据。最近的工作表明，在对这种大规模数据进行训练时，仅监督就可以产生 SotA 物种检测模型 - 然而，在这些社区驱动的数据中心内记录可用的元数据的形式仍然存在未利用的潜力。在这项工作中，我们探索使用元数据（例如位置和时间）作为辅助监督信号，使模型能够在其学习表示中利用物种元数据相关性。
- Abstract: Bioacoustic foundation models rely on large-scale citizen science platforms like Xeno-Canto for geographically and ecologically diverse data. Recent work has shown that supervision alone can produce SotA species detection models when trained on this large-scale data -- however, there remains unutilized potential in the form of recording metadata readily available within these community-driven data hubs. In this work...
- Summary (fallback): 机器翻译摘要显示：生物声学基础模型依赖于 Xeno-Canto 等大型公民科学平台来获取地理和生态多样性数据。最近的工作表明，在对这种大规模数据进行训练时，仅监督就可以产生 SotA 物种检测模型 - 然而，在这些社区驱动的数据中心内记录可用的元数据的形式仍然存在未利用的潜力。在这项工作中，我们探索使用元数据（例如位置和时间）作为辅助监督信号，使模型能够在其学习表示中利用物种元数据相关性。
- Keywords: metadata, foundation, models, species, metaperch

### 5. [使用 Evo 2 探针筛选宏基因组数据中的生物安全特征](https://arxiv.org/abs/2607.14070v1)
- Original title: Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes
- Authors: Jeremy Guntoro, Alexander Dack, Dylan Danno, Michaela Jančovičová, Križan Jurinović et al.
- Meta: 2026-07-15 | q-bio.GN
- 中文摘要: Evo 2 等基因组基础模型可以学习丰富的序列表示，但它们对于生物安全筛选的价值在很大程度上尚未被开发。我们询问通过在冻结的 Evo 2 第 26 层激活上训练最小线性和注意力探针，在这些表示中可以线性访问多少生物安全相关信号，而无需微调底层模型。在保留的宏基因组测试集中，探针以很强的辨别力检测抗菌素耐药性 (AMR)：线性探针的区域级 ROC-AUC 为 0.888（平均池），而单头注意力探针则升至 0.977。这些探针解析了更细粒度的 AMR 药物类别子类别，并将它们与不相关的功能基因分开，提供了额外的证据，证明所获悉的信号不能仅由通用功能基因状态来解释。
- Abstract: Genomic foundation models such as Evo 2 learn rich sequence representations, but their value for biosecurity screening is largely unexplored. We ask how much biosecurity-relevant signal is linearly accessible in these representations by training minimal linear and attention probes on frozen Evo 2 layer-26 activations, without fine-tuning the underlying model. Across held-out metagenomic test sets, the probes detect...
- Summary (fallback): 机器翻译摘要显示：Evo 2 等基因组基础模型可以学习丰富的序列表示，但它们对于生物安全筛选的价值在很大程度上尚未被开发。我们询问通过在冻结的 Evo 2 第 26 层激活上训练最小线性和注意力探针，在这些表示中可以线性访问多少生物安全相关信号，而无需微调底层模型。在保留的宏基因组测试集中，探针以很强的辨别力检测抗菌素耐药性 (AMR)：线性探针的区域级 ROC-AUC 为 0.888（平均池），而单头注意力探针则升至 0.977。这些探针解析了更细粒度的 AMR 药物类别子类别，并将它们与不相关的功能基因分开，提供了额外的证据，证明所获悉的信号不能仅由通用功能基因状态来解释。
- Keywords: probes, biosecurity, metagenomic, probe, roc-auc

### 6. [基于似然深度学习的散斑回归的极小极大理论](https://arxiv.org/abs/2607.14064v1)
- Original title: Minimax Theory of Likelihood-Based Deep Learning for Speckle Regression
- Authors: Soham Jana
- Meta: 2026-07-15 | math.ST
- 中文摘要: 散斑噪声是合成孔径雷达、光学相干断层扫描和数字全息术等相干成像模式中常见的倍性噪声。尽管深度学习方法在实践中已经在散斑去噪方面取得了最先进的性能，但其基本的统计限制在很大程度上仍未被探索。与加性噪声模型不同，乘性散斑噪声使得回归函数无法从条件均值中识别出来，从而使得传统的基于最小二乘的深度学习方法不适用。我们在具有乘性散斑噪声和加性高斯噪声的模型下使用基于似然的深度神经网络（DNN）估计器研究平滑非参数回归函数的极小极大估计。我们的框架同时适应低维和稀疏高维特征。
- Abstract: Speckle noise is a multiplicative noise commonly encountered in coherent imaging modalities such as synthetic aperture radar, optical coherence tomography, and digital holography. Although deep learning methods, in practice, have achieved state-of-the-art performance for speckle denoising, their fundamental statistical limits remain largely unexplored. Unlike additive noise models, multiplicative speckle noise makes...
- Summary (fallback): 机器翻译摘要显示：散斑噪声是合成孔径雷达、光学相干断层扫描和数字全息术等相干成像模式中常见的倍性噪声。尽管深度学习方法在实践中已经在散斑去噪方面取得了最先进的性能，但其基本的统计限制在很大程度上仍未被探索。与加性噪声模型不同，乘性散斑噪声使得回归函数无法从条件均值中识别出来，从而使得传统的基于最小二乘的深度学习方法不适用。我们在具有乘性散斑噪声和加性高斯噪声的模型下使用基于似然的深度神经网络（DNN）估计器研究平滑非参数回归函数的极小极大估计。我们的框架同时适应低维和稀疏高维特征。
- Keywords: noise, speckle, minimax, deep, regression

### 7. [三价阳离子在空气-水界面上凝胶化功能性肽](https://arxiv.org/abs/2607.14061v1)
- Original title: Gelation of functional peptides by trivalent cations at the air-water interface
- Authors: Stephen A. Crane, Felipe Jimenez Angeles, Monica Olvera de la Cruz, Ivan J. Dmochowski, Kathleen J. Stebe
- Meta: 2026-07-15 | cond-mat.soft
- 中文摘要: 我们报告了一种由多价阳离子介导的桥接驱动的流体界面凝胶化机制。在空气-水界面，结合有镧系元素阳离子的肽经历配位几何转变，将金属从单肽结合态转化为多肽桥接态，驱动电荷反转和凝胶形成。这一转变涉及表面吸附和非理想界面静电。该凝胶通过可逆的金属-配体配位键来稳定，该配位键可以抵抗大量盐的筛选，这与蛋白质中的静电荷反转凝胶有根本的区别。这揭示了肽协调球的分解作为界面凝胶化的独特途径，独立于控制大量蛋白质聚集的扩散静电机制。
- Abstract: We report a mechanism for gelation at fluid interfaces driven by multivalent-cation-mediated bridging. At the air-water interface, peptides with bound lanthanide cations undergo a coordination-geometry transition that converts the metal from a single-peptide bound state to a multi-peptide bridging state, driving charge inversion and gel formation. Surface adsorption and non-ideal interfacial electrostatics are impli...
- Summary (fallback): 机器翻译摘要显示：我们报告了一种由多价阳离子介导的桥接驱动的流体界面凝胶化机制。在空气-水界面，结合有镧系元素阳离子的肽经历配位几何转变，将金属从单肽结合态转化为多肽桥接态，驱动电荷反转和凝胶形成。这一转变涉及表面吸附和非理想界面静电。该凝胶通过可逆的金属-配体配位键来稳定，该配位键可以抵抗大量盐的筛选，这与蛋白质中的静电荷反转凝胶有根本的区别。这揭示了肽协调球的分解作为界面凝胶化的独特途径，独立于控制大量蛋白质聚集的扩散静电机制。
- Keywords: gelation, peptides, cations, air-water, interface

### 8. [多域低资源 OCR 的多专家路由：满文案例研究](https://arxiv.org/abs/2607.14041v1)
- Original title: Multi-Expert Routing for Multi-Domain Low-Resource OCR: A Manchu Case Study
- Authors: Zhan Chen, Jiqiao Ma, Chih-wen Kuo
- Meta: 2026-07-15 | cs.CV
- 中文摘要: 历史满文 OCR 必须适应各种视觉上不同的书写风格，包括楷书、行书和宫殿纪念馆中使用的半草书，尽管标记数据有限。我们研究了一个多专家系统，该系统作为领域专家重用迭代微调过程中的检查点，并使用轻量级页面级图像分类器按视觉风格分派页面。当检查点池缺乏合适的专家时，我们会为该领域培训一名额外的专家。在三个冻结测试集上，路由系统以两位小数精度匹配每种风格的选定专家：楷书的 CER 为 0.30%，纪念章的 CER 为 1.57%，行书的 CER 为 4.83%。该路由器实现了 99.3% 的页面级域准确度，并以相同的精度与域标签预言机进行匹配。
- Abstract: Historical Manchu OCR must accommodate various visually distinct writing styles, including regular script, running script, and the semi-cursive chancery hand used in palace memorials, despite limited labeled data. We study a multi-expert system that reuses checkpoints from an iterative fine-tuning process as domain specialists and uses a lightweight page-level image classifier to dispatch pages by visual style. When...
- Summary (fallback): 机器翻译摘要显示：历史满文 OCR 必须适应各种视觉上不同的书写风格，包括楷书、行书和宫殿纪念馆中使用的半草书，尽管标记数据有限。我们研究了一个多专家系统，该系统作为领域专家重用迭代微调过程中的检查点，并使用轻量级页面级图像分类器按视觉风格分派页面。当检查点池缺乏合适的专家时，我们会为该领域培训一名额外的专家。在三个冻结测试集上，路由系统以两位小数精度匹配每种风格的选定专家：楷书的 CER 为 0.30%，纪念章的 CER 为 1.57%，行书的 CER 为 4.83%。该路由器实现了 99.3% 的页面级域准确度，并以相同的精度与域标签预言机进行匹配。
- Keywords: domain, script, percent, multi-expert, manchu

### 9. [GitHub 项目早期采用代理编码工具](https://arxiv.org/abs/2607.14037v1)
- Original title: Early Adoption of Agentic Coding Tools by GitHub Projects
- Authors: Maliha Noushin Raida, Daqing Hou
- Meta: 2026-07-15 | cs.SE
- 中文摘要: 代理编码工具越来越能够生成并向软件项目提交拉取请求 (PR)，从而在软件开发中引入新形式的人机协作。虽然之前的研究已经检验了代理生成的贡献的 PR 级别结果，但对于如何在项目级别采用和管理代理编码工具却知之甚少。在本文中，我们分析了来自 2,361 个流行 GitHub 存储库的 25,264 个代理 PR，以调查 (1) 代理编码工具的采用情况，(2) 项目级代理 PR 生产力，以及 (3) 人工代理协作模式。我们的结果表明，中位数存储库在三个月内仅生成一到两个代理 PR，这表明密集采用仍然集中在一小部分项目中。
- Abstract: Agentic coding tools are increasingly capable of generating and submitting pull requests (PRs) to software projects, introducing new forms of human-agent collaboration in software development. While prior studies have examined PR-level outcomes of agent-generated contributions, less is known about how agentic coding tools are adopted and managed at the project level. In this paper, we analyze 25,264 agentic PRs from...
- Summary (fallback): 机器翻译摘要显示：代理编码工具越来越能够生成并向软件项目提交拉取请求 (PR)，从而在软件开发中引入新形式的人机协作。虽然之前的研究已经检验了代理生成的贡献的 PR 级别结果，但对于如何在项目级别采用和管理代理编码工具却知之甚少。在本文中，我们分析了来自 2,361 个流行 GitHub 存储库的 25,264 个代理 PR，以调查 (1) 代理编码工具的采用情况，(2) 项目级代理 PR 生产力，以及 (3) 人工代理协作模式。我们的结果表明，中位数存储库在三个月内仅生成一到两个代理 PR，这表明密集采用仍然集中在一小部分项目中。
- Keywords: agentic, projects, adoption, coding, tools

### 10. [规格：特定进化电路合成](https://arxiv.org/abs/2607.14027v1)
- Original title: SPECS: Speciated Evolutionary Circuit Synthesis
- Authors: Yağız Gençer, Stefan Uhlich, Andrea Bonetti, Arun Venkitaraman, Chia-Yu Hsieh et al.
- Meta: 2026-07-15 | cs.NE
- 中文摘要: 我们提出了 SPECS，一种用于自动模拟电路合成的遗传算法，具有联合拓扑和尺寸优化。 SPECS 的灵感来自增强拓扑的 NeuroEvolution (NEAT)，这是一种最初开发用于合成神经网络的进化算法。通过重新制定基因组表示并使遗传算子适应模拟电路领域，我们成功地将 NEAT 的核心原理转移到模拟电路综合中。电路特定的布线约束被纳入其中，以确保在整个进化过程中有效且具有物理意义的设计，并且物种形成用于在保持种群多样性的同时保留创新。我们在一组由平方、立方、平方根和立方根函数组成的计算电路综合任务上评估所提出的方法。
- Abstract: We propose SPECS, a genetic algorithm for automated analog circuit synthesis with joint topology and sizing optimization. SPECS is inspired by NeuroEvolution of Augmenting Topologies (NEAT), an evolutionary algorithm originally developed to synthesize neural networks. By reformulating the genome representation and adapting the genetic operators to the analog circuit domain, we successfully transfer the core principl...
- Summary (fallback): 机器翻译摘要显示：我们提出了 SPECS，一种用于自动模拟电路合成的遗传算法，具有联合拓扑和尺寸优化。 SPECS 的灵感来自增强拓扑的 NeuroEvolution (NEAT)，这是一种最初开发用于合成神经网络的进化算法。通过重新制定基因组表示并使遗传算子适应模拟电路领域，我们成功地将 NEAT 的核心原理转移到模拟电路综合中。电路特定的布线约束被纳入其中，以确保在整个进化过程中有效且具有物理意义的设计，并且物种形成用于在保持种群多样性的同时保留创新。我们在一组由平方、立方、平方根和立方根函数组成的计算电路综合任务上评估所提出的方法。
- Keywords: circuit, specs, synthesis, evolutionary, analog

### 11. [通过基于包装的高效特征选择改进风能和太阳能预测：实证研究](https://arxiv.org/abs/2607.14024v1)
- Original title: Improving Wind and Solar Power Prediction with Efficient Wrapper-based Feature Selection: An Empirical Study
- Authors: Daniel Grillmeyer, Marius Hadry, Michael Stenger, Vanessa Borst, Veronika Lesch et al.
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 随着全球能源需求的不断增长以及人们对气候变化及其影响的认识不断增强，可再生能源在全球能源结构中的份额持续增长。与传统发电不同，可再生能源的输出由于其对环境条件的依赖而无法得到一致的控制。因此，对当前和未来能源生产的可靠预测至关重要。在本文中，我们报告了关于现实世界可再生能源预测任务的两篇结构化文献综述的结果：风力涡轮机功率曲线建模和光伏功率预测。对于前者，我们自己进行了全面的文献综述，而对于后者，我们根据现有调查综合了有关频繁选择的输入特征的关键发现。
- Abstract: With rising global energy demand and growing awareness of climate change and its impacts, the share of renewable energies in the global energy mix continues to grow. Unlike conventional power generation, the output of renewable energy sources cannot be controlled as consistently due to their dependence on environmental conditions. Therefore, reliable prediction of current and future energy production is essential. I...
- Summary (fallback): 机器翻译摘要显示：随着全球能源需求的不断增长以及人们对气候变化及其影响的认识不断增强，可再生能源在全球能源结构中的份额持续增长。与传统发电不同，可再生能源的输出由于其对环境条件的依赖而无法得到一致的控制。因此，对当前和未来能源生产的可靠预测至关重要。在本文中，我们报告了关于现实世界可再生能源预测任务的两篇结构化文献综述的结果：风力涡轮机功率曲线建模和光伏功率预测。对于前者，我们自己进行了全面的文献综述，而对于后者，我们根据现有调查综合了有关频繁选择的输入特征的关键发现。
- Keywords: feature, selection, energy, prediction, power

### 12. [对抗性双目标价值函数的精确分解及其在最佳药物剂量中的应用](https://arxiv.org/abs/2607.14023v1)
- Original title: Exact Decomposition of Adversarial Dual-Objective Value Functions, with Applications to Optimal Drug Dosing
- Authors: Dylan Hirsch, William Sharpless, Sylvia Herbert
- Meta: 2026-07-15 | eess.SY
- 中文摘要: 汉密尔顿-雅可比可达性 (HJR) 是安全控制理论的核心框架。虽然 HJR 传统上专注于一些基本任务，但人们越来越有兴趣扩展到更复杂的目标。最近的工作研究了无对手环境中两个基本双目标任务的价值函数的精确分解。然而，并非 HJR 中的所有价值函数分解对于对手都有效。在这项工作中，我们开发了理论方法来证明对于这两个复合价值函数，所提出的分解仍然适用于对手。最后，我们展示了这些结果如何解决将 HJR 应用于最佳药物治疗方案设计时出现的问题。
- Abstract: Hamilton-Jacobi Reachability (HJR) is a central framework in safe control theory. While HJR has traditionally focused on a few fundamental tasks, there is increasing interest in scaling to more complex objectives. Recent works have studied the exact decomposition of the value functions for two fundamental dual-objective tasks in the adversary-free setting. However, not all value function decompositions in HJR remain...
- Summary (fallback): 机器翻译摘要显示：汉密尔顿-雅可比可达性 (HJR) 是安全控制理论的核心框架。虽然 HJR 传统上专注于一些基本任务，但人们越来越有兴趣扩展到更复杂的目标。最近的工作研究了无对手环境中两个基本双目标任务的价值函数的精确分解。然而，并非 HJR 中的所有价值函数分解对于对手都有效。在这项工作中，我们开发了理论方法来证明对于这两个复合价值函数，所提出的分解仍然适用于对手。最后，我们展示了这些结果如何解决将 HJR 应用于最佳药物治疗方案设计时出现的问题。
- Keywords: value, functions, exact, decomposition, dual-objective

### 13. [转变等级：建筑如何驾驭深度的光谱病理学](https://arxiv.org/abs/2607.14018v1)
- Original title: Transforming Rank: How Architecture Navigates the Spectral Pathologies of Depth
- Authors: Katie Everett
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 我们研究了 Transformer 前馈块架构设计的每个组件如何确定初始化时在深度上存活的等级。我们将长期以来被理解为控制幅度的跳跃连接和归一化重新解释为在深度上保留梯度等级的机制，因为使网络具有表达能力的矩阵乘法和非线性激活也会降低等级。我们表明，跳跃连接会权衡等级崩溃与集成行为，这由分支和跳跃的相对规模控制：跳跃连接将梯度围绕剩余分支（等级丢失）路由，而不是沿着鼓励层组合的长梯度路径。
- Abstract: We investigate how each component of the Transformer feedforward block architecture design determines how much rank survives across depth at initialization. We reinterpret skip connections and normalization, long understood as controlling magnitude, as mechanisms for preserving gradient rank across depth, since the very matrix multiplications and nonlinear activations that make the network expressive also reduce the...
- Summary (fallback): 机器翻译摘要显示：我们研究了 Transformer 前馈块架构设计的每个组件如何确定初始化时在深度上存活的等级。我们将长期以来被理解为控制幅度的跳跃连接和归一化重新解释为在深度上保留梯度等级的机制，因为使网络具有表达能力的矩阵乘法和非线性激活也会降低等级。我们表明，跳跃连接会权衡等级崩溃与集成行为，这由分支和跳跃的相对规模控制：跳跃连接将梯度围绕剩余分支（等级丢失）路由，而不是沿着鼓励层组合的长梯度路径。
- Keywords: rank, depth, architecture, across, skip

### 14. [Lighthouse RL：通过策略重置点实现采样高效的电路优化](https://arxiv.org/abs/2607.14008v1)
- Original title: Lighthouse RL: Sample-Efficient Circuit Optimization via Strategic Reset Points
- Authors: Mustafa Emre Gürsoy, Stefan Uhlich, Ryoga Matsuo, Yağız Gençer, Arun Venkitaraman et al.
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 在本文中，我们介绍了 Lighthouse RL，这是一种用于模拟电路尺寸调整的样本高效强化学习 (RL) 方法。传统方法缺乏对不同性能目标的泛化，而标准强化学习方法则浪费资源探索无前途的区域。我们的方法通过战略重置策略来解决这些低效率问题，该策略从训练期间发现的高性能配置（称为“灯塔”）初始化事件。这些状态更接近目标，引导勘探走向有希望的地区。与文献中的 RL 和贝叶斯优化方法相比，我们证明了我们的方法在 2D 基准问题和两个模拟电路上的有效性，显示了样本效率（快达 1.72 倍）、优化性能（100% 与 0-87% 成功率）、泛化（75%...
- Abstract: In this paper, we introduce Lighthouse RL, a sample-efficient reinforcement learning (RL) approach for analog circuit sizing. Traditional methods lack generalization across different performance targets, while standard RL approaches waste resources exploring unpromising regions. Our method addresses these inefficiencies through a strategic reset strategy that initializes episodes from high-performing configurations...
- Summary (fallback): 机器翻译摘要显示：在本文中，我们介绍了 Lighthouse RL，这是一种用于模拟电路尺寸调整的样本高效强化学习 (RL) 方法。传统方法缺乏对不同性能目标的泛化，而标准强化学习方法则浪费资源探索无前途的区域。我们的方法通过战略重置策略来解决这些低效率问题，该策略从训练期间发现的高性能配置（称为“灯塔”）初始化事件。这些状态更接近目标，引导勘探走向有希望的地区。与文献中的 RL 和贝叶斯优化方法相比，我们证明了我们的方法在 2D 基准问题和两个模拟电路上的有效性，显示了样本效率（快达 1.72 倍）、优化性能（100% 与 0-87% 成功率）、泛化（75%...
- Keywords: optimization, reset, approach, lighthouse, sample-efficient

### 15. [代理优化器是否复合？ Terminal-Bench 2.0 的持续学习评估](https://arxiv.org/abs/2607.14004v1)
- Original title: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0
- Authors: Wenxiao Wang, Priyatham Kattakinda, Soheil Feizi
- Meta: 2026-07-15 | cs.AI
- 中文摘要: 大多数报告的智能体优化方法的收益都是一次性的：智能体根据固定基准进行优化，并报告所得的改进，就好像它是该方法的稳定属性一样。这不会测试对已部署的代理而言重要的设置，其中随着时间的推移出现新的故障和新任务，递归地应用优化。这就提出的核心问题是优化器驱动的收益是否会复合：在代理优化一次之后，是否可以在新到达的任务上再次优化而不侵蚀第一轮产生的收益？我们通过基于 Terminal-Bench 2.0 中的硬任务构建的两阶段持续学习评估来研究这个问题，比较了相同优化预算下的三种代理线束优化方法（GEPA、Meta Harness 和 RELAI 的可验证持续学习，RELAI-VCL）。
- Abstract: Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the method. This does not test the setting that matters for deployed agents, where optimization is applied recursively as new failures and new tasks appear over time. The central question this raises is whether optimizer-driven...
- Summary (fallback): 机器翻译摘要显示：大多数报告的智能体优化方法的收益都是一次性的：智能体根据固定基准进行优化，并报告所得的改进，就好像它是该方法的稳定属性一样。这不会测试对已部署的代理而言重要的设置，其中随着时间的推移出现新的故障和新任务，递归地应用优化。这就提出的核心问题是优化器驱动的收益是否会复合：在代理优化一次之后，是否可以在新到达的任务上再次优化而不侵蚀第一轮产生的收益？我们通过基于 Terminal-Bench 2.0 中的硬任务构建的两阶段持续学习评估来研究这个问题，比较了相同优化预算下的三种代理线束优化方法（GEPA、Meta Harness 和 RELAI 的可验证持续学习，RELAI-VCL）。
- Keywords: optimization, tasks, agent, gains, optimized

### 16. [Lyapunov 指数作为物理信息密集奖励：RL 发现卡皮查摆之外的稳定性](https://arxiv.org/abs/2607.14001v1)
- Original title: Lyapunov Exponent as Physics-Informed Dense Reward: RL Discovery of Stabilization Beyond the Kapitza Pendulum
- Authors: Slava Andrejev
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 我们建议使用李亚普诺夫特征指数（LCE）作为稳定垂直运动倒立摆的强化学习问题的密集奖励信号。通过 LCE，该特工不仅成功地发现了被称为卡皮查摆的振荡运动，而且还抑制了摆的旋转，使其处于严格的直立位置。
- Abstract: We suggest using the Lyapunov characteristic exponent (LCE) as a dense reward signal for the reinforcement learning problem of stabilizing the inverted pendulum with vertical motion. With LCE, the agent not only successfully found the oscillatory motion known as the Kapitza pendulum but also damped the pendulum's pivoting, leaving it in a strictly upright position.
- Summary (fallback): 机器翻译摘要显示：我们建议使用李亚普诺夫特征指数（LCE）作为稳定垂直运动倒立摆的强化学习问题的密集奖励信号。通过 LCE，该特工不仅成功地发现了被称为卡皮查摆的振荡运动，而且还抑制了摆的旋转，使其处于严格的直立位置。
- Keywords: pendulum, lyapunov, exponent, dense, reward

### 17. [具有瞬态突触记忆的神经元网络中静默状态的活动再生](https://arxiv.org/abs/2607.14000v1)
- Original title: Activity Regeneration from Silent States in Neuronal Networks with Transient Synaptic Memory
- Authors: Mozhgan Khanjanianpak, Alireza Valiadeh
- Meta: 2026-07-15 | q-bio.NC
- 中文摘要: 瞬时突触记忆已成为即使在没有持续神经元活动的情况下也能维持短期信息的潜在机制。然而，目前尚不清楚隐藏的突触状态是否包含足够的信息来预测活动停止后神经元网络的未来进化。在这里，我们引入了具有有限寿命突触的最小神经元网络模型，并研究了完全神经元沉默后自发活动再生的机制。我们表明，第一个沉默状态下的残余突触配置已经决定了网络活动是在单个激活周期后终止还是自发地再生一个额外的周期。
- Abstract: Transient synaptic memory has emerged as a potential mechanism for maintaining short-term information even in the absence of persistent neuronal activity. However, it remains unclear whether the hidden synaptic state alone contains sufficient information to predict the future evolution of neuronal networks after activity has ceased. Here, we introduce a minimal neuronal network model with finite-lifetime synapses an...
- Summary (fallback): 机器翻译摘要显示：瞬时突触记忆已成为即使在没有持续神经元活动的情况下也能维持短期信息的潜在机制。然而，目前尚不清楚隐藏的突触状态是否包含足够的信息来预测活动停止后神经元网络的未来进化。在这里，我们引入了具有有限寿命突触的最小神经元网络模型，并研究了完全神经元沉默后自发活动再生的机制。我们表明，第一个沉默状态下的残余突触配置已经决定了网络活动是在单个激活周期后终止还是自发地再生一个额外的周期。
- Keywords: neuronal, activity, synaptic, network, memory

### 18. [人体细胞辐射反应机制的因果发现](https://arxiv.org/abs/2607.13994v1)
- Original title: Causal Discovery of Radiation Response Mechanisms in Human Cells
- Authors: Ashka Shah, Rick Stevens
- Meta: 2026-07-15 | q-bio.GN
- 中文摘要: 包括 RNA 测序在内的下一代测序技术可提供基因表达的全基因组测量，并能够广泛探索疾病和治疗反应背后的生物标志物和机制。用于处理这些数据的生物信息学工具（例如差异表达分析）很大程度上是单变量、线性的，并且依赖于预定义的通路知识注释，这限制了它们捕获非线性和多变量基因相互作用的能力。本文探讨了因果发现的应用，以表征人类细胞中辐射转录反应与剂量率的函数关系。
- Abstract: Next-generation sequencing technologies, including RNA-sequencing, provide genome-wide measurements of gene expression and enable broad explorations of biomarkers and mechanisms underlying disease and treatment response. Bioinformatics tools for processing this data, such as differential expression analysis, are largely univariate, linear, and rely on predefined pathway knowledge annotations, which limits their abil...
- Summary (fallback): 机器翻译摘要显示：包括 RNA 测序在内的下一代测序技术可提供基因表达的全基因组测量，并能够广泛探索疾病和治疗反应背后的生物标志物和机制。用于处理这些数据的生物信息学工具（例如差异表达分析）很大程度上是单变量、线性的，并且依赖于预定义的通路知识注释，这限制了它们捕获非线性和多变量基因相互作用的能力。本文探讨了因果发现的应用，以表征人类细胞中辐射转录反应与剂量率的函数关系。
- Keywords: response, causal, radiation, gene, discovery

### 19. [TRACE：通过信用评估为长视野特工分配轮次奖励](https://arxiv.org/abs/2607.13988v1)
- Original title: TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents
- Authors: Leitian Tao, Baolin Peng, Wenlin Yao, Tao Ge, Hao Cheng et al.
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 多轮代理在产生最终答案之前通过扩展的工具交互序列来解决复杂的任务，这使得信用分配成为训练后的基本挑战。结果奖励为短期推理提供了可靠的监督，但随着轨迹增长到数十或数百个工具调用，结果奖励变得稀疏且高方差。它们也可能具有误导性：失败的部署可能包含许多有用的操作，使代理更接近目标，但只注重结果的训练却给他们带来了与最终错误相同的负面优势。我们提出了 TRACE（通过信用估计进行轮级奖励分配），这是一种用于代理强化学习的密集信用分配方法。
- Abstract: Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training. Outcome rewards provide reliable supervision for short-horizon reasoning, but become sparse and high-variance as trajectories grow to tens or hundreds of tool calls. They can also be misleading: a failed rollout may contain many...
- Summary (fallback): 机器翻译摘要显示：多轮代理在产生最终答案之前通过扩展的工具交互序列来解决复杂的任务，这使得信用分配成为训练后的基本挑战。结果奖励为短期推理提供了可靠的监督，但随着轨迹增长到数十或数百个工具调用，结果奖励变得稀疏且高方差。它们也可能具有误导性：失败的部署可能包含许多有用的操作，使代理更接近目标，但只注重结果的训练却给他们带来了与最终错误相同的负面优势。我们提出了 TRACE（通过信用估计进行轮级奖励分配），这是一种用于代理强化学习的密集信用分配方法。
- Keywords: trace, training, assignment, credit, tool

### 20. [用于联合纵向和事件时间建模的多模态经验贝叶斯变分自动编码器](https://arxiv.org/abs/2607.13984v1)
- Original title: Multimodal Empirical Bayes Variational Autoencoders for Joint Longitudinal and Time-to-Event Modeling
- Authors: Anders Sjöberg, Nils Olsson, Marcus Baaz, Mats Jirstrand
- Meta: 2026-07-15 | stat.ML
- 中文摘要: 纵向肿瘤测量、脱落信息和遗传协变量提供了有关治疗反应的补充信息，但将这些数据源整合到单一群体建模框架中仍然具有挑战性。我们将经验贝叶斯变分自动编码器（EB-VAE）框架扩展到联合纵向和事件时间建模，并根据肿瘤生长数据对其进行评估。该框架使用由协变量条件经验贝叶斯先验规范化的潜在个体效应来表示个体间的变异性，而解码器将这些潜在效应映射到肿瘤体积轨迹。为了解释信息丢失，解码器增加了危险模型，产生肿瘤生长和丢失时间的联合预测。
- Abstract: Longitudinal tumor measurements, dropout information, and genetic covariates provide complementary information about treatment response, but integrating these data sources within a single population modeling framework remains challenging. We extend the empirical Bayes variational autoencoder (EB-VAE) framework to joint longitudinal and time-to-event modeling and evaluate it on tumor growth data. The framework repres...
- Summary (fallback): 机器翻译摘要显示：纵向肿瘤测量、脱落信息和遗传协变量提供了有关治疗反应的补充信息，但将这些数据源整合到单一群体建模框架中仍然具有挑战性。我们将经验贝叶斯变分自动编码器（EB-VAE）框架扩展到联合纵向和事件时间建模，并根据肿瘤生长数据对其进行评估。该框架使用由协变量条件经验贝叶斯先验规范化的潜在个体效应来表示个体间的变异性，而解码器将这些潜在效应映射到肿瘤体积轨迹。为了解释信息丢失，解码器增加了危险模型，产生肿瘤生长和丢失时间的联合预测。
- Keywords: decoder, joint, modeling, dropout, framework

### 21. [冷冻水环境中蛋白质稳定性的限制效应](https://arxiv.org/abs/2607.13966v1)
- Original title: Confinement effects on protein stability in a freezing water environment
- Authors: Yanis R. Espinosa, H. Ariel Alvarez, C. Manuel Carlevaro
- Meta: 2026-07-15 | physics.bio-ph
- 中文摘要: 了解蛋白质在低温下的行为仍然是生物物理学的一个核心挑战，对冷变性和冷冻保存有直接影响。虽然过冷液体状态下蛋白质的冷变性已被广泛研究，但嵌入不断生长的冰晶格中的蛋白质的行为在很大程度上仍然无法通过实验获得。在这里，我们使用分子动力学模拟来明确捕获冰 Ih 的形成，以表征酵母 frataxin (Yfh1) 在水环境结晶时的构象动力学。使用四个独立的冰种复制品和三个温度下的液-水控制，我们首先通过溶剂密度、势能和局部键序参数（W4、W6）的收敛变化来验证液-固转变。
- Abstract: Understanding how proteins behave at low temperatures remains a central challenge in biophysics, with direct implications for cold denaturation and cryopreservation. While cold denaturation of proteins in the supercooled liquid regime has been studied extensively, the behavior of a protein embedded in a growing ice lattice remains largely inaccessible to experiments. Here we use molecular dynamics simulations that e...
- Summary (fallback): 机器翻译摘要显示：了解蛋白质在低温下的行为仍然是生物物理学的一个核心挑战，对冷变性和冷冻保存有直接影响。虽然过冷液体状态下蛋白质的冷变性已被广泛研究，但嵌入不断生长的冰晶格中的蛋白质的行为在很大程度上仍然无法通过实验获得。在这里，我们使用分子动力学模拟来明确捕获冰 Ih 的形成，以表征酵母 frataxin (Yfh1) 在水环境结晶时的构象动力学。使用四个独立的冰种复制品和三个温度下的液-水控制，我们首先通过溶剂密度、势能和局部键序参数（W4、W6）的收敛变化来验证液-固转变。
- Keywords: water, protein, conformational, freezing, temperatures

### 22. [PROmop：基于 OMOP 通用数据模型的决策就绪纵向患者健康记录](https://arxiv.org/abs/2607.13947v1)
- Original title: PRomop: A Decision-Ready Longitudinal Patient Health Record on the OMOP Common Data Model
- Authors: Adam Blum, Louis Ferger-Andrews
- Meta: 2026-07-15 | cs.DB
- 中文摘要: 目标：卫生系统和生物制药在存储患者数据和对其采取行动之间面临着持续的差距。记录在各个提供者之间分散，结构化用于存储而不是决策，每个下游应用程序独立地重建患者的临床状态。我们推出了 PRomop（OMOP 上的 PatientRecord），这是一种开源纵向患者记录，旨在缩小这一差距。材料和方法：PROmop 通过肿瘤学扩展扩展了 OMOP 通用数据模型 (CDM 5.4)，并引入了 PatientRecord，这是一种扁平投影，可将每个患者的纵向病史折叠成 286 列的单个决策就绪行。临床状态（包括治疗方案、疾病状态和标准化生物标志物）在预测过程中一次导出，并具体化以供分析、临床试验匹配和护理标准评估重复使用。
- Abstract: Objective: Health systems and biopharma face a persistent gap between storing patient data and acting on it. Records are fragmented across providers, structured for storage rather than decision-making, and each downstream application independently reconstructs patient clinical state. We present PRomop (PatientRecord on OMOP), an open-source longitudinal patient record designed to close that gap. Materials and Method...
- Summary (fallback): 机器翻译摘要显示：目标：卫生系统和生物制药在存储患者数据和对其采取行动之间面临着持续的差距。记录在各个提供者之间分散，结构化用于存储而不是决策，每个下游应用程序独立地重建患者的临床状态。我们推出了 PRomop（OMOP 上的 PatientRecord），这是一种开源纵向患者记录，旨在缩小这一差距。材料和方法：PROmop 通过肿瘤学扩展扩展了 OMOP 通用数据模型 (CDM 5.4)，并引入了 PatientRecord，这是一种扁平投影，可将每个患者的纵向病史折叠成 286 列的单个决策就绪行。临床状态（包括治疗方案、疾病状态和标准化生物标志物）在预测过程中一次导出，并具体化以供分析、临床试验匹配和护理标准评估重复使用。
- Keywords: omop, promop, patient, longitudinal, clinical

### 23. [超出 Dikin 在多面体上行走的 $d^{2.5}$ 混合界限](https://arxiv.org/abs/2607.13943v1)
- Original title: Beyond the $d^{2.5}$-mixing bound for Dikin walks on polytopes
- Authors: Yunbum Kook
- Meta: 2026-07-15 | cs.DS
- 中文摘要: 受到结构化凸优化的内点方法 (IPM) 的启发，Kannan 和 Narayanan 于 2009 年引入了 Dikin walk，用于从多面体中均匀采样。与 IPM 一样，Dikin walk 是仿射不变的，其收敛性由用于定义其局部提议的障碍几何形状控制。他们证明，在 $\mathbb{R}^{d}$ 中，迪金游走与多胞形的对数障碍和 $m$ 线性不等式混合在 $md$ 迭代中。 2017 年，Chen、Dwivedi、Wainwright 和 Yu 使用路易斯权重屏障将其改进为 $d^{2.5}$，并推测正确的混合时间应该为 $d^{2}$。我们通过改进之前的 $d^{2.5}$-混合界限，在这个猜想方面取得了进展。对于多面体上的指数采样，我们证明了 Dikin 行走与缩放的 Lee-Sidford 度量在 $d^{2.25}$ 迭代中从热启动混合。
- Abstract: Inspired by interior-point methods (IPM) for structured convex optimization, Kannan and Narayanan introduced the Dikin walk for sampling uniformly from polytopes in 2009. As in IPMs, the Dikin walk is affine-invariant, and its convergence is governed by the barrier geometry used to define its local proposal. They showed that the Dikin walk with the logarithmic barrier for a polytope in $\mathbb{R}^{d}$ with $m$ line...
- Summary (fallback): 机器翻译摘要显示：受到结构化凸优化的内点方法 (IPM) 的启发，Kannan 和 Narayanan 于 2009 年引入了 Dikin walk，用于从多面体中均匀采样。与 IPM 一样，Dikin walk 是仿射不变的，其收敛性由用于定义其局部提议的障碍几何形状控制。他们证明，在 $\mathbb{R}^{d}$ 中，迪金游走与多胞形的对数障碍和 $m$ 线性不等式混合在 $md$ 迭代中。 2017 年，Chen、Dwivedi、Wainwright 和 Yu 使用路易斯权重屏障将其改进为 $d^{2.5}$，并推测正确的混合时间应该为 $d^{2}$。我们通过改进之前的 $d^{2.5}$-混合界限，在这个猜想方面取得了进展。对于多面体上的指数采样，我们证明了 Dikin 行走与缩放的 Lee-Sidford 度量...
- Keywords: dikin, walk, mixing, barrier, improved

### 24. [纵向个人健康管理的自我进化代理](https://arxiv.org/abs/2607.13940v1)
- Original title: A Self-Evolving Agent for Longitudinal Personal Health Management
- Authors: Haoran Li, Jiebi Deng, Tong Jin, Jinghong Han, Yuxin Wang et al.
- Meta: 2026-07-15 | cs.AI
- 中文摘要: 个人健康管理是在重复的遭遇中展开的，但大多数健康人工智能系统都会单独处理每个请求。我们开发了 HealthClaw，这是一种开源代理架构，可以随着人的日常生活、偏好、测量和风险的变化而更新支持。它将共享的安全规则和医学知识与包含概况事实、可重复使用的程序和情景痕迹的私人纵向记忆分开。每次发作后，归纳确定应更新配置文件、修改程序、保持发作或排除哪些内容。我们使用长达一年的综合基准和 9 个 200 例生物医学任务对 HealthClaw 进行了评估。在 900 个纵向支持调查中，答案准确性从当前查询提示的 0.2% 提高到 HealthClaw 的 45.7%，而提示侧上下文暴露比完整历史提示低 71.7%。
- Abstract: Personal health management unfolds over repeated encounters, yet most health AI systems treat each request in isolation. We developed HealthClaw, an open-source agent architecture that updates support as a person's routines, preferences, measurements and risks change. It separates shared safety rules and medical knowledge from private longitudinal memory containing profile facts, reusable procedures and episodic tra...
- Summary (fallback): 机器翻译摘要显示：个人健康管理是在重复的遭遇中展开的，但大多数健康人工智能系统都会单独处理每个请求。我们开发了 HealthClaw，这是一种开源代理架构，可以随着人的日常生活、偏好、测量和风险的变化而更新支持。它将共享的安全规则和医学知识与包含概况事实、可重复使用的程序和情景痕迹的私人纵向记忆分开。每次发作后，归纳确定应更新配置文件、修改程序、保持发作或排除哪些内容。我们使用长达一年的综合基准和 9 个 200 例生物医学任务对 HealthClaw 进行了评估。在 900 个纵向支持调查中，答案准确性从当前查询提示的 0.2% 提高到 HealthClaw 的 45.7%，而提示侧上下文暴露比完整历史提示低 71.7%。
- Keywords: healthclaw, longitudinal, health, personal, support

### 25. [一种处理多模态心脏 PET/MRI 数据的新型无监督机器学习策略](https://arxiv.org/abs/2607.13936v1)
- Original title: A novel unsupervised machine learning strategy to handle multimodal cardiac PET/MRI data
- Authors: Brunnhilde Ponsi, Thomas Carlier, Lara Marteau, Aurélien Monnet, Thomas Eugène et al.
- Meta: 2026-07-15 | cs.CV
- 中文摘要: 致心律失常性左心室心肌病是一种由于缺乏金标准而难以诊断的遗传性心肌病。同时 PET/MR 成像与多参数定量分析相结合，可以帮助识别与心肌病表型和进展相关的不同特征。这项初步研究的重点是处理 PET/MRI 数据的方法策略，包括患者间数据链接和区域分析。将两步聚类应用于 99 名基因诊断为致心律失常性左心室心肌病患者的 T1 和 T2 图、LGE 和 18F-FDG-PET 图像。每个患者的图像都经过独立的 z 评分并汇总成一个体积，该体积又聚集成超体素。通过谱聚类获得了 32 个患者间的超体素组。
- Abstract: Arrhythmogenic left ventricular cardiomyopathy is a genetic myocardial disease difficult to diagnose due to the lack of gold standard criteria. Simultaneous PET/MR imaging, combined with multiparametric quantitative analysis, could facilitate the identification of different profiles related to the phenotype and progression of cardiomyopathy. This preliminary study focuses on a methodological strategy for dealing wit...
- Summary (fallback): 机器翻译摘要显示：致心律失常性左心室心肌病是一种由于缺乏金标准而难以诊断的遗传性心肌病。同时 PET/MR 成像与多参数定量分析相结合，可以帮助识别与心肌病表型和进展相关的不同特征。这项初步研究的重点是处理 PET/MRI 数据的方法策略，包括患者间数据链接和区域分析。将两步聚类应用于 99 名基因诊断为致心律失常性左心室心肌病患者的 T1 和 T2 图、LGE 和 18F-FDG-PET 图像。每个患者的图像都经过独立的 z 评分并汇总成一个体积，该体积又聚集成超体素。通过谱聚类获得了 32 个患者间的超体素组。
- Keywords: cardiomyopathy, cardiac, arrhythmogenic, left, ventricular

### 26. [VAIOM：连续输入、离散输出仅解码器的金融序列建模](https://arxiv.org/abs/2607.13929v1)
- Original title: VAIOM: Continuous-Input, Discrete-Output Decoder-Only Financial Sequence Modeling
- Authors: Yiming Ma, Xinyu Chen
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 金融观察是连续的、异构的和有噪声的，而仅解码器的下一个令牌模型通常是围绕离散的符号输入构建的。我们引入了序数回报建模的向量输入自回归推理 (VAIOM)，这是一种仅解码器的 Transformer，用于对一小时外汇柱进行概率下一次回报建模。 VAIOM 将输入表示与输出似然分开：连续多元金融事件向量保留输入的数值结构，而下一个波动率归一化回报桶上的分类分布支持交叉熵训练和似然评估。所选的 0.9M 混合连续输入模型将连续事件特征与分类资产元数据、市场状态混合返回头、缺口、波动率机制和序数辅助目标以及全序列监督相结合。
- Abstract: Financial observations are continuous, heterogeneous, and noisy, whereas decoder-only next-token models are usually built around discrete symbolic inputs. We introduce Vector-Input Autoregressive Inference for Ordinal-Return Modeling (VAIOM), a decoder-only Transformer for probabilistic next-return modeling on one-hour foreign-exchange bars. VAIOM separates input representation from output likelihood: continuous mul...
- Summary (fallback): 机器翻译摘要显示：金融观察是连续的、异构的和有噪声的，而仅解码器的下一个令牌模型通常是围绕离散的符号输入构建的。我们引入了序数回报建模的向量输入自回归推理 (VAIOM)，这是一种仅解码器的 Transformer，用于对一小时外汇柱进行概率下一次回报建模。 VAIOM 将输入表示与输出似然分开：连续多元金融事件向量保留输入的数值结构，而下一个波动率归一化回报桶上的分类分布支持交叉熵训练和似然评估。所选的 0.9M 混合连续输入模型将连续事件特征与分类资产元数据、市场状态混合返回头、缺口、波动率机制和序数辅助目标以及全序列监督相结合。
- Keywords: continuous, input, return, likelihood, over

### 27. [对举报人合理的否认保证](https://arxiv.org/abs/2607.13928v1)
- Original title: Plausible Deniability Guarantees for Whistleblowers
- Authors: Leo Richter, Matt J. Kusner
- Meta: 2026-07-15 | cs.CR
- 中文摘要: 举报人是防止组织不当行为的关键保障，但报复的威胁却阻碍了举报。现有的举报人保护提案缺乏正式的隐私保证，并且现有的差别隐私机制并不直接针对自然威胁模型——在该模型中，被审计组织本身观察审计员选择决策并使用它们来识别报告者。我们将针对强对手威胁模型的保护正式化为审计选择记录中的每份报告 $(0, δ)$-差异隐私。在此框架内，我们证明自然方法（在选择步骤中应用随机响应）在任何情况下都不会比统一随机审计的性能超过 δ$。
- Abstract: Whistleblowers are a key safeguard against organizational wrongdoing, but the threat of retaliation deters reporting. Existing whistleblower-protection proposals lack formal privacy guarantees, and existing differential privacy mechanisms do not directly target the natural threat model -- one in which the audited organization itself observes auditor selection decisions and uses them to identify reporters. We formali...
- Summary (fallback): 机器翻译摘要显示：举报人是防止组织不当行为的关键保障，但报复的威胁却阻碍了举报。现有的举报人保护提案缺乏正式的隐私保证，并且现有的差别隐私机制并不直接针对自然威胁模型——在该模型中，被审计组织本身观察审计员选择决策并使用它们来识别报告者。我们将针对强对手威胁模型的保护正式化为审计选择记录中的每份报告 $(0, δ)$-差异隐私。在此框架内，我们证明自然方法（在选择步骤中应用随机响应）在任何情况下都不会比统一随机审计的性能超过 δ$。
- Keywords: threat, privacy, selection, per-report, audit

### 28. [生成编译：人工智能生成代码时的动态编译器反馈](https://arxiv.org/abs/2607.13921v1)
- Original title: Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code
- Authors: Niels Mündler-Sasahara, Hristo Venev, Dawn Song, Martin Vechev, Jingxuan He
- Meta: 2026-07-15 | cs.PL
- 中文摘要: Rust等具有丰富静态语义的语言为AI生成的代码提供了更有力的保证，但其严格性使得生成变得更加困难。现成的编译器可以在生成后提供有用的反馈，但不能指导中间生成步骤，例如自回归 LLM 解码期间的步骤。约束解码通过在采样期间拒绝无效标记来较早进行干预，但需要白盒模型访问和昂贵的语义约束重新实现。我们引入生成编译，这是在生成期间获取部分程序的编译器反馈的第一种方法。核心技术设备是密封器：一种轻量级的、主要是语法引导的转换，可将部分程序转换为标准编译器可以诊断的完整程序。
- Abstract: Languages with rich static semantics, such as Rust, provide stronger guarantees for AI-generated code, but their strictness makes generation more difficult. Off-the-shelf compilers can provide useful feedback post-generation, but does not guide intermediate generation steps, such as those during autoregressive LLM decoding. Constrained decoding intervenes earlier by rejecting invalid tokens during sampling, but requ...
- Summary (fallback): 机器翻译摘要显示：Rust等具有丰富静态语义的语言为AI生成的代码提供了更有力的保证，但其严格性使得生成变得更加困难。现成的编译器可以在生成后提供有用的反馈，但不能指导中间生成步骤，例如自回归 LLM 解码期间的步骤。约束解码通过在采样期间拒绝无效标记来较早进行干预，但需要白盒模型访问和昂贵的语义约束重新实现。我们引入生成编译，这是在生成期间获取部分程序的编译器反馈的第一种方法。核心技术设备是密封器：一种轻量级的、主要是语法引导的转换，可将部分程序转换为标准编译器可以诊断的完整程序。
- Keywords: generation, during, generative, compilation, feedback

### 29. [一种高效的Kullback-Leibler散度非负矩阵分解牛顿算法](https://arxiv.org/abs/2607.13919v1)
- Original title: An Efficient Newton Algorithm for Nonnegative Matrix Factorization with the Kullback-Leibler Divergence
- Authors: Damien Lesens, Jérémy E. Cohen, Bora Uçar
- Meta: 2026-07-15 | cs.LG
- 中文摘要: 非负矩阵分解（NMF）是无监督学习中的基本工具，它通过两个低秩非负因子的乘积来近似非负矩阵。当分解的数据样本遵循泊松分布时，Kullback-Leibler (KL) 散度最适合测量数据与模型的差异，计数数据集（例如术语文档矩阵或图像）就是这种情况。文献中的大多数 KL-NMF 算法都会最小化损失的可分离主数以找到下一个迭代。我们认为这种方法已经达到了其极限，并建议改用损失的二阶泰勒展开式，从而产生牛顿型方法。我们通过提出众所周知的 HALS 算法的推广来最小化这种不可分离的代理。
- Abstract: Nonnegative Matrix Factorization (NMF) is a fundamental tool in unsupervised learning, which approximates a nonnegative matrix by the product of two low-rank nonnegative factors. The Kullback-Leibler (KL) divergence is best suited to measure the data to model discrepancy when the decomposed data sample follows a Poisson distribution, which is the case for count datasets such as term-document matrices or images. Most...
- Summary (fallback): 机器翻译摘要显示：非负矩阵分解（NMF）是无监督学习中的基本工具，它通过两个低秩非负因子的乘积来近似非负矩阵。当分解的数据样本遵循泊松分布时，Kullback-Leibler (KL) 散度最适合测量数据与模型的差异，计数数据集（例如术语文档矩阵或图像）就是这种情况。文献中的大多数 KL-NMF 算法都会最小化损失的可分离主数以找到下一个迭代。我们认为这种方法已经达到了其极限，并建议改用损失的二阶泰勒展开式，从而产生牛顿型方法。我们通过提出众所周知的 HALS 算法的推广来最小化这种不可分离的代理。
- Keywords: nonnegative, which, algorithm, matrix, efficient

### 30. [LLM 框架中的部分相关验证器级联：凹对数赔率、多项式可靠性和盲点上限](https://arxiv.org/abs/2607.13918v1)
- Original title: Partially Correlated Verifier Cascades in LLM Harnesses: Concave Log-Odds, Polynomial Reliability, and Blind-Spot Ceilings
- Authors: Jiangang Han
- Meta: 2026-07-15 | math.ST
- 中文摘要: 串行验证门是 LLM 工具中的核心可靠性原语：仅当 $k$ 验证程序调用全部接受时才返回候选答案。在条件独立门下，最近的赔率定律 (arXiv:2606.15712) 显示后验对数赔率以 $k$ 为单位线性增长，因此失败呈指数衰减，并指出“部分相关验证者级联的紧密理论仍然开放”。本注释给出了此类理论的最低限度。将生成器自身错误的每个实例错误接受率建模为潜在变量 $α\sim G$ (de Finetti)，确切的级联后验为 $\ell_k = \ell_0 - \ln m_k$，其中 $m_k$ 是 $G$ 的第 $k$ 时刻。
- Abstract: Serial verification gates are a core reliability primitive in LLM harnesses: a candidate answer is returned only if $k$ verifier calls all accept it. Under conditionally independent gates, the recent Odds Law (arXiv:2606.15712) shows that posterior log-odds grow linearly in $k$, so failure decays exponentially, and states that "a tight theory of partially correlated verifier cascades remains open." This note gives a...
- Summary (fallback): 机器翻译摘要显示：串行验证门是 LLM 工具中的核心可靠性原语：仅当 $k$ 验证程序调用全部接受时才返回候选答案。在条件独立门下，最近的赔率定律 (arXiv:2606.15712) 显示后验对数赔率以 $k$ 为单位线性增长，因此失败呈指数衰减，并指出“部分相关验证者级联的紧密理论仍然开放”。本注释给出了此类理论的最低限度。将生成器自身错误的每个实例错误接受率建模为潜在变量 $α\sim G$ (de Finetti)，确切的级联后验为 $\ell_k = \ell_0 - \ln m_k$，其中 $m_k$ 是 $G$ 的第 $k$ 时刻。
- Keywords: gates, reliability, correlated, verifier, failure

## biorxiv

### 1. [WAC 损失改变了秀丽隐杆线虫与食物相关的行为和生理稳态以及阶段相关的胆碱能失调](https://www.biorxiv.org/content/10.64898/2026.04.17.719318v2)
- Original title: WAC loss alters food-associated behavior and physiological homeostasis with stage-associated cholinergic dysregulation in Caenorhabditis elegans
- Authors: Kim, D.-W., Boonpraman, N., Kuhn, N. C., Sammi, S. R.
- Meta: 2026-07-16 | neuroscience | DOI: 10.64898/2026.04.17.719318
- 中文摘要: WAC是一种参与转录控制的染色质相关调节蛋白，在人类遗传学研究中已被确定为自闭症相关基因。然而，它在调节行为和突触过程中的功能作用仍不完全清楚。使用秀丽隐杆线虫，我们研究了 wac 缺乏对食物相关社会行为、生长相关表型和胆碱能通路功能的影响。缺乏wac的线虫表现出食物离开行为显着减少，支持对食物相关环境线索的行为反应受损，而聚集行为没有显着改变。 PHX2587 wac 缺失突变蠕虫还表现出体长缩短、咽部泵送减少和寿命缩短，表明更广泛的生长和生理损伤。
- Abstract: WAC is a chromatin-associated regulatory protein involved in transcriptional control and has been identified as an autism-associated gene in human genetic studies. However, its functional role in regulating behavior and synaptic processes remains incompletely understood. Using Caenorhabditis elegans, we investigated the consequences of wac deficiency on food-associated social behavior, growth-associated phenotypes,...
- Summary (fallback): 机器翻译摘要显示：WAC是一种参与转录控制的染色质相关调节蛋白，在人类遗传学研究中已被确定为自闭症相关基因。然而，它在调节行为和突触过程中的功能作用仍不完全清楚。使用秀丽隐杆线虫，我们研究了 wac 缺乏对食物相关社会行为、生长相关表型和胆碱能通路功能的影响。缺乏wac的线虫表现出食物离开行为显着减少，支持对食物相关环境线索的行为反应受损，而聚集行为没有显着改变。 PHX2587 wac 缺失突变蠕虫还表现出体长缩短、咽部泵送减少和寿命缩短，表明更广泛的生长和生理损伤。
- Keywords: behavior, cholinergic, worms, food-associated, physiological

### 2. [p70S6 激酶对 AP2 μ2 亚基的磷酸化促进网格蛋白介导的内吞作用。](https://www.biorxiv.org/content/10.1101/2025.02.13.638021v3)
- Original title: Phosphorylation of the AP2 μ2 subunit by p70S6 kinase facilitates clathrin-mediated endocytosis.
- Authors: Tempes, A., Brzozowska, A., Wegierski, T., Fasemire, A., Olek, K. et al.
- Meta: 2026-07-16 | cell biology | DOI: 10.1101/2025.02.13.638021
- 中文摘要: 网格蛋白介导的内吞作用 (CME) 通过网格蛋白包被的质膜内陷将细胞表面受体内化。网格蛋白和内吞货物都被接头蛋白复合物 AP2 招募到这些位点。 AP2 在封闭的细胞质构象和开放的膜结合状态之间循环，有效的 CME 需要这两种构象及其动态相互转换。调节这些构象变化的机制，包括 AP2 的翻译后修饰，仍不完全清楚。在这里，我们报告 p70S6 激酶磷酸化 AP2 的 2 亚基，并且丝氨酸 45 (S45) 的磷酸化取决于 p70S6K 活性。 S45-2 磷酸化的丧失会导致典型 CME 货物（例如转铁蛋白和 PDGF 受体）的内化减少。
- Abstract: Clathrin-mediated endocytosis (CME) internalizes cell-surface receptors via clathrin-coated invaginations of the plasma membrane. Both clathrin and endocytic cargo are recruited to the these sites by the adaptor protein complex AP2. AP2 cycles between a closed cytoplasmic conformation and an open membrane-bound state, and efficient CME requires both conformations and their dynamic interconversion. The mechanisms reg...
- Summary (fallback): 机器翻译摘要显示：网格蛋白介导的内吞作用 (CME) 通过网格蛋白包被的质膜内陷将细胞表面受体内化。网格蛋白和内吞货物都被接头蛋白复合物 AP2 招募到这些位点。 AP2 在封闭的细胞质构象和开放的膜结合状态之间循环，有效的 CME 需要这两种构象及其动态相互转换。调节这些构象变化的机制，包括 AP2 的翻译后修饰，仍不完全清楚。在这里，我们报告 p70S6 激酶磷酸化 AP2 的 2 亚基，并且丝氨酸 45 (S45) 的磷酸化取决于 p70S6K 活性。 S45-2 磷酸化的丧失会导致典型 CME 货物（例如转铁蛋白和 PDGF 受体）的内化减少。
- Keywords: phosphorylation, s45-2, subunit, p70s6, kinase

### 3. [JanusX：一个集成的高性能平台，用于可扩展的全基因组关联研究和基因组选择](https://www.biorxiv.org/content/10.64898/2026.01.20.700366v2)
- Original title: JanusX: an integrated and high-performance platform for scalable genome-wide association studies and genomic selection
- Authors: Fu, J., Jia, A., Wang, H., Liu, H.-J.
- Meta: 2026-07-16 | bioinformatics | DOI: 10.64898/2026.01.20.700366
- 中文摘要: 随着基因组数据集样本量和标记密度的扩大，全基因组关联研究 (GWAS) 和基因组选择 (GS) 需要工作流程在从基因型矩阵到决策相关输出的整个分析路径中保持统计严谨、计算高效且可重复。在这里，我们介绍 JanusX，这是一个集成的高性能框架，通过统一数据处理、模型执行和可视化，为 GWAS 和 GS 提供简化的、面向用户的工作流程。在模拟和真实数据集中，JanusX 与既定基线保持了高度一致性，同时大幅减少了运行时间和内存使用量。
- Abstract: As genomic datasets expand in both sample size and marker density, genome-wide association studies (GWAS) and genomic selection (GS) require workflows that remain statistically rigorous, computationally efficient, and reproducible across the full analysis path, from genotype matrix to decision-relevant outputs. Here we present JanusX, an integrated high-performance framework that provides a streamlined, user-oriente...
- Summary (fallback): 机器翻译摘要显示：随着基因组数据集样本量和标记密度的扩大，全基因组关联研究 (GWAS) 和基因组选择 (GS) 需要工作流程在从基因型矩阵到决策相关输出的整个分析路径中保持统计严谨、计算高效且可重复。在这里，我们介绍 JanusX，这是一个集成的高性能框架，通过统一数据处理、模型执行和可视化，为 GWAS 和 GS 提供简化的、面向用户的工作流程。在模拟和真实数据集中，JanusX 与既定基线保持了高度一致性，同时大幅减少了运行时间和内存使用量。
- Keywords: janusx, genomic, gwas, memory, integrated

### 4. [ESCRT-III 蛋白质分选机器的植物特异性 VPS2.2/HYADE 定位于分泌室，是拟南芥细胞分裂平面确定所必需的](https://www.biorxiv.org/content/10.64898/2026.07.15.738706v1)
- Original title: The plant specific VPS2.2/HYADE of the ESCRT-III protein sorting machinery localizes to a secretory compartment and is required for cell division plane determination in Arabidopsis
- Authors: Ibl, V., Pritz, C. O., Koehler, V., Mueller, S., Goessweiner-Mohr, N. et al.
- Meta: 2026-07-16 | plant biology | DOI: 10.64898/2026.07.15.738706
- 中文摘要: 划分平面的定位是细胞发育过程中的关键步骤。在动物细胞中，细胞分裂平面是在中期确定的，而在植物中，这一决定是在有丝分裂之前做出的，包括形成称为前期带 (PPB) 的细胞骨架结构。虽然不是必需的，但 PPB 构成了细胞分裂平面的最早标记，并且与胞质分裂过程中细胞板与亲本质膜融合的位点一致。最近的研究表明，内吞作用和胞吐作用参与皮质分裂区的重塑。在这里，我们展示了 Atvps2.2/hyade (hya) 拟南芥突变体中的 PPB、成膜体、细胞板和细胞壁被错位，Atvps2.2/hyade (hya) 是运输所需内体分选复合物 (ESCRT)-III 的植物特异性成分。
- Abstract: Positioning of the division plane is a critical step during cellular development. While in animal cells the plane of cell division is defined during metaphase, in plants this decision is made before mitosis and includes the formation of a cytoskeletal structure termed the preprophase band (PPB). Although not essential, the PPB constitutes the earliest mark for the plane of cell division and coincides with the sites...
- Summary (fallback): 机器翻译摘要显示：划分平面的定位是细胞发育过程中的关键步骤。在动物细胞中，细胞分裂平面是在中期确定的，而在植物中，这一决定是在有丝分裂之前做出的，包括形成称为前期带 (PPB) 的细胞骨架结构。虽然不是必需的，但 PPB 构成了细胞分裂平面的最早标记，并且与胞质分裂过程中细胞板与亲本质膜融合的位点一致。最近的研究表明，内吞作用和胞吐作用参与皮质分裂区的重塑。在这里，我们展示了 Atvps2.2/hyade (hya) 拟南芥突变体中的 PPB、成膜体、细胞板和细胞壁被错位，Atvps2.2/hyade (hya) 是运输所需内体分选复合物 (ESCRT)-III 的植物特异性成分。
- Keywords: cell, division, escrt-iii, plane, secretory

### 5. [青少年社区样本中冷酷无情特征的神经解剖学亚型](https://www.biorxiv.org/content/10.64898/2026.07.14.738524v1)
- Original title: Neuroanatomical Subtypes of Callous-Unemotional Traits in a Community Sample of Youth
- Authors: Murtha, K., Antoniades, M., Seidlitz, J., Barzilay, R., Moore, T. M. et al.
- Meta: 2026-07-16 | neuroscience | DOI: 10.64898/2026.07.14.738524
- 中文摘要: 重要性。冷酷无情（CU）特征与显着的临床和神经生理学异质性相关，可能影响治疗效果。客观的。使用弱监督机器学习揭示 CU 特征的神经解剖学亚型，并评估新出现的亚型在相关临床、气质和环境结构上是否存在差异。设计、设置和参与者。影像数据来自纵向青少年、大脑、认知发展 (ABCD) 研究。参与者基线年龄为 9-10 岁（M=9.925，69.9% 为男性），包括 222 名具有 CU 特征的儿童和 234 名年龄、性别和收入相匹配的典型对照儿童。主要成果和措施。
- Abstract: Importance. Callous Unemotional (CU) traits are associated with significant clinical and neurophysiological heterogeneity that may affect treatment effectiveness. Objective. To uncover neuroanatomical subtypes of CU traits using weakly-supervised machine learning and assess whether emerging subtypes differ on relevant clinical, temperamental, and environmental constructs. Design, Setting, and Participants. Imaging d...
- Summary (fallback): 机器翻译摘要显示：重要性。冷酷无情（CU）特征与显着的临床和神经生理学异质性相关，可能影响治疗效果。客观的。使用弱监督机器学习揭示 CU 特征的神经解剖学亚型，并评估新出现的亚型在相关临床、气质和环境结构上是否存在差异。设计、设置和参与者。影像数据来自纵向青少年、大脑、认知发展 (ABCD) 研究。参与者基线年龄为 9-10 岁（M=9.925，69.9% 为男性），包括 222 名具有 CU 特征的儿童和 234 名年龄、性别和收入相匹配的典型对照儿童。主要成果和措施。
- Keywords: subtypes, traits, clinical, volume, subtype

### 6. [一击：迷幻的见解是独特的强烈、有意义和难以言喻的](https://www.biorxiv.org/content/10.64898/2026.06.02.729484v3)
- Original title: One-shotted: psychedelic insights are uniquely intense, meaningful and ineffable
- Authors: Pogliani, A., Zachary, A., Hall, L., Tangen, J. M., Mond, J. et al.
- Meta: 2026-07-16 | neuroscience | DOI: 10.64898/2026.06.02.729484
- 中文摘要: 洞察力通常在实验室范式中被研究为伴随着特征性的“啊哈！”的理解的突然转变。经验。然而，这样的范式可能无法捕捉自然主义背景下发生的全部现象学洞察力。这项研究在一项针对有迷幻经历的成年人 (N = 73) 的受试者内在线研究中，比较了四种背景下的洞察现象学：迷幻体验、日常生活洞察、复合远程关联问题和模糊图像。参与者对每个洞察的强度、惊喜、自信、愉悦、动力、意义、不可言喻和感知信念变化进行评分。
- Abstract: Insight is commonly studied in laboratory paradigms as a sudden shift in understanding accompanied by characteristic "Aha!" experiences. However, such paradigms may not capture the full phenomenological range of insight as it occurs in naturalistic contexts. This study compared the phenomenology of insight across four contexts: psychedelic experiences, everyday-life insights, Compound Remote Associates problems, and...
- Summary (fallback): 机器翻译摘要显示：洞察力通常在实验室范式中被研究为伴随着特征性的“啊哈！”的理解的突然转变。经验。然而，这样的范式可能无法捕捉自然主义背景下发生的全部现象学洞察力。这项研究在一项针对有迷幻经历的成年人 (N = 73) 的受试者内在线研究中，比较了四种背景下的洞察现象学：迷幻体验、日常生活洞察、复合远程关联问题和模糊图像。参与者对每个洞察的强度、惊喜、自信、愉悦、动力、意义、不可言喻和感知信念变化进行评分。
- Keywords: belief, insight, change, insights, meaning

### 7. [基于结构的哺乳动物 DNA 转座体重铸为专性异二聚体](https://www.biorxiv.org/content/10.64898/2026.07.15.738711v1)
- Original title: Structure-based recasting of a mammalian DNA transpososomeas an obligate heterodimer
- Authors: Mandal, R., Hickman, A. B., Desai, R., Primich, A., Dyda, F.
- Meta: 2026-07-16 | molecular biology | DOI: 10.64898/2026.07.15.738711
- 中文摘要: 真核 DNA 转座体组装为含有多个相同转座酶原体的核蛋白复合物。我们确定了过度活跃的荧光鼠耳蝠 PiggyBat 转座体的结构，并发现它使用不寻常的新月形、不对称四聚体来突触发散反向末端重复。我们发现相同的氨基酸序列基序采用不同的作用来介导两种 DNA 结合模式：一种进行链转移，另一种缺乏催化活性，促进突触，同时保护转座子免受其活性位点的自毁性内部裂解。在观察到的组装模块性的指导下，我们通过识别抑制同二聚体形成的突变，并将其与防止非靶向整合的特定点突变配对，设计了专性异二聚体系统。
- Abstract: Eukaryotic DNA transpososomes assemble as nucleoprotein complexes containing multiple identical transposase protomers. We determined the structure of the hyperactive Myotis lucifugus piggyBat transpososome and discovered that it uses an unusual crescent-shaped, asymmetric tetramer to synapse divergent inverted terminal repeats. We found that identical amino-acid sequence motifs adopt distinct roles to mediate two mo...
- Summary (fallback): 机器翻译摘要显示：真核 DNA 转座体组装为含有多个相同转座酶原体的核蛋白复合物。我们确定了过度活跃的荧光鼠耳蝠 PiggyBat 转座体的结构，并发现它使用不寻常的新月形、不对称四聚体来突触发散反向末端重复。我们发现相同的氨基酸序列基序采用不同的作用来介导两种 DNA 结合模式：一种进行链转移，另一种缺乏催化活性，促进突触，同时保护转座子免受其活性位点的自毁性内部裂解。在观察到的组装模块性的指导下，我们通过识别抑制同二聚体形成的突变，并将其与防止非靶向整合的特定点突变配对，设计了专性异二聚体系统。
- Keywords: sequence, obligate, heterodimer, identical, heterodimeric

### 8. [ALMS1 有助于中心粒近端结构和稳定性](https://www.biorxiv.org/content/10.64898/2026.07.15.738620v1)
- Original title: ALMS1 contributes to centriole proximal architecture and stability
- Authors: De Freitas, S., Riparbelli, M. G., Callaini, G., Laporte, M. H., Durand, B. et al.
- Meta: 2026-07-16 | cell biology | DOI: 10.64898/2026.07.15.738620
- 中文摘要: 中心粒是高度组织化的微管支架，在连续的细胞周期中逐渐生长和成熟。它们的分子组织已被广泛表征，但几种成分对中心粒组装、成熟或稳定性的贡献尚不完全清楚。在这里，我们使用超微结构膨胀显微镜和透射电子显微镜，证明阿尔斯特罗姆综合征中的突变蛋白 ALMS1 是正确的中心粒结构所必需的。在缺乏 ALMS1 的情况下，RPE1 细胞表现出较短的中心粒，微管壁存在缺陷，包括断裂或缺失的三联体或开放的 B/C 小管。这些结构缺陷是在原中心粒组装后出现的。我们发现 ALMS1 丢失选择性地减少了近端区域蛋白 CCDC77 和 CEP44，而留下完整的中央和远端区域蛋白。
- Abstract: Centrioles are highly organised microtubular scaffolds which grow and mature progressively during successive cell cycles. Their molecular organisation is extensively characterized, yet the contribution of several components to centriole assembly, maturation or stability is incompletely understood. Here, using ultrastructure expansion microscopy and transmission electron microscopy, we show that ALMS1, the protein mu...
- Summary (fallback): 机器翻译摘要显示：中心粒是高度组织化的微管支架，在连续的细胞周期中逐渐生长和成熟。它们的分子组织已被广泛表征，但几种成分对中心粒组装、成熟或稳定性的贡献尚不完全清楚。在这里，我们使用超微结构膨胀显微镜和透射电子显微镜，证明阿尔斯特罗姆综合征中的突变蛋白 ALMS1 是正确的中心粒结构所必需的。在缺乏 ALMS1 的情况下，RPE1 细胞表现出较短的中心粒，微管壁存在缺陷，包括断裂或缺失的三联体或开放的 B/C 小管。这些结构缺陷是在原中心粒组装后出现的。我们发现 ALMS1 丢失选择性地减少了近端区域蛋白 CCDC77 和 CEP44，而留下完整的中央和远端区域蛋白。
- Keywords: alms1, proximal, centriole, centrioles, required

### 9. [澳大利亚新西兰细胞外囊泡学会 (ANZSEV) 社区调查](https://www.biorxiv.org/content/10.64898/2026.07.06.736235v1)
- Original title: Survey of the Australian New Zealand Society for Extracellular Vesicles (ANZSEV) Community
- Authors: Hourigan, L., Danielson, K., Cheng, L.
- Meta: 2026-07-16 | cell biology | DOI: 10.64898/2026.07.06.736235
- 中文摘要: 澳大利亚新西兰细胞外囊泡学会 (ANZSEV) 于 2021 年正式成立，是 EV 研究人员的区域性学会。该学会举办年度会议，展示世界一流的研究成果，提供本地和国际联网与合作的机会，积极支持 ECR 网络，举办小型研讨会，并为会员提供各种指导和奖励的机会。作为最近概述协会历史的项目的补充，我们对 ANZSEV 成员及其更广泛的网络进行了调查。四十人参与了这项调查，调查结果揭示了 ANZSEV 社区的构成、兴趣和信仰。
- Abstract: The Australian New Zealand Society for Extracellular Vesicles (ANZSEV) was formally established in 2021 as a regional society for EV researchers. The society holds an annual meeting showcasing world-class research, provides opportunities for local and international networking and collaboration, actively supports a network of ECRs, holds mini-symposiums and provides various opportunities for mentorship and awards for...
- Summary (fallback): 机器翻译摘要显示：澳大利亚新西兰细胞外囊泡学会 (ANZSEV) 于 2021 年正式成立，是 EV 研究人员的区域性学会。该学会举办年度会议，展示世界一流的研究成果，提供本地和国际联网与合作的机会，积极支持 ECR 网络，举办小型研讨会，并为会员提供各种指导和奖励的机会。作为最近概述协会历史的项目的补充，我们对 ANZSEV 成员及其更广泛的网络进行了调查。四十人参与了这项调查，调查结果揭示了 ANZSEV 社区的构成、兴趣和信仰。
- Keywords: society, anzsev, survey, australian, zealand

### 10. [类器官揭示了生态位特异性机械转导引导的人类皮质模式和细胞命运获取](https://www.biorxiv.org/content/10.64898/2026.07.15.736390v1)
- Original title: Organoids reveal niche-specific mechanotransduction-guided human cortical patterning and cell fate acquisition
- Authors: Kingston, A. J., Wurmser, A. A. M., Kulkarni, A. S., Miao, K., Agsu, G. G. et al.
- Meta: 2026-07-16 | developmental biology | DOI: 10.64898/2026.07.15.736390
- 中文摘要: 发育中的大脑皮层的高度动态的机械环境有可能编码对神经元分化至关重要的信息。局部生物物理特性的变化涉及从神经祖细胞的维持到远程轴突引导的过程。然而，皮质力学是否影响神经发生过程中的细胞组织和规范仍然很大程度上尚未被探索。在这里，我们利用人类皮质发育的 3D 镶嵌类器官模型，在该模型中，我们选择性地破坏核机械传感的关键组成部分，即 LINC 复合体，使细胞与其机械环境脱钩。我们表明，LINC 解偶联以隔室特异性方式改变核形态，驱动优先排除生发区并伴随着过早分化。
- Abstract: The highly dynamic mechanical environment of the developing cerebral cortex has the potential to encode information vital for neuronal differentiation. Changes in local biophysical properties have been implicated in processes ranging from the maintenance of neural progenitors to long-range axon guidance. However, whether cortical mechanics influence cellular organisation and specification during neurogenesis remains...
- Summary (fallback): 机器翻译摘要显示：发育中的大脑皮层的高度动态的机械环境有可能编码对神经元分化至关重要的信息。局部生物物理特性的变化涉及从神经祖细胞的维持到远程轴突引导的过程。然而，皮质力学是否影响神经发生过程中的细胞组织和规范仍然很大程度上尚未被探索。在这里，我们利用人类皮质发育的 3D 镶嵌类器官模型，在该模型中，我们选择性地破坏核机械传感的关键组成部分，即 LINC 复合体，使细胞与其机械环境脱钩。我们表明，LINC 解偶联以隔室特异性方式改变核形态，驱动优先排除生发区并伴随着过早分化。
- Keywords: cortical, fate, mechanical, environment, differentiation

### 11. [提取工作流程决定了落叶 eDNA 元条形码中标记特异性的回收率和重现性](https://www.biorxiv.org/content/10.64898/2026.07.15.738510v1)
- Original title: Extraction workflow determines marker-specific recovery andreproducibility in leaf-litter eDNA metabarcoding
- Authors: Weber, S., Banerjee, P., Scali, E., Farrow, A. A., Boren, A. M. et al.
- Meta: 2026-07-16 | ecology | DOI: 10.64898/2026.07.15.738510
- 中文摘要: 森林地面落叶层是一个动态且结构复杂的生态过渡区，因此是陆地 eDNA 元条形码的有前景的基质。然而，这种异质基质的提取工作流程仍然缺乏标准化，特别是在热带系统中，因此基本上不可能跨空间、时间和分类单元比较生态功能。为了指导一系列选择标准（包括生物目标、研究问题和实际考虑因素）的工作流程选择，我们比较了从夏威夷欧胡岛七个不同森林地点的 42 个生物样本收集的落叶 eDNA 的 DNA 提取工作流程。
- Abstract: Forest-floor leaf litter is a dynamic and structurally complex ecological transition zone and thus a promising substrate for terrestrial eDNA metabarcoding. Yet, extraction workflows for this heterogeneous matrix remain poorly standardized, especially in tropical systems, making it largely impossible to compare ecological functions across space, time, and taxa. To guide workflow selection across a series of selectio...
- Summary (fallback): 机器翻译摘要显示：森林地面落叶层是一个动态且结构复杂的生态过渡区，因此是陆地 eDNA 元条形码的有前景的基质。然而，这种异质基质的提取工作流程仍然缺乏标准化，特别是在热带系统中，因此基本上不可能跨空间、时间和分类单元比较生态功能。为了指导一系列选择标准（包括生物目标、研究问题和实际考虑因素）的工作流程选择，我们比较了从夏威夷欧胡岛七个不同森林地点的 42 个生物样本收集的落叶 eDNA 的 DNA 提取工作流程。
- Keywords: extraction, workflows, workflow, across, edna

### 12. [代谢过程塑造微生物相互作用分布](https://www.biorxiv.org/content/10.64898/2026.07.15.738716v1)
- Original title: Metabolic processes shape microbial interaction distributions
- Authors: Padmanabha, P., Mitri, S.
- Meta: 2026-07-16 | ecology | DOI: 10.64898/2026.07.15.738716
- 中文摘要: 微生物群落很大程度上是由代谢相互作用驱动的，物种通过这种相互作用争夺共享资源并交换副产品。此类相互作用通常仅根据其符号进行分类。然而，理论表明，相互作用的强度及其分布的形状会影响共存的物种数量和种类。这种形状在微生物群落中是什么样子以及为什么很少被研究。从资源竞争和交叉喂养的消费者资源模型开始，我们发现这些代谢过程产生了一种偏态分布，具有“许多弱，很少强”的相互作用——这种模式以前在大型生物体的食物网中记录过。当物种具有不同的底物偏好并且代谢物泄漏足够高时，就会出现这种偏差。
- Abstract: Microbial communities are largely driven by metabolic interactions, whereby species compete for shared resources and exchange byproducts. Such interactions are commonly classified by their sign alone. Yet, theory shows that the strength of interactions and the shape of their distribution impact how many and which species coexist. What this shape looks like in microbial communities and why has rarely been examined. S...
- Summary (fallback): 机器翻译摘要显示：微生物群落很大程度上是由代谢相互作用驱动的，物种通过这种相互作用争夺共享资源并交换副产品。此类相互作用通常仅根据其符号进行分类。然而，理论表明，相互作用的强度及其分布的形状会影响共存的物种数量和种类。这种形状在微生物群落中是什么样子以及为什么很少被研究。从资源竞争和交叉喂养的消费者资源模型开始，我们发现这些代谢过程产生了一种偏态分布，具有“许多弱，很少强”的相互作用——这种模式以前在大型生物体的食物网中记录过。当物种具有不同的底物偏好并且代谢物泄漏足够高时，就会出现这种偏差。
- Keywords: interactions, distribution, microbial, metabolic, interaction

### 13. [为什么植物会产生阿片类药物？测试卡痛叶中精神活性生物碱的食草动物防御假说](https://www.biorxiv.org/content/10.64898/2026.07.15.738691v1)
- Original title: Why do plants make opioids? Testing the herbivore defense hypothesis for psychoactive alkaloids in kratom
- Authors: McNutt, B. D., Whitaker, M. R. L.
- Meta: 2026-07-16 | ecology | DOI: 10.64898/2026.07.15.738691
- 中文摘要: 越来越多的文献提出，具有精神活性的植物化合物是为了防御草食性昆虫而进化的，它们对人类的神经系统影响是保守受体结构的进化意外。这个假说——我们称之为食草动物防御假说——被广泛引用，但很少经过实证检验。我们报告了一种受控饮食生物测定，其中向草地贪夜蛾幼虫喂食人工饲料，其中含有冻干卡痛叶粉或纯化的帽柱木碱（卡痛叶中的主要精神活性化合物）。在所有测试浓度下，卡痛叶会导致剂量依赖性幼虫死亡率、抑制生长率并降低化蛹率，在最高剂量下几乎完全死亡。
- Abstract: A growing body of literature proposes that psychoactive plant compounds evolved as defenses against herbivorous insects, with their neurological effects in humans an evolutionary accident of conserved receptor architecture. This hypothesis - which we call the herbivore defense hypothesis - is widely invoked but rarely tested empirically. We report a controlled dietary bioassay in which Spodoptera frugiperda larvae w...
- Summary (fallback): 机器翻译摘要显示：越来越多的文献提出，具有精神活性的植物化合物是为了防御草食性昆虫而进化的，它们对人类的神经系统影响是保守受体结构的进化意外。这个假说——我们称之为食草动物防御假说——被广泛引用，但很少经过实证检验。我们报告了一种受控饮食生物测定，其中向草地贪夜蛾幼虫喂食人工饲料，其中含有冻干卡痛叶粉或纯化的帽柱木碱（卡痛叶中的主要精神活性化合物）。在所有测试浓度下，卡痛叶会导致剂量依赖性幼虫死亡率、抑制生长率并降低化蛹率，在最高剂量下几乎完全死亡。
- Keywords: hypothesis, psychoactive, kratom, leaf, herbivore

### 14. [果蝇 grimshawi 中 DENR 直系同源基因模型](https://www.biorxiv.org/content/10.64898/2026.07.14.738501v1)
- Original title: Gene model for the ortholog of DENR in Drosophila grimshawi
- Authors: Lawson, M. E., Sanow, K. A., Fratian, M., Matura, M., Burton, I. et al.
- Meta: 2026-07-16 | genomics | DOI: 10.64898/2026.07.14.738501
- 中文摘要: 2011 年 5 月 D. grimshawi 的密度调节蛋白 (DENR) 直向同源基因模型 (Agencourt dgri_caf1/DgriCAF1) 基因组组装（GenBank 登录号：GCA_000005155.1）。该直向同源物被描述为正在开发的数据集的一部分，用于使用基于课程的本科生研究经验的基因组学教育合作伙伴基因注释协议来研究果蝇属胰岛素/胰岛素样生长因子信号通路（IIS）的进化。
- Abstract: Gene model for the ortholog of Density regulated protein (DENR) in the May 2011 (Agencourt dgri_caf1/DgriCAF1) Genome Assembly (GenBank Accession: GCA_000005155.1) of D. grimshawi. This ortholog was characterized as part of a developing dataset to study the evolution of the Insulin/insulin-like growth factor signaling pathway (IIS) across the genus Drosophila using the Genomics Education Partnership gene annotation...
- Summary (fallback): 机器翻译摘要显示：2011 年 5 月 D. grimshawi 的密度调节蛋白 (DENR) 直向同源基因模型 (Agencourt dgri_caf1/DgriCAF1) 基因组组装（GenBank 登录号：GCA_000005155.1）。该直向同源物被描述为正在开发的数据集的一部分，用于使用基于课程的本科生研究经验的基因组学教育合作伙伴基因注释协议来研究果蝇属胰岛素/胰岛素样生长因子信号通路（IIS）的进化。
- Keywords: gene, ortholog, model, denr, drosophila

### 15. [生物学的自发进化](https://www.biorxiv.org/content/10.64898/2026.07.14.738476v1)
- Original title: The Spontaneous Evolution of Biology
- Authors: ten Have, S., McMillan, E., Medway, T., Kent, R., Prescott, A. R.
- Meta: 2026-07-16 | biochemistry | DOI: 10.64898/2026.07.14.738476
- 中文摘要: 我们已经证明了氨基酸在缺乏细胞机器（包括核酸、脂质或糖）的情况下聚合成肽、蛋白质并形成细胞样结构的潜力。不仅观察到无细胞蛋白质复制，而且蛋白质模板化的证据强烈表明蛋白质介导的复制。我们相信，这是米勒-尤里实验（从元素起始材料生产氨基酸）与细胞样结构之间联系的首次实验证明。根据定义，生命是动物和植物区别于无机物的条件，包括生长、繁殖、功能活动和死亡前持续变化的能力。
- Abstract: We have demonstrated the potential of amino acids to polymerise into peptides, proteins, and form cell-like structures in the absence of cellular machinery, including nucleic acids, lipids or sugars. Not only has cell-free protein replication been observed, but evidence of protein templating strongly suggests protein mediated replication. We believe this is the first experimental demonstration of the link between th...
- Summary (fallback): 机器翻译摘要显示：我们已经证明了氨基酸在缺乏细胞机器（包括核酸、脂质或糖）的情况下聚合成肽、蛋白质并形成细胞样结构的潜力。不仅观察到无细胞蛋白质复制，而且蛋白质模板化的证据强烈表明蛋白质介导的复制。我们相信，这是米勒-尤里实验（从元素起始材料生产氨基酸）与细胞样结构之间联系的首次实验证明。根据定义，生命是动物和植物区别于无机物的条件，包括生长、繁殖、功能活动和死亡前持续变化的能力。
- Keywords: evolution, acids, which, amino, structures

### 16. [用于组织重塑多参数分析的高通量 3D 微组织平台。](https://www.biorxiv.org/content/10.64898/2026.07.15.738540v1)
- Original title: A high-throughput, 3D microtissue platform for multiparametric analysis of tissue remodeling.
- Authors: Vasan, A., Nguyen, Q., Davis, E., Karakan, M. C., Westphal, E. et al.
- Meta: 2026-07-16 | bioengineering | DOI: 10.64898/2026.07.15.738540
- 中文摘要: 细胞外基质（ECM）重塑和力产生是组织形态发生和修复的基本驱动因素，但定量研究这些动态机械过程的可扩展方法仍然有限。在这里，我们提出了一个高通量筛选平台，该平台将工程三维 (3D) 微组织集成在标准化 96 孔格式中。我们引入了强大的模具铸造制造工艺和逐层表面改性策略，可确保长期组织稳定性并防止脱离（95% 组织形成成功；在培养物中稳定超过 10 天）。该系统能够通过相差成像方式同时纵向量化组织闭合、组织收缩性和组织压实。
- Abstract: Extracellular matrix (ECM) remodeling and force generation are fundamental drivers of tissue morphogenesis and repair, yet scalable methods to quantitatively interrogate these dynamic mechanical processes remain limited. Here, we present a high-throughput screening platform that integrates engineered three-dimensional (3D) microtissues within a standardized 96-well format. We introduce a robust mold-casting fabricat...
- Summary (fallback): 机器翻译摘要显示：细胞外基质（ECM）重塑和力产生是组织形态发生和修复的基本驱动因素，但定量研究这些动态机械过程的可扩展方法仍然有限。在这里，我们提出了一个高通量筛选平台，该平台将工程三维 (3D) 微组织集成在标准化 96 孔格式中。我们引入了强大的模具铸造制造工艺和逐层表面改性策略，可确保长期组织稳定性并防止脱离（95% 组织形成成功；在培养物中稳定超过 10 天）。该系统能够通过相差成像方式同时纵向量化组织闭合、组织收缩性和组织压实。
- Keywords: tissue, remodeling, platform, high-throughput, analysis

### 17. [单个糖胺聚糖连接的残余应变系数解释了猪胸主动脉耗尽后区域张开角度的变化](https://www.biorxiv.org/content/10.64898/2026.07.15.738269v1)
- Original title: A single glycosaminoglycan-linked residual-straincoefficient explains regional opening angle changes afterdepletion in the porcine thoracic aorta
- Authors: Labrosse, M. R., Ghadie, N., St-Pierre, J.-P., Boodhwani, M.
- Meta: 2026-07-16 | bioengineering | DOI: 10.64898/2026.07.15.738269
- 中文摘要: 动脉中的残余应力通常通过径向切割后环的打开来显示。糖胺聚糖 (GAG) 有助于这种反应，但固定电荷密度 (FCD) 驱动的唐南膨胀本身并不能完全解释酶促 GAG 耗尽后测量到的张角减小。因此，我们测试了透壁 FCD 轮廓是否定义了叠加在 GAG 耗尽后保留的结构场上的可去除的首选拉伸场。将简化的分析计算轴对称闭合框架应用于升主动脉、弓和降猪胸主动脉的区域平均测量。每个控制状态均使用其测量的圆周张开角度、几何形状、材料特性和全壁 FCD 轮廓进行拟合。 GAG 消耗通过去除 FCD 连接的首选拉伸成分来表示。
- Abstract: Residual stresses in arteries are commonly revealed by the opening of a ring after a radial cut. Glycosaminoglycans (GAGs) contribute to this response, but fixed-chargedensity (FCD)-driven Donnan swelling alone does not fully explain the opening-angle reduction measured after enzymatic GAG depletion. We therefore tested whether the transmural FCD profile defines a removable preferred-stretch field superposed on a st...
- Summary (fallback): 机器翻译摘要显示：动脉中的残余应力通常通过径向切割后环的打开来显示。糖胺聚糖 (GAG) 有助于这种反应，但固定电荷密度 (FCD) 驱动的唐南膨胀本身并不能完全解释酶促 GAG 耗尽后测量到的张角减小。因此，我们测试了透壁 FCD 轮廓是否定义了叠加在 GAG 耗尽后保留的结构场上的可去除的首选拉伸场。将简化的分析计算轴对称闭合框架应用于升主动脉、弓和降猪胸主动脉的区域平均测量。每个控制状态均使用其测量的圆周张开角度、几何形状、材料特性和全壁 FCD 轮廓进行拟合。 GAG 消耗通过去除 FCD 连接的首选拉伸成分来表示。
- Keywords: degrees, measured, depletion, regional, opening

### 18. [生物医学文献文本摘要方法的系统评估和基准测试：从词频方法到语言模型](https://www.biorxiv.org/content/10.64898/2026.01.09.697335v4)
- Original title: Systematic evaluation and benchmarking of text summarization methods for biomedical literature: From word-frequency methods to language models
- Authors: Baumgärtel, F., Bono, E., Fillinger, L., Galou, L., Keska-Izworska, K. et al.
- Meta: 2026-07-16 | bioinformatics | DOI: 10.64898/2026.01.09.697335
- 中文摘要: 生物医学文献的快速扩展需要自动摘要工具，能够可靠地将研究文章浓缩成简洁、准确的概述。我们对 62 种文本摘要方法进行了基准测试 - 从基于频率的 TextRank 提取器到现代编码器解码器模型 (EDM) 和大型语言模型 (LLM) - 在一组 1,000 份生物医学摘要上进行了基准测试，其中作者生成的亮点部分可作为参考摘要。使用涵盖词汇重叠（ROUGE-1/2/L、BLEU、METEOR）、基于嵌入的语义相似性（RoBERTa、DeBERTa、all-mpnet-base-v2）和事实一致性（AlignScore）的复合指标套件来评估模型。我们的结果表明，通用语言模型（LM）在词汇和语义指标上取得了最高的总体得分，优于面向推理和特定领域的模型。
- Abstract: The rapid expansion of biomedical literature demands automated summarization tools that can reliably condense research articles into concise, accurate overviews. We benchmarked 62 text summarization methods - ranging from frequency-based and TextRank extractors to modern encoder-decoder models (EDMs) and large language models (LLMs) - on a set of 1,000 biomedical abstracts for which author-generated highlights secti...
- Summary (fallback): 机器翻译摘要显示：生物医学文献的快速扩展需要自动摘要工具，能够可靠地将研究文章浓缩成简洁、准确的概述。我们对 62 种文本摘要方法进行了基准测试 - 从基于频率的 TextRank 提取器到现代编码器解码器模型 (EDM) 和大型语言模型 (LLM) - 在一组 1,000 份生物医学摘要上进行了基准测试，其中作者生成的亮点部分可作为参考摘要。使用涵盖词汇重叠（ROUGE-1/2/L、BLEU、METEOR）、基于嵌入的语义相似性（RoBERTa、DeBERTa、all-mpnet-base-v2）和事实一致性（AlignScore）的复合指标套件来评估模型。我们的结果表明，通用语言模型（LM）在词汇和语义指标上取得了最高的总体得分，优于面向推理和特定领域的模型。
- Keywords: models, summarization, methods, biomedical, language

### 19. [高葡萄糖通过 GLUT1 表观遗传重连赋予衰老抵抗力，从而减弱食管鳞状细胞癌的免疫治疗反应](https://www.biorxiv.org/content/10.64898/2026.07.15.738372v1)
- Original title: High glucose confers senescence resistance via GLUT1 epigenetic rewiring to blunt immunotherapy responses in esophageal squamous cell carcinoma
- Authors: Dong, J.-X., Zhou, J., Hao, J.-J., Kong, S., Yin, C. et al.
- Meta: 2026-07-16 | cancer biology | DOI: 10.64898/2026.07.15.738372
- 中文摘要: 治疗耐药和不确定的预测生物标志物严重阻碍了食管鳞状细胞癌（ESCC）免疫治疗的临床普及。在此，我们将葡萄糖转运蛋白 1 (GLUT1) 确定为免疫治疗耐药性的关键决定因素。 GLUT1 表达升高与 ESCC 患者免疫治疗反应不佳和预后不良相关。 GLUT1 缺失或抑制会增强 CD8 T 细胞浸润和细胞毒性，并使 ESCC 肿瘤对抗 PD-1 (-PD1) 治疗敏感。重要的是，当与 -PD1 结合时，饮食葡萄糖限制表现出与 GLUT1 抑制相当的抗肿瘤功效。从机制上讲，GLUT1 与 HAT1 和 FOXM1 建立正反馈环，通过表观遗传重塑染色质可及性以抑制肿瘤细胞衰老，从而阻碍 CD8 T 细胞介导的抗肿瘤免疫。
- Abstract: Therapeutic resistance and undefined predictive biomarkers severely hinder the clinical popularization of immunotherapy in esophageal squamous cell carcinoma (ESCC). Herein, we identify the glucose transporter 1 (GLUT1) as a critical determinant of immunotherapy resistance. Elevated expression of GLUT1 correlates with poor immunotherapy response and unfavorable prognosis in ESCC patients. GLUT1 deletion or inhibitio...
- Summary (fallback): 机器翻译摘要显示：治疗耐药和不确定的预测生物标志物严重阻碍了食管鳞状细胞癌（ESCC）免疫治疗的临床普及。在此，我们将葡萄糖转运蛋白 1 (GLUT1) 确定为免疫治疗耐药性的关键决定因素。 GLUT1 表达升高与 ESCC 患者免疫治疗反应不佳和预后不良相关。 GLUT1 缺失或抑制会增强 CD8 T 细胞浸润和细胞毒性，并使 ESCC 肿瘤对抗 PD-1 (-PD1) 治疗敏感。重要的是，当与 -PD1 结合时，饮食葡萄糖限制表现出与 GLUT1 抑制相当的抗肿瘤功效。从机制上讲，GLUT1 与 HAT1 和 FOXM1 建立正反馈环，通过表观遗传重塑染色质可及性以抑制肿瘤细胞衰老，从而阻碍 CD8 T 细胞介导的抗肿瘤免疫。
- Keywords: glut1, immunotherapy, glucose, resistance, cell

### 20. [Tegavivint 在 Wnt 激活的肝细胞癌中的临床前疗效和安全性](https://www.biorxiv.org/content/10.64898/2026.07.14.738585v1)
- Original title: Preclinical efficacy and safety of Tegavivint in Wnt-activated hepatocellular carcinoma
- Authors: Suzuki, T., Curran, C., Drake, T. M., May, S., Yin Swe, K. L. et al.
- Meta: 2026-07-16 | cancer biology | DOI: 10.64898/2026.07.14.738585
- 中文摘要: 背景与目标：肝细胞癌（HCC）是肝癌的主要形式，仍然是临床上未满足的重大需求。鉴于 30% 至 50% 的 HCC 病例存在 Wnt/{β}-catenin 信号通路突变，针对该级联反应代表了一种有前景的治疗策略。然而，Wnt抑制剂的临床转化受到临床前模型和早期临床试验中观察到的严重不良事件的阻碍，这主要是由于Wnt信号传导在维持肠道和骨骼等正常组织中的重要作用。方法：我们检查了 Tegavivint（一种针对 TBL1 的一流 Wnt 通路抑制剂）对抗 HCC 的功效，以阐明其潜在作用机制。
- Abstract: Background & Aims: Hepatocellular carcinoma (HCC), a predominant form of liver cancer, remains a significant clinical unmet need. Given that 30 to 50% of HCC cases harbour mutations in the Wnt/{beta}-catenin signalling pathway, targeting this cascade represents a promising therapeutic strategy. However, the clinical translation of Wnt inhibitors has been hindered by severe adverse events observed in preclinical mode...
- Summary (fallback): 机器翻译摘要显示：背景与目标：肝细胞癌（HCC）是肝癌的主要形式，仍然是临床上未满足的重大需求。鉴于 30% 至 50% 的 HCC 病例存在 Wnt/{β}-catenin 信号通路突变，针对该级联反应代表了一种有前景的治疗策略。然而，Wnt抑制剂的临床转化受到临床前模型和早期临床试验中观察到的严重不良事件的阻碍，这主要是由于Wnt信号传导在维持肠道和骨骼等正常组织中的重要作用。方法：我们检查了 Tegavivint（一种针对 TBL1 的一流 Wnt 通路抑制剂）对抗 HCC 的功效，以阐明其潜在作用机制。
- Keywords: tegavivint, pathway, cell, efficacy, cancer

### 21. [选择性靶向少突胶质细胞 GPR17 受体可改善雌性 SOD1G93A 小鼠的髓磷脂完整性和运动功能](https://www.biorxiv.org/content/10.64898/2026.04.28.721299v2)
- Original title: Selective targeting of the oligodendroglial GPR17 receptor improves myelin integrity and motor function in female SOD1G93A mice
- Authors: Raffaele, S., Bonifacino, T., Mannella, F. C., Nguyen, N., Torazza, C. et al.
- Meta: 2026-07-16 | pharmacology and toxicology | DOI: 10.64898/2026.04.28.721299
- 中文摘要: 肌萎缩侧索硬化症（ALS）是一种致命的神经退行性疾病，目前尚无明确的疾病缓解疗法，这凸显了迫切需要确定新的药物靶点。 G 蛋白偶联受体 GPR17 是少突胶质细胞成熟的关键调节因子，已成为 ALS 的候选靶点，但其与人类疾病和治疗潜力的相关性仍不清楚。在这里，我们证明病理性 GPR17 上调定义了人类 ALS 中保守的、病理学上不成熟的少突胶质细胞状态，可以在药理学上利用它来恢复髓磷脂完整性并改善体内功能结果。公开的转录组学数据集和组织学分析显示，与非神经系统对照相比，ALS 病例死后人类脊髓组织中表达 GPR17 的未成熟少突胶质细胞的丰度增加......
- Abstract: Amyotrophic lateral sclerosis (ALS) is a fatal neurodegenerative disease with no definitive disease-modifying therapies available, underscoring the urgent need to identify novel druggable targets. The G protein-coupled receptor GPR17 is a critical regulator of oligodendrocyte maturation and has emerged as a candidate target in ALS, yet its relevance to human disease and therapeutic potential remain unclear. Here, we...
- Summary (fallback): 机器翻译摘要显示：肌萎缩侧索硬化症（ALS）是一种致命的神经退行性疾病，目前尚无明确的疾病缓解疗法，这凸显了迫切需要确定新的药物靶点。 G 蛋白偶联受体 GPR17 是少突胶质细胞成熟的关键调节因子，已成为 ALS 的候选靶点，但其与人类疾病和治疗潜力的相关性仍不清楚。在这里，我们证明病理性 GPR17 上调定义了人类 ALS 中保守的、病理学上不成熟的少突胶质细胞状态，可以在药理学上利用它来恢复髓磷脂完整性并改善体内功能结果。公开的转录组学数据集和组织学分析显示，与非神经系统对照相比，ALS 病例死后人类脊髓组织中表达 GPR17 的未成熟少突胶质细胞的丰度增加......
- Keywords: gpr17, mice, oligodendroglial, sod1g93a, myelin

### 22. [用于调节 CAR T 细胞的药理学调节生物正交稳定结构域](https://www.biorxiv.org/content/10.64898/2026.07.15.738628v1)
- Original title: Pharmacologically regulated bioorthogonal stabilization domain for regulation of CAR T cells
- Authors: Rihtar, E., Fink, T., Belak, M., Udvanc, R., Jerala, R.
- Meta: 2026-07-16 | synthetic biology | DOI: 10.64898/2026.07.15.738628
- 中文摘要: 治疗细胞反应的调节对于安全有效的治疗非常重要，特别是对于免疫治疗。理想情况下，调节剂应基于人类蛋白质，使用已被批准用于人类使用的化合物。小分子对蛋白质降解的调节可以实现快速的细胞反应和较小的基因构建体的遗传足迹。在这里，我们提出了一种临床相容的策略，使用基于人雌激素受体 (ER) 的降解决定子结构域和 FDA 批准的小分子对嵌合抗原受体 (CAR) T 细胞功能进行可逆药理学控制。通过将他莫昔芬响应的 ER 配体结合结构域与 CAR 融合，我们生成了配体诱导型 ON-switch CAR，其稳定性、信号传导和效应器功能由 4-羟基他莫昔芬精确控制。
- Abstract: Regulation of therapeutic cell response is important for safe and effective therapy, particularly for immunotherapy. Ideally, the regulators should be based on human proteins using compounds that have already been approved for human use. Regulation of protein degradation by small molecules enables fast cellular response and a small genetic footprint of genetic constructs. Here, we present a clinically compatible str...
- Summary (fallback): 机器翻译摘要显示：治疗细胞反应的调节对于安全有效的治疗非常重要，特别是对于免疫治疗。理想情况下，调节剂应基于人类蛋白质，使用已被批准用于人类使用的化合物。小分子对蛋白质降解的调节可以实现快速的细胞反应和较小的基因构建体的遗传足迹。在这里，我们提出了一种临床相容的策略，使用基于人雌激素受体 (ER) 的降解决定子结构域和 FDA 批准的小分子对嵌合抗原受体 (CAR) T 细胞功能进行可逆药理学控制。通过将他莫昔芬响应的 ER 配体结合结构域与 CAR 融合，我们生成了配体诱导型 ON-switch CAR，其稳定性、信号传导和效应器功能由 4-羟基他莫昔芬精确控制。
- Keywords: regulation, human, small, cars, bioorthogonal

### 23. [层解析诊断可识别深度神经网络中偏差驱动的决策](https://www.biorxiv.org/content/10.1101/2025.09.16.676625v7)
- Original title: A layer-resolved diagnostic identifies bias-driven decisions in deep neural networks
- Authors: Nakuci, J.
- Meta: 2026-07-16 | neuroscience | DOI: 10.1101/2025.09.16.676625
- 中文摘要: 现代人工智能系统可以准确且自信，但仅凭这一点并不能揭示决策是否得到输入的良好支持。这就产生了信任问题，因为信心报告了模型的决定性，但没有支持这种决定性。在这里，我们表明神经网络置信度可以分解为输入相关的特征支持和输入无关的偏移支持。我们通过偏差主导指数（BDI）形式化这种分解，这是一种层解析的度量，量化与输入无关的偏移量对决策边际的相对贡献，揭示置信度主要是特征支持的还是偏差驱动的。在卷积神经网络、视觉转换器和转换器语言模型中，BDI 表明高置信度可以与偏差驱动的决策共存。层解析分析映射了跨网络深度的偏差驱动支持。
- Abstract: Modern AI systems can be accurate and confident, but this alone does not reveal whether a decision is well supported by the input. This creates a trust problem because confidence reports how decisive a model is, but not what supports that decisiveness. Here we show that neural-network confidence can be decomposed into input-dependent feature support and input-independent offset support. We formalize this decompositi...
- Summary (fallback): 机器翻译摘要显示：现代人工智能系统可以准确且自信，但仅凭这一点并不能揭示决策是否得到输入的良好支持。这就产生了信任问题，因为信心报告了模型的决定性，但没有支持这种决定性。在这里，我们表明神经网络置信度可以分解为输入相关的特征支持和输入无关的偏移支持。我们通过偏差主导指数（BDI）形式化这种分解，这是一种层解析的度量，量化与输入无关的偏移量对决策边际的相对贡献，揭示置信度主要是特征支持的还是偏差驱动的。在卷积神经网络、视觉转换器和转换器语言模型中，BDI 表明高置信度可以与偏差驱动的决策共存。层解析分析映射了跨网络深度的偏差驱动支持。
- Keywords: bias-driven, confidence, decision, layer-resolved, decisions

### 24. [我们了解方向选择性吗？模拟研究](https://www.biorxiv.org/content/10.64898/2026.07.14.732589v1)
- Original title: Do we understand orientation selectivity? A simulation study
- Authors: Dictus, H. T., Arnaudon, A., Mandge, D., Herttauinen, J., Markram, H. et al.
- Meta: 2026-07-16 | neuroscience | DOI: 10.64898/2026.07.14.732589
- 中文摘要: 自 1959 年发现视觉皮层的方向选择性以来，它已被广泛研究。在本文中，我们证明了当前对视觉皮层方向选择性的机械解释似乎在简化模型中起作用，但当嵌入到更现实的网络中时，它就不够了。到目前为止，方向选择性仅在具有距离依赖连接和有限细胞多样性的模型中重现。因此，我们构建了一个小鼠初级视觉皮层模型，除其他改进外，还具有现实的神经元多样性和形态学上受限的连接性。我们在该模型中实现了所提出的方向选择性机制，特别是将丘脑皮层输入组织到椭圆形子域中，以及具有相似感受野的神经元之间的互助连接。
- Abstract: Orientation selectivity in the visual cortex has been extensively studied since it was disovered in 1959. In this article we demonstrate that current mechanistic explanations of orientation selectivity in the visual cortex, which appear to work in simplified models, do not suffice when embedded in a more realistic network. Up to now, orientation selectivity has only been reproduced in models with distance-dependent...
- Summary (fallback): 机器翻译摘要显示：自 1959 年发现视觉皮层的方向选择性以来，它已被广泛研究。在本文中，我们证明了当前对视觉皮层方向选择性的机械解释似乎在简化模型中起作用，但当嵌入到更现实的网络中时，它就不够了。到目前为止，方向选择性仅在具有距离依赖连接和有限细胞多样性的模型中重现。因此，我们构建了一个小鼠初级视觉皮层模型，除其他改进外，还具有现实的神经元多样性和形态学上受限的连接性。我们在该模型中实现了所提出的方向选择性机制，特别是将丘脑皮层输入组织到椭圆形子域中，以及具有相似感受野的神经元之间的互助连接。
- Keywords: orientation, selectivity, connectivity, cortex, realistic

### 25. [RiboCollSensor：基于 split-NanoLuc 互补的哺乳动物细胞中核糖体碰撞的灵敏实时检测器](https://www.biorxiv.org/content/10.64898/2026.07.15.738639v1)
- Original title: RiboCollSensor: a sensitive real-time detector of ribosome collisions in mammalian cells based on split-NanoLuc complementation
- Authors: Alcalde, J., Ventoso, I.
- Meta: 2026-07-16 | molecular biology | DOI: 10.64898/2026.07.15.738639
- 中文摘要: 翻译 mRNA 时核糖体通量的破坏可能会导致核糖体碰撞，从而激活关键的细胞反应。尽管人们对该领域的兴趣日益浓厚，但目前检测核糖体碰撞的方法灵敏度有限，并且不适合在活细胞中使用。在这里，我们描述了一种基于分裂纳米荧光素酶互补的新颖、可靠且高度灵敏的方法，用于检测活细胞中的核糖体碰撞。 RiboCollSensor 依赖于 EDF1-LgBiT 特异性招募到 uS4-SmBiT 附近的碰撞核糖体，由于核糖体中伙伴的接近而产生发光。该生物传感器表现出前所未有的灵敏度，可以检测无应激细胞或极低应激水平下的基础核糖体碰撞，从而实现碰撞动力学的实时分析。
- Abstract: Disruption of ribosome flux on translating mRNAs can result in ribosome collisions that activate key cellular responses. Despite growing interest in the field, current methods to detect ribosome collisions have limited sensitivity and are not suitable for use in living cells. Here, we describe a novel, reliable, and highly sensitive method based on split-nanoluciferase complementation to detect ribosome collisions i...
- Summary (fallback): 机器翻译摘要显示：翻译 mRNA 时核糖体通量的破坏可能会导致核糖体碰撞，从而激活关键的细胞反应。尽管人们对该领域的兴趣日益浓厚，但目前检测核糖体碰撞的方法灵敏度有限，并且不适合在活细胞中使用。在这里，我们描述了一种基于分裂纳米荧光素酶互补的新颖、可靠且高度灵敏的方法，用于检测活细胞中的核糖体碰撞。 RiboCollSensor 依赖于 EDF1-LgBiT 特异性招募到 uS4-SmBiT 附近的碰撞核糖体，由于核糖体中伙伴的接近而产生发光。该生物传感器表现出前所未有的灵敏度，可以检测无应激细胞或极低应激水平下的基础核糖体碰撞，从而实现碰撞动力学的实时分析。
- Keywords: ribosome, collisions, cells, stress, cell

### 26. [通过量子退火优化的自旋玻璃代谢哈密顿量揭示了癌症代谢的热力学阶段](https://www.biorxiv.org/content/10.64898/2026.04.05.715441v2)
- Original title: A Spin-Glass Metabolic Hamiltonian optimized by Quantum Annealing Reveals Thermodynamic Phases of Cancer Metabolism
- Authors: Sung, J.-Y., Baek, K., Park, I., Bang, J., Cheong, J.-H.
- Meta: 2026-07-16 | biophysics | DOI: 10.64898/2026.04.05.715441
- 中文摘要: 了解为什么特定代谢状态在癌症中变得稳定仍然是一个基本挑战，因为当前以通路为中心的框架缺乏管理全球代谢组织的统一物理原理。我们引入了代谢自旋玻璃 (MSG) 模型，该模型使用热力学信息有效哈密顿量来表示细胞代谢，该哈密顿量在受挫的多体优化框架内集成了参考反应自由能、辅因子介导的网络耦合和患者特异性转录组场。哈密​​顿量被表述为二元优化问题，并使用混合量子退火来解决。嵌入胃癌转录组（n = 497）表明，恶性表型在有效代谢景观中占据独特的低能量配置，而不是代表孤立的途径扰动。
- Abstract: Understanding why specific metabolic states become stable in cancer has remained a fundamental challenge, as current pathway-centric frameworks lack a unifying physical principle governing global metabolic organization. We introduce the Metabolic Spin-Glass (MSG) model, which represents cellular metabolism using a thermodynamically informed effective Hamiltonian that integrates reference reaction free energies, cofa...
- Summary (fallback): 机器翻译摘要显示：了解为什么特定代谢状态在癌症中变得稳定仍然是一个基本挑战，因为当前以通路为中心的框架缺乏管理全球代谢组织的统一物理原理。我们引入了代谢自旋玻璃 (MSG) 模型，该模型使用热力学信息有效哈密顿量来表示细胞代谢，该哈密顿量在受挫的多体优化框架内集成了参考反应自由能、辅因子介导的网络耦合和患者特异性转录组场。哈密​​顿量被表述为二元优化问题，并使用混合量子退火来解决。嵌入胃癌转录组（n = 497）表明，恶性表型在有效代谢景观中占据独特的低能量配置，而不是代表孤立的途径扰动。
- Keywords: metabolic, cancer, spin-glass, hamiltonian, quantum

### 27. [皮质神经场方向调整动力学的对称性和非线性读出标准](https://www.biorxiv.org/content/10.64898/2025.12.29.696812v3)
- Original title: Symmetry and nonlinear-readout criteria for orientation-tuning dynamics in a cortical neural field
- Authors: Fukushima, M.
- Meta: 2026-07-16 | neuroscience | DOI: 10.64898/2025.12.29.696812
- 中文摘要: 在初级视觉皮层（V1）的循环和反馈调制的研究中，增益变化和调谐形状变化很难分开。我们在具有快速各向同性和较慢各向异性循环分量的平移不变神经场模型中分析了这种区别。在固定的空间和时间频率下，任何旋转对称循环核都会将线性响应乘以与角度无关的复增益，因此保留了归一化方向轮廓的每个度量。弱各向异性打破了这种一阶标量增益对称性，产生延迟锐化和由相量和关系描述的优选方向漂移。然后我们对非线性读数进行分类。
- Abstract: Gain changes and tuning-shape changes are difficult to separate in studies of recurrent and feedback modulation in primary visual cortex (V1). We analyze this distinction in a translation-invariant neural-field model with fast isotropic and slower anisotropic recurrent components. At fixed spatial and temporal frequency, any rotationally symmetric recurrent kernel multiplies the linear response by an angle-independe...
- Summary (fallback): 机器翻译摘要显示：在初级视觉皮层（V1）的循环和反馈调制的研究中，增益变化和调谐形状变化很难分开。我们在具有快速各向同性和较慢各向异性循环分量的平移不变神经场模型中分析了这种区别。在固定的空间和时间频率下，任何旋转对称循环核都会将线性响应乘以与角度无关的复增益，因此保留了归一化方向轮廓的每个度量。弱各向异性打破了这种一阶标量增益对称性，产生延迟锐化和由相量和关系描述的优选方向漂移。然后我们对非线性读数进行分类。
- Keywords: gain, changes, recurrent, symmetry, feedback

### 28. [种子应用的多界合成群落选择性地重塑细菌群落并突出菌株选择的关键标准](https://www.biorxiv.org/content/10.64898/2026.07.15.738658v1)
- Original title: Seed-applied multi-kingdom synthetic communities selectively reshape bacterial communities and highlight key criteria for strain selection
- Authors: Suteau, L., Campion, C., MARAIS, C., Briand, M., Hardouin, A. et al.
- Meta: 2026-07-16 | microbiology | DOI: 10.64898/2026.07.15.738658
- 中文摘要: 确定的微生物群落（也称为合成群落）在植物健康方面显示出有希望的结果，但缺乏有效的实验室到田间的过渡。这是由于关于如何通过考虑复杂环境和多界相互作用来有效调节植物微生物群的知识有限。在这项研究中，我们旨在更好地了解多界合成群落（SynComs）从种子到幼苗阶段的传播和影响。我们使用先验和随机方法从包括 24 种细菌、11 种酵母和 10 种丝状真菌在内的不同菌株库中构建了 20 种不同的 SynCom。 SynComs 接种在甘蓝型油菜种子上，我们监测了传播情况以及对在非无菌土壤中生长的 15 天幼苗微生物群的影响。
- Abstract: Defined microbial communities (also known as synthetic communities) are showing promising results for plant health but are lacking an efficient lab to field transition. This is the due to limited knowledge on how to efficiently modulate plant microbiota by considering complex environments and multi-kingdom interactions. In this study, we aimed to better understand the transmission and impact of multi-kingdom synthet...
- Summary (fallback): 机器翻译摘要显示：确定的微生物群落（也称为合成群落）在植物健康方面显示出有希望的结果，但缺乏有效的实验室到田间的过渡。这是由于关于如何通过考虑复杂环境和多界相互作用来有效调节植物微生物群的知识有限。在这项研究中，我们旨在更好地了解多界合成群落（SynComs）从种子到幼苗阶段的传播和影响。我们使用先验和随机方法从包括 24 种细菌、11 种酵母和 10 种丝状真菌在内的不同菌株库中构建了 20 种不同的 SynCom。 SynComs 接种在甘蓝型油菜种子上，我们监测了传播情况以及对在非无菌土壤中生长的 15 天幼苗微生物群的影响。
- Keywords: syncoms, communities, bacterial, syncom, inoculation

### 29. [非同源激酶 VncS 对 RR06 的交叉磷酸化可激活肺炎链球菌中的粘附素 CbpA。](https://www.biorxiv.org/content/10.64898/2026.07.15.738638v1)
- Original title: Cross-phosphorylation of RR06 by the non-cognate kinase VncS activates the adhesin CbpA in Streptococcus pneumoniae.
- Authors: Tan, S.-Y., Zik, J. J., Chun, Y.-Y., Tan, K. S., Sham, L.-T.
- Meta: 2026-07-16 | microbiology | DOI: 10.64898/2026.07.15.738638
- 中文摘要: 肺炎链球菌在发展为侵袭性疾病之前会在鼻咽部建立无症状定植，这一过程需要对表面粘附素进行精确的时空调节。使用条形码胶囊开关突变体库和随机条形码转座子测序 (RB-TnSeq)，我们确定了肺炎球菌粘附到人肺泡上皮细胞系 A549 的决定因素。该胶囊掩盖了表面粘附素并减少了所有 84 种测试血清型的结合。转座子筛选显示，vncS（双组分系统 TCS10 的传感器激酶）的过度表达显着增加了粘附，而其同源反应调节剂 VncR 的破坏则没有可检测到的效果。转录组分析和遗传上位性证实，已知受 TCS06 调节的粘附素 CbpA 是 VncS 驱动粘附的效应器。
- Abstract: Streptococcus pneumoniae establishes asymptomatic nasopharyngeal colonization before progressing to invasive disease, a process that requires precise spatiotemporal regulation of surface adhesins. Using a barcoded capsule-switch mutant library and randomly barcoded transposon sequencing (RB-TnSeq), we identified determinants of pneumococcal adhesion to the human alveolar epithelial cell line A549. The capsule masked...
- Summary (fallback): 机器翻译摘要显示：肺炎链球菌在发展为侵袭性疾病之前会在鼻咽部建立无症状定植，这一过程需要对表面粘附素进行精确的时空调节。使用条形码胶囊开关突变体库和随机条形码转座子测序 (RB-TnSeq)，我们确定了肺炎球菌粘附到人肺泡上皮细胞系 A549 的决定因素。该胶囊掩盖了表面粘附素并减少了所有 84 种测试血清型的结合。转座子筛选显示，vncS（双组分系统 TCS10 的传感器激酶）的过度表达显着增加了粘附，而其同源反应调节剂 VncR 的破坏则没有可检测到的效果。转录组分析和遗传上位性证实，已知受 TCS06 调节的粘附素 CbpA 是 VncS 驱动粘附的效应器。
- Keywords: rr06, vncs, cbpa, adhesion, kinase

### 30. [波多黎各昆虫特异性病毒组的微空间分区和埃及伊蚊传播登革热病毒的风险](https://www.biorxiv.org/content/10.64898/2026.07.15.738651v1)
- Original title: Microspatial partitioning of insect-specific viromes and dengue virus transmission risk by Aedes aegypti in Puerto Rico
- Authors: Agbodzi, B., Alonso-Palomares, L., Barton, H. J., Nazario-Maldonado, N., Quintana, J. M. et al.
- Meta: 2026-07-16 | microbiology | DOI: 10.64898/2026.07.15.738651
- 中文摘要: 蚊媒病毒仍然是全球主要的健康威胁。尽管昆虫特异性病毒（ISV）可能影响跨地理区域的虫媒病毒传播，但其在微空间尺度上埃及伊蚊种群内的多样性仍然知之甚少。我们假设当地环境变化塑造了埃及伊蚊核心病毒组，从而在波多黎各的农村和城市人群中产生了不同的 ISV 特征。 F0 蚊子的宏转录组 RNA 测序鉴定出 13 种具有栖息地特异性病毒组组成的 ISV。 Partitiviridae 是主要的病毒家族，而 Humaita-Tubiacanga 病毒 (HTV) 和 Phasi Charoen 样 phasivirus (PCLV) 在城市实验室群体中表现出最高的丰度、持久性和流行率。城市A.
- Abstract: Mosquito-borne arboviruses remain a major global health threat. Although insect-specific viruses (ISVs) may influence arbovirus transmission across geographic regions, their diversity within Aedes aegypti populations at microspatial scales remains poorly understood. We hypothesized that local environmental variation shapes the A. aegypti core virome, producing distinct ISV profiles in rural and urban populations in...
- Summary (fallback): 机器翻译摘要显示：蚊媒病毒仍然是全球主要的健康威胁。尽管昆虫特异性病毒（ISV）可能影响跨地理区域的虫媒病毒传播，但其在微空间尺度上埃及伊蚊种群内的多样性仍然知之甚少。我们假设当地环境变化塑造了埃及伊蚊核心病毒组，从而在波多黎各的农村和城市人群中产生了不同的 ISV 特征。 F0 蚊子的宏转录组 RNA 测序鉴定出 13 种具有栖息地特异性病毒组组成的 ISV。 Partitiviridae 是主要的病毒家族，而 Humaita-Tubiacanga 病毒 (HTV) 和 Phasi Charoen 样 phasivirus (PCLV) 在城市实验室群体中表现出最高的丰度、持久性和流行率。城市A.
- Keywords: aegypti, microspatial, transmission, populations, virome

## medrxiv

### 1. [2020-2025 年加纳蛇咬伤的时空模式：全国监测分析](https://www.medrxiv.org/content/10.64898/2026.07.12.26357875v1)
- Original title: Temporal and Spatial Patterns of Snakebite Envenoming in Ghana, 2020-2025: A Nationwide Surveillance Analysis
- Authors: Nyarko, E., Antwi, P., Amponsah, E. B., Ofori-Boadu, L., Oduro-Mensah, E. et al.
- Meta: 2026-07-16 | epidemiology | DOI: 10.64898/2026.07.12.26357875
- 中文摘要: 蛇咬伤是一种被忽视的主要热带疾病，对撒哈拉以南非洲的农村人口影响尤为严重。在加纳，有关风险时空分布的证据仍然有限，限制了有针对性的预防和资源分配。这项研究量化了加纳各地区的蛇咬伤风险，确定了持续存在的热点和环境驱动因素，并评估了蛇咬伤负担与获得治疗的地理机会之间的关系。使用贝叶斯时空模型分析了加纳地区卫生信息管理系统（2020 年至 2025 年）的每月地区级蛇咬伤病例，该模型结合了空间效应、时间随机效应和时空相互作用，并通过集成嵌套拉普拉斯逼近进行拟合。
- Abstract: Snakebite envenoming is a major neglected tropical disease disproportionately affecting rural populations in sub-Saharan Africa. In Ghana, evidence on the spatial and temporal distribution of risk remains limited, constraining targeted prevention and resource allocation. This study quantified district-level snakebite risk across Ghana, identified persistent hotspots and environmental drivers, and evaluated the relat...
- Summary (fallback): 机器翻译摘要显示：蛇咬伤是一种被忽视的主要热带疾病，对撒哈拉以南非洲的农村人口影响尤为严重。在加纳，有关风险时空分布的证据仍然有限，限制了有针对性的预防和资源分配。这项研究量化了加纳各地区的蛇咬伤风险，确定了持续存在的热点和环境驱动因素，并评估了蛇咬伤负担与获得治疗的地理机会之间的关系。使用贝叶斯时空模型分析了加纳地区卫生信息管理系统（2020 年至 2025 年）的每月地区级蛇咬伤病例，该模型结合了空间效应、时间随机效应和时空相互作用，并通过集成嵌套拉普拉斯逼近进行拟合。
- Keywords: risk, snakebite, temporal, spatial, east
