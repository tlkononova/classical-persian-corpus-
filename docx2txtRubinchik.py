# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 04:56:20 2016

@author: TK_adm

k = 10
f = open('.\\Persian Russian Dictionary_IvanovVB 017.docx', 'r', encoding='utf-8')
while k:
    try:
        line = f.readline()
        print(line)
        
    except:
        print('fail on line '+str(11-k))
    k -= 1
f.close()
"""


import docx

filename = r'C:\Users\TK_adm\Documents\HSE\comp_ling_progr\iranica\rubinchik\rubinchik.docx'
def getText(filename):
    doc = docx.Document(filename)
    #fullText = []
    num = 0
    for para in doc.paragraphs:
        num += 1
        if num%100 == 0:
            print(num)
        f.write(str(para.text))
        f.write('\n')
        #fullText.append(para.text)
    #return '\n'.join(fullText), num


#text, num = getText(filename)
#print(num)
with open('testwrite.txt', 'w', encoding='utf-8') as f:
    getText(filename)
    
    
    
    
#import docx2txt
#text = docx2txt.process("rubinchik.docx")
#w = open('write.txt', 'w', encoding='utf-8')
#w.write(text)



'''    
alf = set()
with open('C:\\Users\\TK_adm\\Documents\\HSE\\Persian CLTK\\Persian Russian Dictionary_IvanovVB 017.docx', 'r', encoding='utf-8') as f:
    for line in f:
        alf.add(line[0])
        
print(alf)
'''