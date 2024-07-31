#функция возвращает информацию о файле - словарь вида:
#{'name':<имя файла>, 'lines_amount':<к-во строк в файле>
def file_info(name, file):
    lines_amount = 0
    #считаем количество строк
    for line in file:
        lines_amount += 1
    return {'name':name, 'lines_amount':lines_amount}


#список файлов для задачи (лежат в той же папке, что и программа)
files = ['1.txt', '2.txt', '3.txt', 'empty_lines.txt']
#итоговый файл для объединения вышеупомянутых
result_file = "result.txt"
#узнаём количество строк данных файлов, записываем в список из словарей
files_info = []
for file_name in files:
    with open(file_name) as file:
        files_info.append(file_info(file_name, file))
#сортируем список по количеству строк в конкретном файле
files_info = sorted(files_info, key = lambda file_dict: 
                    file_dict['lines_amount'])

#создаём новый итоговый файл (если уже существует, то полностью перезапишется);
#записываем в него по очереди, в порядке количества строк:
#имя одного из файлов, кол-во строк, его содержимое
with open(result_file, mode = 'w') as file_1:
    for file_2_dict in files_info:
        file_1.write(file_2_dict['name'] + '\n')
        file_1.write(str(file_2_dict['lines_amount']) + '\n')
        with open(file_2_dict['name']) as file_2:
            file_1.write(file_2.read() + '\n')