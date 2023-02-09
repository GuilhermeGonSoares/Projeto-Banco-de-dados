use hospital;


/* ER-SistemaHospitalar: */

CREATE TABLE PACIENTE (
    cpf varchar(11) PRIMARY KEY,
    nome varchar(255),
    endereco varchar(255),
    telefone varchar(20)
);

CREATE TABLE MEDICO (
    crm varchar(12) PRIMARY KEY,
    nome varchar(255),
    telefone varchar(20),
    endereco varchar(255),
    FK_ESPECIALIZACAO_codigo int
);

CREATE TABLE ENFERMEIRA (
    codigo int PRIMARY KEY,
    nome varchar(255),
    telefone varchar(20)
);

CREATE TABLE PRESCRICAO (
    data date,
    codigo_consulta int,
    codigo int PRIMARY KEY
);

CREATE TABLE tipo_EXAME (
    valor decimal,
    codigo_exame int PRIMARY KEY,
    validade date,
    nome_exame varchar(255)
);

CREATE TABLE ESPECIALIZACAO (
    tipo_da_especializacao varchar(255),
    codigo int PRIMARY KEY
);

CREATE TABLE tipo_MEDICACAO (
    codigo_medicamento int PRIMARY KEY,
    nome_do_medicamento varchar(255)
);

CREATE TABLE PROCEDIMENTO (
    codigo int PRIMARY KEY,
    nome varchar(255),
    custo decimal
);

CREATE TABLE INTERNACAO (
    codigo int PRIMARY KEY,
    FK_ESTADIA_codigo int,
    FK_ENFERMEIRA_codigo int,
    FK_PROCEDIMENTO_codigo int,
    FK_MEDICO_crm varchar(12)
);

CREATE TABLE ESTADIA (
    codigo int PRIMARY KEY,
    data_inicial date,
    data_final date,
    FK_PACIENTE_cpf varchar(11),
    FK_QUARTO_numero_quarto int
);

CREATE TABLE QUARTO (
    disponivel boolean,
    numero_quarto int PRIMARY KEY,
    andar int
);

CREATE TABLE CONSULTA (
	codigo int PRIMARY KEY AUTO_INCREMENT,
    fk_MEDICO_crm varchar(12),
    fk_PACIENTE_cpf varchar(11),
    data date,
    valor decimal,
    plano_saude boolean
);

CREATE TABLE EXAME (
    FK_tipo_EXAME_codigo_exame int,
    FK_PRESCRICAO_codigo int,
    codigo int PRIMARY KEY
);

CREATE TABLE MEDICACAO (
    FK_tipo_MEDICACAO_codigo_medicamento int,
    dose varchar(255),
    FK_PRESCRICAO_codigo int,
    codigo int PRIMARY KEY
);

CREATE TABLE ADMINISTRADOR (
	id int PRIMARY KEY,
	email varchar(255) UNIQUE,
	senha varchar(255)
);


ALTER TABLE MEDICO ADD CONSTRAINT FK_MEDICO_2
    FOREIGN KEY (FK_ESPECIALIZACAO_codigo)
    REFERENCES ESPECIALIZACAO (codigo);
 
ALTER TABLE PRESCRICAO ADD CONSTRAINT FK_PRESCRICAO_1
    FOREIGN KEY (codigo_consulta)
    REFERENCES CONSULTA (codigo)
    ON DELETE CASCADE;
 
 
ALTER TABLE INTERNACAO ADD CONSTRAINT FK_INTERNACAO_2
    FOREIGN KEY (FK_ESTADIA_codigo)
    REFERENCES ESTADIA (codigo)
    ON DELETE CASCADE;
 
ALTER TABLE INTERNACAO ADD CONSTRAINT FK_INTERNACAO_3
    FOREIGN KEY (FK_ENFERMEIRA_codigo)
    REFERENCES ENFERMEIRA (codigo)
    ON DELETE CASCADE;
 
ALTER TABLE INTERNACAO ADD CONSTRAINT FK_INTERNACAO_4
    FOREIGN KEY (FK_PROCEDIMENTO_codigo)
    REFERENCES PROCEDIMENTO (codigo)
    ON DELETE CASCADE;
 

ALTER TABLE INTERNACAO ADD CONSTRAINT FK_INTERNACAO_6
    FOREIGN KEY (FK_MEDICO_crm)
    REFERENCES MEDICO (crm)
    ON DELETE CASCADE;
 
ALTER TABLE ESTADIA ADD CONSTRAINT FK_LEITO_FICAR_2
    FOREIGN KEY (FK_PACIENTE_cpf)
    REFERENCES PACIENTE (cpf)
    ON DELETE CASCADE;
 
ALTER TABLE ESTADIA ADD CONSTRAINT FK_LEITO_FICAR_3
    FOREIGN KEY (FK_QUARTO_numero_quarto)
    REFERENCES QUARTO (numero_quarto)
    ON DELETE CASCADE;
 
ALTER TABLE CONSULTA ADD CONSTRAINT FK_consulta_1
    FOREIGN KEY (fk_MEDICO_crm)
    REFERENCES MEDICO (crm)
    ON DELETE RESTRICT;
 
ALTER TABLE CONSULTA ADD CONSTRAINT FK_consulta_2
    FOREIGN KEY (fk_PACIENTE_cpf)
    REFERENCES PACIENTE (cpf)
    ON DELETE CASCADE;
 
ALTER TABLE EXAME ADD CONSTRAINT FK_exame_1
    FOREIGN KEY (FK_tipo_EXAME_codigo_exame)
    REFERENCES tipo_EXAME (codigo_exame)
    ON DELETE SET NULL;
 
ALTER TABLE EXAME ADD CONSTRAINT FK_exame_2
    FOREIGN KEY (FK_PRESCRICAO_codigo)
    REFERENCES PRESCRICAO (codigo);
 
ALTER TABLE MEDICACAO ADD CONSTRAINT FK_medicacao_1
    FOREIGN KEY (FK_tipo_MEDICACAO_codigo_medicamento)
    REFERENCES tipo_MEDICACAO (codigo_medicamento)
    ON DELETE SET NULL;
 
ALTER TABLE MEDICACAO ADD CONSTRAINT FK_medicacao_2
    FOREIGN KEY (FK_PRESCRICAO_codigo)
    REFERENCES PRESCRICAO (codigo);
    
   
   