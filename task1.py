#Запись рецептов из файла в словарь
def read_recipes_to_dict(file):
    dict = {}
    prev_line_is_empty = False
    #Читаем файл до конца (или до двух пустых строк между блюдами)
    while True:
        dish = file.readline().strip()
        #Проверка на конец файла (есть ли дальше название блюда)
        if dish == "":
            if prev_line_is_empty == True:
                break
            else:
                prev_line_is_empty = True
                continue
        else:
            prev_line_is_empty = False
        #если ещё нет такого блюда в словаре, то добавляем его
        if dict.get(dish) == None:
            dict[dish] = []
            #узнаём, сколько у блюда ингредиентов, добавляем их в словарь
            ingredient_amount = int(file.readline().strip())
            for i in range(ingredient_amount):
                s_ingr = file.readline().strip()
                # TODO----------------------пока просто сохраняю строку по ключу-------------------------
                dict[dish].append(s_ingr)
        #если блюдо уже есть, то не сохраняем новых данных
        else:
            ingredient_amount = int(file.readline().strip())
            for i in range(ingredient_amount):
                file.readline()
    return dict

#название файла с рецептами (тут подразумевается, что он в папке с программой)
file_recipes = "recipes.txt"

with open(file_recipes) as file:
    cook_book = (read_recipes_to_dict(file))
    print(cook_book)

#тестирование - с повторяющимся элементом и с двумя пустыми строками
file_recipes = "recipes_test.txt"
with open(file_recipes) as file:
    cook_book = (read_recipes_to_dict(file))
    print("----------\n", cook_book)