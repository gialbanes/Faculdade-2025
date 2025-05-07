/*Criando Ambiente Data Warehouse*/
create database if not exists hoteldallasDW;
use hoteldallasDW;
 
/*Criando Tabelas Dimensão*/
 
-- Tabela DimCliente
CREATE TABLE DimCliente (
    ID_Cliente INT PRIMARY KEY,
    Nome VARCHAR(100),
    Idade INT,
    Pais_Origem VARCHAR(50)
);
 
-- Tabela DimReserva
CREATE TABLE DimReserva (
    ID_Reserva INT PRIMARY KEY,
    Data_Entrada DATE,
    Data_Saida DATE,
    Numero_Noites INT
);
 
-- Tabela DimQuarto
CREATE TABLE DimQuarto (
    ID_Quarto INT PRIMARY KEY,
    Tipo_Quarto VARCHAR(50),
    Andar INT,
    Preco_Diaria DECIMAL(10, 2)
);
 
 
-- Tabela DimTempo
CREATE TABLE DimTempo (
    ID_Tempo INT PRIMARY KEY,
    Data DATE,
    Ano INT,
    Mes INT,
    Trimestre INT,
    Dia_Semana VARCHAR(10)
);
 
-- Tabela DimServico
CREATE TABLE DimServico (
    ID_Servico INT PRIMARY KEY,
    Nome_Servico VARCHAR(100),
    Categoria VARCHAR(50),
    Preco DECIMAL(10, 2)
);

-- Tabela de Ocupações na Produção (fato transacional)
CREATE TABLE FatoOcupacoes (
    ID_Ocupacao INT PRIMARY KEY,
    ID_Cliente INT,
    ID_Reserva INT,
    ID_Quarto INT,
    Data DATE,
    ID_Servico INT,
    Quantidade INT,
    Valor_Total DECIMAL(10, 2),
    FOREIGN KEY (ID_Cliente) REFERENCES DimCliente(ID_Cliente),
    FOREIGN KEY (ID_Reserva) REFERENCES DimReserva(ID_Reserva),
    FOREIGN KEY (ID_Quarto) REFERENCES DimQuarto(ID_Quarto),
    FOREIGN KEY (ID_Servico) REFERENCES DimServico(ID_Servico)
);

-- Processo de ETL - Transferindo os dados da produção para o DW
-- Extrair e inserir dado na DimCliente
-- já estamos no HtelDallasDW
select * from dimCliente;

-- aqui o normal seria com values
-- estou populando a minha dimensão clientes com os dados da tabela clientes da produção
insert into DimCliente (id_cliente, nome, idade, pais_origem) select id_cliente, nome, idade, pais from hotelDallasProd.clientes;

-- extraindo e inserindo dados da DimReserva
-- no DW não tem id_cliente, mas na prod tem -> mas puxo só oq vou querer para o DW
select * from DimReserva;
insert into DimReserva (id_reserva, data_entrada, data_saida, numero_noites) select id_reserva, data_entrada, data_saida, numero_noites from hotelDallasProd.reservas;

-- extraindo e inserindo dados da DimQuarto
select * from DimQuarto;
insert into DimQuarto (id_quarto, tipo_quarto, andar, preco_diaria) select id_quarto, tipo_quarto, andar, preco_diaria from hotelDallasProd.quartos;

-- Extraindo e inserindo dado na DimTempo
-- função responsável por indexar as datas
-- faço a inserção das datas do prod de forma ordenada para alimentar o id_tempo de maneira organizada
select * from DimTempo;
insert into dimTempo (id_tempo, data, ano, mes, trimestre, dia_semana) select row_number() over(order by Data) as id_tempo, data, year(data) as ano, month(data) as mes, quarter(data) as trimestre, dayname(data) as dia_semana 
from(
	select distinct data from hoteldallasprod.ocupacoes
) as t;

select * from hoteldallasprod.ocupacoes;