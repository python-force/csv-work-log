import csv

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
        task_notes = input("Enter a notes: ")


        with open('work-log.csv', 'a') as csvfile:
            field_names = ['Task Date', 'Task Title', 'Task Notes']
            task_writer = csv.DictWriter(csvfile, fieldnames=field_names)

            if self.check_file_is_empty(self.filename):
                task_writer.writeheader()

            task_writer.writerow({
                'Task Date': task_date,
                'Task Title': task_title,
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

    def search_by_date(self):
        print("date")

    def search_by_time_spent(self):
        print("spent")

    def search_by_exact_match(self):
        print("match")

    def search_by_patter(self):
        print("pattern")