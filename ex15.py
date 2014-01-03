from sys import argv

script, filename = argv  # Lines 1-3 Get a filename

txt = open(filename) # new command to 'open' a file. "pydoc open" for more information. 

print "Here's your file %r:" % filename # print a new line
print txt.read()  # call a function on a txt. Give it a command (dot), the name of the command, and parameters.

print "Type the filename again:"
file_again = raw_input("> ")    # I need to stop writing raw_import, raw_imput.

txt_again = open(file_again)

print txt_again.read()