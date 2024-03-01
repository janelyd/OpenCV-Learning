#-------numeric types---------
# 1.int
# 2. float
# 3. complex

x= 10
print( "x: {}, type of x: {}".format(x,type(x)))

y= 3.7
print("y: {}, type of y : {}".format(y,type(y)))

z= 3+7j
print("z: {} , type of z : {}".format(z,type(z)))
      


# -------string---------
print(" -------string---------")
first_message = "hello world"
print(first_message)
# stringteki ilk karaktere erişme
print(first_message[0])
print(first_message[3])
print(first_message[2:7])
# 2 ile 7. karakter arasını yazıyor

# metinsel ifade ile sayı birleştirme
print(first_message + "ceren")

##### print(first_message + 5) #--> bu şekilde birleşemez
# 5 sayısı int. int ile string ifade birleşmesi için %'i integera çevirelim
print(first_message + str(5))




#------LIST-------
print("----lists-----")

first_list = ["ceren",-5, "enes",10.6, "5" ]
print(first_list)
print(first_list[0])
print(first_list[0:3]) #--> 0,1,2 alıcakEXCLUSIVE



#-----tuple---------
print("-----tuple---------")
first_tuple = ["ceren",-5, "enes",10.6, "5" ]
print(first_tuple)
print(first_tuple)
print(first_tuple[0])
print(first_tuple[0:3])
print(first_tuple[:3])


#---------dictionary-----------
# dictionaryler key ve value den oluşuyordu
first_dictionary = {"name" : "ceren",
                    "surname" : "işbilen",
                    "age": 22}
print(first_dictionary)
print(first_dictionary["name"])
print(first_dictionary["surname"])
print(first_dictionary["age"])

print(first_dictionary.keys()) #--> name surname çıktısı
print(first_dictionary.values())# --> ceren, 22 vs 

# EK BILGI: dictionaryleri yapay zekada çok kullanıyoruzz!




#--------boolean---------
a = True
print(a)
print(type(a)) #--> bool tipi olduüu bilgisi

b=False
print(b)
print(type(b))#--> bool tipi olduüu bilgisi

c=None
print(c)
print(type(c))#--> nonetype tipi olduüu bilgisi
