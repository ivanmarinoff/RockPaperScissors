import random

from game_symbols import GameSymbols


class Player(GameSymbols):
    while True:

        player_move = input("Choose [✊r]ock, [✋p]aper or [✌s]cissors: ")
        if player_move.lower() in GameSymbols.rock_list:
            player_move = GameSymbols.rock
        elif player_move.lower() in GameSymbols.paper_list:
            player_move = GameSymbols.paper
        elif player_move.lower() in GameSymbols.scissors_list:
            player_move = GameSymbols.scissors
        else:
            raise SystemExit("Invalid Input. Try again...")

        computer_random_number = random.randint(1, 3)
        computer_move = ""
        if computer_random_number == 1:
            computer_move = GameSymbols.rock
        elif computer_random_number == 2:
            computer_move = GameSymbols.paper
        else:
            computer_move = GameSymbols.scissors
        print(f"The computer choose {computer_move}.\n\n")

        if (player_move == GameSymbols.rock and computer_move == GameSymbols.scissors) \
                or (player_move == GameSymbols.paper and computer_move == GameSymbols.rock) \
                or (player_move == GameSymbols.scissors and computer_move == GameSymbols.paper):
            print("🎉🌟 𝒴ℴ𝓊 𝒲𝒾𝓃! 🌟🎉")
            GameSymbols.count_player_wins += 1
            print(
                f"\n\nPlayer -> {GameSymbols.count_player_wins} wins : Computer -> {GameSymbols.count_computer_wins} wins\n\n")
        elif player_move == computer_move:
            print("🙏 𝒟𝓇𝒶𝓌! 🙏")
            continue
        else:
            print("💥 𝒴ℴ𝓊 ℒℴ𝓈ℯ! 💥")
            GameSymbols.count_computer_wins += 1
            print(
                f"\n\nPlayer -> {GameSymbols.count_player_wins} wins : Computer -> {GameSymbols.count_computer_wins} wins\n\n")
