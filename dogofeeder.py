import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

onoff = int(input('Gostaria de ligar ou desligar o rele \n 1 - Ligar \n 2 - Desligar?\n'))
if onoff == 1:
	rele = int(input('Qual rele voce gostaria de acionar?'))

	if rele == 1:
		GPIO.output(11, 1)
		print('Rele 1 ligado\n')
	elif rele == 2:
		GPIO.output(12, 1)
		print('Rele 2 ligado\n')
	else:
		print('Nenhum rele valido foi acionado, tente outro numero\n')

elif off == 2:
	rele = int(input('Qual rele voce gostaria de desacionar?\n')
	if rele == 1:
		GPIO.output(11,0)
		print('Rele 1 desligado\n')
	elif rele == 2:
		GPIO.output(12,0)
		print('Rele 2 desligado\n')
	else:
		print('Nenhum rele valido foi desacionado, tente outro numero\n')
