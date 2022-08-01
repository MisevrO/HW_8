import random


def validate_user_input(user_input):
    if user_input.isdecimal():
        return int(user_input) in (1, 2, 3)
    else:
        return False


def want_play_again():
    while True:
        play_again = input("Бажаєте продовжити (Y \ N): ")
        if play_again.upper() == 'Y':
            return True
        elif play_again.upper() == 'N':
            return False
        else:
            print("Невірний формат вводу.")


def player_input():
    """УМОВА"""
    while True:
        user_input = input("Зробіть вибір: 1 (камінь), 2 (ножиці), 3 (папір): ")
        if validate_user_input(user_input):
            break
        print("Невірний формат вводу - має бути 1, 2 або 3")

    user_input = int(user_input)
    if user_input == 1:
        print("Ви обрали камінь.")
    elif user_input == 2:
        print("Ви обрали ножиці.")
    elif user_input == 3:
        print("Ви обрали папір.")
    return user_input


def comp_input():
    """Рандомній вибір"""
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        print("Компьютер обрав камінь.")
    elif comp_choice == 2:
        print("Компьютер обрав ножиці.")
    elif comp_choice == 3:
        print("Компьютер обрав папір.")
    return comp_choice


def game_result(player_choice, comp_choice):
    """Обираємо переможця"""
    if player_choice == comp_choice:
        print("Нічия!")
        return 0
    elif (player_choice == 1 and comp_choice == 2) or\
         (player_choice == 2 and comp_choice == 3) or\
         (player_choice == 3 and comp_choice == 1):
        print("Ви перемогли!")
        return 1
    elif (player_choice == 1 and comp_choice == 3) or\
         (player_choice == 2 and comp_choice == 1) or\
         (player_choice == 3 and comp_choice == 2):
        print("Переміг компьютер!")
        return 2
