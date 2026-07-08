import pandas as pd
import random

mbti_types = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

data = []

def generate_value(is_positive_trait):
    # High values for positive trait, low for opposite
    if is_positive_trait:
        return random.choice([4, 5, 4, 5, 3])
    else:
        return random.choice([1, 2, 1, 2, 3])

for _ in range(1000):
    mbti = random.choice(mbti_types)
    row = []

    # Q1–Q5 → E/I
    for _ in range(5):
        row.append(generate_value(mbti[0] == "E"))

    # Q6–Q10 → S/N
    for _ in range(5):
        row.append(generate_value(mbti[1] == "S"))

    # Q11–Q15 → T/F
    for _ in range(5):
        row.append(generate_value(mbti[2] == "T"))

    # Q16–Q20 → J/P
    for _ in range(5):
        row.append(generate_value(mbti[3] == "J"))

    # Labels
    row.append(mbti[0])  # EI
    row.append(mbti[1])  # SN
    row.append(mbti[2])  # TF
    row.append(mbti[3])  # JP

    data.append(row)

columns = [f"Q{i}" for i in range(1, 21)] + ["EI", "SN", "TF", "JP"]

df = pd.DataFrame(data, columns=columns)
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("dataset_1000_fixed.csv", index=False)

print("dataset_1000_fixed.csv created successfully!")