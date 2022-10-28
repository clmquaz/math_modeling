import lec_3_my_module

#print(lec_3_my_module.a)

#b = lec_3_my_module.b * 3
#print(b)

import lec_3_my_module as lmm

#print(lmn.a)

#b = lmm*3
#print(b)
	
#print(lmm.c[2] + b + lmm.c[0])

#from lmm import a, b
#print(a*b)

#from lec_3_my_module import
#print(c[2] * c[1])

from lec_3_my_module import earth_mass as em
from lec_3_my_module import gravity_constant as G
from lec_3_my_module import sigma_steff_bolc as sigma

g = 500*G/10**2
print(g)

x = em*G*sigma
print(x)