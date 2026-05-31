import random

def start_game(): #Начало и конец игры
    print('🐂🐄🐂🐄🐂🐄 ================== Bulls & Cows ================== 🐂🐄🐂🐄🐂🐄\n')
    print('================================= Game Rules ==================================')
    print(' The computer guesses a 4-digit number, in which all the digits are different.\n'
          '                     Your task is to guess the number.\n'
          'After each attempt, the computer gives you a hint in the form of bulls and cows:\n'
          '               🐂 bull - a digit is guessed and stands in its place\n'
          '             🐄 cow - a digit is guessed but stands in a wrong place\n'
          '===============================================================================\n')
    print('Would you like to start?')
    start = choose_yes_no('Enter "Yes" or "No": ')
    if start in ('no', 'n'):
        return
    while True:
        play_game()
        again = choose_yes_no('Would you like to try again? Enter "Yes" or "No": ')
        if again in ('no', 'n'):
            break


def choose_yes_no(phrase):  # Обработка ответа пользователя
    while True:
        answer = input(phrase).strip().lower()
        if answer in ('yes', 'no', 'y', 'n'):
            return answer
        print('Please enter "Yes" or "No"')


def generate_number(): #Генерация загаданного числа
    while True:
        digits = random.sample('0123456789', 4)
        if digits[0] != '0':
            return ''.join(digits)


def choose_difficulty(): #Выбор уровня сложности
    while True:
        print('Choose difficulty level:')
        print('    Level 1 - 10 attempts')
        print('    Level 2 - 7 attempts')
        print('    Level 3 - 5 attempts')
        choice = input('Enter 1, 2 or 3: ').strip()
        #Проверка корректности выбора уровня сложности
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print('❗Incorrect option. Try again!')


def get_guess_number(): #Проверка корректности введенного пользователем числа
    while True:
        guess_number = input('Enter a 4-digit number: ').strip()
        if not guess_number.isdigit() or len(guess_number) != 4:
            print('❗Incorrect number option. Try again!')
            continue
        if guess_number[0] == '0':
            print('❗Incorrect number option. Try again!')
            continue
        if len(set(guess_number)) != 4:
            print('❗Incorrect number option. Try again!')
            continue
        return guess_number


def check(secret_number, guess_number): #Проверка на совпадение чисел и их мест
    bulls = 0
    cows = 0
    for i in range(4):
        if guess_number[i] == secret_number[i]:
            bulls += 1
        elif guess_number[i] in secret_number:
            cows += 1
    return bulls, cows


def play_game(): #Процесс игры
    secret_number = generate_number()
    attempts = choose_difficulty()
    for attempt_number in range(1, attempts + 1):
        attempts_left = attempts - attempt_number + 1
        print(f'📍You have {attempts_left} attempt(s) left.')
        guess_number = get_guess_number()
        bulls, cows = check(secret_number, guess_number)
        if bulls == 4:
            print('✨Congratulations!✨ You’ve found the right number! ✅')
            return
        else:
            print(f'Bulls: {bulls} Cows: {cows}\n')
    print(f'Attempts are over. 🙁 The right number is {secret_number}.\n'
          f'                 ❌ Game over ❌')

start_game()