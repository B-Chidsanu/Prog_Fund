import random
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
bot_card = []
player_card = []
game = True


def deal_card():
    global card
    dack = random.choice(card)
    return dack


def calculate_score(card):
    score = 0
    for dack in card:
        score += dack
    return score


def check_score(score):
    if score >= 21:
        return True


def check_ace(turn):
    if turn[0] == 11 and turn[1] == 10 or turn[0] == 10 and turn[1] == 11:
        return True
    else:
        return False


def compare(user_score, computer_score):
    total = 0
    if user_score > computer_score:
        total = 1
    elif computer_score > user_score:
        total = 2
    elif computer_score == user_score:
        total = 3
    return total


def check_bot_win():
    print(
        f"Computer cards: {bot_card} current score: {calculate_score(bot_card)}")
    print(
        f"Your cards: {player_card} current score: {calculate_score(player_card)}")
    print("Computer Win")


def check_player_win():
    print(
        f"Computer cards: {bot_card} current score: {calculate_score(bot_card)}")
    print(
        f"Your cards: {player_card} current score: {calculate_score(player_card)}")
    print("You Win")


while game:
    while True:
        play = input("Do you want to play a game of Blackjack? [Y/N]: ")
        player_card.clear()
        bot_card.clear()
        if play in "Nn":
            game = False
            break
        elif play in "Yy":
            bot_card.append(deal_card())
            bot_card.append(deal_card())
            check_ace_bot = check_ace(bot_card)
            player_card.append(deal_card())
            player_card.append(deal_card())
            check_ace_player = check_ace(player_card)

            if check_ace_bot == True:
                print(
                    f"Computer card: {bot_card} cerrent score: {calculate_score(bot_card)-10}")
                print(
                    f"Your card: {player_card} cerrent score: {calculate_score(player_card)}")
                print("Computer Win")
                break
            else:
                if check_ace_player == True:
                    print(
                        f"Your card: {player_card} cerrent score: {calculate_score(player_card)-10}")
                    print(
                        f"Computer card: {bot_card} cerrent score: {calculate_score(bot_card)}")
                    print("You Win")
                    break
                else:
                    print(f"Computer's first card: {bot_card[0]}")
                    print(
                        f"Your card: {player_card} cerrent score: {calculate_score(player_card)}")

            check = True
            while True:
                if (check):
                    draw_cards = input(
                        "Type 'y' to get another card, type 'n' to pass:")
                if draw_cards in "Yy":
                    player_card.append(deal_card())
                    if check_score(calculate_score(player_card)) == True:
                        break
                    elif calculate_score(player_card) == 21:
                        check_bot_win()
                        break
                    else:
                        print(f"Computer's first cards : {bot_card[0]}")
                        print(
                            f"You cards : {player_card} current score : {calculate_score(player_card)}")
                elif draw_cards in "Nn":
                    check = False
                    if calculate_score(bot_card) < 16:
                        bot_card.append(deal_card())
                    if check_score(calculate_score(bot_card)) == True:
                        check_player_win()
                        break
                    else:
                        if compare(calculate_score(player_card), calculate_score(bot_card)) == 1:
                            check_player_win()
                            break
                        elif compare(calculate_score(player_card), calculate_score(bot_card)) == 2:
                            check_bot_win()
                            break
                        elif compare(calculate_score(player_card), calculate_score(bot_card)) == 3:
                            print(
                                f"Computer cards : {bot_card} current score : {calculate_score(bot_card)}")
                            print(
                                f"You cards : {player_card} current score : {calculate_score(player_card)}")
                            print("Draw")
                            break
                        break
                else:
                    print("Error")
                    break
        else:
            print("Error")
            break
        if play in "Nn":
            break
