numbers= [1, 2, 3, 4]

#print(globals())
#print(globals()['numbers'])
#globals()['numbers2']= [10, 20, 30 , 40, 50]
#print(globals()['numbers2'])

x = 10 
def func():
    global x
    x=40
    print(locals())
    print(x)

#print(x)
#print(func())


#print(x)
#print(func())
#print(x)
#print(locals()['x'])
#print(globals()['x'])


#Local, Enclosing, Global, Built-Ins
def outer(msg): #enclosing
    lang= 'Python'
    #print(locals())
    def inner(): #enclosed
        #print(locals())
        print(lang, msg, x)
    print(locals())
    inner()

#outer('is fun!!!')

def outer1(msg): #enclosing
    lang= 'Python'
    #print(locals())
    def inner1(): #enclosed
        #print(locals())
        print(lang, msg, x)
    #print(locals())
    return inner1

closure1= outer1('is fun!!!')
#print(globals())
#del outer1
#print(globals())
#closure1()

#print(inner1())

#want a closure
#that takes in two numbers
#and sums them 

def sum(num1):
    def sum_total(num2):
        print(num1+num2)
    return sum_total(10)

total= sum(5)
#print(globals())
#total(100)
###sum(5)(2)
print(total)

def make_multiplier_of(n):
    def multiply(k):
        return k*n
    return multiply

multiplier3= make_multiplier_of(3)
print(multiplier3(5))


#############################################
#############################################

#things we need to be considered a Closure function 
#nested function
#the nested function needs to access at least
#one non-local variable
#return nested function WITHOUT calling it 


#############################################
#############################################

def decorator1(func):
    def wrapper():
        print("I am running before the function call")
        func()
        print("I am running after the function call")
    return wrapper

@decorator1
def i_am_func():
    print("I am the function")
#use_decorator= decorator1(i_am_func)
#use_decorator()
#i_am_func()

def run_n_times(n):
    def dec(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return dec

#def say_hello():
    #print('hello')
                       #dec
#say_hello = run_n_times(5)(say_hello)

def dec(*args):
    #print(type(args))
    #print(args)
    n= args[0]
    def wrapper():
        for _ in range(n):
            func()
    return wrapper
    

@dec(7)
def say_hello():
    print('hello')

say_hello()
#def say_hello():
    #print('hello')

#say_hello = dec(say_hello, 5)
#say_hello()
   


#say_hello = dec(say_hello, 5)
#say_hello()

#def add(num1, num2):
    #print(num1 + num2)

def add3(num1, num2, num3):
    print(num + num2 + num3)

#*args (or *namewewant) is for non-keyword variable assignments
#**kwargs (**namewewant) if for keyword variable assignments

def add(*numbers):
    total= 0
    for num in numbers:
        total += num
    return total


def decorator(*args, **kwargs):
    print("Inside decorator")
     
    def inner(func):
         
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])
         
        func()
         
    # returning inner function   
    return inner
 
#@decorator(like = "geeksforgeeks")
#def my_func():
    #print("Inside actual function")

#my_func()