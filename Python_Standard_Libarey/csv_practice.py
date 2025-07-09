import csv

#file = open("data.csv","w")

# with open("data.csv","w") as file:
#     write = csv.writer(file)
#     write.writerow(["Name","Roll","Class"])
#     write.writerow(["Khadija","01","10"])


# with open("data.csv") as file:
#     reader = csv.reader(file)
#     print(list(reader))



###Prictice
with open("practice.csv","w") as data:
    write = csv.writer(data)
    write.writerow(["Company","Project"])
    write.writerow(["Codenco","HR"])
    write.writerow(["Codenco","ERP"])
    print(write)


with open("practice.csv") as data:
    write = csv.reader(data)
    #print(list(write))
    for row in write:
        print(row)