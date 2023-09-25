import os
from file_work import Files

class Keyboard(Files):
    def __init__(self, help, exit) -> None:
        super().__init__
        self.exit = exit
        self.help = help
        os.system('clear')
        super().__init__()

    def key_check(self):
        self.key_press = input("Enter a key -h for help: ")
        match self.key_press.lower():
            case 'show':
                self.show()
            case 'list':
                self.show()
            case 'save':
                self.save_file()
            case 'add':
                self.add()
            case 'quit':
                self.exit()
            case 'q':
                self.exit()
            case 'exit':
                self.exit()
            case 'remove':
                self.remove()
            case 'help':
                self.help()
            case '--help':
                self.help()
            case '--h':
                self.help()
            case 'h':
                self.help()
            case '-h':
                self.help()
            case 'cls':
                os.system('clear')
            case 'clear':
                os.system('clear')