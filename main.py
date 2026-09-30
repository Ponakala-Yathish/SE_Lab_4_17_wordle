from game import WordleGame, choose_mode

if __name__ == "__main__":
    length = choose_mode()
    game = WordleGame(length)
    game.run()
