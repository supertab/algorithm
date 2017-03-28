# 目标是找到合适的theta是J(theta)最小
import numpy as np
import pickle, time
import matplotlib.pyplot as plt
from pylab import * 
zhfont = mpl.font_manager.FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc')

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

def format_info(ht):
    # 构建X
    size=np.array( [ht[2]], dtype=np.float64).T
    Attr2 = np.c_[size, size**0.5]
    X = norm_A(Attr2)
    price = np.array(ht[5].T, dtype=np.float64)
    price = norm_A(price, addcol=False)
    return X, price

def hypothesis(x, theta, x_mean, x_std, y_mean, y_std):
    x = np.array([x, x**0.5])
    x = (x-x_mean)/ x_std
    x = np.append(np.ones(1), x)
    y = np.dot(theta.T, x)
    return y*y_std+y_mean

# 去重
with open('hs_info_5000.dict.pkl','rb') as f:
    tmp= pickle.load(f)

region_list = [i for i in tmp.keys()]

i = 1
fig = plt.figure(figsize=(6, 6))
# fig = plt.figure()
for region in region_list[:6]:
    houseInfo = np.array(tmp[region])
    ht = houseInfo.T
    X, price = format_info(ht)
    # unwrap
    testA, testA_mean, testA_std = X
    price, price_mean, price_std = price
    theta_init= np.zeros(testA.shape[1])
    theta = gra_descent(theta_init, testA, price, 0.5)
    # hypothesis
    feet_in = list(range(1, 400)) 
    price_out = [hypothesis(feet, theta, testA_mean, testA_std, price_mean, price_std) for feet in feet_in]
    # plot
    pos = '32'+str(i)
    fig.add_subplot(pos)
    plt.xlim(0,350), plt.ylim(0,3000)
    plt.plot(ht[2].T, ht[5].T, 'rx')
    plt.plot(feet_in, price_out)
    plt.xlabel('面积(m^2)',fontproperties=zhfont)
    plt.ylabel('房价(万元）',fontproperties=zhfont)
    plt.title(region, fontproperties=zhfont)
    i +=1
fig.subplots_adjust( wspace=0.5,hspace=1)
plt.show()
