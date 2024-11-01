
"""will be some path in somefile varriable"""
somefile = "" 
text = ""

try:
    with open(somefile) as file:
        text = [word for word in file]

except:
    raise ValueError("Something went wrong")