import streamlit as st 
import pandas as pd
reference_data = pd.read_csv('ReferenceData.csv')
verify_data = pd.read_csv('VerifyDataset.csv')
batch_id = st.text_input("Enter Batch ID")
selected_data = verify_data[verify_data["Batch ID"] == batch_id]

if selected_data.empty:
    st.error("Batch ID not found.")
else:
    for index, row in selected_data.iterrows():
        score = 0
    observations = []
    if row["CropCycleMatch"] == "Yes":
        score += 15
        observations.append("Crop cycle is consistent.")
    elif row["CropCycleMatch"] == "Partial":
        score += 10
        observations.append("Crop cycle is partially consistent.")
    elif row["CropCycleMatch"] == "No":
        score -= 15 
        observations.append("Crop cycle is inconsistent.")
    if row["SoilMatch"] == "Yes":
        score += 10
        observations.append("Soil type is suitable.")
    elif row["SoilMatch"] == "No":
        score -= 10 
        observations.append("Soil type is unsuitable.")
    if row["YieldConsistency"] == "Realistic":
        score += 15
        observations.append("Yield is realistic.")
    elif row["YieldConsistency"] == "Unrealistic":
        score -= 15
        observations.append("Yield is unrealistic.")
    if row["LandAreaConsistency"] == "Realistic":
        score += 10
        observations.append("Land area is consistent.")
    elif row["LandAreaConsistency"] == "Unrealistic":
        score -= 10
        observations.append("Land area is inconsistent.")
    if row["FertilizerTransparency"] == "Transparent":
        score += 15
        observations.append("Fertilizer usage is transparent.")
    elif row["FertilizerTransparency"] == "Vague":
        score -= 15
        observations.append("Fertilizer usage is vague.")
    if row["IrrigationSuitability"] == "Suitable":
        score += 10 
    elif row["IrrigationSuitability"] == "Unsuitable":
        score -= 10 
    if row["TransportStatus"] == "Complete":
        score += 15
    elif row["TransportStatus"] == "Partial":
        score += 10 
    elif row["TransportStatus"] == "Incomplete":
        score -= 15 
    if row["LabTestReports"] == "Complete":
        score += 15
        observations.append("Lab test reports are complete.")
    elif row["LabTestReports"] == "Partial":
        score += 10 
        observations.append("Lab test reports are partially complete.")
    elif row["LabTestReports"] == "Missing":
        score -= 15 
        observations.append("Lab test reports are missing.")
    elif row["LabTestReports"] == "Incomplete":
        score -= 15
        observations.append("Lab test reports are incomplete.")
    # Print verification per row
    st.write("Batch ID:", row["Batch ID"])
    if score >= 90:
        status = "Fully Verified"
    elif 35 <= score < 90:
        status = "Partially Verified"
    else:
        status = "Incomplete Verification"
    st.write("Verification:", status)
    if observations:
        st.write(observations)
