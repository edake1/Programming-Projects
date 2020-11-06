from random import randint

print('W  E  L  C  O  M  E      T  O')
print('*****' * 6 + '*')
print('*****ROCK, PAPER, SCISSORS*****')
print('*****' * 6 + '*')

t = ['Rock', 'Paper', 'Scissors']
computer = t[randint(0, 2)]
player = False


while player == False:
    player = input('Rock[R], Paper[P], Scissors[S]?')

    if player.lower() == computer.lower():
        print('TIE!')
    elif player.lower() == 'rock':
        if computer.lower() == 'paper':
            print('You lose', computer, 'covers', player)
        else:
            print('YOU WIN!!', player, 'smashes', computer)

    elif player.lower() == 'paper':
        if computer.lower() == 'rock':
            print('You lose', computer, 'smashes', player)
        else:
            print('YOU WIN!', player, 'covers', computer)

    elif player.lower() == 'paper':
        if computer.lower() == 'scissors':
            print('You lose', computer, 'cuts', player)
        else:
            print('YOU WIN!!', player, 'covers', computer)

    elif player.lower() == 'scissors':
        if computer.lower() == 'rock':
            print('You lose.....', computer, 'smashes', player)
        else:
            print('YOU WIN!!!', player, 'cuts', computer)

    elif player.lower() == 'rock':
        if computer.lower() == 'scissors':
            print('You lose....', computer, 'tries to cut', player)
        else:
            print('YOU WIN!!', player, 'smashes', computer)

    elif player.lower() == 'scissors':
        if computer.lower() == 'paper':
            print('You lose....', computer, 'covers', player)
        else:
            print('YOU WIN!', player, 'cuts', computer)
    else:
        print('That is not a valid play! Check you spelling')

    player = False
    computer = t[randint(0, 2)]
