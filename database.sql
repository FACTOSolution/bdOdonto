CREATE TABLE ALUNO (
nome
VARCHAR(50)
NOT NULL,
matricula
NUMERIC(11)
NOT NULL,
lsigaa
VARCHAR(20)
not null,
ssigaa
varchar(20)
not null,
PRIMARY KEY (matricula)
)

CREATE TABLE PROFESSOR (
nome
varchar(50)
not null,
code
numeric(11),
lsigaa
VARCHAR(20),
ssigaa
varchar(20),
primary key (code)
)

CREATE TABLE FICHAS (
code
int,
nome
varchar(20),
primary key (code)
)

CREATE TABLE TURMA (
code
char(7),
nome
varchar(30),
prof
numeric(11),
ficha
int,
primary key (code),
foreign key (prof) references PROFESSOR (code),
foreign key (ficha) references FICHAS (code)
)

CREATE TABLE TURMA_ALUNO (
code
int,
periodo
char(6),
codeT
char(7),
matriculaA
numeric(11),
PRIMARY KEY (code),
foreign key (codeT) references TURMA (code),
foreign key (matriculaA) references ALUNO (matricula)
)
	
CREATE TABLE PACIENTE (
nome
varchar(50),
cpf
char(11),
genero
varchar(10),
data
date,
telefone
numeric(11),
nasc
date,
profissao
varchar(20),
nomep
varchar(50),
nomem
varchar(50),
estado
varchar(20),
cidade
varchar(30),
bairro
varchar(20),
rua
varchar(30),
numero
int,
PRIMARY KEY (cpf)
)

CREATE TABLE ATENDIMENTO (
code
int,
data
date,
cpfP
char(11),
codeTA
int,
codeF
int,
PRIMARY KEY (code),
foreign key (codeTA) references TURMA_ALUNO (code),
foreign key (codeF) references FICHAS (code),
foreign key (cpfP) references PACIENTE (cpf)
)

CREATE TABLE FICHA_TURMA (
codeF
int,
codeT
char(7),
foreign key (codeF) references FICHAS (code),
foreign key (codeT) references TURMA (code)
)

CREATE TABLE FICHA_PERIO (
codeA
int
NOT NULL,
p1
boolean,
p2
boolean,
p3 
boolean,
p4
boolean,
p51
boolean,
p52 
boolean,
p53
boolean,
p54
boolean,
p55
varchar(50),
p6
boolean,
p61
varchar(50),
p7
boolean,
p71
varchar(50),
p8
boolean,
p81
varchar(50),
p91
boolean,
p92 
boolean,
p93
boolean,
p94
boolean,
p95
boolean,
p96 
boolean,
p97
boolean,
p98
boolean,
p99
boolean,
p910
boolean,
p911
boolean,
p10
boolean,
p101
varchar(50),
p11
boolean,
p111
boolean,
p12
boolean,
p121
varchar(50),
p122
varchar(20),
p13
boolean,
p131
boolean,
p14
boolean,
p15
boolean,
p16
boolean,
p161
varchar(10),
p162
varchar(3),
p17
boolean,
p171
varchar(30),
p18
boolean,
p19
int,
#odontograma
p20
boolean,
p21
boolean,
p211
int,
p22
boolean,
p221
int,
foreign key (codeA) references ATENDIMENTO (code)
)

CREATE TABLE FICHA_DIAGNOSTICO (
codeA
int
NOT NULL,
p1
varchar(50),
p2
varchar(100),
p3
varchar(20),
p4
varchar(20),
p5
int,
p6
int,
p7
boolean,
p8
boolean,
p9
boolean,
p10
boolean,
p11
boolean,
p12
boolean,
p13
boolean,
p14
boolean,
p15
boolean,
p16
boolean,
p17
boolean,
p171
varchar(20),
p172
varchar(20),
p173
varchar(20),
p18
boolean,
p19
boolean,
p20
boolean,
p201
varchar(20),
p21
boolean,
p211
varchar(20),
p22
boolean,
p23
boolean,
p231
varchar(20),
p24
boolean,
p25
boolean,
p26
boolean,
p261
varchar(20),
p27
boolean,
p271
varchar(20),
p28
boolean,
p281
boolean,
p29
boolean,
p291
boolean,
p30
boolean,
p301
int,
p31
boolean,
p32
boolean,
p33
boolean,
p34
boolean,
p35
boolean,
p36
boolean,
p37
boolean,
p371
varchar(20),
p38
boolean,
p381
varchar(20),
p39
boolean,
p391
varchar(20),
p40
boolean,
p41
boolean,
p42
boolean,
p43
boolean,
p44
boolean,
p45
boolean,
p46
boolean,
p47
boolean,
p471
varchar(20),
p48
boolean,
p481
varchar(20),
pe1
varchar(50),
pe2
varchar(50),
pe3
varchar(50),
pe4
varchar(50),
pe5
varchar(50),
pi1
varchar(50),
pi2
varchar(50),
pi3
varchar(50),
pi4
varchar(50),
pi5
varchar(50),
pi6
varchar(50),
pi7
varchar(50),
pper
varchar(50),
pexam
varchar(100),
#ODONTOGRAMA
pn1
varchar(50),
pn2
varchar(50),
pn3
varchar(50),
pn4
varchar(50),
pn5
varchar(50),
pf
varchar(20),
foreign key (codeA) references ATENDIMENTO (code)
)

CREATE TABLE FICHA_PPR (
codeA
int
NOT NULL,
p1
varchar(20),
p2
varchar(100),
p3
varchar(100),
p4
varchar(20),
p5
varchar(20),
p6
varchar(100),
p7
varchar(100),
p8
varchar(20),
foreign key (codeA) references ATENDIMENTO (code)
)

CREATE TABLE FICHA_ORTODONTIA (
codeA
int
NOT NULL,
pana1
varchar(20),
pana2
int,
pana3
int,
pana4
int,
pana41
varchar(20),
pana5
boolean,
pana6
int,
pana7
int,
pana71
varchar(20),
pana8
int,
pana9
int,
pana91
varchar(20),
pana10
varchar(50),
ppsi
int,
pfront1
boolean,
pfront2
int,
pfront3
boolean,
pfront4
int,
pfront5
int,
pfront6
int,
pfront7
int,
pfront8
int,
pfront9
varchar(50),
pfs1
boolean,
pfs2
int,
pfs3
int,
pfs4
varchar(50),
pper1
int,
pper2
int,
pper3
int,
pper4
boolean,
pper5
int,
pper6
varchar(20),
pper7
int,
pper8
varchar(20),
pper9
int,
pper10
int,
pper11
varchar(20),
pper12
int,
pper13
varchar(50),
pfun1
int,
pfun2
boolean,
pfun3
boolean,
pfun4
int,
pfun5
varchar(20),
pfun6
varchar(20),
poc1
int,
poc2
int,
poc3
int,
poc4
int,
poc5
int,
poc6
int,
poc7
int,
poc8
int,
poc9
int,
poc10
boolean,
poc11
boolean,
poc12
int,
poc13
int,
poc14
int,
poc15
int,
poc16
int,
poc17
int,
poc18
boolean,
poc19
varchar(50),
obs
varchar(50),
penc
int,
foreign key (codeA) references ATENDIMENTO (code)
)


CREATE TABLE FICHA_URGENCIA (
codeA
int
NOT NULL,
p1
varchar(50),
p2
varchar(50),
p3
varchar(50),
p4
varchar(50),
p5
varchar(20),
p6
varchar(50),
p7
varchar(50),
p8
varchar(50),
p9
varchar(20),
foreign key (codeA) references ATENDIMENTO (code)
)

CREATE TABLE FICHA_EXEMPLO (
codeA
int
NOT NULL,
foreign key (codeA) references ATENDIMENTO (code)
)