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

    def search_existing_entries(self):
        pass