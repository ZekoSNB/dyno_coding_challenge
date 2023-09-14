import csv



class Book():
    def __init__(self) -> None:
        self.dictionary = {}
        # print(str(Book) + ' initialized')

    def key_check(self):
        valid_inp = False
        self.key_press = input("Enter a key -h for help: ")
        print(self.key_press.lower)
        match self.key_press.lower():
            case 'add':
                name = input('Please etner a name: ')
                phone_number = input('Please, enter a phone number: ')
                print(f'The name of the person is {name} \n The contact for {name} is {phone_number}')
                while not valid_inp:
                    save = input('Is this correct and do you want to save this ? (y/yes or n/no): ')
                    if save == 'y' or save == 'yes':
                        print('ok, saved')
                        valid_inp = True
                    elif save == 'n' or save == 'no':
                        print('ok, not saving this time')
                        valid_inp = True
                    else:
                        print('please enter y/yes or n/no')
                        valid_inp = True
                
            case 'h':
                a = input("asdf= ")
                print(a)
                return 'neviem'
            case '-h':
                print("Type add to add people \n Type save to save to memory \n Type quit/exit to exit the script \n Type remove to Remove people from the list")


    def start(self):
        # print("Press key -h for help")
        while True:
            self.key_check()
            

if __name__ == '__main__':
    b = Book()
    b.start()



    

        
