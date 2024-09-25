# Sybil-Epi
An improved model for lung cancer risk prediction that combines deep learning features from the Sybil model with clinical and epidemiological factors.

## Coefficients for each factor included in the Sybil-Epi model
|Factor|Model 1|Model 2|Model 3|Model 4|Model 5| 
|-|-|-|-|-|-|
|Intercept|-20.79038191000|-0.24621993000|-7.40740562000|-14.98083140000|0.01625732000|
|6-year Risk Sybil|7.02617157000|6.96079105000|6.92597482000|7.24776249000|7.47072426000|
|Age|0.21847996200|-0.09406773960|0.01853234780|0.13195954400|-0.10165534300|
|BMI|-0.01732394310|-0.01994318480|-0.02247213930|-0.01906357390|-0.02823116440|
|COPD|0.18149021100|0.23223599200|0.18960467600|0.37200519100|0.47694046700|
|Education level|-0.08116632920|-0.08115994020|-0.05201051400|-0.06836542110|-0.05069236120|
|Ethnicity - White|Reference|Reference|Reference|Reference|Reference|
|Ethnicity - Black|0.23084095400|0.15766851600|0.23894223900|0.22021814400|0.45120666500|
|Ethnicity - Asian|0.17212853500|0.43564514700|0.31138165200|-0.05802796240|0.02304009340|
|Ethnicity - Others|0.36442735200|0.30574606700|0.59204369500|0.54687080400|-0.03478278100|
|Family lung cancer history|0.09914501700|0.08925881800|-0.00728941902|0.05297350630|0.02851307510|
|Personal cancer history|0.20821163600|0.24459386000|0.17568551900|0.17857532900|0.07705976050|
|Smoking duration|0.36915862700|-0.04855800000|0.13150375700|0.30506137200|-0.16755627900|
|Smoking intensity|0.01823174660|0.01969007140|0.01734555020|0.01915918910|0.01929939040|
|Smoking quit time|0.00262488699|0.01330713690|0.00645552283|0.00959059658|0.00837984637|
|Smoking status|0.03382896010|0.14971355100|0.11961590300|0.17588838900|0.14322364400|
|Age x Smoking duration|-0.00458450762|0.00171930035|-0.00103727472|-0.00367140897|0.00381010544|

## Isotonic function for each model

### Model 1
|Range|Score| 
|-|-|
|(-inf, -5.54535145507885)|0.0|
|[-5.54535145507885, -5.54443742079984)|0.0|
|[-5.54443742079984, -5.31175599485575)|0.00157480314960629|
|[-5.31175599485575, -5.31143200626821)|0.00157480314960629|
|[-5.31143200626821, -5.08199266314459)|0.00488997555012224|
|[-5.08199266314459, -5.0816819409446)|0.00488997555012224|
|[-5.0816819409446, -5.03867510600285)|0.0104166666666666|
|[-5.03867510600285, -5.03822641268466)|0.0104166666666666|
|[-5.03822641268466, -4.9376550049408)|0.0143540669856459|
|[-4.9376550049408, -4.93695653610866)|0.0143540669856459|
|[-4.93695653610866, -4.76914044854747)|0.0175849941383352|
|[-4.76914044854747, -4.76895524803483)|0.0175849941383352|
|[-4.76895524803483, -4.52447036706167)|0.0215404699738903|
|[-4.52447036706167, -4.52429109634284)|0.0215404699738903|
|[-4.52429109634284, -4.1851070855342)|0.0225340136054421|
|[-4.1851070855342, -4.18507857823729)|0.0225340136054421|
|[-4.18507857823729, -4.13856683549135)|0.0234604105571847|
|[-4.13856683549135, -4.13834600108628)|0.0234604105571847|
|[-4.13834600108628, -4.12227312343759)|0.0241935483870967|
|[-4.12227312343759, -4.1222142981056)|0.0241935483870967|
|[-4.1222142981056, -4.05303979153328)|0.0417536534446764|
|[-4.05303979153328, -4.05303564896005)|0.0417536534446764|
|[-4.05303564896005, -3.86110437983613)|0.0432653061224489|
|[-3.86110437983613, -3.86110032761937)|0.0432653061224489|
|[-3.86110032761937, -3.80980785285466)|0.050314465408805|
|[-3.80980785285466, -3.80976013309103)|0.050314465408805|
|[-3.80976013309103, -3.76522223698408)|0.0519480519480519|
|[-3.76522223698408, -3.76469486998651)|0.0519480519480519|
|[-3.76469486998651, -3.63506267680873)|0.0521885521885521|
|[-3.63506267680873, -3.63504437844557)|0.0521885521885521|
|[-3.63504437844557, -3.58218684183874)|0.0588235294117647|
|[-3.58218684183874, -3.58212663522492)|0.0588235294117647|
|[-3.58212663522492, -3.41422959054526)|0.062700964630225|
|[-3.41422959054526, -3.41407934535584)|0.062700964630225|
|[-3.41407934535584, -3.39395767263892)|0.0862068965517241|
|[-3.39395767263892, -3.3936194461336)|0.0862068965517241|
|[-3.3936194461336, -3.35075959553484)|0.0983606557377049|
|[-3.35075959553484, -3.35049833366132)|0.0983606557377049|
|[-3.35049833366132, -3.32526202667457)|0.126984126984126|
|[-3.32526202667457, -3.32425346311377)|0.126984126984126|
|[-3.32425346311377, -3.16743242146143)|0.132832080200501|
|[-3.16743242146143, -3.16648078040121)|0.132832080200501|
|[-3.16648078040121, -3.11974481801039)|0.158730158730158|
|[-3.11974481801039, -3.11949547782089)|0.158730158730158|
|[-3.11949547782089, -2.88716205883827)|0.187943262411347|
|[-2.88716205883827, -2.88679264910134)|0.187943262411347|
|[-2.88679264910134, -2.28351814304314)|0.192737430167597|
|[-2.28351814304314, -2.28341771334039)|0.192737430167597|
|[-2.28341771334039, -2.25075681964111)|0.222222222222222|
|[-2.25075681964111, -2.24722264484806)|0.222222222222222|
|[-2.24722264484806, -1.81503763638207)|0.3125|
|[-1.81503763638207, -1.80981471342024)|0.3125|
|[-1.80981471342024, -1.56220188001589)|0.510204081632653|
|[-1.56220188001589, -1.56203367410988)|0.510204081632653|
|[-1.56203367410988, -0.883730771581255)|0.528089887640449|
|[-0.883730771581255, -0.881204139655352)|0.528089887640449|
|[-0.881204139655352, -0.747571012833969)|0.588235294117647|
|[-0.747571012833969, -0.747516347831869)|0.588235294117647|
|[-0.747516347831869, 0.26902159779528)|0.60204081632653|
|[0.26902159779528, 0.347617076263695)|0.60204081632653|
|[0.347617076263695, 0.350744122092173)|0.666666666666666|
|[0.350744122092173, 0.364813256341062)|0.666666666666666|
|[0.364813256341062, 1.32971502224201)|0.790697674418604|
|[1.32971502224201, 1.33205349683115)|0.790697674418604|
|[1.33205349683115, 2.25257322093028)|0.8|
|[2.25257322093028, 2.28793489335508)|0.8|
|[2.28793489335508, +inf)|1.0|
