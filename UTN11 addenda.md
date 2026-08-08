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

**Kayah/Karen Ni**

Preferred name seems to be Karen Ni; Kayah is a Burmese label.

p38 Kayah seemingly prefers a triangular medialWa and a sloped medialHa, though this is not a strict requirement.

p38 Kayah also requires the inclusion of punctuation sign Cwi ꤮ uniA92E.

---

**Shan**

p41 The left bowl of Nnya ၺ uni107A may optionally have a loop.

p41 The leg of Fa ၾ uni107E is best kept away from the right bowl where other marks need to sit. A leg descending from the centre of the letter and sloping to the left is a good solution. Here's how that looks in Futura100 Myanmar:

<img width="216" height="230" alt="Screenshot 2026-08-04 at 18 24 55" src="https://github.com/user-attachments/assets/def34bf4-47d1-4208-ae4c-c6ad59c52a49" />

p41 The shape of Ha ႁ uni1081 follows the Unicode chart, but this is not a standard form (perhaps the glyph in the Unicode chart should be fixed). This is preferable:

<img alt="Shan letter Ha" src="https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/1800fe8b-02c7-4c15-8b1e-30b68ef2485c">

Alternatively it can be looped, here's Futura100 Myanmar:

<img width="148" height="228" alt="Screenshot 2026-08-04 at 18 24 06" src="https://github.com/user-attachments/assets/8c620249-2cdd-45b5-a8f6-f34440e1f84e" />

---

**Khamti Shan**

p46 The language and the people are preferably called Tai Khamti rather than Khamti Shan. 

This is the current (as of 2024) consonant inventory, approved by the Tai Khamti Literary and Cultural Association:
<img width="960" height="1280" alt="01" src="https://github.com/user-attachments/assets/d51f0f9d-342e-4d2e-8554-fabd79364c4f" />

p46 ꩱ uniAA71 is incorrect. Khamti Ga is ꩠ uniAA60.

p46 ဂ uni1002 is incorrect. Khamti Gha is ၷ uni1077.

p46 ꩤ uniAA64 is the wrong shape; it needs a loop on the left bowl. Unicode chart probably needs to be updated with the correct glyph.

p46 ရ uni101B seems nowadays to prefer a shorter tail. Alternatively the loop may be reduced to a dot matching the other letters.

p46 ꩮ uniAA6E was wrongly named Khamti letter HHA in Unicode. It is the Pali retroflex LLA and has now been given an alias in Unicode (since 2020).

p46 Khamti digits [are attested](http://www.fontpad.co.uk/Documents/Proposal_for_Pwo_and_PaO_numerals.pdf), but have not yet been encoded due to lack of attestations in real life communication. These (as of 2026) seem to also be undergoing revisions and we should wait until the glyphs have stabilised.

p47 The reduplication sign ꩰ AA70 seems to be a recent invention of the Khamti Cultural Association and has been encoded atomically as a spacing glyph that follows a syllable that is to be spoken twice. In practice, in manuscripts of all the Tai groups in NE India, reduplicated syllables are written with a doubled vowel sign or doubled asat (which seems to be what AA70 represents). For this visual appearance, we can simply store the vowel or asat twice — or three or four times for tripled or quadrupled marks, which also occur. Reduplicated vowels attested include 1083, 102E, 1030, 1032 and 1036). Fonts can support the reduplication sign (AA70) and the doubled vowel characters without conflict, letting users decide which presentation they prefer.

---

**Tai Aiton & Tai Phake**

Two more Tai groups using dotted scripts like Tai Khamti. Based on study of manuscripts, here's my current understanding of their character sets, with green highlights showing glyphs that differ from the Burmese forms or are not used in Burmese. Note AA61, 1010, AA6B, 1078 and AA7A differ between Tai Aiton and Tai Phake, though manuscripts show mixed styles:

<img width="6231" height="2700" alt="Tai Aiton character set" src="https://github.com/user-attachments/assets/eeedf1dd-0726-4ed6-82b9-1688ae5c849b" />

<img width="6231" height="2700" alt="Tai Phake character set" src="https://github.com/user-attachments/assets/edcdea8e-9d8a-4247-a579-5b219f3a1c0c" />

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

p28 uni1056 ◌ၖ and uni1057 ◌ၗ should probably have dotted circles as they are dependent vowels that join a base consonant just like uni102C ◌ာ. However, it's unclear where the glyphs shown in the Unicode chart for all vocalic characters originated (both independent and dependent forms), and they are unattested in the few Sanskrit manuscripts I have seen. Here are the attestations from three Sanskrit manuscripts, with the first column showing the typeforms I've interpreted or guessed from the unclear handwriting. The top row in each cell is the independent form and the bottom is the dependent form:

<img width="3299" height="788" alt="Sanskrit vocalic letters" src="https://github.com/user-attachments/assets/a295d477-96c7-449e-aebc-ed34c1b52872" />

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

p36 Not clear why medial Ya and subjoined Ya are both listed. The subjoined version doesn't appear in my resources (though subjoined YA is not unheard of in Burmese and fonts should include it anyway)

p36 in vowels, uni1033 is annotated as 105C. 1033 is correct.

p37 uni100F ဏ and uni106E ၮ are allographs in both Burmese and in Eastern Pwo Karen, either form can be used in both languages (Unicode might want to assign equivalence to these for search and sort). However one difference is that in Eastern Pwo, the subjoined DDA ဍ does not rotate as it does in Burmese orthography, so keeping the distinction between 100F and 106E is a useful way of triggering the distinct shaping expected in Eastern Pwo.

---

**Pa'O Karen**

Note the orthography described here is for Northern Pa'O language. Southern Pa'O (aka Kham Dom) uses a distinct orthography and characters [have been proposed to Unicode]([url](https://www.fontpad.co.uk/Documents/Kham_Dom_proposal.pdf)).

p39 Medial Ha uni103E ◌ှ is also used.

p39 Dotbelow ◌့ is mis-annotated as 0137, it should be 1037.

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

p48 has -ai vowel uni1032 ◌ဲ annotated as uni1086, which is ◌ႆ Shan final -y. The preferred form is shown here, we encoded it as 1032:

<img width="5962" height="3074" alt="Screenshot 2026-08-04 at 19 16 02" src="https://github.com/user-attachments/assets/ace6ed31-77cd-4e09-81be-b8b21252cdfd" />

p48 As mentioned above, Khamti digits are attested but not yet encoded.

p49 uses uni1032 for -ai vowel, as I have done, but this conflicts with 1086 stated on previous page.

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

My current understanding of Tai Laing is shown here:

<img width="5956" height="3366" alt="Screenshot 2026-08-04 at 19 18 28" src="https://github.com/user-attachments/assets/8fd659f0-9ce4-49ca-8a4b-2c372bfdc9c9" />

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
(updated 8 August 2026)

**Danu (ဓနု) ISO dnv**

According to Wikipedia, [Danu](https://en.wikipedia.org/wiki/Intha-Danu_language) script was invented in 2013–2014 but its use remains controversial. This is unencoded and likely needs a new Unicode range separate from Myanmar. I am in touch with the script's inventor to work out a Unicode proposal.

![Danu](https://github.com/user-attachments/assets/c95e1266-00a6-4e7b-95dd-b32c2d498ce4)

---

**Htanaw or Danau (ထနော့) ISO dnu**

[Htanaw/Danau](https://en.wikipedia.org/wiki/Danau_language) uses the standard Burmese character set, though uses some non-Burmese sequences. The orthography is still a work in progress and is documented [here](https://sites.google.com/view/htanawsar/home/htanaw-alphabet-%E1%80%91%E1%80%94%E1%80%A1%E1%80%80%E1%80%81%E1%80%9B%E1%80%99).

<img width="2092" height="813" alt="Htanaw" src="https://github.com/user-attachments/assets/3bdfec08-1cc3-4d96-a8a6-2af9af66acb4" />


---

**Jingpho (ဈိာင်ဖေါစ်) ISO kac**

[Jingpho](https://en.wikipedia.org/wiki/Jingpho_language) or Kachin has a Latin orthography and a Burmese orthography, which seems to require no special extra characters.

---

**​Kayan or Padaung (ကယန်းဘာသာ) ISO pdu**

[Kayan](https://en.wikipedia.org/wiki/Padaung_language) or Padaung uses a Burmese-script orthography with the addition of two (unencoded) tonemarks. Research ongoing. 
<img width="2010" height="546" alt="Screenshot 2026-08-08 at 17 11 06" src="https://github.com/user-attachments/assets/6ca657f0-725d-4756-9489-80d9f740a227" />

---

**Khami / Khamee (ခမိဖတ်စာ) ISO cnk/cek**

[Khami/Khamee or Khumi](https://en.wikipedia.org/wiki/Khumi_language) is a language of Western Burma and Eastern Bangladesh. It uses an orthography based on Burmese, with the addition of three (unencoded) consonants of uncertain sound values and a tonemark. It's also notable that the normal belowbase ုand  ူ are not used, only the postbase forms.

![Khumi consonants](https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/90c5f98e-cdcb-43dc-a8d6-7e32249eafcc)

---

**Letalanyah (ပဂညံ/လေလ်တလဒ်ညသ်)**

Letalanyah is an orthography for S'gaw Karen used by Buddhist communities (in contrast to the S'gaw orthography listed in UTN11 which is the Christian S'gaw). Letalanyah is based on the Burmese alphabet but uses five extra (unencoded) letters to represent sounds that don't occur in Burmese, and also the medial La (u+1060). See [Kato (2023) "Letalanyah: A Buddhist writing system of S'gaw Karen"](http://user.keio.ac.jp/~kato/Letalanyah.pdf)

![Letalanyah](https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/af7f8ed3-0844-49ae-a310-fa786fa2e13a)

---

**Southern Pa'O or Kham Dom ISO**

As mentioned in the Pa'O section above, a [proposal](https://www.fontpad.co.uk/Documents/Kham_Dom_proposal.pdf) has been submitted for Kham Dom.

![Southern Pa'O](https://github.com/user-attachments/assets/cc5db0a1-7ef4-42b0-8030-f953682f2f1f)

---

**Taung Yoe (တောင်ရိုး/တွေင်ရွိုး)**

[Taung Yoe](https://en.wikipedia.org/wiki/Taungyo) is a language or dialect similar to Rakhine (Arakanese), Intha and Tavoyan (Dawei) spoken in the Eastern regions of Burma. Its orthography adds a diacritic in the shape of a left curly quote. It is likely that ̒ U+0312 "COMBINING TURNED COMMA ABOVE" is a suitable encoded character, though the comma preferably has an open counter in Taung Yoe. It's not fully described what this diacritic signifies, but Pat McCormick suggested it marks letters with a different sound value than the regular Burmese default (the letter should be pronounced in the Taung Yoe way, not the Burmese way). We can see two commas above the ဃ in the first row of this table:

![Taung Yoe](https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/9c63c51b-8310-49c1-9bc5-39fd8716861a)

If using U+0312, we need to make sure sequences like က̒ိ (U+1000 U+0312 U+102D) are handled by the font. Since the comma diacritic modifies the consonant, it would seem logical to store it directly after the consonant, before any dependent vowel sign; however, Harfbuzz doesn't permit u+0312 to come between a Myanmar base and mark, so we advise storing the comma diacritic at the end of the sequence and letting the font reorder it to the correct visual appearance.

---

**Tai Sar (Tai Soh, Maingtha)**

Next to no information about this Tai group in Kachin State. They seem to use a reformed/revised version of the Lik Tai script, with many unique letterforms that could be encoded, though maybe not in the Myanmar ranges.

![Tai Sar image](https://github.com/ohbendy/Myanmar-font-resources/assets/12471463/6e4b4ea4-37d4-4240-a23d-e474e4b4b83e)

