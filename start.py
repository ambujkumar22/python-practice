from math import * #this line of code allow us to import some maths modules to use in our code
print ("hello awesome man!")  #saying hello world in python.
print ("  /|")
print (" / |")
print ("/__|")

#using variables
name = "Ambuj" #different variable names can be separated with a underscore.
age = "22"
print(name +" started Python course at the age of "+ age) #variables are stated as they are in javascript.

name = "Mr. Kumar"
print(name +" started Python course at the age of "+ age) #variable's value can be changed at any instant of time.

animal = "Giraffe"
print(animal.upper()) #converts the string into upper case (same for lower case)
print(animal.isupper()) #checks the code is in upper case or not and returns a boolean value (same for lower case)
print(animal.upper().isupper()) #converts the string and returns a boolean value. (same for lower case)
print(len(animal)) #shows the length of the string.
print(animal[0]) #gives the alphabet at the specific location of the string.
print(animal.index("f")) #gives the alphabet exactly at the index location entered.
print(animal.replace("Giraffe","Elephant")) #used to replace the string value.
print(3 +5.5) #python is able to handle basic arithematic operations just fine.

number = 5
print(str(number) +" hours left to study.") #converting a number into string can help to print out the number with concatenation.
#using functions to take mathematical terms to heights is print(abs(number)) for absolute number 
#taking print(pow(3,4)) which means that 3^4. taking print(max(3,8)) gives the max. no. out of the array(sam eas min. number)
#taking print(round(3.45)) will round off the number.

print(sqrt(144)) #giving the square root of 144.
u_name = input("Enter your name: ") #the input is used to take input from the user.
u_age = input("Enter your age: ")
print("Welcome "+ u_name + "! You are "+ u_age +" years old.")

#adding numbers by taking inout from the user 
num1 = input("Enter the first number for multiplication: ") #by default the numbers taken from the users are converted into string
num2 = input("Enter the second number for multiplication: ")
mul = float(num1) * float(num2) #the numbers taken from the user are converted into floating numbers hwich means it can take decimal values.
print("Your answer is "+ str(mul))

#creating madlibs
color = input("Enter one colour: ")
flower = input("Enter one flower name: ")
celebrity = input("Enter one Celebrity name: ")

print("Roses are "+ color)
print(flower +" are blue")
print("I love "+ celebrity)

#lists
friends = ["Rishabh", "Suhail", "Suhail", "Dharmender"] #in this list python can automatically identifies the array 
print(friends[0]) #by index values the list can be accessed 
evennumbers = [2,4,6,8,10]
friends.sort() #it sorts the list in alphabetical order and numbers in ascending order 
friends.extend(evennumbers) #extend function adds two or more arrays together and in this case the two lists are merged
friends.append("Akash") #append function adds anohter value to the list friends
friends.insert(2,"Divanshu") #adds one value to the list in between the existing values and it takes two parameters
evennumbers.remove(10) #remove removes the entered value from the list.
evennumbers.clear() #clear function clears the whole list
friends2 = friends.copy() #copy function just copies the list.

print(friends) 
print(friends.count("Suhail")) #count tells the total number of entered values inside the list
print(evennumbers)
print(friends2)
 #Tupl(the tuples are similar to lists but the only difference is that you cannot change the value of a tuple)
coordinate = (3, 4)
print(coordinate[1])

def func(name, age): #defining a function and name and age are 2 parameters
    print("Hello "+ name + ", you are "+ str(age)) #indentation is important

func("Ambuj",22) #calling a function and passing the prameters

def cube_of_num(num):
    return num*num*num #return keyword basically returns the process and breaks the function and comes out of it so, after return nothing will be printed or executed.

print(cube_of_num(3)) #cube_of_num is a function which is called inside a print function and assigned a value 3
result = cube_of_num(4) #the result is a variable which contains the value which is equated by the cube_of_num function
print(result) 

male = True
tall = True
if male and tall: #if else condition 
    print("You are male and also tall.")
elif male and not(tall): #for negaition python uses "not" operator
    print("You are male but not tall.")
elif not(male) and tall:
    print("You are not male but tall.")
else:
    print("You are not male neither tall.")

def max_num(num1,num2,num3): #creating a maximum number finder
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3,32,100)) #finding the maximum number from the input numbers

#building advance calculator
number1 = float(input("Enter first number: ")) #float wwill automatically convert the value enters by the user to a number which is easier for the program to read
operator = input("Enter operator: ")
number2 = float(input("Enter second number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "%":
    print(number1 % number2)
else:
    print("invalid operator")

#dictionary
months = { #dictionary usually uses key value pairs where the keys should be always unique.
    1: "January", #in here the 1 is a key and january is the value pair.
    2: "February",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "June",
    7: "Jul",
    8: "Aug",
    9: "Sept",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}
print(months[1]) #tis is one way to call a dictionary and by this means we call the key to access the value.
print(months.get(13,"not valid input or month")) #by get method we can assign a new value to the key.

#while loops
i = 1
while i <= 10:  #runs the loop upto 10
    print(i)
    i += 1 #python doen't uses ++ operator.
print("loop ends")

#for loop 
people = ["ramesh","suresh", "raju"] #a list 
for pep in range(len(people)): #in for loop the pep is a variable which stores the value of range which in this case is 0. len(people) defines the total no. of length of the list.
    print(people[pep])

#use of for loop
def power_of_num(base,power): #function to calculate the power to the number.
    number = 1
    for store in range(power):
        number *= base #this means number = number * base
    return number
print(power_of_num(3,9))

#2-Dimentional lists and nested for loops
grid = [ #it is a 2Dimensional list which shows numbers from 1 to 10.
    [1,2,3],
    [4,5,6],
    [7,8,9,10]
]
for row in grid:
    print(grid[0][2]) #it prints the number which is in 0'th row and 2'nd column
    for col in row:
        print(col) #it prints the numbers which are from 1 to 10

#making a translator
def translator(phase):
    translation = ""
    for letter in phase:
        if letter.lower() in "aeiou": #it checks that the vowels are present in the word or not.
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translator(input("Enter the word or sentence to translate: ")))