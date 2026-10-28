#!/usr/bin/env python3
"""Check consistency of published full-ring totals and six-component files."""
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
FAMILIES = ('RW', 'Wiggler', 'Kicker', 'RF', 'BPM', 'Bellows')
for plane in ('long','dipx','dipy'):
    beta='' if plane=='long' else '_beta_weighted'
    z=np.loadtxt(ROOT/'Impedances/Total'/f'Z_total_{plane}{beta}_v26_2.txt')
    budget=np.genfromtxt(ROOT/'Impedances/Devices'/f'HEB_V26_2_all_component_budget_{plane}.csv',delimiter=',',names=True)
    assert len(z)==len(budget), 'Mismatched impedance grid'
    np.testing.assert_allclose(z[:,0],budget['frequency_GHz'],rtol=1e-9,atol=1e-9)
    for j,part in enumerate(('Re','Im'),1):
        np.testing.assert_allclose(z[:,j],budget[part+'_Total'],rtol=1e-8,atol=1e-4)
        np.testing.assert_allclose(sum(budget[part+'_'+f] for f in FAMILIES),budget[part+'_Total'],rtol=1e-8,atol=1e-4)
    w=np.loadtxt(ROOT/'Wakes/Total'/f'W_total_{plane}{beta}_sigma0p4mm_v26_2.txt')
    cw=np.genfromtxt(ROOT/'Wakes/Devices'/f'HEB_V26_2_all_component_wakes_{plane}_sigma0p4mm.csv',delimiter=',',names=True)
    assert len(w)==len(cw), 'Mismatched wake grid'
    np.testing.assert_allclose(w[:,0],cw['s_mm'],rtol=1e-9,atol=1e-8)
    np.testing.assert_allclose(w[:,1],cw['Total'],rtol=1e-8,atol=1e-4)
    np.testing.assert_allclose(sum(cw[f] for f in FAMILIES),cw['Total'],rtol=1e-8,atol=1e-4)
    print('PASS:',plane)
print('All three planes checked.')
