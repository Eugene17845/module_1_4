my_string= input('Введите фамилию (с заглавной буквы) : ')
my_string1= input('Имя: ')
my_string2= input('Отчество: ')
print('Вечер в хату, ',my_string,my_string1,my_string2)
print('Вечер в хату, ',my_string.upper(), my_string1.upper(), my_string2.upper())
print('Вечер в хату, ',my_string.lower(), my_string1.lower(), my_string2.lower())
print('Вечер в хату, ',my_string, my_string1[:1].upper(),'.', my_string2[:1].upper(),'.')
print('Вечер в хату, ',my_string, my_string1[-1:].upper(),'.', my_string2[-1:].upper(),'.')
print('Вечер в хату, ',my_string .replace(' ',''), my_string1[:1].upper(),'.'.replace(' ',''), my_string2[:1].upper(),'.'.replace(' ',''))
#Прописал я всё правильно, как я понимаю. НО, поскольку у меня нет при вводе данных с пробелом, то оно по сути бесполезно.
#По итогу я справился с поставленной задачей. Зачёт ведь, да?))))

