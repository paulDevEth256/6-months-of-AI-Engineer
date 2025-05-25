"""
step-14.py
Step 14: Modules and Packages
"""
# module usage
import os, sys, math
print(os.getcwd(), sys.platform, math.pi)
# custom module (assuming util.py exists)
# from util import helper
# helper()
# Package: directory with __init__.py
# if __name__ == "__main__": usage
print(__name__)
