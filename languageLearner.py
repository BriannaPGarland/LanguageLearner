#Brianna Garland 
#CPE 551 Final Project
#Language Learner 
#---------------------------------
#goal, maybe have a class for each language so I can do java.forLoop 
#and itll print out a for loop in java
#---------------------------------
#self,forLoop,ifState, whileLoop, variable,comment, dataType, arrays, switchStat, mainMethod, functionDef, classDef

#imports to be able to have options on the ommand line run 
import argparse
from optparse import OptionParser

#different mode flags 
userFriendlyMode = False
quickMode = False

quick = ""
parser= OptionParser ()
parser.set_defaults(quick=True)

#adding the different options to be able to run on the command line 
parser.add_option("-q", "--quick", dest = quick, help = "This is the SWE friendly interface that is structured for quick commandline runs", metavar="QUICK")
parser.add_option("-a", "--auto", action = "store_true", help = "This is the new user friendly mode that individually prompts users for inputs ", default = False)
#parsing the arguments 
(options, args)=parser.parse_args()

#logic to be able to tell what to do with the program 
if options.auto:
    userFriendlyMode = True
    quickMode = False 
elif options.quick:
    quickMode = True 
    userFriendlyMode = False

    #Logic to separate out what the user inputed on the command line for user input 
    usrInput = str(options)
    usrInput = usrInput.split('\'')
    usrInput = usrInput[5]
    usrInput = usrInput.split(',')

    language = usrInput[0].lower()
    structure = usrInput[1].lower()

########################### Java ###########################    
def javaForLoop():
    return ("for (statement 1; statement 2; statement 3) {\n\t// code block to be executed\n}\n\nor\n\nfor (int i = 0; i < 5; i++) {\n\tSystem.out.println(i);\n}")

def javaifStat():
    return("if (condition) {\n\t// block of code to be executed if the condition is true\n}\n\nor\n\nif (condition) {\n\t// block of code to be executed if the condition is true\n} else {\n\t// block of code to be executed if the condition is false\n}")

def javaWhileLoop():
    return("//Normal While Loop: ","while (condition) {\n\t// code block to be executed\n}\n",
    "do {\n\t// code block to be executed\n}\nwhile (condition);")

def javaVariables():
    return "type variableName = value;\nint x = 5, y = 6, z = 50;\nfinal int myNum = 15;""//Do While Loop: "

def javaComments():
     return("// This is a comment")    

def javaDataTypes():
     return("int myNum = 5;             	  // Integer (whole number)\nfloat myFloatNum = 5.99f;  	  // Floating point number\nchar myLetter = 'D';      	  // Character\nboolean myBool = true;      	 // Boolean\nString myText = /'Hello/'; 	 // String") 

def javaArrays():
     return("String[] cars;\n\nString[] cars = {\"Volvo\", \"BMW\", \"Ford\", \"Mazda\"};")

def javaSwitchStat():
     return("switch(expression) {\n\tcase x:\n\t\t// code block\n\t\tbreak;\tncase y:\n\t\t// code block\n\t\tbreak;\n\tdefault:\n\t\t// code block\n}")
 
def javaPrintStat():
    return("System.out.println(\"Hello World\");")

def javaMain():
    return("public static void main(String[] args)")

def javaFunctions():
    return("static void myMethod() {\n\t// code to be executed\n}")

def javaClasses():
    return("public class Main {\n\tint x = 5;\n}")

java = {
    "for loop" : javaForLoop,
    "if statement" : javaifStat,
    "while loop": javaWhileLoop,
    "variable": javaVariables,
    "comment": javaComments,
    "data type": javaDataTypes,
    "array": javaArrays,
    "switch statement": javaSwitchStat,
    "print statement": javaPrintStat,
    "main": javaMain,
    "function": javaFunctions,
    "class": javaClasses
}  

#This is a function to output all the sytnax for a given language 
def allJava():
    for x in structures[:-1]: 
        print("--------------------------------")
        print(x,"\n")
        print(java.get(x, default)())
        print("--------------------------------")

########################### Javascript ###########################    
def jsForLoop():
    return ("for (statement 1; statement 2; statement 3) {\n\t// code block to be executed\n}",
    "\nor\n",
    "for (key in object) {\n\t// code block to be executed\n}", 
    "\nor\n",
    "for (variable of iterable) {\n\t// code block to be executed\n}")

def jsifStat():
    return("if (condition) {\n\t// block of code to be executed if the condition is true\n}",
    "\nor\n",
    "if (condition) {\n\t// block of code to be executed if the condition is true\n} else {\n\t// block of code to be executed if the condition is false\n}")

def jsWhileLoop():
    return("//Normal While Loop: ","while (condition) {\n\t// code block to be executed\n}\n",
    "do {\n\t// code block to be executed\n}\nwhile (condition);")

def jsVariables():
    return("Var: \nvar x = 5;\nvar y = 6;\n\n",
    "Let (Can be redeclared): \nlet x = \"John Doe\";\nlet x = 6;\n\n",
    "Const (Can NOT be redeclared): \nconst PI = 3.141592653589793;")

def jsComments():
    return("// This is a comment")    

def jsDataTypes():
    return("let length = 16;                               // Number\nlet lastName = \"Johnson\";                      // String\nlet x = {firstName:\"John\", lastName:\"Doe\"};    // Object")

def jsArrays():
    return "const array_name = [item1, item2, ...]; "

def jsSwitchStat():
    return("switch(expression) {\n\tcase x:\n\t\t// code block\n\t\tbreak;\tncase y:\n\t\t// code block\n\t\tbreak;\n\tdefault:\n\t\t// code block\n}")

def jsPrintStat():
    return ("console.log()")

def jsMain():
    return "Javascript does not have a main function "

def jsFunctions():
    return("function name(parameter1, parameter2, parameter3) {\n\t// code to be executed\n}")

def jsClasses():
    return("class Car {\n\tconstructor(name, year) {\n\t\tthis.name = name;\n\t\tthis.year = year;\n\t}\n}")

js = {
    "for loop" : jsForLoop,
    "if statement" : jsifStat,
    "while loop": jsWhileLoop,
    "variable": jsVariables,
    "comment": jsComments,
    "data type": jsDataTypes,
    "array": jsArrays,
    "switch statement": jsSwitchStat,
    "print statement": jsPrintStat,
    "main": jsMain,
    "function": jsFunctions,
    "class": jsClasses
}     
   
#This is a function to output all the sytnax for a given language 
def allJs():
    for x in structures[:-1]: 
        print("--------------------------------")
        print(x,"\n")
        print(js.get(x, default)())
        print("--------------------------------")

########################### Python ###########################    
def pyForLoop():
   return ("for x in \"banana\":\n\tprint(x)","\n\nCan either use: In range() or in arrayName")

def pyifStat():
    return("if b > a:\n\tprint(\"b is greater than a\")\nelif a == b:\n\tprint(\"a and b are equal\")\nelse:\n\tprint(\"a is greater than b\")")

def pyWhileLoop():
    return("while i < 6:\n\tprint(i)\n\ti += 1")

def pyVariables():
    return("x = 4       # x is of type int\n\nx = \"Sally\" # x is now of type str")

def pyComments():
    return("# This is a comment")    

def pyDataTypes():
    return("Text Type:		str\nNumeric Types:	int, float, complex\nSequence Types:	list, tuple, range\nMapping Type:	dict\nSet Types:		set, frozenset\nBoolean Type:		bool\nBinary Types:		bytes, bytearray, memoryview") 

def pyArrays():
    return("mylist = [\"apple\", \"banana\", \"cherry\"]")

def pySwitchStat():
     return("Python does not have switch statements in the same sense that other languages do\n However they do have dictionaries that function in a similar way. \nHere is the syntax for a python dictionary:\n",
     "thisdict = {\n\t\"brand\": \"Ford\",\n\t\"model\": \"Mustang\",\n\t\"year\": 1964\n}")

def pyPrintStat():
    return("print(\“String to print\”)")

def pyMain():
    return("Python is an interpreted language so it runs in the order it is coded and does not have a built in main() function ")

def pyFunctions():
    return("Def functionName(param1,param2, etc)\n\t#Code to be executed within the function \n#End of the scope of a function is the un-indentation of the next line")

def pyClasses():
     print("class MyClass:\n\tx = 5")

py = {
    "for loop" : pyForLoop,
    "if statement" : pyifStat,
    "while loop": pyWhileLoop,
    "variable": pyVariables,
    "comment": pyComments,
    "data type": pyDataTypes,
    "array": pyArrays,
    "switch statement": pySwitchStat,
    "print statement": pyPrintStat,
    "main": pyMain,
    "function": pyFunctions,
    "class": pyClasses
}     

   
#This is a function to output all the sytnax for a given language 
def allPython():
    for x in structures[:-1]: 
        print("--------------------------------")
        print(x,"\n")
        print(py.get(x, default)())
        print("--------------------------------")

########################### C++ ###########################    
def cppForLoop():
   return("for (statement 1; statement 2; statement 3) {\n\t// code block to be executed\n}")

def cppifStat():
    return("if (condition1) {\n\t// block of code to be executed if condition1 is true\n} else if (condition2) {\n\t// block of code to be executed if the condition1 is false and condition2 is true\n} else {\n\t// block of code to be executed if the condition1 is false and condition2 is false\n}")

def cppWhileLoop():
    return("while (condition) {\n\t// code block to be executed\n}")

def cppVariables():
    return("type variableName = value;")

def cppComments():
    return("// This is a comment")    

def cppDataTypes():
    return("int myNum = 5;             	  // Integer (whole number)\nfloat myFloatNum = 5.99;   	  // Floating point number\ndouble myDoubleNum = 9.98;  // Floating point number\nchar myLetter = 'D';       	  // Character\nbool myBoolean = true;   	  // Boolean\nstring myText = \"Hello\";   	  // String") 

def cppArrays():
    return("string cars[4] = {\"Volvo\", \"BMW\", \"Ford\", \"Mazda\"};\n\nstring cars[4];")

def cppSwitchStat():
    return("switch(expression) {\n\tcase x:\n\t\t// code block\n\t\tbreak;\n\tcase y:\n\t\t// code block\n\t\tbreak;\n\tdefault:\n\t// code block\n}")

def cppPrintStat():
    return("#include <iostream>\nstd::cout << \"Hello World!\";\n\nOr \n\n#include <iostream>\nusing namespace std;\n\ncout << \"Hello World!\" << endl;")

def cppMain():
    return("int main() {\n\tcout << \"Hello World!\";\n\treturn 0;\n}")

def cppFunctions():
    return("void myFunction() {\n\t// code to be executed\n}")

def cppClasses():
    return("class MyClass {       // The class\n\tpublic:             // Access specifier\n\t\tint myNum;        // Attribute (int variable)\n\t\tstring myString;  // Attribute (string variable)\n};")

cpp = {
    "for loop" : cppForLoop,
    "if statement" : cppifStat,
    "while loop": cppWhileLoop,
    "variable": cppVariables,
    "comment": cppComments,
    "data type": cppDataTypes,
    "array": cppArrays,
    "switch statement": cppSwitchStat,
    "print statement": cppPrintStat,
    "main": cppMain,
    "function": cppFunctions,
    "class": cppClasses
}     
   
#This is a function to output all the sytnax for a given language 
def allCpp():
    for x in structures[:-1]: 
        print("--------------------------------")
        print(x,"\n")
        print(cpp.get(x, default)())
        print("--------------------------------")

#######################################################
def default():
    print("Sorry, there was an error please try running the program again")
#######################################################

#Compatible languages and coding structures 
langs=[
    "python",
    "java",
    "javascript",
    "java script",
    "js"
    "c++",
    "cpp"]
structures=[
    "for loop", 
    "if statement",
    "while loop",
    "variable",
    "comment",
    "data type",
    "array",
    "switch statement",
    "print statement",
    "function",
    "main",
    "class",
    "all"]


def userFriendlyRun():
    #User Input 
    language = input("Please enter the langauge you would like or \"help\" for the help screen\n").lower()
    while language not in langs:
        if language =="help": 
            print("\nYou have asked for the help screen. Below you will see a list of all of the programming languages this program includes: ")
            print(langs,"\n")
            language = input("Now that you have seen the help screen, please enter the langauge you would like.\n").lower()
        else:
            language = input("Sorry that is not a compatible langauge, please enter a different langauge you would like\n").lower()

    structure = input("Please enter the code structure you would like to see or \"help\" for the help screen\n").lower()
    while structure not in structures:
        if structure =="help": 
            print("\nYou have asked for the help screen. Below you will see a list of all of the code structures this program includes: ")
            print(structures,"\n")
            structure = input("Now that you have seen the help screen, please enter the code structure you would like to see.\n").lower()
        else:
            structure = input("Sorry that is not a compatible code structure, please enter a different langauge you would like to see\n").lower()
    return(language,structure)

def quickRun(language,structure):
#User input was entered on the commandline this is a catch if they did not have the correct user input 
    while language not in langs:
        if language =="help": 
            print("\nYou have asked for the help screen. Below you will see a list of all of the programming languages this program includes: ")
            print(langs,"\n")
            language = input("Now that you have seen the help screen, please enter the langauge you would like.\n").lower()
        else:
            language = input("Sorry that is not a compatible langauge, please enter a different langauge you would like\n").lower()
    while structure not in structures:
        if structure =="help": 
            print("\nYou have asked for the help screen. Below you will see a list of all of the code structures this program includes: ")
            print(structures,"\n")
            structure = input("Now that you have seen the help screen, please enter the code structure you would like to see.\n").lower()
        else:
            structure = input("Sorry that is not a compatible code structure, please enter a different langauge you would like to see\n").lower()
    return(language,structure)
#Logic to be able to select which mode to run in: which way to obtain the input language and structure variables 
if userFriendlyMode ==True:
    language,structure = userFriendlyRun()
else: 
    language,structure =quickRun(language.lower(),structure.lower())

#Logic to determine which language and which code structure to return 
print("---------------------------------------------------------")
print ("Here is the sytnax for "+language.upper()+" "+structure.upper()+":\n\n\n" )
if language == "java":
        if structure == "all":
            allJava()
        else:
            print(java.get(structure, default)())
if language == "javascript" or language == "java script" or language == "js":
    if structure == "all":
            allJs()
    else:
        print( js.get(structure, default)())
if language == "python":
    if structure == "all":
            allPython()
    else:
        print( py.get(structure, default)())
if language == "c++" or language == "cpp":
    if structure == "all":
            allJava()
    else:
        print( cpp.get(structure, default)())
print("\n\n\n---------------------------------------------------------")





