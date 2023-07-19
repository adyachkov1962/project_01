# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
def remove_exclamation_marks(s):
    s_del = s.replace('!', '')
    print(s_del)
remove_exclamation_marks("Hi! Hello") # вставка строки и вызов функции для примера


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
def remove_last_em(s):
    if s[-1] == '!':
        return s[:-1]
    else:
        return(s)
print(remove_last_em('!Hi!!')) # вставка строки и вызов функции для примера

   


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
def remove_word_with_one_em(s):
    list_1, list_2 = s.split(), []
    for i in range(len(list_1)):
        if list_1[i].count('!') != 1:
            list_2.append(list_1[i])           
    return list_2        
print(remove_word_with_one_em('hi! !hi! hi!')) # вставка строки и вызов функции для примера
# st = input('Введите строку: ')
# print(*remove_word_with_one_em(st))  # распаковываем список и выводим на печать 