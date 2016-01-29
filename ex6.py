def add(a,b):
    return a+b

def subtract(a,b):
	return a-b

def divide(a,b):
	return a/b

def multiply(a,b):
	return a*b

print "enter any two numbers"
a=int(raw_input())
b=int(raw_input())

print "a * b = %d" %(multiply(a,b))
print "a / b = %d" %(divide(a,float(b)))
print "a - b = %d" %(subtract(a,b))
print "a + b = %d" %(add(a,b))
