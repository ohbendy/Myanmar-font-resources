###########################
### Tai Laing syllables ###
###########################
# tailaingpaliconsonants = ["က", "ၷ", "ꧩ", "ꧪ", "င", "ၸ", "ꩬ", "ꧫ", "ꧬ", "ꧧ", "ꩦ", "ꩧ", "ꧭ", "ꧮ","ꧯ", "တ", "ထ", "ꧻ", "ꧼ", "ꩫ", "ပ", "ꧤ", "ꧽ", "ꧾ", "မ", "ယ", "ꩺ", "လ", "ဝ", "ၐ", "ၑ", "ၯ", "ꧺ", "ဢ", "ꧨ"]
tailaingconsonants = ["က", "ၷ", "င", "ၸ", "ꩬ", "ꧧ", "တ", "ထ", "ꩫ", "ပ", "ꧤ", "ꧨ", "မ", "ယ", "ꩺ", "လ", "ဝ", "ၯ", "ဢ"]
# tailaingvowels = ["", "ႃ", "ိ", "ီ", "ေ", "ေꧥ", "ု", "ူ", "ူဝ်", "ေႃ", "ိုင်", "ိူဝ်", "ႆ", "ံ"] 
tailaingrhymes = ["", "ႃ", "ီ", "ေ", "ေꧥ", "ူ", "ူဝ်", "ေႃ", "ိုဝ်", "ိူဝ်", "ႆ", "ၢႆ", "ုꧧ်", "ူꧧ်", "ႂႆ", "ဝ်", "ၢဝ်", "ိဝ်", "ဵဝ်", "ꧥဝ်", "ႂꧥ", "မ်", "ၢမ်", "ိမ်", "ဵမ်", "ꧥမ်", "ုမ်", "ူမ်", "ွမ်", "ိုမ်", "ိူမ်", "ꩫ်", "ၢꩫ်", "ိꩫ်", "ဵꩫ်", "ꧥꩫ်", "ုꩫ်", "ူꩫ်", "ွꩫ်", "ိုꩫ်", "ိူꩫ်", "င်", "ၢင်", "ိင်", "ဵင်", "ꧥင်", "ုင်", "ူင်", "ွင်", "ိုင်", "ိူင်", "ပ်", "ၢပ်", "ိပ်", "ဵပ်", "ꧥပ်", "ုပ်", "ူပ်", "ွပ်", "ိုပ်", "ိူပ်", "တ်", "ၢတ်", "ိတ်", "ဵတ်", "ꧥတ်", "ုတ်", "ူတ်", "ွတ်", "ိုတ်", "ိူတ်", "က်", "ၢက်", "ိက်", "ဵက်", "ꧥက်"] # Note: because the rhymes have vowel + final, the tonemarks being appended after the rhymes puts them in the wrong spot. To be fixed.
tailainginitialclusters = ["ကျ", "ၷျ", "ၸျ", "တျ", "ꩫျ", "ပျ", "ꧤျ", "မျ", "လျ", "ကျႂ", "ၷျႂ", "ၸျႂ", "ကြ", "ၷြ", "ၸြ", "ꩬြ", "တြ", "ထြ", "ကႂ", "ၷႂ", "ငႂ", "ၸႂ", "ကွ", "ၷွ", "ငွ", "ၸွ"] # Sources are ambiguous, it might be possible to have any consonant with medialRa or the two medialWa characters
tailaingtonemarks = ["", "ႍ", "ꩼ", "း", "့", "ꩽ"]
numerals = "꧰꧱꧲꧳꧴꧵꧶꧷꧸꧹"

print("Every Tai Laing consonant")
for tailaingconsonant in tailaingconsonants:
	print(tailaingconsonant, end=' ')
print()
print()

print("Every Tai Laing rhyme")
for tailaingrhyme in tailaingrhymes:
	print("◌" + tailaingrhyme, end=' ')
print()
print()

print("Every Tai Laing tonemark")
for tailaingtonemark in tailaingtonemarks:
	print("◌" + tailaingtonemark, end=' ')
print()
print()

print("Every Tai Laing consonant with every rhyme and tonemark")
for tailaingconsonant in tailaingconsonants:
	for tailaingrhyme in tailaingrhymes:
		for tailaingtonemark in tailaingtonemarks:
			print(tailaingconsonant + tailaingrhyme + tailaingtonemark, end=' ')
	print()
print()
print()

print("Every Tai Laing intial cluster with every rhyme and tonemark")
for tailainginitialcluster in tailainginitialclusters:
	for tailaingrhyme in tailaingrhymes:
		for tailaingtonemark in tailaingtonemarks:
			print(tailainginitialcluster + tailaingrhyme + tailaingtonemark, end=' ')
	print()
print()
print()
