import pandas as pd
import numpy as np
import scipy as sc
from scipy import stats as st
single = np.array([5, 4, 4, 3, 9, 4])
twins = np.array([4, 8, 7, 5, 1, 5])
triplets = np.array([9, 9, 8, 10, 4, 10])
annova= st.f_oneway(single,twins,triplets)
print(annova)