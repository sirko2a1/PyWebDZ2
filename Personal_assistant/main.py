import os
from abc import ABC, abstractmethod
from AdressBook.AB import main as ab_main
from NoteBook.NB import main as nb_main
from Map.Map import main as map_main
from sort.sort import main as sort_main
from Game.game import main as game_main

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])

class Menu(ABC):

    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def run_selected_option(self, choice):
        pass

class ConcreteMenu(Menu):

    def display_menu(self):
        cls()
        print('MENU')
        choice = input(
            'Вітаю, я ваш персональний помічник.\nОберіть функцію:\n1.Записна книжка\n2.Нотатник\n3.Карта\n4.Сортування папки\n5.Гра\n0.Вихід\n>>>')
        return choice

    def run_selected_option(self, choice):
        if choice == '1':
            cls()
            ab_main()
        elif choice == '2':
            cls()
            nb_main()
        elif choice == '3':
            cls()
            map_main()
        elif choice == '4':
            cls()
            sort_main()
        elif choice == '5':
            cls()
            game_main()

def main():
    concrete_menu = ConcreteMenu()
    while True:
        choice = concrete_menu.display_menu()
        if choice == '0':
            break
        concrete_menu.run_selected_option(choice)

if __name__ == '__main__':
    main()
