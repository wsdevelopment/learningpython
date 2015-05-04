#This is a guide or tutorial for those wishing to begin learning the Python programming language. I will assume that you have no
#experience whatsoever. The guide is structured after Microsoft's Virtual Academy: Introduction to Programming with Python 
#video lessons. By the way, when typing something after a # in Python, it is a comment, and the computer doesn't read it.
#Use comments in your own code if you want to explain why or how you did something so someone else who reads it would understand.
#Note that there are many different flavors of Python, including IronPython, IPython,  PyPY, Canopy, etc. You will be learning
#CPython. This means that code from other flavors may not run on other interpreters. ex. IronPython won't run on a CPython
#interpreter. There aren't huge differences, just syntax and some commands that have other equivalencies.

#The first and most basic thing to learn in almost any language is how to display text on the screen. In Python, this is done
#using the print command, like so:
print("This command displays text on the screen")
#print is followed by a set of parenthesis and quotation marks inside. Anything between quotes is called a string.
#Double (") or Single (') quotes can be used, try to stick to one to develop good habits. The reason this exists is because,
#when you have something like:
#print('It's a very nice day'), the ' in it's closes the string early and the rest isn't recognized as part of the command.
#The same follows for double quotes if used in the middle of a double-quoted string. If both a single and double quote are
#needed in a print command, arrange it like so:
print('"A very nice day it was",' + " Washington's famous quote.")
#We used both single and double quotes in the string, however we joined them by using a +. This will be important in the future.

#As you've noticed, the two print commands written above have their own lines. You can affect this in a few different ways.
#Some basic things you can do is using the backslash (\). \n will create a new line, \t will create an indent. For example:
print("This shows an example of the \\n.\n")
#The backslash is a special character Python recognizes. The reason I typed \\n.\n, was because when you use a backslash,
#whatever follows (single character,) is a command. But what if you want to actually type a backslash? You type \\
#for the backslash to cancel out, leaving you only with the backslash. In the example above, the backslash canceled out the
#other backslash making it regular code, which was why \n appeared. I then typed a period and used the real, working \n.
#Everything that comes after the \n will be on a new line.
print("This code is on the first line of it's string, \nwhile this code is on the second, all while using one print command.")
#Next, is the \t command.
print("\tThe \\t command creates an indent in after where it is\t typed.\n")
#As you can see there, I once again canceled out the backslash with a backslash, having Python understand it's part of the string.
#This is useful, for example, if you want to type something like \news because it's part of a link or something, and this would
#happen:
print("Using backslash example \news.")
#You do this:
print("Using backslash example \\news.")
#Another way to create a multi-line string using on print command is using triple quotes. When using them, the string will
#come out exactly as you typed it. For example:
print("""This string is on the first line,
this on the second
and this on the third.
The way I type this in the code is how it will come
out in the program. This
will also work with triple single quotes.""")
#Keep in mind that as you learn ANY new information, practice a bit and experiment with it. Also, if you have questions,
#sometimes you won't have the answers and the easiest way to find out is to just try it. Experiment.

#Next, we'll learn about variables and inputs. Variables are used to store data within themselves so that it can be re-used later.
#For example, you can have:
age = "42"
print("I am " + age + " years old!")
#Make sure when you have a variable that has the value of a nuimber you want to use in A STRING, there are quotes around it,
#making it a string, otherwise it will cause errors.
#When making a variable, there are a few rules. First, your variable cannot start with a number. It cannot have spaces.
#There are some reserved words which you cannot use as a variable name because Python uses them for other things.
#Keep in mind that when making a variable that's two words, a good example is test_Var, capitalize the second part.
#Variables are also case-sensitive, so test_var is different than test_Var.

#Inputs ask the user to input a value for the variable. Shown below:
fav_President = input("Who is your favorite president?")
#When run, the code will ask who the user's favorite president is, and whatever is entered will be the value of the variable.
#You can then use the variable later on:
print("Your favorite president is " + fav_President + "!")
#Next we'll learn about functions. Run the code below.
firstName = input("What is your first name?\n")
firstName = firstName.upper()
lastName = input("What is your last name?\n")
lastName = lastName.upper()
print("Hello, " + firstName + " " + lastName +"!")
country = input("What country do you live in?\n")
country = country.upper()
print("Hello, " + firstName + " " + lastName + ", from " + country + ".\n")
#As you can see, whatever you input when questioned came out to be in all capitals in the print. This is because of the
#.upper() function attached to the variables. Look at the assigning of the country variable. First, I have an input attached,
#making whatever the user put's as his country the value of the country variable. Then, I say that the variable country
#is equal to country.upper(). This means that whatever the value of country is, it will have the .upper() function attached.
#As you may have guessed, the .upper() function makes everything capitalized. There are other simple functions.
#.upper(), .lower(), .capitalize(), and .swapcase(). .upper() makes everything uppercase, .lower() the opposite,
#.capitalize() will make the first character upper and the rest lower, and .swapcase() inverses upper to lower and vice versa.

#Now we'll quickly learn about counting in code.
testing_Num = "This is how many languages count."
print(testing_Num.find("how"))
#You will see that when run, the print returns 8. This is because, the function .find("x") will tell you the number of characters
#from the beginneing of the string to the first character of the entered value. This means, if I tell it to find the number of 
#characters before how, it will start at 0 with "T", and go up to "h" in how, making 8. Many programming languages count from 0
#and end on the first character of the value given. Note that if using a function with "." at the beginning, you need
#parens at the end, whether or not a value is entered between them.

#We will now learn a little about numbers.
length = 3
height = 5
area = length*height
message = "The answer is:"
print(message)
print(area)
print("\n")
#Analyze the code and guess what it would print. The reason you aren't able to do print(message + area) is because 
#area = length*height returns a numeric value, not a numeric string. The + connects two strings specifically. To fix this, do:
length = 3
height = 5
area = str(length*height)
message = "The answer is:"
print(message + area + ".\n")
#Here, you can see that originally, area = length*height had an integer value and therefore couldn't be put into a string.
#When we do area = str(length*height), the calculations still happens, but Python knows that the returned integer
#should be a string. str is a valuable function that will change an integer to a string, and the same can be done for
#something like this:
age = "42"
#^ 42 is a string
#child_age = age/2 <<< this code produces an error, as 42 is a string and can't be used in calculations.
age = "42"
child_Age = int(age)/2
print(age + " is the age of the parent, " + str(child_Age) + " is the age of the child, making the parent\n " + str(child_Age) + " when the child was birthed.")
#Here you can see the manipulations of the str and int functons, where str makes an integer into a string, and int makes
#a string into an integer.
#Another quick thing about variables is that you can reassign the value. Say we use the age variable again like so:
age = "56"
print("I'm " + age + " years old!")
#As you can see, the two lines of code above didn't affect the code when we talked about the str and int functions.
#In that way, the value of variablescan be reassigned.

#There is also another way to display integer values as part of a string using placeholders.
#Another way to show is to have a placeholder. Don't know entire differences between float/decimal (%f & %d) yet,
#float seems to be attachable to dec, dec seems to be attachable to whole. 
area = 7
print("The area of the square is %f" % area)
#^Displays the number given with the default %f 6 decimals after.
print("The area of the square is %.0f" % area)
#^Displays no decimals as the .0 specifies none.
print("The area of the square is %.02f" % area)
#^Displays 7.00, with two decimals after as specified.
print("The area of the square is %03d" % area)
#^Displays 007, having 3 total "whole" digits.
print("The area of the square is %3d" % area)
#^Displays 7 with 3 total spaces before it, including space given in string.. The area of the square is   7.
print("My favorite number is %d!" % 42)
#Putting %10d will make the number placed after 10 spaces, useful for money formatting and such.
print("The cost of a wheelbarrow is %25d" % 45)
print("This is a different length string than the other %5d" % 65)
#This displays the 45 and 65 in the same column though the strings are of different lengths.

#Next, let's move on to operations. Note that Order of Operations applies, use PEMDAS.
print("5+5= " + str(5+5)) #<Addition
print("15-5= " + str(15-5)) #<Subtraction
print("5*3= " + str(15*3)) #<Multiplication
print("15/3= " + str(15/3)) #<Division
print("3**2= " + str(3**2)) #<Exponents
print("43%5= " + str(43%5)) #<Modulo
#Modulo is available in most if not all languages and returns a remainder. For example, 43 divided by 5 is 8 with remainder of 3.
