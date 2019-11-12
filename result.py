import numpy
import math
import pandas as pd
import csv

#constants
tutorial_1_full_marks = 15
tutorial_2_full_marks = 10

tutorials_overall_weight = 7.5
Attendance_overall_weight = 2.5

total_class = 25


class StudentResult:
    studentCount = -1

    def __init__(self, id, tut1, tut2, clsAttended):
        self.id = id
        self.tutorial_1 = tut1
        self.tutorial_2 = tut2
        
        self.totalMark = 0
        
        self.number_of_class_Present = clsAttended
        
        StudentResult.studentCount += 1

    def displayCount(self):
        print ("Total Student %d" % StudentResult.studentCount)

    def displayStudent(self):
      print ("id : ", self.id,  ", tut1 : ", self.tutorial_1 )



    def getTotalMark(self):
        '''
        '''
        normalized_tutorial_1_marks = (self.tutorial_1 * 100)/ tutorial_1_full_marks
        
        #print ('normalized_tutorial_1_marks : %.2f ' % normalized_tutorial_1_marks)
        
        normalized_tutorial_2_marks = (self.tutorial_2 * 100)/ tutorial_2_full_marks
        #print ('normalized_tutorial_2_marks : %.2f ' % normalized_tutorial_2_marks)

        numerator = normalized_tutorial_1_marks + normalized_tutorial_2_marks;
        denominator = 2;
        avg_of_tutorials_marks = numerator/denominator

        #print ('\t avg_of_tutorials_marks : %.2f ' % avg_of_tutorials_marks)
        
        avg_of_tutorials_marks /= 100
        
        #print ('average_tutorials_marks after scaling to 100 : %.2f ' % avg_of_tutorials_marks)

        tutorial_full_marks = tutorial_1_full_marks+tutorial_2_full_marks;
        #print ('tutorial_full_marks  : %.2f ' % tutorial_full_marks)
        
        weighted_average_tutorials_marks =  avg_of_tutorials_marks * tutorial_full_marks
        self.avg_of_tutorials_marks = weighted_average_tutorials_marks
        #print ('weighted_average_tutorials_marks after scaling to 100 : %.2f ' % weighted_average_tutorials_marks)
        
        
        contribution_of_tutorials_marks = (tutorials_overall_weight * avg_of_tutorials_marks) ;
        self.contribution_of_tutorials_marks = contribution_of_tutorials_marks
        print ('contribution_of_tutorials_marks out of 7.5 : %.2f ' % contribution_of_tutorials_marks)
        
        
        normalized_attendance_pct = (self.number_of_class_Present )/ total_class
        #print ('\t normalized_attendance_pct : %.2f ' % normalized_attendance_pct)
        
        contribution_of_attendance_marks =  (Attendance_overall_weight * normalized_attendance_pct);
        self.contribution_of_attendance_marks = contribution_of_attendance_marks
        print ('contribution_of_attendance_marks out of 2.5 : %.2f ' % contribution_of_attendance_marks)
        
        RAWtotalMark = contribution_of_tutorials_marks + contribution_of_attendance_marks
        print ('\t\t ----RAW  got %.2f out of 10 :  ----- ' % (RAWtotalMark))
        
        self.totalMark = math.ceil(RAWtotalMark)
        
        print ('\t\t ---- The student with id %d got %.2f out of 10 :  ----- \n' % (self.id,self.totalMark))
        return self.totalMark

input = pd.read_csv('Book1.csv')

df = pd.DataFrame(input, columns = ['id','tutorial_1','tutorial_2','class_present'])
#print( df.head())

numberOfStudents = (df.shape[0])-1

A = [StudentResult(a.id, a.tutorial_1,a.tutorial_2,a.class_present) for a in df.itertuples()]

for i in range (0, numberOfStudents):
    
    print(A[i].getTotalMark())


print ("Total student: %d" % StudentResult.studentCount)

#df.to_csv('results.csv')

with open('results_final.csv', mode='w') as csv_file:
    
    fieldnames = ['id','tutorial_1','tutorial_2','avg of tutorials out of 25',
                  'contribution_of_tutorials_marks out of 7.5','class_present','contribution_of_attendance_marks out of 2.5','totalMark']
    
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for i in range (0, numberOfStudents):
    
    
        writer.writerow({'id': A[i].id, 'tutorial_1': A[i].tutorial_1,'tutorial_2': A[i].tutorial_2,
                         'avg of tutorials out of 25':A[i].avg_of_tutorials_marks,'contribution_of_tutorials_marks out of 7.5':A[i].contribution_of_tutorials_marks,
                         'class_present':A[i].number_of_class_Present,'contribution_of_attendance_marks out of 2.5':A[i].contribution_of_attendance_marks,
                         'totalMark': A[i].totalMark})


print('check the file "results_final.csv" for output')
