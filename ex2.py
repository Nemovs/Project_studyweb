import csv
list1 = ['Звездные войны', 'Терминатор', 'Искуственный интеллект']
list2 = ['Дурак', 'Матильда', 'Левиафан']
list3 = ['Люди в черном', 'Я - робот', 'Эволюция']
list_all = [list1, list2, list3]

with open("st.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerows(list_all)

with open("st.csv", "r") as f:
    print(f.read())


'''while True:
    with open("poem.txt", "w") as f:
        x = input('Введите что записать в файл:')
        f.write(f"{x}")

    with open("poem.txt", "r") as f:
        text = f.read()

    my_list.append(text)
    print(my_list)
    '''





