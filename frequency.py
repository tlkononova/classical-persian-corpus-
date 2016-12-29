
path = r"C:\\Users\\TK_adm\\Documents\\HSE\\comp_ling_progr\\iranica\\collect\\poems\\"
punct = set('،', '«', '»', ':', '!', '؟', '؛','...', '.')

Lemmas = {}

with open(path+'corpus.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in Lemmas:
                Lemmas[word] += 1
            else:
                Lemmas[word] = 1
                
                
                
                
   
        
        
with open(path+'frequency.txt', 'w', encoding='utf-8') as w:
    dicSorted = sorted(Lemmas.items(), key=lambda tup: tup[1], reverse=True)
    for word in dicSorted:
        w.write(word[0]+'\t'+str(word[1])+'\n')
        #i+=1 