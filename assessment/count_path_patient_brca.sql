SELECT gene,
clinical_significance,
COUNT(DISTINCT d.patient_id) AS patient_count
FROM Diagnosis d
INNER JOIN Sequencing s ON (d.diagnosis_id = s.diagnosis_id)
WHERE LOWER(s.gene) like '%brca%' and LOWER(s.clinical_significance) = 'pathogenic'
GROUP BY gene;