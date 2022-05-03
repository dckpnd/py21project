import colors
import re

dict_word = {}
with open("slovar.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    for words in data:
        if " — 1)" not in words and "1)" in words:
            patt = re.compile('1\)')
            word_list = re.split(patt, words, maxsplit=0)
            if len(word_list) > 1:
                key_word = word_list[0]
                value_word = " — 1)" + word_list[1]
                patt_2 = re.compile('2\)')
                word_list_2 = re.split(patt_2, value_word, maxsplit=0)
                value_word_1 = word_list_2[0]
                value_word_2 = " — 2)" + word_list_2[1]
                # print(value_word_1)
                # print(value_word_2)
                dict_word.setdefault(key_word, []).append(value_word_1)
                dict_word.setdefault(key_word, []).append(value_word_2)
        elif "/" in words:
            patt = re.compile("(/.{2,12}/|I.{2,12}J)")
            word_list = re.split(patt, words, maxsplit=0)
            if len(word_list) > 2:
                #print(word_list[1:])
                key_word = word_list[0][:-1]
                #if word_list:
                value_word = " ".join(word_list[1:])
                dict_word.setdefault(key_word, []).append(value_word)
        else:
            word_list = re.split(" — ", words, maxsplit=0)
            if len(word_list) > 1:
                key_word = word_list[0]
                value_word = " ".join(word_list[1:])
                dict_word.setdefault(key_word, []).append(value_word)
# print(dict_word)
# for lines in dict_word:
#     print(lines)
no_word = ""
choose_language = input("Выберите язык поиска: русский (напишите 1) или табасаранский (напишите 2): ")
if choose_language == "2":
    find_word = input("Выберите слово на табасаранском языке, перевод которого Вы хотите найти: ")
    for keys in dict_word:
        if find_word == keys:
            value = " ".join(dict_word.get(keys))
            # print(value)
            with colors.pretty_output(colors.FG_BLUE, colors.BOLD) as out:
                out.write(find_word)

                if "/" in value:
                    sep_words = re.split(" — ", value, maxsplit=0)
                    with colors.pretty_output(colors.BOLD) as out_1:
                        out_1.write(sep_words[0])
                        if ";" in value:
                            separ_words = sep_words[1].split(";")
                            # print(separ_words)
                            with colors.pretty_output(colors.BG_GREEN) as out_2:
                                out_2.write(separ_words[0])
                                if "ср." not in value:
                                    print(separ_words[1:])
                                else:
                                    pr_comp = " ".join(separ_words[1:])
                                    comp = pr_comp.split("ср.")
                                    print(comp[0][1:])
                                    print("ср." + comp[1][:-2])
                        else:
                            with colors.pretty_output(colors.BG_GREEN) as out_2:
                                out_2.write(sep_words[1])
                elif ";" in value and "/" not in value:
                    separ_words = value.split(";")
                    # print(separ_words)
                    with colors.pretty_output(colors.BG_GREEN) as out_2:
                        out_2.write(separ_words[0])
                        if "ср." not in value:
                            print(separ_words[1:])
                        else:
                            pr_comp = " ".join(separ_words[1:])
                            comp = pr_comp.split("ср.")
                            print(comp[0][1:])
                            print("ср." + comp[1][:-2])
                else:
                    with colors.pretty_output(colors.BG_GREEN) as out_2:
                        out_2.write(value)
    if find_word not in dict_word:
        with colors.pretty_output(colors.BG_RED) as out_2:
            out_2.write("Этого слова нет в словаре.")
