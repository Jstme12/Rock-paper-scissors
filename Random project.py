import random

def play():
    while True:
        # Get player move
        player_move = input("Enter your move (rock, paper, scissors): ")
        # Get AI move
        ai_move = random.choice(['rock', 'paper', 'scissors'])
        print("AI chose: ", ai_move)
        result = game_over(player_move, ai_move)
        if result != 'Invalid':
            print(result)
            break

def game_over(player_move, ai_move):
    if player_move == ai_move:
        return 'Tie'
    elif player_move == 'rock':
        if ai_move == 'scissors':
            return 'Player wins!'
        else:
            return 'AI wins!'
    elif player_move == 'scissors':
        if ai_move == 'paper':
            return 'Player wins!'
        else:
            return 'AI wins!'
    elif player_move == 'paper':
        if ai_move == 'rock':
            return 'Player wins!'
        else:
            return 'AI wins!'
    else:
        return 'Invalid'

if __name__ == '__main__':
    play()
