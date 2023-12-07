# Python clitools
This package removes annoying boilerplate code that you will see you write yourself over and over again to create a pleasant cli-centered user interface.

[![Downloads](https://static.pepy.tech/badge/JefvdA-python_clitools)](https://pepy.tech/project/JefvdA-python_clitools)
[![GitHub issues](https://img.shields.io/github/issues-raw/JefvdA/python_clitools)](https://github.com/JefvdA/python_clitools/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/JefvdA/python_clitools)](https://github.com/JefvdA/python_clitools/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub contributors](https://img.shields.io/github/contributors-anon/JefvdA/python_clitools)](https://github.com/JefvdA/python_clitools/graphs/contributors)
[![PyPI](https://img.shields.io/pypi/v/JefvdA-python-clitools)](https://pypi.org/project/JefvdA-python-clitools/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/JefvdA/python_clitools)](https://github.com/JefvdA/python_clitools/releases)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/JefvdA/python_clitools/blob/main/LICENCE.md)

* [Installation](#installation)
* [Tools](#tools)
* [Menu](#menu)

# Installation
For more information, check out the [PyPi page](https://pypi.org/project/JefvdA-python-clitools/)

to install the newest version, use:
```
pip install JefvdA-python-clitools
```

# Tools
Methods that are used most-often. <br>
These include:
* **clear()** -> OS independant method to clear the terminal
* **wait_for_enter()** -> method to wair for user input before continuing, clears the screen after
* **get_user_input()** -> method to returns user input. This method formats the text printed for the input to add " >>> " after it. Example: "What is your name?", becomes, "What is your name? >>> "

The 'tools' module also consists of the "Menu" class, read more about that below.
## Menu
A "Menu" class that makes it very easy to display a menu in the terminal, and have different results for all the options the user can choose from.

When initiating a new "Menu" object, make sure to pass it all the options, aswell as their corresponding fucntions. <br>
Example:
```python
menu_options = {
    "Hello world": say_hello_world,
    "Greet by name": ask_for_name,
    "Get random number": get_random_number,
    "Exit": exit
}
menu = Menu(menu_options)
```

When a "Menu" option is created, it can be displayed with the "show()" method.
```python
menu.show()
```
*This will only run the menu once, if you wish to keep displaying the menu. Wrap the "show" in a while loop + add an option to exit the program*
