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

    items = [i for i in items if i != '']

    if header_rows > 0:
        items = items[header_rows:]

    if not data_type:
        data_type = 'string'

        try:
            _ = float(items[0])
            data_type = 'number'

        except ValueError:
            pass

    items = ",".join([f"'{i}'" for i in items])

    if data_type == 'number':
        items = re.sub("'", "", items)

    pyperclip.copy(items)
