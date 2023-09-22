import sys, os

class Keyboard():
    def __init__(self, add, remove, exit, help, save, show) -> None:
        self.add = add
        self.exit = exit
        self.remove = remove
        self.help = help
        self.save_file = save
        self.show = show
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