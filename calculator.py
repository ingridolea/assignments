#Defining sum
def suma(a,b):
	return a+b

#Defining substraction
def resta(a,b):
	return a-b

#Defining multiplication
def mult(a,b):
	return a*b

#Defining division
def div(a,b):
	return a/b

#Defining special "square" function
def square(a):
	return a**2

#Defining special "cube" function
def cubo(a):
	return a**3

#Defining special "square_n_times" function
def square_n_times(number,n):
	return square(number)**n

#Trying in the console
print("I'm going use the calculator functions to multiply 5 and 6")
x = mult(5,6)
print(x)

#Trying square n times in the console
print("I'm going use the weird defined function square_n_times with values 9 and 6")
x = square_n_times(9,6)
print(x)


