import math
import matplotlib.pyplot as plt
import numpy as np

def a1(b):

    N = 500
    x = []
    y = []

    for f in np.linspace(0, 8, N):
        f*=np.pi
        r = math.e**(b*f)
        #r = b**f
        xx = r*np.cos(f)
        yy = r*np.sin(f)
        x.append(xx)
        y.append(yy)
    plt.plot(x, y)
    plt.savefig('p4_1')

def a2(k):

    N = 500
    x = []
    y = []

    for f in np.linspace(0, 8, N):
        f*=np.pi
        r = k*f
        xx = r*np.cos(f)
        yy = r*np.sin(f)
        x.append(xx)
        y.append(yy)
    plt.plot(x, y)
    plt.savefig('p4_2')

def a3(k):
    N = 500
    x = []
    y = []

    for f in np.linspace(0, 8, N):
        f*=np.pi
        r = k/np.sqrt(f)
        xx = r*np.cos(f)
        yy = r*np.sin(f)
        x.append(xx)
        y.append(yy)
    plt.plot(x, y)
    plt.savefig('p4_3')

def a4(k):
    N = 500
    x = []
    y = []

    for f in np.linspace(0, 8, N):
        f*=np.pi
        r = np.sin(k*f)
        xx = r*np.cos(f)
        yy = r*np.sin(f)
        x.append(xx)
        y.append(yy)
    plt.plot(x, y)
    plt.savefig('p4_4')

