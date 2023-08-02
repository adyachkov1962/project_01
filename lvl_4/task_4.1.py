# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)
import sqlite3 as sq
import pandas as pd
con = sq.connect('teachers.db')
cur = con.cursor()
con.execute("""CREATE TABLE IF NOT EXISTS Students(
    Student_Id INT, Student_Name TEXT, School_Id INT PRIMARY kEY); """)
con.commit()

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4
stud_list = ((201, 'Иван', 1), (202, 'Петр', 2), (203, 'Анастасия', 3), (204, 'Игорь', 4))
cur.executemany("REPLACE INTO Students VALUES(?, ?, ?);", stud_list)
con.commit()
cur.execute("SELECT * FROM Students;")
many_result = cur.fetchall()
print(many_result)

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

def request_stud_id(id_stud):
  try: 
    result = cur.execute('SELECT * FROM students '
        'JOIN School ON School.School_id = students.school_id '
        'WHERE student_id =?', [id_stud]).fetchone()
    print(f' ID Студента: {result[0]}\n Имя студента: {result[1]}\n' 
          f' ID школы: {result[2]}\n Название школы: {result[4]}\n')

  except (Exception, sq.Error):
    print ('Студента с таким ID нет')      
request_stud_id(203)
