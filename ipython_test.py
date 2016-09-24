#test
'''
test2
'''

# import pandas as pd

print "Hello {0}!".format('Antoine')

for i in xrange(10):
	if i % 2 != 0:
		print("{0} is odd".format(i))
	else:
		print("{0} is even".format(i))
    
print("Looks like everything's working...")

def summation(a, b):
    return a + b
    
print summation(1,2)