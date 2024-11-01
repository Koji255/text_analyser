import methods

"""will be some path in somefile varriable"""
somefile = "" 
text = ""

try:
    with open(somefile) as file:
        text = [word for word in file]

except ValueError:
    raise ValueError("Value Error")

else:
    raise NameError("Something went wrong")



