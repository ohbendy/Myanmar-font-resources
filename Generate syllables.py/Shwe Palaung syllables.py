##############################
### Shwe Palaung syllables ###
##############################

# Based on incomplete information

shwepalaungconsonants = ["က", "ခ", "ꩾ", "ဂ", "င", "စ", "ဆ", "ꩿ", "ဇ", "ဈ", "ည", "တ", "ထ", "ဒ", "န", "ပ", "ဖ", "ဘ", "မ", "ယ", "ရ", "လ", "ဝ", "ႎ", "ႎှ", "ဟ", "အ", "မှ", "နှ", "ညှ", "ငှ", "ရှ", "ယှ", "ဝှ"]
shwepalaunginitialclusters = ["ပ္လ", "ဖ္လ", "ဘ္လ", "က္လ", "ခ္လ", "ဂ္လ", "ပြ", "ဖြ", "ဘြ", "တြ", "ထြ", "ဒြ", "ကြ", "ခြ", "ဂြ", "မြ", "ဟြ", "ပျ", "ဖျ", "ဘျ", "တျ", "ထျ", "ဒျ", "ကျ", "ချ", "ဂျ", "ႎျ", "ဆျ", "မျ", "နျ", "ငျ", "လျ", "ရျ", "အျ", "ဟျ", "ပွ", "ဖွ", "ဘွ", "တွ", "ထွ", "ဒွ", "စွ", "ဇွ", "ကွ", "ခွ", "ဂွ", "ဆွ", "မွ", "နွ", "ညွ", "ငွ", "လွ", "ရွ", "အွ", "ဟွ", "ယွ", "ပ္လျ", "ဖ္လျ", "ဘ္လျ", "က္လျ", "ခ္လျ", "ဂ္လျ", "ပ္လွ", "ဖ္လွ", "ဘ္လွ", "က္လွ", "ခ္လွ", "ဂ္လွ", "ပျြ", "ဖျြ", "ဘျြ", "ကျြ", "ချြ", "ဂျြ", "မျြ", "ဟျြ"]
shwepalaungfinals = ["ပ်", "တ်", "က်", "့", "မ်", "န်", "င်", "ရႈ", "ရ်", "ည်", "စ်"]
shwepalaungvowels = ["", "ိ", "ီ", "ီု", "ု", "ူ", "ေ", "ိူ", "ို", "ေဲ", "ံ", "ဲ", "်ု", "ာ်", "ါ်", "ော", "ေါ", "ာ", "ါ"]
shwepalaungtones = ["", "ႇ", "း", "ႈ", "ႏ", "့", "ႇ"]
numerals = "𑛚𑛛𑛜𑛝𑛞𑛟𑛠𑛡𑛢𑛣"

print("Every Shwe Palaung consonant")
for shwepalaungconsonant in shwepalaungconsonants:
	print(shwepalaungconsonant, end=' ')
print()
print()

print("Every Shwe Palaung vowel")
for shwepalaungvowel in shwepalaungvowels:
	print("◌" + shwepalaungvowel, end=' ')
print()
print()

print("Every Shwe Palaung final")
for shwepalaungfinal in shwepalaungfinals:
	print("◌" + shwepalaungfinal, end=' ')
print()
print()

print("Every Shwe Palaung tonemark")
for shwepalaungtone in shwepalaungtones:
	print("◌" + shwepalaungtone, end=' ')
print()
print()

print("Every Shwe Palaung consonant with every vowel and tonemark")
for shwepalaungconsonant in shwepalaungconsonants:
	for shwepalaungvowel in shwepalaungvowels:
		for shwepalaungtone in shwepalaungtones:
			print(shwepalaungconsonant + shwepalaungvowel + shwepalaungtone, end=' ')
	print()
print()
print()

print("Every Shwe Palaung consonant with every vowel and final and tonemark")
for shwepalaungconsonant in shwepalaungconsonants:
	for shwepalaungvowel in shwepalaungvowels:
		for shwepalaungfinal in shwepalaungfinals:
			for shwepalaungtone in shwepalaungtones:
				print(shwepalaungconsonant + shwepalaungvowel + shwepalaungfinal + shwepalaungtone, end=' ')
	print()
print()
print()

print("Every Shwe Palaung initial cluster with every vowel and tonemark")
for shwepalaunginitialcluster in shwepalaunginitialclusters:
	for shwepalaungvowel in shwepalaungvowels:
		for shwepalaungtone in shwepalaungtones:
			print(shwepalaunginitialcluster + shwepalaungvowel + shwepalaungtone, end=' ')
	print()
print()
print()

print("Every Shwe Palaung initial cluster with every vowel and final and tonemark")
for shwepalaunginitialcluster in shwepalaunginitialclusters:
	for shwepalaungvowel in shwepalaungvowels:
		for shwepalaungfinal in shwepalaungfinals:
			for shwepalaungtone in shwepalaungtones:
				print(shwepalaunginitialcluster + shwepalaungvowel + shwepalaungfinal + shwepalaungtone, end=' ')
	print()
print()
print()
