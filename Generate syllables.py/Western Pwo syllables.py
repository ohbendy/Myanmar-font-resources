#############################
### Western Pwo syllables ###
#############################

wpwoconsonants = ["က", "ခ", "ဂ", "ဎ", "င", "စ", "ဆ", "ဇ", "ည", "ၡ", "တ", "ထ", "ဒ", "န", "ပ", "ဖ", "ဘ", "မ", "ယ", "ရ", "လ", "ဝ", "ၥ", "ဟ", "အ", "ဧ", "ၦ"] 
wpwomedials = ["ၠ", "ျ", "ြ", "ွ", "ှ"] # uncertain which ones can combine 
wpwovowels = ["ာ", "ါ", "ံ", "့", "ဲ", "ၧ", "ၨ", "ု", "ူ", "ိ", "ီ", ] 
wpwotonemarks = ["", "ၩ", "ၪ", "ၫ", "ၬ", "ၭ", "ၩ့", "ၫ့", "ၪ့", "း"]
numerals = "၀၁၂၃၄၅၆၇၈၉"

print("Every Western Pwo consonant")
for wpwoconsonant in wpwoconsonants:
	print(wpwoconsonant, end=' ')
print()
print()

print("Every Western Pwo vowel")
print("◌ါ", end=' '),
for wpwovowel in wpwovowels:
	print("◌" + wpwovowel, end=' ')
print()
print()

print("Every Western Pwo tonemark")
for wpwotonemark in wpwotonemarks:
	print("◌" + wpwotonemark, end=' ')
print()
print()

print("Every Western Pwo consonant with every vowel and tonemark")
for wpwoconsonant in wpwoconsonants:
	for wpwovowel in wpwovowels:
		for wpwotonemark in wpwotonemarks:
			print(wpwoconsonant + wpwovowel + wpwotonemark, end=' ')
	print()
print()
print()

print("Every Western Pwo consonant with every medial, vowel and tonemark")
for wpwoconsonant in wpwoconsonants:
	for wpwomedial in wpwomedials:
		for wpwovowel in wpwovowels:
			for wpwotonemark in wpwotonemarks:
				print(wpwoconsonant + wpwomedial + wpwovowel + wpwotonemark, end=' ')
	print()
print()
print()
