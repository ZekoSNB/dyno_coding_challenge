import sys

class Keyboard():
    def __init__(self, add, remove, exit) -> None:
        self.add = add
        self.exit = exit
        self.remove = remove
        super().__init__()

    def key_check(self):
        self.key_press = input("Enter a key -h for help: ")
        match self.key_press.lower():
            case 'add':
                self.add()
            case 'quit':
                sys.exit()
            case 'q':
                sys.exit()
            case 'exit':
                sys.exit()
            case 'remove':
                self.remove()
            case 'h':
                a = input("asdf= ")
                print(a)
                return 'neviem'
            case '-h':
                print("Type add to add people \n Type save to save to memory \n Type quit/exit to exit the script \n Type remove to Remove people from the list")