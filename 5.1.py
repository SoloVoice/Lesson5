with open("text_1.txt", 'x', encoding="utf-8") as file:
    while True:
        user_input = input("Введите данные: ")
        if user_input == "":
            break
        else:
            file.write(f"{user_input}\n")
