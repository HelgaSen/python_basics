"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет
определенную ценность. В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо
только английские, либо только русские буквы.
"""


def calculate_word_cost(param_1, param_2):
    """
    Функция для поиска суммы КЛЮЧЕЙ по значениям
    :param param_1: словарь, ключи которого будут суммироваться, если будет
                    найдено значение
    :param param_2: список значений, которые ищем в словаре
    :return: сумма ключей совпавших значений
    """
    word_cost = 0
    for i in range(len(param_2)):
        for key, value in param_1.items():
            if param_2[i] in value:
                word_cost = word_cost + key
        i += 1
    return word_cost


eng_letter_cost = dict()
eng_letter_cost[1] = 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'
eng_letter_cost[2] = 'D', 'G'
eng_letter_cost[3] = 'B', 'C', 'M', 'P'
eng_letter_cost[4] = 'F', 'H', 'V', 'W', 'Y'
eng_letter_cost[5] = 'K'
eng_letter_cost[8] = 'J', 'X'
eng_letter_cost[10] = 'Q', 'Z'

rus_letter_cost = dict()
rus_letter_cost[1] = 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'
rus_letter_cost[2] = 'Д', 'К', 'Л', 'М', 'П', 'У'
rus_letter_cost[3] = 'Б', 'Г', 'Ё', 'Ь', 'Я'
rus_letter_cost[4] = 'Й', 'Ы'
rus_letter_cost[5] = 'Ж', 'З', 'Х', 'Ц', 'Ч'
rus_letter_cost[8] = 'Ш', 'Э', 'Ю'
rus_letter_cost[10] = 'Ф', 'Щ', 'Ъ'

input_word_eng = list(input('Введите слово на английском языке: ').upper())
print(f'По правилам настольной игры "Скрабл" вы заработали  очков: '
      f' {calculate_word_cost(eng_letter_cost, input_word_eng)}')

input_word_rus = list(input('Введите слово на русском языке: ').upper())
print(f'По правилам настольной игры "Скрабл" вы заработали  очков: '
      f' {calculate_word_cost(rus_letter_cost, input_word_rus)}')
