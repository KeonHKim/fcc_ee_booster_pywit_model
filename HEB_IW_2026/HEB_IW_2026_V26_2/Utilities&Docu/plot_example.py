#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
for plane,title,unit in [('long','Longitudinal','Ω'),('dipx','Horizontal dipolar','Ω/m'),('dipy','Vertical dipolar','Ω/m')]:
    suffix='' if plane=='long' else '_beta_weighted'
    f,re,im=np.loadtxt(ROOT/'Impedances/Total'/f'Z_total_{plane}{suffix}_v26_2.txt',unpack=True)
    fig,ax=plt.subplots(2,1,figsize=(9,6),sharex=True,layout='constrained')
    for a,v,name in zip(ax,(re,im),('Re','Im')):
        y=np.where(np.isfinite(v)&(v>=1),v,np.nan)
        a.fill_between(f,1,y,color='#217188',alpha=.20)
        a.plot(f,y,color='#217188',lw=1.3)
        a.set_yscale('log');a.set_ylim(bottom=1)
        a.set_ylabel(f'{name}(Z) [{unit}]');a.grid(alpha=.2,which='both')
    ax[-1].set_xlim(0,50);ax[-1].set_xlabel('Frequency [GHz]')
    fig.suptitle(f'HEB V26.2: {title} (positive display only)');plt.show()
