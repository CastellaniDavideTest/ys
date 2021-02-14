"""Test ys file
"""
from ys import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-2-14"

def test():
	"""Tests the ys function in the ys class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert ys.ys() == "ys", "test failed"
	#assert ys.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
