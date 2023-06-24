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
newN = 3
newBasisAll=boson_basis_1d(newN,Nb=2)
newSubLatOpList=[]
for j in range(0,newN):
    listTmp = [[1, j]]
    staticTmp = [["n", listTmp]]
    opTmp = hamiltonian(staticTmp, [], dtype=np.complex128, basis=newBasisAll,check_symm=False,check_pcon=False,check_herm=False)
    print(opTmp)
    arrTmp = opTmp.tocsc()
    newSubLatOpList.append(arrTmp)




