# Query Setup: [assessment]

## 1. Business Question
1. Count of patients with multiple diagnoses. Why do these patients have more than one
diagnosis (what in the data is resulting in more than one diagnosis entry)? Please
provide:
a. The count of patients with multiple diagnoses

b. The reason why they have multiple diagnoses
c. Output the data for these patients showing why they have multiple diagnoses
2. Count of patients who received surgery. Distribution of patients who received surgery by
stage.
3. Count of patients who started treatment in 2020 or after.
4. Average survival months by cancer type.
5. Count of patients with a BRCA mutation. How many of these patients have a pathogenic
BRCA mutation?

---

## 2. Required Codes and concepts

For question 1, I did a count with having `diagnosis_id` greater than 1 to find patients with multiple diagnoses. They have multiple diagnoses with the same disease because the disease has progressed.

For question 2, I am counting patients who recieved surgery, and then surgery by `stage` using the count aggregate function.

For question 3, I am counting by `patient_id` and I am filtering by `start_date`.

For question 4, I took the avg of `survival_months`, and then the avg by `stage`.

For question 5, I took a count of patients filtering by the BRCA pathogenic mutation using `gene` and `clinical significance`.

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
| [outcomes] | [outcomes] | [gene] | [the gene] |
| [outcomes] | [outcomes] | [clinical_signficance] | [pathogenic versus benign] |

Properties:
patient_id - Unique patient identifer
gender - patient gender
birth_date - patient birth date
country - patient's country
diagnosis_id - unique diagnosis identifier
cancer_type - type of cancer
stage - stage of cancer
diagnosis_date - date of diagnosis
gene - a gene
clinical_significance - pathogenic versus benign
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


# 1: Count of patients with multiple diagnoses. Why do these patients have more than one diagnosis (what in the data is resulting in more than one diagnosis entry)? Please provide: a. The count of patients with multiple diagnoses b. The reason why they have multiple diagnoses c. Output the data for these patients showing why they have multiple diagnoses

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


# 2. Count of patients who received surgery. Distribution of patients who received surgery by stage.

| Metric                              | Count |
|-------------------------------------|-------|
| Patients with Surgery    | 5     |

| Stage | Treatment Count |
|-------|-----------------|
| Stage I | 5 |


# 3. Count of patients who started treatment in 2020 or after.

| Treatment | Patient Count |
|-------|-----------------|
| All treatments | 13 |

# 4. Average survival months by cancer type.

| avg_survival_months | cancer_type |
|---------------------|-------------|
| 30.6 | Breast Cancer |
| 25.0 | Cervical Cancer |
| 27.0 | Colon Cancer |
| 18.5 | Leukemia |
| 19.0 | Liver Cancer |
| 19.0 | Lung Cancer |
| 28.0 | Lymphoma |
| 48.0 | Ovarian Cancer |
| 10.0 | Pancreatic Cancer |
| 30.0 | Prostate Cancer |
| 7.0 | Stomach Cancer |
| 26.0 | Thyroid Cancer |

# 5. Count of patients with a BRCA mutation. How many of these patients have a pathogenic BRCA mutation?

| gene | patient_count |
|------|---------------|
| BRCA1 | 3 |
| BRCA2 | 3 |


| gene | clinical_significance | patient_count |
|------|----------------------|---------------|
| BRCA1 | Pathogenic | 2 |
| BRCA2 | Pathogenic | 2 |