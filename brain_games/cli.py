import prompt


def welcome_user():
    name = prompt.string('What is your name? ')
    print('Hello, ' + name + '!')


if __name__ == '__welcome_user__':
    welcome_user()