import os, sys
from Keyboard import Keyboard
from file_work import Files

'''#TODO 
    - [x] Saving to file
    - [x] Removing user
    - [x] User list
'''
class Book:
    def __init__(self) -> None:
        os.system('clear')
        self.file = Files()
        self.keys = Keyboard(self.file.show, self.file.save_file, self.file.add, self.file.remove, self.help, self.exit)
        
    

    def help(self):
        print("Type add to add people \n Type save to save to memory \n Type quit/exit to exit the script \n Type remove to Remove people from the list")

    def valid(self, inp):
        if inp == 'y' or inp == 'yes':
            return [True, True]
        elif inp == 'n' or inp == 'no':
            return [True, False]
        else:
            return [False, False]
        
    def exit(self):
        ret_list = [False]
        while not ret_list [0]:
            sure_exit = input('Do you really want to exit?: ')
            ret_list = self.valid(sure_exit)

        if ret_list[1]:
            if not self.file.saved_changes:
                save_before_exit = input('Do you want to save before exiting (yes/no): ')
                if save_before_exit == 'yes' or save_before_exit == 'y':
                    self.file.save_file()
                    sys.exit()
                elif save_before_exit == 'no' or save_before_exit == 'n':
                    sys.exit()
                else:
                    self.exit()
            else:
                sys.exit()


    def start(self):
        while True:
            self.keys.key_check()
            

if __name__ == '__main__':
    b = Book()
    b.start()



    

        
