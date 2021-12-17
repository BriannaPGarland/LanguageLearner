# LanguageLearner
This is a final project for an engineering python class at Stevens Institute of Technology 

## Brief Over View 

	We have all been there, working in a new class, new job or new project that requires using the capabilities of a different language. The tool I made for this project is aimed at somewhat experienced programmers who know at least one language and are trying to / need to learn more. As a programmer once you learn the foundations and the way of thinking with one programming language, it is really easy to learn others once you know the new syntax and that is what this program aims to help with.
	I created a program that allows a user to enter a programming language and the code structure they would like to see and the resultant syntax is then displayed in a user friendly way in the terminal. This project can be run anywhere as long as the languageLearner.py file is in the directory you are in. There are built-in help screens that allow the user to see the capabilities of all of the different languages and the different coding structures they can access. As well as a feature to allow users to enter all in place of the named coding structure after they have selected the language that will display all of the basic syntax for that particular language. 
	As a software developer, I know how important it is for software tools to be easy and quick to use so as to not add more time and effort into using it than its worth. That was one of my main goals behind the structure of the code and creating two different options for users of different experience levels. Experienced software developers do not want to be prompted several different times in order to get the input, they benefit from one line and done because it is the most efficient. However new users who are not experienced with using the terminal to run code will benefit from being able to be prompted separately and getting more use out of the further help screens. 
	This project has the capability to be vastly expanded upon in the future. More languages and more specific coding structures can be added. The way I developed and structured the code is that it would be very easy to adapt and add onto and really personalize the experience of the user. It also has the potential to have users enter what they want the code structure to do or contain more user specific information for each structure. 
	Overall, this project was a great learning experience, as well as a chance to create something that will actually have an impact. I used all of the core python knowledge I learned during this class this semester and applied it to my development. Software has the chance to change lives, this class has showed me more and more what it means to be on the development side of things and the full potential of the language python! 

## How to use & Separate Features 
1. Cd to the directory that the file is located in 
2. Run: 
    ### python languageLearner.py -h
     - This will display a help screen that explains the two different modes of the program that you can run 
    ### python languageLearner.py -a   
     - This is the user friendly mode that has the program individually prompt the user for the language and code structure separately 
     - Has error handling if you enter a non compatible language or code structure it allows the user to re-enter, it also does not matter if the user puts capitals        or enters the language in a different way, there are options that account for variety of user input  
     - It also has a help screen option at each of the prompts to assist the user in choosing their language and code 
     - If you put “all” for code structure it will display all of the basic syntax 
     - This is a screenshot of a sample of the output in this mode:
     	![alt text](https://github.com/BriannaPGarland/LanguageLearner/blob/main/Screen%20Shot%202021-12-17%20at%204.58.16%20PM.png)

    ### python languageLearner.py -q “Language”,”Code structure” 
    Need to be sure to have quotes around both and a comma in the middle of the two 
 
    - This is the programmer friendly mode that allows the user to type one line into the terminal and it spits out the result. This allows for speed and         
      convenience 
    - It has all of the same error handling as the other mode. 
    - Can still use the all or help add ins in this mode. 
    - This is an example of the code output:
      ![alt text](https://github.com/BriannaPGarland/LanguageLearner/blob/main/Screen%20Shot%202021-12-17%20at%204.58.24%20PM.png)

## Link to Source Code on Git Hub 
https://github.com/BriannaPGarland/LanguageLearner

## Link to Video Demo 
https://youtu.be/JJU-mtKDkLs 

