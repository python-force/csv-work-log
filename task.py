import csv
import re

class Task:
    filename = "work-log.csv"


class AddTask(Task):

    def check_file_is_empty(self, filename):
        with open(filename, newline='') as csvfile:
            task_reader = csv.reader(csvfile, delimiter=',')
            rows = list(task_reader)
            if len(rows) == 1 and rows[0] == []:
                return True

    def add_new_entry(self):

        task_date = input("Enter a date: ")
        task_title = input("Enter a title: ")
        task_time_spent = input("Enter time spent: ")
        task_notes = input("Enter a notes: ")


        with open('work-log.csv', 'a') as csvfile:
            field_names = ['Task Date', 'Task Title', 'Time Spent', 'Task Notes']
            task_writer = csv.DictWriter(csvfile, fieldnames=field_names)

            if self.check_file_is_empty(self.filename):
                task_writer.writeheader()

            task_writer.writerow({
                'Task Date': task_date,
                'Task Title': task_title,
                'Time Spent': task_time_spent,
                'Task Notes': task_notes
            })


class SearchTask(Task):

    SEARCH_CHOICES = {1: "Date", 2: "Time Spent", 3: "Exact Match", 4: "Pattern"}

    def __init__(self, selection = 0):
        self.selection = input("Which search you would like to perform?: ")
        try:
            search_selection = int(self.selection)
        except ValueError:
            print("Your selection is invalid, please try again")
            SearchTask()
        else:
            if search_selection == 1:
                self.search_by_date()
            elif search_selection == 2:
                self.search_by_time_spent()
            elif search_selection == 3:
                self.search_by_exact_match()
            elif search_selection == 4:
                 self.search_by_patter()

    def show_results(self, data_dict):
        print(data_dict)
        print(len(data_dict))

    def search_by_date(self):
        print("date")

    def search_by_time_spent(self):
        data_dict = {}
        x = 0
        with open(self.filename, newline='') as csvfile:
            task_reader = csv.DictReader(csvfile, delimiter=',')
            for row in task_reader:
                for key, value in row.items():
                    if key == " Time Spent":
                        found = re.search(r'18', row[key])
                        if found:
                            data_dict[x] = row
                            x += 1

        self.show_results(data_dict)

    def search_by_exact_match(self):
        print("match")

    def search_by_patter(self):
        print("pattern")