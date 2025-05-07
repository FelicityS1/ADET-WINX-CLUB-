# ADE'T A3101 ( WINX CLUB)

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from tkinter import messagebox


num_records = 15 # Number of records to generate, change as needed
data = []
for _ in range(num_records):
        data = []
        for _ in range(num_records):
            record = {
                # Identification
                "timestamp": datetime.now() - timedelta(minutes=np.random.randint(0, 1440)),
                "insurance_id": f"INS{np.random.randint(1000, 9999)}",
                "patient_id": f"PAT{np.random.randint(100, 999)}", 
                "patient_name": f"Patient_{np.random.randint(1, 100)}", # Random patient name
                "age": np.random.randint(16, 90), # Age range


                # Physical Activity and Lifestyle
                "exercise_frequency": np.random.randint(0, 7),
                "activity_level": np.random.choice(["Low", "Moderate", "High"]),
                "physical_activity_duration": np.random.randint(0, 120),
                "smoking_status": np.random.choice(["Non-smoker", "Former smoker", "Current smoker"]),
                "alcohol_consumption": np.random.choice(["None", "Occasional", "Moderate", "Heavy"]),
                "dietary_preference": np.random.choice(["Vegetarian", "Vegan", "Non-vegetarian", "Pescatarian"]),
                

                # Health Metrics
                "body_temp": round(np.random.uniform(36.0, 38.0), 1), # Body temperature in Celsius
                "heart_rate": np.random.randint(60, 100), # Heart rate in bpm
                "blood_pressure": f"{np.random.randint(100, 140)}/{np.random.randint(60, 90)}", # Systolic/Diastolic
                "blood_glucose": np.random.randint(70, 180),# Blood glucose level
                "cholesterol": np.random.randint(125, 250), # Cholesterol level
                "oxygen_level": np.random.randint(95, 100), # Oxygen saturation level
                "bmi": round(np.random.uniform(18.5, 30.0), 1), # BMI range

                # Medical Information
                "medication_adherence": np.random.choice([True, False]), # If theres existing any Medication 
                "medication_type": np.random.choice(["None", "Antibiotic", "Asthma", "Diabetes", "Cholesterol"]), # Type of medecine you are taking
                "blood_test_result": np.random.choice(["Normal", "Abnormal"]),
                "vaccination_status": np.random.choice(["Vaccinated", "Not Vaccinated"]),
                "genetic_risk_factor": np.random.choice(["Low", "Moderate", "High"]), 

                # Environmental and Behavioral Factors
                "sleep_quality": np.random.randint(1, 10),# 1-10 scale
                "stress_level": np.random.randint(0, 10), # 0-10 scale
                "allergies": np.random.choice(["None", "Peanuts", "Dust", "Pollen", "Gluten", "Lactose", "Shellfish", "Soy"]),
                
                # Different Health Tests
                "stool_test": np.random.choice(["Normal", "Abnormal"]),
                "urine_test": np.random.choice(["Normal", "Abnormal"]),
                "xray_result": np.random.choice(["Normal", "Abnormal"]),
                "mri_result": np.random.choice(["Normal", "Abnormal"]),
                "ct_scan_result": np.random.choice(["Normal", "Abnormal"]),
                "ultrasound_result": np.random.choice(["Normal", "Abnormal"]),
                "liver_function_test": np.random.choice(["Normal", "Abnormal"]),
                "kidney_function_test": np.random.choice(["Normal", "Abnormal"]),
                "cbc_result": np.random.choice(["Normal", "Abnormal"]),  # Complete Blood Count
                "thyroid_function_test": np.random.choice(["Normal", "Abnormal"]),
                "vitamin_d_level": np.random.randint(10, 50),  # Vitamin D level in ng/mL
                "iron_level": np.random.randint(30, 160),  # Iron level in µg/dL
                "hemoglobin_level": round(np.random.uniform(12.0, 17.5), 1),  # Hemoglobin level in g/dL
                "sodium_level": np.random.randint(135, 145),  # Sodium level in mEq/L
                "potassium_level": round(np.random.uniform(3.5, 5.0), 1),  # Potassium level in mEq/L}
                "calcium_level": round(np.random.uniform(8.5, 10.5), 1),  # Calcium level in mg/dL
                "magnesium_level": round(np.random.uniform(1.5, 2.5), 1),  # Magnesium level in mg/dL
            }

            
            data.append(record)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        
try:
    # Save dataset
    csv_path = r"C:\Users\Ken\Documents\MMDC 2025\healthcare_data.csv" 
    df.to_csv(csv_path, index=4)

    json_path = r"C:\Users\Ken\Documents\MMDC 2025\healthcare_data.json"
    df.to_json(json_path, orient="records", indent=4)
    print("JSON file saved at:", json_path)

    messagebox.showinfo("Success", f"Generated {num_records} Records and Saved to files.")
except Exception as e:
    print(f"An error occurred: {e}")

        
# Generate and display simulated IoT data
csv_path = r"C:\Users\Ken\Documents\MMDC 2025\healthcare_data.csv"
df.to_csv(csv_path, index=False)
