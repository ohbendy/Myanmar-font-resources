########################
### Khamti syllables ###
########################

# Unfortunately based on incomplete information #

khamticonsonants = ["က", "ၵ", "ꩠ", "ၷ", "င", "ꩡ", "သ", "ꩣ", "ꧢ", "ꩥ", "ꩦ", "ꩧ", "ꩨ", "ꩩ", "ꧣ", "တ", "ထ", "ၻ", "ꩪ", "ꩫ", "ပ", "ၸ", "ၿ", "ၹ", "မ", "ယ", "ꩳ", "လ", "ဝ", "ꩬ", "ꩭ", "ꩮ", "ဢ", "ꩯ"] 
khamtimedials = [ "ျ", "ြ"]
khamtivowels = ["","ၢ", "ႃ", "ိ", "ီ", "ႅ", "ဲ", "ု", "ူ", "ေ", "ႄ", "ွ", "ႂ", "ံ", "်"] # Uncertain which vowel characters can combine.
khamtitonemarks = ["", "ႚ", "ႉ", "ႛ", "ႇ", "ႈ", "း", "ႊ" ]
numerals = "၀၁၂၃၄၅၆၇၈၉"

print("Every Khamti consonant")
for khamticonsonant in khamticonsonants:
	print(khamticonsonant, end=' ')
print()
print()

print("Every Khamti vowel")
for khamtivowel in khamtivowels:
	print("◌" + khamtivowel, end=' ')
print()
print()

print("Every Khamti consonant with every vowel and tonemark") # Probably the tallAa cannot combine with tonemarks?
for khamticonsonant in khamticonsonants:
	for khamtivowel in khamtivowels:
		for khamtitonemark in khamtitonemarks:
			print(khamticonsonant + khamtivowel + khamtitonemark, end=' ')
	print()
print()
print()

print("Every Khamti consonant with every medial and vowel and tonemark")
for khamticonsonant in khamticonsonants:
	for khamtimedial in khamtimedials:
		for khamtivowel in khamtivowels:
			for khamtitonemark in khamtitonemarks: 
				print(khamticonsonant + khamtimedial + khamtivowel + khamtitonemark, end=' ')	
	print()
