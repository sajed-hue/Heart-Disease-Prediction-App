import streamlit as st
import joblib

model = joblib.load("heart_model.pkl")

st.set_page_config(page_title="تطبيق توقع أمراض القلب | Heart Disease Prediction", layout="wide")

st.title(" 💓🩺تطبيق توقع أمراض القلب | Heart Disease Prediction App")
st.write("أدخل معلومات المريض أدناه | Enter patient information:")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("العمر | Age", 1, 100, 27)
    sex = st.radio("الجنس | Sex", ["ذكر | Male", "أنثى | Female"])
    cp = st.selectbox("درجة ألم الصدر (0-3) | Chest Pain Level", [0,1,2,3])
    trestbps = st.number_input("ضغط الدم أثناء الراحة | Resting Blood Pressure", 80, 200)
    chol = st.number_input("الكولسترول | Cholesterol", 100, 400)
    fbs = st.radio("سكر الصيام >120mg/dl | Fasting Blood Sugar", ["لا | No", "نعم | Yes"])
    
with col2:
    restecg = st.selectbox("ECG أثناء الراحة (0-2) | Rest ECG", [0,1,2])
    thalach = st.number_input("أقصى معدل ضربات قلب | Max Heart Rate", 60, 220)
    exang = st.radio("ذبحة صدرية بسبب الرياضة | Exercise Induced Angina", ["لا | No", "نعم | Yes"])
    oldpeak = st.number_input("ST Depression", 0.0, 6.0, 0.0)
    slope = st.selectbox("Slope (0-2)", [0,1,2])
    ca = st.selectbox("عدد الأوعية الدموية الرئيسية (0-3) | Major Vessels", [0,1,2,3])
    thal = st.selectbox("Thal (0-3)", [0,1,2,3])

if st.button("توقع | Predict"):

    sex_val = 1 if sex.startswith("ذكر") else 0
    fbs_val = 1 if fbs.startswith("نعم") else 0
    exang_val = 1 if exang.startswith("نعم") else 0

    data = [[age, sex_val, cp, trestbps, chol, fbs_val, restecg,
             thalach, exang_val, oldpeak, slope, ca, thal]]
    
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]


    if prediction == 1:
        st.markdown(f"<h2 style='color:red'>⚠️ خطر عالي من أمراض القلب | High Risk ({probability:.0%})</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='color:green'>✅ خطر منخفض | Low Risk ({probability:.0%})</h2>", unsafe_allow_html=True)
    
    st.progress(int(probability*100))