"""
Visualizing morphological data in a conllu-like form
Showing words with several postags for selecting the most appropriate one
Writing data in a .conllu file
"""

import json

def tag_as_conllu(tag):
    """
    Converting a dict of morphological tags to a 'tag1=value1|tag2=value2' string
    """
    f_tag = ''
    if type(tag) == dict:
        f_tag = '|'.join([key + '=' + value for key, value in sorted(tag.items())])
    elif type(tag) == str:
        f_tag = tag
    
    return f_tag

def print_trans_ru(pos_tag):
    """
    
    """
    if 'trans_ru' in pos_tag.keys():
        return '\t' + pos_tag['trans_ru']
    else:
        return '\t' + '_'


def word_as_conllu(word):
    """
    
    """
    word_conllu = []
    if word['main_pos_tag_no'] > 0:
        main_tag =  word['pos_tags'][word['main_pos_tag_no'] - 1]
        word_conllu.append(str(word['no_in_sent']) + '\t' + word['form'] + '\t' + main_tag['pos'] + '\t' + tag_as_conllu(main_tag['tag']) + print_trans_ru(main_tag))
        
    elif word['main_pos_tag_no'] == 0:
        word_conllu.append('\t')
        word_conllu.append(str(word['no_in_sent']) + '\t' + word['form'] + '\t' + '(1)' + '\t' + word['pos_tags'][0]['pos'] + '\t' + tag_as_conllu(word['pos_tags'][0]['tag']) + print_trans_ru(word['pos_tags'][0]))
        for i in range(1, len(word['pos_tags'])):
            # word_conllu.append('\t')
            word_conllu.append('\t\t\t' + '(' + str(i + 1) +')' + '\t' + word['pos_tags'][i]['pos'] + '\t' + tag_as_conllu(word['pos_tags'][i]['tag']) + print_trans_ru(word['pos_tags'][i]))
        word_conllu.append('\t')

    return word_conllu

def sentence_as_conllu(sent):
    print(sent['text'])
    for word in sent['words']:
        for tag in word_as_conllu(word):
            print(tag)

def text_as_conllu(text):
    for sent in text['sentences']:
        print(sentence_as_conllu(sent))
        print()

def select_tag(word):
    print('Choose tag for ' + str(word['no_in_sent']) + ' ' + word['form'])
    for i in range(1, len(word['pos_tags']) + 1):
           print('\t' + '(' + str(i) +')' + '\t' + word['pos_tags'][i-1]['pos'] + '\t' + tag_as_conllu(word['pos_tags'][i-1]['tag'])+ '\t' + word['pos_tags'][i-1]['trans_ru'])
    best_tag_no = input()
    if best_tag_no.isdecimal():
        if int(best_tag_no) in range(1, len(word['pos_tags']) + 1):
            word['main_pos_tag_no'] = int(best_tag_no)
        elif int(best_tag_no) != 0:
            print('enter a number between 1 and ' + len((word['pos_tags'])))
    else:
        print('enter a number between 1 and ' + len((word['pos_tags'])))

def check_ambiguous_in_sent(sent):
    print(sentence_as_conllu(sent))
    print()
    sent_copy = sent.copy()
    ambiguous = 0
    disambiguated = 0
    for word in sent_copy['words']:
        if word['main_pos_tag_no'] == 0:
            ambiguous += 1
            select_tag(word)
    
    if ambiguous:
        print(sentence_as_conllu(sent_copy))
        print('Ok?')
        wrong = input()
        if not input:
            sent = sent_copy.copy()
            disambiguated += ambiguous
            
        print('Notes?')
        notes = input()
        if notes:
            sent['notes'] = notes
        
    return ambiguous

def check_ambiguous_in_text(text, output_name='in_progress.json'):
    count_ambiguous = 0
    for sent in text['sentences']:
        for word in sent['words']:
            if word['main_pos_tag_no'] == 0:
                count_ambiguous += 1
    print(str(count_ambiguous) + ' ambiguous words')
    
    current_ambiguous =  count_ambiguous
    for sent in text['sentences']:
        disambiguated = check_ambiguous_in_sent(sent)
        dump_checked(text, output_name)
        current_ambiguous -= disambiguated
        print(str(count_ambiguous - current_ambiguous) + ' words disambiguated, ' + str((count_ambiguous - current_ambiguous) / count_ambiguous * 100) + '%')


def dump_checked(data, output_name='in_progress.json'):
    with open(output_name, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False)

def make_conllu_file(data, output_file='current_text.conllu.txt', info=True, trans_ru=True, notes=True):
    with open(output_file, 'w', encoding='utf-8') as fout:
        if info:
            pass
        for sentence in data['sentences']:
            fout.write(sentence_conllu(sentence, trans_ru, notes))

def sentence_conllu(sentence, trans_ru=True, notes=True):
    sent = sentence['text']
    for word in sentence['words']:
        for tag in word_as_conllu(word):
            sent += '\n' + tag
    if notes:
        if 'notes' in sentence.keys():
            sent += '\n##' + sentence['notes']
    sent += '\n------------\n'

    return sent

def read_from_conllu(infile):
    pass
