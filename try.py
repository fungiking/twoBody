import  numpy as np
import matplotlib.pyplot as plt
from quspin.operators import hamiltonian
from quspin.basis import boson_basis_1d
from datetime import datetime
import pandas as pd
from multiprocessing import Pool

import math
from pathlib import Path
import gc
import sys


a=np.array([[1,2,3],[4,5,6],[3,2,3]])
u,v=np.linalg.eig(a)
print(np.argsort(a))
