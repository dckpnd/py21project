with open('slovar_so_znakami_voprosa.txt', 'r', encoding='utf-8') as f:
    words = []
    definitions = []
    for line in f.readlines():
        line = line.split(' — ')
        word = line[0]
        if (line[0]!=line[-1]):
            definition = line[1]
        else:
            definition = ''
        words.append(word)
        definitions.append(definition)
    dictionary = {}
    for i in range(len(words)):
        dictionary[words[i]] = definitions[i]
    request = input()
    for word, definition in dictionary.items():
        slova = definition.split()
        for w in slova:
            if w.startswith(request):
                print(word, definition)
