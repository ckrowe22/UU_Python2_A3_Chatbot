import string
import random


def random_choice_from_list(list):
    choice = list[random.randint(0, len(list) - 1)]
    return choice


def make_list_from_file(file):
    lines = []
    with open(file) as file_list:
        for line in file_list:
            lines.append(line)
    return lines


def convert_response_lines_into_dict(list):
    response_dict = {}
    for item in list:
        key, response = item.split(',')
        response_dict[key] = response
    return response_dict


class Chatter:
    def __init__(self, greeting, key_response, default):
        greetings_list = make_list_from_file(greeting)
        random_lines = make_list_from_file(default)
        keyword_list = make_list_from_file(key_response)
        self.greeting = greetings_list
        self.keyword_and_response = convert_response_lines_into_dict(keyword_list)
        self.default_responses = random_lines

    def greet(self):
        return random_choice_from_list(self.greeting)

    def respond(self, human_text):
        human_text = human_text.lower()
        human_text = human_text.translate(str.maketrans('', '', string.punctuation)).split()
        potential_resp = []
        for word in human_text:
            if word in self.keyword_and_response:
                potential_resp.append(self.keyword_and_response[word])

        if len(potential_resp) > 0:
            return random_choice_from_list(potential_resp)
        else:
            return random_choice_from_list(self.default_responses)


def main():
    # create chatbot
    bot = Chatter('greetings.txt', 'responses.txt', 'default sentences.txt')

    # print random greeting
    print(bot.greet())

    # while loop
    user_input = ""
    while user_input != 'stop':
        user_input = input().lower()
        if user_input == 'stop':
            print('Goodbye!')
        else:
            print(bot.respond(user_input))


if __name__ == '__main__':
    main()
