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

