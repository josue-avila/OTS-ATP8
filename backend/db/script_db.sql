CREATE TABLE seller (
	id serial NOT NULL,
	nome varchar(150) NOT NULL,
	telefone varchar(20) NOT NULL,
    email varchar(100) NOT NULL
	CONSTRAINT seller_pk PRIMARY KEY (id)
);

CREATE TABLE marketplace (
	id serial NOT NULL,
	nome varchar(150) NOT NULL,
	descricao varchar(200) NULL,
	CONSTRAINT marketplace_pk PRIMARY KEY (id)
);

CREATE TABLE produto (
	id serial NOT NULL,
	nome varchar(150) NOT NULL,
	descricao varchar(200) NULL,
    preco money NOT NULL
	CONSTRAINT produto_pk PRIMARY KEY (id)
);

CREATE TABLE categoria (
	id serial NOT NULL,
	nome varchar(150) NOT NULL,
	descricao varchar(200) NULL,
	CONSTRAINT categoria_pk PRIMARY KEY (id)
);

CREATE TABLE logs (
	id serial NOT NULL,
	operacao varchar(20) not null,
	descricao varchar(300) NOT NULL,
	CONSTRAINT logs_pk PRIMARY KEY (id)
);