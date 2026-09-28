# print("hello world")
# a = 22
# a = a * 3
# print(a)
# print (type(a))
# print(type(3.6))

#----------------

# print(int(4.7))   #throws away the 0.7 ---> 4
# print(float(5))   #5.0
# print(type(float(6)))  #class 'float'
# print(round(5.55))    #6
# print(round(5.5))    #6
# print(round(4.7))    #5

#---------------

#print(int(float("10.6")))  #10
#s = "salam"
# print(s[0])  #s
# print(s[2])  #l
# print(s[-2]) #a
# print(s[0:3]) #sal  #0, 1 and 2 (right befor the 3rd one) 
#step --> up to but not including
#print(s[::-1]) #malas (reversed)

#---------------

#str.   #that dot gives us options to alter the characteristics of a string

# import math
# math.           #now we have access to math library and can use more options. the dot bring us the options of the imported library
# print(5 + 5)
# print(11//3)    #3
# print(11%3)     #2 (باقی مانده)
# print(2**5)     #32 (توان)

# print("abc"*2)  #abcabc
# print("werty"+"sdfgh")   #abcabc
# print(type("werty"+"sdfgh"))   #<class 'str'>

# a = True
# print(type(a))  #<class 'bool'>
# b = False                           #boolian = false or true
# print(type(b))  #<class 'bool'>

#-------------- شرط
# if:       elif:  (else is)       else: اگه هکه شرطای بالا درست نبود  
# > < >=  <=  == (بجای مساوی از دوتا مساوی استفاده می کنیم)  != مساوی نیست  
# print(10 == 2)  #false

# if 10 != 5:
#     print("nimosavi nist")    #nimosavi nist
# if 10 >= 9:
#     print("yes")  #yes

# a = 5
# print("salam:", a)  #salam: 5

# a = 24
# if a > 31:
#     print("greater than")
# elif a == 5:
#     print("mew")
# else:
#     print("is not grater than",a)  #is not grater than 24

#------------------


# for i in iterable:
#     statemebt               i,j,k estefade mishe

# for i in "salam":
#     print(i)        
# # s
# # a
# # l
# # a
# # m
# for i in "salam":
#     print(5)  
# # 5
# # 5
# # 5
# # 5
# # 5
# for i in 100:
#     print(5)     KeyError

# for i in str(100):
#     print (int(i))
# # 1
# # 0
# # 0

# for i in range (0, 5):         1 ta 4
#     print(i)

# for i in range (5+1):            1 ta 5
#     print(i)

# for i in range (1, 5+1,+2):         1, 3, 5  do ta do ta mire   
#     print(i)

# for i in range (10000):         1 ta 999
#     print(i)

#-------------

# a= 5
# while a >= 0:
#     print(a)       # تا ابد می نویسه میو
#     a -= 1  (یدونه ازش کم کن)
# 5
# 4
# 3
# 2
# 1
# 0
# a = 1000
# while True:
#     print(a)
#     a -= 1
#     if a < 0:
#         break       1000 ta 0 


# a = 1000
# while True:
#     print(a)
#     a -= 1
#     if a < 100:      هزار تا صد رو می نویسه برک یعنی اینجا دیگه حلقه رو تامام تامام کن
#         break        

# for i  in range(10):
#     if i == 4:
#         break     #0, 1, 2, 3
#     print(i)

# for i in range(10):
#     if i ==4:
#         continue
#     print(i)            #0,1,2,3,5,6,7,8,9,   چهار رو حذف کرده از چهار گذشته

#--------------

# import random                            کتابخونه رندوم رو ایمپورت کردیم و با رند اینت، اینتجر رندوم داد بهمون
# print(random.randint (5, 25))

#--------------

# list []       dict        set         tuple   

# a = []
# print(type(a))    #<class 'list'>

# a = [1, 3.5, "mew", 10]
# print(a[-1])                  #اگر پشت براکت متغیر بذاری اندیس هارو بهمون میگه. مثلا اولین المان
#                               # اندیس منفی یک اخرین المان رو میده که 10 هست

# a = [1, 3.5, "mew", 10, [4, [67, ["mew"]]]]          #[67, ['mew']]
# print(a[-1] [-1])

#a.append(10000)                  #[1, 3.5, 'mew', 10, [4, [67, ['mew']]], 10000]   added 10000
# a.pop()                           #delete the last element   you can give it an index to delete 
# print(a)          

# a = [1, 2, 3, 45, 8, 9, 356, 2]
# zoj = []
# for i in a:
#     if i % 2 == 0:
#         zoj.append(i)
# print(zoj)      #[2, 8, 356, 2]

#--------------------------

# print([1+2+3] + [4+5+6])          #[6, 15]
# print([1,2,3]+[4,5,6])            #[1, 2, 3, 4, 5, 6]
# print([2,4]*2)                    #[2, 4, 2, 4]

# d = {}
# print(type(d))                      #<class 'dict'>

# d = {"k1":10, "k2": 100}              #دیکشنری کلید دو نقطه ولیو (ارزش) بعدی همینطور
#d = {0=100, 1= 1000}                   #کلید میتونه عدد یا رشته باشه و نباید تکراری باشه 

# city -> id, name, pop, rain, age
# d = {"1010":{"name:":"Tehran", "pop":15, "rain":[20,30,40,20,55,12,11]}, "1020":{"name":"shiraz", "pop":4, "rain":[18,22,19,7,6,]}}
# print(d)

# g = {"a":100, "b":200, "c":300}
# for i in g:
#     print(g[i])    #ولیو های کلیدارو

# g = {"a":100, "b":200, "c":300}
# for k,v in g.items():
#     print(k, "->", v)
# a -> 100
# b -> 200
# c -> 300

#---------------------- set

# s = {1, 2, 3}        #کار مجوعه در ریاضی رو انجام میده
# for i in s:
#     print(i)

# a = {1, 2, 10, 20}
# b = {4, 5, 1, 2}
# print(a.union(b))              #{1, 2, 4, 5, 10, 20} اجتماع
# print(a.intersection(b))       #{1, 2} اشتراک
# print(a.difference(b))         # {10, 20} اونایی که توی ای هست توی بی نیست
# print(b.difference(a))           #{4, 5}  اونایی که توی بی هست توی ای نیست

#--------------------- tuple

t = (1, 2, 3, 4) #----->  t = 1,2,3,4
# print(type(t))       #<class 'tuple'>
# print(t[0])            #1
# for i in t:
#     print(i)          #1,2,3,4    
#ویژگی توپل اینه که نمیشه داده هاشو تغییر داد. اگه میخوایم داده ها دست نخورده باقی بمونن ازش استفاده میکنیم
# t = (10)   #int
# t = (10,) 
# t = ()           #tuple

#------------------------------------ تابع
# def power2(a):
#     return a**2
# print(power2(10))     #100

# def power2_3(a):
#     return a**2, a**3     #(100, 1000)
# print(power2_3(10))
# print(power2_3(10)[0])    #100  فقط جواب اولی رو میخوایم اینطوریه

# def f2 (l):
#     for i in l:
#         if i == 5:
#             return
#     return l
# print(f2([1,2,5,3,2]))     #none
# print(f2([1,2,3,2]))       #[1, 2, 3, 2]  چون پنج رو برداشتم

#------------------- class  #magic_method

# class Name1:                    #مرسومه کلاس رو با حروف بزرگ شروع کنیم
#     pass

# class Mostatil:
#     def __init__(self, a, b):
#         self.tool = a
#         self.arz = b
#     def area(self):
#         return self.tool*self.arz                       #magic_method
   
#---------------------
#Anaconda


#dknflskndf;ld
#tdghfj
#Codeyad practice sheet