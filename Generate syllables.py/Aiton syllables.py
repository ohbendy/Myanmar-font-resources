#######################
### Aiton syllables ###
#######################

# Unfortunately based on incomplete information #

aitonconsonants = ["က", "ၵ", "င", "ꩡ", "ꩬ", "ꧧ", "တ", "ထ", "ဒ", "ꩫ", "ပ", "ၸ", "ဗ", "မ", "ယ", "ꩺ", "လ", "ဝ", "ꩭ", "ဢ"] 
aitonmedials = ["ျ", "ြ"]
aitonrhymes = ["", "ႜ", "ႃ", "ီ",  "ူ", "ေ", "ႝ",  "ံ", "ေႃ", "ုဝ်", "ိုဝ်", "ွꧥ", "ၞꧥ", "က်", "င်", "တ်", "ꩫ်", "ပ်", "ꧥံ", "ွႝ", "ွေ", "ိုႜ", "ုံ", "ွံ", "ွႝ", "ိက်", "ိင်", "ိတ်", "ိꩫ်", "ိပ်", "ုက်", "ုင်", "ုတ်", "ုꩫ်", "ုပ်", "ွက်", "ိုက်"]
numerals = "၀၁၂၃၄၅၆၇၈၉"

print("Every Aiton consonant")
for aitonconsonant in aitonconsonants:
	print(aitonconsonant, end=' ')
print()
print()

print("Every Aiton rhyme")
for aitonrhyme in aitonrhymes:
	print("◌" + aitonrhyme, end=' ')
print()
print()

print("Every Aiton consonant with every syllable rhyme") # Probably the tallAa cannot combine with tonemarks?
for aitonconsonant in aitonconsonants:
	for aitonrhyme in aitonrhymes:
		print(aitonconsonant + aitonrhyme, end=' ')
	print()
print()
print()

print("Every Aiton consonant with every medial and vowel and final")
for aitonconsonant in aitonconsonants:
	for aitonmedial in aitonmedials:
		for aitonrhyme in aitonrhymes:
				print(aitonconsonant + aitonmedial + aitonrhyme, end=' ')	
	print()
