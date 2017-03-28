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
        x_n = len(X[1]) # 样本的特征的个数
        err = np.dot(X,theta)-y # 估值与真实值之间的偏差
        # 计算J的值
        J = 1/(2*m) * (err**2).sum()
        print('J=',J)
        # 更新theta
        # 将err扩充成mxn矩阵，直接与X相乘
        err_expand = np.tile(err,(x_n,1)).T
        multi_arr = err_expand*X
        tmp = []
        for i in range(multi_arr.shape[1]):
            tmp.append(multi_arr[0:,i].sum())
        tmp = np.array(tmp)
        remain = rate*tmp/m
        if abs( remain.sum()) > 0.001:
            theta = theta - remain
        else:
            break
    return theta

def hypothesis(x, theta):
    print('-------- hypothesis --------')
    x = [1, x]
    return np.dot(theta.T, x)

# 去重
with open('hs_info_1000.pkl','rb') as f:
    tmp= pickle.load(f)

beg_t = time.time()
houseInfo = np.array(list(set(map(tuple, zip(*tmp)))))

# 分离出rooms, feet, floor ,price
ht = houseInfo.T
# 构建X
fristCol = [1]*len(ht[0])
Attr=np.array( [fristCol, ht[1], ht[2], ht[4] ], dtype=np.float64).T
# y
price = np.array(ht[5].T, dtype=np.float64)

# debug
Attr2 =np.array( [fristCol, ht[2]], dtype=np.float64).T

test_init = np.array([80,20,10,1])
theta = normal_equ(Attr, price)
theta2 = normal_equ(Attr2, price)
data_t = np.array([0,0])
t = gra_descent(data_t, Attr2, price, 0.00005)
end_t = time.time()
print('cost time: %s'%(end_t-beg_t))

feet_in = 130
price_out = hypothesis(feet_in, t)
print('squera: %.2f, price: %.2f'%(feet_in, price_out))

'''
# plot
fet  = list(range(400)) 
pri = [theta2[0]+theta2[1]*i for i in fet]
plt.plot((Attr2.T)[1],price, 'rx')
plt.plot(fet, pri)
plt.show()
'''

