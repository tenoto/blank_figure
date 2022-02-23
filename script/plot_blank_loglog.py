#!/usr/bin/env python

import matplotlib.pylab as plt 

#fig = plt.figure(figsize=(11.69,8.27),tight_layout=True)
fig = plt.figure(figsize=(11.69,11.69),tight_layout=True)
plt.rcParams["mathtext.fontset"] = "dejavuserif"	
plt.rcParams["font.size"] = 20
plt.rcParams["font.family"] = "serif"
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8

plt.plot([1,1e+18],[1,1e+18],'k--',linewidth=1)
plt.xlabel(r"Induction electric field (V)", labelpad=18)
plt.ylabel(r"Observed maximum electron energy (eV)", labelpad=18)
plt.xscale('log')
plt.yscale('log')
plt.xlim(1,1e+18)
plt.ylim(1,1e+18)
#plt.ylim(1e-2,1e+5)
#plt.legend(loc='lower center')

plt.tick_params(axis="both", which='major', direction='in', length=8)
plt.tick_params(axis="both", which='minor', direction='in', length=5)
plt.grid(True,which='major',linestyle='-')
plt.grid(True,which='minor',linestyle='-.')
plt.minorticks_on()

plt.tight_layout(pad=2)
plt.savefig('out/blank_loglog.pdf')
