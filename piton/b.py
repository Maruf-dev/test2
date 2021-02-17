from random import randint
for i in (5):
    print(randint(1,25))






"""import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()!@#$%*,"
all = lower + upper + numbers + symbols
lenth = 16 
password = "".join(random.sample(all,lenth))

print(password)"""


"""def total_length(ss):
    total = 0
    for string in ss:
        total += len(string)
    return total
       
print(total_length(['foo', 'bar']))
print(total_length([]))
print(total_length(['balloons']))
print(total_length(["", '', "", '']))
"""

"""n1 = int(input("enter a number :"))
n2 = int(input("enter another number:"))
n3 = int(input("enter third number:"))
sum = n1 + n2 + n3
print(f' {n1} + {n2} + {n3} = {sum}')
"""

"""def too_long(s):
    lenth = len(s)
    if lenth > 140:
        return True
    else : 
         return False  
print(too_long("I'm a short string!"))
print(too_long("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."))"""
"""def locate_all(string, substring):
    matches = []
    index = 0
    
    while index < len(string):
        if string [index : index + len(substring)] == substring:
           matches.append(index)
           index += len(substring)
        else:
             index +=1
    return matches
print(locate_all('cookbook', 'ook'))
print(locate_all('all your bass are belong to us', 'base'))"""




"""def locate_first(string, substring):
    index = 0
    while index < len(string):
         
        if string[index : index + len(substring)] == substring :
           return index 
        else:
             index += 1
    return -1          
print(locate_first('cookbook', 'ook'))
print(locate_first('all your bass are belong to us', 'base'))"""