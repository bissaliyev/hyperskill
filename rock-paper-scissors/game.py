import random


class RockPaperScissors:


    def __init__(self, ratings_file='rating.txt'):
        self.ratings_file = ratings_file
        self.scores = {}
        self.options = {}
        self.load_all_scores()

    def load_options(self, options):
        if not options:
            self.options = {
                'rock': ['paper'],
                'scissors': ['rock'],
                'paper': ['scissors']
            }
        else:
            single_options_list = list(options.split(','))
            double_options_list = single_options_list * 2
            opponents_nums = len(single_options_list) // 2
            for idx in range(0, len(single_options_list)):
                self.options[double_options_list[idx]] = double_options_list[idx + 1: idx + 1 + opponents_nums]

    def load_all_scores(self):
        with open(file=self.ratings_file, mode='r', encoding='utf-8') as ratings:
            for line in ratings:
                name, score = line.split()
                self.scores[name] = int(score)

    def load_user_score(self, username):
        return self.scores[username] if username in self.scores else 0

    def save_user_scores(self):
        with open(file=self.ratings_file, mode='w+', encoding='utf-8') as ratings:
            for name, score in self.scores.items():
                ratings.write(f'{name} {score}\n')

    def add_new_user(self, username):
        self.scores[username] = 0

    def play(self):
        self.current_user_name = input("Enter your name:")
        self.scores[self.current_user_name] = self.load_user_score(self.current_user_name)
        print(f'Hello, {self.current_user_name}')
        options = input()
        self.load_options(options)
        print("Okay, let's start")
        while True:
            user_option = input()
            if user_option == '!exit':
                self.save_user_scores()
                print('Bye')
                break
            if user_option == '!rating':
                print(f'Your rating: {self.scores[self.current_user_name]}')
            if user_option not in self.options.keys():
                print('Invalid input')
            else:
                ai_option = random.choice(list(self.options.keys()))

                if user_option == ai_option:
                    self.scores[self.current_user_name] = self.scores[self.current_user_name] + 50
                    print(f'There is a draw {ai_option}')
                elif ai_option in self.options[user_option]:
                    print(f'Sorry, but the computer chose {ai_option}')
                else:
                    self.scores[self.current_user_name] = self.scores[self.current_user_name] + 100
                    print(f'Well done. The computer chose {ai_option} and failed')


game = RockPaperScissors()
game.play()