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
        elif ip2 > 255 or ip2 < 0:
            print('ez nem jó!')
            continue
        elif ip3 > 255 or ip3 < 0:
            print('ez nem jó!')
            continue    
        elif ip4 > 255 or ip4 < 0:
            print('ez nem jó!')
            continue
        

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
            if ip1 == 192 and ip2 == 168 and ip3 <= 1 and  ip3 >= 255:
                print('Ez egy "C" osztályú cím és Belső cím!')
        # "D" osztály
        elif ip1 <= 224 and ip1 >= 239:
            print('ez egy "D" osztályos cím, ezt nem oszthatóki mert ezek multicasting-es címek!!!')
        #"E" osztály
        elif ip1 <= 240 and ip1 >= 255:
            print('Ez egy "D" osztályú cím nem osztható ki, mert internet címek!!!')






while True:
    valaszto=input('Mit akkar csinálni : "1" ip cím osztály határozó;  "2" ip cím 10-ből 2-be átváltás(dec - bin); "3" ip cím 2-ből 10-be átváltás (bin - dec); "4" ip cím összebaszkurálás a maszkal; 0 kilépés')
    if valaszto > 0 and < 4:
        print('Nem jó probáld újra!')
    elif valaszto == 1:
        osztalyhatarozo()
    elif valaszto == 2:
        
