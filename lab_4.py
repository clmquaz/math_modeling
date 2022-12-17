import numpy as np
import scipy
import matplotlib.pyplot as plt

def wand (pi=8*np.pi, b=2):
    q = np.arange(0.01, pi, 0.1)
    r = 1.380649*10**(-23)/0.5**(-q)
    x = r*np.cos(q)
    y = r*np.sin(q)
    plt.plot(x, y)
    plt.savefig('plt.png')
print(wand())

def spiral (pi=8*np.pi):
    q = np.arange(0, pi, 0.1)
    r = 1.380649*10**(-23) * q
    x = r*np.cos(q)
    y = r*np.sin(q)
    plt.plot(x, y)
    plt.savefig('spr.png')
print(spiral())

def logarithmic (pi=8*np.pi, b=2):
    q = np.arange(0, pi, 0.1)
    r = np.exp(b*q)
    x = r*np.cos(q)
    y = r*np.sin(q)
    plt.plot(x, y)
    plt.savefig('pp.png')
print(logarithmic())


def rose (pi=8*np.pi, b=2, k = 1000):
    q = np.arange(0, pi, 0.1)
    r = np.sin(k*q)
    x = r*np.cos(q)
    y = r*np.sin(q)
    plt.plot(x, y)
    plt.savefig('yy.png')
print(rose())


