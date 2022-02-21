class game:
    def __init__(self):
        f = open("wordlist.txt")
        self.words = f.read().split("\n")
        self.chosen_word = ""
        self.is_game_over = False


    def play(self):
        self.start()
        is_game_over = False
        guesses = 0
        while not is_game_over:
            print("give word")
            user_input = input()
            if user_input not in self.words or len(user_input) != 5:
                print("this is not a word!")
                continue
            
            if user_input == self.chosen_word:
                print("you win")
                exit(1)
            else:
                self.print_diff(user_input)
            guesses += 1
            if guesses >= 5:
                print("you lose")
                exit(1)


    def print_diff(self, guess):
        string = ""
        for i in range(len(self.chosen_word)):
            if guess[i] == self.chosen_word[i]:
                string += " " + guess[i] + " "
            else:
                # check if the letter appears elsewhere in the string
                if guess[i] in self.chosen_word:
                    string += " " + guess[i] + "* "
                else:
                    string += " _ "
        print(string)

    def start(self):
        self.chosen_word = self.words[0]
        print(self.chosen_word)




if __name__ == '__main__':
    g = game()
    g.play()
