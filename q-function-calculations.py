# IPython log file

from qutip import *
cdm = coherent_dm(3,sqrt(2))
cdm
cdm = coherent_dm(3,sqrt(0.5))
cdm
fdm = fock_dm(3,sqrt(0.5))
get_ipython().set_next_input(u'fdm = fock_dm');get_ipython().magic(u'pinfo fock_dm')
fdm = fock_dm(3)
fdm
get_ipython().set_next_input(u'fdm = fock_dm');get_ipython().magic(u'pinfo fock_dm')
fdm = fock_dm(3,1)
fdm
get_ipython().magic(u'pinfo thermal_dm')
thermal_dm.tr()
get_ipython().magic(u'pinfo tracedist')
thermal_dm
fdm
tdm = thermal_dm(3,sqrt(0.5))
tdm
tdm.sum()
sum(tdm)
tracedist(tdm)
get_ipython().magic(u'pinfo tracedist')
from scipy import *
tdm.tr
tdm.tr()
get_ipython().magic(u'pinfo num')
(tdm*num).tr
(tdm*num)
(tdm*num(3))
(tdm*num(3)).tr
(tdm*num(3)).tr()
thermal_dm(20,sqrt(0.5))*num(20).tr
thermal_dm(20,sqrt(0.5))*num(20)
(thermal_dm(20,sqrt(0.5))*num(20)).tr
(thermal_dm(20,sqrt(0.5))*num(20)).tr()
(thermal_dm(20,0.5)*num(20)).tr()
(coherent_dm(20,0.5)*num(20)).tr()
(coherent_dm(20,sqrt(0.5))*num(20)).tr()
get_ipython().magic(u'pinfo thermal_dm')
get_ipython().magic(u'pinfo coherent_dm')
(coherent_dm(20,sqrt(0.5))*num(20)).tr()
(coherent_dm(50,sqrt(0.5))*num(50)).tr()
qfunc(coherent_dm(50,sqrt(0.5)))
qfunc(coherent_dm(50,sqrt(0.5)),20)
qfunc
get_ipython().magic(u'pinfo qfunc')
qfunc(coherent_dm(50,sqrt(0.5)),linspace(-5,5,200),linspace(-5,5,200))
qdist = qfunc(coherent_dm(50,sqrt(0.5)),linspace(-5,5,200),linspace(-5,5,200))
imshow(qdist)
get_ipython().magic(u'pylab --no-import')
pylab.imshow(qdist)
cdm.matrix_element(basis(20,3),basis(20,3))
cdm.matrix_element(basis(50,3),basis(50,3))
cdm
cdm.matrix_element(basis(3,2),basis(3,2))
cdm.matrix_element(basis(3,2),basis(3,1))
(cdm*cdm).tr()
(tdm*tdm).tr()
cdm*cdm
tdm*tdm
get_ipython().magic(u'pinfo ptrace')
get_ipython().magic(u'pinfo tr')
get_ipython().magic(u'pinfo cdm.tr')
get_ipython().magic(u'pinfo cdm.ptrace')
cdm.ptrace(2)
cdm
cdm = coherent_dm(30,sqrt(5))
cdm
matrix_histogram(cdm)
hinton(cdm)
hinton(thermal_dm(20))
hinton(thermal_dm(20,4))
hinton(thermal_dm(20,10))
hinton(fock_dm(20,10))
hinton(coherent_dm(20,4))
hinton(coherent_dm(20,sqrt(4)))
cdm = coherent_dm(50,sqrt(5))
cdm
qfunc(cdm)
xvec = linspace(-5,5,200)
qvec = linspace(-5,5,200)
pvec = linspace(-5,5,200)
qdist = qfunc(cdm,qvec,pvec)
pylab.imshow(qdist)
cdm = coherent_dm(50,sqrt(3))
qdist = qfunc(cdm,qvec,pvec)
pylab.imshow(qdist)
qvec**2
q, p = meshgrid(qvec,pvec)
imshow(qdist*(q+p))
pylab.imshow(qdist*(q+p))
pylab.imshow(q+p)
pylab.imshow(qdist*(q**2+p**2))
(qdist*(q**2+p**2)).sum()
(qdist*(q**2+p**2)).sum()/2
(qdist*(q**2+p**2)).sum()/2.0
create(50)
(cdm*destroy(50)*create(50)).tr()
qdist
cdm = coherent_dm(5,sqrt(0.5))
cdm
pvec = linspace(-5,5,200)
qdist = qfunc(cdm,qvec,pvec)
qdist
pylab.imshow(qdist)
qdist.max()
qdist.sum()
qdist = qdist/qdist.sum*
qdist = qdist/qdist.sum()
qdist.max()
qdist.sum()
pylab.imshow(qdist)
(qdist*(q**2+p**2)).sum()/2.0
get_ipython().magic(u'logstart')
exit()
