# daily2rxiv Digest - 2026-07-11

共收录 60 篇论文。

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

### 1. [通过基因组基础模型嵌入进行可解释的变异效应预测](https://www.biorxiv.org/content/10.64898/2026.04.10.717844v4)
- Original title: Interpretable variant effect prediction from genomic foundation model embeddings
- Authors: Pearce, M. T., Dooms, T., Yamamoto, R., Ayanian, S., Ryu, A. et al.
- Meta: 2026-07-11 | genomics | DOI: 10.64898/2026.04.10.717844
- 中文摘要: 科学基础模型从不同的数据模式中学习高维表示，但它们编码的内容以及如何提取这些知识仍然是悬而未决的问题。在这里，我们表明，探索 Evo 2（一个 70 亿参数的基因组基础模型）的内部表示可以实现准确且可解释的遗传变异效应预测。我们引入了一种基于协方差的探针，它可以从 Evo 2 序列嵌入中捕获二阶结构，以预测跨变异类型和功能后果的变异致病性，匹配或超过其域内的专门预测因子。为了将这些预测建立在已知的生物机制上，我们在现有注释上训练了一组互补的探针，以检测哪些基因组特性被变体破坏。
- Abstract: Scientific foundation models learn high-dimensional representations from diverse data modalities, yet what they encode and how to extract that knowledge remain open questions. Here we show that probing the internal representations of Evo 2, a 7-billion-parameter genomic foundation model, enables accurate and interpretable genetic variant effect prediction. We introduce a covariance-based probe that captures second-o...
- Summary (fallback): 机器翻译摘要显示：科学基础模型从不同的数据模式中学习高维表示，但它们编码的内容以及如何提取这些知识仍然是悬而未决的问题。在这里，我们表明，探索 Evo 2（一个 70 亿参数的基因组基础模型）的内部表示可以实现准确且可解释的遗传变异效应预测。我们引入了一种基于协方差的探针，它可以从 Evo 2 序列嵌入中捕获二阶结构，以预测跨变异类型和功能后果的变异致病性，匹配或超过其域内的专门预测因子。为了将这些预测建立在已知的生物机制上，我们在现有注释上训练了一组互补的探针，以检测哪些基因组特性被变体破坏。
- Keywords: variant, genomic, foundation, effect, model

### 2. [scDiagnostics：单细胞转录组数据中细胞类型注释的系统评估](https://www.biorxiv.org/content/10.64898/2026.01.29.701618v2)
- Original title: scDiagnostics: systematic assessment of cell type annotation in single-cell transcriptomics data
- Authors: Christidis, A., Ghazi, A. R., Chawla, S., Turaga, N., Gentleman, R. et al.
- Meta: 2026-07-11 | bioinformatics | DOI: 10.64898/2026.01.29.701618
- 中文摘要: 尽管细胞类型注释已成为单细胞分析工作流程不可或缺的一部分，但计算注释的评估仍然具有挑战性。许多注释工具将标签从带注释的参考数据集转移到感兴趣的新查询数据集，但盲目地将标签从一个数据集转移到另一个数据集有其自身的一系列挑战。数据集之间通常不存在完美的对齐，特别是当从健康参考图谱转移注释以发现疾病状态时。我们推出了 scDiagnostics，这是一种新的开源软件包，有助于检测复杂或模糊的注释情况，否则这些情况可能会被忽视，从而解决当前单细胞分析工作流程中未满足的关键需求。 scDiagnostics 配备了与所有主要细胞类型注释工具兼容的新型诊断方法。
- Abstract: Although cell type annotation has become an integral part of single-cell analysis workflows, the assessment of computational annotations remains challenging. Many annotation tools transfer labels from an annotated reference dataset to a new query dataset of interest, but blindly transferring labels from one dataset to another has its own set of challenges. Often enough there is no perfect alignment between datasets,...
- Summary (fallback): 机器翻译摘要显示：尽管细胞类型注释已成为单细胞分析工作流程不可或缺的一部分，但计算注释的评估仍然具有挑战性。许多注释工具将标签从带注释的参考数据集转移到感兴趣的新查询数据集，但盲目地将标签从一个数据集转移到另一个数据集有其自身的一系列挑战。数据集之间通常不存在完美的对齐，特别是当从健康参考图谱转移注释以发现疾病状态时。我们推出了 scDiagnostics，这是一种新的开源软件包，有助于检测复杂或模糊的注释情况，否则这些情况可能会被忽视，从而解决当前单细胞分析工作流程中未满足的关键需求。 scDiagnostics 配备了与所有主要细胞类型注释工具兼容的新型诊断方法。
- Keywords: scdiagnostics, annotation, single-cell, annotations, cell

### 3. [IGF1 肽靶向雷特综合征星形胶质细胞，降解 IGF 结合蛋白，挽救突触发生并恢复线粒体功能](https://www.biorxiv.org/content/10.64898/2026.01.22.701190v2)
- Original title: IGF1 peptide targets Rett Syndrome astrocytes to degrade IGF binding protein, rescue synaptogenesis and restore mitochondrial function
- Authors: Ojha, P., Kozareva, V., Barlowe, A., Schulte, F., Lam, R. M. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.01.22.701190
- 中文摘要: 雷特综合征 (RTT) 是一种由 MECP2 突变引起的严重神经发育障碍，会导致大脑中严重的突触和回路缺陷。虽然神经元历来是 RTT 病理学的焦点，但新出现的证据表明星形胶质细胞参与损害突触结构、功能和发育的非细胞自主机制。在这里，我们发现了星形胶质细胞分泌的 IGFBP2 在介导这些缺陷中的核心作用，并证明用 IGF1 衍生肽治疗可通过促进 IGFBP2 降解来恢复突触形成。使用间接星形胶质细胞-神经元共培养系统，我们发现来自RTT模型小鼠的星形胶质细胞抑制野生型神经元的兴奋性突触形成，并且当RTT星形胶质细胞用IGF1(1-3)肽处理时，这种损害被逆转。
- Abstract: Rett syndrome (RTT), a severe neurodevelopmental disorder caused by mutations in MECP2, leads to profound synaptic and circuit deficits in the brain. While neurons have historically been the focus of RTT pathology, emerging evidence implicates astrocytes in non-cell autonomous mechanisms that impair synaptic structure, function and development. Here, we uncover a central role for astrocyte-secreted IGFBP2 in mediati...
- Summary (fallback): 机器翻译摘要显示：雷特综合征 (RTT) 是一种由 MECP2 突变引起的严重神经发育障碍，会导致大脑中严重的突触和回路缺陷。虽然神经元历来是 RTT 病理学的焦点，但新出现的证据表明星形胶质细胞参与损害突触结构、功能和发育的非细胞自主机制。在这里，我们发现了星形胶质细胞分泌的 IGFBP2 在介导这些缺陷中的核心作用，并证明用 IGF1 衍生肽治疗可通过促进 IGFBP2 降解来恢复突触形成。使用间接星形胶质细胞-神经元共培养系统，我们发现来自RTT模型小鼠的星形胶质细胞抑制野生型神经元的兴奋性突触形成，并且当RTT星形胶质细胞用IGF1(1-3)肽处理时，这种损害被逆转。
- Keywords: igf1, peptide, astrocytes, igfbp2, function

### 4. [将单细胞转录组标记为大型语言模型的母语](https://www.biorxiv.org/content/10.1101/2025.10.22.684047v2)
- Original title: Tokenizing single-cell transcriptomes as a native language for large language models
- Authors: Xiao, C., Ding, Y., Bian, H., Chen, Y., Wei, L. et al.
- Meta: 2026-07-11 | bioinformatics | DOI: 10.1101/2025.10.22.684047
- 中文摘要: 一旦大型语言模型（LLM）在共享序列空间中表示为标记，就可以处理多种形式的信息。然而，单细胞转录组对于法学硕士来说仍然是一种外来模式，因为它们是连续的、高维的分子谱，而不是离散的语言单元。在这里，我们提出了 CellTok，一种标记化的单细胞语言建模方法，可将转录组图谱转换为紧凑的细胞标记序列，并将它们合并到预训练的法学硕士的词汇中。通过将细胞表示为原生标记，CellTok 能够在同一自回归建模框架内联合处理细胞测量、文本指令、生物背景和多细胞群体。
- Abstract: Large language models (LLMs) can process diverse forms of information once they are represented as tokens in a shared sequence space. However, single-cell transcriptomes remain a foreign modality to LLMs because they are continuous, high-dimensional molecular profiles rather than discrete linguistic units. Here, we propose CellTok, a tokenized single-cell language modeling approach that converts transcriptomic profi...
- Summary (fallback): 机器翻译摘要显示：一旦大型语言模型（LLM）在共享序列空间中表示为标记，就可以处理多种形式的信息。然而，单细胞转录组对于法学硕士来说仍然是一种外来模式，因为它们是连续的、高维的分子谱，而不是离散的语言单元。在这里，我们提出了 CellTok，一种标记化的单细胞语言建模方法，可将转录组图谱转换为紧凑的细胞标记序列，并将它们合并到预训练的法学硕士的词汇中。通过将细胞表示为原生标记，CellTok 能够在同一自回归建模框架内联合处理细胞测量、文本指令、生物背景和多细胞群体。
- Keywords: language, cellular, single-cell, llms, celltok

### 5. [TNFR2 激动剂作为针对新型骨关节炎引起的心脏功能障碍的性别特异性疗法](https://www.biorxiv.org/content/10.64898/2026.07.06.736778v2)
- Original title: TNFR2 Agonism as a Sex-Specific Therapy for Novel Osteoarthritis-Induced Cardiac Dysfunction
- Authors: Prasoon, P., Tammen, K., Russo, R., Meyyappan, A., Dalvi, M. et al.
- Meta: 2026-07-11 | physiology | DOI: 10.64898/2026.07.06.736778
- 中文摘要: 骨关节炎 (OA) 是一种退行性关节疾病，与全身炎症增加、慢性疼痛和心血管功能障碍有关。流行病学证据表明，OA 会使心血管疾病 (CVD) 的风险增加三倍，但 OA 的因果作用仍未得到充分研究。我们纵向评估了内侧半月板（DMM）手术不稳定以诱发小鼠骨关节炎后的心脏功能。 DMM 小鼠的超声心动图参数表现出显着的性别二态性改变。
- Abstract: Osteoarthritis (OA), a degenerative joint disease, is associated with increased systemic inflammation, chronic pain, and cardiovascular dysfunction. Epidemiological evidence establishes that OA increases the risk of cardiovascular disease (CVD) threefold, yet the causal role of OA contributions remains underexamined. We assessed cardiac function longitudinally following destabilization of the medial meniscus (DMM) s...
- Summary (fallback): 机器翻译摘要显示：骨关节炎 (OA) 是一种退行性关节疾病，与全身炎症增加、慢性疼痛和心血管功能障碍有关。流行病学证据表明，OA 会使心血管疾病 (CVD) 的风险增加三倍，但 OA 的因果作用仍未得到充分研究。我们纵向评估了内侧半月板（DMM）手术不稳定以诱发小鼠骨关节炎后的心脏功能。 DMM 小鼠的超声心动图参数表现出显着的性别二态性改变。
- Keywords: dysfunction, mice, cardiac, tnfr2, cardiovascular

### 6. [晚熟，但并非罕见：人类发育时间遵循一般哺乳动物的生活史尺度](https://www.biorxiv.org/content/10.64898/2026.06.16.732383v2)
- Original title: Altricial, but not unusual: Human developmental timing follows general mammalian life-history scaling
- Authors: Akcan, C. D., Kece, D., Kerman, K.
- Meta: 2026-07-11 | zoology | DOI: 10.64898/2026.06.16.732383
- 中文摘要: 人们普遍认为人类发育异常缓慢，童年期延长，对照顾者的依赖也很长。然而，这种观点主要基于与其他灵长类动物的比较，因此人类是否在更广泛的哺乳动物多样性中保持独特性仍悬而未决。我们通过将人类发育置于一个比较框架中来解决这个问题，该比较框架使用了代表 25 个目的 462 种哺乳动物的妊娠长度、断奶年龄和性成熟年龄。每个性状都以绝对值和最长已验证圈养寿命的比例进行了检查。从绝对值来看，人类发育特征属于哺乳动物变异的上限。
- Abstract: Humans are widely regarded as unusually slow to develop, exhibiting prolonged childhood and extended dependence on caregivers. However, this view is based primarily on comparisons with other primates, leaving unresolved whether humans remain distinctive within the broader diversity of mammals. We addressed this question by situating human development in a comparative framework using gestation length, weaning age, an...
- Summary (fallback): 机器翻译摘要显示：人们普遍认为人类发育异常缓慢，童年期延长，对照顾者的依赖也很长。然而，这种观点主要基于与其他灵长类动物的比较，因此人类是否在更广泛的哺乳动物多样性中保持独特性仍悬而未决。我们通过将人类发育置于一个比较框架中来解决这个问题，该比较框架使用了代表 25 个目的 462 种哺乳动物的妊娠长度、断奶年龄和性成熟年龄。每个性状都以绝对值和最长已验证圈养寿命的比例进行了检查。从绝对值来看，人类发育特征属于哺乳动物变异的上限。
- Keywords: human, mammalian, developmental, timing, follows

### 7. [肠系膜神经元和回肠肌间神经元之间的双向通讯](https://www.biorxiv.org/content/10.64898/2026.07.04.736073v2)
- Original title: Bidirectional communication between neurons in the mesentery and ileal myenteric neurons
- Authors: Vanden Berghe, P., Guo, F., Van Mechelen, K., Li, Z., Fung, C.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.04.736073
- 中文摘要: 肠系膜最近被归类为“新”器官，含有多种细胞类型，包括脂肪细胞、前脂肪细胞、内皮细胞和免疫细胞。此外，神经元细胞体存在于小肠系膜中，并且单独或与靠近肠壁的小神经节结构中的神经胶质细胞聚集在一起。然而，人们对这些肠外肠系膜神经元的起源或功能知之甚少。本研究的目的是更好地表征肠系膜神经元，并使用附有肠系膜的成年小鼠回肠钙成像检查它们与 ENS 的连接性。在这里，我们证明肠系膜中的神经元表达典型的 ENS 神经化学标记物，对 5-HT、ATP 和烟碱激动剂 DMPP 做出反应，并接收烟碱突触输入。
- Abstract: The intestinal mesentery has been recently classified as a 'new' organ and contains various cell types including adipocytes, preadipocytes, endothelial cells, and immune cells. In addition, neuronal cell bodies are found in the small intestinal mesentery and are situated either individually or clustered together with glial cells in small ganglion structures close to the gut wall. However, little is known about the o...
- Summary (fallback): 机器翻译摘要显示：肠系膜最近被归类为“新”器官，含有多种细胞类型，包括脂肪细胞、前脂肪细胞、内皮细胞和免疫细胞。此外，神经元细胞体存在于小肠系膜中，并且单独或与靠近肠壁的小神经节结构中的神经胶质细胞聚集在一起。然而，人们对这些肠外肠系膜神经元的起源或功能知之甚少。本研究的目的是更好地表征肠系膜神经元，并使用附有肠系膜的成年小鼠回肠钙成像检查它们与 ENS 的连接性。在这里，我们证明肠系膜中的神经元表达典型的 ENS 神经化学标记物，对 5-HT、ATP 和烟碱激动剂 DMPP 做出反应，并接收烟碱突触输入。
- Keywords: neurons, mesentery, intestinal, mesenteric, myenteric

### 8. [自发眨眼作为内部注意力的时间标记](https://www.biorxiv.org/content/10.64898/2026.07.06.736774v2)
- Original title: Spontaneous eye blinks as temporal markers of internal attention
- Authors: Schneider, D., Oezdemir, S., Wascher, E., Arnau, S.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.06.736774
- 中文摘要: 眨眼是脑电图中最大的生理伪影之一，通常会从记录中删除。然而它们的时间可能携带着有关认知的信息。在这里，我们询问试验中自发眨眼的时间分布是否提供了工作记忆中内部注意力集中的时间分辨行为特征。在实验 1 中，眨眼锁定脑电图分析表明，眨眼时间与神经活动一致，反映了注意力集中在相关的内部表征上。在实验 2 中，参与者在不同条件下记住了相同的视觉信息，但相关项目要么在存储过程中早期被提示，要么在稍后出现记忆探针时被提示。眨眼频率曲线相应地发生变化，当选择可能较早时在提示后增加，当选择延迟时在探测后增加。
- Abstract: Eye blinks are among the largest physiological artefacts in electroencephalography and are typically removed from the recordings. Yet their timing may carry information about cognition. Here, we asked whether the temporal distribution of spontaneous blinks across trials provides a time-resolved behavioural signature of internal attentional focusing in working memory. In Experiment 1, blink-locked EEG analyses showed...
- Summary (fallback): 机器翻译摘要显示：眨眼是脑电图中最大的生理伪影之一，通常会从记录中删除。然而它们的时间可能携带着有关认知的信息。在这里，我们询问试验中自发眨眼的时间分布是否提供了工作记忆中内部注意力集中的时间分辨行为特征。在实验 1 中，眨眼锁定脑电图分析表明，眨眼时间与神经活动一致，反映了注意力集中在相关的内部表征上。在实验 2 中，参与者在不同条件下记住了相同的视觉信息，但相关项目要么在存储过程中早期被提示，要么在稍后出现记忆探针时被提示。眨眼频率曲线相应地发生变化，当选择可能较早时在提示后增加，当选择延迟时在探测后增加。
- Keywords: blinks, spontaneous, internal, memory, temporal

### 9. [腹侧被盖区乙酰胆碱产生食欲和厌恶的激励动机](https://www.biorxiv.org/content/10.64898/2026.07.09.737546v1)
- Original title: Ventral tegmental area acetylcholine generates appetitive and aversive incentive motivation
- Authors: Savatdy, S. G., Ye, L., Serrano Colon, N., Russell, G. A., Miller, S. R. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.09.737546
- 中文摘要: 腹侧被盖区神经元参与奖励学习、动机和运动，但在厌恶行为的调节中也发挥着新兴作用。虽然这些不同的贡献归因于腹侧被盖区神经元的不同投射，但这些神经元如何继承其一系列行为功能仍然悬而未决。腹侧被盖区富含乙酰胆碱受体，并接收来自中脑桥被盖的密集胆碱能输入。虽然已知腹侧被盖区乙酰胆碱释放可以增加多巴胺输出，但我们对需要腹侧被盖区乙酰胆碱释放的情况缺乏了解。我们试图全面概述腹侧被盖区乙酰胆碱信号传导跨价到动机行为的参与。
- Abstract: Ventral tegmental area neurons participate in reward learning, motivation, and movement but also have an emerging role in the regulation of aversive behaviors. While these diverse contributions have been attributed to distinct projections of ventral tegmental area neurons, it remains unresolved how these neurons inherit their array of behavioral functions. The ventral tegmental area is rich with acetylcholine recept...
- Summary (fallback): 机器翻译摘要显示：腹侧被盖区神经元参与奖励学习、动机和运动，但在厌恶行为的调节中也发挥着新兴作用。虽然这些不同的贡献归因于腹侧被盖区神经元的不同投射，但这些神经元如何继承其一系列行为功能仍然悬而未决。腹侧被盖区富含乙酰胆碱受体，并接收来自中脑桥被盖的密集胆碱能输入。虽然已知腹侧被盖区乙酰胆碱释放可以增加多巴胺输出，但我们对需要腹侧被盖区乙酰胆碱释放的情况缺乏了解。我们试图全面概述腹侧被盖区乙酰胆碱信号传导跨价到动机行为的参与。
- Keywords: ventral, tegmental, area, acetylcholine, neurons

### 10. [以自我为中心的空间支架组织皮质记忆印迹](https://www.biorxiv.org/content/10.64898/2026.07.09.737550v1)
- Original title: Egocentric spatial scaffolds organize cortical memory engrams
- Authors: Yeo, Y., Na, W., Kwag, J.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.09.737550
- 中文摘要: 情景记忆需要在记忆的环境中重建自我的位置，但记忆印迹是否以及如何结合自我参考的空间信息仍然未知。使用活动依赖性印迹标记、纵向钙成像和压后皮质的光遗传学扰动，我们发现皮层记忆印迹丰富了自我中心和边界编码神经元，这些神经元编码相对于环境边界的自我位置。纵向成像显示，未来的印迹神经元优先从预先存在的空间支架中招募，而不是在学习过程中从头生成。在记忆检索过程中，支架群体经历了协调的细化，并短暂地重组为支架印迹网络状态，其动态跟踪记忆表达。
- Abstract: Episodic memory requires reconstructing the position of the self within a remembered environment, yet whether and how memory engrams incorporate self-referenced spatial information remains unknown. Using activity dependent-engram tagging, longitudinal calcium imaging and optogenetic perturbation in the retrosplenial cortex, we found that cortical memory engrams are enriched for egocentric and boundary coding neurons...
- Summary (fallback): 机器翻译摘要显示：情景记忆需要在记忆的环境中重建自我的位置，但记忆印迹是否以及如何结合自我参考的空间信息仍然未知。使用活动依赖性印迹标记、纵向钙成像和压后皮质的光遗传学扰动，我们发现皮层记忆印迹丰富了自我中心和边界编码神经元，这些神经元编码相对于环境边界的自我位置。纵向成像显示，未来的印迹神经元优先从预先存在的空间支架中招募，而不是在学习过程中从头生成。在记忆检索过程中，支架群体经历了协调的细化，并短暂地重组为支架印迹网络状态，其动态跟踪记忆表达。
- Keywords: memory, spatial, engrams, neurons, scaffold

### 11. [成年抑制神经元中钙结合蛋白的上调重新激活小鼠视觉皮层的关键期可塑性](https://www.biorxiv.org/content/10.64898/2026.07.08.737337v1)
- Original title: Upregulation of Calbindin in Adult Inhibitory Neurons Reactivates Critical Period Plasticity in Mouse Visual Cortex
- Authors: Nakayama, T., Figueroa-Velez, D., England, W., Miyoshi, E., Hasselmann, J. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.08.737337
- 中文摘要: 关键时期是学习表现达到顶峰的时期，突触可塑性的增强使得青少年大脑回路能够快速、稳健地重组。与成年人的可塑性不同，成人的可塑性需要感官体验的持续、持久的变化，而皮质表征可以在关键时期迅速改变，并产生持久的影响。 GABA 能抑制性神经元的移植已被证明可以通过触发宿主抑制性神经元内的信号变化来恢复受体回路的关键期可塑性。在这里，我们对小鼠初级视觉皮层（V1）中的宿主抑制性神经元进行转录分析，以检测移植诱导的可塑性期间的基因表达变化。对宿主抑制性神经元中差异表达（DE）转录本的基因本体富集分析揭示了突触可塑性和抑制性神经元发育相关的特征。
- Abstract: Critical periods are windows of peak learning performance where heightened synaptic plasticity enables fast, robust reorganization in juvenile brain circuits. Unlike adult plasticity which requires ongoing, persistent change in sensory experience, cortical representations can be rapidly changed during critical periods and have enduring effects. Transplantation of GABAergic inhibitory neurons has been shown to restor...
- Summary (fallback): 机器翻译摘要显示：关键时期是学习表现达到顶峰的时期，突触可塑性的增强使得青少年大脑回路能够快速、稳健地重组。与成年人的可塑性不同，成人的可塑性需要感官体验的持续、持久的变化，而皮质表征可以在关键时期迅速改变，并产生持久的影响。 GABA 能抑制性神经元的移植已被证明可以通过触发宿主抑制性神经元内的信号变化来恢复受体回路的关键期可塑性。在这里，我们对小鼠初级视觉皮层（V1）中的宿主抑制性神经元进行转录分析，以检测移植诱导的可塑性期间的基因表达变化。对宿主抑制性神经元中差异表达（DE）转录本的基因本体富集分析揭示了突触可塑性和抑制性神经元发育相关的特征。
- Keywords: plasticity, inhibitory, neurons, critical, expression

### 12. [灵活的神经元参与可靠的运动序列](https://www.biorxiv.org/content/10.64898/2026.07.10.737866v1)
- Original title: Flexible neuronal participation within a reliable motor sequence
- Authors: Peng, J., Duffy, A., Dippenaar, I., Liu, L., Wu, J. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.10.737866
- 中文摘要: 学习的运动序列的可靠执行提出了一个挑战：它们需要可重复的神经元活动模式来实现行为一致性，但必须保留依赖于内部状态和对外部突发事件的适应的调节灵活性。斑胸草雀是一种鸣鸟，它为研究这个问题提供了一个理想的系统，因为它们的发声是高度刻板的，并且与 HVC 中精确时间锁定的爆发相关，而 HVC 是参与歌曲产生的关键核心。然而，他们的歌曲并不是一成不变的/完全固定的，因为它们可以在社交互动过程中进行调整，并且可以在大脑损伤后恢复。在这里，我们在自由创作歌曲期间使用 HVC 投射神经元的钙成像来跟踪同一首歌曲从几秒到几周的重复演绎中的活动。我们首先确认了歌曲锁定的钙事件时间在几天内是稳定的。
- Abstract: The reliable execution of learned motor sequences poses a challenge: they require reproducible neuron activity patterns for behavioral consistency yet must retain flexibility for modulation that depend on internal states and adaptation to external contingencies. The zebra finch, a songbird, provides an ideal system to examine this problem because their vocalizations are highly stereotyped and are associated with pre...
- Summary (fallback): 机器翻译摘要显示：学习的运动序列的可靠执行提出了一个挑战：它们需要可重复的神经元活动模式来实现行为一致性，但必须保留依赖于内部状态和对外部突发事件的适应的调节灵活性。斑胸草雀是一种鸣鸟，它为研究这个问题提供了一个理想的系统，因为它们的发声是高度刻板的，并且与 HVC 中精确时间锁定的爆发相关，而 HVC 是参与歌曲产生的关键核心。然而，他们的歌曲并不是一成不变的/完全固定的，因为它们可以在社交互动过程中进行调整，并且可以在大脑损伤后恢复。在这里，我们在自由创作歌曲期间使用 HVC 投射神经元的钙成像来跟踪同一首歌曲从几秒到几周的重复演绎中的活动。我们首先确认了歌曲锁定的钙事件时间在几天内是稳定的。
- Keywords: participation, motor, song, stable, songs

### 13. [MEG 信息导航 TMS 用于个性化语音皮质映射](https://www.biorxiv.org/content/10.64898/2026.07.10.737657v1)
- Original title: MEG-informed navigated TMS for individualized speech cortical mapping
- Authors: Autti, S., Korkealaakso, S., Gogulski, J., Engelhardt, M., Vaalto, S. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.10.737657
- 中文摘要: 通过导航重复经颅磁刺激 (SCM nrTMS) 进行语音皮质映射，为神经外科医生提供有关个体皮质语音网络的非侵入性先验信息。需要个性化映射，因为语音产生的确切位置和激活模式显示出个体之间的高度可变性。我们假设，个人言语产生的脑磁图 (MEG) 数据可以在时间和空间上指导 SCM TMS 过程，从而导致在 MEG 定义的位置（TMS 脉冲时序与 MEG 活动一致）出现更高的错误率。 13 名健康受试者参与了 MEG 和 TMS 测量，其中 TMS 脉冲的时间（PTI；图片到 TMS 间隔）根据个人在图片命名任务中的 MEG 激活进行调整。
- Abstract: Speech cortical mapping by means of navigated repetitive transcranial magnetic stimulation (SCM nrTMS) provides neurosurgeons with noninvasive prior information about individual's cortical speech network. Individualized mapping is required, since the exact locations and activation patterns of speech production show high variability between individuals. We hypothesized that magnetoencephalography (MEG) data of an ind...
- Summary (fallback): 机器翻译摘要显示：通过导航重复经颅磁刺激 (SCM nrTMS) 进行语音皮质映射，为神经外科医生提供有关个体皮质语音网络的非侵入性先验信息。需要个性化映射，因为语音产生的确切位置和激活模式显示出个体之间的高度可变性。我们假设，个人言语产生的脑磁图 (MEG) 数据可以在时间和空间上指导 SCM TMS 过程，从而导致在 MEG 定义的位置（TMS 脉冲时序与 MEG 活动一致）出现更高的错误率。 13 名健康受试者参与了 MEG 和 TMS 测量，其中 TMS 脉冲的时间（PTI；图片到 TMS 间隔）根据个人在图片命名任务中的 MEG 激活进行调整。
- Keywords: speech, individual, activation, error, cortical

### 14. [注意力重塑丘脑和皮质预测误差学习的信息动态](https://www.biorxiv.org/content/10.64898/2026.07.10.737794v1)
- Original title: Attention reshapes the information dynamics of thalamic and cortical prediction-error learning
- Authors: Aijala, J., Jensen, M. A., Miller, K. J., Hermes, D., Blenkmann, A. O. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.10.737794
- 中文摘要: 预测误差（PE）通过更新感觉环境的内部模型来驱动感知学习，但目前尚不清楚注意力如何在分布式丘脑皮质回路中重塑它们的表征。使用 17 名患者的颅内立体脑电图 (sEEG)，在有人值守和无人值守的条件下执行巡回听觉奇怪任务，我们使用互信息和共信息来量化 PE 编码，以捕获冗余和协同的 PE 表示。丘脑和颞叶皮层中的注意力调节 PE 编码，但具有不同的信息动态。丘脑编码显示在注意力分散期间 PE 信息稳定减少，这与状态依赖性丘脑皮质门控一致。
- Abstract: Prediction errors (PEs) drive perceptual learning by updating internal models of the sensory environment, yet it remains unclear how attention reshapes their representation across distributed thalamocortical circuits. Using intracranial stereoelectroencephalography (sEEG) from 17 patients performing a roving auditory oddball task under attended and unattended conditions, we quantified PE encoding using mutual inform...
- Summary (fallback): 机器翻译摘要显示：预测误差（PE）通过更新感觉环境的内部模型来驱动感知学习，但目前尚不清楚注意力如何在分布式丘脑皮质回路中重塑它们的表征。使用 17 名患者的颅内立体脑电图 (sEEG)，在有人值守和无人值守的条件下执行巡回听觉奇怪任务，我们使用互信息和共信息来量化 PE 编码，以捕获冗余和协同的 PE 表示。丘脑和颞叶皮层中的注意力调节 PE 编码，但具有不同的信息动态。丘脑编码显示在注意力分散期间 PE 信息稳定减少，这与状态依赖性丘脑皮质门控一致。
- Keywords: attention, learning, information, dynamics, cortical

### 15. [对神经音乐处理的自上而下的影响：偏好、享受和熟悉程度以不同方式影响神经跟踪和大脑节律](https://www.biorxiv.org/content/10.64898/2026.07.10.737714v1)
- Original title: Top-down influences on neural music processing: preference, enjoyment and familiarity influence neural tracking and brain rhythms differently
- Authors: Varjopuro, S. M., Timmerman, R. H., Atanasova, T., Allen, S. C., Koukouvinis, S. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.10.737714
- 中文摘要: 音乐享受和熟悉程度密切相关，但在神经音乐处理的研究中经常混淆。在这里，我们使用脑电图（EEG）研究了它们对皮质振荡活动和音乐神经跟踪的独特贡献。三十二名参与者听了自选的一直以来最喜欢的歌曲、最近最喜欢的歌曲以及不喜欢的类型中节奏匹配的歌曲。这种新颖的范式通过包含熟悉度不同的高度欣赏的歌曲，将熟悉度与享受分离。使用具有享受度和熟悉度评级的线性混合效应模型来分析光谱功率和皮质跟踪（使用互信息）。熟悉感与左额叶 α 功率增加有关，而享受则预示着 θ 和 β 功率增加，这表明这些维度具有独特的振荡特征。
- Abstract: Music enjoyment and familiarity are closely related but often confounded in studies of neural music processing. Here, we investigated their distinct contributions to cortical oscillatory activity and neural tracking of music using electroencephalography (EEG). Thirty-two participants listened to self-selected all-time favourite songs, recent favourite songs, and tempo-matched songs from disliked genres. This novel p...
- Summary (fallback): 机器翻译摘要显示：音乐享受和熟悉程度密切相关，但在神经音乐处理的研究中经常混淆。在这里，我们使用脑电图（EEG）研究了它们对皮质振荡活动和音乐神经跟踪的独特贡献。三十二名参与者听了自选的一直以来最喜欢的歌曲、最近最喜欢的歌曲以及不喜欢的类型中节奏匹配的歌曲。这种新颖的范式通过包含熟悉度不同的高度欣赏的歌曲，将熟悉度与享受分离。使用具有享受度和熟悉度评级的线性混合效应模型来分析光谱功率和皮质跟踪（使用互信息）。熟悉感与左额叶 α 功率增加有关，而享受则预示着 θ 和 β 功率增加，这表明这些维度具有独特的振荡特征。
- Keywords: enjoyment, music, familiarity, neural, songs

### 16. [运动信号调节皮层但不调节皮层下对自发声音的处理](https://www.biorxiv.org/content/10.64898/2026.07.10.737812v1)
- Original title: Motor signals modulate cortical but not subcortical processing of self-initiated sounds
- Authors: Raiff, L., Butler, G., McFarlane, K., Chandrasekaran, B., Sitek, K. R.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.10.737812
- 中文摘要: 当我们自己发出声音时，大脑会通过输出复制机制调节听觉神经反应，使我们能够区分自发的听觉输入和外部产生的听觉输入。然而，这种衰减发生的听觉通路的精确水平仍不清楚。虽然来自动物模型的证据表明，自生声音的早期听觉处理可能受到皮质信号传导的调节，但局部皮质调节将保留高保真皮质下声音编码，同时允许在更高级别进行灵活的、依赖于上下文的处理。为了探究早期听觉系统中潜在的运动影响，我们使用 170 毫秒的语音刺激，收集了 33 名听力正常的成年人在主动（自发）和被动（外部呈现）聆听条件下头皮记录的频率跟随反应 (FFR)。
- Abstract: When we produce sounds ourselves, the brain modulates the auditory neural response through an efference copy mechanism, allowing us to distinguish between self-initiated and externally generated auditory inputs. However, the precise level of the auditory pathway at which this attenuation occurs remains unclear. While evidence from animal models suggests that early auditory processing of self-generated sounds may be...
- Summary (fallback): 机器翻译摘要显示：当我们自己发出声音时，大脑会通过输出复制机制调节听觉神经反应，使我们能够区分自发的听觉输入和外部产生的听觉输入。然而，这种衰减发生的听觉通路的精确水平仍不清楚。虽然来自动物模型的证据表明，自生声音的早期听觉处理可能受到皮质信号传导的调节，但局部皮质调节将保留高保真皮质下声音编码，同时允许在更高级别进行灵活的、依赖于上下文的处理。为了探究早期听觉系统中潜在的运动影响，我们使用 170 毫秒的语音刺激，收集了 33 名听力正常的成年人在主动（自发）和被动（外部呈现）聆听条件下头皮记录的频率跟随反应 (FFR)。
- Keywords: auditory, motor, cortical, processing, self-initiated

### 17. [母亲分离重新调整前额叶线粒体功能并防止压力引起的负面认知偏差](https://www.biorxiv.org/content/10.64898/2026.07.08.737201v1)
- Original title: Maternal separation recalibrates prefrontal mitochondrial function and protects against stress-induced negative cognitive bias
- Authors: Stupart, O., Marti-Prats, L., Holzner, L. M. W., Ibegbulam, S., Milton, A. L. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.08.737201
- 中文摘要: 模糊性代表了一种不确定性，其中结果概率无法明确学习，决策依赖于情绪状态和认知偏差。早期生活压力（ELS）会增加不良心理和身体健康结果的风险，并改变情感处理和学习。因此，ELS 可能会影响模糊信息的处理方式，这可能取决于与成年压力 (AS) 的相互作用，并在机制上取决于前额皮质 (PFC) 内自上而下的认知控制系统介导的生物能量机制。本研究调查了暴露于早期母体分离（MS）的大鼠（ELS 的啮齿动物模型）中 AS 对评估认知偏差的任务的影响，以及可能伴随的 PFC 线粒体功能的改变。
- Abstract: Ambiguity represents a form of uncertainty in which outcome probabilities cannot be explicitly learned, making decisions dependent on emotional states and cognitive biases. Early-life stress (ELS) increases the risk of adverse mental and physical health outcomes and alters affective processing and learning. ELS may thus affect how ambiguous information is processed, which may depend on interactions with adulthood st...
- Summary (fallback): 机器翻译摘要显示：模糊性代表了一种不确定性，其中结果概率无法明确学习，决策依赖于情绪状态和认知偏差。早期生活压力（ELS）会增加不良心理和身体健康结果的风险，并改变情感处理和学习。因此，ELS 可能会影响模糊信息的处理方式，这可能取决于与成年压力 (AS) 的相互作用，并在机制上取决于前额皮质 (PFC) 内自上而下的认知控制系统介导的生物能量机制。本研究调查了暴露于早期母体分离（MS）的大鼠（ELS 的啮齿动物模型）中 AS 对评估认知偏差的任务的影响，以及可能伴随的 PFC 线粒体功能的改变。
- Keywords: cognitive, bias, stress, mitochondrial, control

### 18. [尖孢镰刀菌角膜炎分离株 MRL8996 的近乎完整的基因组组装](https://www.biorxiv.org/content/10.64898/2026.07.06.736765v2)
- Original title: A near-complete genome assembly of the Fusarium oxysporum keratitis isolate MRL8996
- Authors: Doddi, A., Puebla-Planas, G., Lopez-Berges, M. S., Di Pietro, A.
- Meta: 2026-07-11 | genomics | DOI: 10.64898/2026.07.06.736765
- 中文摘要: 尖孢镰刀菌 MRL8996 是从严重的隐形眼镜相关性角膜炎病例中分离出来的真菌菌株。在这里，我们使用混合纳米孔和 Hi-C 支架方法报告了该分离株近乎完整的基因组组装。该组装将基因组分解为 16 条不同的染色体，包括 11 条核心染色体和 5 条谱系特异性染色体。这种高质量的参考基因组为研究这种高度通用的真菌谱系的大规模结构变异和驱动适应的进化机制提供了前所未有的工具。
- Abstract: Fusarium oxysporum MRL8996 is a fungal strain isolated from a severe case of contact lens-associated keratitis. Here we report a near-complete genome assembly of this isolate using a hybrid Nanopore and Hi-C scaffolding approach. The assembly resolves the genome into 16 distinct chromosomes, including 11 core and 5 lineage-specific chromosomes. This high-quality reference genome provides an unprecedented tool for in...
- Summary (fallback): 机器翻译摘要显示：尖孢镰刀菌 MRL8996 是从严重的隐形眼镜相关性角膜炎病例中分离出来的真菌菌株。在这里，我们使用混合纳米孔和 Hi-C 支架方法报告了该分离株近乎完整的基因组组装。该组装将基因组分解为 16 条不同的染色体，包括 11 条核心染色体和 5 条谱系特异性染色体。这种高质量的参考基因组为研究这种高度通用的真菌谱系的大规模结构变异和驱动适应的进化机制提供了前所未有的工具。
- Keywords: genome, assembly, near-complete, fusarium, oxysporum

### 19. [SMaHT 网络体细胞突变检测的综合基准测试](https://www.biorxiv.org/content/10.1101/2025.10.09.678885v2)
- Original title: Comprehensive benchmarking of somatic mutation detection by the SMaHT Network
- Authors: The Somatic Mosaicism across Human Tissues Network (SMaHT),, Abyzov, A.
- Meta: 2026-07-11 | genomics | DOI: 10.1101/2025.10.09.678885
- 中文摘要: 体细胞嵌合越来越被认为是人类生物学的基本特征，但体细胞突变的检测仍然具有挑战性。 SMaHT 网络进行了四次涉及细胞系和供体组织的大规模基准实验，以评估用于检测不同类型体细胞突变的测序技术、实验方法和计算方法，为九个分析样本中的每一个样本生成具有 >1,000X 短读长和 100-400X 长读长数据的社区资源。我们确定了利用短读长和长读长测序进行突变检测的有效策略，并证明使用供体特异性组装和人类泛基因组可以改善识别，将突变目录扩展到具有挑战性的基因组区域。
- Abstract: Somatic mosaicism is increasingly recognized as a fundamental feature of human biology, yet the detection of somatic mutations remains challenging. The SMaHT Network conducted four large-scale benchmarking experiments involving cell-lines and donor tissues, to evaluate sequencing technologies, experimental approaches, and computational methods for detecting different types of somatic mutations, generating community...
- Summary (fallback): 机器翻译摘要显示：体细胞嵌合越来越被认为是人类生物学的基本特征，但体细胞突变的检测仍然具有挑战性。 SMaHT 网络进行了四次涉及细胞系和供体组织的大规模基准实验，以评估用于检测不同类型体细胞突变的测序技术、实验方法和计算方法，为九个分析样本中的每一个样本生成具有 >1,000X 短读长和 100-400X 长读长数据的社区资源。我们确定了利用短读长和长读长测序进行突变检测的有效策略，并证明使用供体特异性组装和人类泛基因组可以改善识别，将突变目录扩展到具有挑战性的基因组区域。
- Keywords: somatic, mutation, detection, sequencing, comprehensive

### 20. [多重扰动细胞的联合分析提高了 Perturb-seq 中的统计能力和成本效率](https://www.biorxiv.org/content/10.64898/2026.07.10.737863v1)
- Original title: Joint analysis of multiply perturbed cells improves statistical power and cost efficiency in Perturb-seq
- Authors: Yeung, J., Tan, J., Wang, L., Wu, D., Melo Carlos, S. et al.
- Meta: 2026-07-11 | genomics | DOI: 10.64898/2026.07.10.737863
- 中文摘要: Perturb-seq 大规模测量对遗传扰动的转录组反应，但富集每个细胞一种指导 RNA 的传统设计仍然是资源密集型的。标准分析丢弃携带多个指导的细胞，进一步限制了每个实验的可用产量。在这里，我们描述了合并这些引导多重态如何影响信号恢复、信息丢失和成本降低。在最高的指导负担下，细胞表现出更大的压力并抑制细胞周期进程。我们开发了 PerturbMatch，这是一个可扩展的统计框架，用于分析引导多重态。在不同类别的引导多重态中，双态和三态比高阶多重态更准确地恢复微扰响应。
- Abstract: Perturb-seq measures transcriptomic responses to genetic perturbations at scale, but conventional designs that enrich for one guide RNA per cell remain resource-intensive. Standard analyses discard cells carrying multiple guides, further limiting the usable yield from each experiment. Here, we characterize how incorporating these guide multiplets affects signal recovery, information loss, and cost reduction. At the...
- Summary (fallback): 机器翻译摘要显示：Perturb-seq 大规模测量对遗传扰动的转录组反应，但富集每个细胞一种指导 RNA 的传统设计仍然是资源密集型的。标准分析丢弃携带多个指导的细胞，进一步限制了每个实验的可用产量。在这里，我们描述了合并这些引导多重态如何影响信号恢复、信息丢失和成本降低。在最高的指导负担下，细胞表现出更大的压力并抑制细胞周期进程。我们开发了 PerturbMatch，这是一个可扩展的统计框架，用于分析引导多重态。在不同类别的引导多重态中，双态和三态比高阶多重态更准确地恢复微扰响应。
- Keywords: guide, multiplets, cells, perturb-seq, statistical

### 21. [直接和反向神经精神癌症共病的遗传图谱](https://www.biorxiv.org/content/10.64898/2026.07.10.737193v1)
- Original title: A Genetic Atlas of Direct and Inverse Neuropsychiatric-Cancer Comorbidity
- Authors: Flores-Rodero, M., Fores-Martos, J., Sanchez-Orti, J. V., Martinez-Perez, S., Winkler, F. et al.
- Meta: 2026-07-11 | genomics | DOI: 10.64898/2026.07.10.737193
- 中文摘要: 神经精神疾病和癌症之间的直接和反向共病越来越被认为是神经系统与癌症关系的重要特征，但这些模式背后的遗传基因结构仍然知之甚少。在这里，我们使用连锁不平衡评分回归 (LDSC) 和高清似然 (HDL) 分析了 115 个 GWAS 数据集代表的 35 种疾病的成对遗传相关性，包括 9 种精神疾病、10 种神经系统疾病和 16 种癌症，并辅以荟萃分析、亚型解析分析、局部协方差映射和多组学基准测试。遗传相关性在疾病类别中主要呈正相关且最强，而癌症-神经病学配对显示出最弱的整体遗传亲和力。
- Abstract: Direct and inverse comorbidities between neuropsychiatric disorders and cancer are increasingly recognised as important features of the nervous system-cancer relationship, yet the inherited genetic architecture underlying these patterns remains poorly understood. Here, we analysed pairwise genetic correlations across 35 diseases represented by 115 GWAS datasets, including 9 psychiatric disorders, 10 neurological dis...
- Summary (fallback): 机器翻译摘要显示：神经精神疾病和癌症之间的直接和反向共病越来越被认为是神经系统与癌症关系的重要特征，但这些模式背后的遗传基因结构仍然知之甚少。在这里，我们使用连锁不平衡评分回归 (LDSC) 和高清似然 (HDL) 分析了 115 个 GWAS 数据集代表的 35 种疾病的成对遗传相关性，包括 9 种精神疾病、10 种神经系统疾病和 16 种癌症，并辅以荟萃分析、亚型解析分析、局部协方差映射和多组学基准测试。遗传相关性在疾病类别中主要呈正相关且最强，而癌症-神经病学配对显示出最弱的整体遗传亲和力。
- Keywords: genetic, direct, inverse, comorbidities, correlations

### 22. [基于张量的机器学习，用于多组学集成聚类和特征发现](https://www.biorxiv.org/content/10.64898/2025.11.28.691099v3)
- Original title: Tensor-based machine learning for multi-omics integrative clustering and feature discovery
- Authors: Zhang, Y., Liu, L., Liu, Z., Liu, Q., Ma, L. et al.
- Meta: 2026-07-11 | bioinformatics | DOI: 10.64898/2025.11.28.691099
- 中文摘要: 多组学综合分析对于阐明复杂的分子机制和生物过程至关重要，但由于多组学数据的高维性和异质性，仍然具有挑战性。在这里，我们介绍 MIA，一种机器学习框架，用于从多组学数据中进行准确的样本聚类和特征发现。与主要依赖于二维表示的现有算法不同，MIA 将多组学数据建模为三维张量，并将张量分解、模糊 c 均值和增强型随机森林模型集成在统一框架内。对模拟和经验数据集的基准测试表明，MIA 在聚类和特征识别方面始终优于代表性的最先进算法。
- Abstract: Multi-omics integrative analysis is pivotal for elucidating complex molecular mechanisms and biological processes, yet remains challenging due to the high dimensionality and heterogeneity of multi-omics data. Here we present MIA, a machine learning framework for accurate sample clustering and feature discovery from multi-omics data. Unlike existing algorithms that primarily rely on two-dimensional representations, M...
- Summary (fallback): 机器翻译摘要显示：多组学综合分析对于阐明复杂的分子机制和生物过程至关重要，但由于多组学数据的高维性和异质性，仍然具有挑战性。在这里，我们介绍 MIA，一种机器学习框架，用于从多组学数据中进行准确的样本聚类和特征发现。与主要依赖于二维表示的现有算法不同，MIA 将多组学数据建模为三维张量，并将张量分解、模糊 c 均值和增强型随机森林模型集成在统一框架内。对模拟和经验数据集的基准测试表明，MIA 在聚类和特征识别方面始终优于代表性的最先进算法。
- Keywords: multi-omics, feature, integrative, clustering, discovery

### 23. [空间线粒体谱系追踪揭示了骨肉瘤的转移前生态位和微环境程序化的命运转换](https://www.biorxiv.org/content/10.64898/2026.07.09.737611v1)
- Original title: Spatial mitochondrial lineage tracing uncovers a premetastatic niche and microenvironment programmed fate switching in osteosarcoma
- Authors: Xue, Y., Su, Z., Su, J., Chu, A. S., Wan, L. et al.
- Meta: 2026-07-11 | bioinformatics | DOI: 10.64898/2026.07.09.737611
- 中文摘要: 骨肉瘤的进展涉及复杂的时空动力学，但肿瘤细胞命运决定背后的谱系关系仍然知之甚少。在这里，我们整合单细胞和空间转录组学以及基于线粒体变异的谱系追踪，以绘制晚期非转移性骨肉瘤的进化图。恶性细胞的单细胞伪颞叶重建揭示了转录程序的逐步级联，指示 COL3A1 祖细胞分叉为 ALPL 成骨细胞和 THY1 间充质谱系。至关重要的是，我们证明转移性 THY1 间充质细胞的命运不仅仅由细胞自主转录程序控制；这种促肿瘤发生状态需要通过与 PLVAP 功能失调的内皮细胞直接共定位来形成严格的空间许可，以形成富含 PTN/NOTCH 信号传导的促转移生态位 (THY1-Endo)。
- Abstract: Osteosarcoma progression involves complex spatiotemporal dynamics, yet the lineage relationships underlying tumor cell fate decisions remain poorly understood. Here we integrate single cell and spatial transcriptomics and mitochondrial variants-based lineage tracing to map the evolution of a late-stage, non-metastatic osteosarcoma. Single cell pseudotemporal reconstruction of malignant cells reveals a stepwise casca...
- Summary (fallback): 机器翻译摘要显示：骨肉瘤的进展涉及复杂的时空动力学，但肿瘤细胞命运决定背后的谱系关系仍然知之甚少。在这里，我们整合单细胞和空间转录组学以及基于线粒体变异的谱系追踪，以绘制晚期非转移性骨肉瘤的进化图。恶性细胞的单细胞伪颞叶重建揭示了转录程序的逐步级联，指示 COL3A1 祖细胞分叉为 ALPL 成骨细胞和 THY1 间充质谱系。至关重要的是，我们证明转移性 THY1 间充质细胞的命运不仅仅由细胞自主转录程序控制；这种促肿瘤发生状态需要通过与 PLVAP 功能失调的内皮细胞直接共定位来形成严格的空间许可，以形成富含 PTN/NOTCH 信号传导的促转移生态位 (THY1-Endo)。
- Keywords: spatial, cell, mitochondrial, fate, clonal

### 24. [与环孢素 A 相比，沃罗孢素在灌注人近端小管微生理系统中保留线粒体功能](https://www.biorxiv.org/content/10.64898/2026.07.07.737071v1)
- Original title: Voclosporin Preserves Mitochondrial Function Compared With Cyclosporine A in Perfused Human Proximal Tubule Microphysiological Systems
- Authors: Aryeh, K. S., Tsang, Y. P., Hsu, E. W., Yeung, C. K., MacDonald, J. et al.
- Meta: 2026-07-11 | pharmacology and toxicology | DOI: 10.64898/2026.07.07.737071
- 中文摘要: 摘要背景：钙调磷酸酶抑制剂（CNI）对于移植免疫抑制是不可或缺的，但环孢素A（CsA）会产生肾毒性。 Voclosporin (VCS) 是一种 CsA 类似物，据认为肾毒性较小，但机制仍不清楚。方法：将原代人近端肾小管上皮细胞 (PTEC) 暴露于 2D 单层 CsA 或 VCS 中，并灌注 3D 肾脏微生理系统 (MPS)。通过 MTS 评估 2D 培养物中的活力，通过 TMRM 流式细胞仪评估线粒体膜电位 ({Delta}{Psi}m)，通过 ELISA 和 MSD 多重测定评估 MPS 流出物中的可溶性损伤和炎症生物标志物。 3D 培养的 PTEC 的 RNA 测序用于识别差异表达的基因和通路。结果：在 2D PTEC 中，两种药物均未降低活力。
- Abstract: Abstract Background: Calcineurin inhibitors (CNIs) are indispensable for transplantation immunosuppression, yet cyclosporine A (CsA) produces renal toxicity. Voclosporin (VCS), a CsA analog, is proposed to be less nephrotoxic, but mechanisms remain unclear. Methods: Primary human proximal tubule epithelial cells (PTECs) were exposed to CsA or VCS in 2D monolayers and perfused 3D kidney microphysiological system (MPS...
- Summary (fallback): 机器翻译摘要显示：摘要背景：钙调磷酸酶抑制剂（CNI）对于移植免疫抑制是不可或缺的，但环孢素A（CsA）会产生肾毒性。 Voclosporin (VCS) 是一种 CsA 类似物，据认为肾毒性较小，但机制仍不清楚。方法：将原代人近端肾小管上皮细胞 (PTEC) 暴露于 2D 单层 CsA 或 VCS 中，并灌注 3D 肾脏微生理系统 (MPS)。通过 MTS 评估 2D 培养物中的活力，通过 TMRM 流式细胞仪评估线粒体膜电位 ({Delta}{Psi}m)，通过 ELISA 和 MSD 多重测定评估 MPS 流出物中的可溶性损伤和炎症生物标志物。 3D 培养的 PTEC 的 RNA 测序用于识别差异表达的基因和通路。结果：在 2D PTEC 中，两种药物均未降低活力。
- Keywords: mitochondrial, showed, ptecs, stress, voclosporin

### 25. [胎儿性别影响胎盘对细胞外线粒体 DNA 的炎症反应](https://www.biorxiv.org/content/10.64898/2026.07.09.737607v1)
- Original title: Fetal sex shapes placental inflammatory responses to extracellular mitochondrial DNA
- Authors: da Silva, R. d. N. O., Hula, N., Escalera, D., Lopez, L., Kelly, G. et al.
- Meta: 2026-07-11 | physiology | DOI: 10.64898/2026.07.09.737607
- 中文摘要: 妊娠期间循环游离细胞线粒体 DNA (ccf-mtDNA) 的异常变化与不良妊娠结局相关。鉴于 ccf-mtDNA 通过模式识别受体（例如 Toll 样受体 9 (TLR9​​)）产生的炎症特性，我们假设细胞外 mtDNA 通过 TLR9 信号传导诱导胎盘炎症，并且这种反应因胎儿性别而异。在五项研究中，对怀孕的 Sprague-Dawley 大鼠进行了静脉注射纯化 mtDNA (300 g/kg)、核 DNA (nDNA)、盐水和/或 TLR9 拮抗剂 ODN2088。治疗后 4 小时（研究 1-3）和 24 小时（研究 4）评估胎盘反应；妊娠和新生儿结局在分娩时进行评估（研究 5）。暴露于 mtDNA（而非 nDNA）会增加胎盘 il1{beta}、tnf 和 il10 mRNA (p < 0.05)，从而建立反应特异性。
- Abstract: Aberrant changes in circulating cell-free mitochondrial DNA (ccf-mtDNA) across gestation are associated with adverse pregnancy outcomes. Given the inflammatory properties of ccf-mtDNA via pattern recognition receptors such as Toll-like receptor 9 (TLR9), we hypothesized that extracellular mtDNA induces placental inflammation via TLR9 signaling and that this response differs by fetal sex. Pregnant Sprague-Dawley rats...
- Summary (fallback): 机器翻译摘要显示：妊娠期间循环游离细胞线粒体 DNA (ccf-mtDNA) 的异常变化与不良妊娠结局相关。鉴于 ccf-mtDNA 通过模式识别受体（例如 Toll 样受体 9 (TLR9​​)）产生的炎症特性，我们假设细胞外 mtDNA 通过 TLR9 信号传导诱导胎盘炎症，并且这种反应因胎儿性别而异。在五项研究中，对怀孕的 Sprague-Dawley 大鼠进行了静脉注射纯化 mtDNA (300 g/kg)、核 DNA (nDNA)、盐水和/或 TLR9 拮抗剂 ODN2088。治疗后 4 小时（研究 1-3）和 24 小时（研究 4）评估胎盘反应；妊娠和新生儿结局在分娩时进行评估（研究 5）。暴露于 mtDNA（而非 nDNA）会增加胎盘 il1{beta}、tnf 和 il10 mRNA (p < 0.05)，从而...
- Keywords: mtdna, placental, tlr9, inflammatory, fetal

### 26. [衰老和听力障碍中的外围音素编码和歧视](https://www.biorxiv.org/content/10.64898/2026.01.27.702044v4)
- Original title: Peripheral phoneme encoding and discrimination in aging and hearing impairment
- Authors: Wouters, M., Gaudrain, E., Dapper, K., Schirmer, J., Baskent, D. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.01.27.702044
- 中文摘要: 噪音中的言语感知困难在老年人和听力障碍人士中很常见，但也发生在听力阈值在临床正常范围内的年轻人中。我们研究了衰老、耳蜗突触病 (CS) 和外毛细胞 (OHC) 损伤如何影响语音编码和音素辨别。使用脑电图在安静的情况下记录对矩形调幅（RAM）音调和类语音音素对的包络跟随反应（EFR），并在安静的情况下以及同侧和对侧噪声的情况下评估行为辨别能力。刺激被设计为针对时间包络（TENV）或时间精细结构（TFS）编码。
- Abstract: Speech perception difficulties in noise are common among older adults and individuals with hearing impairment, but also occur among younger adults whose audiometric thresholds are within the clinically-normal range. We examined how aging, cochlear synaptopathy (CS), and outer hair cell (OHC) damage affect speech encoding and phoneme discrimination. Envelope-following responses (EFRs) to rectangular amplitude-modulat...
- Summary (fallback): 机器翻译摘要显示：噪音中的言语感知困难在老年人和听力障碍人士中很常见，但也发生在听力阈值在临床正常范围内的年轻人中。我们研究了衰老、耳蜗突触病 (CS) 和外毛细胞 (OHC) 损伤如何影响语音编码和音素辨别。使用脑电图在安静的情况下记录对矩形调幅（RAM）音调和类语音音素对的包络跟随反应（EFR），并在安静的情况下以及同侧和对侧噪声的情况下评估行为辨别能力。刺激被设计为针对时间包络（TENV）或时间精细结构（TFS）编码。
- Keywords: discrimination, efrs, quiet, phoneme, encoding

### 27. [简单的过度学习时间期望的神经特征类似于情景检索](https://www.biorxiv.org/content/10.64898/2026.07.07.737020v2)
- Original title: The neural signature of simple overlearned temporal expectationsresembles episodic retrieval
- Authors: Sempf, L., Vavra, P., Noesselt, T.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.07.07.737020
- 中文摘要: 时间期望对于对可预测事件的适应性响应至关重要。以前的大多数成像研究都集中在意外事件而不是预期的神经基础上，没有考虑到与时间预期相关的神经反应可能会被并行学习过程所混淆。为了通过功能磁共振成像确定过度学习预期的神经基础，我们采用了多日检测范例，在可能和不太可能的时间点，听觉线索先于视觉目标。训练后，左下顶叶皮层与压后皮层和前额叶皮层一起处理过度学习的时间期望。值得注意的是，与未经训练的对照组相比，我们观察到反向的大脑反应是刺激可能性和训练状态的函数。
- Abstract: Temporal expectations are crucial for adaptive responding to predictable events. Most previous imaging studies have focused on the neural underpinnings of unexpectedness rather than expectedness, without considering that neural responses related to temporal expectations may be confounded by parallel learning processes. To identify the neural basis of overlearned expectancy with fMRI, we employed a multi-day detectio...
- Summary (fallback): 机器翻译摘要显示：时间期望对于对可预测事件的适应性响应至关重要。以前的大多数成像研究都集中在意外事件而不是预期的神经基础上，没有考虑到与时间预期相关的神经反应可能会被并行学习过程所混淆。为了通过功能磁共振成像确定过度学习预期的神经基础，我们采用了多日检测范例，在可能和不太可能的时间点，听觉线索先于视觉目标。训练后，左下顶叶皮层与压后皮层和前额叶皮层一起处理过度学习的时间期望。值得注意的是，与未经训练的对照组相比，我们观察到反向的大脑反应是刺激可能性和训练状态的函数。
- Keywords: temporal, neural, overlearned, expectations, episodic

### 28. [低重力揭示了运动状态表达的本体感觉依赖性机制](https://www.biorxiv.org/content/10.64898/2026.06.02.729513v2)
- Original title: Hypogravity reveals a proprioception-dependent mechanism for locomotor state expression
- Authors: Santuz, A., Luciano, F., Natalucci, V., Mbaye, A., Ma, N. et al.
- Meta: 2026-07-11 | neuroscience | DOI: 10.64898/2026.06.02.729513
- 中文摘要: 动物必须使运动适应不断变化的环境条件，但神经系统如何灵活控制运动仍不清楚。重力提供了强大的扰动，因为它改变了身体负荷、肢体动力学和本体感觉反馈。阿波罗宇航员经常在月球上跳跃，采用地球上很少使用的不对称步态，但这种行为的感觉运动基础尚不清楚。在这里，通过研究人类和小鼠的低重力运动，我们发现重力降低揭示了运动状态表达的保守的本体感觉依赖性机制。对于人类来说，模拟月球重力中的跳跃是通过现有运动模块的灵活时间重新配置而不是构建新的运动架构来产生的。
- Abstract: Animals must adapt locomotion to changing environmental conditions, but how the nervous system flexibly controls movement remains unclear. Gravity provides a powerful perturbation because it alters body loading, limb dynamics, and proprioceptive feedback. Apollo astronauts often skipped on the Moon, adopting an asymmetric gait rarely used on Earth, yet the sensorimotor basis of this behaviour is unknown. Here, by st...
- Summary (fallback): 机器翻译摘要显示：动物必须使运动适应不断变化的环境条件，但神经系统如何灵活控制运动仍不清楚。重力提供了强大的扰动，因为它改变了身体负荷、肢体动力学和本体感觉反馈。阿波罗宇航员经常在月球上跳跃，采用地球上很少使用的不对称步态，但这种行为的感觉运动基础尚不清楚。在这里，通过研究人类和小鼠的低重力运动，我们发现重力降低揭示了运动状态表达的保守的本体感觉依赖性机制。对于人类来说，模拟月球重力中的跳跃是通过现有运动模块的灵活时间重新配置而不是构建新的运动架构来产生的。
- Keywords: locomotor, gravity, hypogravity, reveals, state

### 29. [MT5-MMP C 端突变减少 C99 和 β 积累：基于肽的阿尔茨海默病干预措施的基础](https://www.biorxiv.org/content/10.1101/2025.05.22.655451v3)
- Original title: MT5-MMP C-terminal mutations reduce C99 and β accumulation: A foundation for peptide-based Alzheimer's interventions
- Authors: Belio-Mairal, P., Kamitsou, A., Stephan, D., Jullien, N., Thiane, D. et al.
- Meta: 2026-07-11 | cell biology | DOI: 10.1101/2025.05.22.655451
- 中文摘要: 我们之前的工作确定了膜型 5-基质金属蛋白酶 (MT5-MMP) 在阿尔茨海默病 (AD) 发病机制中的关键作用，特别是通过其 C 端跨膜 (TM) 和细胞内 (IC) 结构域，影响有毒淀粉样前体蛋白 (APP) 代谢物的主要有毒代谢物的命运，特别是 C99 和 A{β}。假设这些结构域中的修饰可以调节 C99 和 A{β} 水平，我们设计了 MT5-MMP 变体，在 TM/IC 结构域或特定 IC 氨基酸簇中进行删除或替换。当共转染到积累 C99 的人类细胞系时，某些 IC 结构域突变促进了 C99 降解并降低了 A{β} 水平，而其他突变则具有不同的影响。
- Abstract: Our prior work established a pivotal role for membrane-type 5-matrix metalloproteinase (MT5-MMP) in Alzheimer's disease (AD) pathogenesis, particularly through its C-terminal transmembrane (TM) and intracellular (IC) domains, which influence the fate of major toxic metabolites of toxic amyloid precursor protein (APP) metabolites, particularly C99 and A{beta}. Hypothesizing that modifications in these domains could m...
- Summary (fallback): 机器翻译摘要显示：我们之前的工作确定了膜型 5-基质金属蛋白酶 (MT5-MMP) 在阿尔茨海默病 (AD) 发病机制中的关键作用，特别是通过其 C 端跨膜 (TM) 和细胞内 (IC) 结构域，影响有毒淀粉样前体蛋白 (APP) 代谢物的主要有毒代谢物的命运，特别是 C99 和 A{β}。假设这些结构域中的修饰可以调节 C99 和 A{β} 水平，我们设计了 MT5-MMP 变体，在 TM/IC 结构域或特定 IC 氨基酸簇中进行删除或替换。当共转染到积累 C99 的人类细胞系时，某些 IC 结构域突变促进了 C99 降解并降低了 A{β} 水平，而其他突变则具有不同的影响。
- Keywords: mt5-mmp, beta, mutations, domains, levels

## medrxiv

### 1. [PABformer：通过可穿戴加速度测量进行基于多通道变压器的身体活动表示学习，用于预测帕金森病](https://www.medrxiv.org/content/10.1101/2025.08.12.25333460v2)
- Original title: PABformer: Multi-Channel Transformer-Based Physical Activity Representation Learning from Wearable Accelerometry for Prediction of Parkinson Disease
- Authors: He, K., Fan, L., Qian, H., Li, C., Wang, M.
- Meta: 2026-07-11 | health informatics | DOI: 10.1101/2025.08.12.25333460
- 中文摘要: 帕金森病 (PD) 是一种常见的神经退行性疾病，由于明显的运动症状延迟发作以及长期行为变化的复杂性，其早期诊断和预测仍然具有挑战性。可穿戴加速度计提供了一种可扩展且非侵入性的方法，用于监测自由生活环境中的身体活动 (PA)，并已成为 PD 预测的一种有前景的工具。然而，现有的基于加速度计的方法通常依赖于粗略的汇总统计数据或模型，捕获多日加速度计记录中的远程时间依赖性的能力有限。在本研究中，我们提出了 PABformer，这是一种多通道 Transformer 框架，专为从加速度计数据学习长期 PA 行为表示而设计。
- Abstract: Parkinson disease (PD) is a prevalent neurodegenerative disorder whose early diagnosis and prediction remain challenging due to the delayed onset of overt motor symptoms and the complexity of long-term behavioral changes. Wearable accelerometers provide a scalable and non-invasive approach for monitoring physical activity (PA) in free-living environments and have emerged as a promising tool for PD prediction. Howeve...
- Summary (fallback): 机器翻译摘要显示：帕金森病 (PD) 是一种常见的神经退行性疾病，由于明显的运动症状延迟发作以及长期行为变化的复杂性，其早期诊断和预测仍然具有挑战性。可穿戴加速度计提供了一种可扩展且非侵入性的方法，用于监测自由生活环境中的身体活动 (PA)，并已成为 PD 预测的一种有前景的工具。然而，现有的基于加速度计的方法通常依赖于粗略的汇总统计数据或模型，捕获多日加速度计记录中的远程时间依赖性的能力有限。在本研究中，我们提出了 PABformer，这是一种多通道 Transformer 框架，专为从加速度计数据学习长期 PA 行为表示而设计。
- Keywords: pabformer, prediction, learning, accelerometer, activity
