# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
  if month in [1, 2, 3] :
    return 'первого'
  elif month in [4, 5, 6] :
    return 'второго' 
  elif month in [7, 8, 9] :
    return 'третьего'  
  else:
    return 'четвёртого'    

number = int(input('Введите номер месяца >  '))
while not 1 <= number <= 12 :
    print('Такого месяца нет!')
    number = int(input('Введите номер месяца >  '))           
 
month = [('январь'), ('февраль'), ('март'), ('апрель'), ('май'), ('июнь'),
          ('июль'), ('август'), ('сентябрь'), ('октябрь'), ('ноябрь'), ('декабрь')]

print(f'месяц {number} ({month[number - 1]}) является частью {quarter_of(number)} квартала')
