import csv, sys
from Keyboard import Keyboard



class Book():
    def __init__(self) -> None:
        self.dictionary = {}
        self.keys = Keyboard(self.add, self.remove, self.exit, self.help)
        self.saved_changes = True
    
    def save_file(self):
        pass

    def help(self):
        print("Type add to add people \n Type save to save to memory \n Type quit/exit to exit the script \n Type remove to Remove people from the list")

    def save(self):
        return_state = False
        while not return_state:
            save = input('Is this correct and do you want to save this ? (y/yes or n/no): ')
            return_state = self.valid(save)

    def valid(self, inp):
        if inp == 'y' or inp == 'yes':
            print('ok, saved')
            return True
        elif inp == 'n' or inp == 'no':
            print('ok, not saving this time')
            return True
        else:
            print('please enter y/yes or n/no')
            return False
    def exit(self):
        if self.saved_changes:
            save_before_exit = input('Do you want to save before exiting (yes/no): ')
            if save_before_exit == 'yes' or save_before_exit == 'y':
                self.save_file()
                sys.exit()
            elif save_before_exit == 'no' or save_before_exit == 'n':
                sys.exit()
            else:
                self.exit()
        else:
            sys.exit()

    def remove(self):
        print('remove')
        
    def add(self):
        name = input('Please etner a name: ')
        phone_number = input('Please, enter a phone number: ')
        print(f'The name of the person is {name} \n The contact for {name} is {phone_number}')
        self.saved_changes = False
        self.save() 

    def start(self):
        while True:
            self.keys.key_check()
            

if __name__ == '__main__':
    b = Book()
    b.start()



    

        
