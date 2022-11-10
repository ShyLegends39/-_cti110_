# Brief INFO: This program does works by processing the given input and then notify the user by asking if it is vaild or not.
# Also, uses a loop to collect the data to work it out and show it in the output and for info go to pseudocode.

# CTI-110

# P4HW1 - List

# Kelly Bullard

# November 10, 2022

#

# Input is: Asking to enter how many scores. Then it asks you to enter each of those scores, if one is not, must
# notify the user asking for a vaild. If it is invalid to then say, "INVALID Score entered!!!!", for that one input
# that will tell with the input line (that in invalid)to enter again. But the line said INVALID and to re-enter the score,
# it needs tell the score's range between 0 and 100. After that it goes on with entering the rest of the scores and read in the bonus and processing for more details!

# Bonus: make sure to have: an empty list, first input line, and then do the initializing of currentNumOfScores by 0!

# Processing(invalid factor and loop and list and sorting out the grades) is:
# Computing grade based on the average score with loop and this where only inputs for entering the scores and woking on & talk about if there is any INVALID factors,
# and use float for these. For the loop(Looping until we have all all required number of scores)
# here used while, if-else, elif. Also, prompting for user input if entered score was invalid.
# Then processes that by adding vaild input into the list and then Breaking out of the loop as a valid score was there.
# Next, it processes it by: works on min, taking out certain ones for min, work on the rest and the average,
# and then incrementing the count of currentNumOfScores by add 1 and for input for this,
# like this(make sure to put it in normally for the code, and this goes for INVAILD):
# print('Enter score #', end=''), print(currentNumOfScores + 1,end=''), print(': ',end=''), scores = float(input()).
# Next it use loop with if-elif in it to process the data for letter. Then it processes everything else in order put be put in the output format.

# Bonus: make sure to stuff like this: >=, ==, +=, or, and, in your loop and use in two of your while loops uses True.

# Output is: Shows inputs and their prompt and then showing the Results with both on sides of it having a lot of dash and same for at the end minus the word.
# Sandwich between Result and the last last line is the output for the results from the processing and
# having first: Lowest Score, Modified List, Scores Average, Grades(ALL: w/ some space then : the result and they will vary from what the processing gives us for each one).

# NOTE: For more read the comments for even more details! Sorry for repeating info in the pseudocode, I just want make sure that I got everything!

# Make an empty list
listOfScores = []

# Input for numberOfScores
numberOfScores = int(input('How many numbers you want to enter? '))
print() # For a space

# Initializing 
currentNumOfScores = 0

# Loop all
while(True):
    
    # For user input
    while(currentNumOfScores < numberOfScores):
        print('Enter score #',end='')
        print(currentNumOfScores + 1,end='')
        print(': ',end='')
        scores = float(input())
        
        
        # Prompting and checking invalid input
        while(True):
            if(scores < 0 or scores > 100):
                print('\nINVALID Score entered!!!!\nScore should be between 0 and 100')
                print('Enter score #',end='')
                print(currentNumOfScores + 1,'again: ',end = '')
                scores = float(input())
                
            
            # If valid score was entered    
            else:
                
                # Adding it to the list
                listOfScores.append(scores)
                
                # No need for Prompting again, so...
                break
        
            
        # When a valid score was entered
        currentNumOfScores += 1 
        
        
    # If user entered all required number of valid scores
    if(currentNumOfScores == numberOfScores):
        # Breaking out of the loop for no further input 
        break

# Computing minimum score
minElement = min(listOfScores)

# Removing min score from the list
listOfScores.remove(min(listOfScores))

# Computing average score
average = sum(listOfScores)/len(listOfScores)

# For computing the average to letter grade 
if(average >= 93 and average <= 100):
    grade = 'A'

elif(average >=90 and average <= 92.9):
    grade = 'B+'
    
elif(average >= 87 and average <= 89.9):
    grade = 'B'
    
elif(average >= 83 and average <= 86.9):
    grade = 'B-'
    
elif(average >= 80 and average <= 82.9):
    grade = 'C+'
    
elif(average >= 77 and average <= 79.9):
    grade = 'C'
    
elif(average >= 73 and average <= 76.9):
    grade = 'C-'
    
elif(average >= 70 and average <= 72.9):
    grade = 'D+'
    
elif(average >= 67 and average <= 69.9):
    grade = 'D'
    
elif(average >= 60 and average <= 66.9):
    grade = 'D-'
    
elif(average <= 0):
    grade = 'F'

# For two spaces
print()
print()
# Displaying the results
print('-----------Results-------------')
print('Lowest Score  :',minElement)
print('Modified List :',listOfScores)
print('Scores Average:',average)
print('Grade         :',grade)
print('---------------------------------')

