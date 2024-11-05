# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:31:27 2018

@author: ikulikov
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rc
import numpy as np
import matplotlib as mpl


exp_data = pd.read_csv('133Cs_1200ms_tof_icr.txt', sep=" ", header=None)
exp_data.columns = ["x", "y", "yerr"]
exp_data.x = exp_data.x -685136.6507

fit_data = pd.read_csv('133Cs_1200ms_tof_icr-fit.txt', sep=" ", header=None)
fit_data.columns = ["x", "y"]
fit_data.x = fit_data.x -685136.6507

ax = exp_data.plot.scatter('x','y', yerr='yerr', c='k', marker='o', s=20)
fit_data.plot('x','y', color='red',ax=ax )
ax.set_ylabel('Mean time of flight, $\mu$s',fontsize=16)
ax.set_xlabel("Excitation frequency-685136.6507, Hz",fontsize=16)
ax.legend(('fit','data'),loc='lower right')
plt.text(-2.5, 145,'T$\ _{rf.}$= 1.2 s',fontsize=14)
plt.text(-2.5, 150,'$^{133}$Cs$^{+}$',fontsize=20)
ax.tick_params(which='major', right=True, top=True, bottom=True, labelleft='on', labelright='on', labelsize=14)
ax.tick_params(which='minor', right=True, top=True, bottom=True, labelleft='on', labelright='on', labelsize=12)
plt.tight_layout()
plt.savefig("133Cs.pdf")
plt.show()
