# coding: utf-8
# 通过蒙特卡洛模拟方法估计欧式看涨期权的价值
#Black-Scholes-Merton（BSM）模型
import numpy as np
import matplotlib.pyplot as plt
from time import time

def bsm_standard_normal(I):
    return np.random.standard_normal(I)

def bsm_index_level(S0,r,sigma,T,z):
     return S0 * np.exp((r - 0.5 * sigma ** 2)* T + sigma * np.sqrt(T) * z)

def bsm_future_intrinsic_vale(ST,K):
     return np.maximum(ST - K, 0)

def bsm_option_value(r,T,hT,I):
     return np.exp(-r * T)* np.sum(hT)/I

def draw_pic(position,y,label,plt):
    plt.subplot(position)
    plt.plot(y, label=label)
    plt.grid(True)
    plt.legend(loc=0)
    plt.ylabel(label)


def print_curve_graph(ST, hT):
    plt.figure(figsize=(12, 7))
    draw_pic(211, ST, 'S_T', plt)
    draw_pic(212, hT, 'h_T', plt)
    plt.savefig('STHT.png', format='png')

def bsm_option_pricing( S0 = 100,K = 105,T = 1,r = 0.05,sigma = 0.2, I = 1000):
    #初始股票指数水平 S0 = 100
    #欧式看涨期权的行权价格 K = 105
    #到期时间 T = 1
    #固定无风险短期利率 r = 0.05
    #固定波动率 sigma = 0.2
    #随机数个数 I = 1000
    
    #从标准正态分布中取得随机数序列
    z = bsm_standard_normal(I)
    start = time()
    #股票到期指数水平
    ST = bsm_index_level(S0,r,sigma,T,z)
    #到期时期权内在价值
    hT = bsm_future_intrinsic_vale(ST,K)
    #期权现值
    C = bsm_option_value(r,T,hT,I)
    end = time()
    print('toatl time is %.6f seconds' % (end - start))
    # 输出期权现值
    print('value of the European call option %.6f' % C)
    #输出结果
    print_curve_graph(ST, hT)

def main():
    bsm_option_pricing()