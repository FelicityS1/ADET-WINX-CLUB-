# ADET-WINX-CLUB-

## 🏥 Smart Healthcare Monitoring

A decentralized health monitoring system designed to simulate and manage patient data securely and efficiently with real-time capabilities.

---

### 🎯 Project Focus

* 📡 **Remote Patient Monitoring**
  Continuously track vital signs and health metrics outside clinical settings.

* 🔐 **Secure Medical Records**
  Ensure data privacy and integrity through encryption and decentralized storage (optional extension).

* 🚨 **Real-Time Health Alerts**
  Trigger automated warnings based on abnormal values in sensor readings.

---

### 🧪 Simulated Sensors

* **Heart Rate Monitors**
  Track fluctuations to identify arrhythmias or irregular pulses.

* **Blood Oxygen (SpO₂) Sensors**
  Measure real-time oxygen saturation levels to detect hypoxia.

* **ECG Sensors**
  Monitor electrical heart activity and detect abnormalities.

* **Temperature Sensors**
  Detect abnormal body temperatures to identify fever or infection.

---

### 🧬 Data Simulation (Python)

The `HealthCare_DataSimulation.py` script generates realistic patient records with:

* **Identification & Demographics**: Unique IDs, names, ages
* **Lifestyle**: Exercise, smoking, alcohol, diet
* **Health Metrics**:

  * Body temperature, heart rate, blood pressure
  * Blood glucose, cholesterol, oxygen level, BMI
* **Medical Data**:

  * Medication adherence, test results, genetic risks
* **Behavioral & Environmental Factors**:

  * Sleep quality, stress, allergies
* **Lab Tests**:

  * Blood, urine, X-ray, MRI, CT scan, and more
  * Vitamin, mineral, and hormone levels

✅ The generated data is saved to both **CSV** and **JSON** formats for further analysis or visualization.

---

### 📁 File Outputs

* `healthcare_data.csv` – Tabular data format suitable for analytics or dashboards
* `healthcare_data.json` – Structured data format for APIs or NoSQL databases

---

### 🚀 Getting Started

1. Install Python dependencies:

   ```bash
   pip install pandas numpy
   ```

2. Run the simulation:

   ```bash
   python HealthCare_DataSimulation.py
   ```

3. Output files will be saved in your project directory.

---