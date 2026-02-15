def create_spreadsheet(title):
    print("Создание электронной таблицы с именем " + title)

create_spreadsheet("Загрузки")

def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием " + title + " with " + str(row_count) + " lines")
