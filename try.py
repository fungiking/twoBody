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
import pandas as pd

df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})
 # make sure indexes pair with number of rows

for index, row in df.iterrows():
    print(row[1])

