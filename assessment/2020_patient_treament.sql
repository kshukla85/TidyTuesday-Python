SELECT COUNT(DISTINCT d.patient_id) AS patient_count
FROM treatment t
INNER JOIN diagnosis d ON t.diagnosis_id = d.diagnosis_id
WHERE t.start_date >= '2020-01-01';