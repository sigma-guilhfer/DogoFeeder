#importa biblioteca para leitura e gravacao de gpios
import RPi.GPIO as GPIO

#seleciona o modo de leitura das gpios
GPIO.setmode (GPIO.BOARD)

#declara se o pino sera lido ou gravado
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

#grava a variavel com o valor da gpio
rele1 = GPIO.input(11)
rele2 = GPIO.input(12)
b1 = GPIO.input(13)
b2 = GPIO.input(15)

print('estados dos botoes {},{}'.format(b1,b2))

print('o rele um estÃ¡ {} e o rele 2 estÃ¡ {}'.format(rele1, rele2))

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

elif onoff == 2:
	rele = int(input('Qual rele voce gostaria de desacionar?\n'))
	if rele == 1:
		GPIO.output(11,0)
		print('Rele 1 desligado\n')
	elif rele == 2:
		GPIO.output(12,0)
		print('Rele 2 desligado\n')
	else:
		print('Nenhum rele valido foi desacionado, tente outro numero\n')
		