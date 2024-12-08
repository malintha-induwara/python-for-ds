#write a python function called "summarize_grades" that accept a students names as a mandetory argument and a arbitery number of grade scores. the function should,
#1) print the student name
#2) calculate and print the highest grade,lowest grade,average grade from the provided scores
#3) If no grades are provided you should print "No grades available"

def summarize_grades(student_name,*grades):
    print("Student Name:",student_name)
    if len(grades)==0:                      #if not grades:
        print("No grades available")
    else:
        print("Highest Grade:",max(grades))
        print("Lowest Grade:",min(grades))
        print("Average Grade:",sum(grades)/len(grades))

summarize_grades("Sam",10,20,35,67,41)

