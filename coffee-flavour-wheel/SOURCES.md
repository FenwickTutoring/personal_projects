# Sources

Every compound on the wheel is listed below with two kinds of reference: one showing that it **occurs in coffee** (ideally as an odour- or taste-active compound), and one for the **descriptor** printed on the poster. The full references are at the bottom.

**How the data were put together.** Molecular formulas are computed from each structure (SMILES in `generator/wheel.py`) using RDKit, so the formula and the drawn structure always agree. The compound list and descriptors were first drafted from general knowledge of the coffee-aroma literature. After a reader asked for sources (thank you!), each entry was checked against the references below. Eight compounds without good evidence were removed and around 25 descriptors were corrected (see [Changes after review](#changes-after-review)).

**Caveats.**
- This is a simplified, enthusiast-level poster, not a complete aroma model. Roasted coffee has more than 1,000 identified volatiles [Budryn2011]. How strongly any one of them is perceived depends on its concentration relative to its odour threshold, and on the rest of the matrix [Czerny1999; Buffo2004].
- Several classic Grosch-group papers (Czerny 1999, Czerny & Grosch 2000, Mayer 2000, Semmelroch & Grosch 1996) were cited via later papers that reproduce their data, because the originals were paywalled during the check. These are marked *(via …)*.
- Descriptors are for the compound in coffee where a coffee study gives one; otherwise they come from odour databases (Flavornet, The Good Scents Company) and are marked as such.
- Corrections are very welcome: please open an issue or pull request.

## Compound by compound

| Compound | Poster descriptor | Occurs in coffee | Descriptor source |
|---|---|---|---|
| **Floral** | | | |
| Linalool | floral, citrus | [Chen2025] (OAV 72–222); [Vezzulli2023] | [Chen2025]: "floral, lemon, rose" |
| β-Damascenone | rose, cooked apple | [Sanz2002]; [Hofmann2001] *(via Mayer 2000)*; [Akiyama2003] | [Scheidig2007]: "cooked apple"; [Flavornet]: "apple, rose, honey" |
| **Fruity** | | | |
| Ethyl 2-methylbutanoate | fruity, sweet | [Scheidig2007] (key odorant of raw coffee) | [Scheidig2007]: "fruity" |
| Ethyl 3-methylbutanoate | fruity, sweet | [Scheidig2007] (key odorant of raw coffee) | [Scheidig2007]: "fruity"; [Flavornet]: "fruit" |
| 3-Mercapto-3-methylbutyl formate (MMB formate) | blackcurrant, catty | [Sanz2002]; [Hofmann2001]; [Akiyama2003] | [Akiyama2003]: "green-black currant"; [TGSC]: "sulfurous catty" |
| Limonene | citrus; variety-dependent | [Chen2025] (weak, FD 1); [Marie2024] (elevated in Geisha) | [Chen2025]: "lemon"/"orange"; [Marie2024]: "citrus note" |
| Acetaldehyde | pungent, fruity | [Hofmann2001] (470 µg/100 mL brew, *via Mayer 2000*); [Holscher1992] | [Holscher1992]: "pungent, fruity" |
| **Sour / Fermented** | | | |
| Citric acid | bright, clean sourness | [Chen2025]; [Yeager2021] | Taste only (non-volatile). [Rune2023]: only citric acid was picked out (as more acidic) by untrained tasters |
| Malic acid | tart, sharp sourness | [Chen2025]; [Yeager2021] | Taste only. [Yeager2021]: raises acidity intensity; no specific fruit note shown |
| Lactic acid | soft, mild sourness | [Chen2025]; [Rune2023] | Taste only. [Yeager2021]: associated with mouthfeel |
| Acetic acid | vinegar, winey | [Chen2025]; [Yeager2021] | [Chen2025]: "vinegar"; [Seninde2020]: "fruity, winey, fermented" |
| Quinic acid | sour, slightly bitter | [Engelhardt1985] (≈4.7 % of titratable acidity) | [Yeager2021]: "slightly bitter", astringent |
| Phosphoric acid | minor; experts can't detect it | [Engelhardt1985] (≈2.5 % of titratable acidity) | [Rune2023]: experts could not identify it even at twice its natural level |
| Butanoic acid | rancid butter | [Chen2025] | [Chen2025]: "butter, cheese, sour"; [WCR2017] "Butyric acid" reference |
| 3-Methylbutanoic acid | sweaty, cheesy | [Scheidig2007]; [Chen2025]; [Chin2011] | [Scheidig2007]: "sweaty"; [WCR2017] "Isovaleric acid": sweaty, aged cheese |
| **Green / Vegetative** | | | |
| IBMP (3-isobutyl-2-methoxypyrazine) | bell pepper, peapod | [Scheidig2007]; [Czerny2000]; [Cantergiani2001] | [Scheidig2007]: "bell pepper-like"; [Cantergiani2001]: "green, earthy, broad bean pod, peas" |
| IPMP (3-isopropyl-2-methoxypyrazine) | potato defect, earthy pea | [Cain2021] (potato taste defect marker); [Scheidig2007] | [Scheidig2007]: "earthy, pea-like"; [WCR-PTD]: "freshly peeled potatoes" |
| 2-Methoxy-3,5-dimethylpyrazine | earthy, musty (raw bean) | [Scheidig2007]; [Czerny2000] (normal raw-coffee odorant) | [Simpson2004]: potent musty odorant (wine corks) |
| Hexanal | green, grassy | [Scheidig2007]; [Marin2008] | [Scheidig2007]: "grassy, green" |
| **Defects & Staling** | | | |
| (E)-2-Nonenal | fatty, papery | [Scheidig2007] (raw coffee; "not a major source of off-odor") | [Scheidig2007]: "fatty"; [WCR2017] "Papery" reference compound; [CzernyButtner2009]: key cardboard odorant |
| 2,4,6-Trichloroanisole (TCA) | Rio defect: musty, iodine | [Spadone1990]; [Cantergiani2001] | [Spadone1990]: Rio flavour "medicinal, phenolic, or iodine-like", "musty" |
| Geosmin | earthy, mouldy | [Cantergiani2001] (mouldy/earthy defect) | [Cantergiani2001]: "mouldy"; [FooDB]: "earthy, musty, beet" |
| **Bitter & Mouthfeel** | | | |
| Caffeine | pure bitter; ~10–15 % of it | [WCR2017] | [WCR2017]: bitter taste reference. ≈10–15 % of coffee bitterness: [ACS2007]; main bitter compounds are CGA lactones [Frank2006] |
| Trigonelline | bitter; partly roasts to niacin | [LangHof2009] | Bitterness: older literature (Ordynsky 1965, via coffeeresearch.org). Partial breakdown to nicotinic acid, N-methylpyridinium and pyridines: [LangHof2009] |
| N-Methylpyridinium | odourless dark-roast marker | [Lang2013]; [LangHof2009] | Non-volatile cation, formed from trigonelline; rich in dark roasts [Lang2013]. No taste role established |
| Chlorogenic acid (5-CQA) | astringent, mouthcoating | [Lang2013] | Not itself bitter [ACS2007]. Mouthcoating/astringency: weak evidence (conference abstract) |
| Chlorogenic acid lactones | coffee-typical bitter | [Frank2006]; [Blumberg2010] | [Blumberg2010]: "coffee-typical bitter taste"; ≈80 % of decaf bitterness [Frank2006] |
| **Oil & Gas** | | | |
| Cafestol | coffee oil; filters remove it | [Urgert1997]; [Moeenfard2015] | [Urgert1997]: retained by paper filters; [Rendon2017]: 87.5 % stays in grounds, 12.4 % in the paper, 0.15 % reaches the brew |
| Carbon dioxide | bloom, crema | [SCA-fresh] | [SCA-fresh]: more crema, stronger bloom in fresh coffee; [IllyNav2011]: espresso foam |
| **Roasted** | | | |
| 2-Furfurylthiol | roasty, coffee-like | [Czerny1999]; [HofSch2002]; [Sanz2002] | [Holscher1992]: "roasty, weak coffee-like" |
| Methanethiol | sulfurous; fresh-roast marker | [Holscher1992] (falls to ≈30 % after 8 days); [HofSch2002]; [Marin2008] | [Holscher1992]: "putrid, sulphurous" |
| Prenylthiol (3-methyl-2-butene-1-thiol) | skunky, foxy | [Czerny1999]; [HofSch2002]; [Holscher1992] | [Holscher1992]: "foxy, skunky" |
| Methional | cooked potato | [Sanz2002]; [Holscher1992] | [Holscher1992]: "cooked potato" |
| 2-Ethyl-3,5-dimethylpyrazine | earthy, roasty | [Chen2025] (OAV 170); [Blank1991] | [Blank1991]: "earthy, roasty" |
| 2,3-Diethyl-5-methylpyrazine | earthy, roasty | [Blank1991] (higher in Robusta); [Buffo2004] (OAV 95, *via Semmelroch 1995*) | [Blank1991]: "earthy, roasty" |
| Guaiacol | phenolic, smoky, spicy | [Sanz2002]; [Chen2025] (OAV 8–63) | [Blank1991] *(via coffeeresearch.org)*: "phenolic, spicy"; "smoky" is the usual flavourist term |
| **Spices** | | | |
| 4-Vinylguaiacol | clove, spicy | [Blank1992] (one of 13 key odorants); [Sanz2002]; [Chen2025] | [Blank1991]: "spicy"; [Flavornet]: "clove, curry" |
| 4-Ethylguaiacol | spicy, smoky; more in Robusta | [Blank1991]; [Buffo2004] (OAV 32); [Sanz2002] | [Blank1991]: "spicy", significantly higher in Robusta; [Chen2025]: "smokey" |
| **Nutty / Cocoa** | | | |
| 2,5-Dimethylpyrazine | nutty, roasted peanut | [Obando2024]; [Chen2025] | [TGSC]: "nutty, peanut… cocoa" (minor contributor in coffee) |
| 3-Methylbutanal | malty | [Blank1991]; [Buffo2004] *(Czerny 1999 omission tests)* | [Blank1991]: "malty" |
| 2-Methylbutanal | malty, cocoa-like | [Buffo2004] *(Czerny 1999 omission tests)* | [Frauendorfer2006]: "malty"; [TGSC]: "cocoa" |
| **Sweet** | | | |
| Diacetyl | buttery | [Blank1991]; [Obando2024] | [Blank1991]: "buttery" |
| 2,3-Pentanedione | buttery, creamy | [Blank1991]; [Obando2024] | [Blank1991]: "buttery"; [Chen2025]: "buttery and creamy" |
| Furaneol (HDMF) | caramel-like | [Blank1991]; [Blank1992]; [Sanz2002]; [Buffo2004] (OAV ≈11,000) | [Blank1991]: "caramel-like" |
| Sotolon | seasoning, maple syrup | [Blank1992] (one of 13 key odorants); [Blank1991] | [Blank1991]: "seasoning-like"; maple at low concentration (Blank & Schieberle 1993, via Wikipedia) |
| Abhexon | seasoning, caramel | [Blank1991]; [Sanz2002] | [Blank1991]: "seasoning-like"; caramel/maple (supplier data, weaker) |
| Maltol | caramel, sweet | [Obando2024]; [Chen2025]; [FoodChem2016] (marker of "baked" roast defect) | [Chen2025]: "caramel"; [TGSC]: "caramellic" |
| Vanillin | vanilla | [Blank1992]; [Buffo2004] (OAV 48); [Sanz2002] | [Blank1991]: "sweet (vanilla)" |
| Phenylacetaldehyde | honey, floral | [Blank1991]; [Chen2025] | [Blank1991]: "honey-like"; [Chen2025]: "floral, honey, cocoa" |

## Changes after review

| Change | Reason |
|---|---|
| Removed **geraniol** | No evidence found that it is a meaningful coffee odorant; the rose note is covered by β-damascenone. |
| Removed **ethyl acetate** and **isoamyl acetate** | Only weak or indirect evidence of occurrence in coffee (a postharvest review; a labelled-transfer fermentation trial). |
| Removed **(Z)-3-hexenal** | Not found in coffee odorant studies; hexanal covers the green note. |
| Removed **kahweol** | No separate sensory role; duplicates cafestol. |
| Removed **dimethyl trisulfide** | Not found in coffee odorant studies. Replaced by **methional** (cooked potato), a well-documented coffee odorant. |
| Removed **2-acetyl-1-pyrroline** | Its popcorn note is real, but no study of real coffee (as opposed to cereal coffee substitutes) was found. |
| Removed **eugenol** | Not found in coffee odorant studies; 4-vinylguaiacol carries the clove/spicy note. |
| Acetaldehyde: "fresh, green apple" → "pungent, fruity" | "Green apple" is the beer/wine convention; the coffee GC-O descriptor is "pungent, fruity" [Holscher1992]. |
| Organic acids: "lemony", "green apple", "yoghurt-like" → plain sourness descriptors | Acids are non-volatile, so they have no fruit aroma; experts can't identify individual acids at coffee levels [Rune2023]. |
| Phosphoric acid: "sparkling, crisp" → "minor; experts can't detect it" | Small share of acidity; not detected even at twice its natural level [Engelhardt1985; Rune2023]. |
| Chlorogenic acid moved from "Bitter" to astringency | It is not itself bitter; its roast-formed lactones are [ACS2007; Frank2006]. |
| CGA lactones: "harsh, lingering" → "coffee-typical bitter" | The harsh bitterness belongs to their dark-roast breakdown products [Blumberg2010]. |
| N-Methylpyridinium: "roasty" → "odourless dark-roast marker" | It is a non-volatile cation with no established taste or odour role [Lang2013]. |
| "Body" category renamed "Oil & Gas" | No evidence that cafestol contributes to perceived body; CO₂'s effect on taste is unstudied [IllyNav2011]. |
| Methanethiol: "fades with freshness" → "fresh-roast marker" | It is lost as coffee stales [Holscher1992]. |
| (E)-2-Nonenal moved from "Staling" to a lipid-oxidation taint | Its staling role is established in beer, not coffee [Scheidig2007]. |
| 2-Methoxy-3,5-dimethylpyrazine moved from "Microbial defect" to Green | In coffee it is documented as a normal raw-bean odorant [Scheidig2007]. |
| Other descriptor fixes | 2,3-diethyl-5-methylpyrazine (nutty → earthy, roasty), 2-methylbutanal, 3-methylbutanal, 2,3-pentanedione, maltol, furaneol, guaiacol, 2-furfurylthiol, trigonelline, caffeine, quinic acid, esters, 4-ethylguaiacol ("Robusta marker" → "more in Robusta"). |

## References

- **[ACS2007]** American Chemical Society press release on T. Hofmann's coffee-bitterness work, 2007. ScienceDaily. https://www.sciencedaily.com/releases/2007/08/070821143629.htm
- **[Akiyama2003]** Akiyama M. et al. Analysis of volatile compounds released during the grinding of roasted coffee beans using solid-phase microextraction. *J. Agric. Food Chem.* 2003, 51, 1961–1969. https://doi.org/10.1021/jf020724p
- **[Blank1991]** Blank I., Sen A., Grosch W. Aroma impact compounds of Arabica and Robusta coffee: qualitative and quantitative investigations. *14th ASIC Colloquium*, San Francisco, 1991, 117–129. https://www.researchgate.net/publication/235694927
- **[Blank1992]** Blank I., Sen A., Grosch W. Potent odorants of the roasted powder and brew of Arabica coffee. *Z. Lebensm. Unters. Forsch.* 1992, 195, 239–245. https://doi.org/10.1007/BF01202802
- **[Blumberg2010]** Blumberg S., Frank O., Hofmann T. Quantitative studies on the influence of the bean roasting parameters and hot water percolation on the concentrations of bitter compounds in coffee brew. *J. Agric. Food Chem.* 2010, 58, 3720–3728. https://doi.org/10.1021/jf9044606
- **[Budryn2011]** Budryn G., Nebesny E., Kula J., Majda T., Krysiak W. HS-SPME/GC/MS profiles of convectively and microwave roasted Ivory Coast Robusta coffee brews. *Czech J. Food Sci.* 2011, 29, 151–160. https://doi.org/10.17221/69/2009-CJFS
- **[Buffo2004]** Buffo R.A., Cardelli-Freire C. Coffee flavour: an overview. *Flavour Fragr. J.* 2004, 19, 99–104. https://doi.org/10.1002/ffj.1325 (reproduces OAVs from Semmelroch et al. 1995 and the omission tests of Czerny et al. 1999)
- **[Cain2021]** Cain C.N. et al. Analytical determination of the severity of potato taste defect in roasted East African arabica coffee. *J. Agric. Food Chem.* 2021, 69. https://doi.org/10.1021/acs.jafc.1c00605
- **[Cantergiani2001]** Cantergiani E. et al. Characterisation of the aroma of green Mexican coffee and identification of mouldy/earthy defect. *Eur. Food Res. Technol.* 2001, 212, 648–657. https://doi.org/10.1007/s002170100305
- **[Chen2025]** Chen X., Wu P., Wang S., Sun J., Chen H. Identification of key aroma-active compounds in commercial coffee using GC-O/AEDA and OAV analysis. *Foods* 2025, 14, 3192. https://doi.org/10.3390/foods14183192
- **[Chin2011]** Chin S.T., Eyres G.T., Marriott P.J. *J. Chromatogr. A* 2011, 1218, 7487–7498. https://doi.org/10.1016/j.chroma.2011.06.039
- **[Czerny1999]** Czerny M., Mayer F., Grosch W. Sensory study on the character impact odorants of roasted Arabica coffee. *J. Agric. Food Chem.* 1999, 47, 695–699. https://doi.org/10.1021/jf980759i
- **[Czerny2000]** Czerny M., Grosch W. Potent odorants of raw Arabica coffee. *J. Agric. Food Chem.* 2000, 48, 868–872. https://doi.org/10.1021/jf990609n
- **[CzernyButtner2009]** Czerny M., Büttner A. Odor-active compounds in cardboard. *J. Agric. Food Chem.* 2009, 57, 9979–9984. https://doi.org/10.1021/jf901435n
- **[Engelhardt1985]** Engelhardt U.H., Maier H.G. Säuren des Kaffees XI (Acids in coffee XI: the proportion of individual acids in the total titratable acid). *Z. Lebensm. Unters. Forsch.* 1985, 181, 20–23. https://doi.org/10.1007/BF01124801
- **[Flavornet]** Acree T., Arn H. Flavornet. https://flavornet.org (β-damascenone, ethyl 3-methylbutanoate, 4-vinylguaiacol pages)
- **[FooDB]** FooDB, geosmin (FDB015352). https://www.foodb.ca/compounds/FDB015352
- **[FoodChem2016]** Yang, Liu C., Liu X., Degn, Münchow, Fisk. Determination of volatile marker compounds of common coffee roast defects. *Food Chem.* 2016, 211, 206–214. https://doi.org/10.1016/j.foodchem.2016.04.124
- **[Frank2006]** Frank O., Zehentbauer G., Hofmann T. Bioresponse-guided decomposition of roast coffee beverage and identification of key bitter taste compounds. *Eur. Food Res. Technol.* 2006, 222, 492–508. https://doi.org/10.1007/s00217-005-0143-6
- **[Frauendorfer2006]** Frauendorfer F., Schieberle P. Identification of the key aroma compounds in cocoa powder based on molecular sensory correlations. *J. Agric. Food Chem.* 2006, 54, 5521–5529. https://doi.org/10.1021/jf060728k
- **[Hofmann2001]** Hofmann T., Czerny M., Calligaris S., Schieberle P. Model studies on the influence of coffee melanoidins on flavor volatiles of coffee beverages. *J. Agric. Food Chem.* 2001, 49, 2382–2386. https://doi.org/10.1021/jf0012042
- **[HofSch2002]** Hofmann T., Schieberle P. Chemical interactions between odor-active thiols and melanoidins involved in the aroma staling of coffee beverages. *J. Agric. Food Chem.* 2002, 50, 319–326 (online 2001). https://doi.org/10.1021/jf010823n
- **[Holscher1992]** Hölscher W., Steinhart H. Investigation of roasted coffee freshness with an improved headspace technique. *Z. Lebensm. Unters. Forsch.* 1992, 195, 33–38. https://doi.org/10.1007/BF01197836 (PDF: https://pages.uoregon.edu/chendon/coffee_literature/old_literature/1992%20Z.%20Lebensm.%20Unters.%20Forsch.,%20Headspace%20freshness%20of%20roasted%20coffee.pdf)
- **[IllyNav2011]** Illy E., Navarini L. Neglected food bubbles: the espresso coffee foam. *Food Biophys.* 2011. https://pubmed.ncbi.nlm.nih.gov/21892345/
- **[Lang2013]** Lang R. et al. Quantitative studies on roast kinetics for bioactives in coffee. *J. Agric. Food Chem.* 2013, 61, 12123–12128. https://doi.org/10.1021/jf403846g
- **[LangHof2009]** Lang R., Hofmann T. On the generation of bioactive trigonelline degradation products upon coffee roasting. *Czech J. Food Sci.* 2009, 27 (special issue). https://doi.org/10.17221/629-CJFS
- **[Marie2024]** Marie L. et al. Combined sensory, volatilome and transcriptome analyses identify a limonene terpene synthase as a major contributor to the characteristic aroma of a *Coffea arabica* L. specialty coffee. *BMC Plant Biol.* 2024, 24. https://doi.org/10.1186/s12870-024-04890-3
- **[Marin2008]** Marin K., Požrl T., Zlatić E., Plestenjak A. A new aroma index to determine the aroma quality of roasted and ground coffee during storage. *Food Technol. Biotechnol.* 2008, 46, 442–447. https://hrcak.srce.hr/en/30422
- **[Moeenfard2015]** Moeenfard M. et al. Diterpenes in espresso coffee: impact of preparation parameters. *Eur. Food Res. Technol.* 2015, 240, 763–773. https://doi.org/10.1007/s00217-014-2381-y
- **[Obando2024]** Obando A.M., Figueroa J.G. Effect of roasting level on the development of key aroma-active compounds in coffee. *Molecules* 2024, 29, 4723. https://doi.org/10.3390/molecules29194723
- **[Rendon2017]** Rendón M.Y., dos Santos Scholz M.B., Bragagnolo N. Is cafestol retained on the paper filter in the preparation of filter coffee? *Food Res. Int.* 2017, 100, 798–803. https://doi.org/10.1016/j.foodres.2017.08.013
- **[Rune2023]** Rune C.J.B., Giacalone D., Steen I., Duelund L., Münchow M., Clausen M.P. Acids in brewed coffees: chemical composition and sensory threshold. *Curr. Res. Food Sci.* 2023. https://doi.org/10.1016/j.crfs.2023.100485
- **[Sanz2002]** Sanz C., Czerny M., Cid C., Schieberle P. Comparison of potent odorants in a filtered coffee brew and in an instant coffee beverage by aroma extract dilution analysis (AEDA). *Eur. Food Res. Technol.* 2002, 214, 299–302. https://doi.org/10.1007/s00217-001-0459-9
- **[SCA-fresh]** Specialty Coffee Association. Coffee Decoded: What is "fresh" coffee? https://sca.coffee/sca-news/coffee-decoded-9-fresh-coffee
- **[Scheidig2007]** Scheidig C., Czerny M., Schieberle P. Changes in key odorants of raw coffee beans during storage under defined conditions. *J. Agric. Food Chem.* 2007, 55, 5768–5775. https://doi.org/10.1021/jf070488o
- **[Seninde2020]** Seninde D.R., Chambers E. Coffee flavor: a review. *Beverages* 2020, 6, 44. https://doi.org/10.3390/beverages6030044
- **[Simpson2004]** Simpson R.F., Capone D.L., Sefton M.A. Isolation and identification of 2-methoxy-3,5-dimethylpyrazine, a potent musty compound from wine corks. *J. Agric. Food Chem.* 2004, 52, 5425–5430. https://doi.org/10.1021/jf049484z
- **[Spadone1990]** Spadone J.-C., Takeoka G., Liardon R. Analytical investigation of Rio off-flavor in green coffee. *J. Agric. Food Chem.* 1990, 38, 226–233. https://doi.org/10.1021/jf00091a050
- **[TGSC]** The Good Scents Company, odour and flavour data. https://www.thegoodscentscompany.com (pages for 3-mercapto-3-methylbutyl formate, 2,5-dimethylpyrazine, 2-methylbutanal, maltol)
- **[Urgert1997]** Urgert R., Katan M.B. The cholesterol-raising factor from coffee beans. *Annu. Rev. Nutr.* 1997, 17, 305–324. https://doi.org/10.1146/annurev.nutr.17.1.305
- **[Vezzulli2023]** Vezzulli F., Lambri M., Bertuzzi T. Volatile compounds in green and roasted Arabica specialty coffee. *Foods* 2023, 12, 489. https://doi.org/10.3390/foods12030489
- **[WCR2017]** World Coffee Research Sensory Lexicon, 2nd edition, 2017. https://worldcoffeeresearch.org/download/5806d8c7-cd7c-4882-a81a-2850bd6fbd36
- **[WCR-PTD]** World Coffee Research. Potato taste defect. https://worldcoffeeresearch.org/es/resources/potato-taste-defect
- **[Yeager2021]** Yeager S.E., Batali M.E., Guinard J.-X., Ristenpart W.D. Acids in coffee: a review of sensory measurements and meta-analysis of chemical composition. *Crit. Rev. Food Sci. Nutr.* 2021 (online). https://doi.org/10.1080/10408398.2021.1957767
