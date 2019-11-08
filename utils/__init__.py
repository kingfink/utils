import pyperclip
import re


def replace_model_references(schema):
    query = pyperclip.paste()

    query = re.sub(r"{{ ref\('", f"{schema}.", query)
    query = re.sub(r"'\) }}", "", query)

    pyperclip.copy(query)


def format_list(data_type, header_rows):
    items = pyperclip.paste()

    items = items.split('\n')

    if header_rows > 0:
        items = items[header_rows:]

    if not data_type and type(items[0]) in(int, float):
        data_type = 'number'

    if data_type == 'string':
        items = ",\n".join([f"'{i}'" for i in items])[:-4]
        pyperclip.copy(items)

    items = ",\n".join([f"{i}" for i in items])[:-3]
    pyperclip.copy(items)
