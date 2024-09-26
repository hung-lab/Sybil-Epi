# Sybil-Epi
A model for lung cancer risk prediction that combines deep learning features from the [Sybil model](https://github.com/reginabarzilaygroup/Sybil/) with clinical and epidemiological factors.

The Sybil-Epi model was calibrated using [isotonic regression](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#) with 5-fold cross validation (default setting), from the scikit-learn package.

## Example on how to use it

Given a subject with the factors below<sup>1</sup>:

|Factor|Value|
|-|-|
|6-year Risk Sybil<sup>2</sup>|0.030889602|
|Age (years)|63|
|BMI (kg/m<sup>2</sup>)|28.88|
|COPD (0-yes, 1-no)|0|
|Education level<sup>3</sup>|6|
|Ethnicity - White (0-yes, 1-no)|1|
|Ethnicity - Black (0-yes, 1-no)|0|
|Ethnicity - Asian (0-yes, 1-no)|0|
|Ethnicity - Others (0-yes, 1-no)|0|
|Family lung cancer history (0-yes, 1-no)|0|
|Personal cancer history (0-yes, 1-no)|1|
|Smoking duration (years)|43|
|Smoking intensity (cigarrettes per day)|1.0|
|Smoking quit time (years)|40|
|Smoking status (0-Former, 1-Current)|0|
|Age x Smoking duration (years<sup>2</sup>)|2520.11|

<sup>1</sup>All factors were measured using the units indicated in the [PLCO<sub>m2012</sub> model](https://www.nejm.org/doi/full/10.1056/NEJMoa1211776).

<sup>2</sup>The 6-year Risk Sybil value can be calculated from a single low-dose CT image, analyzed using the [Sybil model](https://github.com/reginabarzilaygroup/Sybil/).

<sup>3</sup>Education was measured in six ordinal levels: less than high-school graduate (level 1), high-school graduate (level 2), some training after high school (level 3), some college (level 4), college graduate (level 5), and postgraduate or professional degree (level 6).

## 1. Coefficients for each factor included in the Sybil-Epi model
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

## 2. Isotonic function for each model

### 2.1. Model 1
|Range|Score| 
|-|-|
|[-6.83084097765182, -5.54535145507885]|0.0|
|[-5.54443742079984, -5.31175599485575]|0.00157480314960629|
|[-5.31143200626821, -5.08199266314459]|0.00488997555012224|
|[-5.0816819409446, -5.03867510600285]|0.0104166666666666|
|[-5.03822641268466, -4.9376550049408]|0.0143540669856459|
|[-4.93695653610866, -4.76914044854747]|0.0175849941383352|
|[-4.76895524803483, -4.52447036706167]|0.0215404699738903|
|[-4.52429109634284, -4.1851070855342]|0.0225340136054421|
|[-4.18507857823729, -4.13856683549135]|0.0234604105571847|
|[-4.13834600108628, -4.12227312343759]|0.0241935483870967|
|[-4.1222142981056, -4.05303979153328]|0.0417536534446764|
|[-4.05303564896005, -3.86110437983613]|0.0432653061224489|
|[-3.86110032761937, -3.80980785285466]|0.050314465408805|
|[-3.80976013309103, -3.76522223698408]|0.0519480519480519|
|[-3.76469486998651, -3.63506267680873]|0.0521885521885521|
|[-3.63504437844557, -3.58218684183874]|0.0588235294117647|
|[-3.58212663522492, -3.41422959054526]|0.062700964630225|
|[-3.41407934535584, -3.39395767263892]|0.0862068965517241|
|[-3.3936194461336, -3.35075959553484]|0.0983606557377049|
|[-3.35049833366132, -3.32526202667457]|0.126984126984126|
|[-3.32425346311377, -3.16743242146143]|0.132832080200501|
|[-3.16648078040121, -3.11974481801039]|0.158730158730158|
|[-3.11949547782089, -2.88716205883827]|0.187943262411347|
|[-2.88679264910134, -2.28351814304314]|0.192737430167597|
|[-2.28341771334039, -2.25075681964111]|0.222222222222222|
|[-2.24722264484806, -1.81503763638207]|0.3125|
|[-1.80981471342024, -1.56220188001589]|0.510204081632653|
|[-1.56203367410988, -0.883730771581255]|0.528089887640449|
|[-0.881204139655352, -0.747571012833969]|0.588235294117647|
|[-0.747516347831869, 0.26902159779528]|0.60204081632653|
|[0.347617076263695, 0.350744122092173]|0.666666666666666|
|[0.364813256341062, 1.32971502224201]|0.790697674418604|
|[1.33205349683115, 2.25257322093028]|0.8|
|[2.28793489335508, 3.22150837109364]|1.0|

### 2.2. Model 2
|Range|Score| 
|-|-|
|[-5.13976202645897, -4.45855247691666)|0.0|
|[-4.4582698193259, -4.2518450533451)|0.00130378096479791|
|[-4.25157297578535, -4.12103947494856)|0.00404312668463611|
|[-4.12091177902061, -4.02640561549037)|0.0045662100456621|
|[-4.02639931241959, -3.87850590132921)|0.00699300699300699|
|[-3.87836333800783, -3.78265108085928)|0.0122767857142857|
|[-3.78263902318789, -3.66874059942404)|0.0186005314437555|
|[-3.66865649809458, -3.50333686239594)|0.0245398773006134|
|[-3.50322676511143, -3.38260458926028)|0.0252427184466019|
|[-3.38239050905076, -3.36134026536294)|0.0261780104712041|
|[-3.3611225958752, -3.30651259082491)|0.0295983086680761|
|[-3.30631233790642, -3.20914725751849)|0.0464135021097046|
|[-3.20902487646987, -3.11694062505718)|0.0606617647058823|
|[-3.11679462879763, -2.96532175570692)|0.0787096774193548|
|[-2.96511797871301, -2.69559229246829)|0.0954598370197904|
|[-2.69501884194289, -2.62274546546793)|0.124260355029585|
|[-2.6223546843081, -2.48658932345086)|0.129921259842519|
|[-2.48610328068047, -2.30092176611133)|0.151658767772511|
|[-2.30071351946817, -2.24700122492978)|0.166666666666666|
|[-2.24684490923774, -2.01801620372871)|0.2|
|[-2.01495607993973, -1.66317335999902)|0.266272189349112|
|[-1.6569219881803, -1.08676074827303)|0.284360189573459|
|[-1.08249227836323, -1.07366923763311)|0.333333333333333|
|[-1.07010276090708, 0.0705479290336056)|0.503816793893129|
|[0.0738831826353788, 0.401184842679566)|0.558823529411764|
|[0.402345918309606, 0.645414076527883)|0.676470588235294|
|[0.653619752845769, 1.38234013948577)|0.709090909090909|
|[1.38787187448386, 1.48660866194891)|0.75|
|[1.50162544808152, 1.69133780551668)|0.833333333333333|
|[1.70614331310756, 2.0612330181618)|0.923076923076923|
|[2.14202917083523, 3.91208317660163)|1.0|

### 2.3. Model 3
|Range|Score| 
|-|-|
|[-5.40896695555443, -4.44557905591795)|0.0|
|[-4.44556769824729, -4.20796960678975)|0.0050251256281407|
|[-4.20739595368818, -3.91552915782963)|0.00583657587548638|
|[-3.91548039595661, -3.5345198348362)|0.0096698899633211|
|[-3.53431434149028, -3.43490951844732)|0.0177725118483412|
|[-3.43488087385878, -3.42904077520323)|0.0204081632653061|
|[-3.4288999459988, -3.41768951227193)|0.0212765957446808|
|[-3.41754960133783, -3.39211171288659)|0.0241545893719806|
|[-3.39205300926651, -3.32995536982051)|0.0264227642276422|
|[-3.32990172496423, -3.24685531071719)|0.0287277701778385|
|[-3.24671206819021, -3.11901522252616)|0.0375275938189845|
|[-3.11886226305581, -2.99974728760598)|0.0395061728395061|
|[-2.99956474429094, -2.91765833557168)|0.0506607929515418|
|[-2.91750760894448, -2.90054878707901)|0.0666666666666666|
|[-2.90028915863532, -2.6475189963683)|0.0817120622568093|
|[-2.64741434406712, -2.62150132519831)|0.0952380952380952|
|[-2.6209657404627, -2.59858231770701)|0.123076923076923|
|[-2.59812553384104, -2.4554499391278)|0.126262626262626|
|[-2.45529021102402, -2.39397293199902)|0.130081300813008|
|[-2.39363220142586, -1.87769220955232)|0.134304207119741|
|[-1.87523366083048, -1.84412706174444)|0.17391304347826|
|[-1.84244882776309, -1.59368802685856)|0.211678832116788|
|[-1.59106147350401, -1.56382787161001)|0.222222222222222|
|[-1.55982641375981, -1.4549350688779)|0.24074074074074|
|[-1.44902791926516, -1.40284906648665)|0.25|
|[-1.40284160717211, -1.31017627785731)|0.263157894736842|
|[-1.30232455720342, -1.19292612431877)|0.333333333333333|
|[-1.18992323507933, -1.17861833654162)|0.428571428571428|
|[-1.17606128036306, -0.413588502397382)|0.439759036144578|
|[-0.402302355080826, -0.278037063043519)|0.5|
|[-0.252188292713815, 0.28318091010164)|0.52|
|[0.284280188256867, 0.828005605867875)|0.625|
|[0.860334523461037, 0.996858651407914)|0.692307692307692|
|[1.00118109607741, 1.05344457993507)|0.777777777777777|
|[1.0754991844332, 1.66608973697844)|0.878048780487804|
|[1.76795244660686, 2.91795097929127)|0.923076923076923|
|[2.94294776493842, 3.53725043203523)|1.0|

### 2.4. Model 4
|Range|Score| 
|-|-|
|[-5.40297596576861, -4.145046360106)|0.0|
|[-4.14399863519635, -3.96469127014186)|0.00229621125143513|
|[-3.96433456464248, -3.79821097842455)|0.00884955752212389|
|[-3.79779347620638, -3.78276999952974)|0.00952380952380952|
|[-3.7827334089108, -3.71202032064926)|0.0116731517509727|
|[-3.71195047309248, -3.58669159781696)|0.0128055878928987|
|[-3.58668557313358, -3.36313485155923)|0.0199155099577549|
|[-3.36309455610468, -3.34856928840831)|0.0253164556962025|
|[-3.34843950750268, -3.25175025722636)|0.0260416666666666|
|[-3.25173129770055, -3.24480312347089)|0.0476190476190476|
|[-3.244576314838, -2.89445996228474)|0.0486707566462167|
|[-2.89442920543924, -2.43294566623595)|0.0659340659340659|
|[-2.43273732882454, -2.35438840883121)|0.072072072072072|
|[-2.35399267156437, -2.32665326581679)|0.0806451612903225|
|[-2.32644944266306, -2.00073280666356)|0.0842293906810035|
|[-1.99758423146622, -1.87517611131506)|0.102739726027397|
|[-1.87334395146985, -1.47428118372159)|0.131832797427652|
|[-1.47404665717457, -1.2238632031688)|0.158730158730158|
|[-1.22335885613264, -0.94569571043684)|0.288659793814433|
|[-0.943034578788692, -0.170516290240955)|0.343915343915343|
|[-0.159465347170856, 0.00728976386126056)|0.4|
|[0.0145462944545293, 0.0674686168349953)|0.428571428571428|
|[0.0689045131453163, 0.794428399251971)|0.541176470588235|
|[0.794991274019949, 0.860753576674929)|0.545454545454545|
|[0.861091367961949, 1.1731265029034)|0.567567567567567|
|[1.17327917862875, 1.20119869829976)|0.6|
|[1.20950964955107, 1.65124958904896)|0.612244897959183|
|[1.6735448032525, 1.86887592828489)|0.695652173913043|
|[1.88419092062132, 2.65929028108868)|0.741935483870967|
|[2.67248359202892, 2.76664158066157)|0.8|
|[2.78591249999188, 3.84403802653575)|1.0|

### 2.5. Model 5
|Range|Score| 
|-|-|
|[-5.34372288616349, -4.00900324181277)|0.0|
|[-4.008262731788, -3.84370310240735)|0.00617283950617283|
|[-3.84285955438415, -3.49562213214767)|0.00625|
|[-3.49548891109088, -3.19647540660684)|0.00674915635545556|
|[-3.19574010845561, -3.14630729811392)|0.0114285714285714|
|[-3.14629122540069, -2.95688490723843)|0.0181347150259067|
|[-2.95664182722659, -2.31745946097859)|0.0225442834138486|
|[-2.31720653772112, -2.30899511048998)|0.0227272727272727|
|[-2.3089006058332, -1.72097525226115)|0.0361819434872501|
|[-1.72092762782885, -1.68686596037886)|0.0410958904109589|
|[-1.68654701114382, -1.236526434842)|0.0479812755997659|
|[-1.23644413938852, -1.11165732156823)|0.0509915014164305|
|[-1.11144435180836, -1.06707253269346)|0.0787401574803149|
|[-1.0656848188659, -0.899850540104916)|0.0828729281767955|
|[-0.899122118493487, -0.235687989432131)|0.102428722280887|
|[-0.231686727236445, -0.0682802062167959)|0.152|
|[-0.0655954118333348, -0.0517199399968599)|0.153846153846153|
|[-0.0515587696700816, 0.496278828219814)|0.175|
|[0.496381921331663, 0.670826030444628)|0.212765957446808|
|[0.672084076515664, 0.773830880197755)|0.258064516129032|
|[0.786770287499513, 2.20130937840007)|0.391705069124424|
|[2.25738212058063, 2.39931731317832)|0.5|
|[2.42177386174513, 2.68056055833383)|0.527777777777777|
|[2.68100312409866, 2.88201473762726)|0.607142857142857|
|[2.91232541743944, 3.95594449481789)|0.648351648351648|
|[3.97198777284055, 4.33025189595118)|0.75|
|[4.33776582233737, 5.81635295182968)|1.0|
