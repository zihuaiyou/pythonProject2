# lists = [1,2,3,4]
# for index , val in enumerate(lists):
#     print(index,val)

# list1= [1,2,3]
# list2=['a','b','c']
#
# print(dict(zip(list1,list2)))
# import math
# print(math.asin(1)==math.pi/2)
# print(1/math.sqrt(9))
# print(""or '123')
from scipy.optimize import fsolve
import numpy as np

# 按格式要求定义我们需要求的函数
def f(x):
    return np.arcsin(x) - x
# 调用fsolve函数
sol_fsolve = fsolve(f, [0]) # 第一个参数为我们需要求解的方程，第二个参数为方程解的估计值
print(sol_fsolve)