import argparse
import math

# ---------------- Models ---------------- #
MODELS = [
    {
        "age": 0.03845109195667474,
        "bmi": -0.011386701750456835,
        "copd": 0.12928759691449734,
        "education": -0.05193241731109689,
        "black": 0.03305640252878926,
        "asian": 0.09784445590297448,
        "others": 0.13376957580540885,
        "family_history": 0.18966350529865886,
        "personal_history": 0.2668466804813831,
        "duration": 0.055840209011267156,
        "intensity": 0.018940450434839624,
        "quit_time": -0.010966650538136802,
        "smoking_status": 0.03685968494515114,
        "sybil_score": 7.07449145402105,
        "intercept": -8.525320331381652,
    },
    {
        "age": 0.002303841392360946,
        "bmi": -0.01680547871511917,
        "copd": 0.10504996934293911,
        "education": -0.05672137897042658,
        "black": 0.1247465020582522,
        "asian": 0.31053132298073605,
        "others": 0.04422649545382128,
        "family_history": 0.14122733134219667,
        "personal_history": 0.289612052253064,
        "duration": 0.05113662057588997,
        "intensity": 0.021528391225740278,
        "quit_time": -0.005483904343055354,
        "smoking_status": 0.12208435665482772,
        "sybil_score": 7.102737075603964,
        "intercept": -5.891646079306138,
    },
    {
        "age": -0.009365227121743586,
        "bmi": -0.017584596485864287,
        "copd": 0.06135975879299179,
        "education": -0.027680922143483815,
        "black": -0.030752160714064197,
        "asian": 0.35640978236750337,
        "others": 0.29538589515606223,
        "family_history": 0.06287967286709237,
        "personal_history": 0.26082109670718695,
        "duration": 0.05339280084623994,
        "intensity": 0.01826066070397732,
        "quit_time": -0.010139590639593188,
        "smoking_status": 0.1118991589544295,
        "sybil_score": 7.091749157821932,
        "intercept": -5.1618360151227565,
    },
    {
        "age": -0.022391589940648524,
        "bmi": -0.015141864095520916,
        "copd": 0.35096463025956043,
        "education": -0.0441341068232818,
        "black": 0.09996871364164378,
        "asian": 0.18279394664484774,
        "others": 0.2420325052464591,
        "family_history": 0.10343528034088861,
        "personal_history": 0.289568645309188,
        "duration": 0.06454349668304118,
        "intensity": 0.018565514462705858,
        "quit_time": 0.00021373176327254057,
        "smoking_status": 0.1527508244415102,
        "sybil_score": 7.2306869642905,
        "intercept": -4.9212850421682175,
    },
    {
        "age": 0.09548366831836427,
        "bmi": -0.021010852653676554,
        "copd": 0.2784018231289838,
        "education": -0.026466076415995972,
        "black": 0.27518174026893594,
        "asian": -0.009449283066505765,
        "others": -0.4221032657377639,
        "family_history": 0.04613280932621084,
        "personal_history": 0.20970214591522598,
        "duration": 0.06379394350343039,
        "intensity": 0.021895045879674575,
        "quit_time": 0.0025949273006358083,
        "smoking_status": 0.217206886709768,
        "sybil_score": 7.58715314980656,
        "intercept": -12.048447149368291,
    },
]

# ---------------- Calibrators ---------------- #
CALIBRATORS = [
    {"a": -1.2329771175814760, "b": -1.68791783871881180},
    {"a": -1.1765657141893946, "b": -0.67770947946629200},
    {"a": -1.2563689611941198, "b": -0.71005858953171520},
    {"a": -1.0269780235235613, "b":  0.02051234177619454},
    {"a": -0.8470538501992946, "b":  1.75067111594711300},
]

# ---------------- Utility ---------------- #
def calculate_sybil_epi_score(args):
    total_prob = 0.0

    for model, calib in zip(MODELS, CALIBRATORS):
        # Ethnicity coefficient
        ethnicity_coeff = 0
        if args.ethnicity == "Asian":
            ethnicity_coeff = model["asian"]
        elif args.ethnicity == "Black":
            ethnicity_coeff = model["black"]
        elif args.ethnicity == "Others":
            ethnicity_coeff = model["others"]
        # White is reference (0)

        # Linear combination
        z = (
            args.risk_sybil_6_year * model["sybil_score"] +
            args.age * model["age"] +
            args.bmi * model["bmi"] +
            args.copd * model["copd"] +
            args.education * model["education"] +
            ethnicity_coeff +
            args.family_history * model["family_history"] +
            args.personal_history * model["personal_history"] +
            args.smoking_duration * model["duration"] +
            args.smoking_intensity * model["intensity"] +
            args.smoking_quit * model["quit_time"] +
            args.smoking_status * model["smoking_status"] +
            model["intercept"]
        )

        # Apply Platt calibration
        p_calibrated = 1 / (1 + math.exp(calib["a"] * z + calib["b"]))
        total_prob += p_calibrated

    return total_prob / len(MODELS)
    
# ---------------- Argument Parsing ---------------- #
def bounded_float(min_val, max_val):
    def check(val):
        f = float(val)
        if f < min_val or f > max_val:
            raise argparse.ArgumentTypeError(f"Value must be in [{min_val}, {max_val}]")
        return f
    return check

def prepare_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--age", type=bounded_float(0.0, 200.0), required=True)
    parser.add_argument("--bmi", type=bounded_float(0.0, 100.0), required=True)
    parser.add_argument("--copd", type=int, choices=[0,1], required=True)
    parser.add_argument("--education", type=int, choices=[1,2,3,4,5,6], required=True)
    parser.add_argument("--ethnicity", type=str, choices=["Asian","Black","White","Others"], required=True)
    parser.add_argument("--family_history", type=int, choices=[0,1], required=True)
    parser.add_argument("--personal_history", type=int, choices=[0,1], required=True)
    parser.add_argument("--smoking_duration", type=bounded_float(0.0, 200.0), required=True)
    parser.add_argument("--smoking_intensity", type=bounded_float(0.0, 1000.0), required=True)
    parser.add_argument("--smoking_quit", type=bounded_float(0.0, 200.0), required=True)
    parser.add_argument("--smoking_status", type=int, choices=[0,1], required=True)
    parser.add_argument("--risk_sybil_6_year", type=bounded_float(0.0, 1.0), required=True)  
    return parser

# ---------------- Main ---------------- #
if __name__ == "__main__":
    parser = prepare_argument_parser()
    args = parser.parse_args()
    score = calculate_sybil_epi_score(args)
    print(f"Sybil-Epi score = {score}")
    