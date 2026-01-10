-- Create the Patient table
CREATE TABLE Patient (
    patient_id INTEGER PRIMARY KEY,
    gender TEXT,
    birth_date TEXT,
    country TEXT
);

-- Insert data into Patient table
INSERT INTO Patient (patient_id, gender, birth_date, country) VALUES
(1, 'Female', '1975-04-12', 'USA'),
(2, 'Male', '1968-09-30', 'USA'),
(3, 'Female', '1982-01-18', 'Canada'),
(4, 'Male', '1959-11-05', 'UK'),
(5, 'Female', '1990-06-22', 'India'),
(6, 'Male', '1972-03-14', 'Germany'),
(7, 'Female', '1985-12-02', 'France'),
(8, 'Male', '1961-07-19', 'USA'),
(9, 'Female', '1995-02-27', 'Brazil'),
(10, 'Male', '1980-10-10', 'Canada'),
(11, 'Female', '1978-08-09', 'UK'),
(12, 'Male', '1965-01-03', 'India'),
(13, 'Female', '1988-11-23', 'USA'),
(14, 'Male', '1955-06-30', 'Germany'),
(15, 'Female', '1992-04-17', 'France'),
(16, 'Male', '1970-09-12', 'USA'),
(17, 'Female', '1963-12-05', 'Brazil'),
(18, 'Male', '1984-05-21', 'Canada'),
(19, 'Female', '1976-07-14', 'UK'),
(20, 'Male', '1991-03-08', 'India');

-- Create the Diagnosis table
CREATE TABLE Diagnosis (
    diagnosis_id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    cancer_type TEXT,
    stage TEXT,
    diagnosis_date TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
);

-- Insert data into Diagnosis table
INSERT INTO Diagnosis (diagnosis_id, patient_id, cancer_type, stage, diagnosis_date) VALUES
(101, 1, 'Breast Cancer', 'Stage II', '2020-03-15'),
(102, 2, 'Lung Cancer', 'Stage III', '2019-07-10'),
(103, 3, 'Breast Cancer', 'Stage I', '2021-01-25'),
(104, 4, 'Colon Cancer', 'Stage IV', '2018-05-18'),
(105, 5, 'Leukemia', 'Stage II', '2022-08-02'),
(106, 6, 'Prostate Cancer', 'Stage II', '2020-10-11'),
(107, 7, 'Breast Cancer', 'Stage III', '2019-06-05'),
(108, 8, 'Lung Cancer', 'Stage IV', '2017-09-14'),
(109, 9, 'Cervical Cancer', 'Stage I', '2021-11-20'),
(110, 10, 'Lymphoma', 'Stage II', '2020-02-02'),
(111, 11, 'Ovarian Cancer', 'Stage III', '2019-12-15'),
(112, 12, 'Stomach Cancer', 'Stage IV', '2018-08-08'),
(113, 13, 'Breast Cancer', 'Stage I', '2022-03-01'),
(114, 14, 'Pancreatic Cancer', 'Stage IV', '2017-04-22'),
(115, 15, 'Thyroid Cancer', 'Stage I', '2021-06-10'),
(116, 16, 'Colon Cancer', 'Stage II', '2020-09-19'),
(117, 17, 'Liver Cancer', 'Stage III', '2019-05-30'),
(118, 18, 'Lung Cancer', 'Stage I', '2022-01-05'),
(119, 19, 'Breast Cancer', 'Stage II', '2021-07-17'),
(120, 20, 'Leukemia', 'Stage III', '2020-11-11'),
(121, 1, 'Breast Cancer', 'Stage I', '2015-02-10'),
(122, 2, 'Lung Cancer', 'Stage I', '2012-03-18'),
(123, 6, 'Prostate Cancer', 'Stage I', '2015-07-01'),
(124, 10, 'Lymphoma', 'Stage III', '2023-01-09'),
(125, 15, 'Thyroid Cancer', 'Stage II', '2024-02-14');

-- Create the Treatment table
CREATE TABLE Treatment (
    treatment_id INTEGER PRIMARY KEY,
    diagnosis_id INTEGER,
    treatment_type TEXT,
    start_date TEXT,
    end_date TEXT,
    FOREIGN KEY (diagnosis_id) REFERENCES Diagnosis(diagnosis_id)
);

-- Insert data into Treatment table
INSERT INTO Treatment (treatment_id, diagnosis_id, treatment_type, start_date, end_date) VALUES
(215, 114, 'Chemotherapy', '2017-05-01', '2017-10-01'),
(209, 108, 'Immunotherapy', '2017-10-01', '2018-04-01'),
(205, 104, 'Chemotherapy', '2018-06-01', '2018-12-01'),
(213, 112, 'Palliative Care', '2018-09-01', '2019-03-01'),
(218, 117, 'Chemotherapy', '2019-06-15', '2019-12-15'),
(208, 107, 'Chemotherapy', '2019-07-01', '2019-12-01'),
(203, 102, 'Chemotherapy', '2019-08-01', '2020-02-01'),
(212, 111, 'Chemotherapy', '2020-01-01', '2020-07-01'),
(211, 110, 'Chemotherapy', '2020-03-01', '2020-09-01'),
(201, 101, 'Chemotherapy', '2020-04-01', '2020-09-01'),
(202, 101, 'Radiation', '2020-09-15', '2020-11-15'),
(217, 116, 'Radiation', '2020-10-10', '2020-12-10'),
(207, 106, 'Radiation', '2020-11-01', '2021-01-01'),
(221, 120, 'Chemotherapy', '2020-12-01', '2021-06-01'),
(204, 103, 'Surgery', '2021-02-10', '2021-02-20'),
(216, 115, 'Surgery', '2021-06-20', '2021-06-30'),
(220, 119, 'Radiation', '2021-08-01', '2021-10-01'),
(210, 109, 'Surgery', '2021-12-01', '2021-12-10'),
(219, 118, 'Surgery', '2022-02-01', '2022-02-10'),
(214, 113, 'Surgery', '2022-03-15', '2022-03-25'),
(206, 105, 'Bone Marrow Transplant', '2022-09-10', '2023-01-10'),
(222, 124, 'Chemotherapy', '2023-02-01', '2023-08-01'),
(223, 125, 'Radiation', '2024-03-01', '2024-04-15');

-- Create the Outcomes table
CREATE TABLE Outcomes (
    outcome_id INTEGER PRIMARY KEY,
    diagnosis_id INTEGER,
    status TEXT,
    last_followup_date TEXT,
    survival_months INTEGER,
    FOREIGN KEY (diagnosis_id) REFERENCES Diagnosis(diagnosis_id)
);

-- Insert data into Outcomes table
INSERT INTO Outcomes (outcome_id, diagnosis_id, status, last_followup_date, survival_months) VALUES
(301, 101, 'Remission', '2023-12-01', 45),
(302, 102, 'Deceased', '2021-03-15', 20),
(303, 103, 'Remission', '2024-01-01', 36),
(304, 104, 'Deceased', '2019-11-20', 18),
(305, 105, 'Ongoing Treatment', '2024-06-01', 22),
(306, 106, 'Remission', '2023-05-01', 30),
(307, 107, 'Deceased', '2020-08-01', 14),
(308, 108, 'Deceased', '2018-11-10', 13),
(309, 109, 'Remission', '2023-12-10', 25),
(310, 110, 'Remission', '2022-06-01', 28),
(311, 111, 'Ongoing Treatment', '2024-01-15', 48),
(312, 112, 'Deceased', '2019-02-01', 7),
(313, 113, 'Remission', '2024-04-01', 24),
(314, 114, 'Deceased', '2018-02-15', 10),
(315, 115, 'Remission', '2023-07-01', 26),
(316, 116, 'Remission', '2023-10-01', 36),
(317, 117, 'Deceased', '2020-01-01', 19),
(318, 118, 'Remission', '2024-02-01', 24),
(319, 119, 'Ongoing Treatment', '2024-05-01', 34),
(320, 120, 'Deceased', '2022-02-10', 15);

-- Create the Sequencing table
CREATE TABLE Sequencing (
    sequencing_id INTEGER PRIMARY KEY,
    diagnosis_id INTEGER,
    gene TEXT,
    mutation TEXT,
    clinical_significance TEXT,
    FOREIGN KEY (diagnosis_id) REFERENCES Diagnosis(diagnosis_id)
);

-- Insert data into Sequencing table
INSERT INTO Sequencing (sequencing_id, diagnosis_id, gene, mutation, clinical_significance) VALUES
(401, 101, 'BRCA1', 'c.5266dupC', 'Pathogenic'),
(402, 101, 'TP53', 'R175H', 'Pathogenic'),
(403, 102, 'EGFR', 'L858R', 'Pathogenic'),
(404, 102, 'KRAS', 'G12C', 'Pathogenic'),
(405, 103, 'BRCA2', 'c.5946delT', 'Pathogenic'),
(406, 104, 'APC', 'E1309fs', 'Pathogenic'),
(407, 105, 'FLT3', 'ITD', 'Pathogenic'),
(408, 106, 'PTEN', 'R233*', 'Likely Pathogenic'),
(409, 107, 'PIK3CA', 'H1047R', 'Pathogenic'),
(410, 108, 'ALK', 'EML4-ALK', 'Pathogenic'),
(411, 109, 'HPV16', 'E6/E7', 'Pathogenic'),
(412, 110, 'BCL2', 't(14;18)', 'Pathogenic'),
(413, 111, 'BRCA1', 'c.181T>G', 'Pathogenic'),
(414, 112, 'CDH1', 'c.1003C>T', 'Pathogenic'),
(415, 113, 'BRCA2', 'c.7008-1G>A', 'Pathogenic'),
(416, 114, 'KRAS', 'G12D', 'Pathogenic'),
(417, 115, 'RET', 'M918T', 'Pathogenic'),
(418, 116, 'MLH1', 'Promoter Methylation', 'Pathogenic'),
(419, 117, 'TP53', 'R248Q', 'Pathogenic'),
(420, 118, 'EGFR', 'Exon 19 Del', 'Pathogenic'),
(421, 101, 'BRCA1', 'c.1067A>G', 'Benign'),
(422, 103, 'TP53', 'P72R', 'Benign'),
(423, 110, 'ATM', 'c.5557G>A', 'Likely Benign'),
(424, 116, 'MSH2', 'c.2006-6T>C', 'Benign'),
(425, 118, 'EGFR', 'R521K', 'Benign'),
(426, 102, 'EGFR', 'Q787Q', 'Benign'),
(427, 107, 'TP53', 'R213R', 'Benign'),
(428, 113, 'BRCA1', 'c.2612C>T', 'Likely Benign'),
(429, 119, 'BRCA2', 'c.1114A>C', 'Benign'),
(430, 120, 'TP53', 'P72R', 'Benign');
