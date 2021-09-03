from coloristic import *
printc( red("Red text") )
printc( "If you add " + red("red") + " to " + blue("blue") + ", you get " + purple("purple") )

# Print a line in a random colour
printc( randcol("This is a random colour") )

# Print each word in a random colour
mytext = "This is a random piece of text which I want to print in random colours"
mytext = mytext.split(" ")
for word in mytext:
    printc(randcol(word), end=" ")
