import pyperclip


def replace_model_references(schema):
    query = pyperclip.paste()
    pyperclip.copy(query)
    print(query)


def format_list(data_type):
    list = pyperclip.paste()
    pyperclip.copy(list)
