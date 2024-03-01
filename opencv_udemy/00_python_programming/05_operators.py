a = 10
b = 15

# ----------arithmetic operators----------
print("a+b : ",a+b)
print("a-b : ",a-b)
print("-a-b : ",-a-b)


c=-(a+b)
print("-(a+b) : ", c)

exponent = a**b
print("a^b: ",exponent)

division = a/b
print("a/b : ", division)

floor_division = b//2
print("15//2 :",floor_division)
floor_division = b//3
print("15//3 :",floor_division)


modulus = b%2
print("15'i 2ye böldüğünde kalan: ", modulus)
 



#------------comparison operators----------

x = 10
y =11
z= - 11

print("x==y : ", x==y)# -->false: a ve b eşit ise true döndürecek

print("x!=y : ", x!=y) # true 

print("-y==z : ", -y==z) # true

print("x>y : ",x>y)
print("x<y : ",x<y)
print("x>=y : ",x>=y)
print("x<=y : ",x<=y)


# -----------assignment operators------------
# = atama yapar, == eşit mi

k=5
print(" k + 5 =: ", k + 5)

k+=5
print(k)
k= 5
k *=3
print("k*3 :" ,k)





# ----------------logical operators----------------
a = True
b = True
c = False

print("a and b:", a and b) # T
print("a or b ", a or b)
print(" a or c :", a or c)
print("b and c", b and c)
print(c or c)
print("not a :", not a )
print("not a :", not(a) )