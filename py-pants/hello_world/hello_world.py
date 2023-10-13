from colorama import Fore, init
from hello_name import hello_name

init(autoreset=True)


def greet():
    return hello_name.greet("world")


def print_greet():
    print(Fore.CYAN + greet())
