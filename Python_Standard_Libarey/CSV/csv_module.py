import csv

# school_teacher = ["Khadija","Halima","Ibrahim"]
# school_student = ["pintu","rinku","cinku"]


# with open("school_teacher.csv","w",newline='') as school:
#     school_writer = csv.writer(school)
#     for index,value in enumerate(school_teacher,start=1):
#         school_writer.writerow([index,value])
    
# with open("school_teacher.csv","r",newline='')as school:
#     school_reader = csv.reader(school)
#     for i in school_reader:
#         print(i)

# print("Student started")

# with open("school_student.csv","w",newline="") as school1:
#     school1_writer = csv.writer(school1)
#     for index,value in enumerate(school_student,start=1):
#         school1_writer.writerow([index,value])

# with open("school_student.csv","r",newline="") as school1:
#     school1_reader = csv.reader(school1)
#     for i in school1_reader:
#         print(i)


# print("Combain started")
# combain_files = ["school_teacher.csv","school_student.csv"]

# with open("output.csv","w",newline="") as output:
#     output_writer = csv.writer(output)
#     for i in combain_files:
#         with open(i, 'r') as file:
#             read = csv.reader(file)
#             for j in read:
#                 output_writer.writerow(j)

# with open("output.csv","r",newline="") as output:
#     output_reader = csv.reader(output)
#     for i in output:
#         print(i)


## Function

school_teacher = ["Khadija","Halima","Ibrahim"]
school_student = ["pintu","rinku","cinku"]

def csv_write(file_name,data_list):
    with open(file_name,"w",newline='') as file:
        file_writer = csv.writer(file)
        for index,value in enumerate(data_list,start=1):
            file_writer.writerow([index,value])

def csv_read(file_name):
    with open(file_name,"r",newline="") as file:
        file_reader = csv.reader(file)
        for i in file_reader:
            print(i)


combain_files = ["school_teacher.csv","school_student.csv"]

def csv_combain(output_files,combain_files):
    with open(output_files,"w",newline="") as output:
        output_writer = csv.writer(output)
        for i in combain_files:
            with open(i, 'r') as file:
                read = csv.reader(file)
                for j in read:
                    output_writer.writerow(j)
    
            

csv_write("school_teacher.csv",school_teacher)
csv_write("school_student.csv",school_student)

print("School Teacher")
csv_read("school_teacher.csv")
print("School Student")
csv_read("school_student.csv")

print("Comabin")
csv_combain("result.csv",combain_files)
csv_read("result.csv")
