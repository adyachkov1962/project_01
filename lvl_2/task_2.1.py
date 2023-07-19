# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,


# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

list = [4,6,2,1,9,63,-134,566]         #-> max = 566, min = -134
def minimum(list):
    min_n = list[0]
    for i in list[1:]:     
        if i < min_n:
            min_n = i
    return min_n    

def maximum(list):
    max_n = list[0]
    for i in list[1:]:
          if i > max_n:
             max_n = i
    return max_n 
 
print(f'min = {minimum(list)}, max = {maximum(list)}')
