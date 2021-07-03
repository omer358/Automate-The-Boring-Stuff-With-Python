import pyperclip


def past_text_from_clipboard():
    return pyperclip.paste()


def stars_adder(text):
    text_list = text.split('\n')
    for i in range(len(text_list)):
        text_list[i] = "* "+text_list[i]
    pyperclip.copy('\n'.join(text_list))


stars_adder(past_text_from_clipboard())
