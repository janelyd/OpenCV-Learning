#----loops-----
#1-while
# 2-for 
# 3-nested loops



# # while loop

# counter = 1
# # 1er 1er artırıp 10a kadar gitmek için:
# while counter<=10:
#     print(counter)
#     counter = counter + 1
#     # if counter == 8:
#     #     break
#     # elif counter < 5 :
#     #     print("good number {}".format(counter))
#     # else :
#     #     print(" bad number {}".format(counter) )





# LOOP İÇİNDE KARAR YAPISI:


# for döngüsü
test_list = [1,2,3,4]
print(test_list[0])
print(test_list[1])
print(test_list[2])
print(test_list[3])

for i in [1,2,3,4]: #--> i nin test listesinde gezinmesi demek
    print(i)

test_list2 = ["html","java","donald"]
for i in test_list2:
    print(i) # i tek tek html java dolaştı


for i in "python":
    print(i)   # i tek tek karakterleri dolaşacak  
# p
# y
# t
# h
# o
# n
    
    
for i in "python":
    print(i)   # i tek tek karakterleri dolaşacak  
    if i == "h":
        print("warning!")

# p
# y
# t
# h
# o
# n
        
for i in [1,2,3,4]:
    print("i:",i)
    for j in ["a","b","c" , "d"]:
        print("j :",j)
    
# continue , pass

for i in "python":
    if i == "t":
        continue
    print(i) # --> t yi görünce başa sarıyor

for i in "ceren":
    if i == "r":
        pass # ?????????????????????????????????
    # i = "r" oldugunda o adımı yok say
    else :  
        print(i)



