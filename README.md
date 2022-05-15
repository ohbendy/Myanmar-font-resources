# Myanmar font resources
 Bits and bobs for making and checking Myanmar fonts
 
## [Languages](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Languages.md)
This lists the languages that can be written in the Burmese script, with their OpenType and ISO 639 language tags and an estimation of the number of speakers.
 
## [Myanmar alphabets](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Myanmar%20alphabets.md)
This lists all the consonants of each alphabet currently enabled by Unicode. Mainly based on [UTN11v4](https://www.unicode.org/notes/tn11/UTN11_4.pdf) but with additions from my own research.

## [Unicode texts](https://github.com/ohbendy/Myanmar-font-resources/tree/master/Unicode%20texts)
Short texts for proofing fonts in different languages. Texts converted from ASCII or online sources. Depending on the fonts available on your system, text may appear broken, but it also might contain encoding errors. Apologies if any content is inappropriate or copyrighted, I can't read any of these languages.

## [Burmese conjunct table](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Burmese%20conjunct%20table.md)
This shows every pair of consonants of the Burmese alphabet as a stacked conjunct.

## [Burmese Sanskrit conjuncts](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Burmese%20Sanskrit%20conjuncts.txt)
 This contains a list of conjuncts compiled from several sources:
 - Ulrich Stiehl's conjunct list: http://www.sanskritweb.net/sansdocs/mathe.pdf
 - Ulrich Stiehl's Technical Manual: http://www.sanskritweb.net/itrans/itmanual2003.pdf
 - Ulrich Stiehl's Conjunct Consonants in Sanskrit: http://www.sanskritweb.net/sansdocs/preview.pdf
 - Two Burmese Sanskrit conjunct charts received by email
 - Tiro Typeworks' list of Sanskrit Conjuncts

#### In my Burmese transcriptions:
- conjuncts are grouped by their number of consonants for easier font auditing;
- repha is used when r- is the first consonant of a conjunct;
- kinzi is used when ṅ- is the first consonant of a conjunct;

#### Following advice from Christian Lammerts:
- ñ is transcribed with small nya ဉ and not big nnya ည
- when Ya, Ra, Va and Ha appear non-initially, Burmese medial forms are used rather than vertically-stacked virama sequences. This could theoretically lead to ambiguity since -kry- and -kyr- would have the same visual appearance.

Note almost all Burmese fonts go awry when more than two consonants should stack together, so rendering here should not be trusted.

## [Burmese Pali conjuncts](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Burmese%20Pali%20conjuncts.txt)
Compiled from:
- Okell's Burmese: An introduction to the script p384
- Several of my books in Burmese Pali (may contain Sanskrit words?)
- [List of Pali conjuncts from Tiro Typeworks](https://docs.google.com/document/d/10jaDPY0EcYenspj-iPDqZsCSta1eN46L4QLPXqeYMQs/edit#) (thanks John)

## [Shan Pali conjuncts](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Shan%20Pali%20conjuncts.txt)
This is a direct conversion to Pali letters from the Burmese Pali conjuncts list. Standard Shan orthography doesn't stack conjuncts, instead using the asat character to cancel inherent vowels. But some older orthographies stack consonants; those for which attestations have been found are marked with an asterisk. Note most fonts do not support subjoined Shan Pali letters so rendering may be questionable.
Compiled from:
- Transliterating list of Burmese Pali conjuncts above
- Last three at the bottom of the list are found in one of my Shan writing primers.

## [Localised forms](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Localised%20forms.md)
This notes the glyphs variations needed for some of the languages of Burma.

## [Generate syllables](https://github.com/ohbendy/Myanmar-font-resources/tree/master/Generate%20syllables.py)
Python scripts for checking that glyphs are interacting correctly, currently just for Burmese and Mon languages, others can be added.
First we categorise each character or sequence. 

### Burmese ###
For Burmese, consonants includes just the base consonants used for Burmese language. Rhymes includes all possible syllable endings (vowel or vowel + final consonant, with or without tonemarks). (Though the round -aa and tall -aa are used with different bases, we test both with all consonants.) Medials includes each of the four Burmese medial letters (medialYa, medialRa, medialWa and medialHa) and the seven possible combinations of those. Kinzi contains the single sequence 1004 103A 1039, which can be added to any syllable.

We then generate combinations of every consonant with every rhyme; every consonant with every medial and every rhyme; every consonant with every subjoined consonant; every conjunct with every rhyme; every conjunct with medialYa or medialRa and every rhyme; and then the whole lot again with kinzi. 

Beware, this script generates 572,290 Burmese syllables. Is it an exhaustive list of every possible syllable? I don't know :) 

### Mon ###
For Mon language, we combine each Mon initial with each permissible vowel sequence and then each permissible final consonant. We then combine each independent vowel with each final consonant. Finally we combine each permissible conjunct with each vowel and final consonant. This generates 137,909 syllables.

### S'gaw ###
For S'gaw, we run through the consonants, combining them with every vowel and tonemark. We then run through every permitted initial with medial consonant, and do the same with every vowel and tonemark. Tall Aa does not combine with tonemarks so is cycled in a different way. This generates 3420 syllables.

### Western Pwo ###

### Eastern Pwo ###

### Pa'O ###

### Geba ###

### Kayah ###

### Asho ###

### Shan ###
For Shan language, we cycle through each Shan consonant (not currently including borrowed ones from Burmese that occasionally crop up), combining it with every rhyme and tonemark. We then cycle through each permitted initial cluster, combining each with every rhyme and tonemark. This generates 17,364 syllables.

### Tai Khamti ###

### Tai Aiton and Phake ###

### Tai Laing / Shan Ni ###

### Rumai Palaung / Ta'ang ###
Here we cycle through every initial consonant with every syllable rhyme (including tonemarks), and then repeat with initial clusters. This produces 35,916 syllables.

## [Collisions](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Collisions.md)
A list of cluster pairs that cannot be handled by spacing alone, useful for testing collisions in your Burmese font. As so many syllables have above- and below-base elements that stick out further than the base letter, we need to add contextual kerning rules to ensure such collisions are taken care of. 

Each glyph in the list actually stands for a class. မ is a one-bowl letter, so we also need to test clusters where it appears with other one-bowl letters such as ခ ဂ င စ ဇ ဎ ဒ ဓ န ပ ဖ ဗ မ ဝ. Likewise, က stands for any two-bowl letter, e.g ဃ ဆ ဏ တ ထ ဘ ယ လ သ ဟ အ. Similarly, ွ represents any one-bowl subscript letter, ္က represents any two-bowl subscript. Basing our classes on sidebearings means ဠ represents letters with a bowl that opens to the right and has a descender (ဋ ဌ), while ဉ် represents letters with a bowl that opens to the left and has a descender (ည ဍ etc). Characters like ဈ form another class, including medialYa ျ and post-base forms of -u and -uu; those all have the vertical stem and probably the same right sidebearing which needs to be checked against any below-base elements on the following cluster. 

Then there are various 'legs' that attach below base letters, vowels -u and -uu, medialHa, and combinations of those characters. I separated the consonant Na and the below base ligature medialWaHa into their own groups because they present singular challenges. Below base elements may also collide with a following medialRa. And all the combinations need to be tested when there's a dotbelow in the first cluster. 

Coding all the contextual kerning rules manually means measuring the amount of space needed to avoid collisions and writing rules to handle each situation. And of course the distances will vary between weights/styles in the font. And we want to make sure that clusters don't bump when there's also a wordspace between them. So an algorithmic approach would be much more reliable.

## [Confusables](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Confusables.md)
Noting the sequences that have similar visual appearance, and how some designs can distinguish those sequences.

## [Reduplication](https://github.com/ohbendy/Myanmar-font-resources/blob/master/Reduplication.md)
Explaining how reduplication works in different orthographies.
