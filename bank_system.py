
print('Choose your time either in sec,min or hour')
rate = int(input('choose your rate >> '))
hour = int(input('chosose your hour >> '))
pick_time = input('Input time in sec,min or hour :')
if pick_time == 'sec':
    hour = hour/3600
    pay = rate * hour
    
elif(pick_time) == 'min':
        hour = hour/60
        pay = rate * hour
        
else:
    pay = hour * rate
    
print(pay)
