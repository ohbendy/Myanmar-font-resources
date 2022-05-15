#############################
### Eastern Pwo syllables ###
#############################

epwoconsonants = ["က", "ခ", "ဂ", "ဃ", "င", "စ", "ဆ", "ဇ", "ဈ", "ည", "ဋ", "ဌ", "ဍ", "ဎ", "ၮ", "တ", "ထ", "ဒ", "ဓ", "န", "ပ", "ဖ", "ဗ", "ဘ", "မ", "ယ", "ရ", "လ", "ဝ", "ၐ", "ၑ", "သ", "ဟ", "ဠ", "အ", "ၜ", "ၯ", "ၰ"] 
epwomedials = ["ၠ", "ျ", "ြ", "ွ", "ှ"] # uncertain which ones can combine 
epworhymes = ["", "်ု", "ါ", "ာ",  "ါ့", "ာ့", "ါႋ", "ာႋ", "း", "ိ", "ီ", "ီ့", "ီႋ", "ီး", "ု", "ူ", "ူ့", "ူႋ", "ူး", "ေ", "ေ့", "ေႋ", "ေး", "က်", "ယ်", "ယ့်", "ါဲ", "ဲ", "ေါ", "ဴ", "ဝ်", "ှ်", "ိက်", "ါ်", "ေံ", "ေဝ်", "ေဝ့်", "ေဝ်ႋ", "ှ်ေ", "ါင်", "ါင့်", "ါင်ႋ", "ါင်း", "င်", "င့်", "င်ႋ", "င်း", "ံင်", "ံင့်", "ံင်ႋ", "ံင်း", "ိင်", "ိင့်", "ိင်ႋ", "ိင်း", "ုံ", "ုံ့", "ုံႋ", "ုံး", "ုင်", "ုင့်", "ုင်ႋ", "ုင်း", "ို", "ိုင်", "ိုင့်", "ိုင်ႋ", "ိုင်း", "ုက်", "ုဂ်", "ေါတ်", "ေါဝ်", "ေါဝ့်", "ေါဝ်ႋ", "ေါဟ်", "ိုတ်", "ိုဝ်", "ိုဝ့်", "ိုဝ်ႋ", "ိုဝ်း", "ိုဒ်", "ိုဒ်ႋ", "ိုဟ်", "ုဲ", "ုဲ့", "ုဲႋ", "ုဲး", "ိုဲ", "ိုဲ့", "ိုဲႋ", "ိုဲး"] # I can't understand the use of tallAa vs roundAa in the resources I have.
epwomedials = ["ျ", "ြ", "ွ", "ှ", "္ၚ", "္ဍ", "ၞ", "ၟ", "ၠ", "္တ", "္က", "္စ", "္ၜ"] 
numerals = "𑛚𑛛𑛜𑛝𑛞𑛟𑛠𑛡𑛢𑛣"

print("Every Eastern Pwo consonant")
for epwoconsonant in epwoconsonants:
	print(epwoconsonant, end=' ')
print()
print()

print("Every Eastern Pwo vowel")
for epworhyme in epworhymes:
	print("◌" + epworhyme, end=' ')
print()
print()

print("Every Eastern Pwo consonant with every rhyme")
for epwoconsonant in epwoconsonants:
	for epworhyme in epworhymes:
			print(epwoconsonant + epworhyme, end=' ')
	print()
print()
print()

print("Every Eastern Pwo consonant with every medial and rhyme")
for epwoconsonant in epwoconsonants:
	for epwomedial in epwomedials:
		for epworhyme in epworhymes:
				print(epwoconsonant + epwomedial + epworhyme, end=' ')
	print()
print()
print()
