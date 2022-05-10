independentvowels = "ဣဤဥဦၒၓၔၕဧဩဪဨ"
consonants = "ကခဂဃငစဆဇဈဉညဋဌဍဎဏတထဒဓနပဖဗဘမယရလဝၐၑသဿဟဠအၚၛၜၝၡၥၦၮၯၰၵၶၷꧠၸꧡꩡꧢၺꧣၻၼၽၾၿꧤႁဢႀၹꩠꩢꩣꩲꩤꩥꩧꩨꩩꩪꩳꩬꩮꩭꩯꩱꧩꧪꧫꧬꧧꩦꧭꧮꧯꧻꧼꩫꧽꧾꩺꧺꧨꩾꩿႎ"
burmeseconsonants = "ကခဂဃငစဆဇဈဉညဋဌဍဎဏတထဒဓနပဖဗဘမယရလဝသဟဠအ"
burmesevowels = ["ါ", "ာ", "ား", "ိ", "ီ", "ီး", "ု", "ူ", "ူး", "ေ", "ေ့", "ေး", "ဲ", "ဲ့", "ယ်", "ေါ", "ော", "ေါ့", "ော့","ေါ့", "ော်", "ို", "ို့", "ိုး"]
burmeserhymes = ["က်", "င်", "င့်", "င်း", "စ်", "ဉ်", "ဉ့်", "ဉ်း", "ည်", "ည့်", "ည်း", "တ်", "န်", "န့်", "န်း", "ပ်", "ံ", "ံ့", "မ်း", "ယ်", "ါ", "ာ", "ါး", "ား", "ိ", "ိတ်", "ိန်", "ိန့်", "ိန်း", "ိပ်", "ိမ်", "ိမ့်", "ိမ်း", "ီ", "ီး", "ု", "ုတ်", "ုန်", "ုန့်", "ုန်း", "ုပ်", "ုံ", "ုံ့", "ုံး", "ူ", "ူး", "ေ", "ေ့", "ေး", "ဲ", "ဲ့", "ေါ", "ော", "ေါက်", "ောက်", "ေါင်", "ောင်", "ေါင့်", "ောင့်", "ေါင်း", "ောင်း", "ေါ့", "ော့", "ေါ်", "ော်", "ို", "ိုက်", "ိုင်", "ိုင့်", "ိုင်း", "ို့", "ိုး"]
monconsonants = "ကခဂဃၚစဆဇၛဉညဋဌဍဎဏတထဒဓနပဖဗဘမယရလဝၐၑသဿဟဠၜအၝ"
abovevowels = ["ိ", "ၱ", "ီ", "ဳ", "ဵ", "ႅ", "ဲ", "ႝ", "ၲ", "ၳ", "ၴ", "ဴ", "ꧥ", "ႆ"]
leftvowels = "ေႄ"
rightvowels = ["ါ","ာ","ႃ", "ၖ", "ၗ", "ႜ", "ိါ", "ီါ", "ါဲ", "ါံ"]
belowvowels = ["ု", "ူ", "ၘ", "ၙ"]
anusvara = "ံ"
tonemarks = ["့", "း", "ႇ", "ꩻ", "ႈ", "ႏ", "ႉ", "ႊ", "ႚ", "ႛ", "ႋ", "ႌ", "ႍ", "ꩼ", "ꩽ", "ၩ", "ၪ", "ၫ", "ၬ", "ၭ"]
others = ""
numerals = "၀၁၂၃၄၅၆၇၈၉"
medials = ["ျ","ြ","ွ","ႂ","ှ", "ၞ", "ၟ", "ၠ"]
burmesemedials = ["ျ", "ြ", "ွ", "ှ", "ျွှ", "ျွ", "ျှ", "ြွှ", "ြွ", "ြှ", "ွှ" ]
monmedials = ["ျ","ြ","ွ","ႂ","ှ", "ၞ", "ၟ", "ၠ", "္ၜ", "္ၚ", "္ဉ", "္ည", "္ဍ"]
kinzi ="င်္"
tailaingconsonants =["က", "ၷ", "ꧩ", "ꧪ", "င", "ၸ", "ꩬ", "ꧫ", "ꧬ", "ꧧ", "ꩦ", "ꩧ", "ꧭ", "ꧮ","ꧯ", "တ", "ထ", "ꧻ", "ꧼ", "ꩫ", "ပ", "ꧤ", "ꧽ", "ꧾ", "မ", "ယ", "ꩺ", "လ", "ဝ", "ၐ", "ၑ", "ၯ", "ꧺ", "ဢ", "ꧨ"]

print("Every Burmese consonant")
for burmeseconsonant in burmeseconsonants:
	print(burmeseconsonant, end=' ')
print()
print()

print("Every Burmese rhyme")
for burmeserhyme in burmeserhymes:
	print("◌" + burmeserhyme, end=' ')
print()
print()

print("Every Burmese consonant with every rhyme")
for burmeserhyme in burmeserhymes:
	for burmeseconsonant in burmeseconsonants:
		print(burmeseconsonant + burmeserhyme, end=' ')
	print()
print()
print()

print("Every Burmese consonant with every rhyme")
for burmesemedial in burmesemedials:
	for burmeserhyme in burmeserhymes:
		for burmeseconsonant in burmeseconsonants:
			print(burmeseconsonant + burmesemedial + burmeserhyme, end=' ')
		print()
print()
print()

print("Every Burmese consonant stacked with every other Burmese consonant:")
for burmeseconsonant1 in burmeseconsonants:
	print()
	for burmeseconsonant2 in burmeseconsonants:
		print(burmeseconsonant1 + "္" + burmeseconsonant2, end=' ')
print()
print()

print("Every Burmese conjunct with every rhyme:")
for burmeseconsonant1 in burmeseconsonants:
	for burmeserhyme in burmeserhymes:
		print()
		for burmeseconsonant2 in burmeseconsonants:
			print(burmeseconsonant1 + "္" + burmeseconsonant2 + burmeserhyme, end=' ')
print()
print()

print("Every Burmese conjunct with medialRa or medialYa with every rhyme:")
for burmeseconsonant1 in burmeseconsonants:
	for burmeserhyme in burmeserhymes:
		print()
		for burmeseconsonant2 in burmeseconsonants:
			print(burmeseconsonant1 + "္" + burmeseconsonant2 + "ျ" +burmeserhyme, end=' ')
			print(burmeseconsonant1 + "္" + burmeseconsonant2 + "ြ" +burmeserhyme, end=' ')
print()
print()

##########################
### And Now With Kinzi ###
##########################

print("Every Burmese consonant with kinzi")
for burmeseconsonant in burmeseconsonants:
	print(kinzi + burmeseconsonant, end=' ')
print()
print()

print("Every Burmese rhyme with kinzi")
for burmeserhyme in burmeserhymes:
	print(kinzi+ burmeserhyme, end=' ')
print()
print()

print("Every Burmese consonant with every rhyme with kinzi")
for burmeserhyme in burmeserhymes:
	for burmeseconsonant in burmeseconsonants:
		print(kinzi + burmeseconsonant + burmeserhyme, end=' ')
	print()
print()
print()

print("Every Burmese consonant with every rhyme with kinzi")
for burmesemedial in burmesemedials:
	for burmeserhyme in burmeserhymes:
		for burmeseconsonant in burmeseconsonants:
			print(kinzi + burmeseconsonant + burmesemedial + burmeserhyme, end=' ')
		print()
print()
print()

print("Every Burmese consonant stacked with every other Burmese consonant with kinzi")
for burmeseconsonant1 in burmeseconsonants:
	print()
	for burmeseconsonant2 in burmeseconsonants:
		print(kinzi + burmeseconsonant1 + "္" + burmeseconsonant2, end=' ')
print()
print()

print("Every Burmese conjunct with every rhyme with kinzi")
for burmeseconsonant1 in burmeseconsonants:
	for burmeserhyme in burmeserhymes:
		print()
		for burmeseconsonant2 in burmeseconsonants:
			print(kinzi + burmeseconsonant1 + "္" + burmeseconsonant2 + burmeserhyme, end=' ')
print()
print()

print("Every Burmese conjunct with medialRa or medialYa with every rhyme with kinzi")
for burmeseconsonant1 in burmeseconsonants:
	for burmeserhyme in burmeserhymes:
		print()
		for burmeseconsonant2 in burmeseconsonants:
			print(kinzi + burmeseconsonant1 + "္" + burmeseconsonant2 + "ျ" +burmeserhyme, end=' ')
			print(kinzi + burmeseconsonant1 + "္" + burmeseconsonant2 + "ြ" +burmeserhyme, end=' ')
print()
print()

#print("Every consonant with left vowels")
#for leftvowel in leftvowels:
#	for consonant in consonants:
#		print(consonant + leftvowel, end=' ')
#	print()
#print()
#print()
#
#print("Every consonant with above vowels")
#for abovevowel in abovevowels:
#	for consonant in consonants:
#		print(consonant + abovevowel, end=' ')
#	print()
#print()
#print()
#
#print("Every consonant with right vowels")
#for rightvowel in rightvowels:
#	for consonant in consonants:
#		print(consonant + rightvowel, end=' ')
#	print()
#print()
#print()
#
#print("Every consonant with below vowels")
#for belowvowel in belowvowels:
#	for consonant in consonants:
#		print(consonant + belowvowel, end=' ')
#	print()
#print()
#print()
#
#print("Every consonant with tonemarks")
#for tonemark in tonemarks:
#	for consonant in consonants:
#		print(consonant + tonemark, end=' ')
#	print()
#print()
#print()
#
#print("Every consonant with left vowels and tonemarks")
#for leftvowel in leftvowels:
#	for tonemark in tonemarks:
#		for consonant in consonants:
#			print(consonant + leftvowel + tonemark, end=' ')
#		print()
#print()
#print()
#
#print("Every consonant with above vowels and tonemarks")
#for abovevowel in abovevowels:
#	for tonemark in tonemarks:
#		for consonant in consonants:
#			print(consonant + abovevowel + tonemark, end=' ')
#		print()
#print()
#print()
#
#print("Every consonant with right vowels and tonemarks")
#for rightvowel in rightvowels:
#	for tonemark in tonemarks:
#		for consonant in consonants:
#			print(consonant + rightvowel + tonemark, end=' ')
#		print()
#print()
#print()
#
#print("Every consonant with below vowels and tonemarks")
#for belowvowel in belowvowels:
#	for tonemark in tonemarks:
#		for consonant in consonants:
#			print(consonant + belowvowel + tonemark, end=' ')
#		print()
#print()
#print()
#
#print("Every consonant with every medial")
#for medial in medials:
#	for consonant in consonants:
#		print(consonant + medial, end='')
#	print()
#print()
#print()	
#
#print("Every consonant with combined medials")
#for consonant in consonants:
#	print(consonant + "ျ" + "ြ" + "ွ" + "ှ", end='')
#	print(consonant + "ျ" + "ြ" + "ွ", end='')
#	print(consonant + "ျ" + "ြ" + "ှ", end='')
#	print(consonant + "ျ" + "ွ" + "ှ", end='')
#	print(consonant + "ျ" + "ွ", end='')
#	print(consonant + "ျ" + "ှ", end='')
#	print(consonant + "ြ" + "ွ" + "ှ", end='')
#	print(consonant + "ြ" + "ွ", end='')
#	print(consonant + "ြ" + "ှ", end='')
#	print(consonant + "ွ" + "ှ", end='')	
#	print()
#print()
#print()	
#
#print("Tai Laing specials")
#for tailaingconsonant in tailaingconsonants:
#	print(tailaingconsonant + "ျ" + "ူ" + "ႍ", end='')
#	print(tailaingconsonant + "ျ" + "ူ" + "ꩼ", end='')
#	print(tailaingconsonant + "ျ" + "ႃ" + "ႍ", end='')
#	print(tailaingconsonant + "ျ" + "ႃ" + "ꩼ", end='')
#	print(tailaingconsonant + "ွ" + "ႃ" + "ႍ", end='')
#	print(tailaingconsonant + "ွ" + "ႃ" + "ꩼ", end='')
#	print(tailaingconsonant + "ႂ" + "ႃ" + "ႍ", end='')
#	print(tailaingconsonant + "ႂ" + "ႃ" + "ꩼ", end='')
#	print(tailaingconsonant + "ႆ" + "ꩼ", end='')
#	print()
#print()
#print()
#	
#print("Every Burmese consonant stacked with every other Burmese consonant:")
#for burmeseconsonant1 in burmeseconsonants:
#	print()
#	for burmeseconsonant2 in burmeseconsonants:
#		print(burmeseconsonant1 + "္" + burmeseconsonant2, end=' ')
#	print()
#print()
#print()
#
#print("Every Mon consonant with Mon medials:")
#for monconsonant in monconsonants:
#	print()
#	for monmedial in monmedials:
#		print(monconsonant + monmedial, end=' ')
#	print()
#print()
#print()
#
# for medial in medials:
# 	for consonant1 in consonants:
# 		print()
# 		for consonant2 in consonants:
# 			print(consonant1 + "္" + consonant2 + medial, end=' ')
# 	for leftvowel in leftvowels:
# 		for consonant1 in consonants:
# 			print()
# 			for consonant2 in consonants:
# 				print(consonant1 + "္" + consonant2 + medial + leftvowel, end=' ')
# 	for leftvowel in leftvowels:
# 		for consonant1 in consonants:
# 			print()
# 			for consonant2 in consonants:
# 				print(consonant1 + "္" + consonant2 + medial + leftvowel + "" + "", end=' ')
