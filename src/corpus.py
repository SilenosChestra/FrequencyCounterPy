# -*- coding: UTF-8 -*-
# import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, abort, jsonify
import settings
from corpus_localization import localization
from alfavitnachastotny import context, commonize

app = Flask(__name__)

def tocount(s, not_begin, stop_words, symbols):
    import re


    s = re.sub(r'[?!,.]', '', s)

    s = s.replace('\r\n',' ')
    s = s.strip()

    #Сімвалы, з якіх можа складацца, але не можа пачынацца слова
    nb = list(not_begin)

    #Ігнараваць словы
    stop_words_list = stop_words.split('\r\n')


    #Здымаем лішнія перансы строк
    s = s.split(' ')
    for i in range(s.count('')):
        s.remove('')

    #усе фільтрацыі
    unic = list(filter(lambda x: x[0] not in nb and x not in stop_words_list and any(k in symbols for k in x), s))

    result={}

    l1, l2 = len(unic), len(set(unic))

    for i in unic:
            result[i] = s.count(i)

    return result, l1, l2

@app.route('/', methods=['GET', 'POST'])
def ServiceDemonstrator():
    lang = localization.load_localization(localization.get_language_code(request))

    _input = lang['default input'].replace('\\n', '\n')
    is_post = False
    sp = []
    _notbegin = """-'’ʼ"""
    result={}
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяЂЃѓЉЊЌЋЏђљњќћџЎўЈҐЁЄЇІіґёєјЅѕї-"
    stop_words = """груша
цвіла
апошні
год"""
    ln1,ln2 = int(),int()
    contextnum = 3
    words_to_count = ""
    case_sensitive = 'on'
    context_sensitive = 'on'
    contexts_max = 2
    

    if request.method == "POST":
        is_post = True

        _input = request.form.get("inputText")
        _notbegin = request.form.get('symbols_in_words')
        symbols = request.form.get('symbols_of_words')
        stop_words = request.form.get('stop_words')
        words_to_count = request.form.get('words_to_count')
        case_sensitive = request.form.get('caseSensitive')
        context_sensitive = request.form.get('contextSensitive')
        contexts_max = request.form.get('contextsMax')

        text = ''

        words_to_count = words_to_count.replace(',','')
        words_to_count = words_to_count.replace('\r\n',' ')


        if case_sensitive == None:
            text = _input.lower()
        else:
            text = request.form.get("inputText")

        result, ln1, ln2 = tocount(text, str(_notbegin), str(stop_words), symbols)
        d_2 = context(text, int(contextnum))
        sp = commonize(result, d_2)

        if request.form.get('words_to_count'):
            sp_copy = sp.copy()
            sp = []
            for i in range(len(sp_copy)):
                if any(k == sp_copy[i][0] for k in words_to_count.split(' ')):
                    sp.append(sp_copy[i])

    return render_template('index.html', is_post=is_post,_input=_input, lang=lang, notbegin=_notbegin,sp=sp, stop_words=stop_words,
                           ln1=ln1, ln2=ln2, contextnum=contextnum, symbols=symbols, words_to_count=words_to_count,
                           case_sensitive=case_sensitive, context_sensitive=context_sensitive,contexts_max=contexts_max)




if __name__ == '__main__':
    app.run(use_reloader=settings.use_reloader, debug=settings.debug, host=settings.host, port=settings.port)
