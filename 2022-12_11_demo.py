#list comprehension
#expression for variable in sequence (optional predicate)

my_list= []
for i in range(1, 10, 2):
    my_list.append(i**2)

my_list2= [i**2 for i in range(1, 10, 2)]

#print(my_list)
#print(my_list2)

odd_square = [] 
for x in range(1, 11): 
    if x % 2 == 1: 
        odd_square.append(x**2) 

odd_square2= [x**2 for x in range(1,11) if x %2 ==1]



#print(odd_square) 
#print(odd_square2)


#for all numbers inclusive 1-50 give a list of all the prime numbers
#prime= [for num, num2 in range(2,51)]

prime= []
for num in range(2, 51):
    if (num % 2 == 1) and (num % 3 == 1):
        prime.append(num)
#print(prime)

    
prime=[]
for i in range(1,51):
    for j in range(2,i):
        if i%j != 0:
            break
        else:
            prime.append(i)
#print(prime)

#prime= [i for i in range(1,51) if (i%j == 0 for j in range(2, i))]
#print(prime)

for x in range(1,51):
    for y in range(2, x):
        if (x % y
        ) == 0:
            prime.append(i)

#print(prime)




prime= [x for x in range(1, 50) if all(x % y != 0 for y in range(2, x))]
#print(prime)

evens= []
def even():
    for x in range(1,51):
        if x % 2 == 0:
            evens.append(x)

#print(even())
#print(evens)

evens2= [x for x in range(1, 51) if x  % 2 == 0]
#print(evens2)


letters= ['a', 'b', 'c', 'd']
dict= {}

#dict={1:'a', 2:'b', 3:'c', 4: 'd'}

n= 1
for i in letters:
    dict[i]= n
    n += 1

#print(dict)



add_num = {}
for num in range (1,11):
    add_num[num]= num + num

#print(add_num)


#key: value for variable in iterable
add_num2= {i: i+i for i in letters}
#print(add_num2)

#add_num3:= {num: num+num for num in range(1,11)}

dict2 = {number + 1: letter for number, letter in enumerate(letters)}
print(dict2)

help(str)