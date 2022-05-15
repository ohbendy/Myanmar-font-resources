######################
### Geba syllables ###
######################

# Unfortunately based on incomplete information #

gebaconsonants = ["က", "ခ", "ဂ", "င", "စ", "ဇ", "ည", "တ", "ထ", "ဒ", "ဓ", "န", "ပ", "ဖ", "ဘ", "မ", "ယ", "ရ", "လ", "ဝ", "သ", "ၡ", "ဟ", "အ"] 
gebamedials = ["ၠ", "ျ", "ြ", "ွ", "ှ"] # uncertain which ones can combine 
gebavowels = ["", "ါ", "ာ", "ိ", "ီ", "ဳ", "ၱ", "ု", "ူ", "ေ", "ဲ", "ံ", "့"] # Uncertain which vowel characters can combine.
gebatonemarks = ["", "း", "ာ်", "", "ၤ", "", "ၢ်", "", "ၣ်"]
numerals = "၀၁၂၃၄၅၆၇၈၉"

print("Every Geba consonant")
for gebaconsonant in gebaconsonants:
	print(gebaconsonant, end=' ')
print()
print()

print("Every Geba vowel")
for gebavowel in gebavowels:
	print("◌" + gebavowel, end=' ')
print()
print()

print("Every Geba consonant with every vowel and tonemark") # Probably the tallAa cannot combine with tonemarks?
for gebaconsonant in gebaconsonants:
	for gebavowel in gebavowels:
		for gebatonemark in gebatonemarks:
			print(gebaconsonant + gebavowel + gebatonemark, end=' ')
	print()
print()
print()

print("Every Geba consonant with every medial and vowel and tonemark")
for gebaconsonant in gebaconsonants:
	for gebamedial in gebamedials:
		for gebavowel in gebavowels:
			for gebatonemark in gebatonemarks: 
				print(gebaconsonant + gebamedial + gebavowel + gebatonemark, end=' ')
	print()
print()
print()
