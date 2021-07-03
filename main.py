# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: invalid input, can't divide by Zero")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from chapter6.project_chapter import pw
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
