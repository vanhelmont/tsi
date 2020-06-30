from math import log

def tsi_secchi(secchi):
	tsi_secchi = 10 * (2.46 + (3.67-1.57*log(secchi))/log(2.5)) 
	print('The TSI-Secchi corresponding to a Secchi value of ' + str(secchi) + 'm is ' + str(tsi_secchi) + '.')


def tsi_chla(chla):
	tsi_chla = 10 * (2.46 + log(chla)/log(2.5))
	print('The TSI-Chl corresponding to a Secchi value of ' + str(chla) + 'm is ' + str(tsi_chla) + '.')

def tsi_tp(tp):
	tsi_tp = 10 * (2.46 + (6.68-1.15*log(tp))/log(2.5))
	print('The TSI-Secchi corresponding to a TP value of ' + str(tp) + 'm is ' + str(tsi_tp) + '.')

# def check_tsi(tsi_value):


# User input
user_secchi = float(input('Input Secchi depth (in meters): '))
user_chla = float(input('Input chlorophyll-a value (in mg/m3): '))
user_tp = float(input('Input total phosphorus (in mg/l): '))
print('')

# Processing the user input
tsi_secchi(user_secchi)
tsi_chla(user_chla)
tsi_tp(user_tp)

# Press any key to exit
print('')
input('Press any key to exit.')