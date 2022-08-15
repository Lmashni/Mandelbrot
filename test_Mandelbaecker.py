from Mandelbaecker import C
import numpy as np

def test_C():
	'''
	hi
	'''
	assert (C(0,2,2) == np.array([[-2.-2.j,  2.-2.j], [-2.+2.j,  2.+2.j]])).prod()
