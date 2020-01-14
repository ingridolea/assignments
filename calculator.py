def suma(a,b):
	return a+b

def resta(a,b):
	return a-b

def mult(a,b):
	return a*b

def div(a,b):
	return a/b

def square(a):
	return a**2

def cubo(a):
	return a**3

def square_n_times(number,n):
	return square(number)**n

print("I'm going use the calculator functions to multiply 5 and 6")
x = mult(5,6)
print(x)

print("I'm going use the weird defined function square_n_times with values 9 and 6")
x = square_n_times(9,6)
print(x)


