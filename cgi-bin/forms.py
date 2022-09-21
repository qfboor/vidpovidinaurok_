#!usr/bin/env python 3


import cgi


form = cgi.FieldStorage()
user_grade = form.getfirst('user_grade', 'Не задано')
number_of_questions = form.getfirst('user_question', 'Не задано')
print('Content-type: text/html')
print()
print(user_grade)