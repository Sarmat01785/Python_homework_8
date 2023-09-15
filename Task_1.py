"""
                               Задача 38:
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать
функционал для изменения и удаления данных и поиска по фамилии.
"""

import codecs
from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = input("Введите номер телефона: ")
            if len(phone_number) != 11:
                print("Неправильный номер")
            else:
                flag = True
        except ValueError:
            print("Неправильный номер")
    info.append(phone_number)
    return info



def create_file():
    with open("phone.csv", "w", encoding="utf-8") as data:
        f_n_writer = DictWriter(data, fieldnames=["Фамилия", "Имя", "Номер"])
        f_n_writer.writeheader()
        
        
def write_file(lst):
    with open("phone.csv", "r+", newline='', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=["Фамилия", "Имя", "Номер"])
        for el in res:
            f_n_writer.writerow(el)
            
            
def read_file(file_name):
    with open(file_name, encoding='utf-8', errors='ignore') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def record_info():
    lst = get_info()
    write_file(lst)
    
    
def search_and_delete_contact():
    