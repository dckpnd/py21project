from flask import Flask, render_template, request
app = Flask(__name__)

import re

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
new_dict_word = {}
for keys in dict_word:
    for items in dict_word.get(keys):
        value_word = "".join(items)
        new_dict_word[keys] = value_word


@app.route('/', methods=['GET', 'POST'])
def slash_in():
    if request.method == 'POST':
        tabasaran_word = request.form.get('Tabasaran word')
        if tabasaran_word in new_dict_word:


            return '''
                    <h1>The translation is: {}</h1>'''.format(new_dict_word.get(tabasaran_word))
        else:
            return '''
            <h1> This word is not in the dictionary. </h1 > '''
    return '''
                <form method="POST">
                    <div><label>Tabasaran word: <input type="text" name="Tabasaran word"></label></div>
                    <input type="submit" value="Submit">
                </form>'''


if __name__ == '__main__':
    app.run(debug=False)