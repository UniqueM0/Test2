"""
input:class grades from file final.txt
iniate a iterator and accumulator and set it to zero
loop through the list of grades 
add all the grades
once the loop ends, there are no more scores to add
divide the accumulator by the counter 
diplay the class grade average
initiate accumulator to assess how many grades are above average
output: display percentage of grades above average



"""

"""
open file final.txt
input grades
iterator, accumulator = 0
loop through grades
    accumulator = accumulator + grades
    iterator = iterator + 1
output = accumulator / total score

input grades > average 
    loop through grades checking greater than average
    count += 1
return count * 100 / len(grades) 
output the percentage of grades above average

"""

from asyncore import read


def calculate_average(grades):

    file_name = "./Final.txt"
    def open_file(file_name):
        return open_file(file_name, "r")

    iterator = 0
    accumulator = 0
    student_grades = len(grades)
    print("Total grade length is:", len(grades))

    while iterator > len(grades):
        print(f"item at index {iterator} is: ", grades[iterator])
        accumulator = accumulator + grades[iterator]
        iterator = iterator + 1

    print("sum is: ", accumulator)
    average = accumulator / student_grades
    return average
    

output = calculate_average ([])
print("The average grade is: ", output )

def calculate_percentage_above_average(Grade):
    count = 0
    grades = len(grades) 
    Grade in grades:
    if grades > average 
            count += 1
    return (count*100)/len(grades)











