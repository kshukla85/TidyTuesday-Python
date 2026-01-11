SELECT AVG(o.survival_months) AS avg_survival_months,
d.cancer_type
FROM Outcomes as o
INNER JOIN Diagnosis d ON o.diagnosis_id = d.diagnosis_id
GROUP BY d.cancer_type;