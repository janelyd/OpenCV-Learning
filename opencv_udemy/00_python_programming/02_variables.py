# integer variables

x = 5
print(x)
print("x")
# değişken tnaımlarken başta sayı olmamalı
x_type = type(x)
# type control
print(x_type)
print(type("x"))

name = "donald trump"
print(name)
print(type(name))


str_number = "15"
print(type(str_number))
# string döndürdü

#---float---
z = 5.3
print(z)
print(type(z))

# -- type casting(değişken dönüştürme)---
x=15
y="22"
z= "tom hardy"
x_to_string = str(x)
print(type(x_to_string))
print(x_to_string)

y_to_int = int(y)
print(type(y_to_int))
print(y)

z_to_int = int(z)
print(type(z_to_int))
# error var, içeride sayı olmadığı için -->
# integera dönüştüremedik


# ip uçları
x1= 50
# işim bittikten sonra değişken silmek için
print(x1)
del x1
print(x1)



# aynı satırda yazma
x=5
y= 7
x,y = 5,7
w,z,q,e= 2,[2,3,4],"antalya",6.3

# global, local değişkenler

def add(a,b):
    z_sum = a+b 
    print(z_sum) #--->bunun yeri de önemli
# print z_sum kısmı define içinde olmalı
