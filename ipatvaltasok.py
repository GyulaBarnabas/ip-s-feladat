ip = input("Adj meg egy IP-címet: \n")

mask = input("Adj meg egy maszkot: \n")

def is_binary(num):
    return set(num) <= {'0', '1'}

def atvaltasKettesSzamrendszerbe(szam):
    maradek = szam
    eredmeny = ""

    for i in [ 128, 64, 32, 16, 8, 4, 2 , 1 ]:
        if maradek >= i:
            maradek -= i
            eredmeny += "1"
        else:
            eredmeny += "0"

    return eredmeny

def atvaltasTizesSzamrendszerbe(num):
    decimal = 0
    for i, bit in enumerate(num[::-1]):
        if bit == '1':
            decimal += 2 ** i
    return decimal

def convert(num):
    if is_binary(num):
        return str(atvaltasTizesSzamrendszerbe(num))
    else:
        return atvaltasKettesSzamrendszerbe(int(num))


# 192.168.124.1 255.255.255.0 (11111111.11111111.11111111.00000000)

ip2 = ""

for i in ip.split("."):
    szam2 = convert(i)
    ip2 += szam2 + "."

ip2 = ip2[:-1]

mask2 = ""

for i in mask.split("."):
    szam2 = convert(i)
    mask2 += szam2 + "."

mask2 = mask2[:-1]


print(f"Az ip: {ip2}\nA maszk: {mask2}")