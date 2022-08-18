#Sean O'Grady#

#CSC FINAL PROJECT

def histogram():
    fin=open(r"\Users\ograd\Downloads\WordsFileText.txt")
    d1=dict()
    d2=dict()
    d3=dict()
    d4=dict()
    d5=dict()
    d6=dict()
    d7=dict()
    d8=dict()
    d9=dict()
    d10=dict()
    d11=dict()
    d12=dict()
    d13=dict()
    d14=dict()
    d15=dict()
    d16=dict()
    d17=dict()
    d18=dict()
    d19=dict()
    d20=dict()
    
    for line in fin:
        word=line.strip()
        if len(word)==2:
            d1[word]=d1.get(1,0)+1
            qw=len(d1)
        elif len(word)==3:
            d2[word]=d2.get(1,0)+1
            qe=len(d2)
        elif len(word)==4:
            d3[word]=d3.get(1,0)+1
            qr=len(d3)
        elif len(word)==5:
            d4[word]=d4.get(1,0)+1
            qt=len(d4)
        elif len(word)==6:
            d5[word]=d5.get(1,0)+1
            qy=len(d5)
        elif len(word)==7:
            d6[word]=d6.get(1,0)+1
            qu=len(d6)
        elif len(word)==8:
            d7[word]=d7.get(1,0)+1
            qi=len(d7)
        elif len(word)==9:
            d8[word]=d8.get(1,0)+1
            qo=len(d8)
        elif len(word)==10:
            d9[word]=d9.get(1,0)+1
            qp=len(d9)
        elif len(word)==11:
            d10[word]=d10.get(1,0)+1
            qa=len(d10)
        elif len(word)==12:
            d11[word]=d11.get(1,0)+1
            qs=len(d11)
        elif len(word)==13:
            d12[word]=d12.get(1,0)+1
            qd=len(d12)
        elif len(word)==14:
            d13[word]=d13.get(1,0)+1
            qf=len(d13)
        elif len(word)==15:
            d14[word]=d14.get(1,0)+1
            qg=len(d14)
        elif len(word)==16:
            d15[word]=d15.get(1,0)+1
            qh=len(d15)
        elif len(word)==17:
            d16[word]=d16.get(1,0)+1
            qj=len(d16)
        elif len(word)==18:
            d17[word]=d17.get(1,0)+1
            qk=len(d17)
        elif len(word)==19:
            d18[word]=d18.get(1,0)+1
            ql=len(d18)
        elif len(word)==20:
            d19[word]=d19.get(1,0)+1
            qz=len(d19)
        elif len(word)==21:
            d20[word]=d20.get(1,0)+1
            qx=len(d20)
    zx=str(qw)
    zc=str(qe)
    zv=str(qr)
    zb=str(qt)
    zn=str(qy)
    zm=str(qu)
    za=str(qi)
    zs=str(qo)
    zd=str(qp)
    zf=str(qa)
    zg=str(qs)
    zh=str(qd)
    zj=str(qf)
    zk=str(qg)
    zl=str(qh)
    zq=str(qj)
    zw=str(qk)
    ze=str(ql)
    zr=str(qz)
    zt=str(qx)
    return "There are "+zx+" words in the English language with length 2.\nThere are "+zc+" words in the English language with length 3.\nThere are "+zv+" words in the English language with length 4.\nThere are "+zb+" words in the English language with length 5.\nThere are "+zn+" words in the English language with length 6.\nThere are "+zm+" words in the English language with length 7.\nThere are "+za+" words in the English language with length 8.\nThere are "+zs+" words in the English language with length 9.\nThere are "+zd+" words in the English language with length 10.\nThere are "+zf+" words in the English language with length 11.\nThere are "+zg+" words in the English language with length 12.\nThere are "+zh+" words in the English language with length 13.\nThere are "+zj+" words in the English language with length 14.\nThere are "+zk+" words in the English language with length 15.\nThere are "+zl+" words in the English language with length 16.\nThere are "+zq+" words in the English language with length 17.\nThere are "+zw+" words in the English language with length 18.\nThere are "+ze+" words in the English language with length 19.\nThere are "+zr+" words in the English language with length 20.\nThere are "+zt+" words in the English language with length 21."

print(histogram())

#END OF CODE#

