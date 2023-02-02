from posixpath import split

def osztalyhatarozo():
    #osztály meghatározó
    while True:
        be=input("Írja be az ip címet hogy metudja milyen osztályban van: ")
        be=be.split(".")

        ip1=int(be[0])
        ip2=int(be[1])
        ip3=int(be[2])
        ip4=int(be[3])
        # ellenőrző hogy max 255 legyen.
        if ip1 > 255 or ip1 < 0:
            print('ez nem jó!')
            continue


        #teszt print(ip1,ip2,ip3,ip4)
    #Osztály meghatározás
        #"A" osztály
        if ip1 <= 127 and ip1 >= 1:
            if ip1 == 10:
                print('Ez egy belő hálózati cím az "A" osztályban')
            elif ip1 == 127:
                print('Ez a loopback cím  "A" osztályban van')
            else:
                print('Ez az "A" osztályban van')
        #"B" osztály
        elif ip1 >= 128 and ip1 <= 191 :
            if ip1 == 191:
                if ip3 > 0 or ip4 > 0:
                    print('Ötletem sincs hogy most mit kéne ki írni')
                else:
                    print('ez egy "B" osztályú cím')
            if ip1 == 172:
                if ip2 >= 16 and ip2 <= 31:
                    print('Ez egy belső hálózati cím a "B" osztályban')
                else:
                    print('Ez egy "B" osztályi cím')
            else:
                print('Ez egy "B" osztályos ip cím!')
        # "C" osztály
        elif ip1 >= 192 and ip1 <= 223:
            if ip1 == 223:
                if ip4 > 0:
                    print('Ez nem jóóóóóóó!')

        


osztalyhatarozo()
        









        
"""
        #A osztály
        if  <= 127 and be[0] >= '1':
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


"""


#cucc
"""
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
"""
        