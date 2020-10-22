with open("text_6.txt", 'r', encoding="utf-8") as file:
    output_dict = {}
    for el in file.readlines():
        el = el.replace("\n", "")
        el = el.replace("(пр)", "")
        el = el.replace("(лаб)", "")
        el = el.replace("(л)", "")
        el = el.replace("-", "0")
        el = el.split()
        over = [int(el[1]), int(el[2]), int(el[3])]
        over = sum(over)
        output_dict[el[0]] = over
print(output_dict)
