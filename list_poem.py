dict_number = {}
import re

with open('poem.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    patt = re.compile('[,?!. :«»—…\n]')
    word_list = re.split(patt, data.lower(), maxsplit=0)
    print(word_list)
    for words in word_list:
        if words in dict_number and len(words) > 0:
            dict_number[words] += 1
        else:
            dict_number[words] = 1

final_dict = sorted(dict_number.items(),
                    reverse=True,
                    key=lambda kv_pair: kv_pair[1])
# print(final_dict)

with open('poem_result.txt', 'w', encoding='UTF-8') as file_new:
    file_new.write("Частотный словарь стихотворения")
    for items in final_dict:
        print(items)
        print(items[0])
        line = "\n" + items[0] + ": " + str(items[1])
        file_new.write(line)

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# df = pd.DataFrame(dict_number, columns=["word", "freq"])
#
# fig = plt.figure(figsize=(15, 5))
# ax = sns.barplot(x="word", y="freq", data=df)
# plt.xticks(rotation=45)
# plt.show()
