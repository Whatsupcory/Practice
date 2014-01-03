# this one is like your scripts with argv
def print_two(*args):  # def - tells python we want to make a function, then give the function a name (says what it does), *argv like argv parameter but for functions (has to be in side ())
	arg1, arg2 = args   # become attached to this name. This line unpacks the arguments.
	print "arg1: %r, arg2: %r" % (arg1, arg2) # prints out the arguments. 

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r"  % arg1

# this one takes no argument
def print_none():
	print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()