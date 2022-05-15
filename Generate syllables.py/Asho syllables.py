######################
### Asho syllables ###
######################

# Unfortunately based on incomplete information #

ashoconsonants = ["က", "ခ", "ဂ", "င", "စ", "ဆ", "ဇ", "ည", "တ", "ထ", "ဒ", "ဓ", "န", "ပ", "ဖ", "ဗ", "ဘ", "မ", "ယ", "ရ", "ၡ", "လ", "ဝ", "ဟ", "အ", "ဧ"] 
ashomedials = ["ြ", "ၠ", "ွ", "ှ"] # uncertain which ones can combine
ashovowels = ["","ံ", "့", "ဴ", "ဲ", "ၧ", "ၨ", "ု", "ူ", "ိ", "ီ", "ဳ"] # Uncertain which vowel characters can combine.
ashotonemarks = ["", "ၩ", "ၪ", "ၭ", "ၬ", "ၩ့", "ၪ့", "း"]
numerals = "၀၁၂၃၄၅၆၇၈၉"

print("Every Asho consonant")
for ashoconsonant in ashoconsonants:
	print(ashoconsonant, end=' ')
print("ဗာ့")
print()
print()

print("Every Asho vowel")
for ashovowel in ashovowels:
	print("◌" + ashovowel, end=' ')
print()
print()

print("Every Asho consonant with every vowel and tonemark") # Probably the tallAa cannot combine with tonemarks?
for ashoconsonant in ashoconsonants:
	for ashovowel in ashovowels:
		for ashotonemark in ashotonemarks:
			print(ashoconsonant + ashovowel + ashotonemark, end=' ')
	print()
print()
print()

print("Every Asho consonant with every medial and vowel and tonemark")
for ashoconsonant in ashoconsonants:
	for ashomedial in ashomedials:
		for ashovowel in ashovowels:
			for ashotonemark in ashotonemarks: 
				print(ashoconsonant + ashomedial + ashovowel + ashotonemark, end=' ')	
	print()
