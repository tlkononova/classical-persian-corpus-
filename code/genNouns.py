path = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\'

#conj + prep + stem + plur + pron + art + ra + cop
#conj + prep + stem + plur + pron + art + ke
#conj + prep + stem + plur + ez

#conj + prep + stem + plur + pron + art + cop + ke
#conj + prep + stem + plur + pron + art + ra
#conj + prep + stem + plur + ez


conjs = {'و': 'CONJ ', '': ''}

preps = {'اندر': 'PREP ', 'در': 'PREP ', 'بر': 'PREP ', 'ز': 'PREP ', 'ب': 'PREP ', 'از': 'PREP ', 
         u'\u200c'+'به': 'PREP ', '': ''}

plursE = {u'\u200c'+'ها': 'PL', u'\u200c'+'گان': 'PL', 'ات': 'PL', 'گان': 'PL', '': 'SG'}
plursAll = {'ها': 'PL', 'ان': 'PL', '': 'SG', u'\u200c'+'ها': 'PL'}


pronsAll = {'م': ' PRO1SG', 'ت': ' PRO2SG', 'ش': ' PRO3SG', 'مان': ' PRO1PL', 
         'تان': ' PRO2PL', 'شان': ' PRO3PL', '':'', u'\u200c'+'م': ' PRO1SG', u'\u200c'+'ت': ' PRO2SG', 
            u'\u200c'+'ش': ' PRO3SG', u'\u200c'+'مان': ' PRO1PL', 
         u'\u200c'+'تان': ' PRO2PL', u'\u200c'+'شان': ' PRO3PL'} 
pronsE = {u'\u200c'+'ام': ' PRO1SG', u'\u200c'+'ات': ' PRO2SG', u'\u200c'+'اش': ' PRO3SG',
          u'\u200c'+'امان': ' PRO1PL', 
         u'\u200c'+'اتان': ' PRO2PL', u'\u200c'+'اشان': ' PRO3PL', '':'',
         'م': ' PRO1SG', 'ت': ' PRO2SG', 'ش': ' PRO3SG', 'مان': ' PRO1PL', 
         'تان': ' PRO2PL', 'شان': ' PRO3PL', u'\u200c'+'م': ' PRO1SG', u'\u200c'+'ت': ' PRO2SG', 
            u'\u200c'+'ش': ' PRO3SG', u'\u200c'+'مان': ' PRO1PL', 
         u'\u200c'+'تان': ' PRO2PL', u'\u200c'+'شان': ' PRO3PL'
         
         }
pronsAIU = {'یم': ' PRO1SG', 'یت': ' PRO2SG', 'یش': ' PRO3SG', 'یمان': ' PRO1PL', 
         'یتان': ' PRO2PL', 'یشان': ' PRO3PL', '':'',
           'م': ' PRO1SG', 'ت': ' PRO2SG', 'ش': ' PRO3SG', 'مان': ' PRO1PL', 
         'تان': ' PRO2PL', 'شان': ' PRO3PL', u'\u200c'+'م': ' PRO1SG', u'\u200c'+'ت': ' PRO2SG', 
            u'\u200c'+'ش': ' PRO3SG', u'\u200c'+'مان': ' PRO1PL', 
         u'\u200c'+'تان': ' PRO2PL', u'\u200c'+'شان': ' PRO3PL'
           
           }



artsAll = {'ی':' YEH', '': ''}
artsAIUE = {'یی': ' YEH', 'ئی': ' YEH', u'\u200c'+'یی': ' YEH', u'\u200c'+'ئی': ' YEH','': ''}

ras = {'را': ' POSTP', '': ''}


copsE = {u'\u200c'+'ام': ' COP1SG', u'\u200c'+'ای': ' COP2SG', u'\u200c'+'ست': ' COP3SG', 
         u'\u200c'+'ایم': ' COP1PL', u'\u200c'+'اید': ' COP2PL',u'\u200c'+'است': ' COP3SG',
       u'\u200c'+'اند': ' COP3PL', u'\u200c'+'م': ' COP1SG', u'\u200c'+'ی': ' COP2SG',  
         u'\u200c'+'یم': ' COP1PL', u'\u200c'+'ید': ' COP2PL', u'\u200c'+'ند': ' COP3PL', '': '',
        
          'ستم': ' COP1SG', 'ستی': ' COP2SG',  'ستیم': ' COP1PL', 'ستید': ' COP2PL',
       'ستند': ' COP3PL', u'\u200c'+'هستم': ' COP1SG', u'\u200c'+'هستی': ' COP2SG', u'\u200c'+'هست': ' COP3SG', 
         u'\u200c'+'هستیم': ' COP1PL', u'\u200c'+'هستید': ' COP2PL',
       u'\u200c'+'هستند': ' COP3PL', u'\u200c'+'ستم': ' COP1SG', u'\u200c'+'ستی': ' COP2SG',  
         u'\u200c'+'ستیم': ' COP1PL', u'\u200c'+'ستید': ' COP2PL', u'\u200c'+'ستند': ' COP3PL'
        
        }

copsAll = {'م': ' COP1SG', 'ی': ' COP2SG', 'ست': ' COP3SG', 'یم': ' COP1PL', 'ید': ' COP2PL',
       'ند': ' COP3PL', u'\u200c'+'ام': ' COP1SG', u'\u200c'+'ای': ' COP2SG', u'\u200c'+'ست': ' COP3SG', 
         u'\u200c'+'ایم': ' COP1PL', u'\u200c'+'اید': ' COP2PL',u'\u200c'+'است': ' COP3SG',
       u'\u200c'+'اند': ' COP3PL', u'\u200c'+'م': ' COP1SG', u'\u200c'+'ی': ' COP2SG',  
         u'\u200c'+'یم': ' COP1PL', u'\u200c'+'ید': ' COP2PL', u'\u200c'+'ند': ' COP3PL', '': '',
          
           'ستم': ' COP1SG', 'ستی': ' COP2SG',  'ستیم': ' COP1PL', 'ستید': ' COP2PL',
       'ستند': ' COP3PL', u'\u200c'+'هستم': ' COP1SG', u'\u200c'+'هستی': ' COP2SG', u'\u200c'+'هست': ' COP3SG', 
         u'\u200c'+'هستیم': ' COP1PL', u'\u200c'+'هستید': ' COP2PL',
       u'\u200c'+'هستند': ' COP3PL', u'\u200c'+'ستم': ' COP1SG', u'\u200c'+'ستی': ' COP2SG',  
         u'\u200c'+'ستیم': ' COP1PL', u'\u200c'+'ستید': ' COP2PL', u'\u200c'+'ستند': ' COP3PL'
          
          
          }

ezsAll = {'ی': ' EZ', '': ''}
ezsE = {u'\u200c'+'ی': ' EZ', '': ''}

kes = {'که': ' CONJ', '':''}  #if gloss.endswith('YEH')




def nounforms(stem):
    Forms = {}
    pos = 'N'
    
    
    for conj in conjs:
        conjform = ''
        conjtag = ''
        conjform += conj
        conjtag += conjs[conj]
        
        for prep in preps:
            prepform = ''
            preptag = ''
            prepform = conjform + prep
            preptag = conjtag + preps[prep]
            
            stemform = prepform + stem
            
            if (stemform.endswith('ه') or stemform.endswith('ة')):
                plurs = plursE
            else:
                plurs = plursAll
                
            for plur in plurs:
                
                plurform = ''
                plurtag = ''
                
                plurstemform = stemform
                if plur == 'ات' or plur == 'گان':
                    plurstemform = stemform[:-1]
                
                plurform = plurstemform + plur
                plurtag = preptag + plurs[plur]
                
    
                if plurform.endswith('ی') or plurform.endswith('و') or plurform.endswith('ا'):
                    ezs = ezsAll
                elif (plurform.endswith('ه') or plurform.endswith('ة')):
                    ezs = ezsE
                else:
                    ezs = {'':''}
                # if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا') or stem.endswith('ه')
                # u'\u200c' + ez if stem.endswith('ه')

                for ez in ezs:
                    ezform = ''
                    eztag = ''
                    ezform = plurform + ez
                    eztag = plurtag + ezs[ez]
                    
                    #forms.add((ezform, eztag))
                    
                    if ezform in corpus:
                        addform(ezform, eztag, stem, pos)
                
                if plurform.endswith('ی') or plurform.endswith('و') or plurform.endswith('ا'):
                    prons = pronsAIU
                elif (plurform.endswith('ه') or plurform.endswith('ة')):
                    prons = pronsE
                else:
                    prons = pronsAll
                
                for pron in prons:
                    pronform = ''
                    prontag = ''
                    pronform = plurform + pron
                    prontag = plurtag + prons[pron]
                    
                    if pronform.endswith('ی') or pronform.endswith('و') or pronform.endswith('ا') or pronform.endswith('ه') or pronform.endswith('ة'):
                        arts = artsAIUE
                    else:
                        arts = artsAll
                
                    for art in arts:
                        artform = ''
                        arttag = ''
                        artform = pronform + art
                        arttag = prontag + arts[art]
                        
                        if (artform.endswith('ه') or artform.endswith('ة')):
                                cops = copsE
                        else:
                            cops = copsAll
                                
                        for cop in cops:
                            copform = ''
                            coptag = ''
                            copform = artform + cop
                            coptag = arttag + cops[cop]
                        
                        
                            #if 'YEH' in arttag:
                            for ke in kes:
                                keform = ''
                                ketag = ''
                                keform = copform + ke
                                ketag = coptag + kes[ke]

                                #forms.add((keform, ketag))
                                
                                
                                
                                
                                if keform in corpus:
                                    addform(keform, ketag, stem, pos)
                        
                        for ra in ras:
                            raform = ''
                            ratag = ''
                            
                            raform = artform + ra
                            ratag = arttag + ras[ra]
                            
                            if raform in corpus:
                                addform(raform, ratag, stem, pos)
                                




def nounformsArab(stem):
    Forms = {}
    pos = 'N'
    
    stems = {}
    stems = {stem: 'SG'}
    for pl in arab[stem]:
        stems[pl] = 'PL'
    
    #form, tag = addAff(conjs, form, tag)
    
    for conj in conjs:
        conjform = ''
        conjtag = ''
        conjform += conj
        conjtag += conjs[conj]
        
        for prep in preps:
            prepform = ''
            preptag = ''
            prepform = conjform + prep
            preptag = conjtag + preps[prep]
            
            
        
                
            for stemform in stems:
                plurform = ''
                plurtag = ''
                plurform = prepform + stemform
                plurtag = preptag +stems[stemform]
            
                
                
    
                if plurform.endswith('ی') or plurform.endswith('و') or plurform.endswith('ا'):
                    ezs = ezsAll
                elif (plurform.endswith('ه') or plurform.endswith('ة')):
                    ezs = ezsE
                else:
                    ezs = {'':''}
                # if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا') or stem.endswith('ه')
                # u'\u200c' + ez if stem.endswith('ه')

                for ez in ezs:
                    ezform = ''
                    eztag = ''
                    ezform = plurform + ez
                    eztag = plurtag + ezs[ez]
                    
                    #forms.add((ezform, eztag))
                    
                    if ezform in corpus:
                        addform(ezform, eztag, stem, pos)
                    
                
                if plurform.endswith('ی') or plurform.endswith('و') or plurform.endswith('ا'):
                    prons = pronsAIU
                elif (plurform.endswith('ه') or plurform.endswith('ة')):
                    prons = pronsE
                else:
                    prons = pronsAll
                
                for pron in prons:
                    pronform = ''
                    prontag = ''
                    pronform = plurform + pron
                    prontag = plurtag + prons[pron]
                    
                    if pronform.endswith('ی') or pronform.endswith('و') or pronform.endswith('ا') or pronform.endswith('ه') or pronform.endswith('ة'):
                        arts = artsAIUE
                    else:
                        arts = artsAll
                
                    for art in arts:
                        artform = ''
                        arttag = ''
                        artform = pronform + art
                        arttag = prontag + arts[art]
                        
                        if (artform.endswith('ه') or artform.endswith('ة')):
                                cops = copsE
                        else:
                            cops = copsAll
                                
                        for cop in cops:
                            copform = ''
                            coptag = ''
                            copform = artform + cop
                            coptag = arttag + cops[cop]
                        
                        
                            #if 'YEH' in arttag:
                            for ke in kes:
                                keform = ''
                                ketag = ''
                                keform = copform + ke
                                ketag = coptag + kes[ke]

                                #forms.add((keform, ketag))
                                
                                
                                
                                
                                if keform in corpus:
                                    addform(keform, ketag, stem, pos)
                        
                        for ra in ras:
                            raform = ''
                            ratag = ''
                            
                            raform = artform + ra
                            ratag = arttag + ras[ra]
                            
                            if raform in corpus:
                                addform(raform, ratag, stem, pos)
                                
                            
                                
def addform(form, tag, lemm, pos):
    if form not in CorpusTagged:
        CorpusTagged[form] = {pos: {}}
        if lemm not in CorpusTagged[form][pos]:
            CorpusTagged[form][pos][lemm] = {tag}
        else:
            CorpusTagged[form][pos][lemm].add(tag)
    else:
        if pos not in CorpusTagged[form]:
            CorpusTagged[form][pos] = {}
            if lemm not in CorpusTagged[form][pos]:
                CorpusTagged[form][pos][lemm] = {tag}
            else:
                CorpusTagged[form][pos][lemm].add(tag)
        else:
            if lemm not in CorpusTagged[form][pos]:
                CorpusTagged[form][pos][lemm] = {tag}
            else:
                CorpusTagged[form][pos][lemm].add(tag) 
                

def writeCorpusTagged(filename):
    #filepath = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\'
    
    with open(filename, 'w', encoding='utf-8') as w:
        for form in sorted(CorpusTagged):
            w.write(form+'\t')
            npos = 0
            for pos in CorpusTagged[form]:
                npos += 1
                if npos == 1:
                    w.write(pos+'$')
                else:
                    w.write('&' + pos+'$')
                nlem = 0
                for lemma in CorpusTagged[form][pos]:
                    nlem+=1
                    if nlem == 1:
                        w.write(lemma)
                        w.write('+')
                    else:
                        w.write('*')
                        w.write(lemma)
                        w.write('+')
                    ntag = 0
                    for tag in CorpusTagged[form][pos][lemma]:
                        ntag += 1
                        w.write(tag)
                        if ntag != len(CorpusTagged[form][pos][lemma])
                            w.write('#')
                    #w.write('@')
            w.write('\n')
            
            
corpus = set()

corpusfilename = 'wordlist.txt'
corpusfile = ''.join((path,corpusfilename))
with open(corpusfile, 'r', encoding='utf-8') as c:
    for line in c:
        word = line.strip('\n')
        corpus.add(word)



pos = 'N'
k = 0
CorpusTagged = {}

#path = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\'
filename = 'nouns_full.txt' #'nouns.txt'
file = ''.join((path,filename))

with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        Forms = {}
        lemma = line.strip('\n')
        k += 1
        if k%100 == 0:
            print(k)
        if lemma:
            nounforms(lemma)

outfile = 'noun_tagged_new.txt'
outfilename = ''.join((path,outfile))

writeCorpusTagged(outfilename)


filename = 'arabplurals.txt'
file = ''.join((path,filename))

with open(file, 'r', encoding='utf-8') as f:
    
    for line in f:
        #Forms = {}
        sg, pl = line.strip('\n').split('\t')
        if sg not in arab:
            arab[sg] = set()
            arab[sg].add(pl)
        else:
            arab[sg].add(pl)
        k += 1
        if k%100 == 0:
            print(k)
            
            
for word in arab:
    nounformsArab(word)


outfile = 'noun_tagged_new2.txt'
outfilename = ''.join((path,outfile))

writeCorpusTagged(outfilename)