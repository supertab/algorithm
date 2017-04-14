# coding: utf8
'''
# 二分法查找和插值查找（按比例查找），都是基于数据已经排好了顺序，再进行查找
# 二分法：比例是固定的，每次对半找
# 插值法：比例根据需要查找的数据来定，自动更新比例(适用于数据分布均匀的情况)
# 程序说明：
  - method 设置为 fixed_rate 将进行二分查找
  - auto_rate: 进行插值查找
'''

def order_search(d, k, method='auto_rate'):
    # d = range(13)
    low = 0
    high = len(d)-1
    scal = high - low
    iter=1
    if method == 'fixed_rate':
        rate = 1/2
    while low <=high: 
        if method == 'auto_rate':
            rate = (k - d[low])/ (d[high] - d[low])
        mid = low + int(rate * scal)    
        print('iter %d -- high:%s, mid:%s, low:%s'%(iter, high, mid, low))
        if k==d[mid]:
            print('find %s at pos:'%k, mid)
            break
        elif k<d[mid]:
            high = mid-1
        else:
            low = mid + 1
        scal = high - low
        iter += 1
    if low>=high:
        print('not find...')

if __name__=="__main__":
    d =[0,1,2 , 9,11, 12, 15, 23, 52, 58, 90] 
    k = 2.2 
    order_search(d, k)



