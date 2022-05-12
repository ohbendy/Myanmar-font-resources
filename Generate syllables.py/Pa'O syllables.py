#############################
### Pa'O syllables ###
#############################

paoconsonants = ["က", "ခ", "င", "စ", "ဆ", "ည" "တ", "ထ", "ဒ", "န", "ပ", "ဖ", "ဗ", "မ", "ယ", "ရ", "လ", "ဝ", "သ", "ဟ", "အ"] # Ignoring Pali alphabet
paomedials = ["ျ", "ြ", "ွ", "ျွ", "ြွ"] 
paovowels = ["ာ", "ါ", "ိ", "ီ", "ု", "ူ", "ေ", "ဲ", "ံ", "့", "ုံ", "ို", "ေ့", "ဲ့", "ုဲင့်", "ုဲင်", "ေါ့", "ော့", "ေါ", "ော", "ေါ်", "ော်", "ို့", "ို"] 
paotonemarks = ["", "ꩻ", "း", "ႏ"]
numerals = "၀၁၂၃၄၅၆၇၈၉"

print("Every S'gaw consonant")
for paoconsonant in paoconsonants:
	print(paoconsonant, end=' ')
print()
print()

print("Every S'gaw vowel")
print("◌ါ", end=' '),
for paovowel in paovowels:
	print("◌" + paovowel, end=' ')
print()
print()

print("Every S'gaw tonemark")
for paotonemark in paotonemarks:
	print("◌" + paotonemark, end=' ')
print()
print()

print("Every S'gaw consonant with every vowel and tonemark")
for paoconsonant in paoconsonants:
	for paovowel in paovowels:
		for paotonemark in paotonemarks:
			print(paoconsonant + paovowel + paotonemark, end=' ')
	print()
print()
print()

print("Every S'gaw consonant with every medial, vowel and tonemark")
for paoconsonant in paoconsonants:
	for paomedial in paomedials:
		for paovowel in paovowels:
			for paotonemark in paotonemarks:
				print(paoconsonant + paomedial + paovowel + paotonemark, end=' ')
	print()
print()
print()
