-- INSERIR PACIENTE
INSERT INTO PACIENTE  (cpf, nome, endereco, telefone)
VALUES ('12345678901', 'João Silva', 'Rua das Flores, 123', '11 98765-4321');

INSERT INTO PACIENTE (cpf, nome, endereco, telefone)
VALUES ('23456789012', 'Maria Silva', 'Rua dos Jardins, 456', '22 12345-6789');

INSERT INTO PACIENTE (cpf, nome, endereco, telefone)
VALUES ('34567890123', 'Pedro Oliveira', 'Rua dos Pássaros, 789', '33 94321-0987');

INSERT INTO PACIENTE (cpf, nome, endereco, telefone)
VALUES ('45678901234', 'Ana Paula', 'Rua dos Girassóis, 147', '44 87655-3321');

INSERT INTO PACIENTE (cpf, nome, endereco, telefone)
VALUES ('56789012345', 'José Souza', 'Rua das Águas, 258', '55 56789-1234');

-- INSERIR ESPECIALIZACAO

INSERT INTO ESPECIALIZACAO (codigo, tipo_da_especializacao)
VALUES (1, 'Cardiologista');

INSERT INTO ESPECIALIZACAO (codigo, tipo_da_especializacao)
VALUES (2, 'Neurologista');

INSERT INTO ESPECIALIZACAO (codigo, tipo_da_especializacao)
VALUES (3, 'Ortopedista');

INSERT INTO ESPECIALIZACAO (codigo, tipo_da_especializacao)
VALUES (4, 'Oncologista');

INSERT INTO ESPECIALIZACAO (codigo, tipo_da_especializacao)
VALUES (5, 'Dermatologista');

-- INSERIR MEDICO

INSERT INTO MEDICO (crm, nome, telefone, endereco, FK_ESPECIALIZACAO_codigo)
VALUES ('123456', 'João Silva', '11 98765-4321', 'Rua das Flores, 123', 3);

INSERT INTO MEDICO (crm, nome, telefone, endereco, FK_ESPECIALIZACAO_codigo)
VALUES ('234567', 'Maria Silva', '22 12345-6789', 'Rua dos Jardins, 456', 1);

INSERT INTO MEDICO (crm, nome, telefone, endereco, FK_ESPECIALIZACAO_codigo)
VALUES ('345678', 'Pedro Oliveira', '33 94321-0987', 'Rua dos Pássaros, 789', 5);

INSERT INTO MEDICO (crm, nome, telefone, endereco, FK_ESPECIALIZACAO_codigo)
VALUES ('456789', 'Ana Paula', '44 87655-3321', 'Rua dos Girassóis, 147', 2);

INSERT INTO MEDICO (crm, nome, telefone, endereco, FK_ESPECIALIZACAO_codigo)
VALUES ('567890', 'José Souza', '55 56789-1234', 'Rua das Águas, 258', 3);

INSERT INTO MEDICO (crm, nome, telefone, endereco, FK_ESPECIALIZACAO_codigo)
VALUES ('767890', 'Thiago Yuiti', '55 56789-1234', 'Rua das Águas, 258', 4);

-- INSERIR CONSULTA

INSERT INTO CONSULTA (fk_MEDICO_crm, fk_PACIENTE_cpf, `data`, valor, plano_saude)
VALUES('123456', '23456789012', NOW(), 350, 1);

INSERT INTO CONSULTA (fk_MEDICO_crm, fk_PACIENTE_cpf, `data`, valor, plano_saude)
VALUES('123456', '45678901234', NOW(), 550, 0);

INSERT INTO CONSULTA (fk_MEDICO_crm, fk_PACIENTE_cpf, `data`, valor, plano_saude)
VALUES('234567', '12345678901', NOW(), 1550, 0);

INSERT INTO CONSULTA (fk_MEDICO_crm, fk_PACIENTE_cpf, `data`, valor, plano_saude)
VALUES('456789', '34567890123', NOW(), 420, 0);

INSERT INTO CONSULTA (fk_MEDICO_crm, fk_PACIENTE_cpf, `data`, valor, plano_saude)
VALUES('456789', '56789012345', NOW(), 375, 1);

-- INSERIR PRESCRICAO
INSERT INTO PRESCRICAO (`data`, codigo_consulta, codigo)
VALUES (NOW(), 1, 0);

INSERT INTO PRESCRICAO (`data`, codigo_consulta, codigo)
VALUES (NOW(), 1, 1);

INSERT INTO PRESCRICAO (`data`, codigo_consulta, codigo)
VALUES (NOW(), 4, 2);

INSERT INTO PRESCRICAO (`data`, codigo_consulta, codigo)
VALUES (NOW(), 5, 3);


INSERT INTO PRESCRICAO (`data`, codigo_consulta, codigo)
VALUES (NOW(), 2, 4);


-- INSERIR tipo_EXAME

INSERT INTO tipo_EXAME (valor, codigo_exame, validade, nome_exame)
VALUES (235, 111, '2024-06-13', 'Sangue');

INSERT INTO tipo_EXAME (valor, codigo_exame, validade, nome_exame)
VALUES (525, 222, '2024-06-13', 'Colesterol');

INSERT INTO tipo_EXAME (valor, codigo_exame, validade, nome_exame)
VALUES (345, 333, '2024-06-13', 'Hemograma');

INSERT INTO tipo_EXAME (valor, codigo_exame, validade, nome_exame)
VALUES (1525, 444, '2024-06-13', 'Glicemia');

INSERT INTO tipo_EXAME (valor, codigo_exame, validade, nome_exame)
VALUES (157, 555, '2024-06-13', 'Exames de fezes e urina.');


-- INSERIR EXAME

INSERT INTO EXAME (codigo, FK_PRESCRICAO_codigo, FK_tipo_EXAME_codigo_exame)
VALUES (1, 0, 333);

INSERT INTO EXAME (codigo, FK_PRESCRICAO_codigo, FK_tipo_EXAME_codigo_exame)
VALUES (2, 1, 555);

INSERT INTO EXAME (codigo, FK_PRESCRICAO_codigo, FK_tipo_EXAME_codigo_exame)
VALUES (3, 1, 333);

INSERT INTO EXAME (codigo, FK_PRESCRICAO_codigo, FK_tipo_EXAME_codigo_exame)
VALUES (4, 1, 444);

INSERT INTO EXAME (codigo, FK_PRESCRICAO_codigo, FK_tipo_EXAME_codigo_exame)
VALUES (5, 2, 222);


-- INSERIR tipo_MEDICACAO

INSERT INTO tipo_MEDICACAO (codigo_medicamento, nome_do_medicamento)
VALUES (121, 'Dorflex');

INSERT INTO tipo_MEDICACAO (codigo_medicamento, nome_do_medicamento)
VALUES (232, 'Xarelto');

INSERT INTO tipo_MEDICACAO (codigo_medicamento, nome_do_medicamento)
VALUES (343, 'Neosaldina');

INSERT INTO tipo_MEDICACAO (codigo_medicamento, nome_do_medicamento)
VALUES (454, 'Torsilax');

INSERT INTO tipo_MEDICACAO (codigo_medicamento, nome_do_medicamento)
VALUES (565, 'Victoza');

-- INSERIR MEDICACAO

INSERT INTO MEDICACAO (codigo, FK_PRESCRICAO_codigo, FK_tipo_MEDICACAO_codigo_medicamento, dose)
VALUES (1, 0, 121, '50 mg');

INSERT INTO MEDICACAO (codigo, FK_PRESCRICAO_codigo, FK_tipo_MEDICACAO_codigo_medicamento, dose)
VALUES (2, 2, 565, '150 mg');

INSERT INTO MEDICACAO (codigo, FK_PRESCRICAO_codigo, FK_tipo_MEDICACAO_codigo_medicamento, dose)
VALUES (3, 3, 343, '250 mg');

INSERT INTO MEDICACAO (codigo, FK_PRESCRICAO_codigo, FK_tipo_MEDICACAO_codigo_medicamento, dose)
VALUES (4, 4, 343, '50 mg');

INSERT INTO MEDICACAO (codigo, FK_PRESCRICAO_codigo, FK_tipo_MEDICACAO_codigo_medicamento, dose)
VALUES (5, 1, 232, '100 mg');


-- INSERIR ENFERMEIRA

INSERT INTO ENFERMEIRA (codigo, nome, telefone) VALUES (4, 'Luciana Santos', '5554443333');
INSERT INTO ENFERMEIRA (codigo, nome, telefone) VALUES (5, 'Gabriela Ribeiro', '1112223333');
INSERT INTO ENFERMEIRA (codigo, nome, telefone) VALUES (6, 'Camila Ferreira', '2223334444');
INSERT INTO ENFERMEIRA (codigo, nome, telefone) VALUES (7, 'Eduarda Silva', '3334445555');
INSERT INTO ENFERMEIRA (codigo, nome, telefone) VALUES (8, 'Isabela Oliveira', '4445556666');


-- INSERIR QUARTO

INSERT INTO QUARTO (numero_quarto, andar, disponivel) VALUES (101, 1, 1);
INSERT INTO QUARTO (numero_quarto, andar, disponivel) VALUES (102, 1, 1);
INSERT INTO QUARTO (numero_quarto, andar, disponivel) VALUES (103, 2, 1);
INSERT INTO QUARTO (numero_quarto, andar, disponivel) VALUES (104, 2, 0);
INSERT INTO QUARTO (numero_quarto, andar, disponivel) VALUES (105, 3, 1);

-- INSERIR PROCEDIMENTO

INSERT INTO PROCEDIMENTO (codigo, nome, custo) VALUES (6, 'Internação por dia', 500);
INSERT INTO PROCEDIMENTO (codigo, nome, custo) VALUES (7, 'Cirurgia geral', 3000);
INSERT INTO PROCEDIMENTO (codigo, nome, custo) VALUES (8, 'Tratamento intensivo', 1000);
INSERT INTO PROCEDIMENTO (codigo, nome, custo) VALUES (9, 'Tratamento cardíaco', 2500);
INSERT INTO PROCEDIMENTO (codigo, nome, custo) VALUES (10, 'Tratamento neurológico', 2000);


-- INSERIR ESTADIA

INSERT INTO ESTADIA (codigo, data_inicial, data_final, FK_PACIENTE_cpf, FK_QUARTO_numero_quarto) 
VALUES (1, '2023-02-06', '2023-02-10', '12345678901', 101);

INSERT INTO ESTADIA (codigo, data_inicial, data_final, FK_PACIENTE_cpf, FK_QUARTO_numero_quarto)
VALUES (2, '2022-02-01', '2022-02-03', '23456789012', 102);

INSERT INTO ESTADIA (codigo, data_inicial, data_final, FK_PACIENTE_cpf, FK_QUARTO_numero_quarto)
VALUES (3, '2022-03-01', '2022-03-07', '34567890123', 103);

INSERT INTO ESTADIA (codigo, data_inicial, data_final, FK_PACIENTE_cpf, FK_QUARTO_numero_quarto)
VALUES (4, '2022-04-01', '2022-04-05', '45678901234', 104);

INSERT INTO ESTADIA (codigo, data_inicial, data_final, FK_PACIENTE_cpf, FK_QUARTO_numero_quarto)
VALUES (5, '2022-05-01', '2022-05-10', '56789012345', 105);


-- INSERIR INTERNACAO

INSERT INTO INTERNACAO (codigo, FK_ESTADIA_codigo , FK_ENFERMEIRA_codigo, FK_PROCEDIMENTO_codigo, FK_MEDICO_crm)
VALUES (1,1,4,6,'123456');

INSERT INTO INTERNACAO (codigo, FK_ESTADIA_codigo, FK_ENFERMEIRA_codigo, FK_PROCEDIMENTO_codigo, FK_MEDICO_crm)
VALUES (2,2,4,7,'234567');

INSERT INTO INTERNACAO (codigo, FK_ESTADIA_codigo, FK_ENFERMEIRA_codigo, FK_PROCEDIMENTO_codigo, FK_MEDICO_crm)
VALUES (3,3,5,8,'345678');

INSERT INTO INTERNACAO (codigo, FK_ESTADIA_codigo, FK_ENFERMEIRA_codigo, FK_PROCEDIMENTO_codigo, FK_MEDICO_crm)
VALUES (4,4,6,9,'345678');

INSERT INTO INTERNACAO (codigo, FK_ESTADIA_codigo, FK_ENFERMEIRA_codigo, FK_PROCEDIMENTO_codigo, FK_MEDICO_crm)
VALUES (5,5,7,9,'567890');
