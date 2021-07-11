#12
'''
n=int(input('1-Radius, 2-Diametr , 3-Uzunligi , 4-Yuzasi'))
x=float(input('Qiymatini kiriting: '))
if n == 1 :
    d=2*x
    c=2*3.14*x
    s=3.14*x*x
    print('D=',d,'C=',c,'S=',s)    
elif n==2:
    r=x/2
    c=6.28*r
    s=3.14*r*r
    print('R=',r,'C=',c,'S=',s)    
elif n==3:
    r=x/6.28
    d=2*r    
    s=3.14*r*r
    print(r,d,s)    
elif n==4:
    r=(x/3.14)**0.5
    d=2*r    
    c=6.28*r
    print(r,d,c)
'''
#13-14 Mustaqil ish 

#15
'''
n=int(input('1 dan 4 gacha son kiriting: '))
k=int(input('6 dan 14 gacha son kiriting: '))
if 1<=n<=4 and 6<=k<=14:
    if k==6:
        natija = 'olti '
    elif k==7 :
        natija = 'yetti '    
    elif k==8 :
        natija = 'sakkiz '    
    elif k==9 :
        natija = 'to`qqiz '   
    elif k==10:
        natija = 'o`n '    
    elif k==11:
        natija = 'valet '    
    elif k==12:
        natija = 'dama '    
    elif k==13:
        natija = 'qirol '    
    else:
        natija = 'tuz'        
    
    if n==1:
        natija += 'g`isht'    
    elif n== 2:
        natija += 'olma'    
    elif n== 3:
        natija += 'chillak'    
    else:
        natija += 'qarg\'a'    
    print(natija)    
else:
    print("Masala shartiga mos son kiriting!")    
 '''
#16
'''
n=int(input('20 - 69 oraliq'))
if 20<=n<=69:
    unlar = n//10
    birlar = n%10
    if unlar == 2 :
        nat = 'yigirma '
    elif unlar == 3:
        nat = "o'ttiz "        
    elif unlar == 4:
        nat = "qirq "
    elif unlar == 5:
        nat = 'ellik '
    else:
        nat = "oltmish"  
        
    if birlar == 1:
        nat = nat + 'bir '
    elif birlar == 2:
        nat = nat + 'ikki '
    elif birlar == 3:
        nat = nat + 'uch '            
    elif birlar == 4:
        nat = nat + "to'rt "     
        #..... Davomi bor ..... 9 gacha tekshirish kerak 
        
    nat += 'yosh'
    print(nat)        
else:
    print("Masala shartiga mos son kiriting!")    
'''
#17-18 Mustaqil ish    
   
#19
'''
yil = int(input('Yilni kiriting: '))
muchal = yil % 12
rang = yil % 60

if 4<=rang<=15:
    nat = 'yashil '
elif 16<=rang <=27 :
    nat = 'qizil '    
elif 28<=rang <=39 :
    nat = 'sariq '    
elif 40<=rang <=51 :
    nat = 'oq '    
else:
    nat = 'qora '        

if muchal == 4 :
    nat += 'sichqon '
elif muchal == 5 :
    nat += 'sigir '            
elif muchal == 6 :
    nat += "yo'lbars "    
elif muchal == 7 :
    nat += "quyon "    
elif muchal == 8 :
    nat += "ajdar "        
elif muchal == 9 :
    nat += "ilon "        
elif muchal == 10 :
    nat += "ot "    
elif muchal == 11 :
    nat += "qo'y "    
elif muchal == 0 :
    nat += "maymun "        
elif muchal == 1 :
    nat += "tovuq "      
elif muchal == 2 :
    nat += "it "    
elif muchal == 3 :
    nat += "to'ng'iz "     
    
nat += 'yil'    
print(nat)
'''
#20
'''       
d=int(input('d='))     
m=int(input('m='))     

if m == 1:
    if 1<=d<=19:
        print('Echki')
    elif 20<=d<=31:
        print("qovg'a")

elif m == 2:
    if 1<=d<=18:
        print("qovg'a")       
    elif 19<=d<=29:
        print('Baliq')        

elif m == 3:
    if 1<=d<=20:
        print("Baliq")       
    elif 21<=d<=31:
        print("Qo'y")    
 
elif m == 4:
    if 1<=d<=19:
        print("Qo'y")       
    elif 20<=d<=30:
        print("Buzoq")    
        
elif m == 5:
    if 1<=d<=20:
        print("Buzoq")       
    elif 21<=d<=31:
        print("Egizaklar")    

elif m == 6:
    if 1<=d<=21:
        print("Egizaklar")       
    elif 22<=d<=30:
        print("Qisqichbaqa")       
        
elif m == 7:
    if 1<=d<=22:
        print("Qisqichbaqa")       
    elif 23<=d<=31:
        print("Arslon")               
        
elif m == 8:
    if 1<=d<=22:
        print("Arslon")       
    elif 23<=d<=31:
        print("Parizod")                       

elif m == 9:
    if 1<=d<=22:
        print("Parizod")       
    elif 23<=d<=30:
        print("Tarozi")   
        
elif m == 10:
    if 1<=d<=22:
        print("Tarozi")       
    elif 23<=d<=31:
        print("Chayon")           

elif m == 11:
    if 1<=d<=22:
        print("Chayon")       
    elif 23<=d<=30:
        print("O'q otar")           

elif m == 12:
    if 1<=d<=21:
        print("O'q otar")       
    elif 22<=d<=31:
        print("Echki")   
        
# 2-usul 

nat = m*100 + d
if 120<= nat <= 218:
    print("qovg'a")
elif 219<= nat <=320:
    print('Baliq') 
elif 321<= nat <=419:
    print('Qo\'y') 
elif 420<= nat <=520:
    print("Buzoq")     
elif 521<= nat <=621:
    print("Egizaklar")     
elif 622<= nat <=722:
    print("Qisqichbaqa")     
elif 723<= nat <=822:
    print("Arslon")     
elif 823<= nat <=922:
    print("Parizod")     
elif 923<= nat <=1022:
    print("Tarozi")     
elif 1023<= nat <=1122:
    print("Chayon")     
elif 1123<= nat <=1221:
    print("O'qotar")     
elif 1221<= nat <=1231 or (101<=nat<=119):
    print("Echki")         
'''
