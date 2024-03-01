print("ceren işbilen")
name = "enes birlik"
print(name)

age= 26
print(age)

"""
print --> name: ceren işbilen
        age: 21
"""
print("name; ", name)
print("age; ", age)
# c'deki gibi aslında, virgülenden sonra yazdırmak istediğin değişken
print(2,3, name, "alitan",2.1)

print("my name is ", name + ".", "i am ", age, "years old")# boşluk arada var
print("my name is ", name , ".", "i am ", age, "years old")# arada boşluk yok

print(" mete" + "han")
#  metehan
#  + boşluk bırakmadan string birleştiriyor

# new line koutu ---\n
print("my name is ", name + ".\n", "i am ", age, "years old")# boşluk arada var

x1 = 25
y1 = 50
z1= 75
print(x1,y1,z1, sep= "-")
# sep fonksiyonu ayırmak için kullanılır

# ------output formatting-----
# my name is {}
#.format(name,age)

print("my name is {} and i am {} years old".format(name,age))

print("my name is {0} and i am {1} years old".format(name,age))
print("my name is {1} and i am {0} years old".format(name,age))
""" my name is 26 and i am enes birlik years old """