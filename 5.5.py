with open("text_5.txt", 'x+', encoding="utf-8") as file:
    while True:
        user_input = input("Введите данные: ")
        if user_input == "":
            break
        else:
            file.write(f"{int(user_input)} ")
with open("text_5.txt", 'r', encoding="utf-8") as file:
    content = file.read().split()
out_content = []
for i in content:
    out_content.append(int(i))
out_content = sum(out_content)
print(f"Суммва чисел равна: {out_content}")
