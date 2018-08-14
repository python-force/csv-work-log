import datetime
import re
import csv
import shutil
from tempfile import NamedTemporaryFile

from classes.task import Task

class SearchTask(Task):

    SEARCH_CHOICES = {1: "Date", 2: "Time Spent", 3: "Exact Match", 4: "Pattern", 5: "Main Menu"}

    def __init__(self, selection = 0):
        """
        Initialize Menu Selection
        Based on the selection route the user to each method
        :param selection:
        """
        self.main_menu()
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
            elif search_selection == 5:
                self.clear_screen()
            else:
                print("Your selection is invalid, please try again")
                SearchTask()

    def main_menu(self):
        """
        Display Main Menu on the screen with selection
        :return: Menu being displayed
        """
        print("Welcome to Search.")
        for key, value in self.SEARCH_CHOICES.items():
            print(str(key) + ". " + value)

    def edit_record(self, id):
        """
        Edit record
        Validate Date
        Validate time spent if it is an integer
        Since you cannot update files like Database
        It will create a Temp file and put everything into temp file
        Replace original with temp
        :param id: ID of the record being edited
        :return: Updated CSV file
        """
        task_date = input("Enter a date, Format YYYY-MM-DD: ")
        try:
            datetime.datetime.strptime(task_date, '%Y/%m/%d')
        except:
            print("Date you specified is not valid, please try again.")
            self.edit_record(id)
        else:
            task_title = input("Enter a title: ")
            task_time_spent = input("Enter time spent: ")
            try:
                int(task_time_spent)
            except:
                print("Your selection is not a number, please try again: ")
                self.edit_record(id)
            else:
                task_notes = input("Enter a notes: ")

                tempfile = NamedTemporaryFile(mode='w', delete=False)

                fields = ['ID', 'Task Date', 'Task Title', 'Time Spent', 'Task Notes']

                with open(self.filename, 'r') as file, tempfile:
                    reader = csv.DictReader(file, fieldnames=fields)
                    writer = csv.DictWriter(tempfile, fieldnames=fields)
                    for row in reader:
                        if row['ID'] == str(id):
                            # print('Updating row with ID ' + row['ID'] + ' , please wait')
                            row['Task Date'], row['Task Title'], row['Time Spent'], row[
                                'Task Notes'] = task_date, task_title, task_time_spent, task_notes
                            row = {'ID': row['ID'], 'Task Date': row['Task Date'], 'Task Title': row['Task Title'],
                               'Time Spent': row['Time Spent'], 'Task Notes': row['Task Notes']}
                        writer.writerow(row)

                shutil.move(tempfile.name, self.filename)
                self.clear_screen()
                print("Your record was successfuly saved.")
                SearchTask()

    def delete_record(self, id):
        """
        Delete record from the CSV
        Create temp file store everything except the record with ID
        Replace original with the temp file
        :param id: ID of the record being deleted
        :return: New CSV file
        """
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['ID', 'Task Date', 'Task Title', 'Time Spent', 'Task Notes']

        with open(self.filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['ID'] != str(id):
                    # print('updating row', row['ID'])
                    row = {'ID': row['ID'], 'Task Date': row['Task Date'], 'Task Title': row['Task Title'],
                           'Time Spent': row['Time Spent'], 'Task Notes': row['Task Notes']}
                    writer.writerow(row)
                else:
                    deleted_one = {'ID': row['ID'], 'Task Date': row['Task Date'], 'Task Title': row['Task Title'],
                           'Time Spent': row['Time Spent'], 'Task Notes': row['Task Notes']}

        shutil.move(tempfile.name, self.filename)
        self.clear_screen()
        print("Record ID " + deleted_one['ID'] + " called [" + deleted_one['Task Title'] + "], was successfully deleted.")
        SearchTask()

        """
            # TO DO: Upgrade it to version that have validation questions
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

    def crud(self, action, record_id, step, data_dict):
        """
        CREATE, READ, UPDATE, DELETE
        Direct user based on selection to each method
        :param action: Selection
        :param record_id: ID of the record
        :param step: When showing results remembering where I was
        :param data_dict: Results dictionary having records that has been found
        :return: Direct user based on selection to each method
        """

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
        """
        Showing results from each method
        :param data_dict: Results dictionary having records that has been found
        :param message: Result message
        :return: Display results and route user next
        """
        self.clear_screen()
        self.message = message
        step = 0
        record_id = 0
        if message != "":
            print("Your selection was invalid please try again. ")
        if data_dict != None:
            for index, record in data_dict.items():
                for task_header, data in record.items():
                    if task_header != "ID":
                        print(task_header + ": " + data)
                    else:
                        record_id = int(data)
                print("Results " + str(step+1) + " of " + str(len(data_dict)))
                step += 1
                if step == len(data_dict):
                    action = input("[D]elete, [E]dit, [R]eturn to the Menu ")
                    action = action.lower()
                    if self.crud(action, record_id, step, data_dict):
                        continue
                    else:
                        break
                else:
                    action = input("[N]ext, [D]elete, [E]dit, [R]eturn to the Menu ")
                    action = action.lower()
                    if self.crud(action, record_id, step, data_dict):
                        continue
                    else:
                        break
            else:
                self.clear_screen()
                print("No records found.")
                SearchTask()

    def perform_csv_search(self, header, search_data):
        """
        Search for all methods being used to perform search based on input
        :param header: Header of the CSV file being edited
        :param search_data: Data that are being searched
        :return: Route method to show results
        """
        data_dict = {}
        with open(self.filename, newline='') as csvfile:
            task_reader = csv.DictReader(csvfile, delimiter=',')
            for row in task_reader:
                for key, value in row.items():
                    if len(header) > 1:
                        if key == header[0] or key == header[1]:
                            found = re.search(search_data, row[key], re.I)
                            if found:
                                data_dict[row['ID']] = row
                    else:
                        if key == header[0]:
                            found = re.match(r'\b{0}\b'.format(search_data), row[key])
                            if found:
                                data_dict[row['ID']] = row
        message = ""
        self.show_results(data_dict, message)

    def search_by_date(self):
        """
        Searching by valid date
        :return: Route method to show results
        """
        search_data = input("What date you looking for? Format YYYY-MM-DD: ")
        try:
            datetime.datetime.strptime(search_data, '%Y/%m/%d')
        except:
            print("Date you specified is not valid, please try again.")
            self.search_by_date()
        else:
            header = ["Task Date"]
            self.perform_csv_search(header, search_data)

    def search_by_time_spent(self):
        """
        Searching by valid time spent
        :return: Route method to show results
        """
        search_data = input("What time you looking for?: ")
        try:
            int(search_data)
        except:
            print("Your selection is not a number, please try again: ")
            self.search_by_time_spent()
        else:
            header = ["Time Spent"]
            self.perform_csv_search(header, search_data)

    def search_by_exact_match(self):
        """
        Searching by regex to find exact match
        :return: Route method to show results
        """
        search_data = input("Enter a string you looking for: ")
        search_data = r'\b{0}\b'.format(search_data)
        header = ["Task Notes", "Task Title"]
        self.perform_csv_search(header, search_data)

    def search_by_pattern(self):
        """
        Searching by regex valid pattern
        :return: Route method to show results
        """
        search_data = input("Enter pattern: ")
        try:
            re.compile(search_data)
        except:
            print("Your pattern is not valid, please try again.")
            self.search_by_pattern()
        else:
            header = ["Task Notes", "Task Title"]
            self.perform_csv_search(header, search_data)