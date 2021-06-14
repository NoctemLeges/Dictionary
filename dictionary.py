#! /usr/bin/python3.8

from PyDictionary import PyDictionary
switch = True
def Translate(query,targetLangCode):
    return dictionary1.translate(query, targetLangCode)

while switch:
    query = input("[+]Enter the word you wish to learn about, peasant(Enter 'q' to quit,'-t' for translation services): ")
#EXIT_CONDITION
    if(query=='q'or query=='Q'):
        break
    dictionary1 = PyDictionary()
#TRANSLATION
    if(query=='-t'):
        query = input("[+]Enter the sentence to translate: ")
        langCode = input("[+]Enter the lang code: ")
        l = query.split()
        for w in l:
            print(Translate(w,langCode))
        
#MEANING NOUN
    meaning = dictionary1.meaning(query)
    if 'Noun' in meaning:
        meaning_noun = meaning['Noun']

        print("|||NOUN|||: ")
        for s in meaning_noun:
            print(s)
            print("_"*128)
        print("*"*128)
        print('*'*128)

#MEANING_VERB
    if 'Verb' in meaning:
        meaning_verb = meaning['Verb']
        print("|||VERB|||: ")
        for s in meaning_verb:
            print(s)
            print("_"*128)
        print('*'*128)
        print('*'*128)
#MEANING_ADJECTIVE
    if 'Adjective' in meaning:
        meaning_adjective = meaning['Adjective']
        print("|||ADJECTIVE|||: ")
        for s in meaning_adjective:
            print(s)
            print("_"*128)
        print("*"*128)
        print("*"*128)
#SYNONYM
    synonym = dictionary1.synonym(query)
    print("|||SYNONYMS|||: ")
    for s in synonym:
        print(s)
        print('_'*128)
    print("*"*128)
    print('*'*128)

#ANTONYM
    antonyms = dictionary1.antonym(query)

    print("|||ANTONYMS|||: ")
    for s in antonyms:
        print(s)
        print('_'*128)
    print('*'*128)
    print('*'*128)









