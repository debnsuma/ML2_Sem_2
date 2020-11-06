# **Sem2-ML2-Assignment-1**


### Task 1 (Base Code)
-------------------------

**Target** 

Implement the designed CNN architecture for CIFAR-10 dataset

**Results** 

- No. of Parameters     : 157,370
- Best Train Accuracy   : 88%
- Best Test Accuracy    : 70%

**Analysis** 

- The model was not able to generalize well (atthough it was not all that bad)
- The test accuracy was not changing much

[Task 1 - Code](https://github.com/debnsuma/ML2_Sem_2/blob/master/ML/A1/ML-Assignment-1-Task1.ipynb)

### Task 2 (With Regularization)
-------------------------------

**Target** 

Add two regularization techniques and try to to improve the generalization of the model.

I also tried to make use of less parameters within less EPOCH(15)

**Results** 

- No. of Parameters     : 157,594
- Best Train Accuracy   : 85%
- Best Test Accuracy    : 77%

**Analysis** 

- As expected with regularization(dropout and BN) training error increated slightly whereas test error decreased
- The model was able to generalize little better 
- BN added some more no. of parameters 
- The test accuracy was not changing much

[Task 2 - Code](https://github.com/debnsuma/ML2_Sem_2/blob/master/ML/A1/ML-Assignment-1-Task2.ipynb)
