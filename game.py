import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length):
        self.length = length
        self.words = [word for word in WORDS if len(word) == length]

        if not self.words:
            raise ValueError(f"No words available for {length}-letter mode.")

        self.target = random.choice(self.words)
        self.history = []

    def show_history(self):
        if not self.history:
            return

        print("\nGuess history:")
        for guess, feedback in self.history:
            print(f"{guess}: {' '.join(feedback)}")
        print()

    def run(self):
        print(f"Wordle — {self.length}-letter mode, 6 guesses.")
        print("Enter 'q' to quit.")

        attempts = 0

        while attempts < 6:
            guess = input("> ").strip().lower()

            if guess == "q":
                print("\nGame summary")
                print("Result: Quit")
                print(f"Guesses used: {attempts}")
                self.show_history()
                return

            if len(guess) != self.length or not guess.isalpha():
                print(f"Enter a valid {self.length}-letter word.")
                continue

            attempts += 1

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print(" ".join(feedback))
            self.show_history()

            if guess == self.target:
                print("Game summary")
                print("Result: Won")
                print(f"Guesses used: {attempts}")
                return

        print("Game summary")
        print("Result: Lost")
        print(f"Guesses used: {attempts}")
        print(f"Target word: {self.target}")
        self.show_history()


def choose_mode():
    while True:
        choice = input("Choose word length (4, 5, or 6): ").strip()

        if choice in ("4", "5", "6"):
            return int(choice)

        print("Please choose 4, 5, or 6.")


if __name__ == "__main__":
    length = choose_mode()
    game = WordleGame(length)
    game.run()