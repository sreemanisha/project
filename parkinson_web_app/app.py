import streamlit as st
import joblib
import numpy as np

model = joblib.load('parkinson.C5')

# import streamlit as st

st.title("Parkinson's Disease Dataset Input Form")

st.write("Please enter the following numerical variables for analysis:")

mdvp_fo = st.number_input("MDVP:Fo(Hz)")
mdvp_fhi = st.number_input("MDVP:Fhi(Hz)")
mdvp_flo = st.number_input("MDVP:Flo(Hz)")
mdvp_jitter_pct = st.number_input("MDVP:Jitter(%)")
mdvp_jitter_abs = st.number_input("MDVP:Jitter(Abs)")
mdvp_rap = st.number_input("MDVP:RAP")
mdvp_ppq = st.number_input("MDVP:PPQ")
jitter_ddp = st.number_input("Jitter:DDP")
mdvp_shimmer = st.number_input("MDVP:Shimmer")
mdvp_shimmer_db = st.number_input("MDVP:Shimmer(dB)")
shimmer_apq3 = st.number_input("Shimmer:APQ3")
shimmer_apq5 = st.number_input("Shimmer:APQ5")
mdvp_apq = st.number_input("MDVP:APQ")
shimmer_dda = st.number_input("Shimmer:DDA")
nhr = st.number_input("NHR")
hnr = st.number_input("HNR")
rpde = st.number_input("RPDE")
dfa = st.number_input("DFA")
spread1 = st.number_input("spread1")
spread2 = st.number_input("spread2")
d2 = st.number_input("D2")
ppe = st.number_input("PPE")


features = np.array([mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter_pct, mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe])
features = features.reshape(1,-1)


pred = model.predict(features)

if st.button('Predict'):
    if pred[0]==0:
        st.write("This input does not indicate Parkinson's disease.")
    else:
        st.write("This input indicates Parkinson's disease.")

