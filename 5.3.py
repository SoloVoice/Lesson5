with open("text_3.txt", 'r', encoding="utf-8") as file:
    unpack_content = list(file.readlines())
content = []
for i in unpack_content:
    content.append(i.replace("\n", "").split())
final_list = []
i = 0
for e in content:
    content[i][1] = float(content[i][1])
    i += 1
less20 = []
salary = []
for el in content:
    if el[1] < float(20000):
        less20.append(el[0])
    salary.append(el[1])
average_salary = sum(salary)/len(content)
print(f"Сотрудники имеющие оклад менее 20.000: {less20}")
print(f"Средняя зарплата составляет: {average_salary}")


