print('новая ветка')
# sample
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код
def capitalised(yours_films_2):
    capilised_symbols = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    small_symbols = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    for symbol in yours_films:

        if symbol == 'а' or 'б' or 'в' or 'г' or 'д' or 'е' or 'ё' or 'ж' or 'з' or 'и' or 'й' or 'к' or 'л' or 'м' or 'н' or 'о' or 'п' or 'р' or 'с' or 'т' or 'у' or 'ф' or 'х' or 'ц' or 'ч' or 'ш' or 'щ' or 'ъ' or 'ы' or 'ь' or 'э' or 'ю' or 'я':
            for index, value in enumerate(small_symbols):
                if symbol == value:
                    # print(index, value)
                    yours_films_2[0] = capilised_symbols[index]
                    # print(yours_films_2)

            # ставим здесь return чтоб вернуло после первой буквы
            return yours_films_2
            # break


def word_by_symbols(yours_films):
    yours_films_2 = list(yours_films)
    # print(yours_films_2)
    # yours_films_2 = []
    # for symbols in yours_films:
    #     yours_films_2.append(symbols)
    # print(yours_films_2)
    return yours_films_2

def return_to_string(name):
    name = ''
    for _ in yours_films_2:
        name += _
        # print(name)
    # print(name, 'name')
    return name


def comparison(qnts):
    # list_of_exsisting_mov = ''
    qnts = 0
    none = ''
    for movie in films:
        qnts += 1
        if movie == name:

            # print('movie', movie)
            return name

        else: #films[len(films)] != yours_films_2:
            x = len(films)
            if qnts == x:

                print(f'Ошибка: фильма {name} у нас нет :(')
                # return none





qnts_of_films = int(input('Введите кол-во фильмов? '))
yours_films = []
list_of_exsisting_mov_2 = []
for _ in range(qnts_of_films):
    yours_films = input('Введите название фильма? ')
    yours_films_2 = word_by_symbols(yours_films)
    yours_films_2 = capitalised(yours_films_2)
    # yours_films_2 = str(yours_films_2)
    # print(yours_films_2)
    name = return_to_string(yours_films_2)
    list_of_exsisting_mov = comparison(name)
    list_of_exsisting_mov_2.append(list_of_exsisting_mov)

print('Ваш список любимых фильмов: ', end='')
for each in list_of_exsisting_mov_2:

    if each != None:
        print(each, '', end='')