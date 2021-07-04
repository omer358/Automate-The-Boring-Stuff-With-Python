import itertools


def print_table(data):
    x, y, z = data
    for (a, b, c) in zip(x, y, z):
        print(str(a), b, c)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
print_table(tableData)
# apples  Alice  dogs
# oranges Bob    cats
# cherries Carol moose
# banana David goose
