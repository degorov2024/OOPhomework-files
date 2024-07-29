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
            set_ingredients = set() #множество ингредиентов этого блюда
            for i in range(ingredient_amount):
                #выделяем из строки данные - название, кол-во и ед. измерения 
                l_ingr = (file.readline().strip()).split(' | ')
                #если ингредиент не дублируется в описании этого блюда
                if l_ingr[0] not in set_ingredients:
                    d_ingr = {'ingredient_name':l_ingr[0], 'quantity':l_ingr[1],
                              'measure':l_ingr[2]}
                    dict[dish].append(d_ingr)
                    set_ingredients.add(l_ingr[0])
        #если блюдо уже есть, то не сохраняем новых данных
        else:
            ingredient_amount = int(file.readline().strip())
            for i in range(ingredient_amount):
                file.readline()
    return dict

#Подсчёт ингредиентов на количество персон (задание 2)
def get_shop_list_by_dishes(dishes, person_count):
    #Исходя из ответов аспирантов в "Вопросы и ответы", в задаче 
    #подразумевается использование глобальной переменной, а не аргумент функции
    #Словарь с рецептами из Задания 1
    global cook_book
    result = {}
    for dish in dishes:
        #если в "кулинарной книге" есть это блюдо (иначе пропускаем его)
        if cook_book.get(dish) != None:
            for ingredient_d in cook_book[dish]:
                if result.get(ingredient_d['ingredient_name']) == None:
                    result[ingredient_d['ingredient_name']] = {
                        'measure':ingredient_d['measure'], 
                        'quantity':(int(ingredient_d['quantity']) * 
                                    person_count)}
                #когда мы уже используем этот ингредиент при приготовлении
                #другого блюда и надо их просуммировать
                else:
                    result[ingredient_d['ingredient_name']]['quantity'] += (
                        (int(ingredient_d['quantity']) * person_count))
    return result

#название файла с рецептами (тут подразумевается, что он в папке с программой)
file_recipes = "recipes.txt"

with open(file_recipes) as file:
    cook_book = (read_recipes_to_dict(file))
    print(cook_book)

print('----------\n',
      get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

print('----------\n',
      get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))