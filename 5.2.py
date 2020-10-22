with open("text_2.txt", 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines_quant = len(lines)
print(f"Текст содержит: {len(lines)} строк")
for i in enumerate(lines, 1):
    a = list(i[1])
    print(f"Строка {i[0]} содержит {len(a)} символов")
