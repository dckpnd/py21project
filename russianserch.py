import re

#with open('slovar_new.txt', 'r', encoding='utf-8') as f:
    #words = []
    #definitions = []
    #for line in f.readlines():
        #line = line.split(' — ') #посмотреть как делила Настя потому что у меня проблемы (не везде есть тире)
        #word = line[0]
        #if (line[0]!=line[-1]):
            #definition = line[1] #сделать не срез, а удалить из line word??
        #else:
            #definition = ''
        #words.append(word)
        #definitions.append(definition)
    #dictionary = {}
    #for i in range(len(words)):
        #dictionary[words[i]] = definitions[i]
    #request = input()
    #for word, definition in dictionary.items():
        #slova = definition.split()
        #for w in slova:
            #if w.startswith(request):
                #print(word, definition)

dict_word = {}
with open("slovar_new.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    for words in data:
        if " — 1)" not in words and "1)" in words:
            patt = re.compile('1\)')
            word_list = re.split(patt, words, maxsplit=0)
            if len(word_list) > 1:
                key_word = word_list[0][:-1]
                value_word = "— 1)" + word_list[1]
                patt_2 = re.compile('2\)')
                word_list_2 = re.split(patt_2, value_word, maxsplit=0)
                value_word_1 = word_list_2[0][:-2]
                value_word_2 = "— 2)" + word_list_2[1][:-1]
                dict_word.setdefault(key_word, []).append(value_word_1)
                dict_word.setdefault(key_word, []).append(value_word_2)
        elif "/" in words:
            patt = re.compile("(/.{1,12}/|I.{2,12}J)")
            word_list = re.split(patt, words, maxsplit=0)
            if len(word_list) > 2:
                key_word = word_list[0][:-1]
                value_word = " ".join(word_list[1:])
                dict_word.setdefault(key_word, []).append(value_word)
        else:
            word_list = re.split(" — ", words, maxsplit=0)
            if len(word_list) > 1:
                key_word = word_list[0]
                value_word = " ".join(word_list[1:])
                dict_word.setdefault(key_word, []).append(value_word)
request = input()
k = 0
for word, definition in dict_word.items():
    for w in definition:
        if request in w:
            k += 1
            print(word)
            for elem in definition:
                pr_def = elem.split(';')
                for e in pr_def:
                    print(e)
if k == 0:
    print('Такого слова нет в словаре')