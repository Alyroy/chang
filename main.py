import excel "E:\data.xlsx", sheet("Sheet1") firstrow
tsset id year
foreach var in SPEI LST GDPgrowth lnGDPpercapita Populationgrowth lnPopulation Lifeexpectancy GovernmentEffectiveness {
gen `var'_1 = L1.`var'
gen `var'_2 = L2.`var'
gen `var'_3 = L3.`var'
}

reg GPI SPEI
reg GPI SPEI_1
reg GPI SPEI_2
reg GPI SPEI_3

reg GPI LST
reg GPI LST_1
reg GPI LST_2
reg GPI LST_3

reg GPI GDPgrowth
reg GPI GDPgrowth_1
reg GPI GDPgrowth_2
reg GPI GDPgrowth_3

reg GPI lnGDPpercapita
reg GPI lnGDPpercapita_1
reg GPI lnGDPpercapita_2
reg GPI lnGDPpercapita_3

reg GPI Populationgrowth
reg GPI Populationgrowth_1
reg GPI Populationgrowth_2
reg GPI Populationgrowth_3

reg GPI lnPopulation
reg GPI lnPopulation_1
reg GPI lnPopulation_2
reg GPI lnPopulation_3

reg GPI Lifeexpectancy
reg GPI Lifeexpectancy_1
reg GPI Lifeexpectancy_2
reg GPI Lifeexpectancy_3

reg GPI GovernmentEffectiveness
reg GPI GovernmentEffectiveness_1
reg GPI GovernmentEffectiveness_2
reg GPI GovernmentEffectiveness_3

*optimisation modelling
stepwise,pe(0.001) lockterm1: reg GPI (i.id) SPEI SPEI_1 SPEI_2 SPEI_3 LST LST_1 LST_2 LST_3 GDPgrowth GDPgrowth_1 GDPgrowth_2 GDPgrowth_3 GDPpercapita GDPpercapita_1 GDPpercapita_2 GDPpercapita_3 Populationgrowth Populationgrowth_1 Populationgrowth_2 Populationgrowth_3 Population Population_1 Population_2 Population_3 Lifeexpectancy Lifeexpectancy_1 Lifeexpectancy_2 Lifeexpectancy_3 GovernmentEffectiveness GovernmentEffectiveness_1 GovernmentEffectiveness_2 GovernmentEffectiveness_3


*fix effects model
xtreg GPI SPEI LST GDPgrowth lnGDPpercapita Populationgrowth lnPopulation Lifeexpectancy GovernmentEffectiveness,fe

*rebostness check
xtreg GPI SPEI LST lnGDPpercapita lnPopulation GovernmentEffectiveness,fe
xtreg GPI SPEI LST lnGDPpercapita Populationgrowth lnPopulation Lifeexpectancy GovernmentEffectiveness,fe
xtreg GPI SPEI LST GDPgrowth lnGDPpercapita lnPopulation Lifeexpectancy GovernmentEffectiveness,fe
xtreg GPI SPEI LST GDPgrowth lnGDPpercapita Populationgrowth lnPopulation GovernmentEffectiveness,fe

xtreg GPI SPEI LSTworldbank GDPgrowth lnGDPpercapita Populationgrowth lnPopulation Lifeexpectancy GovernmentEffectiveness,fe
