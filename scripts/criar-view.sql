-- RESULTA NO VALOR GANHO PELOS MÉDICOS NAS CONSULTAS DO ANO 2023
CREATE VIEW valor_ganho_medico_2023 AS
SELECT m.crm, m.nome ,e.tipo_da_especializacao , YEAR(`data`) ANO, SUM(VALOR) `Total ganho`
FROM CONSULTA c 
INNER JOIN MEDICO m ON m.crm = c.fk_MEDICO_crm 
INNER JOIN ESPECIALIZACAO e ON e.codigo = m.FK_ESPECIALIZACAO_codigo 
WHERE YEAR(`data`)=2023
GROUP BY fk_MEDICO_crm,  YEAR(`data`)

-- Usando a view para filtrar quem ganho menos de 2000 reais
SELECT * FROM valor_ganho_medico_2023 vgm 
WHERE vgm.`Total ganho` < 2000;