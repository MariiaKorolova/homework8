#Функции в отдельном модуле, проверка работоспособности в main
#1. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.

my_list = ["Summer", "Autumn", "Winter", "Spring"]
def standard (my_list):
    result = []
    name = 'test'
    for index in range(len(my_list)):
        if index % 2:
            result.append(my_list[index][::-1])
        else:
            result.append(my_list[index])
    return result, name
print(standard(["Summer", "Autumn", "Winter", "Spring"]))

#2. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list у которых первый символ - буква "a".

list_with_names = ["Tim", "Boris", "Masha", "Andrey", 'Nastya']
names = []
for name in list_with_names:
    if name.lower().startswith("a"):
        names.append(name)
print(*names)
my_names = [name for name in list_with_names if name.lower().startswith("a")]
print(*my_names)

#3. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["Mariia", "Vasya", "Igor", "Peter", 'Sandra']
names = []
for name in my_list:
    if 'A' in name.upper():
        names.append(name)
print(*names)

#4. Написать функцию которой передается один параметр - список строк my_list в
котором могут быть как строки (type str) так и целые числа (type int).
Функция возвращает новый список в котором содержаться только строки из my_list.

my_list = [100, 200, 300, 400, 500, "1", "2", 600]
print(set(my_list))
my_list.insert(0, "OBJECT")
print(my_list[::])
result = []
for numbers in my_list:
    if type(numbers) == str:
        result.append(numbers)
print(result)

#5. Написать функцию которой передается один параметр - строка my_str.
Функция возвращает новый список в котором содержаться те символы из my_str,
которые встречаются в строке только один раз.

my_str = "hello"
my_set = set(my_str)
my_list = []
for letter in my_set:
    if my_str.count(letter) == 1:
        my_list.append(letter)
print(my_list)

#6. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.

str1_ = "Good morning"
str2_ = "Good evening"
print(list(set(str1_ + str2_)))

#7. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.

my_list1 = [22, 34, 61, 9, 125]
my_list2 = [2, 3, 25]
print(list(set(my_list1).intersection(my_list2)))

#*8. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.