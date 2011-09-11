#	At the end of a string (eg AAACCCCGGTTAAAAA):
#		add a new line return
	
#	scan for A endings with stine's code
#		cull A endings off
#	anaylse sequence normally, do graphs

#	Stine's Code:
#		import re

#		foo = "AGCGTTAGAAATAAAAAAA"
#		bar = re.sub(r"[AT]*$", "", foo)

#		print(bar)


import re

foo = """>ENSDART00000000002			
UUAUACAUAAGUCAACAUUAAAAGUGGAUCAGACCCUUUCAUCAAAGUUGUCCUAAAUCU
AGUAUUCUGAUACAUUGUGUCUCUACACAAAAAAAAAAAAAA

>ENSDART00000000004	[AAAAA -15 AATAAA]	assembly=ZFISH4|chr=9|strand=reverse|downstream UTR [AAAAA -15 AATAAA]	
GUGGGAUUUGAACUCCUUGUAAUUAACUAUGAUGUAAAUAUUCUGCGAUGAGCCUGUAAA
CUCAGUUCCUGGAGGGCCGCAGCUCUGCAGUUUAGAUCUUACCCUAAUUAAACACAUUUG"""

bar = re.sub(r" ", "\n", foo)

print(bar)

print '\n---------------------Run Two, Stripping----------------------\n'

foo2 = bar
bar2 = re.sub(r"AAAA\n", "", foo2)

print(bar2)

