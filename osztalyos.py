from posixpath import split


def oszthatarozo():
    #osztály meghatározó
    while True:
        be=input("Írja be az ip címet hogy metudja milyen osztályban van: ")
        be=be.split(".")
        
        #Osztály meghatározás
        #A osztály
        if be[0] <= '127' and be[0] >= '1':
            if be[0] == '10':
                print('Ez egy "A" osztályú Belső cím',)
            elif be == '127':
                print('Ez a loopback cím, nem lehet kiosztani!',)
            else:
                print('Ez egy "A" osztályú cím!',)
        #B osztály
        elif be[0] >= '128' and be[0] == '191' :                
            if be[0] == '172' and be[1] >= '16' and be[1] <= '31':
                print('Ez egy "B" osztályú Belső cím')
            else:
                print('Ez egy "B" osztályú cím')
        
                
                          

oszthatarozo()






#cucc

from posixpath import split


def osztaly():
    #osztály meghatározó
    while True:
        be=input("Írja be az ip címet hogy metudja milyen osztályban van: ")
        
        be=be.split(".")

        #Osztály meghatározás
        
        #A osztály
        if be[0] <= '127' and be[0] >= '1':
            if be[0] == '10':
                print('Ez egy "A" osztályú Belső cím',)
            elif be == '127':
                print('Ez a loopback cím, nem lehet kiosztani!',)
            else:
                print('Ez egy "A" osztályú cím!',)

        #B osztály
        elif be[0] >= '128' and be[0] == '191' :                
            if be[0] == '172' and be[1] >= '16' and be[1] <= '31':
                print('Ez egy "B" osztályú Belső cím')
            else:
                print('Ez egy "B" osztályú cím')
        
        #C osztály
        elif be[0] >= '192' and be[0] <= '223':
            if be[0] == '192' and be[1] == '168' and be[2] == '1' and  be[2] >= '255':
                print('Belső cím!') 
                
print('Osztály meghatározó!')
osztaly()

        
