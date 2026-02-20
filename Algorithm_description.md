# Sybil-Epi
A model for lung cancer risk prediction that combines deep learning features from the [Sybil model](https://github.com/reginabarzilaygroup/Sybil/) with clinical and epidemiological factors.

The Sybil-Epi model was calibrated using [Platt's method/sigmoid](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html) with 5-fold cross validation (default setting), from the scikit-learn package.
