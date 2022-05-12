#############################
### S'gaw Karen syllables ###
#############################

sgawconsonants = ["က", "ခ", "ဂ", "ဃ", "င", "စ", "ဆ", "ၡ", "ည", "တ", "ထ", "ဒ", "န", "ပ", "ဖ", "ဘ", "မ", "ယ", "ရ", "လ", "ဝ", "သ", "ဟ", "အ", "ဧ"]
sgawinitialclusters = ["စှ", "ဆှ", "ပှ", "ဖှ", "ဘှ", "မှ", "ကၠ", "ခၠ", "ပၠ", "ဖၠ", "ဘၠ", "မၠ", "ကျ", "ချ", "ပျ", "ဖျ", "ဘျ", "မျ", "ကြ", "ခြ", "စြ", "တြ", "ထြ", "ဒြ", "ပြ", "ဖြ", "ဘြ", "သြ", "ကွ", "ခွ", "စွ", "ဆွ", "ၡွ", "တွ", "ထွ", "ဒွ", "နွ", "ပွ", "ဖွ", "ယွ", "ရွ", "လွ", "သွ", "ဟွ"] 

sgawvowels = ["ံ", "့", "ဲ", "ၢ", "ု", "ူ", "ိ", "ီ"] 
sgawtonemarks = ["", "ၢ်", "ာ်", "း", "ၣ်", "ၤ"]
numerals = "၀၁၂၃၄၅၆၇၈၉"

print("Every S'gaw consonant")
for sgawconsonant in sgawconsonants:
	print(sgawconsonant, end=' ')
print()
print()

print("Every S'gaw vowel")
print("◌ါ", end=' '),
for sgawvowel in sgawvowels:
	print("◌" + sgawvowel, end=' ')
print()
print()

print("Every S'gaw tonemark")
for sgawtonemark in sgawtonemarks:
	print("◌" + sgawtonemark, end=' ')
print()
print()

print("Every S'gaw consonant with every vowel and tonemark")
for sgawconsonant in sgawconsonants:
	print(sgawconsonant + "ါ​​​​​​", end=' '), # Note tall Aa cannot combine with a tonemakr
	for sgawvowel in sgawvowels:
		for sgawtonemark in sgawtonemarks:
			print(sgawconsonant + sgawvowel + sgawtonemark, end=' ')
	print()
print()
print()

print("Every S'gaw intial cluster with every vowel and tonemark")
for sgawinitialcluster in sgawinitialclusters:
	print(sgawinitialcluster + "ါ​​​​​​", end=' '), # Note tall Aa cannot combine with a tonemakr
	for sgawvowel in sgawvowels:
		for sgawtonemark in sgawtonemarks:
			print(sgawinitialcluster + sgawvowel + sgawtonemark, end=' ')
	print()
print()
print()
