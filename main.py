import fnmatch
import os
from pprint import pprint

DIR_PATH = os.getcwd()


def sorting_files():
    files = fnmatch.filter(os.listdir(DIR_PATH), '*.txt')
    count_list = []
    files_dict = {}
    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        with open(file_path, encoding='utf-8') as f:
            count = 0
            for line in f:
                count += 1
        with open(file_path, encoding='utf-8') as f:
            files_dict[count] = [file, f.readlines()]
        count_list.append(count)
    count_list.sort()
    with open('result.txt', 'a', encoding='utf-8') as file_result:
        for number, file_struct in sorted(files_dict.items()):
            text = ''.join(file_struct[1])
            file_result.write(f'{file_struct[0]}\n{number}\n{text}\n\n')
    pprint(files_dict)


sorting_files()
