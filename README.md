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
|Ethnicity - White<td colspan=5 align="center">Reference|
|Ethnicity - Black|0.23084095400|0.15766851600|0.23894223900|0.22021814400|0.45120666500|
|Ethnicity - Asian|0.17212853500|0.43564514700|0.31138165200|-0.05802796240|0.02304009340|
|Ethnicity - Others|0.36442735200|0.30574606700|0.59204369500|0.54687080400|-0.03478278100|
|Family lung cancer history|0.09914501700|0.08925881800|-0.00728941902|0.05297350630|0.02851307510|
|Personal cancer history|0.20821163600|0.24459386000|0.17568551900|0.17857532900|0.07705976050|
|Smoking duration|0.36915862700|-0.04855800000|0.13150375700|0.30506137200|-0.16755627900|
|Smoking intensity|0.01823174660|0.01969007140|0.01734555020|0.01915918910|0.01929939040|
|Smoking quit time|0.00262488699|0.01330713690|0.00645552283|0.00959059658|0.00837984637|
|Smoking status|0.03382896010|0.14971355100|0.11961590300|0.17588838900|0.14322364400|
|Age x Smoking duration|-0.00458450762|0.00171930035|-0.00103727472|-0.00367140897|0.00381010544

