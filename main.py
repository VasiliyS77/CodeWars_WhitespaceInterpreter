# Для более удобной отладки
def unbleach(s: str) -> str:
    """Преобразует строку языка Whitespace в последовательность вида sstntn"""
    return s.replace(' ', 's').replace('\t', 't').replace('\n', 'n')


def delete_comments(s: str) -> str:
    """Удаление комментариев
    (оставляются только символы табуляции, перевода строки и пробел"""
    key_words = ['\t', '\n', ' ']
    code = [ch for ch in s if ch in key_words]
    return ''.join(code)


# Whitespace Interpreter
def whitecpace(code: str, input :str = '') -> str:
    """Интерпретация строки
    code - команды интерпретатора
    input - входные данные
    """
    # Выходные данные
    output = ''
    # Стек
    stack = []
    # Куча
    heap = {}

    # Удаляем комментарии
    instructions = delete_comments(code)

    while instructions:

        if instructions[0] == ' ':
            # Операции со стеком (Stack Manipulations)
            instructions = instructions[1:]
            pass
            continue

        if instructions[0:2] == '\t ':
            # Арифметические операции (Arithmetic)
            instructions = instructions[2:]
            pass
            continue

        if instructions[0:2] == '\t\t':
            # Операции с кучей (Heap Access)
            instructions = instructions[2:]
            pass
            continue

        if instructions[0:2] == '\t\n':
            # Ввод/Вывод (Input/Output)
            instructions = instructions[2:]
            pass
            continue

        if instructions[0] == '\n':
            # Управляющая конструкция (Flow Control)
            instructions = instructions[1:]
            pass
            continue

    return output


ex = "   \t \n\t\n \t\n\n\n"
print(unbleach(delete_comments(ex)))
print(whitecpace(ex))