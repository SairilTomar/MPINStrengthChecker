

# mpin_app.py

import streamlit as st
from mpin_checker.mpin import is_common_mpin, check_demographic

st.title("🔐 MPIN Strength Checker")

mpin_length = st.radio("Choose MPIN length:", ("4", "6"))
mpin = st.text_input(f"Enter your {mpin_length}-digit MPIN:")

dob_self = st.text_input("Your DOB (DDMMYY):")
dob_spouse = st.text_input("Spouse's DOB (DDMMYY):")
anniversary = st.text_input("Anniversary (DDMMYY):")

dates = {
    'DOB_SELF': dob_self,
    'DOB_SPOUSE': dob_spouse,
    'ANNIVERSARY': anniversary
}

if st.button("Check MPIN Strength"):
    if not mpin.isdigit() or len(mpin) != int(mpin_length):
        st.error(f"Please enter exactly {mpin_length} digits.")
    else:
        reasons = []
        if is_common_mpin(mpin):
            reasons.append("MPIN is too common or predictable.")
        reasons.extend(check_demographic(mpin, dates))

        if reasons:
            st.error("🔴 Weak MPIN:\n\n" + "\n".join(f"- {r}" for r in reasons))
        else:
            st.success("🟢 Strong MPIN!")
