SELECT 
    d.stage,
    COUNT(DISTINCT t.treatment_id) AS treatment_count
FROM Treatment t
INNER JOIN Diagnosis d ON t.diagnosis_id = d.diagnosis_id
WHERE LOWER(t.treatment_type) = 'surgery'
GROUP BY d.stage
ORDER BY 
    CASE d.stage
        WHEN 'Stage I' THEN 1
        WHEN 'Stage II' THEN 2
        WHEN 'Stage III' THEN 3
        WHEN 'Stage IV' THEN 4
        ELSE 5
    END;
