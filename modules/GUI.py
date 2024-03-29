import time
import os
import colorama

def clear_screen():
    """Cls, qui permet de clearscreen sur le cmd sur windows, implémenté sur python !"""
    os.system('cls' if os.name == 'nt' else 'clear')  # marche même sur linux


def wait():
    """Fonction qui permet de faire une pause, et de demander à l'utilisateur de continuer"""
    input('Appuyez sur entrée pour continuer...')
    clear_screen()


def attend(temps=1.5):
    time.sleep(temps)


def header(couleur, titre):
    try:
        terminal_size = os.get_terminal_size()  # récupère la taille du terminal via la librairie os
    except OSError:
        terminal_size = (100, 100)  # si erreur, on met une taille par défaut
    header_length = terminal_size[0] - 2

    left_margin = (header_length - len(titre)) // 2
    right_margin = header_length - len(titre) - left_margin

    header_roulette = (f'{getattr(colorama.Fore, couleur)}[{"-" * header_length}]{colorama.Style.RESET_ALL}\n'
                       f'{getattr(colorama.Fore, couleur)}{" " * left_margin}|{titre}|'
                       f'{" " * right_margin}'f'{colorama.Style.RESET_ALL}\n'
                       f'{getattr(colorama.Fore, couleur)}[{"-" * header_length}]{colorama.Style.RESET_ALL}')
    print(header_roulette)
    print("\n")


def options_listees(*options):
    print("\n\n")
    for i, option in enumerate(options, 1):
        print(f'{i}) {option}')
    print()


def menu_principal():
    C118 = ('\n'
            '    [-----------------------------------------------------------------------------]\n'
            '               B i e n v e n u e   a u   C a s i n o   d e   l a   C 1 1 8 ...        \n'
            '                        ________  _____    _____  ________     \n'
            '                        |\   ____\/ __  \  / __  \|\   __  \    \n'
            '                        \ \  \___|\/_|\  \|\/_|\  \ \  \|\  \   \n'
            '                         \ \  \  \|/ \ \  \|/ \ \  \ \   __  \  \n'
            '                          \ \  \____  \ \  \   \ \  \ \  \|\  \ \n'
            '                           \ \_______\ \ \__\   \ \__\ \_______|\n'
            '                            \|_______|  \|__|    \|__|\|_______|\n'
            '                            \n'
            '    [-----------------------------------------------------------------------------]\n')
    print(C118)  # logo du casino avec message de bienvenue


def body(couleur, texte):
    try:
        terminal_size = os.get_terminal_size()  # récupère la taille du terminal via la librairie os
    except OSError:
        terminal_size = (100, 100)  # si erreur, on met une taille par défaut
    header_length = terminal_size[0] - 2

    for ligne in texte:
        left_margin = (header_length - len(ligne)) // 2
        right_margin = header_length - len(ligne) - left_margin

        body_line = (f'{getattr(colorama.Fore, couleur)}|{" " * left_margin}{ligne}'
                     f'{" " * right_margin}|{colorama.Style.RESET_ALL}')
        print(body_line)

    print("\n")


def body_game_over():
    GAME_OVER = ('\n'
                 '┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n'
                 '███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n'
                 '██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n'
                 '██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n'
                 '██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n'
                 '███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n'
                 '┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n'
                 '███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n'
                 '██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n'
                 '██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n'
                 '██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n'
                 '███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄\n'
                 '\n')
    print(GAME_OVER)