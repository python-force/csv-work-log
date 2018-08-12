import os
import re
import csv
import shutil
from tempfile import NamedTemporaryFile

class Task:
    filename = "work-log.csv"


class AddTask(Task):

    id = 0

    def check_file_is_empty(self, filename):
        with open(filename, newline='') as csvfile:
            task_reader = csv.reader(csvfile, delimiter=',')
            rows = list(task_reader)
            if len(rows) == 1 and rows[0] == []:
                self.id = 1
                return True
            else:
                self.id = int(rows[-1][0])

    def add_new_entry(self):

        task_date = input("Enter a date: ")
        task_title = input("Enter a title: ")
        task_time_spent = input("Enter time spent: ")
        task_notes = input("Enter a notes: ")


        with open('work-log.csv', 'a') as csvfile:
            field_names = ['ID', 'Task Date', 'Task Title', 'Time Spent', 'Task Notes']
            task_writer = csv.DictWriter(csvfile, fieldnames=field_names)

            if self.check_file_is_empty(self.filename):
                task_writer.writeheader()
                task_writer.writerow({
                    'ID': self.id,
                    'Task Date': task_date,
                    'Task Title': task_title,
                    'Time Spent': task_time_spent,
                    'Task Notes': task_notes
                })
            else:
                task_writer.writerow({
                    'ID': self.id + 1,
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
                 self.search_by_pattern()
            else:
                print("Your selection is invalid, please try again")
                SearchTask()

    def clear_screen(self):
        """
        Clear screen
        :return:
        """
        if os.system == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def edit_record(self, id):

        task_date = input("Enter a date: ")
        task_title = input("Enter a title: ")
        task_time_spent = input("Enter time spent: ")
        task_notes = input("Enter a notes: ")

        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['ID', 'Task Date', 'Task Title', 'Time Spent', 'Task Notes']

        with open(self.filename, 'r') as file, tempfile:
            reader = csv.DictReader(file, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['ID'] == str(id):
                    print('Updating row, please wait', row['ID'])
                    row['Task Date'], row['Task Title'], row['Time Spent'], row[
                        'Task Notes'] = task_date, task_title, task_time_spent, task_notes
                    row = {'ID': row['ID'], 'Task Date': row['Task Date'], 'Task Title': row['Task Title'],
                       'Time Spent': row['Time Spent'], 'Task Notes': row['Task Notes']}
                writer.writerow(row)

        shutil.move(tempfile.name, self.filename)
        print("Your record was successfuly saved.")
        SearchTask()

    def delete_record(self, id):

        """
        # has an issue stacking frames if you type different key multiple times
        # 5x times press x - 5x will replace the file
        question = input("You are about to delete a record, are you sure? ")
        if question == "n":
            SearchTask()
        elif question == "y":
            pass
        else:
            print("Your input is invalid, please choose from the following again.")
            self.delete_record(id)
        """

        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['ID', 'Task Date', 'Task Title', 'Time Spent', 'Task Notes']

        with open(self.filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['ID'] != str(id):
                    print('updating row', row['ID'])
                    row = {'ID': row['ID'], 'Task Date': row['Task Date'], 'Task Title': row['Task Title'],
                           'Time Spent': row['Time Spent'], 'Task Notes': row['Task Notes']}
                    writer.writerow(row)

        shutil.move(tempfile.name, self.filename)

    def crud(self, action, record_id, step, data_dict):
        if action == "n" and step < len(data_dict):
            self.clear_screen()
            return True
        if action == "n" and step >= len(data_dict):
            self.clear_screen()
            SearchTask()
        elif action == "r":
            self.clear_screen()
            SearchTask()
        elif action == "e":
            self.clear_screen()
            self.edit_record(record_id)
        elif action == "d":
            self.clear_screen()
            self.delete_record(record_id)
        else:
            message = "Your selection was invalid please try again: "
            self.show_results(data_dict, message)

    def show_results(self, data_dict, message):
        self.clear_screen()
        self.message = message
        step = 0
        record_id = 0
        if message != "":
            print("Your selection was invalid please try again. ")
        for index, record in data_dict.items():
            for task_header, data in record.items():
                if task_header != "ID":
                    print(task_header + ": " + data)
                else:
                    record_id = int(data)
            print("Results " + str(step+1) + " of " + str(len(data_dict)))
            step += 1
            if step == len(data_dict):
                action = input("Delete, Edit, Return to the Menu ")
                action = action.lower()
                if self.crud(action, record_id, step, data_dict):
                    continue
                else:
                    break
            else:
                action = input("Next, Delete, Edit, Return to the Menu ")
                action = action.lower()
                if self.crud(action, record_id, step, data_dict):
                    continue
                else:
                    break

    def search_by_date(self):
        print("date")

    def search_by_time_spent(self):
        search_time = input("What time you looking for?: ")
        try:
            int(search_time)
        except:
            print("Your selection is not a number, please try again: ")
            self.search_by_time_spent()
        else:
            data_dict = {}
            with open(self.filename, newline='') as csvfile:
                task_reader = csv.DictReader(csvfile, delimiter=',')
                for row in task_reader:
                    for key, value in row.items():
                        if key == "Time Spent":
                            found = re.match(r'\b{0}\b'.format(search_time), row[key])
                            if found:
                                data_dict[row['ID']] = row
            message = ""
            self.show_results(data_dict, message)

    def search_by_exact_match(self):
        print("match")

    def search_by_pattern(self):
        print("pattern")