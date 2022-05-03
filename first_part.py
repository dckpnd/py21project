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
                key_word = word_list[0][:-1]
                value_word = "— 1)" + word_list[1]
                patt_2 = re.compile('2\)')
                word_list_2 = re.split(patt_2, value_word, maxsplit=0)
                value_word_1 = word_list_2[0][:-2]
                value_word_2 = "— 2)" + word_list_2[1][:-1]
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
                if "1)" in value:
                    if "/" in value:
                        sep_words = re.split(" — ", value, maxsplit=0)
                        with colors.pretty_output(colors.BOLD) as out_1:
                            out_1.write(sep_words[0])
                            with colors.pretty_output(colors.BG_GREEN) as out_2:
                                separ_words = sep_words[1].split(";")
                                out_2.write(separ_words[0])
                                out_2.write(separ_words[1][1:])
                                pr_comp = " ".join(separ_words[2:])
                                if len(separ_words) > 2 and "ср." not in value:
                                    out_2.write(pr_comp)
                                elif len(separ_words) > 2 and "ср." in value:
                                    print(pr_comp.split("ср.")[0][1:])
                                    print(separ_words[-1][1:])
                    else:
                        separ_words = value.split(";")
                        with colors.pretty_output(colors.BG_GREEN) as out_1:
                            out_1.write(separ_words[0])
                            out_1.write(separ_words[1][1:])
                            pr_comp = " ".join(separ_words[2:])
                            if len(separ_words) > 2 and "ср." not in value:
                                out_1.write(pr_comp)
                            elif len(separ_words) > 2 and "ср." in value:
                                print(pr_comp.split("ср.")[0][1:])
                                print(separ_words[-1][1:])
                elif "/" in value:
                    sep_words = re.split(" — ", value, maxsplit=0)
                    with colors.pretty_output(colors.BOLD) as out_1:
                        out_1.write(sep_words[0])
                        if ";" in value:
                            separ_words = sep_words[1].split(";")
                            # print(separ_words)
                            with colors.pretty_output(colors.BG_GREEN) as out_2:
                                out_2.write(separ_words[0])
                                if "ср." not in value:
                                    for items in separ_words[1:]:
                                        print(items[1:])
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
                            for items in separ_words[1:]:
                                print(items[1:])
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
