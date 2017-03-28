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

        # err_expand = np.tile(err,(x_n,1)).T
        # multi_arr = err_expand*X
        # tmp = []
        # for i in range(multi_arr.shape[1]):
            # tmp.append(multi_arr[0:,i].sum())
        # tmp = np.array(tmp)

        tmp = np.dot(err, X)
        remain = rate*tmp/m

        if abs( remain.sum()) > 1e-6:
            theta = theta - remain
        else:
            break
    return theta

def hypothesis(x, theta, x_mean, x_std, y_mean, y_std):
# def hypothesis( x, theta, A, Y):
    print('--------- hypothesis ----------')
    # x = x/ x_std 
    # x = (x-A.mean(axis=0))/ (A[:,1:].max(axis=0)-A[:,1:].min(axis=0)) 
    x = (x-x_mean)/ x_std
    x = [1, x]
    y = np.dot(theta.T, x)
    # return y*y_std
    # return y*(Y.max(axis=0)-Y.min(axis=0)) + Y.mean(axis=0)
    return y*y_std+y_mean

# 去重
with open('hs_info_1000.pkl','rb') as f:
    tmp= pickle.load(f)

beg_t = time.time()

# 分离出rooms, feet, floor ,price
ht = houseInfo.T

# 构建X
fristCol = [1]*len(ht[0])
Attr=np.array( [fristCol, ht[1], ht[2], ht[4] ], dtype=np.float64).T

Attr2 =np.array( [fristCol, ht[2]], dtype=np.float64).T
# mean norm Attr2
attr2_mean = Attr2[:,1:].mean(axis=0)
attr2_std = np.std(Attr2[:,1:], axis=0)
attr2_scale = Attr2[:,1:].max(axis=0) - Attr2[:,1:].min(axis=0)
# Attr2[:,1:] = (Attr2[:,1:])/ attr2_std
Attr2[:,1:] = (Attr2[:,1:] - attr2_mean)/ attr2_std # mean norm with standard deviation
# Attr2[:,1:] = (Attr2[:,1:] - attr2_mean)/ attr2_scale # mean norm with scale
price = np.array(ht[5].T, dtype=np.float64)
# norm price
price_mean = price.mean(axis=0)
price_std = np.std(price, axis=0)
price_scale = price.max(axis=0) - price.min(axis=0)
# price = (price )/ price_std
price = (price - price_mean)/ price_std # mean norm with standard deviation
# price = (price - price_mean)/ price_scale # mean norm with scale

# test 3 attribute
test_init = np.array([80,20,10,1])
theta = normal_equ(Attr, price)

# test 1 attribute
# theta2 = normal_equ(Attr2, price)
data_t = np.array([0,0])
theta_gra  = gra_descent(data_t, Attr2, price, 1)
end_t = time.time()
print('cost time: %s'%(end_t-beg_t))

# hypothesis
feet_in = 130
# price_out = hypothesis(feet_in, theta_gra, Attr2, 
price_out = hypothesis(feet_in, theta_gra, attr2_mean, attr2_std, price_mean, price_std)
# price_out = hypothesis(feet_in, theta_gra, attr2_mean, attr2_scale, price_mean, price_scale)
print('squera: %.2f, price: %.2f'%(feet_in, price_out))

# plot
plt.figure(2)
fet = list(range(-2,10)) 
pri = [theta_gra[0]+theta_gra[1]*i for i in fet]
plt.plot((Attr2.T)[1], price, 'rx')
plt.plot(fet, pri)
plt.show()

