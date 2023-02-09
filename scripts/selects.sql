-- Pacientes que ficaram em estadias no ano de 2022
SELECT p.nome Paciente, e.data_inicial, e.data_final, q.numero_quarto  FROM PACIENTE p 
INNER JOIN ESTADIA e ON p.cpf = e.FK_PACIENTE_cpf 
INNER JOIN  QUARTO q ON q.numero_quarto = e.FK_QUARTO_numero_quarto 
WHERE e.data_inicial >= '2022-01-01' AND e.data_final < '2023-01-01'; 
-- ALGEBRA RELACIONAL : Π (Paciente.cpf, Paciente.nome, Estadia.data_inicial, 
--Estadia.data_final, Quarto.numero_quarto)
--(Paciente ⨝ Estadia ⨝ Quarto)
--σ (Estadia.data_inicial >= '2022-01-01' AND Estadia.data_final < '2023-01-01')


-- Pacientes que tiveram mais de uma PRESCRICAO 
SELECT c.fk_PACIENTE_cpf CPF, p2.nome, COUNT(*) Qtd_Prescricao  FROM CONSULTA c 
INNER JOIN PRESCRICAO p ON p.codigo_consulta = c.codigo 
INNER JOIN PACIENTE p2 ON p2.cpf = c.fk_PACIENTE_cpf
GROUP BY c.fk_PACIENTE_cpf 
HAVING Qtd_Prescricao > 1;
-- ALGEBRA RELACIONAL:σ(Prescricao.fk_CONSULTA_codigo)>1(Consulta ⨝ Prescricao) ⨝ Paciente

-- Gasto dos pacientes com consulta
SELECT p.cpf , p.nome, SUM(c.valor) `Total gasto com consulta`  FROM PACIENTE p 
INNER JOIN CONSULTA c ON c.fk_PACIENTE_cpf = p.cpf 
GROUP BY p.cpf ;
-- ALGEBRA RELACIONAL: Π (cpf, nome, SUM(valor)) (Paciente ⨝ (Consulta))

-- Gasto dos pacientes com exames em um ano
SELECT p.cpf, p.nome, YEAR(c.`data`) Ano, SUM(te.valor) `Gasto com exames`  FROM PACIENTE p 
INNER JOIN CONSULTA c ON c.fk_PACIENTE_cpf = p.cpf 
INNER JOIN PRESCRICAO p2 ON p2.codigo_consulta = c.codigo 
INNER JOIN EXAME e ON e.FK_PRESCRICAO_codigo = p2.codigo 
INNER JOIN tipo_EXAME te ON te.codigo_exame = e.FK_tipo_EXAME_codigo_exame 
GROUP BY p.cpf, YEAR(c.`data`);
-- ALGEBRA RELACIONAL: Π p.cpf, p.nome, YEAR(c.data), SUM(te.valor) (
--(PACIENTE ⨝ CONSULTA ⨝ PRESCRICAO ⨝ EXAME ⨝ TIPO_EXAME)
--GROUP BY p.cpf, p.nome, YEAR(c.data))


-- Nome do médico que não fez consulta e especializacao sem medico
SELECT m.nome `Nome do médico`, e.tipo_da_especializacao Especialização FROM CONSULTA c 
RIGHT JOIN MEDICO m ON c.fk_MEDICO_crm = m.crm
RIGHT JOIN ESPECIALIZACAO e ON e.codigo = m.FK_ESPECIALIZACAO_codigo 
WHERE c.codigo IS NULL;
-- ALGEBRA RELACIONAL: π(nome do médico, especialização)(MEDICO - π(fk_MEDICO_crm)(CONSULTA))

-- EXAME QUE AINDA NÃO FOI PRESCRITO
SELECT te.nome_exame  FROM EXAME e 
RIGHT JOIN tipo_EXAME te ON e.FK_tipo_EXAME_codigo_exame  = te.codigo_exame 
LEFT JOIN PRESCRICAO p ON p.codigo = e.FK_PRESCRICAO_codigo 
WHERE p.codigo IS NULL;


SELECT m.nome Médico, e.nome Enfermeira, p2.nome Paciente, p.nome Procedimento, p.custo  
FROM INTERNACAO i 
INNER JOIN PROCEDIMENTO p ON i.FK_PROCEDIMENTO_codigo  = p.codigo 
INNER JOIN ENFERMEIRA e ON e.codigo = i.FK_ENFERMEIRA_codigo
INNER JOIN MEDICO m ON m.crm = i.FK_MEDICO_crm
INNER JOIN ESTADIA e2  ON i.FK_ESTADIA_codigo = e2.codigo 
INNER JOIN PACIENTE p2 ON p2.cpf = e2.FK_PACIENTE_cpf 
WHERE p.custo > 2000;
