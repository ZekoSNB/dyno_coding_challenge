import csv, sys
from Keyboard import Keyboard

#* asdf
'''#TODO 
    - [ ] Saving to file
    - [ ] Removing user
    - [ ] User list
'''
class Book():
    def __init__(self) -> None:
        self.dictionary = []
        self.keys = Keyboard(self.add, self.remove, self.exit, self.help, self.save_file, self.show)
        self.saved_changes = True
        self.read_file()
    
    def is_int(self, num):
        try:
            num = int(num)
            return True
        except ValueError:
            return False

    def generate_ID(self, diff):
        id = len(self.dictionary) + diff
        print(id)
        if len(self.dictionary) != 0:
            for i in self.dictionary:
                # print(id , int(i[2]))
                if id == int(i[2]):
                    self.generate_ID(1)
            return id+1
        else:
            return id

    def show(self):
        for i in self.dictionary:
            print(f'The name is: {i[0]} and the number is {i[1]} Following ID is: {i[2]}')

    def read_file(self):
        with open('files/user.csv', 'r') as data:
            csv_read = csv.reader(data)
            for row in csv_read:
                self.dictionary.append(row)
            data.close()

    def save_file(self):
        with open('files/user.csv', 'w') as data:
            writer_obj = csv.writer(data)
            for i in self.dictionary:
                print(i)
                writer_obj.writerow(i)
            data.close()
            self.saved_changes = True

    def help(self):
        print("Type add to add people \n Type save to save to memory \n Type quit/exit to exit the script \n Type remove to Remove people from the list")

    def save(self, name, phone):
        return_state = False
        while not return_state:
            save = input('Is it correct and do you want to save this ? (y/yes or n/no): ')
            return_list = self.valid(save)
            return_state = return_list[0]
        
        if return_list[1]:
            id = self.generate_ID(0)
            print(id)
            self.dictionary.append([name, phone, id])
            self.saved_changes = False

        else:
            print('not saving to dict')


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
            aff = input('Do you really want to exit?: ')
            ret_list = self.valid(aff)
        if ret_list[1]:
            if not self.saved_changes:
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
        inp_ID = input('Enter a ID you want to remove (show to show ID):')
        if inp_ID == 'show':
            self.show()
            self.remove()
        
        if self.is_int(inp_ID):
            for i in self.dictionary:
                print(i[2] + inp_ID)
                if int(i[2]) == int(inp_ID):
                    self.dictionary.remove(i)
                    return
            print('Did not match an ID!')        
        else:
            print('enter a number!')
            self.remove()
        
    def add(self):
        name = input('Please etner a name: ')
        phone_number = input('Please, enter a phone number: ')
        print(f'The name of the person is {name} \n The contact for {name} is {phone_number}')
        self.saved_changes = False
        self.save(name, phone_number) 

    def start(self):
        while True:
            self.keys.key_check()
            

if __name__ == '__main__':
    b = Book()
    b.start()



    

        
