from pathlib import Path

#read = Path("data.json")

#json_data = read.read_text()

json_data =  [
        {
            "id": 21,
            "first_name": "A.B.M Tanvir",
            "last_name": "Rahman",
            "email": "tonmoy271981@gmail.com",
            "country_code": "+880",
            "phone_number": "1610006608",
            "dob": "1981-03-17",
            "blood_group": "B+",
            "current_city": "Dhaka",
            "image": "https://api.exsppm.com/media/profile_pics/IMG_4060.jpeg",
            "is_approved": "approved",
            "is_external": "true"
        },
        {
            "id": 174,
            "first_name": "ABU KHALED",
            "last_name": "MD MASUM",
            "email": "masumakm11@gmail.com",
            "country_code": "+880",
            "phone_number": "01715600641",
            "dob": "1986-07-11",
            "blood_group": "O+",
            "current_city": "Sylhet",
            "image": "https://api.exsppm.com/media/profile_pics/inbound3834748941262603684.jpg",
            "is_approved": "approved",
            "is_external": "true"
        },
        {
            "id": 102,
            "first_name": "AHMED AL",
            "last_name": "MASUM",
            "email": "al.masumsbl2014@gmail.com",
            "country_code": "+880",
            "phone_number": "01674806703",
            "dob": "1983-05-03",
            "blood_group": "B+",
            "current_city": "Sunamganj",
            "image": "https://api.exsppm.com/media/profile_pics/1000048896.jpg",
            "is_approved": "approved",
            "is_external": "true"
        },
        {
            "id": 31,
            "first_name": "ASHIF",
            "last_name": "IQBAL",
            "email": "ashif.iqbaal@gmail.com",
            "country_code": "+880",
            "phone_number": "1713372954",
            "dob": "1981-11-27",
            "blood_group": "B+",
            "current_city": "DHAKA",
            "image": "https://api.exsppm.com/media/profile_pics/WhatsApp_Image_2025-05-18_at_13.59.55.jpeg",
            "is_approved": "approved",
            "is_external": "true"
        },
        {
            "id": 54,
            "first_name": "Abul",
            "last_name": "Hossain",
            "email": "ah8050082@gmail.com",
            "country_code": "+880",
            "phone_number": "01720521052",
            "dob": "1979-02-12",
            "blood_group": "B+",
            "current_city": "Chhatak, Sunamganj",
            "image": "https://api.exsppm.com/media/profile_pics/IMG-20241228-WA0008.jpg",
            "is_approved": "approved",
            "is_external": "true"
        }
    ]

import csv

fields = [ "id",
            "first_name",
            "last_name",
            "email",
            "country_code",
            "phone_number",
            "dob",
            "blood_group",
            "current_city",
            "image",
            "is_approved",
            "is_external"
            ]


# for i in json_data:
#     print(i['id'])
#     print(i['first_name'])

with open("json_test.csv","w",newline="") as file:
    write = csv.DictWriter(file,fieldnames=fields)
    write.writeheader()
    write.writerows(json_data)

with open("json_practice.csv","w",newline="") as file:
    write =csv.DictWriter(file,fieldnames=fields)
    write.writeheader()
    write.writerow(json_data)