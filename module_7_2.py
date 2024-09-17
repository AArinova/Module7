
def custom_write( file_name, strings):

    with open( file_name, "w+", encoding='utf-8') as file:
        strings_positions = dict()
        index = 0
        for i_string in strings:
            index += 1
            current_position = file.tell()
            print(i_string, file=file)
            strings_positions[(index, current_position)] = i_string

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
 ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
