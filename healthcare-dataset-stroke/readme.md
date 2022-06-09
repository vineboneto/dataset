# [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

## Resume

Take descriptive values ​​from the dataset and transform them into reals or integers.

**Columns**

1. id: unique identifier
2. gender: "Male", "Female" or "Other"
3. age: age of the patient
4. hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5. heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6. ever_married: "No" or "Yes"
7. work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8. Residence_type: "Rural" or "Urban"
9. avg_glucose_level: average glucose level in blood
10. bmi: body mass index
11. smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"\*
12. stroke: 1 if the patient had a stroke or 0 if not

\*Note: "Unknown" in smoking_status means that the information is unavailable for this patient

**Columns Adapter**

2. gender: ["Male" = 0, "Female" = 1, "Other" = 2]
3. ever_married: ["No" = 0, "Yes" = 1]
4. work_type: ["children" = 0, "Govt_jov" = 1, "Never_worked" = 2, "Private" = 3, "Self-employed" = 4]
5. Residence_type: ["Rural" = 0, "Urban" = 1]
6. bmi: in case N/A = -1
7. smoking_status: ["formerly smoked" = 0, "never smoked" = 1, "smokes" = 2, "Unknown" = 3]
