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

- **Deep Crossing** - Embedding layer + multiple hidden layers for automatic feature crossing.  

- **NeuralCF** - Replaces traditional matrix factorization with neural networks.  

- **PNN (Product-based Neural Networks)** - Uses inner/outer product operations for feature interactions.  
- **Wide & Deep** - Combines a wide component for memorization and a deep component for generalization.  
- **Deep & Cross** - Strengthens the wide part of Wide & Deep using a cross network.  
- **FNN (Factorization-Machine Supported Neural Networks)** - Uses FM to initialize the embedding layer.  
- **DeepFM** - Replaces the linear wide part of Wide & Deep with FM.  

- **NFM (Neural Factorization Machine)** - Uses neural networks for second-order feature interactions.  

- **AFM (Attentional Factorization Machine)** - Adds attention to second-order interactions.  

- **DIN (Deep Interest Network)** - Uses attention mechanisms for user history and target ad interactions.  

- **DIEN (Deep Interest Evolution Network)** - Models the evolution of user interest using sequential deep learning.  
- **DRN (Deep Residual Network for Recommendation)** 

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

- **Deep Crossing** - 通过嵌入层 + 多层隐藏层实现自动特征交叉。  

- **NeuralCF** - 用神经网络替代传统矩阵分解。  

- **PNN（基于乘积的神经网络）** - 采用内积/外积操作实现特征交互。  

- **Wide & Deep** - 结合 Wide 记忆部分和 Deep 泛化部分。  

- **Deep & Cross** - 在 Wide & Deep 的 Wide 部分加入 Cross Network 强化交叉。  
- **FNN（因子分解机支持的神经网络）** - 使用 FM 初始化嵌入层。  
- **DeepFM** - 用 FM 替代 Wide & Deep 结构中的线性 Wide 部分。  

- **NFM（神经因子分解机）** - 使用神经网络进行二阶特征交互。  

- **AFM（注意力因子分解机）** - 在二阶交互中引入注意力机制。  

- **DIN（深度兴趣网络）** - 通过注意力机制建模用户历史行为与目标广告的交互。  

- **DIEN（深度兴趣演化网络）** - 使用序列深度学习模型用户兴趣随时间的演变。  

- **DRN（深度残差网络推荐）** -

### 文件结构
- **深度学习模型** 存储于 `Deep Learning Models` 文件夹中。
- **传统机器学习模型** 存储于 `Machine Learning Models` 文件夹中。
