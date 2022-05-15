#######################
### Kayah syllables ###
#######################

# Unfortunately based on incomplete information #

kayahconsonants = ["က", "ခ", "ဂ", "ဃ", "င", "စ", "ဆ", "ဇ", "ည", "တ", "ထ", "ဒ", "န", "ပ", "ဖ", "ဗ", "ဘ", "မ", "ယ", "ရ", "လ", "ဝ", "သ", "ဟ", "အ"] 
kayahmedials = ["ြ", "ျ", "ွ", "ှ"] # uncertain which ones can combine, and the storage order means we can't compile medial + vowel in the normal way for some of these.
kayahmedialsstoredaftervowels = ["ု", "ူ"]
kayahvowels = ["", "ၲ", "ိ", "ီ", "ံ", "ဲ", "ၳ", "ၴ", "ဴ"] # Uncertain which vowel characters can combine.
kayahtonemarks = ["", "ၤ", "း"]
numerals = "၀၁၂၃၄၅၆၇၈၉"

print("Every Kayah consonant")
for kayahconsonant in kayahconsonants:
	print(kayahconsonant, end=' ')
print("ဗာ့")
print()
print()

print("Every Kayah vowel")
for kayahvowel in kayahvowels:
	print("◌" + kayahvowel, end=' ')
print()
print()

print("Every Kayah consonant with every vowel and tonemark") # Probably the tallAa cannot combine with tonemarks?
for kayahconsonant in kayahconsonants:
	for kayahvowel in kayahvowels:
		for kayahtonemark in kayahtonemarks:
			print(kayahconsonant + kayahvowel + kayahtonemark, end=' ')
	print()
for kayahvowel in kayahvowels:
	for kayahtonemark in kayahtonemarks:
		print("ဗ"+ kayahvowel + "ာ့" + kayahtonemark, end=' ') # Not sure about this one
print()
print()

print("Every Kayah consonant with every medial and vowel and tonemark")
for kayahconsonant in kayahconsonants:
	for kayahmedial in kayahmedials:
		for kayahvowel in kayahvowels:
			for kayahtonemark in kayahtonemarks: 
				print(kayahconsonant + kayahmedial + kayahvowel + kayahtonemark, end=' ')	
	for kayahmedialstoredaftervowels in kayahmedialsstoredaftervowels:
		for kayahvowel in kayahvowels:
			for kayahtonemark in kayahtonemarks: 
				print(kayahconsonant + kayahvowel + kayahmedialstoredaftervowels + kayahtonemark, end=' ')
	print()
		
for kayahmedial in kayahmedials:
	for kayahvowel in kayahvowels:
		for kayahtonemark in kayahtonemarks: 
			print("ဗ" + kayahmedial + kayahvowel + "ာ့" +  kayahtonemark, end=' ')
for kayahmedialstoredaftervowels in kayahmedialsstoredaftervowels:
	for kayahvowel in kayahvowels:
		for kayahtonemark in kayahtonemarks: 
			print("ဗ" + kayahvowel + kayahmedialstoredaftervowels + "ာ့" + kayahtonemark, end=' ') # Not sure about this one
print()
