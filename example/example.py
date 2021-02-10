# comments are indicate with hash
#numbers are whole numbers it contains 0,1,2,3....
n=12
n=12.5
print('numbers are {} \n'.format(n))
#here we can understand python is dynamic data type
#data operators
# + indicates addition
# - indicates subtraction
# * mulitiplication
# / division
# % mod operator
# ** power

#*****************strings***********************

#strings are immutable
#and separed by silcing
name="hello world"
#letters can be access by indexing
print("the first letter of string is {}\n".format(name[0]))
#27-01-2020
x1=2
x2=2
print(id(x1))
print(id(x2))
my_iterable=[123,124,125]
for item_name in my_iterable:
	print("variable is {}\n".format(item_name))
#for loop
mylist=[1,2,3,45,5,5,6]
for listvariable in mylist:
	print(listvariable)
#check even or odd
for num in mylist:
	if num % 2 == 0:
		print("even")
	else:
		print("odd")
#list sumation
list_sum=0
for elements in mylist:
	list_sum+=elements
print('sum of{}'.format(list_sum))

#list with sets

mylist=[(1,2),(2,3),(3,4),(4,5)]

for(a,b) in mylist:
	print(a)
	print(b)

#def key word used for create a function
#def name_of_function(): snake casing (all lowercase with underscore)
#''' docstring explains function,''' 
def name_of_function():
	''' printing hello'''
	print("calling function\n")
	print("hello")
name_of_function()

#passing arugument name here 

def name_of_function(name="mohan"):
	'''arugument passing'''
	print("hello "+name)

name_of_function("leelamohan")
name_of_function()

work_hours=[('abby',1000),('billy',2000),('cassie',800)]

def employee_check(work_hours):
	current_max=0
	employee=""
	for name,hours in work_hours:
		if(current_max<hours):
			current_max=hours
			employee=name
	return (employee,current_max)
bestemployee=employee_check(work_hours)
print(bestemployee)	
employee_of_the_month,no_of_hours=employee_check(work_hours)
print(employee_of_the_month)
print(no_of_hours)
#multiple functions
example=[1,2,3,4,5,6,7,8]
from random import shuffle
shuffle(example)
print(example)

#player guess
def player_guess():
	guess=''
	while guess not in ['0','1','2']:
		guess=input("pick number : 0,1,2\n")
	return int(guess)
player_guess()


employee_check(work_hours)























































































































































