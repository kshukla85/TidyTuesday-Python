SELECT gene,
COUNT(DISTINCT d.patient_id) AS patient_count
FROM Diagnosis d
INNER JOIN Sequencing s ON (d.diagnosis_id = s.diagnosis_id)
WHERE LOWER(s.gene) like '%brca%'
GROUP BY gene;