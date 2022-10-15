# Для более удобной отладки
def unbleach(n: str) -> str:
    """Преобразует строку языка Whitespace в последовательность вида sstntn"""
    return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')


# Whitespace Interpreter
def whitecpace(code: str, inp :str = '') -> str:
    output = ''
    stack = []
    heap = {}


print("***", unbleach("  \t\n\t\t  "), "***")