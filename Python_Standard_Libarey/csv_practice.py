import csv
import pandas as pd
#file = open("data.csv","w")

# with open("data.csv","w") as file:
#     write = csv.writer(file)
#     write.writerow(["Name","Roll","Class"])
#     write.writerow(["Khadija","01","10"])


# with open("data.csv") as file:
#     reader = csv.reader(file)
#     print(list(reader))



###Prictice
# with open("practice.csv","w") as data:
#     write = csv.writer(data)
#     write.writerow(["Company","Project"])
#     write.writerow(["Codenco","HR"])
#     write.writerow(["Codenco","ERP"])
#     print(write)


# with open("practice.csv") as data:
#     write = csv.reader(data)
#     #print(list(write))
#     for row in write:
#         print(row)

## Create two csv file and combain them

with open("school.csv","w",newline='') as school:
    school_write = csv.writer(school)
    school_write.writerow(["Class","Student","Roll"])
    school_write.writerow(["Class 8","khadija","1"])
    school_write.writerow(["Class 9","Halima","90"])

    
with open("school.csv","r",newline='') as school:
    school_reader = csv.reader(school)
    for i in school_reader:
        print(i)

with open("school2.csv","w",newline='') as school2:
    write1 = csv.writer(school2)
    write1.writerow(["Class","Teacher","Designation"])
    write1.writerow(["8","khadija","Senior Teacher"])
    write1.writerow(["10","Halima","Junior Teacher"])

    
with open("school2.csv","r",newline='') as school:
    reader2 = csv.reader(school)

    for i in reader2:
        print(i)

files_names = ['school.csv','school2.csv']
output_file = 'merged_data.csv'

print("Loop start")
with open(output_file,'w',newline='') as output:
    writer = csv.writer(output)
    for i in files_names:
        #class 8, khadija ,1
        with open(i, 'r') as infile:
            read = csv.reader(infile)
            for j in read:
                #
                writer.writerow(j)

                

# with open("kk 8, khadija ,1" , 'r') as infile:
#     read = csv.reader(infile)
#     for j in read:
#         print(j)             

        

            

# df1 = pd.read_csv("school.csv")
# df2 = pd.read_csv("school2.csv")

# df_combain = pd.concat([df1,df2],ignore_index=True)

# df_combain.to_csv("combain_output.csv",index=False)

files_names = ['school.csv','school2.csv']

for p in files_names:
    print(p)

class Car:
    def __init__(self,name):
        self.name = name
        print(f"{self.name}")


car = Car("blue")
# car.name = "blue"
