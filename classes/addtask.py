import datetime
import csv

from classes.task import Task


class AddTask(Task):

    id = 0

    def check_file_is_empty(self, filename):
        """
        Check if the file is empty
        :param filename: Name of the CSV file
        :return: True
        """
        with open(filename, newline='') as csvfile:
            task_reader = csv.reader(csvfile, delimiter=',')
            rows = list(task_reader)
            if len(rows) == 1 and rows[0] == []:
                self.id = 1
                return True
            else:
                self.id = int(rows[-1][0])

    def add_new_entry(self):
        """
        Add new record to CSV / Database
        Validate Date - Correct Format
        Validate Spent Time - if it is an integer (minutes)
        :return: Update the File
        """
        task_date = input("Enter a date: ")
        try:
            datetime.datetime.strptime(task_date, '%Y/%m/%d')
        except:
            print("Date you specified is not valid, please try again.")
            self.add_new_entry()
        else:
            task_title = input("Enter a title: ")
            task_time_spent = input("Enter time spent: ")
            try:
                int(task_time_spent)
            except:
                print("Your selection is not a number, please try again: ")
                self.add_new_entry()
            else:
                task_notes = input("Enter a notes: ")

                with open('work-log.csv', 'a') as csvfile:
                    field_names = ['ID',
                                   'Task Date',
                                   'Task Title',
                                   'Time Spent',
                                   'Task Notes']
                    
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

                    """
                    # TO DO
                    # Refactor above the script to this
                    data = OrderedDict([
                        ('ID', self.id),
                        ('Task Date', task_date),
                        ('Task Title', task_title),
                        ('Time Spent', task_time_spent),
                        ('Task Notes', task_notes)
                    ])

                    if self.check_file_is_empty(self.filename):
                        task_writer.writeheader()
                        task_writer.writerow(data)
                    else:
                        data['ID'] += 1  # increment the ID
                        task_writer.writerow(data)
                    """
