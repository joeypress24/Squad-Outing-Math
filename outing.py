hours = 1
lanes = 3
bowlCost = 32.95*lanes*hours #cost of __ lanes for __ hours

plebe = 125
youngster = 225
second = 325
firstie = 500

# adjust whether or not you want the plebes to pay
plebePay = False

numPlebe = 3 # Martonfi, Rimmer, and Cabalu
numYoungster = 3 # Nowell, Duncan, and Inman
numSecond = 2 # Caroline and Kayla
numFirstie = 4 # Paz, Press, WuoloJourney, and Salazar

if(plebePay):
    totalPay = numYoungster*youngster + numSecond*second + numFirstie*firstie + numPlebe*plebe
else:
    totalPay=  numYoungster*youngster + numSecond*second + numFirstie*firstie

print(f'cost of bowling {lanes} lanes for {hours} hours: {round(bowlCost, 2)}')
#calculate the cost per person per class

moneyFirstie = (numFirstie*firstie/totalPay)*bowlCost

moneySecond = (numSecond*second/totalPay)*bowlCost

moneyYoungster = (numYoungster*youngster/totalPay)*bowlCost

if(plebePay):
    moneyPlebe = (numPlebe*plebe/totalPay)*bowlCost

print(f'firsties pay {round(moneyFirstie/numFirstie, 2)}')
print(f'2/C pay {round(moneySecond/numSecond, 2)}')
print(f'youngsters pay {round(moneyYoungster/numYoungster, 2)}')
if(plebePay):
    print(f'plebes pay {round(moneyPlebe/numPlebe, 2)}')


