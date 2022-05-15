######################
### Shan syllables ###
######################

shanconsonants = ["ၵ", "ၶ", "င", "ၸ", "သ", "ၺ", "တ", "ထ", "ၼ", "ပ", "ၽ", "ၾ", "မ", "ယ", "ရ", "လ", "ဝ", "ႁ", "ဢ"]
shanrhymes = ["", "ႃ", "ီ", "ူ", "ေ", "ႄ", "ူဝ်", "ေႃ", "ိုဝ်", "ိူဝ်", "ႆ", "ၢႆ", "ုၺ်", "ူၺ်", "ွႆ", "ိုၺ်", "ဝ်", "ၢဝ်", "ိဝ်", "ဵင်", "ႅဝ်", "ႂ်", "မ်", "ၢမ်", "ိမ်", "ဵမ်", "ႅမ်", "ုမ်", "ူမ်", "ွမ်", "ိုမ်", "ိူမ်", "ၼ်", "ၢၼ်", "ိၼ်", "ဵၼ်", "ႅၼ်", "ုၼ်", "ူၼ်", "ွၼ်", "ိုၼ်", "ိူၼ်", "င်", "ၢင်", "ိင်", "ဵင်", "ႅင်", "ိင်", "ူင်", "ွင်", "ိုင်", "ိူင်", "ပ်", "ၢပ်", "ိပ်", "ဵပ်", "ႅပ်", "ုပ်", "ူပ်", "ွပ်", "ိုပ်", "ိူပ်", "တ်", "ၢတ်", "ိတ်", "ဵတ်", "ႅတ်", "ုတ်", "ူတ်", "ွတ်", "ိုတ်", "ိူတ်", "ၵ်", "ၢၵ်", "ိၵ်", "ဵၵ်", "ႅၵ်", "ုၵ်", "ူၵ်", "ွၵ်", "ိုၵ်", "ိူၵ်"]
shantonemarks = ["", "ႇ", "ႈ", "း", "ႉ", "ႊ"]
shannumerals = "႐႑႒႓႔႕႖႗႘႙"
shaninitialclusters = ["ၵျ", "ၶျ", "ပျ", "ၽျ", "မျ", "လျ", "ၵြ", "ၶြ", "သြ", "တြ", "ၽြ", "ၵႂ", "ၶႂ", "သႂ", "တႂ", "မႂ"]


print("Every Shan consonant")
for shanconsonant in shanconsonants:
	print(shanconsonant, end=' ')
print()
print()

print("Every Shan rhyme")
for shanrhyme in shanrhymes:
	print("◌" + shanrhyme, end=' ')
print()
print()

print("Every Shan tonemark")
for shantonemark in shantonemarks:
	print("◌" + shantonemark, end=' ')
print()
print()

print("Every Shan consonant with every rhyme and tonemark")
for shanconsonant in shanconsonants:
	for shanrhyme in shanrhymes:
		for shantonemark in shantonemarks:
			print(shanconsonant + shanrhyme + shantonemark, end=' ')
	print()
print()
print()

# print("Every Shan initial cluster")
# for shaninitialcluster in shaninitialclusters:
# 	print(shaninitialcluster, end=' ')
# print()
# print()

print("Every Shan initial cluster with every rhyme and tonemark")
for shaninitialcluster in shaninitialclusters:
	for shanrhyme in shanrhymes:
		for shantonemark in shantonemarks:
			print(shaninitialcluster + shanrhyme + shantonemark, end=' ')
	print()
print()
print()
