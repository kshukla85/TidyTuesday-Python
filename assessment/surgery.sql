
SELECT
    COUNT(DISTINCT t.treatment_id) AS treatments_with_surgery
FROM
    Treatment t
GROUP BY t.treatment_type
HAVING t.treatment_type = 'Surgery';