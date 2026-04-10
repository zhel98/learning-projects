from colorama import init, Fore, Back, Style

def main():
    init(autoreset=True)

    print(Fore.RED + "This is red text")
    print(Fore.GREEN + "This is green text")
    print(Fore.YELLOW + "This is yellow text")
    print(Fore.CYAN + "This is cyan text")

    print(Back.BLUE + "Text with a blue background")
    print(Fore.WHITE + Back.MAGENTA + "White text on magenta background")

    print(Style.DIM + "Dim text")
    print(Style.BRIGHT + "Bright text")

if __name__ == "__main__":
    main()