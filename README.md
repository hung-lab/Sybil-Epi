# Sybil-Epi
A model for lung cancer risk prediction that combines deep learning features from the [Sybil model](https://github.com/reginabarzilaygroup/Sybil/) with clinical and epidemiological factors.

## How to use it

First, you need to process a low-dose CT image of the subject to be analyzed using the [Sybil model](https://github.com/reginabarzilaygroup/Sybil/). Then, record the resulting 6-year lung cancer risk prediction value and use it as input in the program below.

To run Sybil-Epi, download the sybil_epi.py file from this repository and run it as indicated below:

`python sybil_epi.py --age 66.08055556 --bmi 29.64582054 --copd 0 --education 6 --ethnicity White --family_history 0 --personal_history 1 --smoking_duration 43 --smoking_intensity 0.8 --smoking_quit 0 --smoking_status 0 --risk_sybil_6_year 0.034103291`

The subject used in the example above presents the following factor values:

|Factor|Value|
|-|-|
|Age (years)|66.08055556|
|BMI (kg/m<sup>2</sup>)|29.64582054|
|COPD (0-yes, 1-no)|0|
|Education level|6|
|Ethnicity|White|
|Family lung cancer history (0-yes, 1-no)|0|
|Personal cancer history (0-yes, 1-no)|1|
|Smoking duration (years)|43|
|Smoking intensity (cigarrettes per day)|0.8|
|Smoking quit time (years)|0|
|Smoking status (0-former, 1-current)|0|
|6-year Risk Sybil|0.034103291|

Further details on how to use sybil_epi.py can be obtained with the command
`python sybil_epi.py -h`
