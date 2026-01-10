-- SQLite
-- QUESTION 1: Count of patients with multiple diagnoses

-- a. Count of patients with multiple diagnoses
SELECT COUNT(*) AS patients_with_multiple_diagnoses
FROM (
    SELECT patient_id
    FROM Diagnosis
    GROUP BY patient_id
    HAVING COUNT(diagnosis_id) > 1
);

-- b & c. Show details of patients with multiple diagnoses
SELECT 
    d.patient_id,
    p.gender,
    p.birth_date,
    p.country,
    d.diagnosis_id,
    d.cancer_type,
    d.stage,
    d.diagnosis_date
FROM Diagnosis d
JOIN Patient p ON d.patient_id = p.patient_id
WHERE d.patient_id IN (
    SELECT patient_id
    FROM Diagnosis
    GROUP BY patient_id
    HAVING COUNT(diagnosis_id) > 1
)
ORDER BY d.patient_id, d.diagnosis_date;
