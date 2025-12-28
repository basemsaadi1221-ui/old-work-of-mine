import random

def play():
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()

        if user != 'r' and user != 'p' and user != 's':
            print("please enter a valid choice")
            continue
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            print(f"computer chose {computer}")
            return 'it\'s a tie'
        elif is_win(user, computer):
            print(f"computer chose {computer}")
            return 'you won'
        else:
            print(f"computer chose {computer}")
            return 'you lost'
    


def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" \
                                                                                      and opponent == "r"):
        return True

print(play())