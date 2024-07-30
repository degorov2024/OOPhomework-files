#функция возвращает информацию о файле - словарь вида:
#{'name':<имя файла>, 'lines_amount':<к-во строк в файле>, 
# 'first_line':<1-ая строка>}
def file_info(name, file):
    #читаем первую строку
    first_line = file.readline().strip()
    lines_amount = 1
    #считаем оставшееся количество строк
    for line in file:
        lines_amount += 1
    return {'name':name, 'lines_amount':lines_amount, 'first_line':first_line}



files = ['1.txt', '2.txt', '3.txt', 'empty_lines.txt']
files_info = []         #---------------------а нужна ли глобальная переменная-------------------------
for file_name in files:
    with open(file_name) as file:
        files_info.append(file_info(file_name, file))
#сортируем информацию о файлах по количеству строк в конкретном файле
files_info = sorted(files_info, key = lambda file_dict: 
                    file_dict['lines_amount'])
print(files_info)

# files_info_sorted = sorted(files_info, key = lambda file_dict: file_dict['lines_amount'])
# print(files_info_sorted)