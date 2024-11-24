import os
def delete_file():
    """Удаляет файл, если он существует."""
    if os.path.exists('generated_document.tex'):
        os.remove('generated_document.tex')
        print("Файл generated_document.tex успешно удален.")
    else:
        print("Файл generated_document.tex не найден.")

def create_latex_document(title, author, date, office, section, subsection, text ):
    '''
    Ф-я генерирует и заполняет LaTeX документ при помощи данных из шаблона professor.tex
    Arguments:
        title (str): Заголовок документа.
        author (str): Автор документа.
        date (str): Дата создания документа.
        office (str): Название и город издательства.
        section (str): Раздел документа.
        subsection (str): Подраздел документа.
        text (str): Основной текст документа, в котором могут быть использованы метки.
    possible errors: 
        FileNotFoundError: Если файл шаблона 'professor.tex' не существует или не может быть открыт.
        IOError: Если возникает ошибка при чтении или записи файла (например, недостаточно прав).
    '''
    # Читаем шаблон
     
    with open('professor.tex', 'r', encoding='utf-8') as file:
        document = file.read()

    # Заменяем метки в шаблоне на переданные значения
    document = document.replace('TITLE', title)
    document = document.replace('AUTHOR', author)
    document = document.replace('DATE', date)
    document = document.replace('NAME, CITY', office)
    document = document.replace('SECTION', section)
    document = document.replace('U', subsection)
    document = document.replace('Main text', text)

    # Записываем новый файл с заполненным шаблоном
    with open('generated_document.tex', 'w', encoding='utf-8') as file:
        file.write(document)

    print("LaTeX документ успешно создан: generated_document.tex")
