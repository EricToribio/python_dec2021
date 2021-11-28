num1 = 42#variable decleration equal to a int
num2 = 2.3#variable decleration equal to a float
boolean = True#variable decleration equal to the boolean true
string = 'Hello World'#variable decleration equal to a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#Dictionary
fruit = ('blueberry', 'strawberry', 'banana')#tuple
print(type(fruit))#type check
print(pizza_toppings[1])#print list @index 1
pizza_toppings.append('Mushrooms') #add to list
print(person['name'])#print the value of the key name in the dic person
person['name'] = 'George' #change dit key name to = George
person['eye_color'] = 'blue'#change  dic key of eye_color to = blue
print(fruit[2]) #print tuple @ index 2
print(pizza_toppings)#print list
if num1 > 45:# if var is greater than int 45
    print("It's greater")#print string
else: #else statement
    print("It's lower")#print String


if len(string) < 5:#if length check
    print("It's a short word!")#print string
elif len(string) > 15:#else if length check
    print("It's a long word!")#print string
else:#else 
    print("Just right!")#print string

for x in range(5):#For loop where loop stops at 5
    print(x)# print value of var
for x in range(2,5):#for loop x =2 and loop stops at 5
    print(x)# will print 2,3,4
for x in range(2,10,3):#for loop x =2 and loop stops at 10 and increments by 3
    print(x)#will print 2 ,5,8
x = 0#initialize var to a int
while(x < 5):#while loop checking if var is less than 5
    print(x)#print var
    x += 1#change x to current value of x + 1

pizza_toppings.pop()#deletes last value in the list
pizza_toppings.pop(1)#deletes value in the list at index 1

print(person)#print the dic person
person.pop('eye_color')#int he person dict delete the key and value of eye color
print(person)#print the dic person

for topping in pizza_toppings:#for loop looping through list
    if topping == 'Pepperoni': #if the value of Peperoni is found in the list do next block of code
        continue#continue loop
    print('After 1st if statement')#print string
    if topping == 'Olives':#if the value of Olive is found in the list do the next block of code
        break#break out of the loop

def print_hello_ten_times():#initialize func
    for num in range(10):#for loop num = 10
        print('Hello')#print string

print_hello_ten_times()#function call

def print_hello_x_times(x):#initialize a func with a param of x
    for num in range(x):#for loop in range of x
        print('Hello')#print string

print_hello_x_times(4)#func call with param of 4

def print_hello_x_or_ten_times(x = 10):#initialize func with a param of x with a default value of 10
    for num in range(x):#for loop that stops at x
        print('Hello')#print string

print_hello_x_or_ten_times()#func call 
print_hello_x_or_ten_times(4)#func call with a param of 4


"""
Bonus section
"""

# print(num3) #err no var named num3
# num3 = 72 #set var = to a int
# fruit[0] = 'cranberry' # err fruit is a tuple cant be change
# print(person['favorite_team']) # error no key in person of favorite team
# print(pizza_toppings[7]) #err out of scope
#   print(boolean) #print True
# fruit.append('raspberry') #err tuple has no func of tuple
# fruit.pop(1) #err tuple has no pop func