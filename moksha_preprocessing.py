"""
"""

import json
import moksha_visualizing

def preprocess_data(data):

    for sent in data['sentences']:
        no_in_sent = 1
        for word in sent['words']:
            word['no_in_sent'] = no_in_sent
            no_in_sent += 1
            
            if 'pos_tags' not in word.keys() or word['pos_tags'] == []:
                word['pos_tags'] = [{'pos': 'X', 'tag': '_'}]
                            
            if len(word['pos_tags']) > 1:
                word['main_pos_tag_no'] = 0
            elif len(word['pos_tags']) == 1:
                word['main_pos_tag_no'] = 1
    
    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'].startswith('эряф') or word['form'].startswith('Эряф'):
                if word['pos_tags'][0]['pos'] == 'VERB' and 'Case' in word['pos_tags'][0]['tag'].keys():
                    word['pos_tags'][0]['pos'] = 'NOUN'
                    del  word['pos_tags'][0]['tag']['PtcpType']
                    del  word['pos_tags'][0]['tag']['Transitivity']
                    del  word['pos_tags'][0]['tag']['VerbForm']
                    word['pos_tags'][0]['trans_ru'] = 'жизнь'
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)


    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == "аф" or word['form'] == "Аф":
                word['pos_tags'][0]['pos'] = 'AUX'
                del  word['pos_tags'][0]['tag']['Connegative']
                word['pos_tags'][0]['tag']['Polarity'] = 'Neg'
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                

    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == "ширде":
                if len(word['pos_tags']) == 1:
                    tag = {'pos': 'NOUN', 'tag': {'Case': 'Abl', 'Number': 'Sing'}, 'trans_ru': 'сторона'}
                    word['pos_tags'].append(tag)
                    word['main_pos_tag_no'] = 2
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                
    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == "кинди":
                if len(word['pos_tags']) == 2:
                    tag = {'pos': 'PRON', 'tag': {'Case': 'Dat', 'Number': 'Sing'}, 'trans_ru': 'кто'}
                    word['pos_tags'].append(tag)
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == "кинь":
                if len(word['pos_tags']) == 4:
                    tag = {'pos': 'PRON', 'tag': {'Case': 'Gen', 'Number': 'Sing'}, 'trans_ru': 'кто'}
                    word['pos_tags'].append(tag)
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == "кит":
                if len(word['pos_tags']) == 2:
                    tag = {'pos': 'PRON', 'tag': {'Case': 'Nom', 'Number': 'Plur'}, 'trans_ru': 'кто'}
                    word['pos_tags'].append(tag)
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)

    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == "самс" and len(word['pos_tags']) == 1:
                tag = {'pos': 'ADP', 'tag': {'AdpType': 'Post'}, 'trans_ru': 'начиная с'}
                word['pos_tags'].append(tag)
                word['main_pos_tag_no'] = 0
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            if word['form'] == "кемот":
                word['pos_tags'][0] = {'pos': 'ADJ', 'tag': {'Case': 'Nom', 'Number': 'Plur'}, 'trans_ru': 'крепкий, здоровый'}
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    

    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'].isdecimal() and word['pos_tags'][0]['pos'] == 'X':
                word['pos_tags'][0]['pos'] = 'NUM'
                word['pos_tags'][0]['tag'] = {}
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)

    for sent in data['sentences']:
        for word in sent['words']:
            if word['pos_tags'][0]['pos'] == 'X':
                if word['form'].endswith('ай') or word['form'].endswith('яй') or word['form'].endswith('ой'):
                    word['pos_tags'][0]['pos'] = 'ADJ'
                    word['pos_tags'][0]['tag'] = {'Rus': 'Yes'}
                    print(word['form'])
                    for tag in moksha_visualizing.word_as_conllu(word):
                        print(tag)

    for sent in data['sentences']:
        for word in sent['words']:
            if word['pos_tags'][0]['pos'] == 'X':
                if word['form'].istitle():
                    if word['form'].endswith('инонь') or word['form'].endswith('инань') or word['form'].endswith('овань') or word['form'].endswith('овонь') or word['form'].endswith('ёвань') or word['form'].endswith('ёвонь') or word['form'].endswith('евань') or word['form'].endswith('евонь'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Gen', 'Number': 'Sing', 'PropnType': 'FamN'}
                        print(word['form'])
                        for tag in moksha_visualizing.word_as_conllu(word):
                            print(tag)
                            
                    elif word['form'].endswith('ин') or word['form'].endswith('ина') or word['form'].endswith('ова') or word['form'].endswith('ов') or word['form'].endswith('ёва') or word['form'].endswith('ёв') or word['form'].endswith('ева') or word['form'].endswith('ев'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Nom', 'Number': 'Sing', 'PropnType': 'FamN'}
                        print(word['form'])
                        
                    elif word['form'].endswith('инць') or word['form'].endswith('инась') or word['form'].endswith('овась') or word['form'].endswith('овсь') or word['form'].endswith('ёвась') or word['form'].endswith('ёвсь') or word['form'].endswith('евась') or word['form'].endswith('евсь'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Nom', 'Definite': 'Def', 'Number': 'Sing', 'PropnType': 'FamN'}
                        print(word['form'])
                        for tag in moksha_visualizing.word_as_conllu(word):
                            print(tag)
                            
                    elif word['form'].endswith('инть') or word['form'].endswith('инать') or word['form'].endswith('овать') or word['form'].endswith('овть') or word['form'].endswith('ёвать') or word['form'].endswith('ёвть') or word['form'].endswith('евать') or word['form'].endswith('евть'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Gen', 'Definite': 'Def', 'Number': 'Sing', 'PropnType': 'FamN'}
                        print(word['form'])
                        for tag in moksha_visualizing.word_as_conllu(word):
                            print(tag)
                            
                    elif word['form'].endswith('вка'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Nom', 'Number': 'Sing', 'PropnType': 'TopN'}
                        word['pos_tags'][0]['trans_ru'] = word['form']
                        print(word['form'])
                        for tag in moksha_visualizing.word_as_conllu(word):
                            print(tag)
                            
                    elif word['form'].endswith('вкась'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Nom', 'Definite': 'Def', 'Number': 'Sing', 'PropnType': 'TopN'}
                        word['pos_tags'][0]['trans_ru'] = word['form'][:-2]
                        print(word['form'])
                        for tag in moksha_visualizing.word_as_conllu(word):
                            print(tag)
                            
                    elif word['form'].endswith('вкань'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Gen', 'Number': 'Sing', 'PropnType': 'TopN'}
                        word['pos_tags'][0]['trans_ru'] = word['form'][:-2]
                        tag = {'pos': 'ADJ', 'tag': {}, 'trans_ru': word['form'][:-4] + 'ский'}
                        word['pos_tags'].append(tag)
                        word['main_pos_tag_no'] = 0
                        print(word['form'])
                        for tag in moksha_visualizing.word_as_conllu(word):
                            print(tag)
                            
                    elif word['form'].endswith('вкаса'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Ine', 'Number': 'Sing', 'PropnType': 'TopN'}
                        word['pos_tags'][0]['trans_ru'] = word['form'][:-2]
                        print(word['form'])
                        for tag in moksha_visualizing.word_as_conllu(word):
                            print(tag)
                        
                    elif word['form'].endswith('вкать'):
                        word['pos_tags'][0]['pos'] = 'PROPN'
                        word['pos_tags'][0]['tag'] = {'Case': 'Gen', 'Definite': 'Def', 'Number': 'Sing', 'PropnType': 'TopN'}
                        word['pos_tags'][0]['trans_ru'] = word['form'][:-2]
                        print(word['form'])
                        for tag in moksha_visualizing.word_as_conllu(word):
                            print(tag)
                    
                    for tag in moksha_visualizing.word_as_conllu(word):
                        print(tag)



    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == 'башка' and len(word['pos_tags']) == 1:
                tag = {'pos': 'ADP', 'tag': {'AdpType': 'Post'}, 'trans_ru': 'кроме, помимо'}
                word['pos_tags'].append(tag)
                tag = {'pos': 'ADV', 'tag': {}, 'trans_ru': 'отдельно, порознь'}
                word['pos_tags'].append(tag)
                word['main_pos_tag_no'] = 0
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)


    prs_tag = {'Conjug': 'NonObj', 'Number[subj]': 'Sing', 'Person[subj]': '3', 'Tense': 'Pres'}
    ptcp_tag = {'VerbForm': 'Part'}

    for sent in data['sentences']:
        for word in sent['words']:
            is_ptcp = False
            for i in range(len(word['pos_tags'])):
                if type(word['pos_tags'][i]['tag']) == dict:
                    if 'VerbForm' in word['pos_tags'][i]['tag'].keys():
                        if word['pos_tags'][i]['tag']['VerbForm'] == 'Part':
                            is_ptcp = True
                            
            
            for i in range(len(word['pos_tags'])):
                if type(word['pos_tags'][i]['tag']) == dict:
                    if word['pos_tags'][i]['tag'].items() >= prs_tag.items():
                        if 'Voice' not in word['pos_tags'][i]['tag'].keys():
                            if is_ptcp == False:
                                tag = word['pos_tags'][i]['tag'].copy()
                                del tag['Conjug']
                                del tag['Number[subj]']
                                del tag['Person[subj]']
                                del tag['Tense']
                                tag.update(ptcp_tag)
                                pos_tag = {'pos': 'VERB', 'tag': tag, 'trans_ru': word['pos_tags'][i]['trans_ru']}
                                word['pos_tags'].append(pos_tag)
                                word['main_pos_tag_no'] = 0
                    
                            print(word['form'])
                            for tag in moksha_visualizing.word_as_conllu(word):
                                print(tag)

    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == 'конат' or word['form'] == 'Конат':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'PRON':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'].startswith('пинг') or word['form'].startswith('Пинг'):
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['trans_ru'] == 'время':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'лия' or word['form'] == 'Лия':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'ADJ':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'пара' or word['form'] == 'Пара':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'ADJ':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'] == 'эрь' or word['form'] == 'Эрь':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'ADJ':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'эряви' or word['form'] == 'Эряви':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'AUX':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'тянди' or word['form'] == 'Тянди':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'PRON':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'] == 'приемнай' or word['form'] == 'Приемнай':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'ADJ':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'] == 'сяда' or word['form'] == 'Сяда':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'PART':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'сави' or word['form'] == 'Сави':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'AUX':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'тов' or word['form'] == 'Тов':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'ADV':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'коза' or word['form'] == 'Коза':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'ADV':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'сидеста' or word['form'] == 'Сидеста':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'ADV':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'] == 'мяль' or word['form'] == 'Мяль':
                for i in range(len(word['pos_tags'])):
                    if 'Case' in word['pos_tags'][i]['tag']:
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)

            """elif word['form'] == 'ули' or word['form'] == 'Ули':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'VERB':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)"""


    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == 'эрявикс' or word['form'] == 'Эрявикс':
                for i in range(len(word['pos_tags'])):
                    if word['pos_tags'][i]['pos'] == 'ADJ':
                        word['main_pos_tag_no'] = i + 1
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'] == 'уликс' or word['form'] == 'Уликс':
                if len(word['pos_tags']) == 2:
                    tag = {'pos': 'ADJ', 'tag': {}, 'trans_ru': 'имеющийся'}
                    word['pos_tags'].append(tag)
                    word['main_pos_tag_no'] = len(word['pos_tags'])
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    

    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == 'шитнень':
                tag = {'pos': 'NOUN', 'tag': {'Case': 'Gen', 'Definite': 'Def', 'Number': 'Plur'}, 'trans_ru': 'день'}
                word['pos_tags'].append(tag)
                word['main_pos_tag_no'] = len(word['pos_tags'])
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'] == 'шитненди':
                tag = {'pos': 'NOUN', 'tag': {'Case': 'Dat', 'Definite': 'Def', 'Number': 'Plur'}, 'trans_ru': 'день'}
                word['pos_tags'].append(tag)
                word['main_pos_tag_no'] = len(word['pos_tags'])
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'] == 'шитне':
                tag = {'pos': 'NOUN', 'tag': {'Case': 'Nom', 'Definite': 'Def', 'Number': 'Plur'}, 'trans_ru': 'день'}
                word['pos_tags'].append(tag)
                word['main_pos_tag_no'] = len(word['pos_tags'])
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
            
            elif word['form'].endswith('ихне') or word['form'].endswith('ихнень') or word['form'].endswith('ихненди') or word['form'].endswith('ихне') or word['form'].endswith('ихнень') or word['form'].endswith('ихненди'):
                if len(word['pos_tags']) > 1:
                    for i in range(len(word['pos_tags'])):
                        if type(word['pos_tags'][i]['tag']) == dict:
                            if 'Definite' in word['pos_tags'][i]['tag'].keys():
                                word['main_pos_tag_no'] = i + 1
                    print(word['form'])
                    for tag in moksha_visualizing.word_as_conllu(word):
                        print(tag)
                
                elif type(word['pos_tags'][0]['tag']) == dict:
                    if 'Person[psor]' in word['pos_tags'][0]['tag'].keys():
                        pos_tag = word['pos_tags'][0].copy()
                        tag = pos_tag['tag'].copy()
                        del tag['Number[psor]']
                        del tag['Person[psor]']
                        tag['Definite'] = 'Def'
                        pos_tag['tag'] = tag
                        word['pos_tags'].append(pos_tag)
                        word['main_pos_tag_no'] = 2
                
                elif word['pos_tags'][0]['pos'] == 'X' :
                    if word['form'].endswith('ень'):
                        tag = {'Case': 'Gen', 'Number': 'Plur', 'Definite': 'Def', 'VerbForm': 'Part'}
                    elif word['form'].endswith('не'):
                        tag = {'Case': 'Nom', 'Number': 'Plur', 'Definite': 'Def', 'VerbForm': 'Part'}
                    elif word['form'].endswith('нди'):
                        tag = {'Case': 'Dat', 'Number': 'Plur', 'Definite': 'Def', 'VerbForm': 'Part'}
                    pos_tag = {'pos': 'VERB', 'tag': tag}
                    word['pos_tags'].append(pos_tag)
                    word['main_pos_tag_no'] = 2
                
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'].endswith('не') or word['form'].endswith('нень') or word['form'].endswith('ненди'):
                if len(word['pos_tags']) > 1 and word['main_pos_tag_no'] == 0 and not word['form'].lower().startswith('кяль'):
                    for i in range(len(word['pos_tags'])):
                        if 'Definite' in word['pos_tags'][i]['tag'].keys():
                            word['main_pos_tag_no'] = i + 1
                    print(word['form'])
                elif type(word['pos_tags'][0]['tag']) == dict:
                    if 'Person[psor]' in word['pos_tags'][0]['tag'].keys():
                        pos_tag = word['pos_tags'][0].copy()
                        tag = pos_tag['tag'].copy()
                        del tag['Number[psor]']
                        del tag['Person[psor]']
                        tag['Definite'] = 'Def'
                        pos_tag['tag'] = tag
                        word['pos_tags'].append(pos_tag)
                        word['main_pos_tag_no'] = 2
                        
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)


    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'].endswith('не') or word['form'].endswith('нень') or word['form'].endswith('ненди'):
                if len(word['pos_tags']) > 1 and word['main_pos_tag_no'] == 0 and not word['form'].lower().startswith('кяль'):
                    for i in range(len(word['pos_tags'])):
                        if 'Definite' in word['pos_tags'][i]['tag'].keys():
                            word['main_pos_tag_no'] = i + 1
                    print(word['form'])
                elif type(word['pos_tags'][0]['tag']) == dict:
                    if 'Person[psor]' in word['pos_tags'][0]['tag'].keys():
                        pos_tag = word['pos_tags'][0].copy()
                        tag = pos_tag['tag'].copy()
                        del tag['Number[psor]']
                        del tag['Person[psor]']
                        tag['Definite'] = 'Def'
                        pos_tag['tag'] = tag
                        word['pos_tags'].append(pos_tag)
                        word['main_pos_tag_no'] = 2
                        
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)

    for sent in data['sentences']:
        for word in sent['words']:
            if word['form'] == 'шитнень':
                tag = {'pos': 'NOUN', 'tag': {'Case': 'Gen', 'Definite': 'Def', 'Number': 'Plur'}, 'trans_ru': 'день'}
                word['pos_tags'].append(tag)
                word['main_pos_tag_no'] = len(word['pos_tags'])
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'] == 'шитненди':
                tag = {'pos': 'NOUN', 'tag': {'Case': 'Dat', 'Definite': 'Def', 'Number': 'Plur'}, 'trans_ru': 'день'}
                word['pos_tags'].append(tag)
                word['main_pos_tag_no'] = len(word['pos_tags'])
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)
                    
            elif word['form'] == 'шитне':
                tag = {'pos': 'NOUN', 'tag': {'Case': 'Nom', 'Definite': 'Def', 'Number': 'Plur'}, 'trans_ru': 'день'}
                word['pos_tags'].append(tag)
                word['main_pos_tag_no'] = len(word['pos_tags'])
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)


    for sent in data['sentences']:
        for word in sent['words']:
            if word['pos_tags'][0]['pos'] == 'X':
                #tag = {'pos': 'ADP', 'tag': {'AdpType': 'Post'}, 'trans_ru': 'начиная с'}
                #word['pos_tags'].append(tag)
                #word['main_pos_tag_no'] = 0
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)


    for sent in data['sentences']:
        for word in sent['words']:
            if word['pos_tags'][0]['tag'] == {}:
                #tag = {'pos': 'ADP', 'tag': {'AdpType': 'Post'}, 'trans_ru': 'начиная с'}
                #word['pos_tags'].append(tag)
                #word['main_pos_tag_no'] = 0
                print(word['form'])
                for tag in moksha_visualizing.word_as_conllu(word):
                    print(tag)


