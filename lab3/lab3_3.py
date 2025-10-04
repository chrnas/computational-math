from Lagrange_interpolation import Lagrange_interpolation, build_Interpolation
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

datapoints = [(1,1), (2,1), (3,2), (4,6), (5,24)]

X, L = build_Interpolation(datapoints, M =150)