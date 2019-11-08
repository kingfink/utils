import pyperclip
import re


def replace_model_references(schema):
    query = pyperclip.paste()

    query = re.sub(r"{{ ref\('", f"{schema}.", query)
    query = re.sub(r"'\) }}", "", query)

    pyperclip.copy(query)
    print(query)


def format_list(data_type):
    list = pyperclip.paste()
    pyperclip.copy(list)
    print(list)
