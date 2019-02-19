# -*- coding: UTF-8 -*-
def load_localization(lang='be'):
    D = dict()
    load_pass = "lang/{}.txt".format(lang)
    file = open(load_pass, "r", encoding="UTF-8")
    lines = file.readlines()
    for i in range(0,len(lines),3):
        D[lines[i].strip()] = lines[i+1].strip()
    return D

def get_language_code(request):
    language = request.values.get("lang","be")
    return language
