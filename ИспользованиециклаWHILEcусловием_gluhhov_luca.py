#1)
#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while vastus!=o_vastus:
#    print("Viga! Sisesta Õige vastus on ...", )

#    vastus=int(input("Sisesta vastus ..."))
#    k+=1
#while True:
#    print("Õige vastus! Katsed oli ...",k )
#    break

#2)
#x=0
#while True:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1
#    if x==30: break
#print("for:")
#for x in range(0,30,1):
#    if x%2==1: print(x, end="")

print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => "))))
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris =0
    paaritu = 0
    while b > 0:
            if b % 2 == 0:
                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10
    print("Paarisarvud:",paaris)
    print("paarituid numbreid:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake * sisestatud number")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine")
    print()
    if c % 2 == 0:
        print("с - paarisarv. Jagame 2-ga.")
    else:
        print("с - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 == 0:
                    c == c / 2
            else:
                    c == (3*c + 1) / 2 
            print(round(c), end="") 
            break
    print()
    print("on tõestatud")