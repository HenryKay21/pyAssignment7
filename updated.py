
print('STUDENT MARKS - PORTAL')
root = Tk()
root.withdraw()
student_info = {}
student_details =[]
name =[]
my_list =[]

def write_to_score(student_name, student_details):
    with open('studentData.txt', 'a') as file:
        file.write('\n'+ student_name + '/' + student_details)
def read_from_score():
    with open('studentData.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            for i in range (len(student_info)):
                student_info[name[i]]= student_details[i]
                student_info[name[i]],student_details[i]= line.split('/')
            print(student_info[name[i]],student_details[i])


student_name = input("Enter new student name:")
test1= int(input('Enter mark for test 1:'))
test2= int(input('Enter mark for test2 :'))
CourseWork= int(input('Enter mark for coursework:'))
FinalExam= int(input('Enter mark for FinalExam:'))

my_list.append(test1)
my_list.append(test2)
my_list.append(CourseWork)

my_list.sort(reverse=True)
print(my_list)
descending_marks = my_list
    
best_two = [descending_marks[0],descending_marks[1]]

def average_percentage(descending_marks):
    average_mark=(descending_marks[0]+descending_marks[1])/2
    Testmark=(average_mark/100)*40
    return int(Testmark)

def exam_percentage(FinalExam):
    ExamMark=(FinalExam/100)*60
    return int(ExamMark)
    
Test= average_percentage(descending_marks)
Exam = exam_percentage(FinalExam)

Total = Test + Exam
print ('From the test your average is ',Test)
print ('From the exam you got ',Exam)
print ('Your total mark is ',Total)
name.append(student_name)
student_details=[{'BestTestResults':best_two,'Finaltest':Exam,'TotalMark':Total}]
student_info=dict(zip(name,student_details))
print (student_info)


write_to_score(student_name,str(student_details))
read_from_score()
