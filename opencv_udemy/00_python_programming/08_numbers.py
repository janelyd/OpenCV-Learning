#---------  type conversion---------
# 1 int()
# 2 float()
# 3 complex()

a = 12
print(type(a))

complex_a = complex(a)
print(complex_a)
# 12 + 0j

# important methods

# 1 range()
# 2 leng()
# 3 abs()
# 4 random ()

# -pi
# -e

range(5)
print(range(5))

# range i döngude kullanabiliriz
for i in range(5):
    print(i)

# belli aralıktaki sayıları yazdırma
for i in range (2,5):
    print(i)

# ardışık yazdırma
    # 2 den 50 ye kadar 5 er artarak :
    # -5 yazarsak 5 azalarak olur
for i in range(2, 50, 5):
    print(i)


programming_lans = ["pyth", "java", "c++","c#"]
# ilk böyle de yazabiliriz
for i in programming_lans:
    print(i)

# böyle de  
for i in range(4):
    print(programming_lans[i])  
    
# listede kaç eleman olduğunu görmek için!!
len(programming_lans)
print(len(programming_lans))

# ---listede fazla eleman olsaydı ;
# range(4) ==>> range(len(programming_langs)) 
for i in range(len(programming_lans)): 
    print(programming_lans[i])


#--random methodu--

import random
# 0 ile 1 arasında random sayı üretmek için
print(random.random())
# 1 ile 10 arası random integer sayı üretmek için
print(random.randint(1,10))


# ---mutlak alma---
# abs() --> mutlak alma methodu
print(abs(-5))

# sabitler : pi,e
import math
print(math.pi) # math kütüphanesinden pi'yi çağırdık