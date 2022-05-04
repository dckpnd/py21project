import re
with open("slovar.txt", "r", encoding="utf-8") as file:
    with open("slovar_new.txt", "w", encoding="utf-8") as file_new:
        data = file.readlines()
        for words in data:
            new = re.sub(r'- |¬|-	|-', '', words)
            new_1 = re.sub(r'ТУ', 'Т./', new)
            new_2 = re.sub(r'ДУ', 'Д./', new_1)
            new_3 = re.sub(r'\b\?\?\?|\.\?\?\?', ')', new_2)
            new_4 = re.sub(r'\?\?\?\b', '(', new_3)
            new_5 = re.sub(r'\?\?\?', 'д', new_4)
            #print(new_5)
            file_new.write(new_5)