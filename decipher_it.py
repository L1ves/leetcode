def decipher_this(s):
    decipher_list = s.split()  # разбиваем по словам
    int_word = []  # первые буквы слова
    int_list = []
    list_decypher = []  # сюда список слов готовый
    word_decipher = []  # сюда будем складывать расшированное слово
    # первые две или три цифры в слове переводим из int в acsii
    # меняем вторую и последнюю букву местами
    # слова разделены пробелом. остальное не трогаем
    int_word = re.findall(r"\d+", s)#matched first char in word
    print(int_word)
    print(decipher_list)
    int_list = ([int(x) for x in int_word]) #convert first char and get int
    print([chr(x) for x in int_list]) # get first char in word

