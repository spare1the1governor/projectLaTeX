from functions import create_latex_document, delete_file

def I_want_green(text):
    '''позволяет любое слово перед которым стоит 
    слово 'green'
    выделить зелёным цветом '''
    # Разбиваем текст на список слов
    l_text = list(text.split(" "))
    # Проходим по каждому слову и выполняем нужную замену
    i = 0
    while i < len(l_text): 
        if l_text[i] == 'green':  # Если нашли слово 'green'
            if i + 1 < len(l_text):
                l_text[i] = '{\\' + l_text[i] + ' ' + l_text[i+1] + '}'
                # Удаляем следующее слово из списка, так как оно уже добавлено в фигурные скобки
                del l_text[i+1]
            i += 1  # Переходим к следующему слову
        else:
            i += 1  # Просто двигаемся по списку 
    # Возвращаем изменённую строку
    modified_text = " ".join(l_text)
    return modified_text

# Запрос для пользователя с циклом для повторного ввода
while True:
    user_input = input('Вы хотите создать или удалить файл? (введите "создать", "удалить" или "выход"): ').strip().lower()
    
    if user_input == 'создать':  
        title = input('Заголовок: ')
        author = input('Автор: ')
        date = input('Дата: ')
        office = input('Название и город издательства: ')
        section = input('Раздел: ')
        subsection = input('Подраздел: ')
        text = input('Основной текст: ')
        modified_text = I_want_green(text)
        # Вызов функции для создания LaTeX документа
        create_latex_document(title, author, date, office, section, subsection, modified_text)
    
    elif user_input == 'удалить':
        delete_file()  # Вызываем функцию для удаления файла
    
    elif user_input == 'выход':
        print("Выход из программы.")
        break  # Выход из цикла, программа завершена

    else:
        print("Неверный ввод. Пожалуйста, введите 'создать', 'удалить' или 'выход'.")


