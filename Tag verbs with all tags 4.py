
# coding: utf-8

# In[12]:



conjs = {'و': 'CONJ', 'ک': 'CONJ', 'پر': 'PREF', 'بد': 'PREF', 'چرا': 'PREF', 'او': 'PREF'}

nas = {'': 'POS', 'ن': 'NEG', 'نه'+u'\u200c': 'NEG', 'م':'NEG'}
#nasAIU = {}
mis = {'': '', 'می': 'MI', 'همی':'MI', 'می'+u'\u200c': 'MI', 'همی'+u'\u200c':'MI'}
bes = {'':'', 'ب':'BE', 'به'+u'\u200c':'BE'}



termPres = {'م':'1SG', 'ی': '2SG', 'د':'3SG', 'یم': '1PL', 'ید':'2PL', 'ند': '3PL'}
termPresAIU = {'یم':'1SG', 'یی': '2SG', 'ید':'3SG', 'ییم': '1PL', 'یید':'2PL', 'یند': '3PL'}

termPast = {'م':'1SG', 'ی': '2SG', '':'3SG', 'یم': '1PL', 'ید':'2PL', 'ند': '3PL'}
#termPresAIU = {'یم':'1SG', 'یی': '2SG', 'ید':'3SG', 'ییم': '1PL', 'یید':'2PL', 'یند': '3PL'}


termPerf = {'ه'+u'\u200c'+'ام': ' 1SG PERF', 'ه'+u'\u200c'+'ای': ' 2SG PERF', 'ه'+u'\u200c'+'ست': ' 3SG PERF', 
         'ه'+u'\u200c'+'ایم': ' 1PL PERF', 'ه'+u'\u200c'+'اید': ' 2PL PERF', 'ه'+u'\u200c'+'است': ' 3SG PERF',
       'ه'+u'\u200c'+'اند': ' 3PL PERF',  'ه'+u'\u200c'+'ئی': ' 2SG PERF',
	   u'\u200c'+'ست': ' 3SG PERF', u'\u200c'+'است': ' 3SG PERF',
	'ست': ' 3SG PERF', 'است': ' 3SG PERF'
	   
	   }


termPerf2 = {'ه'+u'\u200c'+'استم': ' 1SG PERF2','ه'+u'\u200c'+'ستم': ' 1SG PERF2', 'ه'+u'\u200c'+'استی': ' 2SG PERF2', 
             'ه'+u'\u200c'+'ستی': ' 2SG PERF2','ه'+u'\u200c'+'استیم': ' 1PL PERF2', 'ه'+u'\u200c'+'ستیم': ' 1PL PERF2',
             'ه'+u'\u200c'+'ستید': ' 2PL PERF2', 'ه'+u'\u200c'+'استید': ' 2PL PERF2',
       'ه'+u'\u200c'+'ستند': ' 3PL PERF2', 'ه'+u'\u200c'+'استند': ' 3PL PERF2',
	   
	   u'\u200c'+'استم': ' 1SG PERF2','ستم': ' 1SG PERF2', u'\u200c'+'استی': ' 2SG PERF2', 
             'ستی': ' 2SG PERF2', u'\u200c'+'استیم': ' 1PL PERF2', 'ستیم': ' 1PL PERF2',
             'ستید': ' 2PL PERF2', u'\u200c'+'استید': ' 2PL PERF2',
       'ستند': ' 3PL PERF2', u'\u200c'+'استند': ' 3PL PERF2', 
	   'ه'+u'\u200c'+'ایست' : '3SG PERF2',  'ه'+u'\u200c'+'ئیست' : '3SG PERF2' 
	   
	   }

 
termPPerf = {'ه'+u'\u200c'+'بودم': ' 1SG PPERF', 'ه'+u'\u200c'+'بودی': ' 2SG PPERF', 'ه'+u'\u200c'+'بود': ' 3SG PPERF', 
         'ه'+u'\u200c'+'بودیم': ' 1PL PPERF', 'ه'+u'\u200c'+'بودید': ' 2PL PPERF', 'ه'+u'\u200c'+'بودند': ' 3PL PPERF'
}   

termPPerf2 = {'ه'+u'\u200c'+'بودستم': ' 1SG PPERF2', 'ه'+u'\u200c'+'بودستی': ' 2SG PPERF2', 'ه'+u'\u200c'+'بودست': ' 3SG PPERF2', 
         'ه'+u'\u200c'+'بودستیم': ' 1PL PPERF2', 'ه'+u'\u200c'+'بودستید': ' 2PL PPERF2', 'ه'+u'\u200c'+'بودستند': ' 3PL PPERF2'
}


termPerfSubj = {'ه'+u'\u200c'+'باشم': ' SG PPERF', 'ه'+u'\u200c'+'باشی': ' SG PPERF', 'ه'+u'\u200c'+'باشد': ' SG PPERF', 
         'ه'+u'\u200c'+'باشیم': ' PL PPERF', 'ه'+u'\u200c'+'باشید': ' PL PPERF', 'ه'+u'\u200c'+'باشند': ' PL PPERF',
'ه'+u'\u200c'+'بوم': ' SG PPERF', 'ه'+u'\u200c'+'بوی': ' SG PPERF', 'ه'+u'\u200c'+'بود': ' SG PPERF', 
         'ه'+u'\u200c'+'بویم': ' PL PPERF', 'ه'+u'\u200c'+'بوید': ' PL PPERF', 'ه'+u'\u200c'+'بوند': ' PL PPERF'

}


#termIRR

termInFin = {'':'INF', '':'PP', '': 'F'}

# u'\u200c' + pron
# stem[:-1] + pron if stem.endswith('ه') or stem.endswith('ة') and plur in {'جات', 'ات', 'گان'}

pronsAll = {'م': ' PRO1SG', 'ت': ' PRO2SG', 'ش': ' PRO3SG', 'مان': ' PRO1PL', 
         'تان': ' PRO2PL', 'شان': ' PRO3PL', '':'', u'\u200c'+'م': ' PRO1SG', u'\u200c'+'ت': ' PRO2SG', 
            u'\u200c'+'ش': ' PRO3SG', u'\u200c'+'مان': ' PRO1PL', 
         u'\u200c'+'تان': ' PRO2PL', u'\u200c'+'شان': ' PRO3PL'} 
pronsE = {u'\u200c'+'ام': ' PRO1SG', u'\u200c'+'ات': ' PRO2SG', u'\u200c'+'اش': ' PRO3SG',
          u'\u200c'+'امان': ' PRO1PL', 
         u'\u200c'+'اتان': ' PRO2PL', u'\u200c'+'اشان': ' PRO3PL', '':''}
pronsAIU = {'یم': ' PRO1SG', 'یت': ' PRO2SG', 'یش': ' PRO3SG', 'یمان': ' PRO1PL', 
         'یتان': ' PRO2PL', 'یشان': ' PRO3PL', '':''}

# u'\u200c' + pron
# 'ا' + pron if stem.endswith('ه')
# 'ی' + pron if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا')

ezsAll = {'ی': ' EZ', '': ''}
ezsE = {u'\u200c'+'ی': ' EZ', '': ''}
# if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا') or stem.endswith('ه')
# u'\u200c' + ez if stem.endswith('ه')




# In[13]:

#na = {'a', 'b', 'c'}
#mi= {'1', '2', '3'}
#be= {'A', 'B', 'C'}

import itertools

namibes = set(''.join(namibe) for namibe in list(itertools.product(nas, mis, bes)))


# In[ ]:




# In[ ]:

conj + (pref) + na mi be + present|past + termPres|termPast|termPerf| termPPerf|termPP| + pron

PRESENT (PRES): conj + (pref) + na mi be + present + termPres + pron
IMPERATIVE (IMP): conj + (pref) + na mi be + present + (i, id) +pron
CONJPRES: conj + (pref) + na mi be + present + alef + termPres + pron
IRREALIS (IRR): conj + (pref) + na mi be + present + termPres + (i, id) +pron
PAST (PAST): conj + na mi be + past + termPast
PERFECT (PERF): conj + na mi be + past + termPP + termPerf + pron
PERFECT2 (PERF2): conj + na mi be + past + termPP + termPerf2+ pron
IRREALISPAST (IRRP): conj + (pref) + na mi be + past + termPast + (i, id) +pron
PLUPERF (PPERF): conj + na mi be + past + termPP + termPPerf+ pron
PastParticiple (PP):  conj + na mi be + past + termPP+ pron/ez
INFINITIVE (INF): conj + na mi be + past + termINF + pron

Наклонение: 1) IND 2) IMP 3) SUB
Время: 1) PRES 2) PAST 3) PERF 4) PERF2 5) PPERF 6) PPERF2  7) IRR 8) IRRP
Лицо и число: SG1,2,3 PL1,2,3
Энклитики: 1) PRO SG1,2,3PL1,2,3
Полярность: 1. POS 2. NEG/ NEGMA
Префиксы: 1) MI, 2) BE, 3) Pref
Слитно с: 1) CONJ
Форма: INF, PP, F


# In[ ]:

#stems = {'کتاب'}

path = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\'
#w = open(path+'Nforms.txt', 'w', encoding='utf-8')

#forms = set()
k = 0

form = ''
tag = ''


pos = 'V'

conj + (pref) + na mi be + present|past + termPres|termPast|termPerf| termPPerf|termPP| + pron


def verbforms(stem):
    Forms = {}
    pos = 'V'
    
    #form, tag = addAff(conjs, form, tag)
    
    for conj in conjs:
        conjform = ''
        conjtag = ''
        conjform += conj
        conjtag += conjs[conj]
        
        for pref in prefs:
            prefform = ''
            preftag = ''
            prefform = conjform + pref
            preftag = conjtag + prefs[pref]
            
            
            for namibe in namibes:
                namibeform = ''
                namibetag = ''
                namibeform = prefform + namibe
                namibetag = preftag + namibes[namibe] #NOT READY
                
            
                presentform = namibeform + present
                presenttag = namibetag + 'PRES'
                pastform = namibeform + past
                pasttag = namibetag + 'PAST'
                
                
                for mood in moods:
                    if mood == 'IMP':
                        impmoodtag = ''
                        impmoodtag = presenttag + mood
                        for term in termImp:
                            impform = ''
                            imptag = ''
                            impform = presentform + term
                            imptag = impmoodtag + termImp[term]
                            
                            addform(impform, imptag, past)
                        
                    elif mood == 'SUB':
                        submoodtag = ''
                        submoodtag = presenttag + mood
                        
                        for term in termPerfSubj:
                            perfSubjform = ''
                            perfSubjtag = ''
                            perfSubjform = pastform + term
                            perfSubjtag = submoodtag + termPerfSubj[term]
                            
                            addform(perfSubjform, perfSubjtag, past)
                            
                        for term in termPres:
                            irrpresform = ''
                            irrprestag = ''
                            irrpresform = presentform + term + 'ی'
                            irrprestag = submoodtag + 'IRR' +termPres[term]
                            
                            addform(irrpresform, irrprestag, past)
                            
                            subjpresform = ''
                            subjprestag = ''
                            subjpresform = presentform + 'ا' + term
                            subjprestag = submoodtag + termPres[term]
                            
                            addform(subjpresform, subjprestag, past)
                            
                        for term in termPast:
                            irrpastform = ''
                            irrpasttag = ''
                            irrpastform = pastform + term + ''
                            irrpasttag = submoodtag + 'IRRP' + termPast[term]
                        
                    #elif mood == 'IND':
                        

                for comp in comps:
                    compform = ''
                    comptag = ''

                    compform = stemform + comp
                    comptag = preptag + comps[comp]



                    if compform.endswith('ی') or compform.endswith('و') or compform.endswith('ا'):
                        ezs = ezsAll
                    elif (compform.endswith('ه') or compform.endswith('ة')):
                        ezs = ezsE
                    else:
                        ezs = {'':''}
                    # if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا') or stem.endswith('ه')
                    # u'\u200c' + ez if stem.endswith('ه')

                    for ez in ezs:
                        ezform = ''
                        eztag = ''
                        ezform = compform + ez
                        eztag = comptag + ezs[ez]

                        #forms.add((ezform, eztag))

                        if ezform in corpus:
                            addform(ezform, eztag, stem)
                            '''
                            if ezform not in CorpusTagged:
                                CorpusTagged[ezform] = {pos: {}}
                                if stem not in CorpusTagged[ezform][pos]:
                                    CorpusTagged[ezform][pos][stem] = {eztag}
                                else:
                                    CorpusTagged[ezform][pos][stem].add(eztag)
                            else:
                                if stem not in CorpusTagged[ezform][pos]:
                                    CorpusTagged[ezform][pos][stem] = {eztag}
                                else:
                                    CorpusTagged[ezform][pos][stem].add(eztag)
                            '''



                    if compform.endswith('ی') or compform.endswith('و') or compform.endswith('ا'):
                        prons = pronsAIU
                    elif (compform.endswith('ه') or compform.endswith('ة')):
                        prons = pronsE
                    else:
                        prons = pronsAll

                    for pron in prons:
                        pronform = ''
                        prontag = ''
                        pronform = compform + pron
                        prontag = comptag + prons[pron]

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
                                        addform(keform, ketag, stem)
                                        '''
                                        if keform not in CorpusTagged:
                                            CorpusTagged[keform] = {pos: {}}
                                            if stem not in CorpusTagged[keform][pos]:
                                                CorpusTagged[keform][pos][stem] = {ketag}
                                            else:
                                                CorpusTagged[keform][pos][stem].add(ketag)
                                        else:
                                            if stem not in CorpusTagged[keform][pos]:
                                                CorpusTagged[keform][pos][stem] = {ketag}
                                            else:
                                                CorpusTagged[keform][pos][stem].add(ketag)
                                        '''


                            for ra in ras:
                                raform = ''
                                ratag = ''

                                raform = artform + ra
                                ratag = arttag + ras[ra]

                                if raform in corpus:
                                    addform(raform, ratag, stem)
                                    '''
                                    if raform not in CorpusTagged:
                                        CorpusTagged[raform] = {pos: {}}
                                        if stem not in CorpusTagged[raform][pos]:
                                            CorpusTagged[raform][pos][stem] = {ratag}
                                        else:
                                            CorpusTagged[raform][pos][stem].add(ratag)
                                    else:
                                        if stem not in CorpusTagged[raform][pos]:
                                            CorpusTagged[raform][pos][stem] = {ratag}
                                        else:
                                            CorpusTagged[raform][pos][stem].add(ratag)
                                    '''
                                    #forms.add((copform, coptag))

                                
def addform(form, tag, stem):
    if form not in CorpusTagged:
        CorpusTagged[form] = {pos: {}}
        if stem not in CorpusTagged[form][pos]:
            CorpusTagged[form][pos][stem] = {tag}
        else:
            CorpusTagged[form][pos][stem].add(tag)
    else:
        if pos not in CorpusTagged[form]:
            CorpusTagged[form][pos] = {}
            if stem not in CorpusTagged[form][pos]:
                CorpusTagged[form][pos][stem] = {tag}
            else:
                CorpusTagged[form][pos][stem].add(tag)
        else:
            if stem not in CorpusTagged[form][pos]:
                CorpusTagged[form][pos][stem] = {tag}
            else:
                CorpusTagged[form][pos][stem].add(tag)                            
                        
    #return Forms
#w.close()


# In[ ]:




# In[50]:




# In[12]:



conjs = {'ک': 'CONJ ', 'و': 'CONJ ', '':''}

prefs = { 'پر': 'PREF ', 'بد': 'PREF ', 'چرا': 'PREF ', 'او': 'PREF ', '':''}


nas = {'': 'POS ', 'ن': 'NEG ', 'نه'+u'\u200c': 'NEG ', 'م':'NEG '}
#nasAIU = {}
mis = {'': '', 'می': 'MI ', 'همی':'MI ', 'می'+u'\u200c': 'MI ', 'همی'+u'\u200c':'MI '}
bes = {'':'', 'ب':'BE ', 'به'+u'\u200c':'BE '}



termPres = {'م':'1SG', 'ی': '2SG', 'د':'3SG', 'یم': '1PL', 'ید':'2PL', 'ند': '3PL'}
termPresAIU = {'یم':'1SG', 'یی': '2SG', 'ید':'3SG', 'ییم': '1PL', 'یید':'2PL', 'یند': '3PL'}

termPast = {'م':'1SG', 'ی': '2SG', '':'3SG', 'یم': '1PL', 'ید':'2PL', 'ند': '3PL'}
#termPresAIU = {'یم':'1SG', 'یی': '2SG', 'ید':'3SG', 'ییم': '1PL', 'یید':'2PL', 'یند': '3PL'}


termPerf = {'ه'+u'\u200c'+'ام': ' 1SG PERF', 'ه'+u'\u200c'+'ای': ' 2SG PERF', 'ه'+u'\u200c'+'ست': ' 3SG PERF', 
         'ه'+u'\u200c'+'ایم': ' 1PL PERF', 'ه'+u'\u200c'+'اید': ' 2PL PERF', 'ه'+u'\u200c'+'است': ' 3SG PERF',
       'ه'+u'\u200c'+'اند': ' 3PL PERF',  'ه'+u'\u200c'+'ئی': ' 2SG PERF',
       u'\u200c'+'ست': ' 3SG PERF', u'\u200c'+'است': ' 3SG PERF',
    'ست': ' 3SG PERF', 'است': ' 3SG PERF'
       
       }


termPerf2 = {'ه'+u'\u200c'+'استم': ' 1SG PERF2','ه'+u'\u200c'+'ستم': ' 1SG PERF2', 'ه'+u'\u200c'+'استی': ' 2SG PERF2', 
             'ه'+u'\u200c'+'ستی': ' 2SG PERF2','ه'+u'\u200c'+'استیم': ' 1PL PERF2', 'ه'+u'\u200c'+'ستیم': ' 1PL PERF2',
             'ه'+u'\u200c'+'ستید': ' 2PL PERF2', 'ه'+u'\u200c'+'استید': ' 2PL PERF2',
       'ه'+u'\u200c'+'ستند': ' 3PL PERF2', 'ه'+u'\u200c'+'استند': ' 3PL PERF2',
       
       u'\u200c'+'استم': ' 1SG PERF2','ستم': ' 1SG PERF2', u'\u200c'+'استی': ' 2SG PERF2', 
             'ستی': ' 2SG PERF2', u'\u200c'+'استیم': ' 1PL PERF2', 'ستیم': ' 1PL PERF2',
             'ستید': ' 2PL PERF2', u'\u200c'+'استید': ' 2PL PERF2',
       'ستند': ' 3PL PERF2', u'\u200c'+'استند': ' 3PL PERF2', 
       'ه'+u'\u200c'+'ایست' : '3SG PERF2',  'ه'+u'\u200c'+'ئیست' : '3SG PERF2' 
       
       }


termPPerf = {'ه'+u'\u200c'+'بودم': ' 1SG PPERF', 'ه'+u'\u200c'+'بودی': ' 2SG PPERF', 'ه'+u'\u200c'+'بود': ' 3SG PPERF', 
         'ه'+u'\u200c'+'بودیم': ' 1PL PPERF', 'ه'+u'\u200c'+'بودید': ' 2PL PPERF', 'ه'+u'\u200c'+'بودند': ' 3PL PPERF'
}   

termPPerf2 = {'ه'+u'\u200c'+'بودستم': ' 1SG PPERF2', 'ه'+u'\u200c'+'بودستی': ' 2SG PPERF2', 'ه'+u'\u200c'+'بودست': ' 3SG PPERF2', 
         'ه'+u'\u200c'+'بودستیم': ' 1PL PPERF2', 'ه'+u'\u200c'+'بودستید': ' 2PL PPERF2', 'ه'+u'\u200c'+'بودستند': ' 3PL PPERF2'
}


termPerfSubj = {'ه'+u'\u200c'+'باشم': ' 1SG PAST', 'ه'+u'\u200c'+'باشی': ' 2SG PAST', 'ه'+u'\u200c'+'باشد': ' 3SG PAST', 
         'ه'+u'\u200c'+'باشیم': ' 1PL PAST', 'ه'+u'\u200c'+'باشید': ' 2PL PAST', 'ه'+u'\u200c'+'باشند': ' 3PL PAST',
'ه'+u'\u200c'+'بوم': ' 1SG PAST', 'ه'+u'\u200c'+'بوی': ' 2SG PAST', 'ه'+u'\u200c'+'بود': ' 3SG PAST', 
         'ه'+u'\u200c'+'بویم': ' 1PL PAST', 'ه'+u'\u200c'+'بوید': ' 2PL PAST', 'ه'+u'\u200c'+'بوند': ' 3PL PAST'

}

termImp = {'':' 2SG', 'ید':' 2PL'}

#termIRR

termInFin = {'ن':'INF', 'ه':'PP'}

# u'\u200c' + pron
# stem[:-1] + pron if stem.endswith('ه') or stem.endswith('ة') and plur in {'جات', 'ات', 'گان'}

pronsAll = {'م': ' PRO1SG', 'ت': ' PRO2SG', 'ش': ' PRO3SG', 'مان': ' PRO1PL', 
         'تان': ' PRO2PL', 'شان': ' PRO3PL', '':'', u'\u200c'+'م': ' PRO1SG', u'\u200c'+'ت': ' PRO2SG', 
            u'\u200c'+'ش': ' PRO3SG', u'\u200c'+'مان': ' PRO1PL', 
         u'\u200c'+'تان': ' PRO2PL', u'\u200c'+'شان': ' PRO3PL'} 
pronsE = {u'\u200c'+'ام': ' PRO1SG', u'\u200c'+'ات': ' PRO2SG', u'\u200c'+'اش': ' PRO3SG',
          u'\u200c'+'امان': ' PRO1PL', 
         u'\u200c'+'اتان': ' PRO2PL', u'\u200c'+'اشان': ' PRO3PL', '':''}
pronsAIU = {'یم': ' PRO1SG', 'یت': ' PRO2SG', 'یش': ' PRO3SG', 'یمان': ' PRO1PL', 
         'یتان': ' PRO2PL', 'یشان': ' PRO3PL', '':''}

# u'\u200c' + pron
# 'ا' + pron if stem.endswith('ه')
# 'ی' + pron if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا')

ezsAll = {'ی': ' EZ', '': ''}
ezsE = {u'\u200c'+'ی': ' EZ', '': ''}
# if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا') or stem.endswith('ه')
# u'\u200c' + ez if stem.endswith('ه')

moods = {'IND', 'IMP', 'SUB', ''}


# In[25]:


import itertools


termPerfAll = termPerf.copy()
termPerfAll.update(termPerf2)
termPerfAll.update(termPPerf)
termPerfAll.update(termPPerf2)


# In[26]:


def getnamibes():
    #namibes = set(''.join(namibe) for namibe in list(itertools.product(nas, mis, bes)))

    forms = list(''.join(namibe) for namibe in list(itertools.product(nas, mis, bes)))
    tags = list(itertools.product(nas.values(), mis.values(), bes.values()))
    standarttags = []

    for tagset in tags:
        na = ''
        mi = ''
        be = ''
        for tag in tagset:
            
            #print(type(tag))
            #print(tag)
            if 'NEG' in tag:
                #print('NEG in')
                na = tag
            elif 'MI' in tag:
                mi = tag
            elif 'BE' in tag:
                be = tag
        standarttags.append(na + mi + be)

    namibes = dict(zip(forms,standarttags))

    return namibes


# In[53]:

path = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\'
#w = open(path+'Nforms.txt', 'w', encoding='utf-8')

#forms = set()
k = 0

form = ''
tag = ''
CorpusTagged = {}

pos = 'V'

#conj + (pref) + na mi be + present|past + termPres|termPast|termPerf| termPPerf|termPP| + pron

#Forms = set()

def verbforms(past, present):
    Forms = set()
    pos = 'V'
    
    #form, tag = addAff(conjs, form, tag)
    
    for conj in conjs:
        conjform = ''
        conjtag = ''
        conjform += conj
        conjtag += conjs[conj]
        
        for pref in prefs:
            prefform = ''
            preftag = ''
            prefform = conjform + pref
            preftag = conjtag + prefs[pref]
            
            
            for namibe in namibes:
                namibeform = ''
                namibetag = ''
                namibeform = prefform + namibe
                namibetag = preftag + namibes[namibe] 
                
            
                presentform = namibeform + present
                presenttag = namibetag #+ 'PRES'
                pastform = namibeform + past
                pasttag = namibetag #+ 'PAST'
                
                
                for mood in moods:
                    if mood == 'IMP':
                        impmoodtag = ''
                        impmoodtag = presenttag + mood
                        for term in termImp:
                            impform = ''
                            imptag = ''
                            impform = presentform + term
                            imptag = impmoodtag + termImp[term]
                            
                            pronforms = set()
                            pronforms = addPron(impform, imptag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                        
                    elif mood == 'SUB':
                        submoodtag = ''
                        submoodtag = presenttag + mood
                        
                        for term in termPerfSubj:
                            perfSubjform = ''
                            perfSubjtag = ''
                            perfSubjform = pastform + term
                            perfSubjtag = submoodtag + termPerfSubj[term]
                            
                            pronforms = set()
                            pronforms = addPron(perfSubjform, perfSubjtag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                            
                        for term in termPres:
                            irrpresform = ''
                            irrprestag = ''
                            irrpresform = presentform + term + 'ی'
                            irrprestag = submoodtag + ' IRR ' +termPres[term]
                            
                            pronforms = set()
                            pronforms = addPron(irrpresform, irrprestag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                            
                            subjpresform = ''
                            subjprestag = ''
                            subjpresform = presentform + 'ا' + term
                            subjprestag = submoodtag + ' PRES ' +termPres[term]
                            
                            pronforms = set()
                            pronforms = addPron(subjpresform, subjprestag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                            
                        for term in termPast:
                            irrpastform = ''
                            irrpasttag = ''
                            irrpastform = pastform + term + 'ی'
                            irrpasttag = submoodtag + ' IRRP ' + termPast[term]
                            
                            pronforms = set()
                            pronforms = addPron(irrpastform, irrpasttag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                        
                    elif mood == 'IND':
                        indmoodtag = ''
                        indmoodtag = presenttag + mood
                        
                        for term in termPres:
                            presform = ''
                            prestag = ''
                            presform = presentform + term
                            prestag = indmoodtag + ' PRES ' +termPres[term]
                            
                            pronforms = set()
                            pronforms = addPron(presform, prestag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                                
                                
                        for term in termPerfAll:
                            perfform = ''
                            perftag = ''
                            perfform = pastform + term
                            perftag = indmoodtag +termPerfAll[term]
                            
                            pronforms = set()
                            pronforms = addPron(perfform, perftag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                                
                        for term in termPast:
                            pstform = ''
                            psttag = ''
                            pstform = pastform + term
                            psttag = indmoodtag + ' PAST ' +termPast[term]
                            
                            pronforms = set()
                            pronforms = addPron(pstform, psttag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                       
                    elif mood == '':
                        for term in termInFin:
                            infform = ''
                            inftag = ''
                            infform = past + term
                            inftag = termInFin[term]
                            
                            pronforms = set()
                            pronforms = addPron(infform, inftag)
                            for pronform, prontag in pronforms:
                                addform(pronform, prontag, past)
                                Forms.add((pronform, prontag, past))
                            '''
                            if infform.endswith('ه'):
                                ezs = ezsE
                            for ez in ezs:
                                ezform = ''
                                eztag = ''
                                ezform = compform + ez
                                eztag = comptag + ezs[ez]
                                
                                addform(ezform, eztag, past)
                                Forms.add((ezform, eztag, past))

                            '''
                    '''

                    if compform.endswith('ی') or compform.endswith('و') or compform.endswith('ا'):
                        ezs = ezsAll
                    elif (compform.endswith('ه') or compform.endswith('ة')):
                        ezs = ezsE
                    else:
                        ezs = {'':''}
                    # if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا') or stem.endswith('ه')
                    # u'\u200c' + ez if stem.endswith('ه')

                    for ez in ezs:
                        ezform = ''
                        eztag = ''
                        ezform = compform + ez
                        eztag = comptag + ezs[ez]

                        #forms.add((ezform, eztag))

                        if ezform in corpus:
                            addform(ezform, eztag, stem)
                            



                    if compform.endswith('ی') or compform.endswith('و') or compform.endswith('ا'):
                        prons = pronsAIU
                    elif (compform.endswith('ه') or compform.endswith('ة')):
                        prons = pronsE
                    else:
                        prons = pronsAll

                    for pron in prons:
                        pronform = ''
                        prontag = ''
                        pronform = compform + pron
                        prontag = comptag + prons[pron]

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
                                        addform(keform, ketag, stem)
                                        


                            for ra in ras:
                                raform = ''
                                ratag = ''

                                raform = artform + ra
                                ratag = arttag + ras[ra]

                                if raform in corpus:
                                    addform(raform, ratag, stem)
                                   
                                    #forms.add((copform, coptag))
                    '''
                    
    return Forms
#def addform(form, tag, stem):
                                
def addform(form, tag, stem):
    if form not in CorpusTagged:
        CorpusTagged[form] = {pos: {}}
        if stem not in CorpusTagged[form][pos]:
            CorpusTagged[form][pos][stem] = {tag}
        else:
            CorpusTagged[form][pos][stem].add(tag)
    else:
        if pos not in CorpusTagged[form]:
            CorpusTagged[form][pos] = {}
            if stem not in CorpusTagged[form][pos]:
                CorpusTagged[form][pos][stem] = {tag}
            else:
                CorpusTagged[form][pos][stem].add(tag)
        else:
            if stem not in CorpusTagged[form][pos]:
                CorpusTagged[form][pos][stem] = {tag}
            else:
                CorpusTagged[form][pos][stem].add(tag)                            
                        
    #return Forms
#w.close()


def addPron(prevform, prevtag):
    pronforms = set()
    if prevform.endswith('ی') or prevform.endswith('و') or prevform.endswith('ا'):
        prons = pronsAIU
    elif (prevform.endswith('ه') or prevform.endswith('ة')):
        prons = pronsE
    else:
        prons = pronsAll

    for pron in prons:
        pronform = ''
        prontag = ''
        pronform = prevform + pron
        prontag = prevtag + prons[pron]
        
        pronforms.add((pronform, prontag))
        
    return pronforms


# In[44]:

namibes = getnamibes()

#namibes


# In[52]:

past, present = 'شد', 'شو'

Forms = verbforms(past, present)
path = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\code\\'
file = 'verbforms_test.txt'
with open(path+file, 'w', encoding='utf-8') as w:
    for form in Forms:
        w.write('\t'.join(form))
        w.write('\n')


# In[ ]:




# # TRY IT ALL

# In[55]:







conjs = {'ک': 'CONJ ', 'و': 'CONJ ', '':''}

prefs = { 'پر': 'PREF ', 'بد': 'PREF ', 'چرا': 'PREF ', 'او': 'PREF ', '':''}


nas = {'': 'POS ', 'ن': 'NEG ', 'نه'+u'\u200c': 'NEG ', 'م':'NEG '}
#nasAIU = {}
mis = {'': '', 'می': 'MI ', 'همی':'MI ', 'می'+u'\u200c': 'MI ', 'همی'+u'\u200c':'MI '}
bes = {'':'', 'ب':'BE ', 'به'+u'\u200c':'BE '}



termPres = {'م':'1SG', 'ی': '2SG', 'د':'3SG', 'یم': '1PL', 'ید':'2PL', 'ند': '3PL'}
termPresAIU = {'یم':'1SG', 'یی': '2SG', 'ید':'3SG', 'ییم': '1PL', 'یید':'2PL', 'یند': '3PL'}

termPast = {'م':'1SG', 'ی': '2SG', '':'3SG', 'یم': '1PL', 'ید':'2PL', 'ند': '3PL'}
#termPresAIU = {'یم':'1SG', 'یی': '2SG', 'ید':'3SG', 'ییم': '1PL', 'یید':'2PL', 'یند': '3PL'}


termPerf = {'ه'+u'\u200c'+'ام': ' 1SG PERF', 'ه'+u'\u200c'+'ای': ' 2SG PERF', 'ه'+u'\u200c'+'ست': ' 3SG PERF', 
         'ه'+u'\u200c'+'ایم': ' 1PL PERF', 'ه'+u'\u200c'+'اید': ' 2PL PERF', 'ه'+u'\u200c'+'است': ' 3SG PERF',
       'ه'+u'\u200c'+'اند': ' 3PL PERF',  'ه'+u'\u200c'+'ئی': ' 2SG PERF',
       u'\u200c'+'ست': ' 3SG PERF', u'\u200c'+'است': ' 3SG PERF',
    'ست': ' 3SG PERF', 'است': ' 3SG PERF'
       
       }


termPerf2 = {'ه'+u'\u200c'+'استم': ' 1SG PERF2','ه'+u'\u200c'+'ستم': ' 1SG PERF2', 'ه'+u'\u200c'+'استی': ' 2SG PERF2', 
             'ه'+u'\u200c'+'ستی': ' 2SG PERF2','ه'+u'\u200c'+'استیم': ' 1PL PERF2', 'ه'+u'\u200c'+'ستیم': ' 1PL PERF2',
             'ه'+u'\u200c'+'ستید': ' 2PL PERF2', 'ه'+u'\u200c'+'استید': ' 2PL PERF2',
       'ه'+u'\u200c'+'ستند': ' 3PL PERF2', 'ه'+u'\u200c'+'استند': ' 3PL PERF2',
       
       u'\u200c'+'استم': ' 1SG PERF2','ستم': ' 1SG PERF2', u'\u200c'+'استی': ' 2SG PERF2', 
             'ستی': ' 2SG PERF2', u'\u200c'+'استیم': ' 1PL PERF2', 'ستیم': ' 1PL PERF2',
             'ستید': ' 2PL PERF2', u'\u200c'+'استید': ' 2PL PERF2',
       'ستند': ' 3PL PERF2', u'\u200c'+'استند': ' 3PL PERF2', 
       'ه'+u'\u200c'+'ایست' : '3SG PERF2',  'ه'+u'\u200c'+'ئیست' : '3SG PERF2' 
       
       }


termPPerf = {'ه'+u'\u200c'+'بودم': ' 1SG PPERF', 'ه'+u'\u200c'+'بودی': ' 2SG PPERF', 'ه'+u'\u200c'+'بود': ' 3SG PPERF', 
         'ه'+u'\u200c'+'بودیم': ' 1PL PPERF', 'ه'+u'\u200c'+'بودید': ' 2PL PPERF', 'ه'+u'\u200c'+'بودند': ' 3PL PPERF'
}   

termPPerf2 = {'ه'+u'\u200c'+'بودستم': ' 1SG PPERF2', 'ه'+u'\u200c'+'بودستی': ' 2SG PPERF2', 'ه'+u'\u200c'+'بودست': ' 3SG PPERF2', 
         'ه'+u'\u200c'+'بودستیم': ' 1PL PPERF2', 'ه'+u'\u200c'+'بودستید': ' 2PL PPERF2', 'ه'+u'\u200c'+'بودستند': ' 3PL PPERF2'
}


termPerfSubj = {'ه'+u'\u200c'+'باشم': ' 1SG PAST', 'ه'+u'\u200c'+'باشی': ' 2SG PAST', 'ه'+u'\u200c'+'باشد': ' 3SG PAST', 
         'ه'+u'\u200c'+'باشیم': ' 1PL PAST', 'ه'+u'\u200c'+'باشید': ' 2PL PAST', 'ه'+u'\u200c'+'باشند': ' 3PL PAST',
'ه'+u'\u200c'+'بوم': ' 1SG PAST', 'ه'+u'\u200c'+'بوی': ' 2SG PAST', 'ه'+u'\u200c'+'بود': ' 3SG PAST', 
         'ه'+u'\u200c'+'بویم': ' 1PL PAST', 'ه'+u'\u200c'+'بوید': ' 2PL PAST', 'ه'+u'\u200c'+'بوند': ' 3PL PAST'

}

termImp = {'':' 2SG', 'ید':' 2PL'}

#termIRR

termInFin = {'ن':'INF', 'ه':'PP'}

# u'\u200c' + pron
# stem[:-1] + pron if stem.endswith('ه') or stem.endswith('ة') and plur in {'جات', 'ات', 'گان'}

pronsAll = {'م': ' PRO1SG', 'ت': ' PRO2SG', 'ش': ' PRO3SG', 'مان': ' PRO1PL', 
         'تان': ' PRO2PL', 'شان': ' PRO3PL', '':'', u'\u200c'+'م': ' PRO1SG', u'\u200c'+'ت': ' PRO2SG', 
            u'\u200c'+'ش': ' PRO3SG', u'\u200c'+'مان': ' PRO1PL', 
         u'\u200c'+'تان': ' PRO2PL', u'\u200c'+'شان': ' PRO3PL'} 
pronsE = {u'\u200c'+'ام': ' PRO1SG', u'\u200c'+'ات': ' PRO2SG', u'\u200c'+'اش': ' PRO3SG',
          u'\u200c'+'امان': ' PRO1PL', 
         u'\u200c'+'اتان': ' PRO2PL', u'\u200c'+'اشان': ' PRO3PL', '':''}
pronsAIU = {'یم': ' PRO1SG', 'یت': ' PRO2SG', 'یش': ' PRO3SG', 'یمان': ' PRO1PL', 
         'یتان': ' PRO2PL', 'یشان': ' PRO3PL', '':''}

# u'\u200c' + pron
# 'ا' + pron if stem.endswith('ه')
# 'ی' + pron if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا')

ezsAll = {'ی': ' EZ', '': ''}
ezsE = {u'\u200c'+'ی': ' EZ', '': ''}
# if stem.endswith('ی') or stem.endswith('و') or stem.endswith('ا') or stem.endswith('ه')
# u'\u200c' + ez if stem.endswith('ه')

moods = {'IND', 'IMP', 'SUB', ''}


# In[25]:


# In[73]:



import itertools


termPerfAll = termPerf.copy()
termPerfAll.update(termPerf2)
termPerfAll.update(termPPerf)
termPerfAll.update(termPPerf2)


# In[26]:


def getnamibes():
    #namibes = set(''.join(namibe) for namibe in list(itertools.product(nas, mis, bes)))

    forms = list(''.join(namibe) for namibe in list(itertools.product(nas, mis, bes)))
    tags = list(itertools.product(nas.values(), mis.values(), bes.values()))
    standarttags = []

    for tagset in tags:
        na = ''
        mi = ''
        be = ''
        for tag in tagset:
            
            #print(type(tag))
            #print(tag)
            if 'NEG' in tag:
                #print('NEG in')
                na = tag
            elif 'MI' in tag:
                mi = tag
            elif 'BE' in tag:
                be = tag
        standarttags.append(na + mi + be)

    namibes = dict(zip(forms,standarttags))

    return namibes


# In[53]:

path = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\'
#w = open(path+'Nforms.txt', 'w', encoding='utf-8')

#forms = set()
k = 0

form = ''
tag = ''
CorpusTagged = {}
corpus = set()
pos = 'V'

#conj + (pref) + na mi be + present|past + termPres|termPast|termPerf| termPPerf|termPP| + pron

#Forms = set()



# In[98]:

def verbforms(past, present, verbpref):
    Forms = set()
    pos = 'V'
    
    #form, tag = addAff(conjs, form, tag)
    
    for conj in conjs:
        conjform = ''
        conjtag = ''
        conjform += conj
        conjtag += conjs[conj]
        
        if verbpref:
            #print(type(verbpref))
            newprefs = prefs.copy()
            newprefs.update(verbpref)
            stem = list(verbpref.keys())[0]+past
        else:
            newprefs = prefs
            stem = past
        
        for pref in newprefs:
            prefform = ''
            preftag = ''
            prefform = conjform + pref
            preftag = conjtag + newprefs[pref]
            
            
            for namibe in namibes:
                namibeform = ''
                namibetag = ''
                namibeform = prefform + namibe
                namibetag = preftag + namibes[namibe] 
                
                presentformlist = getStem(present, namibeform)
                pastformlist = getStem(past, namibeform)
                #presentform = namibeform + present
                presenttag = namibetag #+ 'PRES'
                #pastform = namibeform + past
                pasttag = namibetag #+ 'PAST'
                
                
                for mood in moods:
                    if mood == 'IMP':
                        impmoodtag = ''
                        impmoodtag = presenttag + mood
                        for term in termImp:
                            for presentform in presentformlist:
                                impform = ''
                                imptag = ''
                                impform = presentform + term
                                imptag = impmoodtag + termImp[term]
                                
                                pronforms = set()
                                pronforms = addPron(impform, imptag)
                                for pronform, prontag in pronforms:
                                    if pronform in corpus:
                                        addform(pronform, prontag, stem)
                                    #Forms.add((pronform, prontag, past))
                        
                    elif mood == 'SUB':
                        submoodtag = ''
                        submoodtag = presenttag + mood
                        
                        for term in termPerfSubj:
                            for pastform in pastformlist:
                                perfSubjform = ''
                                perfSubjtag = ''
                                perfSubjform = pastform + term
                                perfSubjtag = submoodtag + termPerfSubj[term]
                                
                                pronforms = set()
                                pronforms = addPron(perfSubjform, perfSubjtag)
                                for pronform, prontag in pronforms:
                                    if pronform in corpus:
                                        addform(pronform, prontag, stem)
                                    #Forms.add((pronform, prontag, past))
                            
                        for term in termPres:
                            for presentform in presentformlist:
                                irrpresform = ''
                                irrprestag = ''
                                irrpresform = presentform + term + 'ی'
                                irrprestag = submoodtag + ' IRR ' +termPres[term]
                                
                                pronforms = set()
                                pronforms = addPron(irrpresform, irrprestag)
                                for pronform, prontag in pronforms:
                                    if pronform in corpus:
                                        addform(pronform, prontag, stem)
                                    #Forms.add((pronform, prontag, past))
                                
                                subjpresform = ''
                                subjprestag = ''
                                subjpresform = presentform + 'ا' + term
                                subjprestag = submoodtag + ' PRES ' +termPres[term]
                                
                                pronforms = set()
                                pronforms = addPron(subjpresform, subjprestag)
                                for pronform, prontag in pronforms:
                                    if pronform in corpus:
                                        addform(pronform, prontag, stem)
                                    #Forms.add((pronform, prontag, past))
                            
                        for term in termPast:
                            for pastform in pastformlist:
                                irrpastform = ''
                                irrpasttag = ''
                                irrpastform = pastform + term + 'ی'
                                irrpasttag = submoodtag + ' IRRP ' + termPast[term]
                                
                                pronforms = set()
                                pronforms = addPron(irrpastform, irrpasttag)
                                for pronform, prontag in pronforms:
                                    if pronform in corpus:
                                        addform(pronform, prontag, stem)
                                    #Forms.add((pronform, prontag, past))
                        
                    elif mood == 'IND':
                        indmoodtag = ''
                        indmoodtag = presenttag + mood
                        
                        for term in termPres:
                            for presentform in presentformlist:
                                presform = ''
                                prestag = ''
                                presform = presentform + term
                                prestag = indmoodtag + ' PRES ' +termPres[term]
                                
                                pronforms = set()
                                pronforms = addPron(presform, prestag)
                                for pronform, prontag in pronforms:
                                    if pronform in corpus:
                                        addform(pronform, prontag, stem)
                                    #Forms.add((pronform, prontag, past))
                                
                                
                        for term in termPerfAll:
                            for pastform in pastformlist:
                                perfform = ''
                                perftag = ''
                                perfform = pastform + term
                                perftag = indmoodtag +termPerfAll[term]
                                
                                pronforms = set()
                                pronforms = addPron(perfform, perftag)
                                for pronform, prontag in pronforms:
                                    if pronform in corpus:
                                        addform(pronform, prontag, stem)
                                    #Forms.add((pronform, prontag, past))
                                
                        for term in termPast:
                            for pastform in pastformlist:
                                pstform = ''
                                psttag = ''
                                pstform = pastform + term
                                psttag = indmoodtag + ' PAST ' +termPast[term]
                                
                                pronforms = set()
                                pronforms = addPron(pstform, psttag)
                                for pronform, prontag in pronforms:
                                    if pronform in corpus:
                                        addform(pronform, prontag, stem)
                                    #Forms.add((pronform, prontag, past))
                       
                    elif mood == '':
                        for term in termInFin:
                            infform = ''
                            inftag = ''
                            infform = past + term
                            inftag = termInFin[term]
                            
                            pronforms = set()
                            pronforms = addPron(infform, inftag)
                            for pronform, prontag in pronforms:
                                if pronform in corpus:
                                    addform(pronform, prontag, stem)
                                #Forms.add((pronform, prontag, past))
                            '''
                            if infform.endswith('ه'):
                                ezs = ezsE
                            for ez in ezs:
                                ezform = ''
                                eztag = ''
                                ezform = compform + ez
                                eztag = comptag + ezs[ez]
                                
                                addform(ezform, eztag, past)
                                Forms.add((ezform, eztag, past))

                            '''
                    
                    
    #return Forms
#def addform(form, tag, stem):
                                
def addform(form, tag, stem):
    if form not in CorpusTagged:
        CorpusTagged[form] = {pos: {}}
        if stem not in CorpusTagged[form][pos]:
            CorpusTagged[form][pos][stem] = {tag}
        else:
            CorpusTagged[form][pos][stem].add(tag)
    else:
        if pos not in CorpusTagged[form]:
            CorpusTagged[form][pos] = {}
            if stem not in CorpusTagged[form][pos]:
                CorpusTagged[form][pos][stem] = {tag}
            else:
                CorpusTagged[form][pos][stem].add(tag)
        else:
            if stem not in CorpusTagged[form][pos]:
                CorpusTagged[form][pos][stem] = {tag}
            else:
                CorpusTagged[form][pos][stem].add(tag)                            
                        
    #return Forms
#w.close()


def addPron(prevform, prevtag):
    pronforms = set()
    if prevform.endswith('ی') or prevform.endswith('و') or prevform.endswith('ا'):
        prons = pronsAIU
    elif (prevform.endswith('ه') or prevform.endswith('ة')):
        prons = pronsE
    else:
        prons = pronsAll

    for pron in prons:
        pronform = ''
        prontag = ''
        pronform = prevform + pron
        prontag = prevtag + prons[pron]
        
        pronforms.add((pronform, prontag))
        
    return pronforms

    
def getStem(present, namibe):
    if present.startswith('آ') and namibe:
        newpresent =  'ا'+present[1:]
        return [namibe+present, namibe+newpresent]
    elif (present.startswith('ای') or present.startswith('او')) and namibe:
        newpresent = present[1:]
        return [namibe+present, namibe+newpresent]
    elif present.startswith('ا') and namibe:
        newpresent = present[1:]
        newpresent2 = 'ی' + present
        newpresent3 = 'ی' + present[1:]
        return [namibe+present, namibe+newpresent, namibe+newpresent2, namibe+newpresent3]
    else:
        return [namibe+present]


def getPref(past, present):
    verbprefs = ('اندر', 'در', 'باز', 'بر', 'فرو')
    #if past, present in prefverbs:
    if past[:2] in verbprefs:
        #print('pref in!')
        verbpref = past[:2]
        #print(verbpref)
        newpast = past[2:]
        #print(newpast)
        newpresent = present[2:]
        #print(newpresent)
        return newpast, newpresent, {verbpref:'PREF '}
    elif past[:3] in verbprefs:
        verbpref = past[:3]
        newpast = past[3:]
        newpresent = present[3:]
        return newpast, newpresent, {verbpref:'PREF '}
    elif past[:4] in verbprefs:
        verbpref = past[:4]
        newpast = past[4:]
        newpresent = present[4:]
        
        return newpast, newpresent, {verbpref:'PREF '}
    else:
       verbpref = ''
       newpast = past
       newpresent = present
       return newpast, newpresent, {verbpref:''}
# In[44]:



namibes = getnamibes()

#namibes


# In[52]:

past, present = 'انداخت', 'انداز'

Forms = verbforms(past, present, False)
path = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\code\\'
file = 'verbforms_test2.txt'
with open(path+file, 'w', encoding='utf-8') as w:
    for form in Forms:
        w.write('\t'.join(form))
        w.write('\n')


# In[ ]:



# In[75]:

namibes = getnamibes()

corpus = set()
corpusfile = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\collect\\corpus_doc2\\wordlist.txt'
with open(corpusfile, 'r', encoding='utf-8') as c:
    for line in c:
        word = line.strip('\n')
        corpus.add(word)


# In[76]:

verbfile = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\allverbs_duble.txt'
#verbfile = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\allverbs_duble_test.txt'

prefverbfile = 'C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\data\\prefverbs_short.txt'
verbs = set()
prefverbs = set()

with open(verbfile, 'r', encoding='utf-8') as f:
    for line in f:
        past, present = line.strip('\n').split('\t')
        verbs.add((past, present))


# In[77]:

k = 0
for past, present in verbs:
    k += 1
    print(k)
    #if k %50 == 0:
    #    print(k)
    verbforms(past, present, False)
    


# In[ ]:


with open(prefverbfile, 'r', encoding='utf-8') as f:
  for line in f:
      past, present = line.strip('\n').split('\t')
      prefverbs.add((past, present))
      
for past, present in prefverbs:
  #newpast, newpresent, verbpref = getPref(past, present)
  present, past, verbpref = getPref(past, present)
  verbforms(present, past, verbpref)


# In[ ]:


with open('TaggedWords_verb.txt', 'w', encoding='utf-8') as w: 
    for form in sorted(CorpusTagged):
        w.write(form+'\t')
        for pos in CorpusTagged[form]:
            w.write(pos+'$')
            for lemma in CorpusTagged[form][pos]:
                w.write(lemma)
                w.write('+')
                for tag in CorpusTagged[form][pos][lemma]:
                    w.write(tag)
                    w.write('#')
                #w.write('@')
        w.write('\n')


# In[ ]:




# In[78]:

len(CorpusTagged)


# In[92]:

CorpusTagged.keys()


# In[80]:

CorpusTagged['چراباشی']


# In[99]:

present, past, verbpref = getPref('برداشت', 'بردار')
verbforms(present, past, verbpref)


# In[100]:

len(CorpusTagged)
CorpusTagged['برداشتمی']

