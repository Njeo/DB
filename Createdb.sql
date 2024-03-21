CREATE TABLE ansattStatus
(
    ansattStatusId    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    status            VARCHAR(50)
);

CREATE TABLE person
(
    personId        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    navn            VARCHAR(100),
    epost    VARCHAR(200), 
    ansattStatusId  INTEGER NOT NULL,
    FOREIGN KEY (ansattStatusId) REFERENCES ansattStatus(ansattStatusId)
);

CREATE TABLE teater
(
    sesongId        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    sesongnavn      VARCHAR(50)
);

CREATE TABLE direktor
(
    personId        INTEGER PRIMARY KEY NOT NULL,
    sesongId        INTEGER,
    FOREIGN KEY (personId) REFERENCES person(personId) ON DELETE CASCADE,
    FOREIGN KEY (sesongId) REFERENCES teater(sesongId) ON DELETE CASCADE
);

CREATE TABLE oppgavetype
(
    beskrivelse     VARCHAR(50) PRIMARY KEY NOT NULL
);

CREATE TABLE arbeidsoppgaver
(
    oppgaveId       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    beskrivelse     VARCHAR(50),
    tittel      VARCHAR(512),
    FOREIGN KEY (beskrivelse) REFERENCES oppgavetype(beskrivelse) ON DELETE CASCADE,
    FOREIGN KEY (tittel) REFERENCES teaterstykke(tittel) ON DELETE CASCADE
);


CREATE TABLE ansatt
(   
    personId        INTEGER PRIMARY KEY NOT NULL,
    oppgaveId       INTEGER,
    FOREIGN KEY (personId) REFERENCES person(personId) ON DELETE CASCADE,
    FOREIGN KEY (oppgaveId) REFERENCES arbeidsoppgaver(oppgaveId)
);

CREATE TABLE sal
(
    salId       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    salnavn     VARCHAR(50),
    antallSeter INTEGER,
    antallRader INTEGER
);

CREATE TABLE omraade
(
    omraadeId    INTEGER NOT NULL,
    salId       INTEGER NOT NULL,
    omraadenavn  VARCHAR(50),
    PRIMARY KEY (salId, omraadeId),
    FOREIGN KEY (salId) REFERENCES sal(salId) ON DELETE CASCADE
);

CREATE TABLE sete
(   
    seteId      INTEGER NOT NULL,
    seteNr      INTEGER,
    salId       INTEGER,
    radNr       INTEGER,
    omraadeId    INTEGER,
    PRIMARY KEY (seteId, salId)
    FOREIGN KEY (salId) REFERENCES sal(salId) ON DELETE CASCADE,
    FOREIGN KEY (omraadeId) REFERENCES omraade(omraadeId)
);

CREATE TABLE teaterstykke
(
    tittel      VARCHAR(512) PRIMARY KEY NOT NULL,
    salId       INTEGER,
    antallAkter INTEGER,
    FOREIGN KEY (salId) REFERENCES sal(salId) ON DELETE CASCADE
);

CREATE TABLE skuespiller
(
    personId        INTEGER PRIMARY KEY NOT NULL,
    tittel          VARCHAR(512),
    FOREIGN KEY (personId) REFERENCES person(personId) ON DELETE CASCADE,
    FOREIGN KEY (tittel) REFERENCES teaterstykke(tittel)
);

CREATE TABLE prisklasse
(
    prisklasseNavn  VARCHAR(50),
    tittel          VARCHAR(512),
    pris            INTEGER,
    PRIMARY KEY (tittel, prisklasseNavn),
    FOREIGN KEY (tittel) REFERENCES teaterstykke(tittel) ON DELETE CASCADE
);

CREATE TABLE kunde
(
    kundeId         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    mobilnummer     INTEGER,
    navn            VARCHAR(100),
    adresse         VARCHAR(256)
);

CREATE TABLE billettkjop
(
    kjopsreferanse  INTEGER NOT NULL,
    kundeId         INTEGER NOT NULL,
    kjopstidspunkt  TIMESTAMP CURRENT_TIMESTAMP,
    billettantall   INTEGER,
    totalpris       INTEGER,
    forestillingId INTEGER NOT NULL,
    PRIMARY KEY (kjopsreferanse),
    FOREIGN KEY (kundeId) REFERENCES kunde(kundeId),
    FOREIGN KEY (forestillingId) REFERENCES forestilling(forestillingId)
);

CREATE TABLE billett
(
    billettId       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    tittel          VARCHAR(512),
    prisklasseNavn  VARCHAR(50),
    seteId          INTEGER,
    kjopsreferanse  INTEGER,
    FOREIGN KEY (tittel) REFERENCES prisklasse(tittel),
    FOREIGN KEY (prisklasseNavn) REFERENCES prisklasse(prisklasseNavn),
    FOREIGN KEY (seteId) REFERENCES sete(seteId),
    FOREIGN KEY (kjopsreferanse) REFERENCES billettkjøp(kjopsreferanse) ON DELETE CASCADE
);

CREATE TABLE forestilling
(
    forestillingId  INTEGER PRIMARY KEY NOT NULL,
    tittel          VARCHAR(256),
    spilledato      DATE,
    klokkeslett     TIME,
    FOREIGN KEY (tittel) REFERENCES teaterstykke(tittel) ON DELETE CASCADE
);

CREATE TABLE akt
(
    aktNr           INTEGER NOT NULL,
    tittel          VARCHAR(256),
    aktNavn         VARCHAR(256),
    PRIMARY KEY (aktNr, tittel),
    FOREIGN KEY (tittel) REFERENCES teaterstykke(tittel) ON DELETE CASCADE
);

CREATE TABLE rolle
(
    rolleId         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    personId        INTEGER,
    aktNr           INTEGER,
    rollenavn       VARCHAR(256),
    FOREIGN KEY (personId) REFERENCES person(personId),
    FOREIGN KEY (aktNr) REFERENCES akt(aktNr)
);
