import os

class Keyboard():
    def __init__(self, show, save_file,add, remove, helpp, exiit) -> None:
        self.show = show
        self.exit = exiit
        self.save_file = save_file
        self.add = add
        self.remove = remove
        self.help = helpp

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