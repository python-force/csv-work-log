import os
import time

from task import AddTask, SearchTask, Task

# Script doesn't execute when imported
if __name__ == '__main__':
    # The script will keep running till the user is satisfied
    while True:
        Task().clear_screen()

        # job to do
        i = Task().job_selected()

        # validation if the input is a number (int)
        if isinstance(i, int):

            if i == 1:
                AddTask().add_new_entry()
                Task()
                print("Record successfully added.")
            elif i == 2:
                Task().clear_screen()
                SearchTask()
            elif i == 3:
                Task().clear_screen()
                print("Thank you for using our Mars Data Log.")
                break

        else:
            # The selection is not a number, delay for 2 secs
            # with explanation and ask again
            print("That choice is not in the binder, please try again. Loading menu...")
            time.sleep(3)

    print("Thank you and have a very safe and productive day. Work Safe. Work Smart.")