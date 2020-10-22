lang_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4.txt", 'r', encoding="utf-8") as file:
    content = []
    for el in file.readlines():
        content.append(el.split(" - "))
print(content)
output_content = []
for i in content:
    i[0] = lang_dict.get(i[0])
    output_content.append(' - '.join(i))
with open("text_new_4.txt", 'w', encoding="utf-8") as output_file:
    output_file.writelines(output_content)
