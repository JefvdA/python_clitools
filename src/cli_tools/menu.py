from tools import get_user_input, clear

class Menu():
    def __init__(self, options) -> None:
            self.option_texts = list(options.keys())
            self.option_functions = list(options.values())

    def add_option(self, text, function):
        self.option_texts.append(text)
        self.option_functions.append(function)

    def show(self):
        clear()
        print("Menu:")
        for i in range(len(self.option_texts)):
            print(str(i+1) + ": " + self.option_texts[i])
        choice = int(get_user_input("Select an option: "))
        self.option_functions[choice-1]()