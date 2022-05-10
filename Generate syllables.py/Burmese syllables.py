independentvowels = "ဣဤဥဦဧဩဪ"
burmeseconsonants = "ကခဂဃငစဆဇဈဉညဋဌဍဎဏတထဒဓနပဖဗဘမယရလဝသဟဠအ"
burmeserhymes = ["က်", "င်", "င့်", "င်း", "စ်", "ဉ်", "ဉ့်", "ဉ်း", "ည်", "ည့်", "ည်း", "တ်", "န်", "န့်", "န်း", "ပ်", "ံ", "ံ့", "မ်း", "ယ်", "ါ", "ာ", "ါး", "ား", "ိ", "ိတ်", "ိန်", "ိန့်", "ိန်း", "ိပ်", "ိမ်", "ိမ့်", "ိမ်း", "ီ", "ီး", "ု", "ုတ်", "ုန်", "ုန့်", "ုန်း", "ုပ်", "ုံ", "ုံ့", "ုံး", "ူ", "ူး", "ေ", "ေ့", "ေး", "ဲ", "ဲ့", "ေါ", "ော", "ေါက်", "ောက်", "ေါင်", "ောင်", "ေါင့်", "ောင့်", "ေါင်း", "ောင်း", "ေါ့", "ော့", "ေါ်", "ော်", "ို", "ိုက်", "ိုင်", "ိုင့်", "ိုင်း", "ို့", "ိုး"]
numerals = "၀၁၂၃၄၅၆၇၈၉"
burmesemedials = ["ျ", "ြ", "ွ", "ှ", "ျွှ", "ျွ", "ျှ", "ြွှ", "ြွ", "ြှ", "ွှ" ]
kinzi ="င်္"

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

print("Every Burmese consonant with every medial and every rhyme")
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