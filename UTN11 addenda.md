## Version 4 (13/12/2012) ##

---

p1 Geba, a Karen language, is not included. It is based on the other Karen orthographies (S'gaw, Pwo, Pa'O) with the addition of one extra character, uni1071 ၱ .

---

**Pali/Sanskrit**

p28 Note the sha ၐ uni1050 and ssa ၑ uni1051 have open rings inside the bowls in the Padauk font used here. The Unicode chart has simple dots, which will lead to confusion with Tai Laing letter Ba ꧽ uniA9FD.

p28 Note that uni1056 and uni1057 should be shown with dotted circles as they are dependent signs that join visually to the base consonant.

p28 Burmese Sanskrit conjunct tables show quite a lot of special ligature forms which fontmakers could optionally include.

p29 rapha -> r*e*pha

---

**Arakanese**

p30 Arakenese -> Arak*a*nese

We find quite a lot of [different letterforms](https://www.unicode.org/L2/L2020/20163-arakanese-mon.pdf) in Arakanese manuscripts which fontmakers may wish to use in place of the Burmese letterforms.

---

**Mon**

p31 Mon in Thailand use [alternate forms](https://www.unicode.org/L2/L2020/20163-arakanese-mon.pdf) of ဆ ဇ ဈ ဋ ဌ ဍ န ရ သ ဠ အ ဥု ာ ၊ ။ ၉ which fontmakers may wish to use in place of the Burmese letterforms. Note also the Thai Mon do not always use the Tall Aa but may use a round aa with a dip in the top to differentiate က from ဂ + ာ.

p31 Mon letter BBA ၜ uni105C can have a dot instead of a ring, depending on the design of the font.

p31 Note also Great Sa ဿ uni103F is not used in Mon; instead the stacked form သ္သ is used.

p31 The sequence uni102C/102B followed by uni1032 follows the same logic as uni102C/102B followed by uni1036, i.e the 1032 or 1036 appears above the 102C or preceding the 102B carried on the base consonant of the cluster. Fonts need to reorder both 1032 and 1036 before a tall Aa to achieve this.

---

**Eastern Pwo**

p36 should include the consonants Ywa ၯ uni106F and Ghwa ၰ uni1070. The leg is normally centred below the right-hand bowl.

p36 Numerals for Eastern Pwo are now encoded in the range uni116DA–uni116E3.

---

**Pa'O**

p37 Numerals for Pa'O are now encoded in the range uni116D0–116D9.

---

**Kayah**

p38 Kayah seemingly prefers a triangular medialWa and a sloped medialHa.

p38 Kayah also requires the inclusion of punctuation sign Cwi ꤮ uniA92E.

---

**Shan**

p41 The left bowl of Nnya ၺ uni107A may optionally have a loop.

p41 The leg of Fa ၾ uni107E is best kept away from the right bowl where other marks need to sit. A leg descending from the centre of the letter and sloping to the left is a good solution.

p41 The shape of Ha ႁ uni1081 follows the Unicode chart, but this is not a standard form. This is preferable:

<img alt="Shan letter Ha" src="https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/1800fe8b-02c7-4c15-8b1e-30b68ef2485c">

---

**Khamti Shan**

p46 The language and the people are preferably called Tai Khamti rather than Khamti Shan. 

p46 ꩱ uniAA71 is incorrect. Khamti Ga is ꩠ uniAA60.

p46 ဂ uni1002 is incorrect. Khamti Gha is ၷ uni1077.

p46 ꩤ uniAA64 is the wrong shape; it needs a loop on the left bowl. Unicode chart needs to be updated with the correct glyph.

p46 ရ uni101B uses the dotted form, and it seems nowadays to prefer a shorter tail. If using variation selectors this should be reflected. I don't prefer using VS — that mechanism doesn't work for nonspacing characters like the vowel signs, and implementation is extremely unpredictable. For the dotted letterforms we can either consider it a font-level question (different fonts for Burmese and Khamti languages, with dots for Khamti) or using OpenType LOCL features to switch from default to dotted forms.

p46 ꩮ uniAA6E was wrongly named Khamti letter HHA in Unicode. It is the Pali retroflex LLA.

p46 Khamti digits [are attested](http://www.fontpad.co.uk/Documents/Proposal_for_Pwo_and_PaO_numerals.pdf), but have not yet been encoded.

p47 The reduplication sign ꩰ AA70 seems to be a recent invention of the Khamti Cultural Association and has been encoded atomically as a spacing glyph that follows a syllable that is to be spoken twice. In practice, reduplicated syllables are written with a doubled vowel sign or doubled asat (which seems to be what AA70 represents). For this visual appearance, we can simply store the vowel or asat twice — or three or four times for tripled or quadrupled marks. Reduplicated vowels attested include 1083, 102E, 1030, 1032 and 1036). Supporting both ways allows the user to choose either the reduplication sign or the doubled vowels.

---

**Aiton & Phake**

p49 It's a bit confusing to have Aiton and Phake presented in a Khamti style.

p49 The consonant list is missing Sa ꩬ AA6C.

p49 In the 'subjoined consonants' list, AA60 is a Shan letter which is not listed in the 'consonants' section. It was probably meant to be Ca ꩡ AA61. Stephen Morey also suggests Nga င 1004, Nya ၺ 107A, Na AA6B, Ma မ 1019, Sa ꩬ AA6C can be subjoined.

p49 In the diphthongs list, the au vowel ꧥ  A9E5 has been misidentified as the asat ်  103A, and I believe the medial Na ၞ 105E in the last sequence is a misidentification of Shan medial Wa ႂ  1082 (it is analysed as a medial Wa phonetically). Thus we have: 

| ံ | ꧥံ | ႝ | ွႝ | ွေ | ိုႜ | ွꧥ | ႂꧥ (or sometimes just ꧥ  ) | 
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| -am | -ɛm | -ai | -ɔi | -oi (Phake only) | -ui | -au | -aɯ |
|1036|A9E5 1036|109D|103D 109D|103D 1031|102D 102F 109C|103D A9E5|1082 A9E5 (or A9E5)|

---
 
## Version 5 (02/07/2020) ##

---

**Old Burmese**

p26 In Old Burmese, medial La (◌္လ 1039 101C) is also used. 

p27 uni1051 (ၑ) is not listed in consonant inventory on p26. Conjunct forms vary (see https://github.com/googlefonts/noto-fonts/issues/1158#issuecomment-753618024)

p27 On the last line, medial La and medial Wa should stack vertically, not overlap.

---

**Pali-Sanskrit**

p28 uni1056 ◌ၖ and uni1057 ◌ၗ should probably have dotted circles as they are dependent vowels that join a base consonant just like uni102C ◌ာ.

---

**Mon**

p31 In Mon language, the letter Nga uni105A ၚ does not lose its tail when combining with vowels -u and -uu; instead those switch to post-base forms. Nga does lose its tail when combined with asat uni103A.

p31 Some sequences should be added to dependent vowels:
- 102E (= 102D + 1036) ◌ီ
- 102E 102F ◌ီု
- 102F 1032 ◌ုဲ
- 1031 1032 ေဲ
- 1031 102C 1032 ေ◌ာဲ
- 102D 102F 1032 ◌ိုဲ

p31 Sequence of tallAa uni102B ◌ါ followed by -ai vowel uni1032 ◌ဲ behaves the same as tallAa followed by anusvara uni1036 ◌ံ, i.e. the mark sits on the consonant, not the tallAA.

---

**S'gaw Karen**

p34 Medial Wa is preferably triangular.

p34 What font mechanism is suggested to allow post-base forms of -u and -uu? ZWJ/ZWNJ is not reliable.

---

**Eastern Pwo Karen**

p36 Not clear why medial Ya and subjoined Ya are both listed. The subjoined version doesn't appear in my resources.

p36 in vowels, uni1033 is annotated as 105C. 1033 is correct.

p37 uni106E ၮ is equally possible as uni100F ဏ; it's not clear to me why 106E was encoded separately, it's just a stylistic difference and both styles are found in Standard Burmese and in Karen. If two codepoints are proposed to be used for the same letter, Unicode should probably assign equivalence so that search and sort treat them the same way.

---

**Pa'O Karen**

p39 Medial Ha uni103E ◌ှ is also used.

p39 Dotbelow ◌့ is mis-annotated as 0137, it should be 1037.

p39 Tonemark uni108F ◌ႏ can optionally take the alternate style made of three dots stacked vertically.

---

**Kayah**

p40 Medial Ha is preferably sloped.

---

**Asho Chin**

p42 Dotbelow uni1037 ◌့ preferably sits to the left of other below-base marks.

---

**Shan**

p43 lists uni109F ႟ as a vowel, but it is a punctuation sign.

---

**Khamti Shan**

p48 Further vowel sequences include:

- 1032/1086 1062  ဲၢ
- 101D 103A ◌ဝ်
- 1062 101D 103A ◌ၢဝ်
- 102D 101D 103A ◌ိဝ်
- 103B 1083 ◌ျႃ
- 1085 101D 103A ◌ႅဝ်
- 1031 1030 ေူ
- 103D ◌ွ (note this is a vowel in Khamti, not a medial)
- 103D 1083 ◌ွႃ
- 103D 1032 ◌ွဲ
- 102D 1030 ◌ိူ
- 102D 102F 101D 103A ◌ိုဝ်
- 102D 1030 101D 103A ◌ိူဝ်
- 1030 101D 103A ◌ူဝ်
- 1031 1083 ေႃ
- 103A ◌်

p48 has -ai vowel uni1032 ◌ဲ annotated as uni1086, which is ◌ႆ Shan final -y.

p48 Khamti digits are attested but not yet encoded.

p49 uses uni1032 for -ai vowel, but p48 suggests uni1086, unclear which to use.

---

**Aiton & Phake**

p51 uniAA6C Khamti letter Sa ꩬ is missing from the consonant inventory.

p51 There seems to be a font issue with the subjoined consonants.

p51 In diphthongs we also find:

- 103D 102F ◌ွု as a ligature
- 102F 1036 ◌ုံ

The following are also used:

- 103A ◌်
- AA70 ꩰ reduplication mark (and combinations with 102E, 1036, 103A, 109D/1086/1032), though implementation is unclear.

---

**Tai Laing** (Endonym is Shan-Ni)

p53 uniA9EC ꧬ appears twice in the consonant inventory.

p53 The following should be included:

- 103D ◌ွ (medial wa used as vowel)
- 1062 ၢ
- 1035 ဵ
- 1062 1086 ၢႆ 
- 103D 1086 ◌ွႆ

p53 Numeral 9 is a 180° rotation of numeral 8, this sideways version seems to be outdated.

---

**Pale Palaung**

p58 Sequence 102D 102F 101D 1038 is represented as 102D 102F 101D **103A** 1038

---

**Rumai Palaung**

p60 Tonemark annotated as uni1089 is in fact uni1087.

---

**Moken**

p61 Moken language tag should be mwt as per the SIL website, not mwk.


---

# Additional languages #
(updated 12 July 2024)

**Danu (ဓနု) ISO dnv**

According to Wikipedia, [Danu](https://en.wikipedia.org/wiki/Intha-Danu_language) script was invented in 2013–2014 but its use remains controversial. Uncertain whether Danu should be encoded into the existing Burmese ranges or as a unique script, since some of the letters match Burmese, some are very different, and some conflict with Burmese (e.g ဎ = ပ).

![Danu](https://github.com/user-attachments/assets/c95e1266-00a6-4e7b-95dd-b32c2d498ce4)

---

**Jingpho (ဈိာင်ဖေါစ်) ISO kac**

[Jingpho](https://en.wikipedia.org/wiki/Jingpho_language) or Kachin has a Latin orthography and a Burmese orthography, which seems to require no special extra characters.

---

**Khami (ခမိဖတ်စာ) ISO cnk/cek**

[Khami or Khumi](https://en.wikipedia.org/wiki/Khumi_language) is a language of Western Burma and Eastern Bangladesh. It uses an orthography based on Burmese, with the addition of three (unencoded) consonants and a tonemark. It's also notable that the normal belowbase ုand  ူ are not used, only the postbase forms.

![Khumi consonants](https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/90c5f98e-cdcb-43dc-a8d6-7e32249eafcc)

---

**Letalanyah (ပဂညံ/လေလ်တလဒ်ညသ်)**

Letalanyah is an orthography for S'gaw Karen used by Buddhist communities (in contrast to the S'gaw orthography listed in UTN11 which is the Christian S'gaw). Letalanyah is based on the Burmese alphabet but uses five extra (unencoded) letters to represent sounds that don't occur in Burmese, and also the medial La (u+1060). See [Kato (2023) "Letalanyah: A Buddhist writing system of S'gaw Karen"](http://user.keio.ac.jp/~kato/Letalanyah.pdf)

![Letalanyah](https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/af7f8ed3-0844-49ae-a310-fa786fa2e13a)

---

**Southern Pa'O**

A couple of extra characters — a diagonal diacritic below and a triple dot tonemark — need encoding for Southern Pa'O, I'm discussing with Alys Boote-Cooper to get more info.

![Southern Pa'O](https://github.com/user-attachments/assets/cc5db0a1-7ef4-42b0-8030-f953682f2f1f)

---

**Taung Yoe (တောင်ရိုး/တွေင်ရွိုး)**

[Taung Yoe](https://en.wikipedia.org/wiki/Taungyo) is a language or dialect similar to Rakhine (Arakanese), Intha and Tavoyan (Dawei) spoken in the Eastern regions of Burma. Its orthography adds a diacritic in the shape of a left curly quote. It is likely that ̒ U+0312 "COMBINING TURNED COMMA ABOVE" is a suitable encoded character, though the comma preferably has an open counter in Taung Yoe. It's not fully described what this diacritic signifies, but Pat McCormick suggested it marks letters with a different sound value than the regular Burmese default (the letter should be pronounced in the Taung Yoe way, not the Burmese way). We can see two commas above the ဃ in the first row of this table:

![Taung Yoe](https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/9c63c51b-8310-49c1-9bc5-39fd8716861a)

If using U+0312, we need to make sure sequences like က̒ိ (U+1000 U+0312 U+102D) are handled by the font. Since the comma diacritic modifies the consonant, it would seem logical to store it directly after the consonant, before any dependent vowel sign; however, Harfbuzz doesn't permit u+0312 to come between a Myanmar base and mark, so we advise storing the comma diacritic at the end of the sequence and letting the font reorder it to the correct visual appearance.

---

**Tai Sar (Tai Soh, Maingtha)**

Next to no information about this Tai group in Kachin State. They seem to use a reformed/revised version of the Lik Tai script, with many unique letterforms that could be encoded.

![Tai Sar image](https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/6e4b4ea4-37d4-4240-a23d-e474e4b4b83e)

