import os
import time

from task import AddTask, SearchTask

CHOICES = {1: "AddTask", 2: "SearchTask", 3: "Quit"}

def clear_screen():
    """
    Clear screen
    :return:
    """
    if os.system == "nt":
        os.system('cls')
    else:
        os.system('clear')

def job_selected():
    """
    Job method selection
    :return:
    """
    selection = input("Hello Commander, what we doing today? "
                "Please choose a number: ")
    if check_selection(selection):
        print("Great choice, " + str(selection) + " it is then.")
        return int(selection)

def check_selection(selection):
    """
    Validation of the user's choice of the job
    :param selection:
    :return:
    """
    try:
        int(selection)
        return True
    except:
        pass

# Script doesn't execute when imported
if __name__ == '__main__':
    # The script will keep running till the user is satisfied
    while True:
        clear_screen()

        # job to do
        i = job_selected()

        # validation if the input is a number (int)
        if isinstance(i, int):

            if i == 1:
                AddTask().add_new_entry()
                print("Record successfully added.")
                break
            elif i == 2:
                SearchTask()
                break

        else:
            # The selection is not a number, delay for 2 secs
            # with explanation and ask again
            print("That choice is not in the binder, please try again. Loading menu...")
            time.sleep(3)

    print("Done Coding - No more messages to send")