lang_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4.txt", 'r', encoding="utf-8") as file:
    content = file.readlines()
ass = []
for el in content:
    ass.append(el.replace("\n", ""))
print(ass)
