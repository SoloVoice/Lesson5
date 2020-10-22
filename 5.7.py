import json
with open("text_7.txt", 'r', encoding="utf-8") as file:
    ltd_dict = {}
    avr_profit = 0
    profitable_companies = 0
    for el in file.readlines():
        el = el.replace("\n", "").split()
        profit = int(el[2])-int(el[3])
        ltd_dict[el[0]] = profit
        if profit > 0:
            avr_profit += profit
            profitable_companies += 1
avr_profit = avr_profit/profitable_companies
ltd_dict["Усредненная прибыль"] = avr_profit
print(ltd_dict)
with open("text_78.json", 'w', encoding="utf-8") as json_file:
    json.dump(ltd_dict, json_file, ensure_ascii=False)
