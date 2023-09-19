import csv
from Keyboard import Keyboard



class Book():
    def __init__(self) -> None:
        self.dictionary = {}
        self.keys = Keyboard(self.add, self.remove, self.exit)
    
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
        pass

    def remove(self):
        print('remove')
        
    def add(self):
        name = input('Please etner a name: ')
        phone_number = input('Please, enter a phone number: ')
        print(f'The name of the person is {name} \n The contact for {name} is {phone_number}')
        self.save() 

    def start(self):
        # print("Press key -h for help")
        while True:
            self.keys.key_check()
            

if __name__ == '__main__':
    b = Book()
    b.start()



    

        
