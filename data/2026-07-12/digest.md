# daily2rxiv Digest - 2026-07-12

共收录 46 篇论文。

## arxiv

### 1. [想法有基因组：对科学谱系推理和基于谱系的想法生成进行基准测试](https://arxiv.org/abs/2607.08758v1)
- Original title: Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation
- Authors: Yifan Zhou, Qihao Yang, Yan Li, Donggang Li, Xiru Hu et al.
- Meta: 2026-07-09 | cs.AI
- 中文摘要: 科学思想很少是从白纸开始的。它们继承机制，修复已知的局限性，并重组早期工作的片段，就像生物基因组一样。目前的基准测试仍然很少谈到人工智能系统是否可以遵循这种继承结构。我们推出 IdeaGene-Bench (IG-Bench)，这是科学谱系推理和基于谱系的想法生成的基准。 IG-Bench 围绕 IdeaGene 框架进行组织：每篇论文或提案都表示为一组最小的、有类型的、有证据的 Idea Genome 对象，GenomeDiff 对齐这些对象以记录六种操作进化动态下的继承、突变、丢失、外部导入和新颖插入。该基准包含 1,961 个黄金谱系痕迹、1,085 个精心策划的 Idea Genome 对象以及 10 个科学领域的 920 个成对 GenomeDiff 记录。它支持两种评估。
- Abstract: Scientific ideas rarely start from a blank page. They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes. Current benchmarks still say little about whether AI systems can follow this inheritance structure. We present IdeaGene-Bench (IG-Bench), a benchmark for scientific lineage reasoning and lineage-grounded idea generation. IG-Bench is organized around t...
- Summary (fallback): 机器翻译摘要显示：科学思想很少是从白纸开始的。它们继承机制，修复已知的局限性，并重组早期工作的片段，就像生物基因组一样。目前的基准测试仍然很少谈到人工智能系统是否可以遵循这种继承结构。我们推出 IdeaGene-Bench (IG-Bench)，这是科学谱系推理和基于谱系的想法生成的基准。 IG-Bench 围绕 IdeaGene 框架进行组织：每篇论文或提案都表示为一组最小的、有类型的、有证据的 Idea Genome 对象，GenomeDiff 对齐这些对象以记录六种操作进化动态下的继承、突变、丢失、外部导入和新颖插入。该基准包含 1,961 个黄金谱系痕迹、1,085 个精心策划的 Idea Genome 对象以及 10 个科学领域的 920 个成对 GenomeDiff 记录。它支持两种评估。
- Keywords: lineage, idea, reasoning, scientific, genome

### 2. [沿前向扩散的评分精度并不能证明扩散采样中的数值稳定性](https://arxiv.org/abs/2607.08757v1)
- Original title: Score Accuracy Along the Forward Diffusion Does Not Certify Numerical Stability in Diffusion Sampling
- Authors: Yiwei Zhou
- Meta: 2026-07-09 | stat.ML
- 中文摘要: 分数匹配控制前向边缘下的平均误差，但离散逆时采样器沿着其自己的轨迹评估学习的分数。我们表明，小的前向边缘误差并不能保证数值稳定性。我们构造一个具有任意小的前向边际 $L^2$ 误差的单个平滑得分场。学习到的逆时过程是非爆炸性的，具有每个阶的矩，并且可以任意接近路径空间总变分中的精确逆时过程。然而，它的欧拉-丸山离散化在概率上收敛，而每个正矩都发散。因此，即使每个 Wasserstein 距离 $W_p$、$p\ge1$ 发散，弱收敛也可以保持。同样的故障也可能发生在一种固定的有限神经架构中。
- Abstract: Score matching controls average error under the forward marginals, but a discretized reverse-time sampler evaluates the learned score along its own trajectory. We show that small forward-marginal error does not guarantee numerical stability. We construct a single smooth score field with arbitrarily small forward-marginal $L^2$ error. The learned reverse-time process is nonexplosive, has moments of every order, and c...
- Summary (fallback): 机器翻译摘要显示：分数匹配控制前向边缘下的平均误差，但离散逆时采样器沿着其自己的轨迹评估学习的分数。我们表明，小的前向边缘误差并不能保证数值稳定性。我们构造一个具有任意小的前向边际 $L^2$ 误差的单个平滑得分场。学习到的逆时过程是非爆炸性的，具有每个阶的矩，并且可以任意接近路径空间总变分中的精确逆时过程。然而，它的欧拉-丸山离散化在概率上收敛，而每个正矩都发散。因此，即使每个 Wasserstein 距离 $W_p$、$p\ge1$ 发散，弱收敛也可以保持。同样的故障也可能发生在一种固定的有限神经架构中。
- Keywords: score, error, small, every, along

### 3. [MulTTiPop：流行音乐的多轨转录数据集](https://arxiv.org/abs/2607.08756v1)
- Original title: MulTTiPop: A Multitrack Transcription Dataset for Pop Music
- Authors: Nathan Pruyne, Benjamin Stoler, William Chen, Chien-yu Huang, Shinji Watanabe et al.
- Meta: 2026-07-09 | cs.SD
- 中文摘要: 我们提出了 MulTTiPop，这是一个流行音乐片段及其相关多轨 MIDI 录音的数据集，用于评估自动音乐转录模型。 MulTTiPop 包含 572 个流行音乐片段，总计 3.5 小时的音频，并且包含来自 1930 年代到 2000 年代不同流派和几十年的歌曲。为了收集此数据集，我们对来自 Lakh MIDI 和 TheoryTab 数据集的歌曲片段执行基于元数据的匹配，手动识别音频和 MIDI 之间的锚点节拍，然后对音频使用节拍跟踪并扭曲 MIDI 以匹配其节奏和时间。我们在 MulTTiPop 上评估最先进的自动音乐转录模型，发现很大的改进空间，最好的模型实现了 38% 的 Onset F1。有关 MulTTiPop 的更多详细信息和声音示例，请访问 https://gclef-cmu.org/multtipop。
- Abstract: We present MulTTiPop, a dataset of pop music segments and their associated multitrack MIDI recordings for the evaluation of automatic music transcription models. MulTTiPop contains 572 segments of popular music totaling 3.5 hours of audio, and contains songs from diverse genres and decades from the 1930s to 2000s. To collect this dataset, we perform metadata-based matching on song segments from the Lakh MIDI and The...
- Summary (fallback): 机器翻译摘要显示：我们提出了 MulTTiPop，这是一个流行音乐片段及其相关多轨 MIDI 录音的数据集，用于评估自动音乐转录模型。 MulTTiPop 包含 572 个流行音乐片段，总计 3.5 小时的音频，并且包含来自 1930 年代到 2000 年代不同流派和几十年的歌曲。为了收集此数据集，我们对来自 Lakh MIDI 和 TheoryTab 数据集的歌曲片段执行基于元数据的匹配，手动识别音频和 MIDI 之间的锚点节拍，然后对音频使用节拍跟踪并扭曲 MIDI 以匹配其节奏和时间。我们在 MulTTiPop 上评估最先进的自动音乐转录模型，发现很大的改进空间，最好的模型实现了 38% 的 Onset F1。有关 MulTTiPop 的更多详细信息和声音示例，请访问 https://gclef-cmu.org/mult...
- Keywords: multtipop, music, midi, transcription, dataset

### 4. [SLORR：简单高效的训练中低阶正则化](https://arxiv.org/abs/2607.08754v1)
- Original title: SLORR: Simple and Efficient In-Training Low-Rank Regularization
- Authors: David González-Martínez, Shiwei Liu
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 低秩分解广泛用于压缩神经网络，但现代模型通常不能自然地适应激进的分解而不造成显着的准确性损失。现有的训练时低秩正则化器可以提高可压缩性，但它们通常需要大型权重矩阵的 SVD、修改模型架构（引入额外的可训练参数）或依赖有状态的缓存量。为了解决这些限制，我们引入了 SLORR，这是一种简单、无状态且保留架构的框架，用于训练中的低秩正则化，并使用基于 Hoyer 稀疏度度量和核范数的两个主要变体进行实例化。 SLORR 使用 GPU 友好的近似值直接正则化原始权重矩阵，用于正则化器的前向和后向传递，为此我们提供近似保证。
- Abstract: Low-rank factorization is widely used to compress neural networks, but modern models are often not naturally amenable to aggressive factorization without significant accuracy loss. Existing training-time low-rank regularizers can improve compressibility, but they often require SVDs of large weight matrices, modify the model architecture (introducing additional trainable parameters), or rely on stateful cached quanti...
- Summary (fallback): 机器翻译摘要显示：低秩分解广泛用于压缩神经网络，但现代模型通常不能自然地适应激进的分解而不造成显着的准确性损失。现有的训练时低秩正则化器可以提高可压缩性，但它们通常需要大型权重矩阵的 SVD、修改模型架构（引入额外的可训练参数）或依赖有状态的缓存量。为了解决这些限制，我们引入了 SLORR，这是一种简单、无状态且保留架构的框架，用于训练中的低秩正则化，并使用基于 Hoyer 稀疏度度量和核范数的两个主要变体进行实例化。 SLORR 使用 GPU 友好的近似值直接正则化原始权重矩阵，用于正则化器的前向和后向传递，为此我们提供近似保证。
- Keywords: slorr, low-rank, models, training, simple

### 5. [降维与网络科学相遇：UMAP 的 kNN 图上的意义建构](https://arxiv.org/abs/2607.08746v1)
- Original title: Dimensionality Reduction Meets Network Science: Sensemaking on UMAP's kNN Graph
- Authors: Duen Horng Chau, Donghao Ren, Fred Hohman, Dominik Moritz
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 虽然 UMAP 广泛用于探索高维数据，但典型的工作流程侧重于其低维嵌入，很大程度上忽略了 UMAP 内部构造的丰富的 k 最近邻 (kNN) 图。在 UMAP 的 2D 投影引入失真之前，该图将数据流形编码在其原始高维空间中。我们展示了这种内部表示的未开发潜力，展示了应用于该图的标准图算法如何增强数据意义：(1) PageRank 识别代​​表性数据点，(2) k 核心分解揭示密集的核心区域与稀疏的外围区域，(3) 聚类系数检测具有高度相似数据点的紧密邻域。
- Abstract: While UMAP is widely used for exploring high-dimensional data, typical workflows focus on its lower-dimensional embedding, largely overlooking the rich k-nearest-neighbor (kNN) graph that UMAP constructs internally. This graph encodes the data manifold in its original high-dimensional space, before the distortion that UMAP's 2D projection introduces. We demonstrate the untapped potential of this internal representat...
- Summary (fallback): 机器翻译摘要显示：虽然 UMAP 广泛用于探索高维数据，但典型的工作流程侧重于其低维嵌入，很大程度上忽略了 UMAP 内部构造的丰富的 k 最近邻 (kNN) 图。在 UMAP 的 2D 投影引入失真之前，该图将数据流形编码在其原始高维空间中。我们展示了这种内部表示的未开发潜力，展示了应用于该图的标准图算法如何增强数据意义：(1) PageRank 识别代​​表性数据点，(2) k 核心分解揭示密集的核心区域与稀疏的外围区域，(3) 聚类系数检测具有高度相似数据点的紧密邻域。
- Keywords: graph, umap, sensemaking, high-dimensional, points

### 6. [ARDY：用于交互式人体运动生成的自回归扩散与混合表示](https://arxiv.org/abs/2607.08741v1)
- Original title: ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation
- Authors: Kaifeng Zhao, Mathis Petrovich, Haotian Zhang, Tingwu Wang, Siyu Tang et al.
- Meta: 2026-07-09 | cs.GR | DOI: 10.1145/3811284
- 中文摘要: 在交互式应用程序中实时生成逼真的 3D 人体动作是动画、模拟和人形机器人技术的关键。虽然最近的离线运动生成方法通过文本和运动学约束提供了精确控制，但它们缺乏交互设置所需的推理速度。相反，现有的在线方法可以实现实时合成，但由于上下文窗口有限，往往会牺牲可控性或难以应对复杂的文本语义和长期目标。在这项工作中，我们介绍了 ARDY，这是一种流式生成框架，它通过在线文本提示和灵活的运动学约束实现可控制的高保真运动生成，从而弥补了这一差距。 ARDY 采用混合表示，将显式根特征与潜在身体嵌入相结合，平衡精确的轨迹控制与高效的生成学习。
- Abstract: Generating realistic 3D human motions in real-time within interactive applications is key for animation, simulation, and humanoid robotics. While recent offline motion generation approaches offer precise control via text and kinematic constraints, they lack the inference speed required for interactive settings. Conversely, existing online methods enable real-time synthesis but often sacrifice controllability or stru...
- Summary (fallback): 机器翻译摘要显示：在交互式应用程序中实时生成逼真的 3D 人体动作是动画、模拟和人形机器人技术的关键。虽然最近的离线运动生成方法通过文本和运动学约束提供了精确控制，但它们缺乏交互设置所需的推理速度。相反，现有的在线方法可以实现实时合成，但由于上下文窗口有限，往往会牺牲可控性或难以应对复杂的文本语义和长期目标。在这项工作中，我们介绍了 ARDY，这是一种流式生成框架，它通过在线文本提示和灵活的运动学约束实现可控制的高保真运动生成，从而弥补了这一差距。 ARDY 采用混合表示，将显式根特征与潜在身体嵌入相结合，平衡精确的轨迹控制与高效的生成学习。
- Keywords: ardy, interactive, motion, generation, text

### 7. [法学硕士的超级权重和选择性培训的失败](https://arxiv.org/abs/2607.08733v1)
- Original title: Super Weights in LLMs and the Failure of Selective Training
- Authors: Shreyas Subramanian, Adewale Akinfaderin, Akarsha Sehwag
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 最近的工作确定了超级权重，即单个参数，删除这些参数会使模型性能降低几个数量级。我们表明，由于修剪超级权重而导致的这种退化并不普遍适用于所有法学硕士。此外，如果这些参数如此重要，超级重量意识训练应该是有效的。我们展示相反的情况。单独训练超级权重（100 到 8,192 个参数）会将 OLMo-1B 和 OLMo-7B 上的准确性降低到随机猜测水平，并且扩展到最多 36K 参数的局部邻域并没有提供任何改进。该失败特定于超级权重坐标：在相同的 down_proj 层中训练相同数量的随机选择的位置，而不是在基线上进行改进，因此崩溃来自于针对超级权重，而不是稀疏性本身。
- Abstract: Recent work identified Super Weights, individual parameters whose removal degrades model performance by orders of magnitude. We show that this degradation due to pruning Super Weights does not universally apply to all LLMs. Furthermore, if these parameters are so important, Super Weight-aware training should be effective. We show the opposite. Training Super Weights in isolation (100 to 8,192 parameters) drops accur...
- Summary (fallback): 机器翻译摘要显示：最近的工作确定了超级权重，即单个参数，删除这些参数会使模型性能降低几个数量级。我们表明，由于修剪超级权重而导致的这种退化并不普遍适用于所有法学硕士。此外，如果这些参数如此重要，超级重量意识训练应该是有效的。我们展示相反的情况。单独训练超级权重（100 到 8,192 个参数）会将 OLMo-1B 和 OLMo-7B 上的准确性降低到随机猜测水平，并且扩展到最多 36K 参数的局部邻域并没有提供任何改进。该失败特定于超级权重坐标：在相同的 down_proj 层中训练相同数量的随机选择的位置，而不是在基线上进行改进，因此崩溃来自于针对超级权重，而不是稀疏性本身。
- Keywords: super, weights, parameters, training, weight

### 8. [姿势到生物力学：桥接 3D 人体姿势估计和生物力学属性预测](https://arxiv.org/abs/2607.08725v1)
- Original title: Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction
- Authors: Ayda Eghbalian, Kevin Desai
- Meta: 2026-07-09 | cs.CV
- 中文摘要: 3D 人体姿势估计的最新进展使得骨骼运动的无标记恢复变得越来越准确和可扩展。然而，大多数姿势估计器仍然针对几何关键点精度进行了优化，而康复、运动科学、人体工程学和临床运动分析中的许多实际应用需要描述身体如何移动、加载和激活的生物力学量。在这项工作中，我们提出了 BioModule，这是一种轻量级插件时间转换器，可附加到任何 3D 姿态估计器的下游，并根据标准 17 关节 3D 骨架预测生物力学属性。 BioModule 与估计器无关，不需要修改上游姿态模型，使现有的姿态估计器能够扩展到物理上可解释的运动分析。
- Abstract: Recent progress in 3D human pose estimation has made markerless recovery of skeletal motion increasingly accurate and scalable. However, most pose estimators remain optimized for geometric keypoint accuracy, while many real-world applications in rehabilitation, sports science, ergonomics, and clinical movement analysis require biomechanical quantities that describe how the body moves, loads, and activates. In this w...
- Summary (fallback): 机器翻译摘要显示：3D 人体姿势估计的最新进展使得骨骼运动的无标记恢复变得越来越准确和可扩展。然而，大多数姿势估计器仍然针对几何关键点精度进行了优化，而康复、运动科学、人体工程学和临床运动分析中的许多实际应用需要描述身体如何移动、加载和激活的生物力学量。在这项工作中，我们提出了 BioModule，这是一种轻量级插件时间转换器，可附加到任何 3D 姿态估计器的下游，并根据标准 17 关节 3D 骨架预测生物力学属性。 BioModule 与估计器无关，不需要修改上游姿态模型，使现有的姿态估计器能够扩展到物理上可解释的运动分析。
- Keywords: pose, biomechanical, biomodule, estimation, analysis

### 9. [潜在记忆宫殿：作为自回归变分推理的控制推理](https://arxiv.org/abs/2607.08724v1)
- Original title: Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference
- Authors: Chuning Zhu, Eva Xu, Jose Barreiros, Krishnan Srinivasan, Paarth Shah et al.
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 人类的决策是高度灵活的——有些行动是立即采取的，有些是立即采取的。其他的则需要更长时间的深思熟虑。语言模型表现出了类似的自适应“推理”能力。然而，将这种能力转移到连续控制策略一直具有挑战性，因为语言空间中的直接推理可能缺乏空间理解和精确运动的粒度。在这项工作中，我们表明，通过在让人想起记忆宫殿的自回归潜在空间中组织信息，可以出现控制策略的推理，其中检索是迭代和自适应的。我们的方法，潜在记忆宫殿（LMP），将推理公式化为具有自回归潜在分布的变分推理。我们推导出一种潜在空间强化学习技术来轻松优化其变分下界。
- Abstract: Human decision-making is highly flexible -- some actions are taken immediately; others require longer deliberation. Language models have exhibited a similar capacity for adaptive "reasoning." However, transferring this capability to continuous control policies has been challenging, as directly reasoning in language space may lack the granularity for spatial understanding and precise motions. In this work, we show th...
- Summary (fallback): 机器翻译摘要显示：人类的决策是高度灵活的——有些行动是立即采取的，有些是立即采取的。其他的则需要更长时间的深思熟虑。语言模型表现出了类似的自适应“推理”能力。然而，将这种能力转移到连续控制策略一直具有挑战性，因为语言空间中的直接推理可能缺乏空间理解和精确运动的粒度。在这项工作中，我们表明，通过在让人想起记忆宫殿的自回归潜在空间中组织信息，可以出现控制策略的推理，其中检索是迭代和自适应的。我们的方法，潜在记忆宫殿（LMP），将推理公式化为具有自回归潜在分布的变分推理。我们推导出一种潜在空间强化学习技术来轻松优化其变分下界。
- Keywords: reasoning, latent, control, autoregressive, variational

### 10. [OFDM 系统中联合窄带干扰消除和软解调的深度学习](https://arxiv.org/abs/2607.08717v1)
- Original title: Deep Learning for Joint Narrowband Interference Cancellation and Soft Demodulation in OFDM Systems
- Authors: Emmanouil Kavvousanos, Francky Catthoor, Vassilis Paliouras
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 窄带干扰 (NBI) 会破坏子载波并使经典软解调无效，从而严重降低正交频分复用 (OFDM) 系统的性能。传统的压缩感知 (CS) 缓解措施表现出较高的顺序延迟，并留下结构化的非高斯残差，在采用经典高斯解映射器时，这些残差会导致对数似然比 (LLR) 不可靠性、解码器饱和和严重的错误平台。我们使用统一的深度学习框架来解决这种管道不匹配问题，以进行联合 NBI 消除和鲁棒的软解调。首先，NBI-CNet 采用基于物理的卷积架构来估计 NBI 参数并消除单次前向传播中的多音干扰。
- Abstract: Narrowband interference (NBI) severely degrades orthogonal frequency-division multiplexing (OFDM) systems by corrupting subcarriers and rendering classical soft demodulation ineffective. Conventional compressed-sensing (CS) mitigation exhibits high sequential latency and leaves structured, non-Gaussian residuals that cause log-likelihood ratio (LLR) unreliability, decoder saturation, and severe error floors when emp...
- Summary (fallback): 机器翻译摘要显示：窄带干扰 (NBI) 会破坏子载波并使经典软解调无效，从而严重降低正交频分复用 (OFDM) 系统的性能。传统的压缩感知 (CS) 缓解措施表现出较高的顺序延迟，并留下结构化的非高斯残差，在采用经典高斯解映射器时，这些残差会导致对数似然比 (LLR) 不可靠性、解码器饱和和严重的错误平台。我们使用统一的深度学习框架来解决这种管道不匹配问题，以进行联合 NBI 消除和鲁棒的软解调。首先，NBI-CNet 采用基于物理的卷积架构来估计 NBI 参数并消除单次前向传播中的多音干扰。
- Keywords: interference, soft, error, joint, demodulation

### 11. [哮喘多模态数字生物标志物：声音、临床和人口因素的互补作用](https://arxiv.org/abs/2607.08714v1)
- Original title: Multimodal Digital Biomarker for Asthma: Complementary Roles of Vocal, Clinical and Demographic Factors
- Authors: Vladimir Despotovic, Milena Despotovic, Abir Elbeji, Petr V. Nazarov, Guy Fagherazzi
- Meta: 2026-07-09 | eess.AS
- 中文摘要: 哮喘影响着全世界超过 2.6 亿人，但诊断仍然依赖于肺活量测定和专家评估，这限制了初级保健和资源匮乏环境中的可及性。声音生物标志物提供了一种有前景的非侵入性替代方案，但之前的研究主要集中在声学特征上，而没有整合临床背景。我们提出了一种用于哮喘检测的多模式专家混合框架，该框架自适应地将来自持续元音发声和阅读段落任务的声学嵌入与结构化的临床和人口统计数据相结合。该模型在 Colive Voice 研究中的 1,218 例哮喘病例和健康对照的匹配队列中进行了评估。多模态模型的 AUROC 为 0.85，Brier 评分为 0.17，优于单模态和双模态方法。
- Abstract: Asthma affects over 260 million people worldwide, yet diagnosis remains dependent on spirometry and specialist assessment, limiting accessibility in primary care and low-resource settings. Vocal biomarkers offer a promising non-invasive alternative, but prior studies have largely focused on acoustic features without integrating clinical context. We present a multimodal Mixture-of-Experts framework for asthma detecti...
- Summary (fallback): 机器翻译摘要显示：哮喘影响着全世界超过 2.6 亿人，但诊断仍然依赖于肺活量测定和专家评估，这限制了初级保健和资源匮乏环境中的可及性。声音生物标志物提供了一种有前景的非侵入性替代方案，但之前的研究主要集中在声学特征上，而没有整合临床背景。我们提出了一种用于哮喘检测的多模式专家混合框架，该框架自适应地将来自持续元音发声和阅读段落任务的声学嵌入与结构化的临床和人口统计数据相结合。该模型在 Colive Voice 研究中的 1,218 例哮喘病例和健康对照的匹配队列中进行了评估。多模态模型的 AUROC 为 0.85，Brier 评分为 0.17，优于单模态和双模态方法。
- Keywords: asthma, clinical, multimodal, features, vocal

### 12. [LTM：针对易发生野火景观的大型地形模型](https://arxiv.org/abs/2607.08711v1)
- Original title: LTM: Large-scale Terrain Model for Wildfire-prone Landscapes
- Authors: Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan
- Meta: 2026-07-09 | cs.CV
- 中文摘要: 在评估野火危害时，准确的 3D 地形图对于应急响应至关重要。然而，野火多发地区往往跨越广阔的地区，而传统的重建方法效果不佳。机载激光雷达系统提供高分辨率地形数据，但价格昂贵且不经常更新。基于图像的方法提供了一种成本较低的替代方案，但由于稀疏的视觉特征和有限的图像重叠而举步维艰。我们提出了一种多模态重建框架，利用过时的数字高程模型 (DEM) 作为基于图像的 3D 重建的几何先验。我们的关键创新是图像和 DEM 数据之间基于物理的像素对像素对齐，通过消除昂贵的特征匹配程序来显着降低计算复杂性。
- Abstract: Accurate 3D terrain maps are essential for emergency response when assessing wildfire hazards. However, wildfire-prone regions often span vast areas where conventional reconstruction methods underperform. Airborne LiDAR systems provide high-resolution terrain data, but they are expensive and infrequently updated. Image-based methods offer a lower-cost alternative, but struggle due to sparse visual features and limit...
- Summary (fallback): 机器翻译摘要显示：在评估野火危害时，准确的 3D 地形图对于应急响应至关重要。然而，野火多发地区往往跨越广阔的地区，而传统的重建方法效果不佳。机载激光雷达系统提供高分辨率地形数据，但价格昂贵且不经常更新。基于图像的方法提供了一种成本较低的替代方案，但由于稀疏的视觉特征和有限的图像重叠而举步维艰。我们提出了一种多模态重建框架，利用过时的数字高程模型 (DEM) 作为基于图像的 3D 重建的几何先验。我们的关键创新是图像和 DEM 数据之间基于物理的像素对像素对齐，通过消除昂贵的特征匹配程序来显着降低计算复杂性。
- Keywords: reconstruction, terrain, wildfire-prone, images, maps

### 13. [定向人工智能建议：来自医疗保健的实验证据](https://arxiv.org/abs/2607.08706v1)
- Original title: Directional AI Advice: Experimental Evidence from Healthcare
- Authors: Yuyu Chen, Hongbin Li, Lingsheng Meng, Xinyao Qiu, Qingxu Yang
- Meta: 2026-07-09 | econ.GN
- 中文摘要: 生成式人工智能正迅速成为人们寻求专家建议的第一个地方。它提供的建议可以是定向的而不是中立的，部分是由其设计者和监管者的选择决定的。当客户在会见专家之前咨询人工智能时，他们会将这种定向建议带入曾经仅依赖于专家判断的关系中。我们通过在中国一家医院进行的大规模预先注册现场实验来研究其对医疗保健的影响，我们在患者就诊之前随机分配人工智能聊天机器人的访问权限。对对话日志的检查显示，聊天机器人通常会警告不要使用药物，尤其是中药和抗生素，同时发布明确的诊断测试建议，这与人工智能培训中编码的责任驱动的护栏一致。
- Abstract: Generative AI is fast becoming the first place people turn for expert advice. The advice it provides can be directional rather than neutral, shaped in part by the choices of its designers and regulators. When clients consult AI before meeting an expert, they carry this directional advice into a relationship that once rested on the expert's judgment alone. We study its consequences in healthcare through a large-scale...
- Summary (fallback): 机器翻译摘要显示：生成式人工智能正迅速成为人们寻求专家建议的第一个地方。它提供的建议可以是定向的而不是中立的，部分是由其设计者和监管者的选择决定的。当客户在会见专家之前咨询人工智能时，他们会将这种定向建议带入曾经仅依赖于专家判断的关系中。我们通过在中国一家医院进行的大规模预先注册现场实验来研究其对医疗保健的影响，我们在患者就诊之前随机分配人工智能聊天机器人的访问权限。对对话日志的检查显示，聊天机器人通常会警告不要使用药物，尤其是中药和抗生素，同时发布明确的诊断测试建议，这与人工智能培训中编码的责任驱动的护栏一致。
- Keywords: advice, directional, healthcare, expert, patients

### 14. [MPFlow：通过深度图强化学习在闪电网络上学习预算最大流优化](https://arxiv.org/abs/2607.08703v1)
- Original title: MPFlow: Learning Budgeted Max-Flow Optimization on the Lightning Network with Deep Graph Reinforcement Learning
- Authors: Harrison Rush, Vincent Davis, Simone Antonelli, Vikash Singh, Jesse Shrader et al.
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 我们解决比特币闪电网络（LN）中的流动性配置问题：给定固定预算，节点应该打开哪些通道以最大化其路由能力？我们将其视为图上的预算约束组合优化问题，选择最大化 $s$--$t$ max-flow 的 $k$ 边添加，这是基于理论的路由容量度量，并通过图强化学习来解决它。我们的轻量级代理将消息传递策略网络与近端策略优化（PPO）和动作屏蔽相结合，并在集线器排除课程下进行训练：网络的顶级集线器从训练子图中删除，迫使策略学习容量感知的放置而不是集线器附件。
- Abstract: We address liquidity placement in the Bitcoin Lightning Network (LN): given a fixed budget, which channels should a node open to maximize its routing capacity? We cast this as a budget-constrained combinatorial optimization problem on graphs, selecting $k$ edge additions that maximize $s$--$t$ max-flow, a theory-grounded measure of routing capacity, and solve it with graph reinforcement learning. Our lightweight age...
- Summary (fallback): 机器翻译摘要显示：我们解决比特币闪电网络（LN）中的流动性配置问题：给定固定预算，节点应该打开哪些通道以最大化其路由能力？我们将其视为图上的预算约束组合优化问题，选择最大化 $s$--$t$ max-flow 的 $k$ 边添加，这是基于理论的路由容量度量，并通过图强化学习来解决它。我们的轻量级代理将消息传递策略网络与近端策略优化（PPO）和动作屏蔽相结合，并在集线器排除课程下进行训练：网络的顶级集线器从训练子图中删除，迫使策略学习容量感知的放置而不是集线器附件。
- Keywords: network, learning, max-flow, optimization, lightning

### 15. [免训练宽松推测解码的实际研究](https://arxiv.org/abs/2607.08690v1)
- Original title: A Practical Investigation of Training-free Relaxed Speculative Decoding
- Authors: Guoxuan Xia, Luka Ribar, Paul Balanca
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 推测性解码通过使用更快的辅助模型来起草令牌，然后由 LLM 并行验证，从而加速自回归 LLM 的采样。标准推测解码是无损的：它的拒绝和重采样步骤准确地保留了 LLM 的采样分布。最近的研究表明，放松这种严格的保证可以带来进一步的加速、受控的能力与速度权衡，甚至能力增益。我们实际上研究了免训练的宽松推测解码技术，将现有方法统一在一个共享框架内，在当代环境中进行基准测试，并为从业者提炼出要点和实证结果。
- Abstract: Speculative decoding accelerates sampling from an autoregressive LLM by using a faster auxiliary model to draft tokens which are then verified in parallel by the LLM. Standard speculative decoding is lossless: its rejection and resampling steps exactly preserve the LLM's sampling distribution. Recent work argues that relaxing this strict guarantee can yield further speed-ups, controlled capability-speed trade-offs,...
- Summary (fallback): 机器翻译摘要显示：推测性解码通过使用更快的辅助模型来起草令牌，然后由 LLM 并行验证，从而加速自回归 LLM 的采样。标准推测解码是无损的：它的拒绝和重采样步骤准确地保留了 LLM 的采样分布。最近的研究表明，放松这种严格的保证可以带来进一步的加速、受控的能力与速度权衡，甚至能力增益。我们实际上研究了免训练的宽松推测解码技术，将现有方法统一在一个共享框架内，在当代环境中进行基准测试，并为从业者提炼出要点和实证结果。
- Keywords: speculative, decoding, relaxed, training-free, sampling

### 16. [重新采样还是重新路由？大型语言模型的预算感知测试时间模型选择](https://arxiv.org/abs/2607.08665v1)
- Original title: Resample or Reroute? Budget-Aware Test-Time Model Selection for Large Language Models
- Authors: Teng-Ruei Chen
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 大型语言模型 (LLM) 之间的路由会根据服务成本来交换响应质量，其动机是报告的已部署路由器与每个实例预言机之间的差距。最近的分析表明，测试时重采样可以恢复单提交路由器无法捕获的每个实例选择余量；然而，这种保证仅在配备正确性标签和不受限制的预算的理想化预言机下成立，而部署的系统则不具备这两者。据我们所知，以前的工作没有将重新采样提交的模型和重新路由到替代模型视为单个每个查询成本预算的竞争使用。因此，这项工作制定了预算感知的测试时间模型选择：给定每个查询的预算和不完美的验证器，在重采样和重新路由之间分配每个预算单位，以便最大化预期的正确性。
- Abstract: Routing among large language models (LLMs) trades response quality against serving cost, motivated by the reported gap between deployed routers and a per-instance oracle. Recent analysis shows that test-time resampling can recover per-instance selection headroom that no single-commit router captures; however, that guarantee holds only under an idealized oracle equipped with correctness labels and an unconstrained bu...
- Summary (fallback): 机器翻译摘要显示：大型语言模型 (LLM) 之间的路由会根据服务成本来交换响应质量，其动机是报告的已部署路由器与每个实例预言机之间的差距。最近的分析表明，测试时重采样可以恢复单提交路由器无法捕获的每个实例选择余量；然而，这种保证仅在配备正确性标签和不受限制的预算的理想化预言机下成立，而部署的系统则不具备这两者。据我们所知，以前的工作没有将重新采样提交的模型和重新路由到替代模型视为单个每个查询成本预算的竞争使用。因此，这项工作制定了预算感知的测试时间模型选择：给定每个查询的预算和不完美的验证器，在重采样和重新路由之间分配每个预算单位，以便最大化预期的正确性。
- Keywords: model, selection, correctness, budget, budget-aware

### 17. [EdgeRefine：边缘差分隐私下通过 Jaccard 采样实现图的隐私-效用平衡](https://arxiv.org/abs/2607.08659v1)
- Original title: EdgeRefine: Privacy-Utility Balance for Graphs via Jaccard Sampling under Edge Differential Privacy
- Authors: Wenxiu Ding, Muzhi Liu, Zheng Yan, Mingjun Wang, Yifan Zhao et al.
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 图神经网络（GNN）在从图结构数据中学习方面取得了相当大的成功，但它们在隐私敏感领域的使用仍然很困难，因为图结构可能会泄漏敏感的链接信息。为了满足边级差分隐私，一种常见的方法是将噪声注入图的邻接矩阵的所有元素中，从而混淆任何单个边的存在。然而，更强的隐私需要更多的噪声，而过多的噪声会降低效用，使得隐私-效用平衡成为实际隐私保护图学习的主要障碍。为了解决这个问题，我们提出了 EdgeRefine，这是一种本地差分隐私框架，可以通过自适应边缘细化来改善这种权衡。 EdgeRefine 首先使用 Jaccard 相似度估计边缘存在概率，并对边缘进行排序以去除噪声边缘。
- Abstract: Graph Neural Networks (GNNs) have shown considerable success in learning from graph-structured data, but their use in privacy-sensitive areas remains difficult because graph structure can leak sensitive link information. To satisfy edge-level differential privacy, a common approach is to inject noise into all elements of the graph's adjacency matrix, thereby obfuscating the existence of any single edge. However, str...
- Summary (fallback): 机器翻译摘要显示：图神经网络（GNN）在从图结构数据中学习方面取得了相当大的成功，但它们在隐私敏感领域的使用仍然很困难，因为图结构可能会泄漏敏感的链接信息。为了满足边级差分隐私，一种常见的方法是将噪声注入图的邻接矩阵的所有元素中，从而混淆任何单个边的存在。然而，更强的隐私需要更多的噪声，而过多的噪声会降低效用，使得隐私-效用平衡成为实际隐私保护图学习的主要障碍。为了解决这个问题，我们提出了 EdgeRefine，这是一种本地差分隐私框架，可以通过自适应边缘细化来改善这种权衡。 EdgeRefine 首先使用 Jaccard 相似度估计边缘存在概率，并对边缘进行排序以去除噪声边缘。
- Keywords: privacy, graph, edgerefine, under, edge

### 18. [通过八卦和虚拟投票确保分散式联合学习的安全](https://arxiv.org/abs/2607.08651v1)
- Original title: Secure Decentralized Federated Learning via Gossip and Virtual Voting
- Authors: Amirhossein Taherpour, Xiaodong Wang
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 去中心化联合学习（DFL）通过让节点通过点对点八卦交换模型更新来消除中央服务器，但现有的基于八卦的方法通常缺乏来源最终性和对拜占庭或懒惰参与者的弹性。账本辅助的联邦学习 (FL) 提高了可审计性，但区块链、分片或结算委员会可能会重新引入与 DFL 局部性相冲突的全局协调成本。本文提出了 \emph{gspDAG-FL}，这是一种安全的 DFL 框架，它从用于传播模型的相同八卦历史中得出共识。节点仅与邻居交换模型负载，而全节点收集事件证书和接收者认可的接受的八卦证明，重建紧凑的拓扑有向无环图（DAG），并运行哈希图式的虚拟投票，然后运行紧凑的全节点证书。
- Abstract: Decentralized federated learning (DFL) removes the central server by letting nodes exchange model updates through peer-to-peer gossip, but existing gossip-based methods often lack provenance finality and resilience to Byzantine or lazy participants. Ledger-assisted federated learning (FL) improves auditability, yet blockchains, shards, or settlement committees can reintroduce global coordination costs that conflict...
- Summary (fallback): 机器翻译摘要显示：去中心化联合学习（DFL）通过让节点通过点对点八卦交换模型更新来消除中央服务器，但现有的基于八卦的方法通常缺乏来源最终性和对拜占庭或懒惰参与者的弹性。账本辅助的联邦学习 (FL) 提高了可审计性，但区块链、分片或结算委员会可能会重新引入与 DFL 局部性相冲突的全局协调成本。本文提出了 \emph{gspDAG-FL}，这是一种安全的 DFL 框架，它从用于传播模型的相同八卦历史中得出共识。节点仅与邻居交换模型负载，而全节点收集事件证书和接收者认可的接受的八卦证明，重建紧凑的拓扑有向无环图（DAG），并运行哈希图式的虚拟投票，然后运行紧凑的全节点证书。
- Keywords: gossip, learning, federated, nodes, gspdag-fl

### 19. [多模式、多环境机器教学，实现稳健的奖励学习](https://arxiv.org/abs/2607.08647v1)
- Original title: Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning
- Authors: Ali Larian, Qian Lin, Chang Zong Wu, Daniel S. Brown
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 随着自主代理越来越多地部署在不同的操作环境中，将其行为与人类意图保持一致需要奖励功能对此类变化保持鲁棒性，而不是过度适应任何单一环境。逆向强化学习（IRL）提供了一种从人类反馈中推断此类目标的原则性方法。然而，现有的 IRL 最佳教学方法分析侧重于单一环境、仅演示设置，而尚未充分探索异构反馈模式和环境动态如何共同约束跨多个环境的奖励函数。由于 MDP 中的演示将奖励信息与该环境的特定结构纠缠在一起，因此当代理部署在新环境中时，所得到的奖励常常无法泛化。
- Abstract: As autonomous agents are increasingly deployed across diverse operational contexts, aligning their behavior with human intent demands reward functions that remain robust to such changes rather than overfitting to any single environment. Inverse reinforcement learning (IRL) provides a principled way to infer such objectives from human feedback. However, existing analyses of optimal teaching approaches for IRL focus o...
- Summary (fallback): 机器翻译摘要显示：随着自主代理越来越多地部署在不同的操作环境中，将其行为与人类意图保持一致需要奖励功能对此类变化保持鲁棒性，而不是过度适应任何单一环境。逆向强化学习（IRL）提供了一种从人类反馈中推断此类目标的原则性方法。然而，现有的 IRL 最佳教学方法分析侧重于单一环境、仅演示设置，而尚未充分探索异构反馈模式和环境动态如何共同约束跨多个环境的奖励函数。由于 MDP 中的演示将奖励信息与该环境的特定结构纠缠在一起，因此当代理部署在新环境中时，所得到的奖励常常无法泛化。
- Keywords: reward, teaching, feedback, environments, learning

### 20. [BiSCo-LLM：用于极低位大型语言模型压缩的免查找二进制球形编码](https://arxiv.org/abs/2607.08643v1)
- Original title: BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Large Language Model Compression
- Authors: Yuantian Shao, Peisong Wang, Zhilei Liu, Chuangyi Li, Yuanteng Chen et al.
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 大型语言模型 (LLM) 在部署过程中越来越受到内存容量、权重带宽和检查点存储的限制。现有的低比特压缩方法主要遵循两个方向。标量或分组量化很简单，并且与高效的低精度内核兼容，但当目标预算接近每个权重 2 位时，其表示能力就会受到限制。矢量量化权重压缩提供了更丰富的块级表示，但通常会引入显式码本、索引查找和额外的存储核算。本文提出了 BiSCo-LLM，一种用于极低位 LLM 权重压缩的无码本二进制球形编码框架。核心管道基于三个组件构建。
- Abstract: Large language models (LLMs) are increasingly constrained by memory capacity, weight bandwidth, and checkpoint storage during deployment. Existing low-bit compression methods mainly follow two directions. Scalar or group-wise quantization is simple and compatible with efficient low-precision kernels, but its representation capacity becomes limited when the target budget approaches 2 bits per weight. Vector-quantized...
- Summary (fallback): 机器翻译摘要显示：大型语言模型 (LLM) 在部署过程中越来越受到内存容量、权重带宽和检查点存储的限制。现有的低比特压缩方法主要遵循两个方向。标量或分组量化很简单，并且与高效的低精度内核兼容，但当目标预算接近每个权重 2 位时，其表示能力就会受到限制。矢量量化权重压缩提供了更丰富的块级表示，但通常会引入显式码本、索引查找和额外的存储核算。本文提出了 BiSCo-LLM，一种用于极低位 LLM 权重压缩的无码本二进制球形编码框架。核心管道基于三个组件构建。
- Keywords: weight, spherical, compression, binary, low-bit

### 21. [通过基于部分依赖的可解释约束来指导神经网络训练](https://arxiv.org/abs/2607.08641v1)
- Original title: Steering Neural Network Training through Interpretable Constraints Based on Partial Dependence
- Authors: Yann Claes, Pierre Geurts, Vân Anh Huynh-Thu
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 在过去的几年里，人们对提高机器学习模型的可解释性越来越感兴趣。尽管在开发解释给定模型所学到的相互作用的技术方面投入了大量精力，但很少有研究关注评估此类解释的质量。更少有人关注如何调整模型以产生忠实于先验知识的解释，这一过程称为解释引导学习。此外，该领域的大多数方法都关注分类问题，并且通常假设先验知识关于哪些输入特征或区域是最重要的。在这项工作中，我们引入了一种基于部分依赖来引导神经网络的新方法，使得它们对某些特征的平均响应与有关问题的特定功能领域知识相一致。
- Abstract: Over the last few years, there has been an increased interest in making machine learning models more interpretable. Although a great deal of effort goes into developing techniques for interpreting the interactions learned by a given model, fewer studies focus on assessing the quality of such explanations. Even fewer focus on how to adjust the model to produce explanations faithful to prior knowledge, a process known...
- Summary (fallback): 机器翻译摘要显示：在过去的几年里，人们对提高机器学习模型的可解释性越来越感兴趣。尽管在开发解释给定模型所学到的相互作用的技术方面投入了大量精力，但很少有研究关注评估此类解释的质量。更少有人关注如何调整模型以产生忠实于先验知识的解释，这一过程称为解释引导学习。此外，该领域的大多数方法都关注分类问题，并且通常假设先验知识关于哪些输入特征或区域是最重要的。在这项工作中，我们引入了一种基于部分依赖来引导神经网络的新方法，使得它们对某些特征的平均响应与有关问题的特定功能领域知识相一致。
- Keywords: knowledge, models, focus, steering, neural

### 22. [以患者为中心的对话人工智能的复杂性](https://arxiv.org/abs/2607.08625v1)
- Original title: The complexities of patient-centred conversational artificial intelligence
- Authors: João Matos, Olivia Buege, Donny Cheung, Gary S. Collins, Paula Dhiman et al.
- Meta: 2026-07-09 | cs.AI
- 中文摘要: 由大型语言模型 (LLM) 提供支持的面向消费者的健康聊天机器人越来越多地用于症状评估。然而，聊天机器人的开发和评估通常依赖于合作的、善于表达的、模拟的患者。我们分析了 2,053 个真实的患者与聊天机器人对话，发现不同用户的沟通模式和情绪表达差异很大。我们开发了一个病人模拟器，可以单独模拟临床内容、情绪状态、对话策略和沟通方式。在由 15 名人类评分者进行的受图灵启发的现实主义评估中，模拟对话与真实对话几乎没有区别，人类评分者的准确率达到了 55%。我们使用 1,164 个临床医生分级病例中的 5 名不同患者角色来评估 4 名法学硕士在紧急情况评估中的表现。我们发现沟通方式可以显着改变分类...
- Abstract: Consumer-facing health chatbots powered by large language models (LLMs) are increasingly used for symptom assessment. However, chatbot development and evaluation often rely on cooperative, articulate, simulated patients. We analysed 2,053 real patient-chatbot conversations and found that communication patterns and expression of emotions vary widely across users. We developed a patient simulator that separately model...
- Summary (fallback): 机器翻译摘要显示：由大型语言模型 (LLM) 提供支持的面向消费者的健康聊天机器人越来越多地用于症状评估。然而，聊天机器人的开发和评估通常依赖于合作的、善于表达的、模拟的患者。我们分析了 2,053 个真实的患者与聊天机器人对话，发现不同用户的沟通模式和情绪表达差异很大。我们开发了一个病人模拟器，可以单独模拟临床内容、情绪状态、对话策略和沟通方式。在由 15 名人类评分者进行的受图灵启发的现实主义评估中，模拟对话与真实对话几乎没有区别，人类评分者的准确率达到了 55%。我们使用 1,164 个临床医生分级病例中的 5 名不同患者角色来评估 4 名法学硕士在紧急情况评估中的表现。我们发现沟通方式可以显着改变分类...
- Keywords: communication, conversational, real, patient-centred, artificial

### 23. [当结构化稀疏自动编码器跨模态学习一致的概念时](https://arxiv.org/abs/2607.08605v1)
- Original title: When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities
- Authors: Weiduo Liao, Yunqiao Yang, Ying Wei
- Meta: 2026-07-09 | cs.CV
- 中文摘要: 稀疏自动编码器（SAE）已成为一种有前途的机械可解释性技术，它通过学习大型模型中的一组稀疏潜在特征（每个特征编码一个不同的概念）来实现。然而，在视觉语言模型 (VLM) 中，普通的 SAE 很难学习模态一致的概念，这些概念通常在视觉模态中表现出碎片化的覆盖范围（即不相交的区域）。为了应对这一挑战，我们提出了一种结构化稀疏自动编码器（$S^2AE$），它从视觉模态的语义和空间角度强制概念一致性。具体来说，我们根据 Transformer 注意力相似性和空间邻近性对图像块进行分组，并在训练普通 SAE 时引入结构化稀疏正则化。
- Abstract: Sparse autoencoders (SAEs) have emerged as a promising technique for mechanistic interpretability by learning a set of sparse latent features in large models, each of which encodes a distinct concept. However, in vision-language models (VLMs), vanilla SAEs struggle to learn modality-consistent concepts, with concepts often exhibiting fragmented coverage (i.e., disjoint regions) in the visual modality. To address thi...
- Summary (fallback): 机器翻译摘要显示：稀疏自动编码器（SAE）已成为一种有前途的机械可解释性技术，它通过学习大型模型中的一组稀疏潜在特征（每个特征编码一个不同的概念）来实现。然而，在视觉语言模型 (VLM) 中，普通的 SAE 很难学习模态一致的概念，这些概念通常在视觉模态中表现出碎片化的覆盖范围（即不相交的区域）。为了应对这一挑战，我们提出了一种结构化稀疏自动编码器（$S^2AE$），它从视觉模态的语义和空间角度强制概念一致性。具体来说，我们根据 Transformer 注意力相似性和空间邻近性对图像块进行分组，并在训练普通 SAE 时引入结构化稀疏正则化。
- Keywords: sparse, concepts, concept, structured, saes

### 24. [走向肝细胞癌的精准治疗：风险分层和治疗指导的临床推理法学硕士](https://arxiv.org/abs/2607.08602v1)
- Original title: Towards Precision Therapy in Hepatocellular Carcinoma: A Clinical-Reasoning LLM for Risk Stratification and Treatment Guidance
- Authors: Peng Cui, Jitao Wang, Siyan Xue, Yao Huang, Haoming Xia et al.
- Meta: 2026-07-09 | cs.AI
- 中文摘要: 肝细胞癌（HCC）是一种常见的恶性肿瘤，也是癌症相关死亡的主要原因。当前的指南和分期系统提供了粗略的分类，但经常忽略阶段内的异质性和电子病历 (EMR) 中的临床背景。我们提出 HCC-STAR（肝细胞癌分期、治疗和预后），这是一种临床对齐的大语言模型，可读取常规 EMR 叙述并联合输出基于风险评分的分期、基于证据的基本原理对符合指南的治疗进行排名以及个体化生存估计。我们从 SEER 中收集了约 30,000 个 HCC 病例，并使用经临床医生验证、基于提示的增强工作流程将其扩展为 EMR 式叙述训练数据。
- Abstract: Hepatocellular carcinoma (HCC) is a common malignancy and a leading cause of cancer-related mortality. Current guidelines and staging systems provide coarse categories, but often miss within-stage heterogeneity and the clinical context in electronic medical records (EMRs). We present HCC-STAR (Hepatocellular Carcinoma Staging, Treatment And pRognosis), a clinically aligned large language model that reads routine EMR...
- Summary (fallback): 机器翻译摘要显示：肝细胞癌（HCC）是一种常见的恶性肿瘤，也是癌症相关死亡的主要原因。当前的指南和分期系统提供了粗略的分类，但经常忽略阶段内的异质性和电子病历 (EMR) 中的临床背景。我们提出 HCC-STAR（肝细胞癌分期、治疗和预后），这是一种临床对齐的大语言模型，可读取常规 EMR 叙述并联合输出基于风险评分的分期、基于证据的基本原理对符合指南的治疗进行排名以及个体化生存估计。我们从 SEER 中收集了约 30,000 个 HCC 病例，并使用经临床医生验证、基于提示的增强工作流程将其扩展为 EMR 式叙述训练数据。
- Keywords: hcc-star, risk, treatment, hepatocellular, carcinoma

### 25. [用于保护隐私的心血管疾病风险预测的联合深度学习](https://arxiv.org/abs/2607.08595v1)
- Original title: Federated Deep Learning for Privacy-Preserving Cardiovascular Disease Risk Prediction
- Authors: Hyunho Mo, Djura Smits, Mahlet A. Birhanu, Maarten J. G. Leening, Daniel Bos et al.
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 心血管疾病风险预测模型通常依赖于来自单个机构或集中汇总数据集的数据。跨机构扩展这些模型可能会受到隐私法规和共享患者级数据的限制的限制。联合学习可以在不传输敏感患者数据的情况下实现协作模型开发，但其在医疗保健中的应用仍然具有挑战性，因为数据集通常在大小、人群特征和结果定义方面存在差异。
- Abstract: Cardiovascular disease risk prediction models often rely on data from a single institution or centrally pooled datasets. Extending these models across institutions could be limited by privacy regulations and constraints on sharing patient-level data. Federated learning enables collaborative model development without transferring sensitive patient data, but its application in healthcare remains challenging because da...
- Summary (fallback): 机器翻译摘要显示：心血管疾病风险预测模型通常依赖于来自单个机构或集中汇总数据集的数据。跨机构扩展这些模型可能会受到隐私法规和共享患者级数据的限制的限制。联合学习可以在不传输敏感患者数据的情况下实现协作模型开发，但其在医疗保健中的应用仍然具有挑战性，因为数据集通常在大小、人群特征和结果定义方面存在差异。
- Keywords: federated, learning, deep, cardiovascular, disease

### 26. [对抗性不确定性下的鲁棒贝叶斯决策](https://arxiv.org/abs/2607.08590v1)
- Original title: Robust Bayesian Decision Making under Adversarial Uncertainty
- Authors: Haripriya Harikumar, Sammie Katt, Yasir Zubayr Barlas, Samuel Kaski
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 科学实验通常旨在最大化信息增益，但在许多应用中，主要目标是支持可靠的下游决策。现有的决策感知实验设计和主动学习方法通​​常假设明确的结果模型，并隐含地依赖于现实世界扰动下最优决策的稳定性。然而，在实践中，实验结果经常受到隐藏效应或弱建模效应的影响，这可能会极大地改变决策的最优性并导致误导性的结论。我们研究顺序对抗性鲁棒决策感知实验设计，其中数据采集必须考虑针对可能的最坏情况意外影响的信息增益，此处建模为对抗性变量的变化。
- Abstract: Scientific experiments are often designed to maximize information gain, yet in many applications the primary objective is to support reliable downstream decision-making. Existing decision-aware experimental design and active learning methods typically assume well-specified outcome models and implicitly rely on the stability of the optimal decision under real-world perturbations. In practice, however, experimental ou...
- Summary (fallback): 机器翻译摘要显示：科学实验通常旨在最大化信息增益，但在许多应用中，主要目标是支持可靠的下游决策。现有的决策感知实验设计和主动学习方法通​​常假设明确的结果模型，并隐含地依赖于现实世界扰动下最优决策的稳定性。然而，在实践中，实验结果经常受到隐藏效应或弱建模效应的影响，这可能会极大地改变决策的最优性并导致误导性的结论。我们研究顺序对抗性鲁棒决策感知实验设计，其中数据采集必须考虑针对可能的最坏情况意外影响的信息增益，此处建模为对抗性变量的变化。
- Keywords: decision, under, experimental, design, robust

### 27. [基于伪逆的极限学习机的谱稳定性](https://arxiv.org/abs/2607.08581v1)
- Original title: Spectral Stability of Pseudoinverse-Based Extreme Learning Machine
- Authors: Bich Van Nguyen, Ngoc Anh Khong
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 极限学习机 (ELM) 使用 Moore-Penrose 伪逆来分析计算输出权重。尽管这可以实现快速训练，但其数值稳定性在很大程度上取决于隐藏层矩阵的条件。本文从谱的角度研究基于伪逆的ELM。我们表明，最小奇异值控制输出权重中的扰动放大，而条件数提供了隐藏层不稳定性的定量测量。我们将基于 SVD 的伪逆计算与迭代超幂方法进行比较，并通过随机特征解释讨论宽度相关条件。合成矩阵和 ELM 基准的实验表明，基于 SVD 的方法在病态条件下仍然是最可靠的，而迭代方法对光谱特性更敏感。
- Abstract: Extreme Learning Machine (ELM) computes output weights analytically using the Moore-Penrose pseudoinverse. Although this leads to fast training, its numerical stability depends strongly on the conditioning of the hidden layer matrix. This paper studies pseudoinverse-based ELM from a spectral perspective. We show that the smallest singular value governs perturbation amplification in the output weights, while the cond...
- Summary (fallback): 机器翻译摘要显示：极限学习机 (ELM) 使用 Moore-Penrose 伪逆来分析计算输出权重。尽管这可以实现快速训练，但其数值稳定性在很大程度上取决于隐藏层矩阵的条件。本文从谱的角度研究基于伪逆的ELM。我们表明，最小奇异值控制输出权重中的扰动放大，而条件数提供了隐藏层不稳定性的定量测量。我们将基于 SVD 的伪逆计算与迭代超幂方法进行比较，并通过随机特征解释讨论宽度相关条件。合成矩阵和 ELM 基准的实验表明，基于 SVD 的方法在病态条件下仍然是最可靠的，而迭代方法对光谱特性更敏感。
- Keywords: spectral, stability, conditioning, methods, pseudoinverse-based

### 28. [ImputeViz：用于诊断缺失数据和比较插补方法的可视化分析仪表板](https://arxiv.org/abs/2607.08579v1)
- Original title: ImputeViz: A Visual Analytics Dashboard for Diagnosing Missing Data and Comparing Imputation Methods
- Authors: Aitik Dandapat, Lalith Punepalle Raveendrareddy, Mithilesh Kumar Singh, Klaus Mueller
- Meta: 2026-07-09 | cs.HC
- 中文摘要: 缺失数据是科学、社会科学和公共卫生研究中持续存在的障碍，常常使分析产生偏差，并要求分析师对如何处理缺失值承担责任。我们推出了 ImputeViz，这是一个集成的可视化分析仪表板，支持诊断缺失、配置插补模型和评估结果。该系统在交互式环境中汇集了广泛使用的方法，包括 MICE、随机森林、XGBoost 和 kNN，使缺失模式变得明确。为了支持地理空间推理，我们引入了 gKNN，这是一种基于地理信息的 kNN 变体，它融合了社会经济和空间距离并公开了捐助者的贡献，通过显示哪些区域驱动每个估计来实现基于来源的视觉问责制。
- Abstract: Missing data is a persistent obstacle in scientific, social science, and public health research, often biasing analyses and placing accountability on analysts for how they handle missing values. We introduce ImputeViz, an integrated visual analytics dashboard that supports diagnosing missingness, configuring imputation models, and evaluating results. The system brings together widely used methods, including MICE, Ra...
- Summary (fallback): 机器翻译摘要显示：缺失数据是科学、社会科学和公共卫生研究中持续存在的障碍，常常使分析产生偏差，并要求分析师对如何处理缺失值承担责任。我们推出了 ImputeViz，这是一个集成的可视化分析仪表板，支持诊断缺失、配置插补模型和评估结果。该系统在交互式环境中汇集了广泛使用的方法，包括 MICE、随机森林、XGBoost 和 kNN，使缺失模式变得明确。为了支持地理空间推理，我们引入了 gKNN，这是一种基于地理信息的 kNN 变体，它融合了社会经济和空间距离并公开了捐助者的贡献，通过显示哪些区域驱动每个估计来实现基于来源的视觉问责制。
- Keywords: visual, missingness, methods, imputeviz, analytics

### 29. [逆变理论：困难任务最小解决方案的强一致性](https://arxiv.org/abs/2607.08561v1)
- Original title: Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks
- Authors: Dan Yamins, Aran Nayebi
- Meta: 2026-07-09 | cs.LG
- 中文摘要: NeuroAI 在过去 15 年中取得的一系列结果提出了核心问题：如何将深度神经网络 (DNN) 模型与大脑进行比较，以及人工网络和真实大脑网络之间的趋同进化程度。在这里，我们展示了对于足够困难的任务的任何两个最小 DNN 解决方案：（i）基于仿射映射的网络表示的“弱”对齐保证了特权轴的“强”对齐，以及（ii）对齐网络层次结构的“拉链”，导致端到端任务优化中特权轴的出现。
- Abstract: A series of results from the NeuroAI over the past fifteen years have raised core questions both about how to compare Deep Neural Network (DNN) models to the brain, and about how much convergent evolution to expect between artificial networks and real brain networks. Here, we show that for any two minimal DNN solutions to a sufficiently hard task: (i) "weak" alignment of network representations based on affine mappi...
- Summary (fallback): 机器翻译摘要显示：NeuroAI 在过去 15 年中取得的一系列结果提出了核心问题：如何将深度神经网络 (DNN) 模型与大脑进行比较，以及人工网络和真实大脑网络之间的趋同进化程度。在这里，我们展示了对于足够困难的任务的任何两个最小 DNN 解决方案：（i）基于仿射映射的网络表示的“弱”对齐保证了特权轴的“强”对齐，以及（ii）对齐网络层次结构的“拉链”，导致端到端任务优化中特权轴的出现。
- Keywords: alignment, strong, network, contravariance, theory

### 30. [CAAD：通过多尺度对齐和结构因果一致性进行因果感知多元时间序列异常检测](https://arxiv.org/abs/2607.08555v1)
- Original title: CAAD: Causality-Aware Multivariate Time Series Anomaly Detection via Multi-Scale Alignment and Structural Causal Consistency
- Authors: Xin Wang, Yunshi Wen, Yanan He, Haotian Xu, Youlan Zhao et al.
- Meta: 2026-07-09 | cs.LG
- 中文摘要: 复杂工业系统的运行完整性依赖于精确的异常检测和诊断。绝大多数现有方法都狭隘地专注于捕获表示的时间相似性，常常忽视内部因果关系的破坏，而内部因果关系是系统故障和潜在异常的特征。在本文中，我们提出了一种新颖的框架（CAAD），它将异常检测重新定义为通过外生变量对格兰杰因果关系一致性的持续验证。具体来说，CAAD 框架将外生时间序列变量建模为残差，将异常识别为外部干预引起的显着偏差。所提出的框架利用多尺度对齐来内部化系统动力学，并利用基于梯度的矩阵来监控内部因果关系的崩溃。
- Abstract: The operational integrity of complex industrial systems relies on precise anomaly detection and diagnosis. The vast majority of existing methods narrowly focus on capturing temporal similarities of representations, often overlooking the disruption of internal causal relationships, which characterizes system failures and latent anomalies. In this paper, we propose a novel framework (CAAD) that reframes anomaly detect...
- Summary (fallback): 机器翻译摘要显示：复杂工业系统的运行完整性依赖于精确的异常检测和诊断。绝大多数现有方法都狭隘地专注于捕获表示的时间相似性，常常忽视内部因果关系的破坏，而内部因果关系是系统故障和潜在异常的特征。在本文中，我们提出了一种新颖的框架（CAAD），它将异常检测重新定义为通过外生变量对格兰杰因果关系一致性的持续验证。具体来说，CAAD 框架将外生时间序列变量建模为残差，将异常识别为外部干预引起的显着偏差。所提出的框架利用多尺度对齐来内部化系统动力学，并利用基于梯度的矩阵来监控内部因果关系的崩溃。
- Keywords: caad, anomaly, detection, causal, framework

## biorxiv

### 1. [TRACR：一种顺行跨神经元追踪系统，用于跨突触的遗传访问和纵向电路分析](https://www.biorxiv.org/content/10.64898/2026.02.08.704659v2)
- Original title: TRACR: an anterograde transneuronal tracing system for genetic access across synapses and longitudinal circuit analysis
- Authors: Ibrahimi, M., Gray, M. T., Rochon, P.-L., Eiras, S. M., Lee, J. J. et al.
- Meta: 2026-07-12 | neuroscience | DOI: 10.64898/2026.02.08.704659
- 中文摘要: 跟踪神经信号汇聚到单个神经元或从单个神经元发散是理解回路功能和疾病相关功能障碍的核心。现有的顺行跨神经元示踪剂受到细胞毒性和对连接伙伴的不完整遗传访问的限制。为了解决这些限制，我们采用合成 Notch 设计来创建 TRanssynaptic 顺行电路读数 (TRACR)。工程配体-受体跨突触的结合诱导 TRE 驱动的报告基因转录，从而能够表征突触后神经元。 TRACR 提供对突触前和突触后群体的分离遗传访问，并且可以与标记、传感器或效应器结合以扩展电路分析。
- Abstract: Following neural signals as they converge onto and diverge from individual neurons is central to understanding circuit function and disease-related dysfunction. Existing anterograde transneuronal tracers are limited by cytotoxicity and incomplete genetic access over connected partners. To address these limitations, we adapted synthetic Notch designs to create TRanssynaptic Anterograde Circuit Readout (TRACR). Bindin...
- Summary (fallback): 机器翻译摘要显示：跟踪神经信号汇聚到单个神经元或从单个神经元发散是理解回路功能和疾病相关功能障碍的核心。现有的顺行跨神经元示踪剂受到细胞毒性和对连接伙伴的不完整遗传访问的限制。为了解决这些限制，我们采用合成 Notch 设计来创建 TRanssynaptic 顺行电路读数 (TRACR)。工程配体-受体跨突触的结合诱导 TRE 驱动的报告基因转录，从而能够表征突触后神经元。 TRACR 提供对突触前和突触后群体的分离遗传访问，并且可以与标记、传感器或效应器结合以扩展电路分析。
- Keywords: tracr, circuit, synapses, anterograde, transneuronal

### 2. [小胶质细胞 Trem2 R47H 阿尔茨海默病风险变异体不会明显改变幼鼠的海马突触传递](https://www.biorxiv.org/content/10.1101/2025.08.22.671714v2)
- Original title: The Microglial Trem2 R47H Alzheimer's Disease Risk Variant Does Not Detectably Alter Hippocampal Synaptic Transmission in Young Mice
- Authors: Aljawder, A., Choudhury, H., Cummings, D. M., Wood, J., Edwards, F. A.
- Meta: 2026-07-12 | neuroscience | DOI: 10.1101/2025.08.22.671714
- 中文摘要: 小胶质细胞 TREM2 基因的罕见 R47H 变异会增加阿尔茨海默病 (AD) 风险，但其对早期海马回路的影响仍不清楚。据报道，Trem2 对于发育中的兴奋性突触回路的小胶质细胞依赖性细化非常重要。我们假设 TREM2 功能的丧失可能会导致电路发生变化，因为小胶质细胞修剪不活跃突触的能力降低，这可能会使个体更容易患上以后的疾病。我们使用体外膜片钳记录和 Bassoon-Homer1 免疫组织化学比较了 3 周龄 WT 和纯合 Trem2 R47H 敲入小鼠的基础突触传递和突触密度。基础突触活动、微型兴奋事件和诱发释放概率没有变化。
- Abstract: The rare R47H variant of the microglial TREM2 gene increases Alzheimers disease (AD) risk, but its effects on early hippocampal circuitry remain unclear. Trem2 has been reported to be important for microglial-dependent refinement of excitatory synaptic circuits in development. We hypothesized that loss of TREM2 function might result in changes in circuitry due to reduced microglial ability to prune inactive synapses...
- Summary (fallback): 机器翻译摘要显示：小胶质细胞 TREM2 基因的罕见 R47H 变异会增加阿尔茨海默病 (AD) 风险，但其对早期海马回路的影响仍不清楚。据报道，Trem2 对于发育中的兴奋性突触回路的小胶质细胞依赖性细化非常重要。我们假设 TREM2 功能的丧失可能会导致电路发生变化，因为小胶质细胞修剪不活跃突触的能力降低，这可能会使个体更容易患上以后的疾病。我们使用体外膜片钳记录和 Bassoon-Homer1 免疫组织化学比较了 3 周龄 WT 和纯合 Trem2 R47H 敲入小鼠的基础突触传递和突触密度。基础突触活动、微型兴奋事件和诱发释放概率没有变化。
- Keywords: synaptic, trem2, density, r47h, excitatory

### 3. [记忆痕迹反映了它们最后一次被检索的方式](https://www.biorxiv.org/content/10.1101/2025.05.30.657135v2)
- Original title: Memory Traces Reflect How They Were Last Retrieved
- Authors: Qi, X., Coutanche, M. N.
- Meta: 2026-07-12 | neuroscience | DOI: 10.1101/2025.05.30.657135
- 中文摘要: 众所周知，情景记忆会随着每次检索行为而改变。我们假设在情景检索过程中以不同的方式访问语义知识——从独特的感知特征到分类和主题背景——塑造了这些记忆随后在识别过程中的表示方式。在这项功能性磁共振成像 (fMRI) 研究中，人类参与者学习了新颖的文字-图像对，并进行了重新接触，这需要访问三个不同级别之一的语义知识：项目、类别或主题。然后参与者完成了识别任务。尽管行为记忆表现在不同条件下是匹配的，但识别期间的神经活动根据先前的语义访问历史而变化。
- Abstract: Episodic memories are known to change with each act of retrieval. We hypothesize that accessing semantic knowledge in different ways during episodic retrieval -- from unique perceptual features to taxonomic and thematic context -- shapes how those memories are subsequently represented during recognition. In this functional magnetic resonance imaging (fMRI) study, human participants learned novel word-image pairs and...
- Summary (fallback): 机器翻译摘要显示：众所周知，情景记忆会随着每次检索行为而改变。我们假设在情景检索过程中以不同的方式访问语义知识——从独特的感知特征到分类和主题背景——塑造了这些记忆随后在识别过程中的表示方式。在这项功能性磁共振成像 (fMRI) 研究中，人类参与者学习了新颖的文字-图像对，并进行了重新接触，这需要访问三个不同级别之一的语义知识：项目、类别或主题。然后参与者完成了识别任务。尽管行为记忆表现在不同条件下是匹配的，但识别期间的神经活动根据先前的语义访问历史而变化。
- Keywords: semantic, access, during, recognition, visual

### 4. [使用强大的蔗糖合酶变体进行高效且低影响的酶糖基化](https://www.biorxiv.org/content/10.64898/2026.01.30.702896v2)
- Original title: Efficient and low-impact enzymatic glycosylation with robust sucrose synthase variants
- Authors: Mejia-Otalvaro, F., Delima, D., Hobusch, M., Lax, B. M., Mendonca, C. et al.
- Meta: 2026-07-12 | biochemistry | DOI: 10.64898/2026.01.30.702896
- 中文摘要: 蔗糖合酶 (SuSy) 为生物催化 UDP-葡萄糖回收提供了一条有吸引力的途径，但性能不足限制了其使用。在这里，我们报告了一个集成的工程工作流程，该工作流程克服了糖基供体回收酶的效率和稳健性之间长期存在的权衡。我们设计的 SuSy 变体结合了超野生型活性 (178%) 和增强的热稳定性 ({Delta}Tmapp = 13.3 {°C)、溶剂耐受性（在 25% DMSO 中保留了 70% 的活性）和 123 倍长的半衰期。这些变体的总周转数达到约 100 万（60°C），支持了它们的工业相关性。
- Abstract: Sucrose synthase (SuSy) offers an attractive route for biocatalytic UDP-glucose recycling, but inadequate performance has limited its use. Here, we report an integrated engineering workflow that overcomes the longstanding trade-off between efficiency and robustness in glycosyl donor recycling enzymes. We engineered SuSy variants combining supra-wildtype activity (178%) with enhanced thermostability ({Delta}Tmapp = 1...
- Summary (fallback): 机器翻译摘要显示：蔗糖合酶 (SuSy) 为生物催化 UDP-葡萄糖回收提供了一条有吸引力的途径，但性能不足限制了其使用。在这里，我们报告了一个集成的工程工作流程，该工作流程克服了糖基供体回收酶的效率和稳健性之间长期存在的权衡。我们设计的 SuSy 变体结合了超野生型活性 (178%) 和增强的热稳定性 ({Delta}Tmapp = 13.3 {°C)、溶剂耐受性（在 25% DMSO 中保留了 70% 的活性）和 123 倍长的半衰期。这些变体的总周转数达到约 100 万（60°C），支持了它们的工业相关性。
- Keywords: glycosylation, variants, susy, robustness, sucrose

### 5. [硫辛酰合酶 RSSY 基序中的氨基酸控制底物结合和反应性](https://www.biorxiv.org/content/10.64898/2026.05.25.727706v2)
- Original title: Amino Acids in the RSSY Motif of Lipoyl Synthase Control Substrate Binding and Reactivity
- Authors: Jeyachandran, V., Lanz, N., Pandelia, M.-E., Rectenwald, J., Pendyala, J. et al.
- Meta: 2026-07-12 | biochemistry | DOI: 10.64898/2026.05.25.727706
- 中文摘要: 硫辛酰辅助因子 (LipCo) 生物合成的最后一步是在正辛酰链的 C6 和 C8 处添加两个硫原子，该链以酰胺键连接到硫辛酰载体蛋白的目标赖氨酰残基上。该反应由硫辛酰合酶催化，硫辛酰合酶是自由基 S-腺苷甲硫氨酸 (SAM) 超家族的成员。硫辛酰合酶需要两个 [4Fe-4S] 簇。一个簇用于还原性裂解 SAM，生成两个 5'-脱氧腺苷基 5'-自由基，这会通过两个连续步骤提取底物的 C6 和 C8 氢原子。第二个簇称为辅助簇，在周转过程中被消耗以提供附着的硫原子。辅助簇由 CX4CX5C 基序中的 3 个半胱氨酸和蛋白质 C 末端区域高度保守的 R306、S、S308、Y 基序中的 1 个丝氨酸残基（大肠杆菌中的 Ser308）连接。
- Abstract: The last step in the biosynthesis of the lipoyl cofactor (LipCo) is the addition of two sulfur atoms at C6 and C8 of an n-octanoyl chain attached in an amide linkage to a target lysyl residue of a lipoyl carrier protein. This reaction is catalyzed by lipoyl synthase, a member of the radical S-adenosylmethionine (SAM) superfamily. Lipoyl synthase requires two [4Fe-4S] clusters. One cluster is used to cleave SAM reduc...
- Summary (fallback): 机器翻译摘要显示：硫辛酰辅助因子 (LipCo) 生物合成的最后一步是在正辛酰链的 C6 和 C8 处添加两个硫原子，该链以酰胺键连接到硫辛酰载体蛋白的目标赖氨酰残基上。该反应由硫辛酰合酶催化，硫辛酰合酶是自由基 S-腺苷甲硫氨酸 (SAM) 超家族的成员。硫辛酰合酶需要两个 [4Fe-4S] 簇。一个簇用于还原性裂解 SAM，生成两个 5'-脱氧腺苷基 5'-自由基，这会通过两个连续步骤提取底物的 C6 和 C8 氢原子。第二个簇称为辅助簇，在周转过程中被消耗以提供附着的硫原子。辅助簇由 CX4CX5C 基序中的 3 个半胱氨酸和蛋白质 C 末端区域高度保守的 R306、S、S308、Y 基序中的 1 个丝氨酸残基（大肠杆菌中的 Ser308）连接。
- Keywords: cluster, lipoyl, motif, auxiliary, synthase

### 6. [用于将药物局部输送至目标器官的可生物降解的动脉内装置](https://www.biorxiv.org/content/10.64898/2026.02.23.707478v2)
- Original title: Biodegradable Intra-arterial Devices for Focal Drug Delivery to Targeted Organs
- Authors: Kinra, M., Sheng, R., Chen, Y., Souza, A. d., Bhatia, A. et al.
- Meta: 2026-07-12 | bioengineering | DOI: 10.64898/2026.02.23.707478
- 中文摘要: 本研究介绍了用于目标器官局部治疗的可生物降解的动脉内药物输送（IADD）装置的开发。 IADD 装置使用镁 (Mg) 和聚癸二酸甘油酯 (PGS) 制造，利用其生物相容性和可调节的生物降解性，并装载两种模型药物：地塞米松 (DEX) 或顺铂 (CIS)。制造具有螺旋和线性设计的 IADD 装置，用于将药物集中输送到目标器官，并使用扫描电子显微镜 (SEM)、能量色散 X 射线光谱 (EDS)、热重分析 (TGA) 和傅里叶变换红外光谱 (FTIR) 对其微观结构和成分进行表征。结果证实了药物在装置内的成功掺入和稳定性。
- Abstract: This study presents the development of biodegradable intra-arterial drug delivery (IADD) devices for the focal treatment of targeted organs. The IADD devices are fabricated using magnesium (Mg) and poly(glycerol sebacate) (PGS), leveraging their biocompatibility and tunable biodegradability, and are loaded with two model drugs, dexamethasone (DEX) or cisplatin (CIS). The IADD devices with helical and linear designs...
- Summary (fallback): 机器翻译摘要显示：本研究介绍了用于目标器官局部治疗的可生物降解的动脉内药物输送（IADD）装置的开发。 IADD 装置使用镁 (Mg) 和聚癸二酸甘油酯 (PGS) 制造，利用其生物相容性和可调节的生物降解性，并装载两种模型药物：地塞米松 (DEX) 或顺铂 (CIS)。制造具有螺旋和线性设计的 IADD 装置，用于将药物集中输送到目标器官，并使用扫描电子显微镜 (SEM)、能量色散 X 射线光谱 (EDS)、热重分析 (TGA) 和傅里叶变换红外光谱 (FTIR) 对其微观结构和成分进行表征。结果证实了药物在装置内的成功掺入和稳定性。
- Keywords: devices, drug, iadd, focal, delivery

### 7. [从咬合到吞噬：目标力学通过曲率-肌动蛋白耦合决定吞噬模式](https://www.biorxiv.org/content/10.64898/2026.01.28.702248v2)
- Original title: From biting to engulfment: Target mechanics determines modes of phagocytosis through curvature--actin coupling
- Authors: Sadhukhan, S., Cornell, C. E., Sandhu, M. K., Palau, M. B., Peeters, Y. et al.
- Meta: 2026-07-12 | biophysics | DOI: 10.64898/2026.01.28.702248
- 中文摘要: 吞噬作用是一种核心的先天免疫过程，可清除具有广泛机械特性的目标，但目标力学在识别和吞噬中的作用仍不清楚。在这里，我们结合理论模型和实验来揭示目标刚度如何控制吞噬细胞与目标相互作用的不同模式。我们开发了一种基于膜的模拟框架，其中吞噬细胞及其目标都是可变形的并经历较大的形状变化，而肌动蛋白驱动的突起则受到曲率敏感膜复合物的调节。该模型预测了随着目标刚度增加而出现的三种机械状态：（i）咬合（trogocytosis），其中部分目标被提取； (ii) 推动，目标被移位而不是被吞没； (iii) 完全吞没。
- Abstract: Phagocytosis is a core innate immune process that clears targets spanning a wide range of mechanical properties, yet the role of target mechanics in recognition and engulfment remains unclear. Here, we combine theoretical modeling and experiments to reveal how target stiffness governs distinct modes of phagocyte--target interaction. We develop a membrane-based simulation framework in which both the engulfing cell an...
- Summary (fallback): 机器翻译摘要显示：吞噬作用是一种核心的先天免疫过程，可清除具有广泛机械特性的目标，但目标力学在识别和吞噬中的作用仍不清楚。在这里，我们结合理论模型和实验来揭示目标刚度如何控制吞噬细胞与目标相互作用的不同模式。我们开发了一种基于膜的模拟框架，其中吞噬细胞及其目标都是可变形的并经历较大的形状变化，而肌动蛋白驱动的突起则受到曲率敏感膜复合物的调节。该模型预测了随着目标刚度增加而出现的三种机械状态：（i）咬合（trogocytosis），其中部分目标被提取； (ii) 推动，目标被移位而不是被吞没； (iii) 完全吞没。
- Keywords: target, engulfment, mechanics, biting, modes

### 8. [代谢 STAMP 揭示了编程 β 细胞胰岛素分泌的 GPCR 信号网络](https://www.biorxiv.org/content/10.1101/2025.10.03.680349v2)
- Original title: Metabolic STAMP reveals GPCR signaling networks that program β-cell insulin secretion
- Authors: Aziz-Zanjani, M. O., Turn, R. E., Hang, Y., Asthana, A., LaBrie, L. E. et al.
- Meta: 2026-07-12 | physiology | DOI: 10.1101/2025.10.03.680349
- 中文摘要: 在健康和糖尿病中，胰岛 {β} 细胞整合葡萄糖和激素信号，通过空间和时间组织的磷酸化网络来控制胰岛素分泌。在这里，我们使用代谢 STAMP（通过显微镜和磷酸化蛋白质组进行同步时空分析），将小鼠 {β} 细胞和人类胰岛中的时间分辨磷酸化蛋白质组学、成像和激酶抑制相结合，以绘制刺激特异性 GPCR 信号通路。代谢 STAMP 揭示 GLP1-R 和 FFAR4 参与不同的分区激酶程序，包括 GLP1-R 偏向的 ERK 激活、受体特异性 cAMP-PKA 结构域以及磷酸化 ATAT1/HDAC6 节点，该节点在 GSIS 期间根据刺激条件差异调节微管乙酰化和胰岛素分泌。
- Abstract: Pancreatic islet {beta} cells integrate glucose and hormonal cues to control insulin secretion through spatially and temporally organized phosphorylation networks in health and diabetes. Here, using Metabolic STAMP (Synchronized Temporal-Spatial Analysis via Microscopy and Phosphoproteomics), we combine time-resolved phosphoproteomics, imaging, and kinase inhibition in mouse {beta} cells and human islets to map stim...
- Summary (fallback): 机器翻译摘要显示：在健康和糖尿病中，胰岛 {β} 细胞整合葡萄糖和激素信号，通过空间和时间组织的磷酸化网络来控制胰岛素分泌。在这里，我们使用代谢 STAMP（通过显微镜和磷酸化蛋白质组进行同步时空分析），将小鼠 {β} 细胞和人类胰岛中的时间分辨磷酸化蛋白质组学、成像和激酶抑制相结合，以绘制刺激特异性 GPCR 信号通路。代谢 STAMP 揭示 GLP1-R 和 FFAR4 参与不同的分区激酶程序，包括 GLP1-R 偏向的 ERK 激活、受体特异性 cAMP-PKA 结构域以及磷酸化 ATAT1/HDAC6 节点，该节点在 GSIS 期间根据刺激条件差异调节微管乙酰化和胰岛素分泌。
- Keywords: metabolic, signaling, insulin, secretion, stamp

### 9. [疟疾寄生虫通过 AP2-HCR DNA 结合蛋白协调宿主细胞重塑](https://www.biorxiv.org/content/10.64898/2026.06.23.733580v2)
- Original title: Malaria parasites coordinate host cell remodeling through the AP2-HCR DNA-binding protein
- Authors: Subudhi, A. K., Vedagiri, D., Mfarrej, S., Abu-Shamma, R., Satyam, R. et al.
- Meta: 2026-07-12 | microbiology | DOI: 10.64898/2026.06.23.733580
- 中文摘要: 寄生虫诱导的宿主细胞重塑对于恶性疟原虫在红细胞内发育周期（IDC）中的生存至关重要，但协调这一过程的转录机制仍知之甚少。在这里，我们描述了恶性疟原虫无性和有性血液阶段中必需的 ApiAP2 转录因子 PfAP2-HCR（宿主细胞重塑）。 pfap2-hcr 的条件截短表明 PfAP2-HCR 对于环期发育和寄生虫成熟至关重要。 PfAP2-HCR 的缺失破坏了宿主细胞重塑基因的表达，导致毛雷氏裂的消失和寄生虫蛋白输出机制的崩溃。
- Abstract: Parasite-induced host cell remodeling is essential for Plasmodium falciparum survival during the intraerythrocytic developmental cycle (IDC), yet the transcriptional mechanisms coordinating this process remain poorly understood. Here, we characterize an essential ApiAP2 transcription factor, PfAP2-HCR (host cell remodeling), during both the asexual and sexual blood stages of P. falciparum. Conditional truncation of...
- Summary (fallback): 机器翻译摘要显示：寄生虫诱导的宿主细胞重塑对于恶性疟原虫在红细胞内发育周期（IDC）中的生存至关重要，但协调这一过程的转录机制仍知之甚少。在这里，我们描述了恶性疟原虫无性和有性血液阶段中必需的 ApiAP2 转录因子 PfAP2-HCR（宿主细胞重塑）。 pfap2-hcr 的条件截短表明 PfAP2-HCR 对于环期发育和寄生虫成熟至关重要。 PfAP2-HCR 的缺失破坏了宿主细胞重塑基因的表达，导致毛雷氏裂的消失和寄生虫蛋白输出机制的崩溃。
- Keywords: pfap2-hcr, host, cell, remodeling, essential

### 10. [功能代孕可以在缺乏 COL3A1 直向同源物的情况下对斑马鱼进行血管埃勒斯-当洛斯综合征建模](https://www.biorxiv.org/content/10.64898/2026.07.03.736265v2)
- Original title: Functional surrogacy enables Vascular Ehlers-Danlos Syndrome modelling in zebrafish in the absence of a COL3A1 ortholog
- Authors: Baird, D. A., Pidlisnyuk, N., Matischen, A., Matelowska, Z., Seo, S. et al.
- Meta: 2026-07-12 | genetics | DOI: 10.64898/2026.07.03.736265
- 中文摘要: COL3A1 的致病变异会导致血管埃勒斯-当洛斯综合征 (vEDS)，这是一种罕见的结缔组织疾病，其特征是血管脆性，增加动脉破裂/夹层的风险。基因组测序的进步导致 COL3A1 变异数量不断增加，其临床意义尚不清楚，这些变异被称为意义不确定的变异 (VUS)。 VUS 给诊断和临床管理带来了挑战。因此，人们做出了重大努力，将这些变异重新分类为疾病因果关系中的致病变异或良性变异。来自模型系统的功能数据可以为临床医生提供有关变异致病性的重要证据。
- Abstract: Pathogenic variants in COL3A1 cause Vascular Ehlers-Danlos syndrome (vEDS), a rare connective tissue disorder characterised by vascular fragility, increasing the risk of arterial ruptures/dissection. Advances in genomic sequencing have led to an increasing number of COL3A1 variants where the clinical significance is unclear, with these being termed variants of uncertain significance (VUS). VUS creates challenges for...
- Summary (fallback): 机器翻译摘要显示：COL3A1 的致病变异会导致血管埃勒斯-当洛斯综合征 (vEDS)，这是一种罕见的结缔组织疾病，其特征是血管脆性，增加动脉破裂/夹层的风险。基因组测序的进步导致 COL3A1 变异数量不断增加，其临床意义尚不清楚，这些变异被称为意义不确定的变异 (VUS)。 VUS 给诊断和临床管理带来了挑战。因此，人们做出了重大努力，将这些变异重新分类为疾病因果关系中的致病变异或良性变异。来自模型系统的功能数据可以为临床医生提供有关变异致病性的重要证据。
- Keywords: col3a1, functional, zebrafish, variants, vascular

## medrxiv

### 1. [PABformer：通过可穿戴加速度测量进行基于多通道变压器的身体活动表示学习，用于预测帕金森病](https://www.medrxiv.org/content/10.1101/2025.08.12.25333460v2)
- Original title: PABformer: Multi-Channel Transformer-Based Physical Activity Representation Learning from Wearable Accelerometry for Prediction of Parkinson Disease
- Authors: He, K., Fan, L., Qian, H., Li, C., Wang, M.
- Meta: 2026-07-11 | health informatics | DOI: 10.1101/2025.08.12.25333460
- 中文摘要: 帕金森病 (PD) 是一种常见的神经退行性疾病，由于明显的运动症状延迟发作以及长期行为变化的复杂性，其早期诊断和预测仍然具有挑战性。可穿戴加速度计提供了一种可扩展且非侵入性的方法，用于监测自由生活环境中的身体活动 (PA)，并已成为 PD 预测的一种有前景的工具。然而，现有的基于加速度计的方法通常依赖于粗略的汇总统计数据或模型，捕获多日加速度计记录中的远程时间依赖性的能力有限。在本研究中，我们提出了 PABformer，这是一种多通道 Transformer 框架，专为从加速度计数据学习长期 PA 行为表示而设计。
- Abstract: Parkinson disease (PD) is a prevalent neurodegenerative disorder whose early diagnosis and prediction remain challenging due to the delayed onset of overt motor symptoms and the complexity of long-term behavioral changes. Wearable accelerometers provide a scalable and non-invasive approach for monitoring physical activity (PA) in free-living environments and have emerged as a promising tool for PD prediction. Howeve...
- Summary (fallback): 机器翻译摘要显示：帕金森病 (PD) 是一种常见的神经退行性疾病，由于明显的运动症状延迟发作以及长期行为变化的复杂性，其早期诊断和预测仍然具有挑战性。可穿戴加速度计提供了一种可扩展且非侵入性的方法，用于监测自由生活环境中的身体活动 (PA)，并已成为 PD 预测的一种有前景的工具。然而，现有的基于加速度计的方法通常依赖于粗略的汇总统计数据或模型，捕获多日加速度计记录中的远程时间依赖性的能力有限。在本研究中，我们提出了 PABformer，这是一种多通道 Transformer 框架，专为从加速度计数据学习长期 PA 行为表示而设计。
- Keywords: pabformer, prediction, learning, accelerometer, activity

### 2. [全球热适宜性的变化和面临伊蚊传播登革热风险的人群。 CMIP6场景下的蚊子](https://www.medrxiv.org/content/10.64898/2026.07.02.26357126v2)
- Original title: Global shifts in thermal suitability and population at risk for dengue transmission by Aedes spp. mosquitoes under CMIP6 scenarios
- Authors: Ryan, S. J., Lippi, C. J., Johnson, L. R., Meredith, J.
- Meta: 2026-07-11 | public and global health | DOI: 10.64898/2026.07.02.26357126
- 中文摘要: 过去十年中，全球登革热风险和负担不断增加，破纪录的疫情导致病例数量不断增加，现有适宜传播地区的疫情不断增加，并在新的地点发生。包括气候变化在内的全球变化过程的结合，为蚊子传播的登革热病毒的引入和死灰复燃提供了环境背景。了解暴露风险的变化是公共卫生准备工作不可或缺的一部分。这项研究通过一系列大气环流模型 (GCM) 提供了 CMIP6 气候情景下登革热传播的热适宜性的全球地图，并且我们使用针对人口和排放情景的年份匹配的 RCP-SSP 框架创建了传播风险的空间明确的人口预测。
- Abstract: Dengue fever risk and burden has increased globally in the past decade, with record-breaking outbreaks driving high case numbers, outbreaks increasing in existing transmission suitable regions, and occurring in new locations. A combination of global change processes, including climate change, have provided the environmental backdrop for introductions and resurgences of mosquito-transmitted dengue virus. Understandin...
- Summary (fallback): 机器翻译摘要显示：过去十年中，全球登革热风险和负担不断增加，破纪录的疫情导致病例数量不断增加，现有适宜传播地区的疫情不断增加，并在新的地点发生。包括气候变化在内的全球变化过程的结合，为蚊子传播的登革热病毒的引入和死灰复燃提供了环境背景。了解暴露风险的变化是公共卫生准备工作不可或缺的一部分。这项研究通过一系列大气环流模型 (GCM) 提供了 CMIP6 气候情景下登革热传播的热适宜性的全球地图，并且我们使用针对人口和排放情景的年份匹配的 RCP-SSP 框架创建了传播风险的空间明确的人口预测。
- Keywords: transmission, suitability, risk, dengue, global

### 3. [盆底健康的知识和实践：国家田径队医务人员的横断面研究方案](https://www.medrxiv.org/content/10.1101/2025.09.16.25335684v2)
- Original title: Knowledge and practice toward pelvic floor health: a cross-sectional study protocol within the medical staff of national Athletics teams
- Authors: Giagio, S., Adami, P. E., Bermon, S., Rial-Rebullido, T., Turolla, A. et al.
- Meta: 2026-07-11 | sports medicine | DOI: 10.1101/2025.09.16.25335684
- 中文摘要: 目标。本研究旨在评估国家田径队医务人员与盆底 (PF) 健康相关的知识和实践。次要目标是 a) 探索不同个人、职业和背景特征的 PF 健康知识的差异； b) 检查个人临床实践和团队层面的 PF 健康方法是否会因亚组而异。方法。这项研究将是一项观察性横断面设计，采用基于网络的调查，在 2025 年 9 月至 2026 年 9 月的世界田径赛季期间进行。参与者将包括属于国家田径队医务人员的医疗保健专业人员，例如医生、物理治疗师、护士、营养师和其他专职医疗专业人员。
- Abstract: Objectives. This study will aim to assess the knowledge and practices related to pelvic floor (PF) health within the medical staff of national Athletics teams. Secondary objectives will be to a) explore differences in PF health knowledge across individual, professional, and contextual characteristics; b) examine whether individual clinical practices and team-level approaches toward PF health will vary across subgrou...
- Summary (fallback): 机器翻译摘要显示：目标。本研究旨在评估国家田径队医务人员与盆底 (PF) 健康相关的知识和实践。次要目标是 a) 探索不同个人、职业和背景特征的 PF 健康知识的差异； b) 检查个人临床实践和团队层面的 PF 健康方法是否会因亚组而异。方法。这项研究将是一项观察性横断面设计，采用基于网络的调查，在 2025 年 9 月至 2026 年 9 月的世界田径赛季期间进行。参与者将包括属于国家田径队医务人员的医疗保健专业人员，例如医生、物理治疗师、护士、营养师和其他专职医疗专业人员。
- Keywords: will, health, knowledge, athletics, medical

### 4. [绘制从肾乳头到膀胱的尿路感染的遗传易感性](https://www.medrxiv.org/content/10.64898/2026.07.07.26357417v1)
- Original title: Mapping Genetic Susceptibility to Urinary Tract Infection from Kidney Papilla to Bladder
- Authors: Xu, K., Khan, A., Shang, N., Zeng, W., Wang, C. et al.
- Meta: 2026-07-11 | genetic and genomic medicine | DOI: 10.64898/2026.07.07.26357417
- 中文摘要: 尿路感染（UTI）是最常见的细菌感染之一，但影响易感性的遗传因素仍然知之甚少。我们对复发性尿路感染进行了全基因组关联研究，涉及 1,860,836 名个体（213,869 例病例和 1,646,967 名对照）。我们鉴定了 36 个独立的非 HLA 全基因组显着基因座，编码肾上皮和免疫反应基因，并证明一些基因座具有性别特异性效应。综合功能注释、表达和蛋白质数量性状基因座共定位以及单细胞多组学分析表明，UTI 风险等位基因优先调节肾脏、输尿管和膀胱上皮细胞的基因表达。
- Abstract: Urinary tract infections (UTIs) are among the most common bacterial infections, yet the genetic factors influencing susceptibility remain poorly understood. We performed a genome-wide association study of recurrent UTI involving 1,860,836 individuals (213,869 cases and 1,646,967 controls). We identified 36 independent non-HLA genome-wide significant loci encoding kidney epithelial and immune response genes and demon...
- Summary (fallback): 机器翻译摘要显示：尿路感染（UTI）是最常见的细菌感染之一，但影响易感性的遗传因素仍然知之甚少。我们对复发性尿路感染进行了全基因组关联研究，涉及 1,860,836 名个体（213,869 例病例和 1,646,967 名对照）。我们鉴定了 36 个独立的非 HLA 全基因组显着基因座，编码肾上皮和免疫反应基因，并证明一些基因座具有性别特异性效应。综合功能注释、表达和蛋白质数量性状基因座共定位以及单细胞多组学分析表明，UTI 风险等位基因优先调节肾脏、输尿管和膀胱上皮细胞的基因表达。
- Keywords: epithelial, urinary, kidney, tract, loci

### 5. [使用体内 MRI 和数据驱动的疾病进展模型对痴呆进行跨诊断定量评估：阿尔茨海默病和路易体痴呆的案例研究](https://www.medrxiv.org/content/10.1101/2025.10.03.25337171v2)
- Original title: Transdiagnostic quantitative assessment of dementias using in vivo MRI and data-driven disease progression modelling: a case study in Alzheimer's disease and dementia with Lewy bodies
- Authors: Castro Leal, G., Konuri, A., Young, A. L., Zebarjadi, N., Samantaray, T. et al.
- Meta: 2026-07-11 | neurology | DOI: 10.1101/2025.10.03.25337171
- 中文摘要: 简介：阿尔茨海默病 (AD) 和路易体病会导致脑萎缩，产生具有共同临床症状的痴呆综合征。我们假设这些疾病呈现出不同的萎缩模式，从而使疾病进展建模方法可用于生物分期。方法：利用来自六个国际队列的磁共振成像 (MRI) 扫描的特征，我们对阿尔茨海默病痴呆 (ADD) 和路易体痴呆 (DLB) 诊断患者的脑容量数据应用疾病进展亚型和阶段建模。我们评估了与发现的萎缩亚型的临床、生物标志物和组织病理学关联。结果：我们确定了三种数据驱动的跨综合征脑萎缩亚型，可以支持体内生物学诊断：边缘系统、皮质-边缘系统和皮质。
- Abstract: INTRODUCTION: Alzheimer's disease (AD) and Lewy body disease cause brain atrophy producing dementia syndromes with shared clinical symptoms. We hypothesise that those diseases present with differential atrophy patterns, thus making disease progression modelling methods useful for biological staging. METHODS: Using features derived from magnetic resonance imaging (MRI) scans from six international cohorts, we applied...
- Summary (fallback): 机器翻译摘要显示：简介：阿尔茨海默病 (AD) 和路易体病会导致脑萎缩，产生具有共同临床症状的痴呆综合征。我们假设这些疾病呈现出不同的萎缩模式，从而使疾病进展建模方法可用于生物分期。方法：利用来自六个国际队列的磁共振成像 (MRI) 扫描的特征，我们对阿尔茨海默病痴呆 (ADD) 和路易体痴呆 (DLB) 诊断患者的脑容量数据应用疾病进展亚型和阶段建模。我们评估了与发现的萎缩亚型的临床、生物标志物和组织病理学关联。结果：我们确定了三种数据驱动的跨综合征脑萎缩亚型，可以支持体内生物学诊断：边缘系统、皮质-边缘系统和皮质。
- Keywords: disease, dementia, atrophy, vivo, data-driven

### 6. [前女足球运动员的认知和行为功能：头部撞击和创伤监测研究 (HITSS) 的结果](https://www.medrxiv.org/content/10.64898/2026.02.25.26347083v2)
- Original title: Cognitive and Behavioral Functioning in Female Former Soccer Players: Results from the Head Impact and Trauma Surveillance Study (HITSS)
- Authors: Mulayi, S. C., Aaronson, A., Goostrey, K. J., Tuz-Zahra, F., Tripodis, Y. et al.
- Meta: 2026-07-11 | neurology | DOI: 10.64898/2026.02.25.26347083
- 中文摘要: 接触和碰撞运动造成的重复性头部撞击 (RHI) 与晚年认知和神经行为障碍以及慢性创伤性脑病 (CTE) 等神经退行性疾病有关。具体而言，女性前足球运动员中与 RHI 相关的临床后遗症尚不清楚。这项横断面研究旨在调查 2,732 名年龄在 40 岁或以上、参加了头部撞击和创伤监测研究 (HITSS) 的女性（所有这些女性都曾经参加过有组织的足球比赛）中 RHI 暴露指标（例如，踢足球的总年数、脑震荡历史、最高比赛水平和估计的累积头球频率）与临床指标（例如，主观认知抱怨、客观认知表现、行为失调和抑郁症状）之间的关系。
- Abstract: Repetitive head impacts (RHI) from contact and collision sports have been associated with later-life cognitive and neurobehavioral impairments, as well as neurodegenerative conditions such as chronic traumatic encephalopathy (CTE). RHI-associated clinical sequelae among female former soccer players, specifically, are not well understood. This cross-sectional study aimed to examine the relationship of RHI exposure pr...
- Summary (fallback): 机器翻译摘要显示：接触和碰撞运动造成的重复性头部撞击 (RHI) 与晚年认知和神经行为障碍以及慢性创伤性脑病 (CTE) 等神经退行性疾病有关。具体而言，女性前足球运动员中与 RHI 相关的临床后遗症尚不清楚。这项横断面研究旨在调查 2,732 名年龄在 40 岁或以上、参加了头部撞击和创伤监测研究 (HITSS) 的女性（所有这些女性都曾经参加过有组织的足球比赛）中 RHI 暴露指标（例如，踢足球的总年数、脑震荡历史、最高比赛水平和估计的累积头球频率）与临床指标（例如，主观认知抱怨、客观认知表现、行为失调和抑郁症状）之间的关系。
- Keywords: cognitive, soccer, behavioral, play, former
