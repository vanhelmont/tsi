from math import log

def tsi_secchi(secchi):
	tsi_secchi = 10 * (2.46 + (3.67-1.57*log(secchi))/log(2.5))
	tsi_secchi = int(round(tsi_secchi, 0)) 
	ts_secchi = check_tsi(tsi_secchi)
	print('The TSI-Secchi corresponding to a Secchi value of ' + str(secchi) + 'm is ' + str(tsi_secchi) + ' - Categorized: ' + ts_secchi)


def tsi_chla(chla):
	tsi_chla = 10 * (2.46 + log(chla)/log(2.5))
	tsi_chla = int(round(tsi_chla, 0))
	ts_chla = check_tsi(tsi_chla)
	print('The TSI-Chl corresponding to a Secchi value of ' + str(chla) + 'm is ' + str(tsi_chla) + ' - Categorized: ' + ts_chla)

def tsi_tp(tp):
	tsi_tp = 10 * (2.46 + (6.68-1.15*log(tp))/log(2.5))
	tsi_tp = int(round(tsi_tp, 0))
	ts_tp = check_tsi(tsi_tp)
	print('The TSI-Secchi corresponding to a TP value of ' + str(tp) + 'm is ' + str(tsi_tp) + ' - Categorized: ' + ts_tp)

def check_tsi(tsi_value):
	if tsi_value >= 0 and tsi_value <= 100:
		if tsi_value < 30:
			return 'Oligotrphic'
		elif tsi_value < 60:
			return 'Mesotrophic'
		elif tsi_value < 90:
			return 'Eutrophic'
		else:
			return 'Hipereutrophic'
	else:
		return 'ERROR'

# START
version = '0.1'
print('TSI-CALCULATOR - v{0}'.format(version))

# User input
user_secchi = float(input('Input Secchi depth (in meters): '))
user_chla = float(input('Input chlorophyll-a value (in mg/m3): '))
user_tp = float(input('Input total phosphorus (in mg/l): '))
print('')

# Processing the user input
tsi_secchi(user_secchi)
tsi_chla(user_chla)
tsi_tp(user_tp)
print('')

# Press any key to exit
input('Press any key to exit.')