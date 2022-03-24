## Languages supported by Myanmar script

With __language__ tags for OpenType, ISO 639, BCP 47 and concatenated Harfbuzz language + script tags for HTML. 

For making and testing fonts, we need to know the OpenType language tags as well as the ISO 639 language tags; to achieve variant forms for Mon, for example, a font's OpenType lookups need to be registered under `MON `, but the HTML language needs to be set as `mnw`.

Note the OpenType __script__ tag `mymr` is deprecated, we should always use `mym2`. 

Number of speakers is very approximate in some cases, and should not be taken as an estimate of number of script users as literacy rates vary. Likewise languages no longer spoken do not imply there are no script users, since Pali, Sanskrit and Old Burmese are used for religious and academic purposes.

| Language | № of speakers | OpenType | ISO 639-1 | ISO 639-2 | ISO 639-3 | BCP 47 | Harfbuzz | 
|-----------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Burmese|33 million|BRM_|my|bur/mya|mya||my-x-hbscmym2|
|Arakanese [Rakhine]|1m|ARK_|||mhv, rmz, rki||rki-x-hbscmym2|
|Chin, Asho Chin|50k|QIN_|||bgr, cnh, cnw, czt, sez, tcp, csy, ctd, flm, pck, tcz, zom, cmr, dao, hlt, cka, cnk, mrh, cbl, cnb, csh||
|Eastern Pwo Karen, monastic orthography|1m|KJP_||||kjp-Mymr-x-phlouyu|
|Eastern Pwo Karen, Buddhist orthography||KJP_||||kjp-Mymr-x-thiyon||
|Eastern Pwo Karen, Christian orthography||KJP_||||kjp-Mymr-x-chekhi||
|Geba Karen|40k|(KRN_)*|||kvq|kvq-x-hbot-4b565120|
|Intha|100-200k||||int||
|Jingpho [Kachin]|1m|||kac|kac|||
|Karen||KRN_|||kar||
|Kayah [Li] [Western Kayah]|190k|KYU_|||kyu||
|Moken|8k||||mwt||
|Mon (in Burma)|851k|MON_|||mnw||
|Mon (in Thailand)||MONT|||mnw|mnw-Mymr-x-thai|
|Old Burmese|no longer spoken||||obr||
|Pa'O Karen|560k|BLK_|||blk||
|Pale [Ruching] Palaung|All Palaung 560k|PLG_|||pce||
|Pali|no longer spoken|PAL_|pi|pli|pli||
|Rumai Palaung|All Palaung 560k|PLG_|||rbb||
|S'gaw Karen|1.5m|KSW_|||ksw||
|Sanskrit|no longer spoken|SAN_|sa|san|san||
|Shan|3.3m|SHN_||shn|shn||
|Shan Ni [Tai Laing]|100k|TJL_|||tjl||
|Shwe Palaung|All Palaung 560k|PLG_|||pll||
|Tai Aiton|1500|AIO_|||||
|Tai Khamti [Khamti Shan]|13k|KHT_|||kht||
|Tai Khamyang| 50 |||| ksu, nrr ||
|Tai Phake|2000|PHK_|||phk||
|Tai Turung|no longer spoken||||try|| 
|Tavoyan|440k||||tvn||
|Western Pwo Karen|210k|PWO_|||pwo||

* No tag currently exists for Geba Karen; KRN_ is the generic tag for Karen languages
