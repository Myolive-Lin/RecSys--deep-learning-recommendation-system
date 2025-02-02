## RecSys

### Project Description
This project is based on *Deep Learning Recommendation Systems* by Wang Zhe. It focuses on implementing and experimenting with various recommendation models, including:

### Machine Learning Models
- **Collaborative Filtering**
- **Matrix Factorization**
- **Logistic Regression**
- **Factorization Machines (FM)**
- **GBDT + LR**
- **LS-PLM**

### Deep Learning Models
- **AutoRec** - Uses autoencoders for user/item encoding.  
  *Pros:* Simple structure, fast training and deployment.  
  *Cons:* Limited expressive power.

- **Deep Crossing** - Embedding layer + multiple hidden layers for automatic feature crossing.  
  *Pros:* Classic deep learning framework.  
  *Cons:* Lacks specificity in feature interactions.

- **NeuralCF** - Replaces traditional matrix factorization with neural networks.  
  *Pros:* Higher expressive power.  
  *Cons:* Uses only user and item IDs, ignoring additional features.

- **PNN (Product-based Neural Networks)** - Uses inner/outer product operations for feature interactions.  
  *Pros:* Improves feature crossing capabilities.  
  *Cons:* Approximation in outer product pooling may affect expressiveness.

- **Wide & Deep** - Combines a wide component for memorization and a deep component for generalization.  
  *Pros:* Pioneered hybrid model structures, influencing later models.  
  *Cons:* Wide part requires manual feature engineering.

- **Deep & Cross** - Strengthens the wide part of Wide & Deep using a cross network.  
  *Pros:* Automates feature combination.  
  *Cons:* High cross-network complexity.

- **FNN (Factorization-Machine Supported Neural Networks)** - Uses FM to initialize the embedding layer.  
  *Pros:* Faster convergence.  
  *Cons:* Lacks dedicated feature crossing layers.

- **DeepFM** - Replaces the linear wide part of Wide & Deep with FM.  
  *Pros:* Enhances feature interactions.  
  *Cons:* Structure is similar to Wide & Deep.

- **NFM (Neural Factorization Machine)** - Uses neural networks for second-order feature interactions.  
  *Pros:* More powerful than FM.  
  *Cons:* Similar to PNN.

- **AFM (Attentional Factorization Machine)** - Adds attention to second-order interactions.  
  *Pros:* Learns feature importance.  
  *Cons:* Complex training.

- **DIN (Deep Interest Network)** - Uses attention mechanisms for user history and target ad interactions.  
  *Pros:* More personalized recommendations.  
  *Cons:* Does not fully utilize all available features.

- **DIEN (Deep Interest Evolution Network)** - Models the evolution of user interest using sequential deep learning.  
  *Pros:* Captures time-dependent user behavior.  
  *Cons:* Complex training, high serving latency.

- **DRN (Deep Residual Network for Recommendation)** - *(Description to be added.)*

### Folder Structure
- **Deep learning models** are stored in the `Deep Learning Models` folder.
- **Traditional machine learning models** are stored in the `Machine Learning Models` folder.


## RecSys

### 项目描述
本项目基于王喆的 *《深度学习推荐系统》*，重点实现和实验各种推荐模型，包括：

### 机器学习模型
- **协同过滤**
- **矩阵分解**
- **逻辑回归**
- **因子分解机（FM）**
- **GBDT + LR**
- **LS-PLM**

### 深度学习模型
- **AutoRec** - 使用自编码器进行用户/物品编码。  
  *优点：* 结构简单，训练和部署速度快。  
  *缺点：* 表达能力有限。

- **Deep Crossing** - 通过嵌入层 + 多层隐藏层实现自动特征交叉。  
  *优点：* 经典深度学习框架。  
  *缺点：* 缺乏特定的特征交互。

- **NeuralCF** - 用神经网络替代传统矩阵分解。  
  *优点：* 表达能力更强。  
  *缺点：* 仅使用用户和物品 ID，未利用额外特征。

- **PNN（基于乘积的神经网络）** - 采用内积/外积操作实现特征交互。  
  *优点：* 增强特征交叉能力。  
  *缺点：* 外积池化近似可能影响表达能力。

- **Wide & Deep** - 结合 Wide 记忆部分和 Deep 泛化部分。  
  *优点：* 开创性地结合两种模型，影响后续模型。  
  *缺点：* Wide 部分需要手工特征工程。

- **Deep & Cross** - 在 Wide & Deep 的 Wide 部分加入 Cross Network 强化交叉。  
  *优点：* 自动化特征组合。  
  *缺点：* 交叉网络复杂度较高。

- **FNN（因子分解机支持的神经网络）** - 使用 FM 初始化嵌入层。  
  *优点：* 收敛速度更快。  
  *缺点：* 缺少专门的特征交叉层。

- **DeepFM** - 用 FM 替代 Wide & Deep 结构中的线性 Wide 部分。  
  *优点：* 增强特征交互能力。  
  *缺点：* 结构与 Wide & Deep 相似。

- **NFM（神经因子分解机）** - 使用神经网络进行二阶特征交互。  
  *优点：* 比 FM 更强大。  
  *缺点：* 结构类似 PNN。

- **AFM（注意力因子分解机）** - 在二阶交互中引入注意力机制。  
  *优点：* 能学习特征重要性。  
  *缺点：* 训练复杂。

- **DIN（深度兴趣网络）** - 通过注意力机制建模用户历史行为与目标广告的交互。  
  *优点：* 个性化推荐效果更好。  
  *缺点：* 没有充分利用所有特征。

- **DIEN（深度兴趣演化网络）** - 使用序列深度学习模型用户兴趣随时间的演变。  
  *优点：* 捕捉用户行为的时间依赖性。  
  *缺点：* 训练复杂，推理延迟较高。

- **DRN（深度残差网络推荐）** - *（描述待补充）*

### 文件结构
- **深度学习模型** 存储于 `Deep Learning Models` 文件夹中。
- **传统机器学习模型** 存储于 `Machine Learning Models` 文件夹中。
