
bowlCost = 32.95*3*2 #cost of 3 lanes for two hours

plebe = 125
youngster = 225
second = 300
firstie = 500

#numPlebe = 3 # Martonfi, Rimmer, and Cabalu
numYoungster = 3 # Nowell, Duncan, and Inman
numSecond = 1 # Caroline and Kayla
numFirstie = 3 # Paz, Press, WuoloJourney, and Salazar

totalPay = youngster + second + firstie

print(f'cost of bowling: {bowlCost}')
#calculate the cost per person per class

moneyFirstie = (firstie/totalPay)*bowlCost

moneySecond = (second/totalPay)*bowlCost

moneyYoungster = (youngster/totalPay)*bowlCost

print(f'firsties pay {moneyFirstie/numFirstie}')
print(f'2/C pay {moneySecond/numSecond}')
print(f'youngsters pay {moneyYoungster/numYoungster}')

