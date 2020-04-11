from nameko.rpc import rpc
import os


def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('####################')
    print('#    Main Menu     #')
    print('####################')
    print()
    print('1) View Show Times')
    print('2) Pick Your Seat')
    print('3) Movie Info')

    choice = input('\nPlease enter your selection: ')


main_menu()
