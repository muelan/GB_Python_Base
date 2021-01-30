# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
#    выполнить подсчет количества строк, количества слов в каждой строке.

count_line = 0
#count_word = 0

with open('my_file_content_02.txt') as f_obj:
    print(f'Файл содержит {len(f_obj.readlines())} строк(и)')

with open('my_file_content_02.txt') as f_obj:
    for line in f_obj:
        count_line += 1
        count_word = len(line.split())
        print(f'В строке №{count_line} - {count_word} слов(а).')

