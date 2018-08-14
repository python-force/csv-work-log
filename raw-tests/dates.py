import datetime
import csv

"""
def validate(date_text):
    try:
        
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
"""

text = datetime.datetime.strptime("1981/12/25", '%Y/%m/%d')
text2 = datetime.datetime.strptime("1981/12/27", '%Y/%m/%d')
x = datetime.datetime.strptime("1981/12/28", '%Y/%m/%d')

y = text <= x <= text2
# print(y)


start_date = datetime.datetime.strptime("2027/03/14", '%Y/%m/%d')
end_date = datetime.datetime.strptime("2034/11/23", '%Y/%m/%d')
value = "2026/04/21"
value = datetime.datetime.strptime(value, '%Y/%m/%d')
found = start_date <= value <= end_date
print(found)

data_dict = {}
header = ["Task Date"]
with open("work-log.csv", newline='') as csvfile:
    task_reader = csv.DictReader(csvfile, delimiter=',')
    for row in task_reader:
        for key, value in row.items():
            if key == header[0]:
                value = datetime.datetime.strptime(value, '%Y/%m/%d')
                found = start_date <= value <= end_date
                if found:
                    data_dict[row['ID']] = row
for key, value in data_dict.items():
    print(key, value)
