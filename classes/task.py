import os


class Task:
    filename = "work-log.csv"

    CHOICES = {1: "AddTask", 2: "SearchTask", 3: "Quit"}

    def menu(self):
        """
        Display menu choices on the screen, defined in CHOICES dicttionary
        :return:
        """
        print("Welcome to Work Log.")
        for key, value in self.CHOICES.items():
            print(str(key) + ". " + value)

    def clear_screen(self):
        """
        Clear screen
        :return:
        """
        if os.system == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def job_selected(self):
        """
        Job method selection
        :return:
        """
        self.menu()
        selection = input("Hello Commander, what we doing today? "
                          "Please choose a number: ")
        if self.check_selection(selection):
            return int(selection)

    def check_selection(self, selection):
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
