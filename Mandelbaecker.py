#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:16:30 2020

@author: lyth
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams as rc

def C(cnt=0j, l=2, dim=128):
    """ 
    C(cnt=0, l=2, dim=128)
    
    Creates a complex array of shape (dim, dim) representing part of the complex 
    plane, centered around cnt and extening from -l to l
    
    Parameters
    ------------
    cnt : complex 
        complex number arround which the array fould be centered.
    l : float
        extent of complex domain.
    dim : int
        dimentions of array
    
    Returns
    ---------
    out : numpy.ndarray
        A complex array to input into the mandelbrot iteration
    """
    c =np.zeros((dim,dim),dtype=complex)
    for i in range(len(c)):
        c[i,:] += np.linspace(cnt.real-l,cnt.real+l,dim)
        c[:,i] += np.linspace(cnt.imag-l,cnt.imag+l,dim)*1j
    return c

def Mandel_Iter(z,cnst):
    """
    Mandel_Iter(z,cnst)
    
    executes a single Mandelbrot iteration According to z(1) = z(0) *z(0) + cnst. 
    Typicly the first iteration starts at z = 0. Depending on the value of cnst
    the series converges, in which case it is part of the Mandelbrot set, or deverges
    in which case its outside. 
    
    Parameters
    ----------
    z : complex or ndarray
        starting value of iteration
    cnst : complex or ndarray
        postition in complex plane to execute interations
    Returns
    -------
    out : complex or ndarray
        result of Mandelbrot iterations
    """
    return z**2 + cnst
    


def label_nans(x):
    """
    label_nans(x)
    
    Discard nans from given array. Sets nans to 0 and other to 1
     
    
    Parameters
    ----------
    z : ndarray
    -------
    out : ndarray
        array with 1s where there was no nan
    """
    #for x,i in zip(X,range(len(X))):
    x[np.logical_not( np.isnan(x))] = 1
    x[ np.isnan(x)] = 0
    return x

def divergence_map(z,cnt,itrs):
    x = np.zeros(z.shape,dtype = complex)
    for i in range(itrs):
        if i%int(itrs/5)==0:
            print(i)
        z = Mandel_Iter(z,cnt)
        x += label_nans(z.copy())
    return x

def normalize(xx):
    return (xx.real+xx.real.min())/(xx.real+xx.real.min()).max()

def show(xx,cnt,l):
    rc.update({'font.size': 12})

    plt.imshow(xx.real,alpha=normalize(1/xx),extent=[cnt.real-l,cnt.real+l,cnt.imag-l,cnt.imag+l],cmap='inferno')
    plt.imshow(xx.real,alpha=normalize(xx**(2)),extent=[cnt.real-l,cnt.real+l,cnt.imag-l,cnt.imag+l],cmap='jet')
    plt.imshow(xx.real,alpha=normalize(1/xx),extent=[cnt.real-l,cnt.real+l,cnt.imag-l,cnt.imag+l],cmap='inferno')

    plt.imshow(xx.real,alpha=normalize(xx**(2)),extent=[cnt.real-l,cnt.real+l,cnt.imag-l,cnt.imag+l],cmap='jet')
    plt.title('diverged after n iteration of '
                  r'$z_{n}(c) = z_{n-1} + c $'
                  '\n at   '
                  r'$c = x + yi$')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.colorbar(label='n')
    plt.show()
    
# select resolution and number of iterations to do.
dim = 1024
itrs = 1000

# choose the region of the comlex plane where to do the iterations. The reggion is centered around
# cnt and has extent l. below are a few commen adresses. Uncomment to chose.

cnt,l = -1.25066+ 0.02012j , 1.7e-4

# set up input arrays
c =C(cnt,l,dim)
z =np.zeros((dim,dim))

# Make divergence map
div_map = divergence_map(z,c,itrs)



show(div_map,cnt,l)
