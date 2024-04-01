import random

options = ('piedra', 'papel', 'tijera')
player_score = 0
computer_score = 0

print('JUEGO DE PIEDRA, PAPEL Y TIJERA')

while player_score < 2 and computer_score < 2:
    print(' ')
    user_choice = input('Usuario Escoja una opción: piedra, papel o tijera: ').lower()
    if user_choice not in options:
        print('Opción no válida')
        continue

    computer_choice = random.choice(options)
    result = ''
    if user_choice == computer_choice:
        result = 'Empate'
    elif user_choice == 'piedra' and computer_choice == 'tijera':
        result = 'Usuario gana'
        player_score += 1
    elif user_choice == 'piedra' and computer_choice == 'papel':
        result = 'Computador gana'
        computer_score += 1
    elif user_choice == 'papel' and computer_choice == 'piedra':
        result = 'Usuario gana'
        player_score += 1
    elif user_choice == 'papel' and computer_choice == 'tijera':
        result = 'Computador gana'
        computer_score += 1
    elif user_choice == 'tijera' and computer_choice == 'papel':
        result = 'Usuario gana'
        player_score += 1
    elif user_choice == 'tijera' and computer_choice == 'piedra':
        result = 'Computador gana'
        computer_score += 1

    print('-' * 20)
    print('El usuario escogió:', user_choice)
    print('El pc escogió:', computer_choice)
    print(result)

if player_score == 2:
    print('El usuario es el vencedor')
else:
    print('El pc es el vencedor')