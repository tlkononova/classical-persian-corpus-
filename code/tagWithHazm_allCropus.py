rowDic = {}

import re, csv
import os
from __future__ import unicode_literals
from hazm import *

delimiters = ['،', '«', '»', ':', '!', '؟', '؛','...', '.', '(',')', '-']


def punctsplit(delimiters, string, maxsplit=0):
    
    regexPattern = '|'.join(map(re.escape, delimiters))
    regexPattern = '(' + regexPattern+')| '
    #return re.split('('+regexPattern+')', string)
    #return re.split(regexPattern, string)
    matches = list(filter(None, re.split(regexPattern, string)))
    return matches


def punctsplit_withoutdelim(delimiters, string, maxsplit=0):
    
    regexPattern = '|'.join(map(re.escape, delimiters))
    regexPattern = regexPattern+'| '
    #return re.split('('+regexPattern+')', string)
    #return re.split(regexPattern, string)
    matches = list(filter(None, re.split(regexPattern, string)))
    return matches


def getnumwords(f):
    
    #rowDic = {}
    #sentno = 0
    #wordno = 0
    numwords = 0
    
    
    for line in f:
        if line.startswith('#'):
            continue
            
        try:
            b1, b2 = line.strip('\n').split('\t') 
        except:
            continue
        for b in [b1, b2]:
            words = punctsplit(delimiters, b.strip())
            for w in words:
                if w not in delimiters:
                    numwords += 1
            
    #print(numwords) 
    return numwords
    
    
    


def tagwithhazm(f, w):
    meta = []
    for line in f:
        #print('in')
        
        if line.startswith('#'):
            if line.startswith('#meta.'):
            #rename meta!!!
                
                meta.append(line.split('\t')[1])
                if len(meta) == 9:
                    metastring = '#meta.docid\t' + str(meta[0])
                    metastring += '#meta.author\t'+ str(meta[1])
                    metastring += '#meta.title\t'+ str(meta[2])
                    metastring += '#meta.date1\t'+ str(meta[4])
                    metastring += '#meta.date2\t'+ str(meta[3])
                    metastring += '#meta.genre\t'+ str(meta[6])# + '\n'
                    metastring += '#meta.words\t'+ str(numwords) + '\n'
                    metastring += '#meta.sentences\t'+ str(meta[7])# + '\n'
                    metastring += '#meta.date_displayed\t'+ str(meta[5])# + '\n'
                    #print('try')
                    w.write(metastring)
                    
                    
            continue
        #sentno += 1

        try:
            b1, b2 = line.strip('\n').split('\t') 
        except:
            continue
    
    
    
        
        

        
        
      
        k = 0
        for b in [b1, b2]:
            k += 1
            
            sentence = normalizer.normalize(b)

            words = punctsplit(delimiters, sentence.strip())
            
            tagged = tagger.tag(words)
            #tagged = tagger.tag(word_tokenize(words))
        

            #sentence = normalizer.normalize(line)
            #words = word_tokenize(normalizer.normalize(line))
            #sentence = ' '.join(word_tokenize(normalizer.normalize(line)))
            #tagged = tagger.tag(word_tokenize(sentence))

            for word, tag in tagged:
                w.write(word +'\t'+ tag +'\n')
            if k == 2:
                w.write('##\n')
            else:
                w.write('#\n')


    #w.close()
    
    
    


fieldnames = ['#sentno','#wordno','#lang','#graph','#word','#indexword','#nvars','#nlems','#nvar',
              '#lem','#trans','#trans_ru','#lex','#gram','#flex','#punctl','#punctr','#sent_pos']




path = "C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\collect\\corpus_doc2\\fa\\"


normalizer = Normalizer()
tagger = POSTagger(model='resources/postagger.model')


count = 0
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        oldfile = '\\'.join((dirpath, filename))
        #print('\\'.join((dirpath, filename)))
        newfile = oldfile.replace('corpus_doc2', 'tagger')
        #newfile = newfile.replace('.txt', '.prs')
        
        os.makedirs(os.path.dirname(newfile), exist_ok=True)
        
        taggedfile = open(newfile, 'w', encoding='utf-8')
        writer = csv.DictWriter(taggedfile, fieldnames=fieldnames, delimiter = '\t', restval = '', lineterminator='\n')
        writer.writeheader()
        
        #print(oldfile)
        #print(newfile)
        
        with open(oldfile, 'r', encoding='utf-8') as f:
            numwords = getnumwords(f)
        with open(oldfile, 'r', encoding='utf-8') as f:
            tagwithhazm(f, taggedfile)
            #writePRS(f, numwords)
          
        count += 1
        if count%100 == 0:
            print(count)

        taggedfile.close()