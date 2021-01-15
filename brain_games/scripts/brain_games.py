#!/usr/bin/env python
from brain_games import cli


def greet(where):
    print('Welcome {}!'.format(where))


def main():
    greet('to the Brain Games')
    cli.welcome_user()


if __name__ == '__main__':
    main()
