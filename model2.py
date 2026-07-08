import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Load dataset
df = pd.read_csv("dataset_1000_fixed.csv")

# 2. Features (Q1–Q20)
X = df[[f"Q{i}" for i in range(1, 21)]]

# 3. Labels
y_EI = df['EI']
y_SN = df['SN']
y_TF = df['TF']
y_JP = df['JP']

# 4. Train-test split (same split for all)
X_train, X_test, y_EI_train, y_EI_test = train_test_split(X, y_EI, test_size=0.2, random_state=42)
_, _, y_SN_train, y_SN_test = train_test_split(X, y_SN, test_size=0.2, random_state=42)
_, _, y_TF_train, y_TF_test = train_test_split(X, y_TF, test_size=0.2, random_state=42)
_, _, y_JP_train, y_JP_test = train_test_split(X, y_JP, test_size=0.2, random_state=42)

# 5. Create models
model_EI = RandomForestClassifier(n_estimators=100, random_state=42)
model_SN = RandomForestClassifier(n_estimators=100, random_state=42)
model_TF = RandomForestClassifier(n_estimators=100, random_state=42)
model_JP = RandomForestClassifier(n_estimators=100, random_state=42)

# 6. Train models
model_EI.fit(X_train, y_EI_train)
model_SN.fit(X_train, y_SN_train)
model_TF.fit(X_train, y_TF_train)
model_JP.fit(X_train, y_JP_train)

# 7. Evaluate accuracy
pred_EI = model_EI.predict(X_test)
pred_SN = model_SN.predict(X_test)
pred_TF = model_TF.predict(X_test)
pred_JP = model_JP.predict(X_test)

acc_EI = accuracy_score(y_EI_test, pred_EI)
acc_SN = accuracy_score(y_SN_test, pred_SN)
acc_TF = accuracy_score(y_TF_test, pred_TF)
acc_JP = accuracy_score(y_JP_test, pred_JP)

print("Accuracy:")
print("EI:", round(acc_EI * 100, 2), "%")
print("SN:", round(acc_SN * 100, 2), "%")
print("TF:", round(acc_TF * 100, 2), "%")
print("JP:", round(acc_JP * 100, 2), "%")

# 8. Function to predict MBTI from user input
def predict_mbti(answers):
    import pandas as pd
    
    input_df = pd.DataFrame([answers], columns=[f"Q{i}" for i in range(1, 21)])

    ei = model_EI.predict(input_df)[0]
    sn = model_SN.predict(input_df)[0]
    tf = model_TF.predict(input_df)[0]
    jp = model_JP.predict(input_df)[0]

    return ei + sn + tf + jp


# 9. Test with sample input (optional)
if __name__ == "__main__":
    sample = [5]*20  # example: all high answers
    result = predict_mbti(sample)
    print("Sample Prediction:", result)