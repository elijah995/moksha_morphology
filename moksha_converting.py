"""
"""

import json

def process_file(file):
    f_data = []
    for text in file:
        f_data.append(process_text(text))
        
    return f_data


def process_text(text):
    f_text = {}
    f_text['meta'] = text['meta']
    f_text['sentences'] = []
    for sent in text['sentences']:
        f_text['sentences'].append(process_sentence(sent))
        
    return f_text


def process_sentence(sent):
    f_sentence = {}
    f_sentence['text'] = sent['text']
    f_sentence['words'] = []
    for word in sent['words']:
        f_sentence['words'].append(convert(word))
    
    return f_sentence


def convert(word):
    f_word = {}
    if 'sentence_index' in word.keys():
        f_word['no_in_sent'] = word['sentence_index'] + 1
    f_word['form'] = word['wf']
    f_word['pos_tags'] = []
    
    if word['wtype'] == 'punct':
        f_word['pos_tags'].append({'pos': 'PUNCT', 'tag': '_'})
        
    elif 'ana' in word.keys():
        for pos_tag in word['ana']:
            f_word['pos_tags'].append(format_pos_tag(pos_tag))
                        
    else:
        f_word['pos_tags'].append({'pos': 'X', 'tag': '_'})
        
    if len(f_word['pos_tags']) == 1:
        f_word['main_pos_tag_no'] = 0
    
    return f_word
            

def process_pos(pos_tag):
    
    f_pos = str
    f_tag = {}
    if pos_tag['gr.pos'] in ['ADV', 'CONJ', 'NUM', 'PART']:
        f_pos = pos_tag['gr.pos']
        
    elif pos_tag['gr.pos'] == 'A':
        f_pos = 'ADJ'
        
    elif pos_tag['gr.pos'] == 'APRO':
        f_pos = 'ADJ'
        f_tag['AdjType'] = 'Pron'
        
    elif pos_tag['gr.pos'] == 'ADVPRO':
        f_pos = 'ADV'
        f_tag['AdvType'] = 'Pron'
    
    elif pos_tag['gr.pos'] == 'IMIT':
        f_pos = 'ADV'
        f_tag['AdvType'] = 'Imit'
        
    elif pos_tag['gr.pos'] == 'INTRJ':
        f_pos = 'INTJ'
        
    elif pos_tag['gr.pos'] == 'N':
        if 'gr.nType' in pos_tag.keys() and "PN" in pos_tag['gr.nType']:
            f_pos = 'PROPN'
        else:
            f_pos = 'NOUN'
            
    elif pos_tag['gr.pos'] == 'PARENTH':
        f_pos = 'ADV'
        f_tag['AdvType'] = 'Parenth'
        
    elif pos_tag['gr.pos'] == 'POST':
        f_pos = 'ADP'
        f_tag['AdpType'] = 'Post'
        
    elif pos_tag['gr.pos'] == 'PREDIC':
        f_pos = 'AUX'
        
    elif pos_tag['gr.pos'] == 'PRO':
        f_pos = 'PRON'
        
    elif pos_tag['gr.pos'] == 'V':
        f_pos = 'VERB'
        
    else:
        f_pos = 'X'
        
    return f_pos, f_tag


def add(pos_tag):
    
    f_tag = {}
    if 'gr.add' in pos_tag.keys():
        if 'abbr' in pos_tag['gr.add']:
            f_tag['Abbr'] = 'Yes'
            
        if 'add' in pos_tag['gr.add']:
            f_tag['Clitic'] = 'Add'
        
        if 'missp' in pos_tag['gr.add']:
            f_tag['Typo'] = 'Yes'
        
        if 'rus' in pos_tag['gr.add']:
            f_tag['Rus'] = 'Yes'
    
    return f_tag



def nType(pos_tag):
    
    f_tag = {}
    if 'gr.nType' in pos_tag.keys():
        if 'dim' in pos_tag['gr.nType']:
            f_tag['Derivation'] = 'Dimin'
            
        if 'hum' in pos_tag['gr.nType']:
            f_tag['Animacy'] = 'Hum'
        elif 'anim' in pos_tag['gr.nType']:
            f_tag['Animacy'] = 'Anim'
        elif 'anim' in pos_tag['gr.nType']:
            f_tag['Animacy'] = 'Supernat'
            
        if 'persn' in pos_tag['gr.nType']:
            f_tag['PropnType'] = 'PersN'
        elif 'patrn' in pos_tag['gr.nType']:
            f_tag['PropnType'] = 'PatrN'
        elif 'famn' in pos_tag['gr.nType']:
            f_tag['PropnType'] = 'FamN'
        elif 'topn' in pos_tag['gr.nType']:
            f_tag['PropnType'] = 'TopN'
        
        if 'body' in pos_tag['gr.nType']:
            f_tag['NounType'] = 'BodyPart'
        elif 'time_meas' in pos_tag['gr.nType']:
            f_tag['NounType'] = 'TimeMeas'
        elif 'transport' in pos_tag['gr.nType']:
            f_tag['NounType'] = 'Transport'
            
    return f_tag


def case(pos_tag):
    
    f_tag = {}
    if 'gr.case' in pos_tag.keys():
        if 'abl' in pos_tag['gr.case']:
            f_tag['Case'] = 'Abl'
        elif 'all' in pos_tag['gr.case']:
            f_tag['Case'] = 'Lat'
        elif 'car' in pos_tag['gr.case']:
            f_tag['Case'] = 'Abe'
        elif 'com' in pos_tag['gr.case']:
            f_tag['Case'] = 'Com'
        elif 'comp' in pos_tag['gr.case']:
            f_tag['Case'] = 'Comp'
        elif 'csl' in pos_tag['gr.case']:
            f_tag['Case'] = 'Cau'
        elif 'dat' in pos_tag['gr.case']:
            f_tag['Case'] = 'Dat'
        elif 'el' in pos_tag['gr.case']:
            f_tag['Case'] = 'Ela'
        elif 'gen' in pos_tag['gr.case']:
            f_tag['Case'] = 'Gen'
        elif 'ill' in pos_tag['gr.case']:
            f_tag['Case'] = 'Ill'
        elif 'loc' in pos_tag['gr.case']:
            f_tag['Case'] = 'Ine'
        elif 'nom' in pos_tag['gr.case']:
            f_tag['Case'] = 'Nom'
        elif 'prol' in pos_tag['gr.case']:
            f_tag['Case'] = 'Prl'
        elif 'temp' in pos_tag['gr.case']:
            f_tag['Case'] = 'Temp'
        elif 'trans' in pos_tag['gr.case']:
            f_tag['Case'] = 'Tra'
    
    return f_tag


def number(pos_tag):
    
    f_tag = {}
    if 'gr.number' in pos_tag.keys():
        if type(pos_tag['gr.number']) == list:
            number_tag = pos_tag['gr.number']
        else:
            number_tag = []
            number_tag.append(pos_tag['gr.number'])
            
        if 'sg' in number_tag:
            f_tag['Number'] = 'Sing'
        elif 'pl' in number_tag:
            f_tag['Number'] = 'Plur'
            
        if 'sg.s' in number_tag:
            f_tag['Number[subj]'] = 'Sing'
        elif 'pl.s' in number_tag:
            f_tag['Number[subj]'] = 'Plur'
        
        if 'sg.o' in number_tag:
            f_tag['Number[obj]'] = 'Sing'
        elif 'pl.o' in number_tag:
            f_tag['Number[obj]'] = 'Plur'
            
    return f_tag


def poss(pos_tag):
    
    f_tag = {}
    if 'gr.poss' in pos_tag.keys():
        if 'def' in pos_tag['gr.poss']:
            f_tag['Definite'] = 'Def'
        else:
            if pos_tag['gr.poss'].endswith('sg'):
                f_tag['Number[psor]'] = 'Sing'
            elif pos_tag['gr.poss'].endswith('pl'):
                f_tag['Number[psor]'] = 'Plur'
                
            if pos_tag['gr.poss'].startswith('1'):
                f_tag['Person[psor]'] = '1'
            elif pos_tag['gr.poss'].startswith('2'):
                f_tag['Person[psor]'] = '2'
            elif pos_tag['gr.poss'].startswith('3'):
                f_tag['Person[psor]'] = '3'
    
    return f_tag


def v_subcat(pos_tag):
    
    f_tag = {}
    if 'gr.v_subcat' in pos_tag.keys():
        if 'intr' in pos_tag['gr.v_subcat']:
            f_tag['Transitivity'] = 'Intr'
        elif 'tr' in pos_tag['gr.v_subcat']:
            f_tag['Transitivity'] = 'Tr'
        elif 'impers' in pos_tag['gr.v_subcat']:
            f_tag['Transitivity'] = 'Impers'
    
    return f_tag


def v_form(pos_tag):
    
    f_tag = {}
    if 'gr.v_form' in pos_tag.keys():
        if 'inf' in pos_tag['gr.v_form']:
            f_tag['VerbForm'] = 'Inf'
        elif 'imp' in pos_tag['gr.v_form']:
            f_tag['Mood'] = 'Imp'
        elif 'neg' in pos_tag['gr.v_form']:
            f_tag['Connegative'] = 'Yes'
        elif 'non_obj' in pos_tag['gr.v_form']:
            f_tag['Conjug'] = 'NonObj'
        elif 'cvb' in pos_tag['gr.v_form']:
            f_tag['VerbForm'] = 'Conv'
            if 'cvb.sim' in pos_tag['gr.v_form']:
                f_tag['CvbType'] = 'Simult'
        elif 'nmlz' in pos_tag['gr.v_form']:
            f_tag['VerbForm'] = 'Vnoun'
            if 'nmlz_mka' in pos_tag['gr.v_form']:
                f_tag['VnounType'] = 'Instr'
            
    return f_tag


def pers(pos_tag):
    
    f_tag = {}
    if 'gr.pers' in pos_tag.keys():
        if type(pos_tag['gr.pers']) == list:
            pers_tag = pos_tag['gr.pers']
        else:
            pers_tag = []
            pers_tag.append(pos_tag['gr.pers'])
            
        if '1' in pers_tag:
            f_tag['Person'] = '1'
        elif '2' in pers_tag:
            f_tag['Person'] = '2'
        elif '3' in pers_tag:
            f_tag['Person'] = '3'
        else:        
            
            if '1.s' in pers_tag:
                f_tag['Person[subj]'] = '1'
            elif '2.s' in pers_tag:
                f_tag['Person[subj]'] = '2'
            elif '3.s' in pers_tag:
                f_tag['Person[subj]'] = '3'
        
            if '1.o' in pers_tag:
                f_tag['Person[obj]'] = '1'
            elif '2.o' in pers_tag:
                f_tag['Person[obj]'] = '2'
            elif '3.o' in pers_tag:
                f_tag['Person[obj]'] = '3'
            
    return f_tag


def tense(pos_tag):
    
    f_tag = {}
    if 'gr.tense' in pos_tag.keys():
        if pos_tag['gr.tense'] == 'pst':
            f_tag['Tense'] = 'Prt1'
        elif pos_tag['gr.tense'] == 'npst':
            f_tag['Tense'] = 'Pres'
        elif pos_tag['gr.tense'] == 'pst2':
            f_tag['Tense'] = 'Prt2'
    
    return f_tag


def v_deriv(pos_tag):
    
    f_tag = {}
    if 'gr.v_deriv' in pos_tag.keys():
        if 'caus' in pos_tag['gr.v_deriv']:
            f_tag['Caus'] = 'Yes'
            
        if 'pass' in pos_tag['gr.v_deriv']:
            f_tag['Voice'] = 'Pass'
            
        if 'iter' in pos_tag['gr.v_deriv']:
            f_tag['Aspect'] = 'Iter'
        elif 'inch' in pos_tag['gr.v_deriv']:
            f_tag['Aspect'] = 'Inch'
            
        if 'mult' in pos_tag['gr.v_deriv']:
            f_tag['Mult'] = 'Yes'
    
    return f_tag


def ptcp_form(pos_tag):
    
    f_tag = {}
    if 'gr.ptcp_form' in pos_tag.keys():
        if 'ptcp.pst' in pos_tag['gr.ptcp_form']:
            f_tag['VerbForm'] = 'Part'
            f_tag['PtcpType'] = 'Res'
        elif 'ptcp.prs.pass' in pos_tag['gr.ptcp_form']:
            f_tag['VerbForm'] = 'Part'
            f_tag['Voice'] = 'Pass'
    
    return f_tag


def num_deriv(pos_tag):
    
    f_tag = {}
    if 'gr.num_deriv' in pos_tag.keys():
        if 'ord' in pos_tag['gr.num_deriv']:
            f_tag['NumType'] = 'Ord'
        elif 'num_approx' in pos_tag['gr.num_deriv']:
            f_tag['NumType'] = 'Approx'
        elif 'distr' in pos_tag['gr.num_deriv']:
            f_tag['NumType'] = 'Dist'
        elif 'coll' in pos_tag['gr.num_deriv']:
            f_tag['NumType'] = 'Sets'
        elif 'pair' in pos_tag['gr.num_deriv']:
            f_tag['NumType'] = 'Pair'
    
    return f_tag


def proType(pos_tag):
    
    f_tag = {}
    if 'gr.proType' in pos_tag.keys():
        if 'refl' in pos_tag['gr.proType']:
            f_tag['PronType'] = 'Refl'
    
    return f_tag


def mood(pos_tag):
    
    f_tag = {}
    if 'gr.mood' in pos_tag.keys():
        if 'opt' in pos_tag['gr.mood']:
            f_tag['Mood'] = 'Opt'
        elif 'cond' in pos_tag['gr.mood']:
            f_tag['Mood'] = 'Cnd'
    
    return f_tag

def format_pos_tag(pos_tag):
    formatted_pos_tag = {}
    formatted_pos_tag['pos'], formatted_pos_tag['tag'] = process_pos(pos_tag)
    
    for func in tag_processing_functions:
        if 'gr.' + func.__name__ in pos_tag.keys():
            formatted_pos_tag['tag'].update(func(pos_tag))
            
    if 'trans_ru' in pos_tag.keys():
        formatted_pos_tag['trans_ru'] = pos_tag['trans_ru']
           
    return formatted_pos_tag 
    

tag_processing_functions = [add, nType, case, number, poss, v_subcat, v_deriv, v_form, 
             ptcp_form, pers, tense, num_deriv, proType, mood]



# import os
# import gzip


def convert_file_to_ud(file):
    
    with open(file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)
    
    text = [sentence['text'] for sentence in data['sentences']]
    formatted_data = process_text(data)
    
    with open(file[:file.index('.json')] + '_formatted.json', 'w', encoding='utf-8') as fout:
        json.dump(formatted_data, fout, ensure_ascii=False)
        
    with open(file[:file.index('.json')] + '.txt', 'w', encoding='utf-8') as fout:
        for sent in text:
            fout.write(sent + '\n')

    return formatted_data
