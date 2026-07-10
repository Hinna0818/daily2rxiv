# daily2rxiv Digest - 2026-07-11

共收录 90 篇论文。

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
- 中文摘要: 窄带干扰 (NBI) 会破坏子载波并使经典软解调无效，从而严重降低正交频分复用 (OFDM) 系统的性能。传统的压缩感知 (CS) 缓解措施表现出较高的顺序延迟，并留下结构化的非高斯残差，在采用经典高斯解映射器时，这些残差会导致对数似然比 (LLR) 不可靠性、解码器饱和和严重的错误平台。我们使用统一的深度学习框架来解决这种管道不匹配的问题，该框架用于联合 NBI 消除和鲁棒的软解调。首先，NBI-CNet 采用基于物理的卷积架构来估计 NBI 参数并消除单次前向传播中的多音干扰。
- Abstract: Narrowband interference (NBI) severely degrades orthogonal frequency-division multiplexing (OFDM) systems by corrupting subcarriers and rendering classical soft demodulation ineffective. Conventional compressed-sensing (CS) mitigation exhibits high sequential latency and leaves structured, non-Gaussian residuals that cause log-likelihood ratio (LLR) unreliability, decoder saturation, and severe error floors when emp...
- Summary (fallback): 机器翻译摘要显示：窄带干扰 (NBI) 会破坏子载波并使经典软解调无效，从而严重降低正交频分复用 (OFDM) 系统的性能。传统的压缩感知 (CS) 缓解措施表现出较高的顺序延迟，并留下结构化的非高斯残差，在采用经典高斯解映射器时，这些残差会导致对数似然比 (LLR) 不可靠性、解码器饱和和严重的错误平台。我们使用统一的深度学习框架来解决这种管道不匹配的问题，该框架用于联合 NBI 消除和鲁棒的软解调。首先，NBI-CNet 采用基于物理的卷积架构来估计 NBI 参数并消除单次前向传播中的多音干扰。
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

### 1. [鉴定细菌中小非编码 RNA (sRNA) 候选物的管道](https://www.biorxiv.org/content/10.64898/2026.07.02.735529v1)
- Original title: A pipeline for identifying small noncoding RNA (sRNA) candidates in bacteria
- Authors: Elhedi, S., NDiaye, K. D. S., Perreault, J.
- Meta: 2026-07-10 | molecular biology | DOI: 10.64898/2026.07.02.735529
- 中文摘要: 细菌小非编码 RNA (sRNA) 是转录后调控的核心，但由于转录噪声和缺乏规范编码特征，它们的计算识别假阳性率较高。我们开发了一个三阶段流程，集成了 sRNA 预测 (sRNA-Detect)、转录起始位点定位（TSSAR、dRNA-seq）和 Rho 独立终止子检测 (RNIE)，应用于跨越六个门的九个系统发育多样化的细菌物种。顺序过滤在 9 个物种中实现了 1.4 至 33 倍的精度提高，将候选集减少了高达 99.6%，同时以反映参考数据库深度的速度恢复已知 sRNA（金黄色葡萄球菌的召回率为 6%，大肠杆菌和金黄色葡萄球菌的召回率为 33-34%）。
- Abstract: Bacterial small non-coding RNAs (sRNAs) are central post-transcriptional regulators, yet their computational identification suffers from high false-positive rates due to transcriptional noise and the absence of canonical coding features. We developed a three-stage pipeline integrating sRNA prediction (sRNA-Detect), transcription start site mapping (TSSAR, dRNA-seq), and Rho-independent terminator detection (RNIE), a...
- Summary (fallback): 机器翻译摘要显示：细菌小非编码 RNA (sRNA) 是转录后调控的核心，但由于转录噪声和缺乏规范编码特征，它们的计算识别假阳性率较高。我们开发了一个三阶段流程，集成了 sRNA 预测 (sRNA-Detect)、转录起始位点定位（TSSAR、dRNA-seq）和 Rho 独立终止子检测 (RNIE)，应用于跨越六个门的九个系统发育多样化的细菌物种。顺序过滤在 9 个物种中实现了 1.4 至 33 倍的精度提高，将候选集减少了高达 99.6%，同时以反映参考数据库深度的速度恢复已知 sRNA（金黄色葡萄球菌的召回率为 6%，大肠杆菌和金黄色葡萄球菌的召回率为 33-34%）。
- Keywords: across, pipeline, srna, bacterial, srnas

### 2. [核仁是一种机械敏感的凝聚物，使核糖体生物发生适应机械力](https://www.biorxiv.org/content/10.64898/2026.07.02.731374v1)
- Original title: The nucleolus is a mechanosensitive condensate that adapts ribosome biogenesis to mechanical forces
- Authors: Shetty, Y., Elias, K. O., Badawi, S., Pernet, L., Ribba, A.-S. et al.
- Meta: 2026-07-10 | cell biology | DOI: 10.64898/2026.07.02.731374
- 中文摘要: 细胞内区室化是细胞组织的基础，但机械生物学在很大程度上是通过膜界定的结构和相关的信号传导途径来理解的。机械力是否直接调节生物分子凝聚体（组织许多核心细胞功能）仍然很大程度上未知。这个问题与核仁特别相关，核仁是一种重要的核凝聚体，它协调核糖体的生物发生，并且已知会根据不同的生化扰动进行重塑，将其置于细胞状态和生物合成控制之间的界面。在这里，我们证明机械压缩重塑核仁组织并减少（核糖体 DNA）rDNA 转录，并确定核仁素是这种适应性反应的关键介质。
- Abstract: Intracellular compartmentalization is fundamental to cellular organization, yet mechanobiology has been largely understood through membrane-delimited structures and associated signaling pathways. Whether mechanical forces directly regulate biomolecular condensates, which organize many core cellular functions, remains largely unknown. This question is particularly relevant for the nucleolus, a prominent nuclear conde...
- Summary (fallback): 机器翻译摘要显示：细胞内区室化是细胞组织的基础，但机械生物学在很大程度上是通过膜界定的结构和相关的信号传导途径来理解的。机械力是否直接调节生物分子凝聚体（组织许多核心细胞功能）仍然很大程度上未知。这个问题与核仁特别相关，核仁是一种重要的核凝聚体，它协调核糖体的生物发生，并且已知会根据不同的生化扰动进行重塑，将其置于细胞状态和生物合成控制之间的界面。在这里，我们证明机械压缩重塑核仁组织并减少（核糖体 DNA）rDNA 转录，并确定核仁素是这种适应性反应的关键介质。
- Keywords: nucleolus, mechanical, condensate, ribosome, biogenesis

### 3. [动力蛋白-微管力驱动 T 细胞中的核运动和迁移](https://www.biorxiv.org/content/10.64898/2026.07.02.736211v2)
- Original title: Dynein-microtubule forces drive nucleokinesis and transmigration in T cells
- Authors: Tagay, Y., Zhovmer, A. S., Sarkar, N., Stoop, J., Su, L. et al.
- Meta: 2026-07-10 | cell biology | DOI: 10.64898/2026.07.02.736211
- 中文摘要: 除了在允许的细胞外环境中典型的肌动球蛋白驱动的变形虫运动的机械能力之外，细胞核成为限制组织中 T 细胞迁移的主要障碍。我们将动力蛋白-微管 (MT) 力传递轴建立为受限 T 细胞迁移和轮回过程中核转位的重要机制。我们认为，动力蛋白既充当马达，又充当 F-肌动蛋白锚定的力传递元件（支点），沿着细胞皮层滑动 MT 和 MT 耦合核，以驱动核运动和生产性细胞位移。动力蛋白是核运动的主要驱动力：它的抑制作用可阻止细胞核运动，而与肌球蛋白 II 的活性无关，而 F-肌动蛋白动力学在时空上与核振荡保持脱钩。
- Abstract: Beyond the mechanical capacity of canonical actomyosin-driven amoeboid motility in permissive extracellular environments, the nucleus becomes the principal barrier to T cell migration in confining tissues. We establish the dynein-microtubule (MT) force-transmission axis as an essential mechanism for nuclear translocation during confined T cell migration and transmigration. We argue that dynein acts both as a motor a...
- Summary (fallback): 机器翻译摘要显示：除了在允许的细胞外环境中典型的肌动球蛋白驱动的变形虫运动的机械能力之外，细胞核成为限制组织中 T 细胞迁移的主要障碍。我们将动力蛋白-微管 (MT) 力传递轴建立为受限 T 细胞迁移和轮回过程中核转位的重要机制。我们认为，动力蛋白既充当马达，又充当 F-肌动蛋白锚定的力传递元件（支点），沿着细胞皮层滑动 MT 和 MT 耦合核，以驱动核运动和生产性细胞位移。动力蛋白是核运动的主要驱动力：它的抑制作用可阻止细胞核运动，而与肌球蛋白 II 的活性无关，而 F-肌动蛋白动力学在时空上与核振荡保持脱钩。
- Keywords: nucleus, cell, nuclear, dynein, nucleokinesis

### 4. [西高止山脉鸟类表现出独特的季节性海拔变化模式和依赖于热状态的变化策略的组合。](https://www.biorxiv.org/content/10.1101/2025.11.05.684726v2)
- Original title: Western Ghat birds exhibit a unique pattern of seasonal elevational shifts and a combination of thermal regime dependent shift strategies.
- Authors: Faizee, A. K., Ramesh, V., Robin, V. V.
- Meta: 2026-07-10 | ecology | DOI: 10.1101/2025.11.05.684726
- 中文摘要: 全球山地鸟类通过海拔变化来追踪天气模式和资源的季节性变化，从而表现出海拔迁徙。由于难以跨山地梯度采样数据，调查这种海拔变化的模式和机制的研究在空间尺度上受到限制。在这里，我们将世界上最大的参与性科学项目 (eBird) 的数据与系统调查相结合，以研究可能解释西高止山脉生物多样性热点尼尔吉里山鸟类海拔范围变化的模式和机制。我们计算了尼尔吉里斯全年最热和最冷月份之间鸟类海拔范围的变化程度，并使用系统发育广义最小二乘回归量化这些变化与物种特征之间的关联。
- Abstract: Elevational migration is globally exhibited by montane bird species through elevational range shifts to track seasonal changes in weather patterns and resources. Studies investigating the patterns and mechanisms of such elevational shifts have been limited in spatial scale owing to the difficulty of sampling data across montane gradients. Here, we integrated data from the world's largest participatory science projec...
- Summary (fallback): 机器翻译摘要显示：全球山地鸟类通过海拔变化来追踪天气模式和资源的季节性变化，从而表现出海拔迁徙。由于难以跨山地梯度采样数据，调查这种海拔变化的模式和机制的研究在空间尺度上受到限制。在这里，我们将世界上最大的参与性科学项目 (eBird) 的数据与系统调查相结合，以研究可能解释西高止山脉生物多样性热点尼尔吉里山鸟类海拔范围变化的模式和机制。我们计算了尼尔吉里斯全年最热和最冷月份之间鸟类海拔范围的变化程度，并使用系统发育广义最小二乘回归量化这些变化与物种特征之间的关联。
- Keywords: elevational, shifts, species, thermal, birds

### 5. [空间免疫结构和肿瘤谱系计划共同塑造晚期胰腺导管腺癌的临床结果](https://www.biorxiv.org/content/10.64898/2026.06.28.734525v2)
- Original title: Spatial immune architecture and tumor lineage programs jointly shape clinical outcomes in advanced pancreatic ductal adenocarcinoma
- Authors: Oo, H. M., Anekpuritanang, T., Angkathunyakul, N., Degirmenci, U., Pongpaibul, A. et al.
- Meta: 2026-07-10 | cancer biology | DOI: 10.64898/2026.06.28.734525
- 中文摘要: 胰腺导管腺癌（PDAC）表现出广泛的分子和微环境异质性，但晚期疾病中肿瘤谱系状态如何与空间免疫组织相互作用仍知之甚少。在这里，我们使用组织循环免疫荧光 (t-CyCIF) 对 27 名晚期 PDAC 患者进行了多重空间蛋白质组分析，并将这些分析与代表性肿瘤的空间转录组分析相结合。根据 GATA6 和 CK5 表达，肿瘤被分为经典、混合、基础和无效上皮状态，揭示了与临床结果相关的不同免疫结构。经典肿瘤和混合肿瘤表现出富含淋巴细胞的免疫炎症微环境，而基底肿瘤和无效肿瘤表现出免疫排斥、巨噬细胞主导的景观，其特征是 M2 巨噬细胞增加。
- Abstract: Pancreatic ductal adenocarcinoma (PDAC) exhibits extensive molecular and microenvironmental heterogeneity, yet how tumor lineage states interact with spatial immune organization in advanced disease remains poorly understood. Here, we performed multiplexed spatial proteomic profiling using tissue cyclic immunofluorescence (t-CyCIF) in 27 patients with advanced PDAC and integrated these analyses with spatial transcrip...
- Summary (fallback): 机器翻译摘要显示：胰腺导管腺癌（PDAC）表现出广泛的分子和微环境异质性，但晚期疾病中肿瘤谱系状态如何与空间免疫组织相互作用仍知之甚少。在这里，我们使用组织循环免疫荧光 (t-CyCIF) 对 27 名晚期 PDAC 患者进行了多重空间蛋白质组分析，并将这些分析与代表性肿瘤的空间转录组分析相结合。根据 GATA6 和 CK5 表达，肿瘤被分为经典、混合、基础和无效上皮状态，揭示了与临床结果相关的不同免疫结构。经典肿瘤和混合肿瘤表现出富含淋巴细胞的免疫炎症微环境，而基底肿瘤和无效肿瘤表现出免疫排斥、巨噬细胞主导的景观，其特征是 M2 巨噬细胞增加。
- Keywords: spatial, immune, advanced, hybrid, lineage

### 6. [精氨基琥珀酸合成酶 1 将肝脏尿素循环与全身脂质代谢联系起来](https://www.biorxiv.org/content/10.64898/2026.06.02.729618v2)
- Original title: Argininosuccinate Synthase 1 links hepatic urea cycle to whole body lipid metabolism
- Authors: Kim, L. C., Lesner, N. P., Cai, X., Han, X., Jung, J. W. et al.
- Meta: 2026-07-10 | cancer biology | DOI: 10.64898/2026.06.02.729618
- 中文摘要: 在肝病和肝细胞癌 (HCC) 中，肝尿素循环始终受到抑制，但单个酶的损失是否会导致疾病的发生和进展仍不清楚。使用肝细胞特异性缺失精氨琥珀酸合酶 1 (ASS1)（一种将瓜氨酸和天冬氨酸缩合成精氨琥珀酸的尿素循环酶）的小鼠，我们研究了 ASS1 在饮食和致癌物诱导的肝病进展中的作用。我们发现肝脏 Ass1 完全丧失是致命的，但高脂肪饮食可以延长寿命。出乎意料的是，肝脏 Ass1 损失约 85% 的动物完全免受饮食引起的肥胖、肝脂肪变性、纤维化和 HCC 的影响。我们确定肝脏 Ass1 损失会激活外周氧化组织中的脂肪酸氧化，从而导致能量消耗增加并预防疾病表型。
- Abstract: The hepatic urea cycle is consistently suppressed in liver disease and hepatocellular carcinoma (HCC), but whether loss of individual enzymes contributes to disease initiation and progression remains unknown. Using mice with hepatocyte-specific deletion of argininosuccinate synthase 1 (ASS1), the urea cycle enzyme that condenses citrulline and aspartate into argininosuccinate, we investigated the role of ASS1 in die...
- Summary (fallback): 机器翻译摘要显示：在肝病和肝细胞癌 (HCC) 中，肝尿素循环始终受到抑制，但单个酶的损失是否会导致疾病的发生和进展仍不清楚。使用肝细胞特异性缺失精氨琥珀酸合酶 1 (ASS1)（一种将瓜氨酸和天冬氨酸缩合成精氨琥珀酸的尿素循环酶）的小鼠，我们研究了 ASS1 在饮食和致癌物诱导的肝病进展中的作用。我们发现肝脏 Ass1 完全丧失是致命的，但高脂肪饮食可以延长寿命。出乎意料的是，肝脏 Ass1 损失约 85% 的动物完全免受饮食引起的肥胖、肝脂肪变性、纤维化和 HCC 的影响。我们确定肝脏 Ass1 损失会激活外周氧化组织中的脂肪酸氧化，从而导致能量消耗增加并预防疾病表型。
- Keywords: ass1, hepatic, liver, disease, loss

### 7. [动态组蛋白超乙酰化塑造环境响应染色质状态](https://www.biorxiv.org/content/10.64898/2026.06.19.732295v2)
- Original title: Dynamic histone hyperacetylation shapes environmentally responsive chromatin states
- Authors: Ammari, M., Dash, L., Choudhary, A., Mamania, H., Gupta, J. et al.
- Meta: 2026-07-10 | plant biology | DOI: 10.64898/2026.06.19.732295
- 中文摘要: 转录因子（TF）通过激活靶基因来协调环境反应，但它们如何重塑表观基因组结构以协调基因表达仍然知之甚少。我们之前在拟南芥和番茄中鉴定出 SIENA（刺激诱导增强乙酰化）结构域是茉莉酸 (JA) 诱导的 H3K9 超乙酰化围绕 MYC2 TF 结合位点的大区域。然而，SIENA 结构域（SIENA）形成的机制及其功能意义仍然未知。在这里，我们发现 SIENAs 也在大豆的主要 JA 响应基因和基因簇上形成，将这种现象扩展到进化上遥远的作物物种。
- Abstract: Transcription factors (TFs) orchestrate environmental responses by activating target genes, yet how they reshape epigenome architecture to coordinate gene expression remains poorly understood. We previously identified SIENA (Stimulus-Induced ENhancer Acetylation) domains as large regions of jasmonic acid (JA)-induced H3K9 hyperacetylation surrounding MYC2 TF binding sites in Arabidopsis and tomato. However, the mech...
- Summary (fallback): 机器翻译摘要显示：转录因子（TF）通过激活靶基因来协调环境反应，但它们如何重塑表观基因组结构以协调基因表达仍然知之甚少。我们之前在拟南芥和番茄中鉴定出 SIENA（刺激诱导增强乙酰化）结构域是茉莉酸 (JA) 诱导的 H3K9 超乙酰化围绕 MYC2 TF 结合位点的大区域。然而，SIENA 结构域（SIENA）形成的机制及其功能意义仍然未知。在这里，我们发现 SIENAs 也在大豆的主要 JA 响应基因和基因簇上形成，将这种现象扩展到进化上遥远的作物物种。
- Keywords: histone, sienas, hyperacetylation, chromatin, gene

### 8. [Carpobrotus 属杂交的细胞基因组特征揭示了亲本优势的偏见](https://www.biorxiv.org/content/10.64898/2026.07.03.736328v2)
- Original title: Cytogenomic signatures of hybridisation in the genus Carpobrotus reveal biased parental dominance
- Authors: Pascual-Diaz, J. P., Torres, M., Bacovsky, V., Horakova, L., Kruzlicova, J. et al.
- Meta: 2026-07-10 | plant biology | DOI: 10.64898/2026.07.03.736328
- 中文摘要: O_LI杂交通常与植物入侵有关；然而，它对入侵物种的基因组组织和染色体进化的影响仍然知之甚少。我们研究了入侵性 Carpobrotus edulis-acinaciformis 杂种复合体中的杂交程度，并确定了亲本物种在杂种种质中的细胞基因组贡献。 C_LIO_LI我们结合了全基因组测序、群体基因组分析、基因组大小估计、重复组表征、染色体计数和荧光原位杂交来比较来自南非和地中海盆地的亲本物种和杂交种质。 C_LIO_LIP种群基因组分析揭示了广泛的杂交和基因渗入，大多数侵入性种质显示出混合祖先。 Pattersons D 统计支持对 C. edulis 的不对称等位基因共享。
- Abstract: O_LIHybridisation is frequently associated with plant invasions; however, its consequences for genome organisation and chromosome evolution remain poorly understood in invasive species. We investigated the extent of hybridisation in the invasive Carpobrotus edulis--acinaciformis hybrid complex and determined the cytogenomic contribution of parental species in hybrid accessions. C_LIO_LIWe combined whole-genome seque...
- Summary (fallback): 机器翻译摘要显示：O_LI杂交通常与植物入侵有关；然而，它对入侵物种的基因组组织和染色体进化的影响仍然知之甚少。我们研究了入侵性 Carpobrotus edulis-acinaciformis 杂种复合体中的杂交程度，并确定了亲本物种在杂种种质中的细胞基因组贡献。 C_LIO_LI我们结合了全基因组测序、群体基因组分析、基因组大小估计、重复组表征、染色体计数和荧光原位杂交来比较来自南非和地中海盆地的亲本物种和杂交种质。 C_LIO_LIP种群基因组分析揭示了广泛的杂交和基因渗入，大多数侵入性种质显示出混合祖先。 Pattersons D 统计支持对 C. edulis 的不对称等位基因共享。
- Keywords: hybrid, accessions, hybridisation, parental, genome

### 9. [域插入提高了 CRISPR 腺嘌呤碱基编辑器的精度](https://www.biorxiv.org/content/10.64898/2026.07.03.736350v1)
- Original title: Domain Insertion Improves the Precision of a CRISPR Adenine Base Editor
- Authors: Müller, M. M., Southern, N. T., Niopek, D.
- Meta: 2026-07-10 | synthetic biology | DOI: 10.64898/2026.07.03.736350
- 中文摘要: 腺嘌呤碱基编辑器 (ABE) 可实现 A*T 到 G*C 的高效转换，但其广泛的活动窗口经常导致意外的旁观者编辑。我们假设将庞大的惰性蛋白质结构域插入碱基编辑器将限制脱氨酶的有效范围，从而优先将编辑定向到预期的目标腺嘌呤。在这里，我们使用结构引导设计和计算推理系统地绘制高活性 TadA8e 腺嘌呤碱基编辑器中的域插入位点。我们发现 TadA8e 接受多个表面位点的结构域插入，总体活性和编辑窗口宽度取决于插入位置而不是结构域身份。令人兴奋的是，在残基 L68 处插入结构域保留了跨多个基因组位点的稳健编辑，同时将编辑窗口紧密聚焦在位置 5 周围。
- Abstract: Adenine base editors (ABEs) enable efficient A*T to G*C conversion, but their broad activity windows frequently cause unintended bystander edits. We hypothesized that insertion of a bulky, inert protein domain into the base editor would limit the effective reach of the deaminase, thereby preferentially directing editing to the intended target adenine. Here, we systematically map domain insertion sites within the hig...
- Summary (fallback): 机器翻译摘要显示：腺嘌呤碱基编辑器 (ABE) 可实现 A*T 到 G*C 的高效转换，但其广泛的活动窗口经常导致意外的旁观者编辑。我们假设将庞大的惰性蛋白质结构域插入碱基编辑器将限制脱氨酶的有效范围，从而优先将编辑定向到预期的目标腺嘌呤。在这里，我们使用结构引导设计和计算推理系统地绘制高活性 TadA8e 腺嘌呤碱基编辑器中的域插入位点。我们发现 TadA8e 接受多个表面位点的结构域插入，总体活性和编辑窗口宽度取决于插入位置而不是结构域身份。令人兴奋的是，在残基 L68 处插入结构域保留了跨多个基因组位点的稳健编辑，同时将编辑窗口紧密聚焦在位置 5 周围。
- Keywords: domain, base, editing, insertion, adenine

### 10. [二次切割驱动的非规范启动将启动编辑扩展到 5 个方向](https://www.biorxiv.org/content/10.1101/2025.05.20.655067v2)
- Original title: Second-cleavage-driven non-canonical priming expands prime editing in 5 direction
- Authors: Chen, P.-R., Yuan, X.-Z., Wang, S.-G., Xia, P.-F.
- Meta: 2026-07-10 | synthetic biology | DOI: 10.1101/2025.05.20.655067
- 中文摘要: 切割依赖性 CRISPR-Cas 基因编辑依赖于 RNA 引导的 DNA 切割，推动细胞机器整合预期的编辑。然而，CRISPR 核酸酶也可以对已切割的 DNA 链进行第二次切割。然而，这一功能从未被重新用于基因编辑。在这里，我们报告了 Cas9 的第二次切割活性的首次整合，用于精确基因编辑，允许在切口的 5 方向上进行以前不可能的引物编辑。我们阐明了第二切割驱动的途径，该途径引发切口上游的非规范逆转录事件。我们确定了非规范途径和规范途径之间的竞争，可以通过合理设计带有预期编辑的 RNA 模板来调节这种竞争。
- Abstract: Cleavage-dependent CRISPR-Cas gene editing relies on RNA-guided DNA cleavages that push cellular machinery to incorporate intended edits. Yet, a second cleavage on the already cut DNA strand can also be executed by CRISPR nucleases. This feature, however, has never been repurposed for gene editing. Here, we report the first integration of the second cleavage activity of Cas9 for precision gene editing, allowing prev...
- Summary (fallback): 机器翻译摘要显示：切割依赖性 CRISPR-Cas 基因编辑依赖于 RNA 引导的 DNA 切割，推动细胞机器整合预期的编辑。然而，CRISPR 核酸酶也可以对已切割的 DNA 链进行第二次切割。然而，这一功能从未被重新用于基因编辑。在这里，我们报告了 Cas9 的第二次切割活性的首次整合，用于精确基因编辑，允许在切口的 5 方向上进行以前不可能的引物编辑。我们阐明了第二切割驱动的途径，该途径引发切口上游的非规范逆转录事件。我们确定了非规范途径和规范途径之间的竞争，可以通过合理设计带有预期编辑的 RNA 模板来调节这种竞争。
- Keywords: editing, non-canonical, prime, gene, second

### 11. [形态发生的可微分设计 I：模拟与拟像](https://www.biorxiv.org/content/10.64898/2026.07.02.736195v2)
- Original title: Differentiable Design for Morphogenesis I: Simulation and Simulacra
- Authors: Beker, O., Dumitrascu, B.
- Meta: 2026-07-10 | systems biology | DOI: 10.64898/2026.07.02.736195
- 中文摘要: 细胞通过力和信息的局部交换来构建组织，但很难从稀疏的观察中推断出控制这些相互作用的规则。在这里，我们介绍waxMorph，一个可微分的基于细胞的框架，用于生成和重建三维形态发生。在合成和生物数据中，waxMorph 再现了已建立的机械化学形状程序，从静态组织体积推断出连续轨迹，并恢复了空间组织的潜在信号。在发育中的小鼠心肌数据集中，它比最佳传输插值更准确地重建了未观察到的中间几何形状，而在前肢中，它区分了相关的发育轨迹。通过改变细胞可用的潜在线索的容量和空间组织，waxMorph 还提供了一种基于模型的方法来量化形状组装的复杂性。
- Abstract: Cells build tissues through local exchanges of force and information, yet the rules governing these interactions are difficult to infer from sparse observations. Here, we introduce waxMorph, a differentiable cell-based framework for generating and reconstructing three-dimensional morphogenesis. In synthetic and biological data, waxMorph reproduced established mechanochemical shape programs, inferred continuous traje...
- Summary (fallback): 机器翻译摘要显示：细胞通过力和信息的局部交换来构建组织，但很难从稀疏的观察中推断出控制这些相互作用的规则。在这里，我们介绍waxMorph，一个可微分的基于细胞的框架，用于生成和重建三维形态发生。在合成和生物数据中，waxMorph 再现了已建立的机械化学形状程序，从静态组织体积推断出连续轨迹，并恢复了空间组织的潜在信号。在发育中的小鼠心肌数据集中，它比最佳传输插值更准确地重建了未观察到的中间几何形状，而在前肢中，它区分了相关的发育轨迹。通过改变细胞可用的潜在线索的容量和空间组织，waxMorph 还提供了一种基于模型的方法来量化形状组装的复杂性。
- Keywords: waxmorph, differentiable, morphogenesis, cells, local

### 12. [mACrob：用于高通量细菌图像分析的开源框架](https://www.biorxiv.org/content/10.1101/2025.10.21.683709v3)
- Original title: mAIcrobe: an open-source framework for high-throughput bacterial image analysis
- Authors: Brito, A. D., Alwardt, D., Mariz, B. d. P., Filipe, S. R., Pinho, M. G. et al.
- Meta: 2026-07-10 | microbiology | DOI: 10.1101/2025.10.21.683709
- 中文摘要: 细菌显微镜下的定量分析常常受到不同细胞形态、群体异质性以及对专业计算专业知识的需求的阻碍。为了应对这些挑战，引入了 mACrob 作为开源框架，通过集成一套深度学习模型，拓宽了高级细菌图像分析的范围。 maIcrobe 整合了多种分割算法，包括 StarDist、CellPose 和 U-Net，以及全面的形态分析和适应性强的神经网络分类器，所有这些都在 napari 生态系统内。这个统一的平台能够在单一环境中通过各种显微镜模式分析从球形金黄色葡萄球菌到杆状大肠杆菌的各种细菌种类。
- Abstract: Quantitative analysis in bacterial microscopy is often hindered by diverse cell morphologies, population heterogeneity, and the requirement for specialised computational expertise. To address these challenges, mAIcrobe is introduced as an open-source framework that broadens access to advanced bacterial image analysis by integrating a suite of deep learning models. mAIcrobe incorporates multiple segmentation algorith...
- Summary (fallback): 机器翻译摘要显示：细菌显微镜下的定量分析常常受到不同细胞形态、群体异质性以及对专业计算专业知识的需求的阻碍。为了应对这些挑战，引入了 mACrob 作为开源框架，通过集成一套深度学习模型，拓宽了高级细菌图像分析的范围。 maIcrobe 整合了多种分割算法，包括 StarDist、CellPose 和 U-Net，以及全面的形态分析和适应性强的神经网络分类器，所有这些都在 napari 生态系统内。这个统一的平台能够在单一环境中通过各种显微镜模式分析从球形金黄色葡萄球菌到杆状大肠杆菌的各种细菌种类。
- Keywords: maicrobe, bacterial, analysis, image, microscopy

### 13. [MYO7A 基因补充或 Myo7b 激活治疗 Usher 综合征 1B](https://www.biorxiv.org/content/10.64898/2026.07.02.736025v1)
- Original title: Gene Supplementation of MYO7A or activation of Myo7b for treatment of Usher syndrome 1B
- Authors: Mittas, D. M., Otify, D. Y., Gavrilov, Z., Heigl, T., Suchomski, J. et al.
- Meta: 2026-07-10 | molecular biology | DOI: 10.64898/2026.07.02.736025
- 中文摘要: MYO7A 突变会导致最严重的亚瑟氏综合症亚型，这是导致耳聋盲的主要遗传原因。 MYO7A 的大尺寸需要双腺相关病毒 (AAV) 载体进行基因转移或治疗视网膜缺陷的替代方法。在这里，我们评估了两种治疗方法：i) 通过双 mRNA 反式剪接 AAV 补充人类 MYO7A 基因，以及 ii) CRISPR/Cas 介导的相关小鼠 Myo7b 基因的激活。补充 MYO7A 后，转基因 MYO7A 转录物和蛋白质在小鼠、猪和人视网膜类器官的视网膜色素上皮 (RPE) 和光感受器中表达并正确定位。在 RPE 和光感受器特异性 Myo7a 敲除小鼠中，我们可以将 RPE 细胞中 MYO7A 的表达和黑素体的定位恢复到野生型水平。
- Abstract: Mutations in MYO7A result in the most severe subtype of Usher syndrome, the leading genetic cause of deafblindness. The large size of MYO7A requires dual adeno-associated virus (AAV) vectors for gene transfer or alternative methods to treat retinal defects. Here, we evaluated two treatment approaches: i) Supplementation of the human MYO7A gene via dual mRNA trans-splicing AAVs, and ii) CRISPR/Cas-mediated activation...
- Summary (fallback): 机器翻译摘要显示：MYO7A 突变会导致最严重的亚瑟氏综合症亚型，这是导致耳聋盲的主要遗传原因。 MYO7A 的大尺寸需要双腺相关病毒 (AAV) 载体进行基因转移或治疗视网膜缺陷的替代方法。在这里，我们评估了两种治疗方法：i) 通过双 mRNA 反式剪接 AAV 补充人类 MYO7A 基因，以及 ii) CRISPR/Cas 介导的相关小鼠 Myo7b 基因的激活。补充 MYO7A 后，转基因 MYO7A 转录物和蛋白质在小鼠、猪和人视网膜类器官的视网膜色素上皮 (RPE) 和光感受器中表达并正确定位。在 RPE 和光感受器特异性 Myo7a 敲除小鼠中，我们可以将 RPE 细胞中 MYO7A 的表达和黑素体的定位恢复到野生型水平。
- Keywords: myo7a, gene, myo7b, supplementation, activation

### 14. [挥发性二乙酰通过 DHAP-甘油分流诱导触发快速 fmo-2 表达](https://www.biorxiv.org/content/10.64898/2026.07.01.735788v1)
- Original title: Volatile diacetyl triggers rapid fmo-2 expression through DHAP-glycerol shunt induction
- Authors: Giorda, M., Sen, A., Denzel, M. S.
- Meta: 2026-07-10 | molecular biology | DOI: 10.64898/2026.07.01.735788
- 中文摘要: 秀丽隐杆线虫可以通过感知细菌衍生的挥发物来定位短暂的食物来源。然而，这些嗅觉线索是否也能触发预期的营养反应程序仍然未知。利用无偏见的转录组学和代谢组学，我们发现禁食蠕虫暴露于挥发性食物线索二乙酰快速诱导 DHAP-甘油分流中酶的表达，DHAP-甘油分流是糖酵解和甘油脂生物合成交叉点的代谢途径。我们证明，这条已知被糖毒性和高渗应激激活的途径也受到食物供应的调节。分流诱导需要 MDT-15 转录因子并驱动快速代谢重塑，其特征是甘油和磷脂酰甘油的积累。
- Abstract: C. elegans can locate ephemeral food sources by sensing bacterially-derived volatiles. However, whether these olfactory cues can also trigger anticipatory nutrient-responsive programs remains unknown. Using unbiased transcriptomics and metabolomics, we discover that fasting worms exposed to the volatile food cue diacetyl rapidly induce expression of enzymes in the DHAP-Glycerol shunt, a metabolic pathway at the inte...
- Summary (fallback): 机器翻译摘要显示：秀丽隐杆线虫可以通过感知细菌衍生的挥发物来定位短暂的食物来源。然而，这些嗅觉线索是否也能触发预期的营养反应程序仍然未知。利用无偏见的转录组学和代谢组学，我们发现禁食蠕虫暴露于挥发性食物线索二乙酰快速诱导 DHAP-甘油分流中酶的表达，DHAP-甘油分流是糖酵解和甘油脂生物合成交叉点的代谢途径。我们证明，这条已知被糖毒性和高渗应激激活的途径也受到食物供应的调节。分流诱导需要 MDT-15 转录因子并驱动快速代谢重塑，其特征是甘油和磷脂酰甘油的积累。
- Keywords: expression, shunt, food, volatile, diacetyl

### 15. [酸中毒引发的脂肪酸超载会导致内皮细胞功能障碍。](https://www.biorxiv.org/content/10.64898/2026.07.09.737452v1)
- Original title: Acidosis-triggered fatty acid overload induces endothelial cell dysfunction.
- Authors: Al-Siyabi, S., Ibanez, S., Serafimov, K., Lallement, J., Marchand, D. et al.
- Meta: 2026-07-10 | cell biology | DOI: 10.64898/2026.07.09.737452
- 中文摘要: 血管缺血的特征不仅是缺氧，还包括酸中毒，由于糖酵解产生的 H+ 增加和 H+ 清除不足，酸中毒会影响内皮细胞 (EC)。我们最近证明，酸性环境有利于非离子形式的脂肪酸（FA）跨癌细胞质膜的翻转运输。在这项研究中，我们研究了酸中毒如何影响高糖酵解 EC 管理 FA 的能力并参与内皮功能障碍。我们首先使用油红 O 染色和全息显微镜追踪脂滴 (LD) 的形成。纯化的单不饱和油酸酯以及反映体内血清成分的 FA 混合物，通过 FA 转运蛋白独立机制导致剂量和时间依赖性 LD 积累。
- Abstract: Vascular ischemia is characterized not only by hypoxia but also by acidosis, which affects endothelial cells (ECs) due to increased H+ production from glycolysis and a deficit in H+ washout. We recently documented that an acidic environment facilitates the flip-flop transport of the non-ionized form of fatty acids (FAs) across the plasma membrane of cancer cells. In this study, we investigated how acidosis influence...
- Summary (fallback): 机器翻译摘要显示：血管缺血的特征不仅是缺氧，还包括酸中毒，由于糖酵解产生的 H+ 增加和 H+ 清除不足，酸中毒会影响内皮细胞 (EC)。我们最近证明，酸性环境有利于非离子形式的脂肪酸（FA）跨癌细胞质膜的翻转运输。在这项研究中，我们研究了酸中毒如何影响高糖酵解 EC 管理 FA 的能力并参与内皮功能障碍。我们首先使用油红 O 染色和全息显微镜追踪脂滴 (LD) 的形成。纯化的单不饱和油酸酯以及反映体内血清成分的 FA 混合物，通过 FA 转运蛋白独立机制导致剂量和时间依赖性 LD 积累。
- Keywords: endothelial, dysfunction, acidosis, which, levels

### 16. [ECD 的新型 RNA 结合活性有助于 U5 snRNP 稳定性和前 mRNA 剪接](https://www.biorxiv.org/content/10.1101/2025.01.24.634785v4)
- Original title: A novel RNA-binding activity of ECD contributes to U5 snRNP stability and pre-mRNA splicing
- Authors: Raza, M., Rajan, A. R., Kalluchi, A., Mohapatra, B., Saleem, I. et al.
- Meta: 2026-07-10 | cell biology | DOI: 10.1101/2025.01.24.634785
- 中文摘要: 人类无蜕皮激素蛋白（ECD）在调节细胞周期进程和细胞存活中发挥着重要作用。 ECD 先前已通过其与剪接体蛋白的关联而参与 RNA 剪接。在这里，我们使用 EMSA、荧光偏振测定和突变分析证明 ECD 直接与 RNA 结合。增强的 CLIP-seq 分析鉴定了细胞中与 ECD 结合的广泛 mRNA。 RNA-seq 分析表明，ECD 缺失会导致广泛的剪接畸变和基因表达改变。 ECD 与 RNA 的结合在剪接位点附近富集，并且 ECD 结合转录物的很大一部分在 ECD 耗尽时表现出剪接缺陷。 ECD 与 U5 snRNP 复合物特异性蛋白结合并稳定其。
- Abstract: Human ecdysoneless protein (ECD) plays an essential role in regulating cell cycle progression and cell survival. ECD has previously been implicated in RNA splicing through its association with spliceosomal proteins. Here, using EMSA, fluorescence polarization assays, and mutational analysis, we demonstrate that ECD directly binds to RNA. Enhanced CLIP-seq analysis identified a broad repertoire of mRNAs bound to ECD...
- Summary (fallback): 机器翻译摘要显示：人类无蜕皮激素蛋白（ECD）在调节细胞周期进程和细胞存活中发挥着重要作用。 ECD 先前已通过其与剪接体蛋白的关联而参与 RNA 剪接。在这里，我们使用 EMSA、荧光偏振测定和突变分析证明 ECD 直接与 RNA 结合。增强的 CLIP-seq 分析鉴定了细胞中与 ECD 结合的广泛 mRNA。 RNA-seq 分析表明，ECD 缺失会导致广泛的剪接畸变和基因表达改变。 ECD 与 RNA 的结合在剪接位点附近富集，并且 ECD 结合转录物的很大一部分在 ECD 耗尽时表现出剪接缺陷。 ECD 与 U5 snRNP 复合物特异性蛋白结合并稳定其。
- Keywords: proteins, splicing, depletion, highwire, dtlvardef

### 17. [细胞类型特异性 ATF6α 程序在生理和暴露加速的肺衰老过程中调节上皮线粒体稳态和周细胞重塑](https://www.biorxiv.org/content/10.64898/2026.07.09.737329v1)
- Original title: Cell-type-specific ATF6α programs regulate epithelial mitochondrial homeostasis and pericyte remodeling during physiological and exposure-accelerated lung aging
- Authors: Huang, X., Bard, J. E., Tumenbayar, B.-I., Vedagiri, K., Nelson, C. E. et al.
- Meta: 2026-07-10 | cell biology | DOI: 10.64898/2026.07.09.737329
- 中文摘要: 蛋白质稳态随着肺衰老而下降，而未折叠蛋白反应（UPR）在肺衰老和年龄相关肺部疾病中的作用仍未得到充分研究。我们研究了 UPR 传感器 ATF6 的缺陷如何影响生理和烟雾暴露加速的肺部衰老。 ATF6缺陷的小鼠表现出肺泡简化加速，这是肺实质老化的标志，吸烟会加剧这种老化。然而，小气道血管纤维化重塑（一种主要的吸烟引起的病理学）在暴露于烟雾的 ATF6 缺陷小鼠中并不明显。从机制上讲，这些不同的表型源于细胞类型特异性的 ATF6 程序。在 2 型肺泡上皮细胞 (AEC2s)（肺实质的兼性祖细胞）中，ATF6 维持线粒体生物能并持续有效地再分化为 1 型肺泡上皮细胞 (AEC1s)。
- Abstract: Proteostasis declines with lung aging, while the role of the Unfolded Protein Response (UPR) in lung aging and age-associated pulmonary diseases remains understudied. We investigated how deficiency in the UPR sensor ATF6 affects physiological and smoke exposure-accelerated lung aging. ATF6 -deficient mice exhibited accelerated alveolar simplification, a sign of lung parenchymal aging, which was exacerbated by smokin...
- Summary (fallback): 机器翻译摘要显示：蛋白质稳态随着肺衰老而下降，而未折叠蛋白反应（UPR）在肺衰老和年龄相关肺部疾病中的作用仍未得到充分研究。我们研究了 UPR 传感器 ATF6 的缺陷如何影响生理和烟雾暴露加速的肺部衰老。 ATF6缺陷的小鼠表现出肺泡简化加速，这是肺实质老化的标志，吸烟会加剧这种老化。然而，小气道血管纤维化重塑（一种主要的吸烟引起的病理学）在暴露于烟雾的 ATF6 缺陷小鼠中并不明显。从机制上讲，这些不同的表型源于细胞类型特异性的 ATF6 程序。在 2 型肺泡上皮细胞 (AEC2s)（肺实质的兼性祖细胞）中，ATF6 维持线粒体生物能并持续有效地再分化为 1 型肺泡上皮细胞 (AEC1s)。
- Keywords: atf6, lung, aging, cell-type-specific, programs

### 18. [二氯乙酸可改善丙酮酸脱氢酶复合物缺乏症 (PDCD) 线虫 pdha-1 和 dld-1 RNAi 模型中的动物存活、生长、神经肌肉活动、线粒体应激和生理机能，并提高乳酸水平](https://www.biorxiv.org/content/10.64898/2026.07.08.737008v1)
- Original title: Dichloroacetate improves animal survival, growth, neuromuscular activity, mitochondrial stress and physiology, and elevated lactate in C. elegans pdha-1 and dld-1 RNAi models of pyruvate dehydrogenase complex deficiency (PDCD)
- Authors: Remes, C., Mathew, N. D., Miranda, V., Haroon, S., O'Hara, T. et al.
- Meta: 2026-07-10 | cell biology | DOI: 10.64898/2026.07.08.737008
- 中文摘要: 丙酮酸脱氢酶复合物 (PDHc) 缺乏症 (PDCD) 是一种原发性线粒体疾病，其特征是神经发育障碍、中间代谢改变和早期死亡。二氯乙酸 (DCA) 是一种丙酮酸类似物，是一种广为人知的 PDHc 激活剂，目前仍在临床研究中用于治疗 PDCD。在这里，我们研究了 DCA 5 点对数浓度范围对线虫动物健康和代谢的体内功效，通过分级程度地敲低 PDHA-1 或 DLD-1 同源物的 RNA 干扰 (RNAi) 表达来模拟不同疾病的严重程度。这些蠕虫模型概括了在人类患者中观察到的 PDCD 表型特征，包括存活率降低、生长延迟、运动障碍以及乳酸和/或丙酮酸组织水平升高。
- Abstract: Pyruvate dehydrogenase complex (PDHc) deficiency (PDCD) is a primary mitochondrial disorder characterized by neurodevelopmental disability, altered intermediary metabolism and early mortality. Dichloroacetate (DCA), a pyruvate analogue, is a well-described PDHc activator that remains under clinical investigation for treatment of PDCD. Here, we studied the in vivo efficacy of a 5-point log concentration range of DCA...
- Summary (fallback): 机器翻译摘要显示：丙酮酸脱氢酶复合物 (PDHc) 缺乏症 (PDCD) 是一种原发性线粒体疾病，其特征是神经发育障碍、中间代谢改变和早期死亡。二氯乙酸 (DCA) 是一种丙酮酸类似物，是一种广为人知的 PDHc 激活剂，目前仍在临床研究中用于治疗 PDCD。在这里，我们研究了 DCA 5 点对数浓度范围对线虫动物健康和代谢的体内功效，通过分级程度地敲低 PDHA-1 或 DLD-1 同源物的 RNA 干扰 (RNAi) 表达来模拟不同疾病的严重程度。这些蠕虫模型概括了在人类患者中观察到的 PDCD 表型特征，包括存活率降低、生长延迟、运动障碍以及乳酸和/或丙酮酸组织水平升高。
- Keywords: rnai, dld-1, survival, mitochondrial, physiology

### 19. [TIAM1 在中心粒组装和自溶酶体循环界面的功能](https://www.biorxiv.org/content/10.64898/2026.07.02.735969v1)
- Original title: Functions of TIAM1 at the interface of centriole assembly and autolysosome cycling
- Authors: Coelho, P. A., Yu, C., Glover, D. M.
- Meta: 2026-07-10 | cell biology | DOI: 10.64898/2026.07.02.735969
- 中文摘要: 中心体扩增通常与染色体不稳定和肿瘤进展相关，但细胞如何协调中心体组装与中心体数量和质量的控制仍知之甚少。 TIAM1 是一种 RAC1 鸟嘌呤核苷酸交换因子，之前与中心体相关信号传导和 PLK4 丰度的 {β}TrCP 依赖性控制有关。在这里，我们研究了 Tiam1 如何调节诱导过度表达 PLK4 的小鼠胚胎成纤维细胞中的自噬-溶酶体稳态。与之前的 Tiam1 丢失促进生产性中心粒过度复制的模型相反，我们通过超分辨率成像和扩展显微镜发现，TIAM1 耗尽后 PLK4 在中心粒相关结构上的异常分布，表明 TIAM1 可能支持中心粒的组织或成熟。
- Abstract: Centrosome amplification is frequently associated with chromosomal instability and tumor progression, but how cells coordinate centriole assembly with the control of centrosome numbers and quality remains poorly understood. TIAM1 is a RAC1 guanine nucleotide exchange factor previously implicated in centrosome-associated signaling and {beta}TrCP-dependent control of PLK4 abundance. Here, we examined how Tiam1 regulat...
- Summary (fallback): 机器翻译摘要显示：中心体扩增通常与染色体不稳定和肿瘤进展相关，但细胞如何协调中心体组装与中心体数量和质量的控制仍知之甚少。 TIAM1 是一种 RAC1 鸟嘌呤核苷酸交换因子，之前与中心体相关信号传导和 PLK4 丰度的 {β}TrCP 依赖性控制有关。在这里，我们研究了 Tiam1 如何调节诱导过度表达 PLK4 的小鼠胚胎成纤维细胞中的自噬-溶酶体稳态。与之前的 Tiam1 丢失促进生产性中心粒过度复制的模型相反，我们通过超分辨率成像和扩展显微镜发现，TIAM1 耗尽后 PLK4 在中心粒相关结构上的异常分布，表明 TIAM1 可能支持中心粒的组织或成熟。
- Keywords: tiam1, centriole, assembly, centrosome, plk4

### 20. [分泌途径的乙酰化依赖性重塑塑造了衰老相关的分泌组](https://www.biorxiv.org/content/10.64898/2026.06.23.733964v2)
- Original title: Acetylation-dependent remodeling of the secretory pathway shapes the senescence-associated secretome
- Authors: Nasrashvili, T., Emini, B., Cirri, E., Rahnis, N., Poempner, N. et al.
- Meta: 2026-07-10 | cell biology | DOI: 10.64898/2026.06.23.733964
- 中文摘要: 细胞衰老的特征是稳定的细胞周期停滞和衰老相关的分泌表型（SASP），这会驱动组织重塑和炎症。 SASP 细胞因子和其他分泌蛋白分泌增加，其背后是分泌途径的大规模重组。虽然衰老的转录调控已被广泛研究，但翻译后修饰 (PTM) 对分泌途径调控的贡献仍知之甚少。在这里，我们将定量蛋白质组学与磷酸化、泛素化和乙酰化的多层 PTM 分析相结合，以研究衰老过程中细胞内运输和分泌的调节方式。
- Abstract: Cellular senescence is characterized by stable cell cycle arrest and the senescence-associated secretory phenotype (SASP), which drives tissue remodeling and inflammation. Underlying SASP with its increased secretion of cytokines and other secreted proteins is a massive reorganization of the secretory pathway. While transcriptional regulation of senescence has been extensively studied, the contribution of post-trans...
- Summary (fallback): 机器翻译摘要显示：细胞衰老的特征是稳定的细胞周期停滞和衰老相关的分泌表型（SASP），这会驱动组织重塑和炎症。 SASP 细胞因子和其他分泌蛋白分泌增加，其背后是分泌途径的大规模重组。虽然衰老的转录调控已被广泛研究，但翻译后修饰 (PTM) 对分泌途径调控的贡献仍知之甚少。在这里，我们将定量蛋白质组学与磷酸化、泛素化和乙酰化的多层 PTM 分析相结合，以研究衰老过程中细胞内运输和分泌的调节方式。
- Keywords: senescence, secretory, senescence-associated, remodeling, pathway

### 21. [组织层压状态将脊椎动物视网膜中的神经元易位从主动转为被动](https://www.biorxiv.org/content/10.64898/2026.07.02.736014v1)
- Original title: Tissue lamination state switches neuronal translocation from active to passive in the vertebrate retina
- Authors: Cruz, M. R., Paixao, T., Coelho, J., Norden, C.
- Meta: 2026-07-10 | developmental biology | DOI: 10.64898/2026.07.02.736014
- 中文摘要: 神经元迁移对于发育中的中枢神经系统中建立功能性组织结构至关重要。虽然驱动神经元运动的细胞内在机制已经被确定，但迁移策略如何适应动态发育组织变化仍然知之甚少。在这里，我们使用在未层压和层压阶段生成的视网膜双极细胞来解决这个问题。这使得能够直接比较跨组织状态的神经元易位。将定量实时成像与目标扰动相结合，我们发现双极细胞的迁移模式根据组织层压状态进行切换。在光感受器层形成之前出生的双极细胞会经历定向的、微管依赖性的体细胞易位。相比之下，后来出生的细胞表现出由集体组织运动驱动的被动、非定向位移。
- Abstract: Neuronal migration is essential for establishing functional tissue architecture in the developing central nervous system. While cell-intrinsic mechanisms driving neuronal movement have been identified, how migratory strategies adapt to dynamic developmental tissue changes remains less understood. Here, we address this question using retinal bipolar cells generated across unlaminated and laminated stages. This enable...
- Summary (fallback): 机器翻译摘要显示：神经元迁移对于发育中的中枢神经系统中建立功能性组织结构至关重要。虽然驱动神经元运动的细胞内在机制已经被确定，但迁移策略如何适应动态发育组织变化仍然知之甚少。在这里，我们使用在未层压和层压阶段生成的视网膜双极细胞来解决这个问题。这使得能够直接比较跨组织状态的神经元易位。将定量实时成像与目标扰动相结合，我们发现双极细胞的迁移模式根据组织层压状态进行切换。在光感受器层形成之前出生的双极细胞会经历定向的、微管依赖性的体细胞易位。相比之下，后来出生的细胞表现出由集体组织运动驱动的被动、非定向位移。
- Keywords: tissue, neuronal, cells, translocation, migration

### 22. [全胚胎 3D 定量揭示了非洲爪蟾胚层的保守拓扑设计和缩放](https://www.biorxiv.org/content/10.64898/2026.06.16.732511v2)
- Original title: Whole-Embryo 3D Quantification Reveals Conserved Topological Design and Scaling of Germ Layers in Xenopus
- Authors: Santos, H. M., Diakova, M., Brambach, M., Anderson, C., Petrova, K. et al.
- Meta: 2026-07-10 | developmental biology | DOI: 10.64898/2026.06.16.732511
- 中文摘要: 不同大小的胚胎如何产生可重复的身体计划仍然是发育生物学的中心问题。较大的胚胎是否包含更多的细胞，或者保留保守的组织原则以确保独立于规模的稳健的组织模式？在这里，我们通过爪蟾早期发育过程中细胞数量、组织分配和空间组织的全胚胎定量绘图来解决这个问题。利用优化的整体 3D 成像、组织清除和深度学习进行细胞核分割，我们量化了细胞数量并重建了早期胚胎阶段细胞的空间分布。尽管非洲爪蟾胚胎比热带爪蟾胚胎表现出更大的胚胎体积和更高的细胞总数，但外胚层、中胚层和内胚层之间的细胞比例分配在物种之间仍然高度保守。
- Abstract: How embryos of different sizes generate reproducible body plans remains a central question in developmental biology. Do larger embryos contain more cells, or preserve conserved organizational principles that ensure robust tissue patterning independent of scale? Here, we address this question through whole-embryo quantitative mapping of cell number, tissue allocation, and spatial organization during early development...
- Summary (fallback): 机器翻译摘要显示：不同大小的胚胎如何产生可重复的身体计划仍然是发育生物学的中心问题。较大的胚胎是否包含更多的细胞，或者保留保守的组织原则以确保独立于规模的稳健的组织模式？在这里，我们通过爪蟾早期发育过程中细胞数量、组织分配和空间组织的全胚胎定量绘图来解决这个问题。利用优化的整体 3D 成像、组织清除和深度学习进行细胞核分割，我们量化了细胞数量并重建了早期胚胎阶段细胞的空间分布。尽管非洲爪蟾胚胎比热带爪蟾胚胎表现出更大的胚胎体积和更高的细胞总数，但外胚层、中胚层和内胚层之间的细胞比例分配在物种之间仍然高度保守。
- Keywords: conserved, embryos, tissue, quantitative, cells

### 23. [印度南部热带干燥常绿森林的恢复：平衡固碳与生物多样性保护](https://www.biorxiv.org/content/10.64898/2026.07.08.737378v1)
- Original title: Restoration of tropical dry evergreen forest in southern India: balancing carbon sequestration with biodiversity conservation
- Authors: Shanmugam, M., Pulla, S., Epinal, L. N.
- Meta: 2026-07-10 | ecology | DOI: 10.64898/2026.07.08.737378
- 中文摘要: 热带干燥常绿森林（TDEF）是干燥热带地区独特且高度威胁的森林类型。如果本地物种表现出与广泛使用的非本地树木相当的碳固存能力，那么它们的恢复可能会得到加强。我们评估了印度经过修复的 TDEF 的生物多样性和碳固存，该地区经过 50 多年的发展，从一片贫瘠的土地上发展而来。该遗址现在拥有高度的木本植物多样性，有 34 个科的 91 个本土物种。地上生物量 (AGB) 平均为 66.91 +/- 41.2 毫克/公顷，与全球季节性干燥的热带森林相当。尽管本地物种种植时间较晚且比非本地物种矮，但它们对 AGB 贡献了 23.86 +/- 23.4 毫克/公顷，并显示出未来断面积增加的潜力。
- Abstract: Tropical dry evergreen forests (TDEFs) are a unique and highly threatened forest type of the dry tropics. Their restoration could be strengthened if native species demonstrate carbon sequestration comparable to widely used non-native trees. We assessed biodiversity and carbon sequestration in a restored TDEF in India, developed over 50 years from a largely barren landscape. The site now supports high woody-plant div...
- Summary (fallback): 机器翻译摘要显示：热带干燥常绿森林（TDEF）是干燥热带地区独特且高度威胁的森林类型。如果本地物种表现出与广泛使用的非本地树木相当的碳固存能力，那么它们的恢复可能会得到加强。我们评估了印度经过修复的 TDEF 的生物多样性和碳固存，该地区经过 50 多年的发展，从一片贫瘠的土地上发展而来。该遗址现在拥有高度的木本植物多样性，有 34 个科的 91 个本土物种。地上生物量 (AGB) 平均为 66.91 +/- 41.2 毫克/公顷，与全球季节性干燥的热带森林相当。尽管本地物种种植时间较晚且比非本地物种矮，但它们对 AGB 贡献了 23.86 +/- 23.4 毫克/公顷，并显示出未来断面积增加的潜力。
- Keywords: species, carbon, native, tropical, sequestration

### 24. [后生动物中携带包膜的反转录转座子的前寒武纪起源](https://www.biorxiv.org/content/10.1101/2023.10.26.564294v5)
- Original title: Pre-Cambrian origin of envelope-carrying retrotransposons in metazoans
- Authors: Chary, S., Hayashi, R.
- Meta: 2026-07-10 | evolutionary biology | DOI: 10.1101/2023.10.26.564294
- 中文摘要: 逆转录转座子或内源逆转录病毒（ERV）本质上携带gag和pol的开放阅读框，它们被用来在宿主种系基因组中自私地复制自身。另外携带包膜基因的 ERV 的一个罕见例子是果蝇中的 Ty3/gypsy errantiviruses。尽管它们在结构上与逆转录病毒相似，但仍不清楚包含包膜的 Ty3/gypsy 元件是否代表最近获得的病毒融合剂的谱系特异性，或者逆转录转座子和包膜样基因之间的古老关联。我们系统地搜索了无脊椎动物后生动物基因组中与 Ty3/gypsy 同源的完整的包含包膜的 ERV，发现它们广泛分布在包括刺胞动物、栉水母和被囊动物等古代动物在内的分类群中。
- Abstract: Retrotransposons or endogenous retroviruses (ERVs) essentially carry open reading frames of gag and pol, which are utilized to selfishly replicate themselves in the host germline genome. One rare example of ERVs that additionally carry envelope genes is Ty3/gypsy errantiviruses in Drosophila. Though they are structurally analogous to retroviruses, it remained unclear whether envelope-containing Ty3/gypsy elements re...
- Summary (fallback): 机器翻译摘要显示：逆转录转座子或内源逆转录病毒（ERV）本质上携带gag和pol的开放阅读框，它们被用来在宿主种系基因组中自私地复制自身。另外携带包膜基因的 ERV 的一个罕见例子是果蝇中的 Ty3/gypsy errantiviruses。尽管它们在结构上与逆转录病毒相似，但仍不清楚包含包膜的 Ty3/gypsy 元件是否代表最近获得的病毒融合剂的谱系特异性，或者逆转录转座子和包膜样基因之间的古老关联。我们系统地搜索了无脊椎动物后生动物基因组中与 Ty3/gypsy 同源的完整的包含包膜的 ERV，发现它们广泛分布在包括刺胞动物、栉水母和被囊动物等古代动物在内的分类群中。
- Keywords: genes, ervs, envelope, retrotransposons, host

### 25. [来自相同细胞的匹配基因组和蛋白质组的细胞类型解析空间蛋白质组学](https://www.biorxiv.org/content/10.64898/2026.07.09.737478v1)
- Original title: Cell-type-resolved spatial proteogenomics from matched genome and proteome of the same cells
- Authors: Zwiebel, M., Wahle, M., Stadler, R., Levesque, M. P., Dummer, R. et al.
- Meta: 2026-07-10 | biochemistry | DOI: 10.64898/2026.07.09.737478
- 中文摘要: 同一细胞的基因组和蛋白质组很少一起测量，这在癌症中尤其重要，因为体细胞突变在克隆之间存在差异并导致疾病。我们证明，单个标准蛋白质组学提取吸头可以在消化后保留肽在吸头上，同时基因组 DNA 进入通常丢弃的流通液中。与深度视觉蛋白质组学相结合，流通共分离可以从档案 FFPE 组织中进行细胞类型解析的空间蛋白质基因组学，这在黑色素瘤中得到了证明。
- Abstract: The genome and proteome of the same cells are rarely measured together, which is especially consequential in cancer, where somatic mutations vary across clones and drive disease. We show that a single standard proteomics extraction tip can retain peptides on-tip after digestion while genomic DNA passes into the normally discarded flowthrough. Combined with Deep Visual Proteomics, flowthrough co-isolation enables cel...
- Summary (fallback): 机器翻译摘要显示：同一细胞的基因组和蛋白质组很少一起测量，这在癌症中尤其重要，因为体细胞突变在克隆之间存在差异并导致疾病。我们证明，单个标准蛋白质组学提取吸头可以在消化后保留肽在吸头上，同时基因组 DNA 进入通常丢弃的流通液中。与深度视觉蛋白质组学相结合，流通共分离可以从档案 FFPE 组织中进行细胞类型解析的空间蛋白质基因组学，这在黑色素瘤中得到了证明。
- Keywords: cell-type-resolved, spatial, proteogenomics, genome, proteome

### 26. [MHC 结合肽的混合量子经典从头设计](https://www.biorxiv.org/content/10.64898/2026.07.09.736951v1)
- Original title: Hybrid quantum-classical de novo design of MHC-binding peptides
- Authors: Engdal, E. S., Funk, J., Bacarreza, O., Machado, L., Johansen, K. H. et al.
- Meta: 2026-07-10 | biochemistry | DOI: 10.64898/2026.07.09.736951
- 中文摘要: 深度生成模型已成为设计治疗分子的主要方法，但有效探索巨大的生物分子序列空间仍然很困难，特别是对于训练数据有限的目标。生成模型的先验分布决定了它探索的序列空间区域，最近的工作表明，从量子处理器采样的非经典分布可以作为默认使用的因式分解高斯先验的结构化替代方案。这些先验是否有助于复杂的生物设计任务在很大程度上尚未得到检验。在这里，我们提出了第一个端到端混合量子经典管道，用于 MHC I 类结合肽的从头设计，将生成对抗网络 (GAN) 与从真实光子量子处理器采样的潜在向量耦合。
- Abstract: Deep generative models have become a leading approach for designing therapeutic molecules, yet efficiently exploring vast biomolecular sequence spaces remains difficult, particularly for targets with limited training data. The prior distribution that seeds a generative model shapes which regions of sequence space it explores, and recent work suggests that non-classical distributions sampled from quantum processors c...
- Summary (fallback): 机器翻译摘要显示：深度生成模型已成为设计治疗分子的主要方法，但有效探索巨大的生物分子序列空间仍然很困难，特别是对于训练数据有限的目标。生成模型的先验分布决定了它探索的序列空间区域，最近的工作表明，从量子处理器采样的非经典分布可以作为默认使用的因式分解高斯先验的结构化替代方案。这些先验是否有助于复杂的生物设计任务在很大程度上尚未得到检验。在这里，我们提出了第一个端到端混合量子经典管道，用于 MHC I 类结合肽的从头设计，将生成对抗网络 (GAN) 与从真实光子量子处理器采样的潜在向量耦合。
- Keywords: design, generative, priors, alleles, peptides

### 27. [I-F3 CRISPR 相关转座酶的转座子末端识别和配对](https://www.biorxiv.org/content/10.64898/2026.07.09.737429v1)
- Original title: Transposon end recognition and pairing by I-F3 CRISPR-associated transposase
- Authors: Truong, V., Miller, D., Fatma, S., Sheng, Y., Pindi, C. et al.
- Meta: 2026-07-10 | biochemistry | DOI: 10.64898/2026.07.09.737429
- 中文摘要: 为了开发基于 CRISPR 相关转座子 (CAST) 的基因治疗工具，必须定义转座过程中转座子末端的识别和配对方式。 Tn7 样转座子通常包含不对称的左端和右端序列，位于侧翼并定义 DNA 货物。然而，转座酶如何识别这些不同的序列并将它们组装成配对末端复合物以进行剪切和粘贴转座仍然未知。在这里，我们展示了 I-F3 型 (VchCAST) CAST 转座酶 TnsB 与转座子 DNA 末端和宿主因子 IHF 复合的冷冻电镜结构，以及生物化学、分子动力学和体内分析。我们的结构揭示了组装的化学计量和结构，以及适应转座子末端不对称性所需的 DNA 扭曲。
- Abstract: To develop gene therapy tools based on CRISPR-associated transposons (CASTs), it is essential to define how transposon ends are recognized and paired during transposition. Tn7-like transposons typically contain asymmetric left- and right-end sequences that flank and define DNA cargo. However, how the transposase recognizes these different sequences and assembles them into a paired end complex for cut-and-paste trans...
- Summary (fallback): 机器翻译摘要显示：为了开发基于 CRISPR 相关转座子 (CAST) 的基因治疗工具，必须定义转座过程中转座子末端的识别和配对方式。 Tn7 样转座子通常包含不对称的左端和右端序列，位于侧翼并定义 DNA 货物。然而，转座酶如何识别这些不同的序列并将它们组装成配对末端复合物以进行剪切和粘贴转座仍然未知。在这里，我们展示了 I-F3 型 (VchCAST) CAST 转座酶 TnsB 与转座子 DNA 末端和宿主因子 IHF 复合的冷冻电镜结构，以及生物化学、分子动力学和体内分析。我们的结构揭示了组装的化学计量和结构，以及适应转座子末端不对称性所需的 DNA 扭曲。
- Keywords: transposon, pairing, transposase, ends, transposition

### 28. [扩展遗传密码以生成具有脉管系统和小胶质细胞的人脑类器官](https://www.biorxiv.org/content/10.64898/2026.07.08.737383v1)
- Original title: Expanding genetic code to generate human brain organoids with both vasculature and microglia
- Authors: Lin, H., Wang, Y., Du, H., Qin, Y., Zhang, H. et al.
- Meta: 2026-07-10 | bioengineering | DOI: 10.64898/2026.07.08.737383
- 中文摘要: 脑类器官为研究人类大脑发育和疾病提供了宝贵的模型系统。然而，建立具有包括脉管系统和免疫细胞在内的多种细胞谱系的高保真脑类器官仍然是一个巨大的挑战。在这里，我们提出了一种新策略，通过位点特异性蛋白质工程，使用遗传密码扩展技术（GCE-T）生成具有脉管系统和小胶质细胞样细胞的人类大脑类器官。该策略通过 PiggyBac 转座子系统将正交基因翻译机制整合到 hPSC 中，从而能够暂时控制 hPSC 衍生的脑类器官中的 ETV2 表达和内皮分化。血管化的人脑类器官（vhCO）表现出多种细胞谱系和血脑屏障（BBB）特征的协调发育。
- Abstract: Brain organoids offer an invaluable model system for studying human brain development and disease. However, the establishment of high-fidelity brain organoids with multiple cell lineages including vasculature and immune cells remains a huge challenge. Here, we present a new strategy to generate human cerebral organoids with vasculature and microglia-like cells using genetic code expansion technology (GCE-T) via site...
- Summary (fallback): 机器翻译摘要显示：脑类器官为研究人类大脑发育和疾病提供了宝贵的模型系统。然而，建立具有包括脉管系统和免疫细胞在内的多种细胞谱系的高保真脑类器官仍然是一个巨大的挑战。在这里，我们提出了一种新策略，通过位点特异性蛋白质工程，使用遗传密码扩展技术（GCE-T）生成具有脉管系统和小胶质细胞样细胞的人类大脑类器官。该策略通过 PiggyBac 转座子系统将正交基因翻译机制整合到 hPSC 中，从而能够暂时控制 hPSC 衍生的脑类器官中的 ETV2 表达和内皮分化。血管化的人脑类器官（vhCO）表现出多种细胞谱系和血脑屏障（BBB）特征的协调发育。
- Keywords: organoids, brain, human, vhcos, vasculature

### 29. [肝素模拟聚合物的区域选择性硫酸化定义了体内活性](https://www.biorxiv.org/content/10.64898/2026.07.09.737190v1)
- Original title: Regio-selective sulfation of heparin mimicking polymers defines in vivo activity
- Authors: Grinstaff, M., Loffredo, M., Ham, H. O., Varghese, M., Haller, C. et al.
- Meta: 2026-07-10 | bioengineering | DOI: 10.64898/2026.07.09.737190
- 中文摘要: 肝素是一种天然来源的糖胺聚糖，是世界上最常用的抗血栓栓塞药物。然而，肝素的生物来源本质上会导致批次间的差异、大的分散指数和潜在的污染，从而导致活性不一致和患者依赖性剂量反应。因此，新型合成抗凝剂引起了人们的浓厚兴趣，特别是那些模仿肝素同时能够改变聚合物结构和组成以优化性能的抗凝剂。在此，我们报告了明确的、区域选择性功能化的二硫酸化聚酰胺糖（disulPAS）的策略、合成和评估，包括探索分子量和硫酸化密度对抗凝血活性的结构-功能关系。
- Abstract: Heparin, a naturally derived glycosaminoglycan, is the most commonly used anti-thromboembolic in the world. However, the biological origin of heparin inherently results in batch-to-batch variability, large dispersity indexes, and potential contamination, leading to inconsistent activity and patient-dependent dose-response. As such, new synthetic anticoagulants are of keen interest, particularly those that mimic hepa...
- Summary (fallback): 机器翻译摘要显示：肝素是一种天然来源的糖胺聚糖，是世界上最常用的抗血栓栓塞药物。然而，肝素的生物来源本质上会导致批次间的差异、大的分散指数和潜在的污染，从而导致活性不一致和患者依赖性剂量反应。因此，新型合成抗凝剂引起了人们的浓厚兴趣，特别是那些模仿肝素同时能够改变聚合物结构和组成以优化性能的抗凝剂。在此，我们报告了明确的、区域选择性功能化的二硫酸化聚酰胺糖（disulPAS）的策略、合成和评估，包括探索分子量和硫酸化密度对抗凝血活性的结构-功能关系。
- Keywords: heparin, activity, sulfation, clotting, vivo

### 30. [折叠酶缩合物的化学增强加速氧化蛋白质折叠](https://www.biorxiv.org/content/10.64898/2026.07.08.737393v1)
- Original title: Chemical Boosting of Foldase Condensates Accelerates Oxidative Protein Folding
- Authors: Watabe, M., Kuramochi, T., Fukushima, M., Kinoshita, M., Akiba, H. et al.
- Meta: 2026-07-10 | bioengineering | DOI: 10.64898/2026.07.08.737393
- 中文摘要: 动态生物分子凝聚体在细胞内区室化和生理功能中发挥着至关重要的作用。虽然用于分隔的工程工具已经扩展了附加功能，但直接放大生物相分离液滴内固有的催化机制仍然难以实现。在此，我们开发了一种基于蛋白质二硫键异构酶 A6 (PDIA6) 的相分离氧化折叠反应室，通过化学靶向其活性位点 CxxC 基序来增强 PDIA6 液滴内的酶活性。对位取代的 N-甲基化吡啶基甲硫醇 (pMePySH) 在体外 PDIA6 液滴中将牛胰蛋白酶抑制剂、胰岛素原和抗体的催化氧化折叠增强了 12 倍。此外，pMePySH 靶向内质网内的 PDIA6 病灶，显着促进胰岛素分泌。
- Abstract: Dynamic biomolecular condensates play crucial roles in intracellular compartmentalization and physiological functions. While engineering tools for compartmentalization have expanded add-on functionalities, directly amplifying the inherent catalytic machinery within biological phase-separated droplets has remained elusive. Herein, we developed a phase-separated oxidative folding reaction chamber based on protein disu...
- Summary (fallback): 机器翻译摘要显示：动态生物分子凝聚体在细胞内区室化和生理功能中发挥着至关重要的作用。虽然用于分隔的工程工具已经扩展了附加功能，但直接放大生物相分离液滴内固有的催化机制仍然难以实现。在此，我们开发了一种基于蛋白质二硫键异构酶 A6 (PDIA6) 的相分离氧化折叠反应室，通过化学靶向其活性位点 CxxC 基序来增强 PDIA6 液滴内的酶活性。对位取代的 N-甲基化吡啶基甲硫醇 (pMePySH) 在体外 PDIA6 液滴中将牛胰蛋白酶抑制剂、胰岛素原和抗体的催化氧化折叠增强了 12 倍。此外，pMePySH 靶向内质网内的 PDIA6 病灶，显着促进胰岛素分泌。
- Keywords: folding, within, pdia6, oxidative, protein

## medrxiv

### 1. [肯尼亚公共卫生紧急事件分类和升级的人工智能辅助决策支持系统的开发和评估](https://www.medrxiv.org/content/10.64898/2026.07.07.26357475v1)
- Original title: Development and Evaluation of Artificial Intelligence-Assisted Decision Support System for Public Health Emergency Classification and Escalation in Kenya
- Authors: Nanyingi, M., Osoro, E., Siwo, G. H., Ngere, I., Kadivane, S. et al.
- Meta: 2026-07-10 | public and global health | DOI: 10.64898/2026.07.07.26357475
- 中文摘要: 背景 公共卫生事件的及时评估、分类和升级对于有效应对疫情至关重要，但由于指导分散，升级标准解释各异，事件检测后的决策仍然具有挑战性。为了加强公共卫生应急管理，肯尼亚开发了突发公共卫生事件决策工具（DMT-PHE），这是一个事件评估、分类、通知和升级的框架。随后开发了支持人工智能 (AI) 的版本 DMT-PHE AI Agent，以通过决策支持来操作该框架。本研究描述了 DMT-PHE AI 代理的开发，并评估了其性能、可用​​性、安全性和用户可接受性。
- Abstract: Background Timely assessment, classification, and escalation of public health events are essential for effective outbreak response, yet decision-making after event detection remains challenging because of fragmented guidance and variable interpretation of escalation criteria.To strengthen public health emergency management, Kenya developed the Decision-Making Tool for Public Health Emergencies (DMT-PHE), a framework...
- Summary (fallback): 机器翻译摘要显示：背景 公共卫生事件的及时评估、分类和升级对于有效应对疫情至关重要，但由于指导分散，升级标准解释各异，事件检测后的决策仍然具有挑战性。为了加强公共卫生应急管理，肯尼亚开发了突发公共卫生事件决策工具（DMT-PHE），这是一个事件评估、分类、通知和升级的框架。随后开发了支持人工智能 (AI) 的版本 DMT-PHE AI Agent，以通过决策支持来操作该框架。本研究描述了 DMT-PHE AI 代理的开发，并评估了其性能、可用​​性、安全性和用户可接受性。
- Keywords: public, health, dmt-phe, agent, emergency

### 2. [改良的血栓弹力测定法能够快速、实时评估补体驱动的免疫血栓形成](https://www.medrxiv.org/content/10.64898/2026.06.30.26356356v1)
- Original title: A Modified Thromboelastometry Assay Enables Rapid, Real-Time Evaluation of Complement-Driven Immunothrombosis
- Authors: Papadimitriou, E., Natsi, A.-M., Papagoras, C., Mastellos, D., Tsironidou, V. et al.
- Meta: 2026-07-10 | health systems and quality improvement | DOI: 10.64898/2026.06.30.26356356
- 中文摘要: 简介 补体和凝血是紧密相连的系统，有助于免疫血栓形成，并可引发炎症或血栓性疾病。利用这种关系和串扰，我们开发了一种使用血栓弹力测定法（补体驱动免疫血栓形成的热弹性测定法；TCDI）功能性评估补体诱导的凝血活性的方法。方法 为了研究补体依赖性凝血激活，在存在或不存在基于坎普他汀的 C3 抑制剂 Cp40 的情况下，将患者的贫血小板血浆 (PPP) 与健康血液混合。分析来自健康对照 (n = 10) 或抗磷脂综合征 (APS; n = 6)、严重 COVID-19 (n = 13)、类风湿性关节炎 (RA; n = 7) 或 RA 患者滑液 (SF) 患者的 PPP 诱导健康血液中补体激活的能力。
- Abstract: Introduction Complement and coagulation are tightly interconnected systems that contribute to immunothrombosis and can drive inflammatory or thrombotic diseases. Leveraging this relationship and crosstalk we developed a method to functionally evaluate complement-induced coagulation activity using thromboelastometry (thermoelastometry of complement-driven immunothrombosis; TCDI). Methods To study the complement-depen...
- Summary (fallback): 机器翻译摘要显示：简介 补体和凝血是紧密相连的系统，有助于免疫血栓形成，并可引发炎症或血栓性疾病。利用这种关系和串扰，我们开发了一种使用血栓弹力测定法（补体驱动免疫血栓形成的热弹性测定法；TCDI）功能性评估补体诱导的凝血活性的方法。方法 为了研究补体依赖性凝血激活，在存在或不存在基于坎普他汀的 C3 抑制剂 Cp40 的情况下，将患者的贫血小板血浆 (PPP) 与健康血液混合。分析来自健康对照 (n = 10) 或抗磷脂综合征 (APS; n = 6)、严重 COVID-19 (n = 13)、类风湿性关节炎 (RA; n = 7) 或 RA 患者滑液 (SF) 患者的 PPP 诱导健康血液中补体激活的能力。
- Keywords: immunothrombosis, cp40, complement-driven, coagulation, tcdi

### 3. [将因果推理融入药物警戒：针对医疗保险受益人阿托伐他汀起始主动信号检测的目标试验模拟](https://www.medrxiv.org/content/10.64898/2026.07.01.26356874v1)
- Original title: Integrating Causal Inference into Pharmacovigilance: Target Trial Emulations for Proactive Signal Detection of Atorvastatin Initiation in Medicare Beneficiaries
- Authors: Rowan, C. G., Tran, M., Srivastava, S.
- Meta: 2026-07-10 | epidemiology | DOI: 10.64898/2026.07.01.26356874
- 中文摘要: 重要性：老年人的药物不良事件是一个巨大的公共卫生负担，但由于报告不足和缺乏明确的人群，自发报告系统未能很好地发现这些事件。这些限制对于老年人来说尤其令人担忧，他们在批准前试验中的代表性不足，但由于多重用药、多发病以及与年龄相关的药物代谢变化而面临较高的风险。目的：开发并应用一个主动的、基于索赔的药物警戒框架，使用序贯目标试验模拟来检测老年人的不良药物事件信号，以阿托伐他汀作为初始应用。方法：利用 Medicare 按服务收费索赔（2017-2019 年），我们研究了 65 岁或以上的心肌梗塞或脑梗塞后未接受过他汀类药物治疗的受益人。
- Abstract: Importance: Adverse drug events in older adults are a substantial public health burden, yet spontaneous reporting systems detect them poorly owing to underreporting and the lack of a defined population. These limitations are of particular concern for older adults, who are underrepresented in pre-approval trials yet at elevated risk owing to polypharmacy, multimorbidity, and age-related changes in drug metabolism. Ob...
- Summary (fallback): 机器翻译摘要显示：重要性：老年人的药物不良事件是一个巨大的公共卫生负担，但由于报告不足和缺乏明确的人群，自发报告系统未能很好地发现这些事件。这些限制对于老年人来说尤其令人担忧，他们在批准前试验中的代表性不足，但由于多重用药、多发病以及与年龄相关的药物代谢变化而面临较高的风险。目的：开发并应用一个主动的、基于索赔的药物警戒框架，使用序贯目标试验模拟来检测老年人的不良药物事件信号，以阿托伐他汀作为初始应用。方法：利用 Medicare 按服务收费索赔（2017-2019 年），我们研究了 65 岁或以上的心肌梗塞或脑梗塞后未接受过他汀类药物治疗的受益人。
- Keywords: atorvastatin, older, trial, drug, adults

### 4. [从流行病到地方病：巴西先天性寨卡综合症的纵向监测](https://www.medrxiv.org/content/10.64898/2026.07.07.26357442v1)
- Original title: From Epidemic to Endemic: Longitudinal Surveillance of Congenital Zika Syndrome in Brazil
- Authors: Oliveira Ferreira, R., Ma, H. L., Pestana Garcez, P., Zatz, M.
- Meta: 2026-07-10 | epidemiology | DOI: 10.64898/2026.07.07.26357442
- 中文摘要: 寨卡病毒（ZIKV）于2015年在巴西出现，引发了前所未有的先天性寨卡综合症（CZS）流行。十年后，评估 CZS 负担时间趋势和地方异质性的纵向分析仍然有限。利用 SINAN/DATASUS 和 RESP-小头畸形登记处（SVS/卫生部，2024 年 7 月更新）的公开数据，我们对 2015 年至 2023 年巴西的 ZIKV 感染和 CZS 进行了描述性生态分析。在 331,309 例通报的寨卡病例中（2015-2023 年），其中 213,350 例发生在 2016 年，其次是 2016 年。 2017年下降91.75%，此后持续低水平流行。在 3,751 例确诊的小头畸形病例中，1,828 例确诊为寨卡病毒感染。东北地区人口约占全国27%，但仍占确诊病例的75.4%。
- Abstract: Zika virus (ZIKV) emerged in Brazil in 2015, causing an unprecedented epidemic of Congenital Zika Syndrome (CZS). A decade later, longitudinal analyses evaluating temporal trends and subnational heterogeneity in CZS burden remain limited. Using publicly available data from SINAN/DATASUS and the RESP-Microcephaly registry (SVS/Ministry of Health, updated July 2024), we conducted a descriptive ecological analysis of Z...
- Summary (fallback): 机器翻译摘要显示：寨卡病毒（ZIKV）于2015年在巴西出现，引发了前所未有的先天性寨卡综合症（CZS）流行。十年后，评估 CZS 负担时间趋势和地方异质性的纵向分析仍然有限。利用 SINAN/DATASUS 和 RESP-小头畸形登记处（SVS/卫生部，2024 年 7 月更新）的公开数据，我们对 2015 年至 2023 年巴西的 ZIKV 感染和 CZS 进行了描述性生态分析。在 331,309 例通报的寨卡病例中（2015-2023 年），其中 213,350 例发生在 2016 年，其次是 2016 年。 2017年下降91.75%，此后持续低水平流行。在 3,751 例确诊的小头畸形病例中，1,828 例确诊为寨卡病毒感染。东北地区人口约占全国27%，但仍占确诊病例的75.4%。
- Keywords: zika, congenital, brazil, zikv, cases

### 5. [基于 RoPE 的免对准双流变压器，用于 NICU 中 PPG 引导的新生儿心电图分段修复](https://www.medrxiv.org/content/10.64898/2026.07.06.26357087v1)
- Original title: Alignment-Free RoPE-Based Dual-Stream Transformer for PPG-Guided Neonatal ECG Segment Inpainting in the NICU
- Authors: Choi, S., Gu, G., Kim, Y., Lee, S., Sim, S.-i. et al.
- Meta: 2026-07-10 | pediatrics | DOI: 10.64898/2026.07.06.26357087
- 中文摘要: 新生儿重症监护病房 (NICU) 中使用的粘附性心电图 (ECG) 电极可能会导致早产儿皮肤受伤。尽管已经探索了基于光电体积描记法（PPG）的心电图重建，但现有研究主要集中于成人数据，并且通常依赖直接的 PPG 到心电图映射或人工信号对齐，这可能不适合脉搏到达时间（PAT）高度可变的新生儿。在本研究中，我们提出了一种基于 RoPE 的免对齐双流 Transformer，用于使用并发 PPG 信号和双向心电图上下文重建缺失的新生儿心电图片段。从 159 名 NICU 患者中提取了总共 52,566 个 10 秒 ECG-PPG 窗口，并在患者级别进行分割以防止数据泄漏。
- Abstract: Adhesive electrocardiography (ECG) electrodes used in neonatal intensive care units (NICUs) may cause skin injury in premature infants. Although photoplethysmography (PPG)-based ECG reconstruction has been explored, existing studies have mainly focused on adult data and often rely on direct PPG-to-ECG mapping or artificial signal alignment, which may be unsuitable for neonates with highly variable pulse arrival time...
- Summary (fallback): 机器翻译摘要显示：新生儿重症监护病房 (NICU) 中使用的粘附性心电图 (ECG) 电极可能会导致早产儿皮肤受伤。尽管已经探索了基于光电体积描记法（PPG）的心电图重建，但现有研究主要集中于成人数据，并且通常依赖直接的 PPG 到心电图映射或人工信号对齐，这可能不适合脉搏到达时间（PAT）高度可变的新生儿。在本研究中，我们提出了一种基于 RoPE 的免对齐双流 Transformer，用于使用并发 PPG 信号和双向心电图上下文重建缺失的新生儿心电图片段。从 159 名 NICU 患者中提取了总共 52,566 个 10 秒 ECG-PPG 窗口，并在患者级别进行分割以防止数据泄漏。
- Keywords: neonatal, nicu, alignment-free, rope-based, dual-stream

### 6. [正念介导热瑜伽期间抑郁症状的改善：随机对照试验的二次分析](https://www.medrxiv.org/content/10.64898/2026.07.01.26353530v1)
- Original title: Mindfulness mediates depressive symptom improvement during heated yoga: A secondary analysis of a randomized controlled trial
- Authors: Copeland, D., Mac Giollabhui, N., Sylvia, L., Cetinkaya, D., Puzak, S. J. et al.
- Meta: 2026-07-10 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.01.26353530
- 中文摘要: 背景。尽管越来越多的证据表明生活方式干预可以减少抑郁症状，但这些影响背后的心理机制仍然知之甚少。这项研究检验了正念和沉思是否介导热瑜伽（HY）的抗抑郁作用，HY是一种结合身体活动、注意力训练和体温调节压力的多成分干预措施。方法。这种预先指定的二级中介分析建立在一项随机对照试验的基础上，其中 80 名患有中度至重度抑郁症 (IDS-CR > 23) 的成年人被随机分配到为期 8 周、每周两次的 HY 或候补名单对照。具有完整中介数据的子样本有助于沉思（n = 56）和正念（n = 60）模型。使用 10,000 个 bootstrap 重采样进行因果中介分析，通过第 4 周中介变量的变化估计对第 8 周抑郁症严重程度的间接影响。
- Abstract: Background. Despite growing evidence that lifestyle interventions reduce depressive symptoms, the psychological mechanisms underlying these effects remain poorly understood. This study examined whether mindfulness and rumination mediate the antidepressant effects of heated yoga (HY), a multicomponent intervention combining physical activity, attentional training, and thermoregulatory stress. Methods. This prespecifi...
- Summary (fallback): 机器翻译摘要显示：背景。尽管越来越多的证据表明生活方式干预可以减少抑郁症状，但这些影响背后的心理机制仍然知之甚少。这项研究检验了正念和沉思是否介导热瑜伽（HY）的抗抑郁作用，HY是一种结合身体活动、注意力训练和体温调节压力的多成分干预措施。方法。这种预先指定的二级中介分析建立在一项随机对照试验的基础上，其中 80 名患有中度至重度抑郁症 (IDS-CR > 23) 的成年人被随机分配到为期 8 周、每周两次的 HY 或候补名单对照。具有完整中介数据的子样本有助于沉思（n = 56）和正念（n = 60）模型。使用 10,000 个 bootstrap 重采样进行因果中介分析，通过第 4 周中介变量的变化估计对第 8 周抑郁症严重程度的间接影响。
- Keywords: mindfulness, effects, rumination, depressive, week

### 7. [从怀孕到产后五年母子关系满意度的轨迹和预测因素](https://www.medrxiv.org/content/10.64898/2026.07.01.26356966v1)
- Original title: TRAJECTORY AND PREDICTORS OF MATERNAL RELATIONSHIP SATISFACTION FROM PREGNANCY TO FIVE YEARS POSTPARTUM
- Authors: Crowther, M. E., Strakie, S. C. O., Pinnington, D. M., Drummond, S. P., Bei, B.
- Meta: 2026-07-10 | psychiatry and clinical psychology | DOI: 10.64898/2026.07.01.26356966
- 中文摘要: 目的：关系满意度是女性心理健康和幸福结果的关键因素，然而，关系满意度可能会在压力和不确定时期（例如围产期）发生变化。虽然围产期积极的浪漫关系可能会带来好处，但关系满意度的变化以及可能对它们产生纵向影响的因素目前尚不清楚。方法：157 名怀孕后期（妊娠 30 周）的女性参与了从怀孕到产后五年、跨越 8 个时间点的关系满意度的纵向分析。该研究是对睡眠和饮食干预的随机对照试验的二次分析。潜在增长模型用于检查关系满意度随时间变化的轨迹，并探索该轨迹的预测因素。
- Abstract: Purpose: Relationship satisfaction is a key factor in women s mental health and wellbeing outcomes, however, relationship satisfaction may change in times of stress and uncertainty, such as the perinatal period. While positive romantic relationships during the perinatal period may offer benefits, changes in relationship satisfaction and what may contribute to them longitudinally is not currently well understood. Met...
- Summary (fallback): 机器翻译摘要显示：目的：关系满意度是女性心理健康和幸福结果的关键因素，然而，关系满意度可能会在压力和不确定时期（例如围产期）发生变化。虽然围产期积极的浪漫关系可能会带来好处，但关系满意度的变化以及可能对它们产生纵向影响的因素目前尚不清楚。方法：157 名怀孕后期（妊娠 30 周）的女性参与了从怀孕到产后五年、跨越 8 个时间点的关系满意度的纵向分析。该研究是对睡眠和饮食干预的随机对照试验的二次分析。潜在增长模型用于检查关系满意度随时间变化的轨迹，并探索该轨迹的预测因素。
- Keywords: relationship, satisfaction, pregnancy, postpartum, trajectory

### 8. [滤泡外 B 细胞分化和炎症环境之间的前馈循环控制系统性红斑狼疮的缓解和复发](https://www.medrxiv.org/content/10.64898/2026.07.03.26356448v1)
- Original title: A Feed-Forward Loop Between Extrafollicular B Cell Differentiation and the Inflammatory Milieu Governs Remission and Relapse in Systemic Lupus Erythematosus
- Authors: Noethling, D.-M., Anoshkin, K., Gavin, P. G., Rothe, T., Bucci, L. et al.
- Meta: 2026-07-10 | rheumatology | DOI: 10.64898/2026.07.03.26356448
- 中文摘要: 系统性红斑狼疮 (SLE) 由致病性 B 细胞驱动。然而，为什么一些接受 B 细胞去除的患者获得持久缓解，而另一些患者却失败，仍不清楚。在此，我们使用 CD19 定向嵌合抗原受体 (CAR) T 细胞疗法作为机制探针，对 18 名难治性 SLE 患者进行治疗，纵向随访长达 40 个月。我们表明，持久、无药物缓解不仅仅取决于 B 细胞耗竭的深度，还取决于滤泡外 (EF) B 细胞分化轨迹的消除 - 具体来说，是激活的幼稚 B 细胞前体和 CD11c+ T-bet+ 双阴性2型B细胞。在长期应答者中，B 细胞重建重现了健康的个体发育，而 EF 通路仍然被截断，与富含干扰素的环境崩溃和 PD1hi T 外周辅助细胞收缩同时发生。
- Abstract: Systemic lupus erythematosus (SLE) is driven by pathogenic B cells. Yet, why some patients receiving B cell depletion achieve durable remission, whilst others fail remains unclear. Herewe use CD19-directed chimeric antigen receptor (CAR) T cell therapy as a mechanistic probein 18 patients with refractory SLE, with longitudinal follow-up extending up to 40 months.We show that durable, drug-free remission is defined n...
- Summary (fallback): 机器翻译摘要显示：系统性红斑狼疮 (SLE) 由致病性 B 细胞驱动。然而，为什么一些接受 B 细胞去除的患者获得持久缓解，而另一些患者却失败，仍不清楚。在此，我们使用 CD19 定向嵌合抗原受体 (CAR) T 细胞疗法作为机制探针，对 18 名难治性 SLE 患者进行治疗，纵向随访长达 40 个月。我们表明，持久、无药物缓解不仅仅取决于 B 细胞耗竭的深度，还取决于滤泡外 (EF) B 细胞分化轨迹的消除 - 具体来说，是激活的幼稚 B 细胞前体和 CD11c+ T-bet+ 双阴性2型B细胞。在长期应答者中，B 细胞重建重现了健康的个体发育，而 EF 通路仍然被截断，与富含干扰素的环境崩溃和 PD1hi T 外周辅助细胞收缩同时发生。
- Keywords: cell, cells, differentiation, remission, extrafollicular

### 9. [脑膨出相关颞叶癫痫的类淋巴系统](https://www.medrxiv.org/content/10.64898/2026.07.02.26356654v1)
- Original title: Glymphatic System in Temporal Lobe Epilepsy Associated with Encephalocele
- Authors: Di Giacomo, R., Biancheri, D., Burini, A., Doniselli, F. M., Rossini, L. et al.
- Meta: 2026-07-10 | neurology | DOI: 10.64898/2026.07.02.26356654
- 中文摘要: 目的 颞叶脑膨出 (ENC) 是耐药性颞叶癫痫 (TLE) 的诊断不足的原因，通常与特发性颅内高压 (IIH) 相关。新的证据表明 IIH 和 TLE 均存在类淋巴系统功能障碍。我们研究了与 ENC 相关的 TLE 中的类淋巴标志物，与不同病因的无癫痫术后 TLE 对照进行比较。方法 对 13 例 TLE-ENC 患者和 12 例 TLE 对照患者的手术标本进行分析。组织学类淋巴标志物包括水通道蛋白 4 (AQP4)、胶质原纤维酸性蛋白 (GFAP)、平足蛋白 (PDPN)、血管周围间隙 (PVS) 扩大和血管密度。高分辨率 MRI 用于评估整体 PVS 评分。
- Abstract: Objective Temporal lobe encephaloceles (ENC) are underdiagnosed causes of drug-resistant temporal lobe epilepsy (TLE), frequently associated with idiopathic intracranial hypertension (IIH). Emerging evidence suggests glymphatic system dysfunction in both IIH and TLE. We investigated glymphatic markers in TLE associated with ENC compared with seizure-free postoperative TLE controls of different aetiology. Methods Sur...
- Summary (fallback): 机器翻译摘要显示：目的 颞叶脑膨出 (ENC) 是耐药性颞叶癫痫 (TLE) 的诊断不足的原因，通常与特发性颅内高压 (IIH) 相关。新的证据表明 IIH 和 TLE 均存在类淋巴系统功能障碍。我们研究了与 ENC 相关的 TLE 中的类淋巴标志物，与不同病因的无癫痫术后 TLE 对照进行比较。方法 对 13 例 TLE-ENC 患者和 12 例 TLE 对照患者的手术标本进行分析。组织学类淋巴标志物包括水通道蛋白 4 (AQP4)、胶质原纤维酸性蛋白 (GFAP)、平足蛋白 (PDPN)、血管周围间隙 (PVS) 扩大和血管密度。高分辨率 MRI 用于评估整体 PVS 评分。
- Keywords: glymphatic, patients, tle-enc, aqp4, temporal

### 10. [社会概念依赖于腹侧前额叶皮层和岛叶中的通用前颞中枢和社会辐条](https://www.medrxiv.org/content/10.64898/2026.07.02.26357102v1)
- Original title: Social concepts rely on a domain-general anterior-temporal hub and social spokes in ventral prefrontal cortex and insula
- Authors: Rouse, M., Garrard, P., Rowe, J., Lambon Ralph, M., Rogers, T.
- Meta: 2026-07-10 | neurology | DOI: 10.64898/2026.07.02.26357102
- 中文摘要: 围绕社会概念的神经基础的长期争论涉及前颞叶（ATL）的作用。一种观点认为，ATL 次区域专门致力于社会知识；另一种观点认为，ATL 构成了概念知识的通用领域中心，但具有分级的功能专业化，具体取决于与特定模态辐条的连接性。由于社会和非社会知识测试中存在许多混杂因素，这些立场很难裁定。我们通过额颞叶痴呆 (FTD) 知识评估的三项创新来应对这些挑战。首先，我们引入一个新任务来控制几个潜在的混淆。其次，我们将混合线性模型应用于行为数据分析，从而进一步控制混杂因素。
- Abstract: A long-standing debate surrounding the neural bases of social concepts concerns the role of anterior temporal lobe (ATL). One perspective suggests ATL subregions are dedicated specifically to social knowledge; another suggests the ATLs constitute a domain-general hub for conceptual knowledge, but with graded functional specialisation depending on connectivity to modality specific spokes. The positions have been diff...
- Summary (fallback): 机器翻译摘要显示：围绕社会概念的神经基础的长期争论涉及前颞叶（ATL）的作用。一种观点认为，ATL 次区域专门致力于社会知识；另一种观点认为，ATL 构成了概念知识的通用领域中心，但具有分级的功能专业化，具体取决于与特定模态辐条的连接性。由于社会和非社会知识测试中存在许多混杂因素，这些立场很难裁定。我们通过额颞叶痴呆 (FTD) 知识评估的三项创新来应对这些挑战。首先，我们引入一个新任务来控制几个潜在的混淆。其次，我们将混合线性模型应用于行为数据分析，从而进一步控制混杂因素。
- Keywords: social, knowledge, concepts, factors, non-social

### 11. [使用高通量方法鉴定帕金森病痴呆的血液蛋白质组标记物](https://www.medrxiv.org/content/10.64898/2026.06.30.26356774v1)
- Original title: Identifying Blood Proteomic Markers of Parkinson's Disease Dementia Using High-Throughput Approaches
- Authors: Real, R., Ravazio, R., Nodehi, A., Ben-Shlomo, Y., Williams, N. et al.
- Meta: 2026-07-10 | neurology | DOI: 10.64898/2026.06.30.26356774
- 中文摘要: 简介：帕金森病 (PD) 表现为运动和非运动症状，包括痴呆，但认知能力下降的严重程度和速度各不相同，临床上难以预测。方法：我们使用高通量 SomaScan(R) 测定法对 834 名帕金森病患者的基线血清蛋白进行了定量，并进行了 Cox 回归以确定与痴呆症后续发展相关的蛋白。候选生物标志物蛋白在独立队列的 371 名个体中进行了复制并进行了荟萃分析。结果：与痴呆进展显着相关的蛋白质靶标主要涉及突触可塑性、蛋白质降解/溶酶体功能和细胞外基质组织。孟德尔随机化进一步揭示 Nogo 受体 RTN4R 的变化可能与路易体痴呆的发展存在因果关系。
- Abstract: INTRODUCTION: Parkinson's disease (PD) presents with motor and non-motor symptoms, including dementia, but the severity and rate of cognitive decline are heterogeneous and difficult to predict clinically. METHODS: We quantified baseline serum proteins with the high-throughput SomaScan(R) assay in 834 PD individuals and performed Cox regression to identify proteins associated with subsequent development of dementia....
- Summary (fallback): 机器翻译摘要显示：简介：帕金森病 (PD) 表现为运动和非运动症状，包括痴呆，但认知能力下降的严重程度和速度各不相同，临床上难以预测。方法：我们使用高通量 SomaScan(R) 测定法对 834 名帕金森病患者的基线血清蛋白进行了定量，并进行了 Cox 回归以确定与痴呆症后续发展相关的蛋白。候选生物标志物蛋白在独立队列的 371 名个体中进行了复制并进行了荟萃分析。结果：与痴呆进展显着相关的蛋白质靶标主要涉及突触可塑性、蛋白质降解/溶酶体功能和细胞外基质组织。孟德尔随机化进一步揭示 Nogo 受体 RTN4R 的变化可能与路易体痴呆的发展存在因果关系。
- Keywords: dementia, proteins, individuals, associated, development

### 12. [使用联合脑电图和压缩频谱阵列特征进行新生儿癫痫发作检测：机器学习概念验证研究](https://www.medrxiv.org/content/10.64898/2026.07.02.26354953v1)
- Original title: Neonatal Seizure Detection Using Combined aEEG and Compressed Spectral Array Features: A Machine-Learning Proof-of-Concept Study
- Authors: Edoigiawerie, S., Henry, J., Beaulieu-Jones, B., David, H., Issa, N.
- Meta: 2026-07-10 | neurology | DOI: 10.64898/2026.07.02.26354953
- 中文摘要: 背景 使用振幅积分脑电图 (aEEG) 和压缩频谱阵列 (CSA) 构建临床可转化的新生儿癫痫发作检测算法。方法 使用带注释的新生儿脑电图的公共数据集，从左右顶叶电极中提取 aEEG 和 CSA 的特征。然后，使用这些功能来训练和测试三种机器学习分类器：随机森林 (RF)、支持向量机 (SVM) 和人工神经网络 (ANN)。结果 经过训练的 RF、SVM 和 ANN 分类器捕获癫痫发作时间段的曲线下面积 (AUC) 分别为 0.80、0.69 和 0.79，捕获癫痫发作和非癫痫发作时间段的平均准确度分别为 0.91、0.90 和 0.92。
- Abstract: Background To build a clinically translatable neonatal seizure detection algorithm using amplitude-integrated electroencephalography (aEEG) and compressed spectral array (CSA). Methods Using a public dataset of annotated neonatal EEGs, features of the aEEG and CSA were extracted from the left and right centroparietal electrodes. These features were then used to train and test three machine learning classifiers, Rand...
- Summary (fallback): 机器翻译摘要显示：背景 使用振幅积分脑电图 (aEEG) 和压缩频谱阵列 (CSA) 构建临床可转化的新生儿癫痫发作检测算法。方法 使用带注释的新生儿脑电图的公共数据集，从左右顶叶电极中提取 aEEG 和 CSA 的特征。然后，使用这些功能来训练和测试三种机器学习分类器：随机森林 (RF)、支持向量机 (SVM) 和人工神经网络 (ANN)。结果 经过训练的 RF、SVM 和 ANN 分类器捕获癫痫发作时间段的曲线下面积 (AUC) 分别为 0.80、0.69 和 0.79，捕获癫痫发作和非癫痫发作时间段的平均准确度分别为 0.91、0.90 和 0.92。
- Keywords: seizure, features, neonatal, detection, aeeg

### 13. [口咽放疗后放射相关吞咽困难的四种纵向表型：潜在类别轨迹分析](https://www.medrxiv.org/content/10.64898/2026.07.06.26357052v1)
- Original title: Four longitudinal phenotypes of radiation-associated dysphagia following oropharyngeal radiotherapy: a latent class trajectory analysis
- Authors: Manduchi, B., Barbon, C. E., Moreno, A. C., Peterson, C. B., Swanson, D. M. et al.
- Meta: 2026-07-10 | oncology | DOI: 10.64898/2026.07.06.26357052
- 中文摘要: 背景和目的。接受放疗 (RT) 治疗的口咽癌 (OPC) 患者在恢复过程中表现出不同程度的放射相关吞咽困难 (RAD)，但大多数生存模型通常对 RAD 进行统一治疗。本研究旨在根据从治疗前到 RT 后 30 个月的成像分级吞咽功能，识别不同的、数据驱动的 RAD 纵向表型，并表征其基线预测因子。材料和方法。将异质线性混合效应潜在类别轨迹模型应用于 Stiefel MDA-OPC 前瞻性注册表的纵向 DIGEST 评分。符合条件的患者在基线和 RT 后 30 个月之间进行了 [≥]3 次改良吞钡 (MBS) 评估。跨功能形式和 1-5 个潜在类别对模型进行评估；最终选择使用贝叶斯信息准则。
- Abstract: Background and purpose. Patients with oropharyngeal cancer (OPC) treated with radiotherapy (RT) exhibit heterogeneous courses of radiation-associated dysphagia (RAD) during recovery, yet most survivorship models typically treat RAD uniformly. This study aimed to identify distinct, data-driven RAD longitudinal Phenotypes based on imaging-graded swallow function from pre-treatment to 30 months post-RT and to character...
- Summary (fallback): 机器翻译摘要显示：背景和目的。接受放疗 (RT) 治疗的口咽癌 (OPC) 患者在恢复过程中表现出不同程度的放射相关吞咽困难 (RAD)，但大多数生存模型通常对 RAD 进行统一治疗。本研究旨在根据从治疗前到 RT 后 30 个月的成像分级吞咽功能，识别不同的、数据驱动的 RAD 纵向表型，并表征其基线预测因子。材料和方法。将异质线性混合效应潜在类别轨迹模型应用于 Stiefel MDA-OPC 前瞻性注册表的纵向 DIGEST 评分。符合条件的患者在基线和 RT 后 30 个月之间进行了 [≥]3 次改良吞钡 (MBS) 评估。跨功能形式和 1-5 个潜在类别对模型进行评估；最终选择使用贝叶斯信息准则。
- Keywords: phenotypes, longitudinal, baseline, four, latent

### 14. [年轻发病肺癌风险和分子亚型的种系决定因素](https://www.medrxiv.org/content/10.64898/2026.06.30.26356693v1)
- Original title: Germline determinants of risk and molecular subtype in young-onset lung cancer
- Authors: LoPiccolo, J., Collins, R. L., Fields, N., Nakagawa, C., Taraszka, K. et al.
- Meta: 2026-07-10 | oncology | DOI: 10.64898/2026.06.30.26356693
- 中文摘要: 年轻发病的肺癌富含从不吸烟和癌基因驱动的肿瘤，但其遗传基础仍不清楚。我们对 251 例年轻发病的肺癌病例（中位年龄 37 岁）进行了种系全基因组测序，并与从不吸烟病例（n = 196；中位年龄 68）和无癌症对照（n = 1,883）进行了联合分析。我们在 55 个癌症相关基因组中发现了罕见有害编码变异的富集，包括 EGFR/ERBB2 信号传导和先前肺癌 GWAS 涉及的基因。对罕见编码变异的全外显子组分析证实 TP53 是一种渗透性肺癌易感基因（比值比 [OR]=36.1，p=1.02x10-7），并发现了两种新的全外显子组显着肿瘤亚型依赖性关联：融合驱动型肿瘤中的 IREB2（p=1.39x10-6）和融合阴性肿瘤中的 SMAD6（p=2.05x10-6）。
- Abstract: Young-onset lung cancer is enriched for never-smoking and oncogene-driven tumors, yet its inherited genetic basis remains poorly defined. We performed germline whole-genome sequencing in 251 young-onset lung cancer cases (median age 37), which we jointly analyzed with never-smoking cases (n=196; median age 68) and cancer-free controls (n=1,883). We identified enrichments of rare deleterious coding variants across 55...
- Summary (fallback): 机器翻译摘要显示：年轻发病的肺癌富含从不吸烟和癌基因驱动的肿瘤，但其遗传基础仍不清楚。我们对 251 例年轻发病的肺癌病例（中位年龄 37 岁）进行了种系全基因组测序，并与从不吸烟病例（n = 196；中位年龄 68）和无癌症对照（n = 1,883）进行了联合分析。我们在 55 个癌症相关基因组中发现了罕见有害编码变异的富集，包括 EGFR/ERBB2 信号传导和先前肺癌 GWAS 涉及的基因。对罕见编码变异的全外显子组分析证实 TP53 是一种渗透性肺癌易感基因（比值比 [OR]=36.1，p=1.02x10-7），并发现了两种新的全外显子组显着肿瘤亚型依赖性关联：融合驱动型肿瘤中的 IREB2（p=1.39x10-6）和融合阴性肿瘤中的 SMAD6（p=2.05x10-6）。
- Keywords: lung, cancer, germline, risk, young-onset

### 15. [肾上腺肿瘤患者血清脂质组学变化的初步研究](https://www.medrxiv.org/content/10.64898/2026.07.01.26356676v1)
- Original title: A Pilot Study on Serum Lipidomic Alterations in Patients with Adrenal Tumors
- Authors: Chocholouskova, M., Ctvrtlik, F., Tudos, Z., Hartmann, I., Schovanek, J. et al.
- Meta: 2026-07-10 | oncology | DOI: 10.64898/2026.07.01.26356676
- 中文摘要: 肾上腺皮质癌（ACC）是一种罕见的侵袭性恶性肿瘤，由于影像学和生化特征重叠，给诊断带来了重大挑战，特别是在将其与其他肾上腺肿瘤（如腺瘤和嗜铬细胞瘤）区分开来时。为了更早、更准确地对这种罕见癌症进行分类，迫切需要改进的非侵入性工具。这项初步研究分析了 ACC、嗜铬细胞瘤和腺瘤患者与健康志愿者的血清脂质组学特征。最显着的变化发生在鞘磷脂 (SM) 和二酰甘油 (DG) 中。所有肿瘤样本均显示极长奇数链 SM 减少（例如 SM 39:1、SM 41:1、SM 41:2）和 DG 升高（例如 DG 34:1、DG 34:2、DG 36:2）。这些异常在恶性肿瘤中最为明显：ACC 和转移瘤 (AUC = 0.933)，其次是嗜铬细胞瘤 (AUC = 0.800) 和腺瘤 (AUC = 0.711)。
- Abstract: Adrenocortical carcinoma (ACC) is a rare, aggressive malignancy posing significant diagnostic challenges, particularly in distinguishing it from other adrenal tumors, such as adenoma and pheochromocytoma, due to overlapping imaging and biochemical features. Improved non-invasive tools are critically needed for earlier, more accurate classification of this rare cancer. This pilot study analyzed serum lipidomic profil...
- Summary (fallback): 机器翻译摘要显示：肾上腺皮质癌（ACC）是一种罕见的侵袭性恶性肿瘤，由于影像学和生化特征重叠，给诊断带来了重大挑战，特别是在将其与其他肾上腺肿瘤（如腺瘤和嗜铬细胞瘤）区分开来时。为了更早、更准确地对这种罕见癌症进行分类，迫切需要改进的非侵入性工具。这项初步研究分析了 ACC、嗜铬细胞瘤和腺瘤患者与健康志愿者的血清脂质组学特征。最显着的变化发生在鞘磷脂 (SM) 和二酰甘油 (DG) 中。所有肿瘤样本均显示极长奇数链 SM 减少（例如 SM 39:1、SM 41:1、SM 41:2）和 DG 升高（例如 DG 34:1、DG 34:2、DG 36:2）。这些异常在恶性肿瘤中最为明显：ACC 和转移瘤 (AUC = 0.933)，其次是嗜铬细胞瘤 (AUC = 0.800) 和腺瘤 (AUC = 0.711)。
- Keywords: pheochromocytoma, lipidomic, adrenal, adenoma, tumor

### 16. [探索利益相关者对肩峰下疼痛综合征患者共同决策的内容、交付和情境交付的看法：一项包含未来研讨会和访谈的多方法研究](https://www.medrxiv.org/content/10.64898/2026.07.02.26356879v1)
- Original title: Exploring stakeholder perspectives on the content, delivery, and contextual delivery of shared decision-making for people living with subacromial pain syndrome: a multimethod study with future workshops and interviews
- Authors: Lyng, K. D., Johansen, S. K., Foster, N. E., Olesen, J. L., Thomsen, J. L. et al.
- Meta: 2026-07-10 | pain medicine | DOI: 10.64898/2026.07.02.26356879
- 中文摘要: 背景：共享决策 (SDM) 是以患者为中心的护理的关键组成部分，适用于因慢性肌肉骨骼疼痛（包括肩峰下疼痛综合征 (SAPS)）而咨询医疗保健的人。有限的研究探讨了患者、亲属和医疗保健专业人员如何看待 SDM 在初级保健中管理 SAPS 的内容和交付。因此，本研究旨在探讨利益相关者对 SAPS 特定情境 SDM 干预的内容、交付和情境要求的看法，并确定共同的挑战和共同开发想法，为干预措施的制定提供信息。方法：我们举办了三个独立的未来研讨会（患者/亲属、物理治疗师/脊椎按摩师和全科医生），每个研讨会都包含结构化批评、幻想和实施阶段。
- Abstract: Background: Shared decision-making (SDM) is a key component in patient-centered care for people consulting health care due to chronic musculoskeletal pain, including subacromial pain syndrome (SAPS). Limited research has explored how patients, relatives, and healthcare professionals perceive the content and delivery of SDM for managing SAPS in primary care. Thus, this study aims to explore stakeholder perspectives o...
- Summary (fallback): 机器翻译摘要显示：背景：共享决策 (SDM) 是以患者为中心的护理的关键组成部分，适用于因慢性肌肉骨骼疼痛（包括肩峰下疼痛综合征 (SAPS)）而咨询医疗保健的人。有限的研究探讨了患者、亲属和医疗保健专业人员如何看待 SDM 在初级保健中管理 SAPS 的内容和交付。因此，本研究旨在探讨利益相关者对 SAPS 特定情境 SDM 干预的内容、交付和情境要求的看法，并确定共同的挑战和共同开发想法，为干预措施的制定提供信息。方法：我们举办了三个独立的未来研讨会（患者/亲属、物理治疗师/脊椎按摩师和全科医生），每个研讨会都包含结构化批评、幻想和实施阶段。
- Keywords: care, stakeholder, saps, delivery, shared

### 17. [评估四个英国人群样本中神经精神疾病和大脑内表型的多基因指数的表现](https://www.medrxiv.org/content/10.64898/2026.07.07.26357467v1)
- Original title: Evaluating the performance of polygenic indices of neuropsychiatric conditions and brain endophenotypes in four UK population samples
- Authors: Dearman, A. R., Vrticka, P., Moore, J., Kumari, M., Schalkwyk, L.
- Meta: 2026-07-10 | genetic and genomic medicine | DOI: 10.64898/2026.07.07.26357467
- 中文摘要: 神经精神多基因指数（NPGI）被用作心理健康状况不佳的遗传预测因子。然而，NPGI 也与可能影响成年期心理健康的环境因素有关，包括抚养环境。因此，它们的“遗传”效应既是直接的，又是环境介导的。需要在没有环境信号的情况下识别替代遗传预测因子。针对大脑结构和功能进行训练的基于内表型的多基因指数 (EPGI) 是一种尚未得到充分研究的替代方案，由于它们在生物学上的相对接近性，可能会表现出与心理健康结果的关联，而这种关联比 NPGI 受环境影响较小。
- Abstract: Neuropsychiatric polygenic indices (NPGIs) are used as genetic predictors of poor mental health. However, NPGIs are also associated with environmental factors which could affect mental health in adulthood, including the rearing environment. Hence, their "genetic" effects are both direct and environmentally mediated. There is a need to identify alternative genetic predictors without environmental signal. Endophenotyp...
- Summary (fallback): 机器翻译摘要显示：神经精神多基因指数（NPGI）被用作心理健康状况不佳的遗传预测因子。然而，NPGI 也与可能影响成年期心理健康的环境因素有关，包括抚养环境。因此，它们的“遗传”效应既是直接的，又是环境介导的。需要在没有环境信号的情况下识别替代遗传预测因子。针对大脑结构和功能进行训练的基于内表型的多基因指数 (EPGI) 是一种尚未得到充分研究的替代方案，由于它们在生物学上的相对接近性，可能会表现出与心理健康结果的关联，而这种关联比 NPGI 受环境影响较小。
- Keywords: mental, health, npgis, genetic, associated

### 18. [OmicFormer：一种基于统计先验的转换器，用于对疾病和复杂性状进行准确且可概括的组学预测](https://www.medrxiv.org/content/10.64898/2026.07.06.26357359v1)
- Original title: OmicFormer: a statistical priors-informed transformer for accurate and generalizable omics prediction of diseases and complex traits
- Authors: Jiang, H., Yang, C., Qin, M., You, J., Feng, J. et al.
- Meta: 2026-07-10 | health informatics | DOI: 10.64898/2026.07.06.26357359
- 中文摘要: 精准医学面临着将高维组学数据转化为跨不同人群的可靠疾病预测的严峻挑战。当前的方法经常在分布变化的情况下失败，部分原因是它们无法编码复杂的生物特征依赖性。我们提出了 OmicFormer，一种基于 Transformer 的架构，它将两个互补的统计先验，即特征-标签关联和特征-特征依赖性，直接嵌入到其表示学习中。这种设计捕获了传统方法经常错过的局部和远程组学相互作用。
- Abstract: Precision medicine faces a critical challenge in translating high-dimensional omics data into robust disease predictions across diverse populations. Current approaches often fail under distribution shifts, partly due to their inability to encode complex biological feature dependencies. We present OmicFormer, a Transformer-based architecture that embeds two complementary statistical priors, i.e., feature-label associ...
- Summary (fallback): 机器翻译摘要显示：精准医学面临着将高维组学数据转化为跨不同人群的可靠疾病预测的严峻挑战。当前的方法经常在分布变化的情况下失败，部分原因是它们无法编码复杂的生物特征依赖性。我们提出了 OmicFormer，一种基于 Transformer 的架构，它将两个互补的统计先验，即特征-标签关联和特征-特征依赖性，直接嵌入到其表示学习中。这种设计捕获了传统方法经常错过的局部和远程组学相互作用。
- Keywords: omicformer, across, statistical, prediction, generalizable

### 19. [骨质疏松症预测的机器学习模型：系统回顾和荟萃分析](https://www.medrxiv.org/content/10.64898/2026.07.03.26357134v1)
- Original title: Machine Learning Models for Osteoporosis Prediction: A Systematic Review and Meta-Analysis
- Authors: de Carvalho, F. R., Gavaia, P. J.
- Meta: 2026-07-10 | health informatics | DOI: 10.64898/2026.07.03.26357134
- 中文摘要: 目的 机器学习 (ML) 在骨质疏松症预测中的应用已迅速扩展，但尚未有全面的荟萃分析综合这些模型在所有 ML 类别、数据类型和验证策略中的判别性能。这项系统综述和荟萃分析旨在评估机器学习和深度学习模型对成人骨质疏松症预测的诊断和预测准确性。方法 对 PubMed、Embase、Web of Science 和 IEEE Xplore 2020 年 1 月至 2026 年 2 月期间发表的研究进行系统检索。其中包括开发、验证或应用 ML 模型来预测成人骨质疏松症、低骨矿物质密度或骨质疏松性骨折的研究。使用预测模型偏倚风险评估工具 (PROBAST) 评估方法学质量。
- Abstract: Purpose The application of machine learning (ML) to osteoporosis prediction has expanded rapidly, yet no comprehensive meta-analysis has synthesized the discriminative performance of these models across all ML categories, data types, and validation strategies. This systematic review and meta-analysis aimed to evaluate the diagnostic and predictive accuracy of ML and deep learning models for osteoporosis prediction i...
- Summary (fallback): 机器翻译摘要显示：目的 机器学习 (ML) 在骨质疏松症预测中的应用已迅速扩展，但尚未有全面的荟萃分析综合这些模型在所有 ML 类别、数据类型和验证策略中的判别性能。这项系统综述和荟萃分析旨在评估机器学习和深度学习模型对成人骨质疏松症预测的诊断和预测准确性。方法 对 PubMed、Embase、Web of Science 和 IEEE Xplore 2020 年 1 月至 2026 年 2 月期间发表的研究进行系统检索。其中包括开发、验证或应用 ML 模型来预测成人骨质疏松症、低骨矿物质密度或骨质疏松性骨折的研究。使用预测模型偏倚风险评估工具 (PROBAST) 评估方法学质量。
- Keywords: models, learning, prediction, studies, osteoporosis

### 20. [如何最好地向临床医生解释机器学习模型：解释类型的用户研究](https://www.medrxiv.org/content/10.64898/2026.06.30.26356761v1)
- Original title: How Best to Explain Machine Learning Models to Clinicians: A User Study of Explanation Types
- Authors: Brown, B., Oguss, M., Carey, K. A., Martin, J., Kotula, C. A. et al.
- Meta: 2026-07-10 | health informatics | DOI: 10.64898/2026.06.30.26356761
- 中文摘要: 背景：解释在帮助临床医生理解黑盒机器学习模型如何在临床环境中进行预测方面发挥着至关重要的作用。已经开发了几种不同类型的解释，每种解释都对应于表征模型输入和预测之间关系的独特方法。然而，目前尚不清楚临床医生最看重哪种类型的解释。目的：为了提高机器学习在临床环境中的实用性，我们的目的是评估临床医生如何在临床重要指标上评价不同的解释方法，例如重要性、信任、理解，以及解释如何影响临床医生对患者的看法。方法：我们对 39 名重症监护和医院医学护士和医生进行了一项用户研究，以比较归因、反事实和基于规则的解释。
- Abstract: Background: Explanations play a crucial role in helping clinicians understand how black-box machine learning models make predictions in clinical settings. Several different types of explanations have been developed, each corresponding to a unique approach for characterizing the relationships between model inputs and predictions. However, it remains unclear what types of explanations are the most valued by clinicians...
- Summary (fallback): 机器翻译摘要显示：背景：解释在帮助临床医生理解黑盒机器学习模型如何在临床环境中进行预测方面发挥着至关重要的作用。已经开发了几种不同类型的解释，每种解释都对应于表征模型输入和预测之间关系的独特方法。然而，目前尚不清楚临床医生最看重哪种类型的解释。目的：为了提高机器学习在临床环境中的实用性，我们的目的是评估临床医生如何在临床重要指标上评价不同的解释方法，例如重要性、信任、理解，以及解释如何影响临床医生对患者的看法。方法：我们对 39 名重症监护和医院医学护士和医生进行了一项用户研究，以比较归因、反事实和基于规则的解释。
- Keywords: explanations, clinicians, explanation, types, machine

### 21. [评估初级保健远程医疗准备情况的设施级工具的适应性和心理测量验证](https://www.medrxiv.org/content/10.64898/2026.07.01.26356790v1)
- Original title: Adaptation and Psychometric Validation of a Facility-Level Tool to Assess Telemedicine Readiness in Primary Care
- Authors: Escobar-Agreda, S., Villarreal-Zegarra, D., Reategui-Rivera, C. M., Paredes-Gonzales, Y., Rojas-Mezarina, L.
- Meta: 2026-07-10 | health informatics | DOI: 10.64898/2026.07.01.26356790
- 中文摘要: 背景：远程医疗迅速扩展，但其在应急响应之外的持续使用仍然不平衡。设施和组织条件是医疗保健干预实施的可修改决定因素，准备情况评估是早期采用和进一步采用过程中的关键步骤。然而，许多远程医疗准备评估工具缺乏心理测量证据，限制了它们在基准测试、优先投资和大规模监测进展方面的价值。目标：调整并在心理测量上验证设施级别的远程医疗准备清单 (TRI-F)。方法：我们使用 2023 年 12 月至 2024 年 3 月期间对秘鲁初级保健机构 (PCF) 大样本在线评估的数据进行了横断面分析。
- Abstract: Background: Telehealth has expanded rapidly, yet its sustained use beyond emergency responses remains uneven. Facility and organizational conditions are modifiable determinants of healthcare intervention implementation, and readiness assessments are key steps in the early adoption and further uptake process. However, many telemedicine readiness assessment instruments lack psychometric evidence, limiting their value...
- Summary (fallback): 机器翻译摘要显示：背景：远程医疗迅速扩展，但其在应急响应之外的持续使用仍然不平衡。设施和组织条件是医疗保健干预实施的可修改决定因素，准备情况评估是早期采用和进一步采用过程中的关键步骤。然而，许多远程医疗准备评估工具缺乏心理测量证据，限制了它们在基准测试、优先投资和大规模监测进展方面的价值。目标：调整并在心理测量上验证设施级别的远程医疗准备清单 (TRI-F)。方法：我们使用 2023 年 12 月至 2024 年 3 月期间对秘鲁初级保健机构 (PCF) 大样本在线评估的数据进行了横断面分析。
- Keywords: telemedicine, readiness, facility, internal, across

### 22. [使用连续时间隐马尔可夫模型模拟抗生素治疗对脓毒症的有效性](https://www.medrxiv.org/content/10.64898/2026.07.03.26357092v1)
- Original title: Modeling the Effectiveness of Antibiotic Therapies Against Sepsis Using Continuous-time Hidden Markov Models
- Authors: Schmiegel, S., Marchi, H., Borgstedt, R., Rehberg, S., Fuchs, C. et al.
- Meta: 2026-07-10 | health informatics | DOI: 10.64898/2026.07.03.26357092
- 中文摘要: 脓毒症患者需要在脓毒症发病后的第一小时内接受有效的抗生素治疗，以降低死亡风险。然而，提供抗生素治疗适宜性信息的微生物数据通常只能在 72 小时后才能获得。因此，治疗医生需要根据患者的健康记录和一般健康状况来判断治疗的有效性。这种医疗评估很复杂，需要多年的经验。在我们的研究中，我们研究了统计模型如何有助于评估抗生素疗法的有效性。为此，我们通过使用三态连续时间隐马尔可夫模型（ctHMM）对脓毒症患者的健康状况进行建模来描述抗生素治疗的有效性。
- Abstract: Patients suffering from sepsis need to be treated with an effective antibiotic therapy within the first hour after sepsis onset to decrease their risk of death. Microbiological data that provide information about the suitability of antibiotic therapies, however, is usually available only after 72 hours. Consequently, the treating physicians need to judge a therapy's effectiveness based on the patients' measured heal...
- Summary (fallback): 机器翻译摘要显示：脓毒症患者需要在脓毒症发病后的第一小时内接受有效的抗生素治疗，以降低死亡风险。然而，提供抗生素治疗适宜性信息的微生物数据通常只能在 72 小时后才能获得。因此，治疗医生需要根据患者的健康记录和一般健康状况来判断治疗的有效性。这种医疗评估很复杂，需要多年的经验。在我们的研究中，我们研究了统计模型如何有助于评估抗生素疗法的有效性。为此，我们通过使用三态连续时间隐马尔可夫模型（ctHMM）对脓毒症患者的健康状况进行建模来描述抗生素治疗的有效性。
- Keywords: antibiotic, effectiveness, therapies, sepsis, patients

### 23. [使用链接电子病历设计和实施母婴临床试验招募警报，并评估研究人员感知的警报可用性](https://www.medrxiv.org/content/10.64898/2026.06.30.26356791v1)
- Original title: Design and implementation of maternal-infant clinical trial recruitment alert using linked electronic medical records, and evaluation of researcher-perceived alert usability
- Authors: Panganiban, H. P., Segal, A., Kuschel, C.
- Meta: 2026-07-10 | health informatics | DOI: 10.64898/2026.06.30.26356791
- 中文摘要: 背景 配置为电子病历警报的临床决策支持系统可以通过识别合格的参与者来支持临床试验招募。虽然它们通常用于评估单个患者记录，但它们在链接母婴图表中的应用尚未得到广泛探索。目标 该项目旨在使用链接的母婴记录设计和实施临床试验警报，并评估研究人员感知的可用性。材料和方法我们进行了一个两阶段的质量保证项目：（1）设计和实施与预期招聘工作流程一致的警报，以及（2）使用系统可用性量表评估可用性。基本内容分析描述了警报设计和实施过程，而定量评分则评估了感知的可用性。
- Abstract: Background Clinical decision support systems configured as electronic medical records alerts can support clinical trial recruitment by identifying eligible participants. While they are typically used to evaluate a single patient record, their application for a linked maternal infant chart has not been extensively explored. Objective This project aimed to design and implement a clinical trial alert using linked mater...
- Summary (fallback): 机器翻译摘要显示：背景 配置为电子病历警报的临床决策支持系统可以通过识别合格的参与者来支持临床试验招募。虽然它们通常用于评估单个患者记录，但它们在链接母婴图表中的应用尚未得到广泛探索。目标 该项目旨在使用链接的母婴记录设计和实施临床试验警报，并评估研究人员感知的可用性。材料和方法我们进行了一个两阶段的质量保证项目：（1）设计和实施与预期招聘工作流程一致的警报，以及（2）使用系统可用性量表评估可用性。基本内容分析描述了警报设计和实施过程，而定量评分则评估了感知的可用性。
- Keywords: alert, usability, recruitment, clinical, workflow

### 24. [NigBench：尼日利亚大语言模型的多语言床旁医疗查询基准研究](https://www.medrxiv.org/content/10.64898/2026.07.05.26356776v1)
- Original title: NigBench: A multilingual point-of-care medical query benchmarking study of large language models in Nigeria
- Authors: Olatunji, T., Aka, C., Okocha, C., Ayodele, E., Orisakwe, J. et al.
- Meta: 2026-07-10 | health informatics | DOI: 10.64898/2026.07.05.26356776
- 中文摘要: 在这项研究中，我们引入了一个新颖的基准，其中包含来自尼日利亚一线卫生工作者的 9,000 多个现实世界、现场护理、多语言和多模式临床问答对。使用该数据集，我们将当地的全科医生与多个领先的开放式和封闭式法学硕士进行比较。我们的结果揭示了关于法学硕士作为资源匮乏环境中的临床决策支持系统的适用性的几个重要见解。结果证实，性能因语言和输入方式（例如文本与语音）而异：虽然模型在英语文本输入上表现最佳，但对于本地语言语音，其准确性显着下降。至关重要的是，在获得法学硕士学位之前，通过将其他语言转录和翻译成英语，可以实现显着的性能提升——这对于非英语产品开发人员来说是一个重要的见解。
- Abstract: In this study, we introduce a novel benchmark comprising over 9,000 real-world, point-of-care, multilingual, and multimodal clinical question-answer pairs sourced from frontline health workers in Nigeria. Using the dataset, we compare local general practitioners to multiple leading open and closed LLMs. Our results reveal several critical insights into the suitability of LLMs as clinical decision support systems in...
- Summary (fallback): 机器翻译摘要显示：在这项研究中，我们引入了一个新颖的基准，其中包含来自尼日利亚一线卫生工作者的 9,000 多个现实世界、现场护理、多语言和多模式临床问答对。使用该数据集，我们将当地的全科医生与多个领先的开放式和封闭式法学硕士进行比较。我们的结果揭示了关于法学硕士作为资源匮乏环境中的临床决策支持系统的适用性的几个重要见解。结果证实，性能因语言和输入方式（例如文本与语音）而异：虽然模型在英语文本输入上表现最佳，但对于本地语言语音，其准确性显着下降。至关重要的是，在获得法学硕士学位之前，通过将其他语言转录和翻译成英语，可以实现显着的性能提升——这对于非英语产品开发人员来说是一个重要的见解。
- Keywords: multilingual, point-of-care, language, models, nigeria

### 25. [没有必要在便盆周围殴打：来自院内主要产生 NDM 的大肠杆菌携带爆发的教训：一项混合方法研究。](https://www.medrxiv.org/content/10.64898/2026.07.06.26354129v1)
- Original title: No Point Beating Around the Bedpan: Lessons from a Major Intra-Hospital NDM-Producing Escherichia coli Carriage Outbreak : a Mixed-Methods Study.
- Authors: Le Hir, A., Vincent, P., Sardi, F. S., Giglione, C., Bouton, N. et al.
- Meta: 2026-07-10 | infectious diseases | DOI: 10.64898/2026.07.06.26354129
- 中文摘要: 抗生素耐药性对全球公共卫生构成重大威胁。在新兴的广泛耐药细菌 (eXDR) 中，产生碳青霉烯酶的肠杆菌科细菌 (CPE) 使医院因快速传播而面临疫情爆发的风险，并面临治疗限制。通过流行病学-定性混合方法研究，我们报告了法国迄今为止最广泛的 CPE 携带疫情，该疫情发生在 2025 年 1 月至 6 月期间在马赛欧洲医院 (HEM)。到 2024 年 11 月底，一名从塞内加尔返回的指示患者入院，该患者携带产生 NDM 的大肠杆菌，导致了广泛的传播，尽管遵守了国家筛查和隔离指南。超过 7,500 次直肠筛查测试证实了 481 例 CPE 携带者（包括 343 例 NDM、129 例 OXA-48 样和 9 例其他 CPE）和 14 例耐万古霉素屎肠球菌携带者。
- Abstract: Antimicrobial resistance constitutes a major threat to global public health. Among emerging extensively drug-resistant bacteria (eXDR), carbapenemase-producing Enterobacteriaceae (CPE) expose hospitals to outbreaks through rapid dissemination, and to therapeutic limitations. Through a mixed epidemiological-qualitative methods study, we report the most extensive CPE carriage outbreak known to date in France, which oc...
- Summary (fallback): 机器翻译摘要显示：抗生素耐药性对全球公共卫生构成重大威胁。在新兴的广泛耐药细菌 (eXDR) 中，产生碳青霉烯酶的肠杆菌科细菌 (CPE) 使医院因快速传播而面临疫情爆发的风险，并面临治疗限制。通过流行病学-定性混合方法研究，我们报告了法国迄今为止最广泛的 CPE 携带疫情，该疫情发生在 2025 年 1 月至 6 月期间在马赛欧洲医院 (HEM)。到 2024 年 11 月底，一名从塞内加尔返回的指示患者入院，该患者携带产生 NDM 的大肠杆菌，导致了广泛的传播，尽管遵守了国家筛查和隔离指南。超过 7,500 次直肠筛查测试证实了 481 例 CPE 携带者（包括 343 例 NDM、129 例 OXA-48 样和 9 例其他 CPE）和 14 例耐万古霉素屎肠球菌携带者。
- Keywords: outbreak, major, lessons, ndm-producing, escherichia

### 26. [中心静脉血氧饱和度、二氧化碳静脉动脉梯度和乳酸水平作为心脏手术后组织灌注标志物的比较评估：一项前瞻性探索性观察研究](https://www.medrxiv.org/content/10.64898/2026.07.04.26357161v1)
- Original title: Comparative Evaluation of Central Venous Oxygen Saturation, Carbon Dioxide Venous Arterial Gradient, and Lactate Levels as Markers of Tissue Perfusion After Cardiac Surgery: A Prospective Exploratory Observational Study
- Authors: Neves, J. K., Venturini, V., Zeferino, S., Galas, F. R. B. G., Auler Junior, J.
- Meta: 2026-07-10 | intensive care and critical care medicine | DOI: 10.64898/2026.07.04.26357161
- 中文摘要: 目的：本研究旨在确定哪些组织灌注不足的标志物，特别是乳酸水平、中心静脉氧饱和度 (ScvO2) 和静脉动脉二氧化碳梯度 (CO2 梯度)，在预测心脏手术患者术后 48 小时内从 ICU 出院时具有最高的敏感性和特异性。这是一项探索性的、假设生成的调查。方法：前瞻性观察研究，涉及 InCor-HCFMUSP 外科 ICU 中 100 名接受体外循环心脏手术的患者。在 ICU 入院时和入院后 24 小时评估灌注标志物。结果：24 小时 ScvO2 是唯一与 ICU 出院显着相关的标志物（OR=1.096；95% CI=1.020-1.180；p=0.012）。
- Abstract: Objective: This study aims to identify which markers of tissue hypoperfusion - specifically lactate levels, central venous oxygen saturation (ScvO2), and venous arterial carbon dioxide gradient (CO2 gradient) - have the highest sensitivity and specificity in predicting the discharge of postoperative cardiac surgical patients from the ICU within 48 hours. This is an exploratory, hypothesis-generating investigation. M...
- Summary (fallback): 机器翻译摘要显示：目的：本研究旨在确定哪些组织灌注不足的标志物，特别是乳酸水平、中心静脉氧饱和度 (ScvO2) 和静脉动脉二氧化碳梯度 (CO2 梯度)，在预测心脏手术患者术后 48 小时内从 ICU 出院时具有最高的敏感性和特异性。这是一项探索性的、假设生成的调查。方法：前瞻性观察研究，涉及 InCor-HCFMUSP 外科 ICU 中 100 名接受体外循环心脏手术的患者。在 ICU 入院时和入院后 24 小时评估灌注标志物。结果：24 小时 ScvO2 是唯一与 ICU 出院显着相关的标志物（OR=1.096；95% CI=1.020-1.180；p=0.012）。
- Keywords: venous, lactate, scvo2, hours, gradient

### 27. [系统综述，批判性评价超加工食品、心血管疾病和高血压研究方法的严谨性](https://www.medrxiv.org/content/10.64898/2026.07.09.26357611v1)
- Original title: A systematic review to critically appraise methodological rigour in research on ultra-processed food and cardiovascular disease and hypertension
- Authors: Mekonnen, T. C., Bitew, Z. A., Dessie, A. M., Tegegne, T., Ushula, T. et al.
- Meta: 2026-07-10 | cardiovascular medicine | DOI: 10.64898/2026.07.09.26357611
- 中文摘要: 尽管越来越多的研究将超加工食品（UPF）的消费与心血管疾病（CVD）和高血压的风险联系起来，但还没有研究系统地评估这些关联背后的方法学严谨性。我们系统地检索了主要数据库以识别符合条件的研究。提取数据用于饮食评估方法、UPF 分类、协变量选择、混杂控制、统计模型和效果估计。进行随机效应荟萃分析以汇总效应估计。进行荟萃回归和敏感性分析来探索异质性的来源。在 46 项符合条件的研究中应用 NOVA 分类对 UPF 进行分类时观察到了显着的异质性。
- Abstract: Despite growing research linking ultra-processed food (UPF) consumption to risk of cardiovascular disease (CVD) and hypertension, no study has systematically evaluated the methodological rigor underlying these associations. We systematically searched major databases to identify eligible studies. Data were extracted for dietary assessment methods, UPF classification, covariate selection, confounding control, statisti...
- Summary (fallback): 机器翻译摘要显示：尽管越来越多的研究将超加工食品（UPF）的消费与心血管疾病（CVD）和高血压的风险联系起来，但还没有研究系统地评估这些关联背后的方法学严谨性。我们系统地检索了主要数据库以识别符合条件的研究。提取数据用于饮食评估方法、UPF 分类、协变量选择、混杂控制、统计模型和效果估计。进行随机效应荟萃分析以汇总效应估计。进行荟萃回归和敏感性分析来探索异质性的来源。在 46 项符合条件的研究中应用 NOVA 分类对 UPF 进行分类时观察到了显着的异质性。
- Keywords: methodological, hypertension, higher, consumption, risk

### 28. [MRI 衍生的脂肪库和心力衰竭风险背后的心脏代谢途径：孟德尔随机研究](https://www.medrxiv.org/content/10.64898/2026.07.06.26357230v1)
- Original title: MRI-Derived Fat Depots and Cardiometabolic Pathways Underlying Heart Failure Risk: A Mendelian Randomization Study
- Authors: Sharma, P., Levin, M.
- Meta: 2026-07-10 | cardiovascular medicine | DOI: 10.64898/2026.07.06.26357230
- 中文摘要: 背景：肥胖是心力衰竭（HF）的一个主要可改变危险因素，但体重指数（BMI）并不能区分生物学上不同的脂肪库。成像来源的脂肪组织库是否能够超越传统的人体测量方法来捕获心力衰竭风险的特定心脏代谢途径仍不确定。方法：我们使用已发表的全基因组关联研究摘要统计数据进行了两个样本孟德尔随机化 (MR) 和多变量 MR 中介分析。一般肥胖特征包括 BMI、腰臀比 (WHR) 以及根据 GIANT 和英国生物银行对多达 694,649 人的荟萃分析根据 BMI 调整的 WHR。 MRI 衍生的内脏脂肪组织 (VAT)、腹部皮下脂肪组织 (ASAT) 和臀股脂肪组织 (GFAT) 来自 38,965 名英国生物银行参与者。
- Abstract: Background: Obesity is a major modifiable risk factor for heart failure (HF), but body mass index (BMI) does not distinguish biologically distinct fat depots. Whether imaging-derived adipose tissue depots capture specific cardiometabolic pathways underlying HF risk beyond conventional anthropometric measures remains uncertain. Methods: We performed two-sample Mendelian randomization (MR) and multivariable MR mediati...
- Summary (fallback): 机器翻译摘要显示：背景：肥胖是心力衰竭（HF）的一个主要可改变危险因素，但体重指数（BMI）并不能区分生物学上不同的脂肪库。成像来源的脂肪组织库是否能够超越传统的人体测量方法来捕获心力衰竭风险的特定心脏代谢途径仍不确定。方法：我们使用已发表的全基因组关联研究摘要统计数据进行了两个样本孟德尔随机化 (MR) 和多变量 MR 中介分析。一般肥胖特征包括 BMI、腰臀比 (WHR) 以及根据 GIANT 和英国生物银行对多达 694,649 人的荟萃分析根据 BMI 调整的 WHR。 MRI 衍生的内脏脂肪组织 (VAT)、腹部皮下脂肪组织 (ASAT) 和臀股脂肪组织 (GFAT) 来自 38,965 名英国生物银行参与者。
- Keywords: risk, adipose, cardiometabolic, tissue, asat

### 29. [荷兰意外怀孕后的支持经历](https://www.medrxiv.org/content/10.64898/2026.07.03.26356675v1)
- Original title: Support Experiences Following Unintended Pregnancy in the Netherlands
- Authors: Inan, Z., Sprenger, M., Slagboom, N. M., Molenaar, J. M.
- Meta: 2026-07-10 | sexual and reproductive health | DOI: 10.64898/2026.07.03.26356675
- 中文摘要: 背景：意外怀孕会带来压力并改变生活轨迹。社会支持可能会缓冲这些影响，但其在意外怀孕和育儿早期的影响尚不清楚。本研究旨在了解这一时期所经历的社会支持的类型和差距。方法：本研究利用荷兰海牙 RISE UP 研究的访谈数据。 2024 年至 2025 年间，13 名经历过意外怀孕的母亲和 8 名伴侣参加了半结构化访谈。使用 House 的社会支持框架对访谈进行了主题分析。结果：从怀孕到早期为人父母的整个时间轴上强调了不同类型的支持，强调了其动态性质。情感和工具支持在整个过程中最为突出。
- Abstract: Background: Unintended pregnancies can introduce stress and shift life trajectories. Social support may buffer these effects, yet its influence during an unintended pregnancy and into the early parenthood period is not clear. This study aimed to understand the types and gaps of social support experienced throughout this period. Methods: This study utilized interview data under the RISE UP study in The Hague, the Net...
- Summary (fallback): 机器翻译摘要显示：背景：意外怀孕会带来压力并改变生活轨迹。社会支持可能会缓冲这些影响，但其在意外怀孕和育儿早期的影响尚不清楚。本研究旨在了解这一时期所经历的社会支持的类型和差距。方法：本研究利用荷兰海牙 RISE UP 研究的访谈数据。 2024 年至 2025 年间，13 名经历过意外怀孕的母亲和 8 名伴侣参加了半结构化访谈。使用 House 的社会支持框架对访谈进行了主题分析。结果：从怀孕到早期为人父母的整个时间轴上强调了不同类型的支持，强调了其动态性质。情感和工具支持在整个过程中最为突出。
- Keywords: support, pregnancy, unintended, social, throughout

### 30. [拉丁美洲人乳头瘤病毒筛查试验呈阳性、宫颈肿瘤或宫颈癌女性的生活质量](https://www.medrxiv.org/content/10.64898/2026.07.06.26357411v1)
- Original title: Quality of life in women with a human papillomavirus-positive screening test, cervical neoplasia, or cervical cancer in Latin America
- Authors: Tejada, R. A., Ramirez, A. T., Ferrera, A., Cabrera, Y., Teran, C. A. et al.
- Meta: 2026-07-10 | sexual and reproductive health | DOI: 10.64898/2026.07.06.26357411
- 中文摘要: 目的：人乳头瘤病毒 (HPV) 感染和 HPV 相关疾病影响健康相关的生活质量 (HRQOL)。我们的目的是测量拉丁美洲 HPV 检测结果呈阳性、患有宫颈上皮内瘤变 (CIN) 或宫颈癌的女性的 HRQOL。方法：我们招募了来自玻利维亚、哥伦比亚、洪都拉斯、秘鲁和乌拉圭的 18 至 75 岁女性。我们使用 EQ-5D-5L 工具根据特定国家/地区的健康偏好集（如果有）计算 EQ-5D 指数得分。我们计算了 EQ-5D 指数的中位数和四分位距 (IQR)，并进行了探索性分析，通过伽马回归比较了按诊断和国家划分的 HRQOL 损失。结果：我们展示了 1,073 名参与者的结果。中位年龄为 43 岁（IQR：34-52）。
- Abstract: Purpose: Human papillomavirus (HPV) infection and HPV-associated diseases impact health-related quality of life (HRQOL). We aimed to measure HRQOL in women with HPV-positive test results, cervical intraepithelial neoplasia (CIN), or cervical cancer in Latin America. Methods: We enrolled women aged 18 to 75 years from Bolivia, Colombia, Honduras, Peru, and Uruguay. We used the EQ-5D-5L instrument to calculate EQ-5D i...
- Summary (fallback): 机器翻译摘要显示：目的：人乳头瘤病毒 (HPV) 感染和 HPV 相关疾病影响健康相关的生活质量 (HRQOL)。我们的目的是测量拉丁美洲 HPV 检测结果呈阳性、患有宫颈上皮内瘤变 (CIN) 或宫颈癌的女性的 HRQOL。方法：我们招募了来自玻利维亚、哥伦比亚、洪都拉斯、秘鲁和乌拉圭的 18 至 75 岁女性。我们使用 EQ-5D-5L 工具根据特定国家/地区的健康偏好集（如果有）计算 EQ-5D 指数得分。我们计算了 EQ-5D 指数的中位数和四分位距 (IQR)，并进行了探索性分析，通过伽马回归比较了按诊断和国家划分的 HRQOL 损失。结果：我们展示了 1,073 名参与者的结果。中位年龄为 43 岁（IQR：34-52）。
- Keywords: hrqol, cervical, women, diagnosis, test
