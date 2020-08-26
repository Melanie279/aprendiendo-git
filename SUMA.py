def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
	if(b==0):
		return 0
	else:
    	return a/b
a=int(input("Ingrese primer numero:"))
b=int(input("Ingrese segundo numero:"))
print (suma(a,b))
print (resta(a,b))
print (multi(a,b))
print (div(a,b))
