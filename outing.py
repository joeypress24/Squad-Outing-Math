
bowlCost = 32.95*3*2 #cost of 3 lanes for two hours

plebe = 125
youngster = 225
second = 300
firstie = 500

#numPlebe = 3 # Martonfi, Rimmer, and Cabalu
numYoungster = 3 # Nowell, Duncan, and Inman
numSecond = 2 # Caroline and Kayla
numFirstie = 4 # Paz, Press, WuoloJourney, and Salazar

totalPay = numYoungster*youngster + numSecond*second + numFirstie*firstie

print(f'cost of bowling: {bowlCost}')
#calculate the cost per person per class

moneyPerFirstie = (firstie/totalPay)*bowlCost / numFirstie
#print(moneyPerFirstie)

moneyPerSecond = (second/totalPay)*bowlCost / numSecond

moneyPerYoungster = (youngster/totalPay)*bowlCost / numYoungster

print(f'firsties pay {moneyPerFirstie}')
print(f'2/C pay {moneyPerSecond}')
print(f'youngsters pay {moneyPerYoungster}')

