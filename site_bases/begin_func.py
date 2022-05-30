import re
from dict import new_dict_word

voc_syll = {'А': 'А́', 'Е': 'Е́', 'И': 'И́', 'О': 'О́', 'У': 'У́', 'Ы': 'Ы́', 'Э': 'Э́', 'Ю': 'Ю́', 'Я': 'Я́',
            'а': 'а́', 'е': 'е́', 'и': 'и́', 'о': 'о́', 'у': 'у́', 'ы': 'ы́', 'э': 'э́', 'ю': 'ю́', 'я': 'я́'}


def search_begin(x):
    out = {}
    for key in new_dict_word:
        for let in x:
            if let in voc_syll:
                x_new = str()
                x_new = re.sub(let, voc_syll[let], x)
                if key.startswith(x_new):
                    out[key] = new_dict_word[key]
        if key.startswith(x):
            out[key] = new_dict_word[key]
    return out


# y = input()
# for i, j in search_begin(y).items():
#     print(str(i) + ':\n' + str(j))
