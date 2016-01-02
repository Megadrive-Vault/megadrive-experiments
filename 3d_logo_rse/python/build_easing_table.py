import os
import string
import codecs
import ast
import math

filename_out			=	"../src/RSE_easing_table"
table_size				=	512
fix16_precision			=	16
fixed_point_precision 	=	(1 << 16)

def Clamp(k, a, b):
	k = min(k, b)
	k = max(k, a)
	return k


def	EaseInOutQuick(x):
	x = Clamp(x, 0.0, 1.0)
	return	(x * x * (3 - 2 * x))

def EaseInOutByPow(x, p = 2.0):
	x = Clamp(x, 0.0, 1.0)
	y = math.pow(x, p) / (math.pow(x, p) + math.pow(1 - x, p))
	return y

def  main():
	##	Creates the header
	f = codecs.open(filename_out + '.h', 'w')

	f.write('#include "genesis.h"\n\n')

	f.write('#define EASING_TABLE_LEN ' + str(table_size) + '\n')
	f.write('\n')

	f.write('extern const unsigned short easing_fp[EASING_TABLE_LEN];' + '\n')
	f.write('extern const fix16 easing_fix16[EASING_TABLE_LEN];' + '\n')

	f.close()

	##	Creates the C file
	f = codecs.open(filename_out + '.c', 'w')

	f.write('#include "genesis.h"\n\n')

	f.write('/* Integer Fixed Point Table */\n')
	f.write('const unsigned short easing_fp[] = {' + '\n')

	out_str = '\t'

	for i in range(table_size):
		value = EaseInOutQuick(i / table_size)
		value *= fixed_point_precision
		out_str += str(int(value)) + ', '
		if i > 0 and i%16 == 0:
			out_str += '\n\t'

	f.write(out_str[:-2])

	f.write('\n};' + '\n')

	f.write('/* FP16 Table */\n')
	f.write('const fix16 easing_fix16[] = {' + '\n')

	out_str = '\t'

	for i in range(table_size):
		value = EaseInOutQuick(i / table_size)
		value *= fix16_precision
		out_str += 'FIX16({0:.6f}), '.format(value)
		if i > 0 and i%4 == 0:
			out_str += '\n\t'

	f.write(out_str[:-2])

	f.write('\n};' + '\n')

	f.close()

main()