# Query Setup: [assessment]

## 1. Business Question
[In 1–2 sentences, describe in plain language what this query aims to answer.]

---

## 2. Required Codes and concepts
[List all relevant codes, identifiers, or reference lists needed for the query.]
Test Codes, etc

[Notes: ]
---

## 3. Data Locations

| Schema | Table | Column | Notes |
|--------|-------|--------|-------|
| [diagnosis] | [diagnosis] | [diagnosis_id] | [Unique diagnosis id] |
| [diagnosis] | [diagnosis] | [patient_id] | [Unique patient identifier] |
| [diagnosis] | [diagnosis] | [cancer_type] | [type of cancer] |
| [diagnosis] | [diagnosis] | [stage] | [stage of cancer] |
| [diagnosis] | [diagnosis] | [diagnosis_date] | [date of diagnosis] |
| [patient] | [patient] | [gender] | [gender] |
| [patient] | [patient] | [birth_date] | [birth date] |
| [patient] | [patient] | [country] | [patient's country] |

Properties:
patient_id - Unique patient identifer
gender - patient gender
birth_date - patient birth date
country - patient's country
diagnosis_id - unique diagnosis identifier
cancer_type - type of cancer
stage - stage of cancer
diagnosis_date - date of diagnosis
---

## 4. Caveats & Limitations
No quirks with data logic.

---

## 6. Additional Notes
No additional notes.

---

## 7. Prepared By
- **Name:** [Kunal]  
- **Date:** [2026-01-09]


# Question 1a: Count of Patients with Multiple Diagnoses

| Metric                              | Count |
|-------------------------------------|-------|
| Patients with Multiple Diagnoses    | 5     |

---

## Alternative Format (More Detailed)

| patient_id | Number of Diagnoses | Cancer Type        |
|------------|---------------------|-------------------|
| 1          | 2                   | Breast Cancer     |
| 2          | 2                   | Lung Cancer       |
| 6          | 2                   | Prostate Cancer   |
| 10         | 2                   | Lymphoma          |
| 15         | 2                   | Thyroid Cancer    |
| **Total**  | **5 patients**      |                   |

---

## Summary

✓ **5 patients** have multiple diagnosis records in the database.

Each of these patients has **exactly 2 diagnoses** of the **same cancer type** but at **different stages** and **different time points**, indicating disease progression or recurrence.





# Patients with Multiple Diagnoses

Here's the data formatted as a markdown table:

| patient_id | gender | birth_date | country | diagnosis_id | cancer_type      | stage     | diagnosis_date |
|------------|--------|------------|---------|--------------|------------------|-----------|----------------|
| 1          | Female | 1975-04-12 | USA     | 121          | Breast Cancer    | Stage I   | 2015-02-10     |
| 1          | Female | 1975-04-12 | USA     | 101          | Breast Cancer    | Stage II  | 2020-03-15     |
| 2          | Male   | 1968-09-30 | USA     | 122          | Lung Cancer      | Stage I   | 2012-03-18     |
| 2          | Male   | 1968-09-30 | USA     | 102          | Lung Cancer      | Stage III | 2019-07-10     |
| 6          | Male   | 1972-03-14 | Germany | 123          | Prostate Cancer  | Stage I   | 2015-07-01     |
| 6          | Male   | 1972-03-14 | Germany | 106          | Prostate Cancer  | Stage II  | 2020-10-11     |
| 10         | Male   | 1980-10-10 | Canada  | 110          | Lymphoma         | Stage II  | 2020-02-02     |
| 10         | Male   | 1980-10-10 | Canada  | 124          | Lymphoma         | Stage III | 2023-01-09     |
| 15         | Female | 1992-04-17 | France  | 115          | Thyroid Cancer   | Stage I   | 2021-06-10     |
| 15         | Female | 1992-04-17 | France  | 125          | Thyroid Cancer   | Stage II  | 2024-02-14     |

---

## Key Observations

**5 patients have multiple diagnoses:**
- **Patient 1**: Breast Cancer progressed from Stage I (2015) to Stage II (2020) - **5 years apart**
- **Patient 2**: Lung Cancer progressed from Stage I (2012) to Stage III (2019) - **7 years apart**
- **Patient 6**: Prostate Cancer progressed from Stage I (2015) to Stage II (2020) - **5 years apart**
- **Patient 10**: Lymphoma progressed from Stage II (2020) to Stage III (2023) - **3 years apart**
- **Patient 15**: Thyroid Cancer progressed from Stage I (2021) to Stage II (2024) - **3 years apart**

**Why they have multiple diagnoses:** These represent **cancer progression/recurrence** of the same cancer type at different time points with advancing stages, not different primary cancers.