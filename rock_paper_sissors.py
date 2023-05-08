from RockPaperScissors.game_symbols import GameSymbols


class Game:
    while True:
        command = input("Type [𝒀𝒆𝒔✔️] to Play Again or [𝒩ℴ❌️] to quit❓: ")
        if command.lower() in GameSymbols.yes_list:
            continue
        elif command.lower() in GameSymbols.no_list:
            print("""
    
                    🙏THANK✌️➡YOU✋➡FOR➡✊PLAYING!🙏
            """)
            break
        else:
            raise SystemExit("Invalid Input. Try again...")
