#1
'''
kunlar = ['Dushanba','Seshanba','Chorshanba','Payshanba' , '...']
n=int(input('n='))
if n==1 :
    print('Dushanba')
elif n==2:
    print('Seshanba')    
elif n==3:
    print('Chorshanba')
elif n==4:
    print('Payshanba')    
elif n==5:
    print('Juma')    
elif n==6:
    print('Shanba')
elif n==7:
    print('Yakshanba')    
else:
    print('1 dan 7 gacha kiriting!')        
print(kunlar[n-1])
    '''
#2
'''
k=int(input('n='))
if k==1 :
    print('yomon')
elif k==2:
    print('qoniqarsiz')    
elif k==3:
    print('qoniqarli')
elif k==4:
    print('yaxshi')    
elif k==5:
    print('A\'LO')    
else:
    print('Xato')     
    '''
#3
'''
n=int (input('n='))
if (n==1) or (n==2) or n==12 :
    print('qish')
elif 3<=n<=5:
    print('Bahor')    
elif 6<=n<=8:
    print('Yoz')    
elif 9<=n<=11:
    print('Kuz')    
else:
    print('1 dan 12 gacha son kiriting!')  
'''
#4
'''
n=int(input('n='))
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12 :
    print('31')
elif n==4 or n==6 or n==9 or n==11:
    print('30')    
elif n==2:
    print('28 yoki 29')
else:
    print('Yilda 12 oy mavjud!')
'''
#5
'''
a=float(input('a='))
b=float(input('b='))
amal = input('Amalni kiriting: +,-,*,/ ko\'rinishida')
if amal == '+':
    print(a+b)
elif amal == '-':
    print(a-b)
elif amal == '*':
    print(a*b)
elif amal == '/':
    print(a/b)
else: 
    print('Amalni to\'g\'ri kiriting!')
'''
#6
'''
uzunlik = float(input('Uzunlikni kiriting: '))
birlik = int(input('Birlikni kiriting: 1-dm 2-km 3-m 4-mm 5-cm '))
if birlik == 1 :
    natija = uzunlik/10
elif birlik == 2:
    natija = uzunlik * 1000    
elif birlik == 3:
    natija = uzunlik 
elif birlik == 4:
    natija = uzunlik / 1000        
elif birlik == 5:
    natija = uzunlik / 100   
print(natija,' metr')    
'''
#7
'''
ogirlik = float(input('Uzunlikni kiriting: '))
birlik = int(input('Birlikni kiriting: 1-kg 2-mg 3-g 4-t 5-sr '))
if birlik == 1 :
    natija = ogirlik
elif birlik == 2:
    natija = ogirlik / 100000    
elif birlik == 3:
    natija = ogirlik / 1000
elif birlik == 4:
    natija = ogirlik * 1000        
elif birlik == 5:
    natija = ogirlik * 100   
print(natija,' kg')
'''
#8
'''
d=int(input('D= (kun) '))      
m=int(input('M=(oy) '))      
d-=1
if d==0 : 
    # bir kun oldingi sana nolga teng bo'lsa 
    # oldingi yni olish uchun m dan 1 ni ayiramiz. 
    #  M: 1-mart dan oldingi kun 28-fevral 
    m-=1
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12 :
        d=31
    elif m==4 or m==6 or m==9 or m==11:
        d=30
    elif m==2:
        d=28
print('Oldingi kun: ', d,'.',m)
'''
#9
'''
d=int(input('D= (kun) '))      
m=int(input('M=(oy) '))      
d+=1
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10  :
    if d>31:
        d=1
        m+=1
elif m==4 or m==6 or m==9 or m==11:
    if d>30:
        d=1
        m+=1
elif m==2:
    if d>28:
        d=1
        m+=1
elif m==12:
    if d>31:
        d=1
        m=1
print('Keyingi kun: ', d,'.',m)
'''
#10
'''
t=input('Tomon: “s”-shimol, “j”-janub, “q”-sharq, “g”-g’arb  ')      
h=int(input('0-harakni davom ettir, 1-chapga buril, 2-o`ngga buril.  '))  
if t=='s': #qaysi tomonga qarab turganligi 
    if h==0:
        print('shimol')
    elif h==1:
        print("G'arb")        
    elif h==2:
        print("Sharq")       
elif t=='j':
    if h==0:
        print('janub')
    elif h==1:
        print("Sharq")        
    elif h==2:
        print("G'arb") 
elif t=='q':
    if h==0:
        print('Sharq')
    elif h==1:
        print("Shimol")        
    elif h==2:
        print("Janub")         
elif t=='g':
    if h==0:
        print("G'arb")
    elif h==1:
        print("Janub")        
    elif h==2:
        print("Shimol")   
'''
#11
'''
t=input('Tomon: “s”-shimol, “j”-janub, “q”-sharq, “g”-g’arb  ')      
h=int(input('0-o`ngga buril, 1-chapga buril, 2-burilish 180  '))  
if t=='s': #qaysi tomonga qarab turganligi 
    if h==2:
        print('janub')
    elif h==1:
        print("G'arb")        
    elif h==0:
        print("Sharq")       
elif t=='j':
    if h==2:
        print('shimol')
    elif h==1:
        print("Sharq")        
    elif h==0:
        print("G'arb") 
elif t=='q':
    if h==2:
        print('G\'arb')
    elif h==1:
        print("Shimol")        
    elif h==0:
        print("Janub")         
elif t=='g':
    if h==2:
        print("Sharq")
    elif h==1:
        print("Janub")        
    elif h==0:
        print("Shimol")      
'''   
#Pifagor sonlari:
n=int(input('n='))
for a in range(1,n+1):
    for b in range(a+1,n+1):
        for c in range(1,n+1):
            if a*a+b*b==c*c:
                print(a,b,c)

