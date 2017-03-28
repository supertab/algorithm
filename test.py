# 目标是找到合适的theta是J(theta)最小
import numpy as np
import pickle, time
import matplotlib.pyplot as plt

# normal equation: theta = (X^T*X)^(-1)*X^T*y
# 矩阵相乘使用np.dot 求逆: np.linalg.inv
def normal_equ(X, y):
    return np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T),y)

# gradiant descent: 梯度下降公式
def gra_descent( theta, X, y, rate=0.1, iter_n=0):
    '''
    theta: 初始参数
    X: 输入量，y: 输出量
    rate: 学习速率
    iter_n: 迭代次数，当使用迭代次数作为收敛条件时设置
    '''
    while iter_n<20:
        iter_n+=1
        print('iter:',iter_n, theta)
        m = len(X) # 样本的个数
        x_n = len(X[0]) # 样本的特征的个数
        err = np.dot(X,theta)-y # 估值与真实值之间的偏差
        # 计算J的值
        J = 1/(2*m) * (err**2).sum()
        print('J=',J)
        tmp = np.dot(err, X)
        remain = rate*tmp/m
        if abs( remain.sum()) > 1e-6:
            theta = theta - remain
        else:
            break
    return theta

def norm_A(A, addcol = True):
    A_mean = A.mean(axis=0)
    A_std = np.std(A, axis=0)
    A_scal = A.max(axis=0) - A.min(axis=0)
    A = (A-A_mean)/ A_std
    if addcol:
        # add first col
        lenA = len(A[:,0])
        first = np.ones(lenA).reshape((lenA, 1))
        A = np.c_[first, A]
    return A, A_mean, A_std


def hypothesis(x, theta, x_mean, x_std, y_mean, y_std):
    x = np.array([x, x**0.5])
    x = (x-x_mean)/ x_std
    x = np.append(np.ones(1), x)
    y = np.dot(theta.T, x)
    return y*y_std+y_mean

# 去重
with open('hs_info_5000.dict.pkl','rb') as f:
    tmp= pickle.load(f)
    houseInfo = np.array(tmp['通州'])
beg_t = time.time()
# 分离出rooms, feet, floor ,price
ht = houseInfo.T
# 构建X
fristCol = [1]*len(ht[0])
Attr=np.array([ht[1], ht[2], ht[4] ], dtype=np.float64).T
size=np.array( [ht[2]], dtype=np.float64).T
Attr2 = np.c_[size, size**0.5]
testA, testA_mean, testA_std = norm_A(Attr2)
price = np.array(ht[5].T, dtype=np.float64)
price, price_mean, price_std = norm_A(price, addcol=False)

# test 1 attribute
# theta2 = normal_equ(Attr2, price)
data_t = np.zeros(testA.shape[1])
theta_gra  = gra_descent(data_t, testA, price, 0.5)
end_t = time.time()
print('cost time: %s'%(end_t-beg_t))

# hypothesis
feet_in = list(range(1, 400)) 
# price_out = hypothesis(feet_in, theta_gra, Attr2, 
price_out = [hypothesis(feet, theta_gra, testA_mean, testA_std, price_mean, price_std) for feet in feet_in]
# print('squera: %.2f, price: %.2f'%(feet_in, price_out))

# plot
plt.figure(2)
# fet = list(range(-2,10)) 
# pri = [theta_gra[0]+theta_gra[1]*i for i in fet]
plt.plot(ht[2].T, ht[5].T, 'rx')
# line
plt.plot(feet_in, price_out)
plt.xlabel('feet')
plt.ylabel('price')
plt.show()
