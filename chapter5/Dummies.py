the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def pretty_print():
    import pprint
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for char in message:
        count.setdefault(char, 0)
        count[char] = count[char] + 1

    pprint.pprint(count)


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def play():
    turn = 'X'
    for i in range(9):
        print_board(the_board)
        print("Turn for " + turn + '. Move on which space?')
        move = input()
        the_board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
        return num_brought
