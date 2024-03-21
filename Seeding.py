import datetime as dt
import sqlite3

def seed_ansattstatus(dbpath, status):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        for stat in status:
            cur.execute("INSERT INTO ansattStatus (status) VALUES (?)", (stat,))

def seed_person(dbpath, personer):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        for person in personer:
            cur.execute("INSERT INTO person (ansattStatusId, navn, epost) VALUES (?,?,?)", person)

def seed_akt(dbpath, acts_data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        for act in acts_data:
            cur.execute("INSERT INTO akt (aktNr, tittel, aktNavn) VALUES (?,?,?)", act)

def seed_skuespiller(dbpath, actors_data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        for actor in actors_data:
            cur.execute("INSERT INTO skuespiller (tittel, personId) VALUES (?,?)", actor)

def seed_rolle(dbpath, roles):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        for role in roles:
            cur.execute("INSERT INTO rolle (personId, aktNr, rollenavn) VALUES (?,?,?)", role)


def seed_sal(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO sal (salnavn, antallSeter, antallRader) VALUES (?,?,?)",
                (data[0], data[1], data[2]))
    
    conn.commit()
    conn.close()

def seed_teaterstykke(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO teaterstykke (tittel, antallAkter, salId) VALUES (?,?,?)",
                (data[0], data[1], data[2]))

    conn.commit()
    conn.close()


def seed_direktør(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO direktor (sesongId, personId) VALUES (?,?)",
                (data[0], data[1]))
    
    conn.commit()
    conn.close()


def seed_teater(dbpath,data ):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO teater (sesongnavn) VALUES (?)",
                (data[0]))
    conn.commit()
    conn.close()

def seed_arbeidsoppgave(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO arbeidsoppgaver (beskrivelse, tittel) VALUES (?,?)",
                (data[0], data[1]))
    
    conn.commit()
    conn.close()
    

def seed_oppgavetype(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
    

    cur.execute("INSERT INTO oppgavetype (beskrivelse) VALUES (?)",
                (data))
    
    conn.commit()
    conn.close()


def seed_område(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute('INSERT INTO omraade (omraadeId, omraadenavn, salId) VALUES (?,?,?)',
                (data[0], data[1], data[2]))
    
    conn.commit()
    conn.close() 


def seed_sete(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO sete (seteId, seteNr, salId, radNr, omraadeId) VALUES (?,?,?,?,?)",
                    (data[0], data[1], data[2], data[3], data[4]))
        conn.commit()

def seed_prisklasse(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO prisklasse (prisklasseNavn, tittel, pris) VALUES (?,?,?)",
                (data[0], data[1], data[2]))
    
    conn.commit()
    conn.close()

def seed_kunde(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO kunde (mobilnummer, navn, adresse) VALUES (?,?,?)",
                (data[0], data[1], data[2]))

    conn.commit()
    conn.close()

def seed_billettkjøp(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO billettkjop (kjopsreferanse, kundeId, kjopstidspunkt, billettantall, totalpris, forestillingId) VALUES (?,?,?,?,?,?)",
                (data[0], data[1], data[2], data[3], data[4], data[5]))

    conn.commit()
    conn.close()

def seed_billett(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO billett (tittel, prisklasseNavn, seteId, kjopsreferanse) VALUES (?,?,?,?)",
                (data[0], data[1], data[2], data[3]))

    conn.commit()
    conn.close()

def seed_forestilling(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO forestilling (tittel, spilledato, klokkeslett) VALUES (?,?,?)",
                (data[0], data[1], data[2]))

    conn.commit()
    conn.close()

def seed_akt(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO akt (aktNr, tittel, aktNavn) VALUES (?,?,?)",
                (data[0], data[1], data[2]))

    conn.commit()
    conn.close()

def seed_ansatt(dbpath,data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
    
    cur.execute("INSERT INTO ansatt (personId, oppgaveId) VALUES (?,?)",
                (data[0],data[1]))
    
    conn.commit()
    conn.close()


def seed_data(dbpath):
    saler = [
        ("Hovedscenen", 516, 18), 
        ("Gamle scene", 338, 33)
    ]

    områder_hovedscene = [
        (1, "hovedområde", 1), (2, "øvre galleri", 1), (3, "nedre galleri", 1)
    ]

    områder_gamlescene = [
        (1, "parkett", 2), (2, "balkong", 2), (3, "galleri", 2)
    ]

    
    status = [
        "deltid", "fulltid", "innleid"]

    personer = [
        (1, 'Ola', 'Ola@example.com'),
        (2, 'Helene', 'helene@example.com'),
        (1, 'Iver', 'iver@example.com'),
        (1, 'Julia', 'julia@example.com'),
        (2, 'Alexander', 'alexander@example.com'),
        (1, 'Caroline', 'caroline@example.com'),
        (2, 'Erling', 'erling@example.com'),
        (1, 'Markus', 'markus@example.com'),
        (1, 'Martin', 'martin@example.com'),
        (2, 'Kari', 'kari@example.com'),
        (2, 'Stefan', 'stefan@example.com'),
        (1, 'Håkon', 'håkon@example.com'),
        (1, 'Kristoffer', 'miles@example.com'),
        (2, 'Selma', 'selma@example.com'),
        (2,"Dikt Tøresen","dikt@example.com"),
        (2,"Ann settelsen", "Ann@example.com"),
        (3, "Ida", "ida@example.com"),
        (2, "Frida", "frida@example.com"),
        (1, "Isabella", "isabella@example.com"),
        (3, "Isabelle", "isabelle@example.com"),
        (3, "Mads", "mads@example.com"),
        (1, "Mats", "mats@example.com"),
        (2, "Marius", "marius@example.com"),
        (2, "Magnus", "magnus@example.com"),

        (3, "Anne", "anne@example.com"),
        (2, "Anette", "anette@example.com"),
        (1, "Anine", "anine@example.com"),
        (2, "Annie", "annie@example.com"),
        (3, "Anne Grete", "annegrete@example.com"),
        (2, "Anita", "anita@example.com"),
        (1, "Arnold", "arnold@example.com"),
        (2, "Arne", "arne@example.com"),
        (3, "Andreas", "andreas@example.com"),
    ]

    roles = [
        (1, 1, "Håkon Håkonson"),
        (1, 2, "Håkon Håkonson"),
        (1, 3, "Håkon Håkonson"),
        (1, 4, "Håkon Håkonson"),
        (1, 5, "Håkon Håkonson"),
        (2, 1, "Dagfinn Bonde"),
        (2, 2, "Dagfinn Bonde"),
        (2, 3, "Dagfinn Bonde"),
        (2, 4, "Dagfinn Bonde"),
        (2, 5, "Dagfinn Bonde"),
        (3, 4, "Jatgeir Skald"),
        (4, 1, "Sigrid"),
        (4, 2, "Sigrid"),
        (4, 5, "Sigrid"),
        (5, 4, "Ingeborg"),
        (6, 1, "Guttorm Ingesson"),
        (7, 1, "Skule Jarl"),
        (7, 2, "Skule Jarl"),
        (7, 3, "Skule Jarl"),
        (7, 4, "Skule Jarl"),
        (7, 5, "Skule Jarl"),
        (8, 1, "Inga frå Vartejg"),
        (8, 3, "Inga frå Vartejg"),
        (9, 1, "Paal Flida"),
        (9, 2, "Paal Flida"),
        (9, 3, "Paal Flida"),
        (9, 4, "Paal Flida"),
        (9, 5, "Paal Flida"),
        (10, 1, "Ragnhild"),
        (10, 5, "Ragnhild"),
        (11, 1, "Gregorius Jonsson"),
        (11, 2, "Gregorius Jonsson"),
        (11, 3, "Gregorius Jonsson"),
        (11, 4, "Gregorius Jonsson"),
        (11, 5, "Gregorius Jonsson"),
        (12, 1, "Margrete"),
        (12, 2, "Margrete"),
        (12, 3, "Margrete"),
        (12, 4, "Margrete"),
        (12, 5, "Margrete"),
        (13, 1, "Biskop Nikolas"),
        (13, 2, "Biskop Nikolas"),
        (13, 3, "Biskop Nikolas"),
        (14, 3, "Peter"),
        (14, 4, "Peter"),
        (14, 5, "Peter"),
    ]
    
    acts_data = [
        (1, 0, 'Akt1'),
        (2, 0, 'Akt2'),
        (3, 0, 'Akt3'),
        (4, 0, 'Akt4'),
        (5, 0, 'Akt5'),
        (1, 1, 'Akt1'),
        (2, 1, 'Akt2'),
        (3, 1, 'Akt3'),
        (4, 1, 'Akt4'),
        (5, 1, 'Akt5'),
        (4, 2, 'Akt4'),
        (1, 3, 'Akt1'),
        (2, 3, 'Akt2'),
        (5, 3, 'Akt5'),
        (4, 4, 'Akt4'),
        (1, 5, 'Akt1'),
        (1, 6, 'Akt1'),
        (2, 6, 'Akt2'),
        (3, 6, 'Akt3'),
        (4, 6, 'Akt4'),
        (5, 6, 'Akt5'),
        (1, 7, 'Akt1'),
        (3, 7, 'Akt3'),
        (1, 8, 'Akt1'),
        (2, 8, 'Akt2'),
        (3, 8, 'Akt3'),
        (4, 8, 'Akt4'),
        (5, 8, 'Akt5'),
        (1, 9, 'Akt1'),
        (5, 9, 'Akt5'),
        (1, 10, 'Akt1'),
        (2, 10, 'Akt2'),
        (3, 10, 'Akt3'),
        (4, 10, 'Akt4'),
        (5, 10, 'Akt5'),
        (1, 11, 'Akt1'),
        (2, 11, 'Akt2'),
        (3, 11, 'Akt3'),
        (4, 11, 'Akt4'),
        (5, 11, 'Akt5'),
        (1, 12, 'Akt1'),
        (2, 12, 'Akt2'),
        (3, 12, 'Akt3'),
        (3, 13, 'Akt3'),
        (4, 13, 'Akt4'),
        (5, 13, 'Akt5')
    ]
    
    actors_data = [
        ("Kongsemnene", 0),
        ("Kongsemnene", 1),
        ("Kongsemnene", 2),
        ("Kongsemnene", 3),
        ("Kongsemnene", 4),
        ("Kongsemnene", 5),
        ("Kongsemnene", 6),
        ("Kongsemnene", 7),
        ("Kongsemnene", 8),
        ("Kongsemnene", 9),
        ("Kongsemnene", 10),
        ("Kongsemnene", 11),
        ("Kongsemnene", 12),
        ("Kongsemnene", 13)
    ]

    oppgavetyper = [
        ("musiker"),
        ("regissør"),
        ("scenografiansvarlig"),
        ("ansvarlig for kostymedesign"),
        ("koreograf"),
        ("ansvarlig for musikk og lyddesign"),
        ("dramaturg"),
        ("sufflør"),
        ("regnskap")
    ]

    teaterstykker = [
        ("Kongsemnene",5,1),
        ("Størst av alt er kjærligheten",1,2)
    ]

    kunder = [
        (45397121,"Marius Gisleberg","Tormods gate 3A"),
        (47266475, "Leo Yuen", "Klostergata 29A"),
    ]

    seter_hovedscene = [
        (1, 1, 1, 1, 1), (2, 2, 1, 1, 1), (3, 3, 1, 1, 1), (4, 4, 1, 1, 1), (5, 5, 1, 1, 1), (6, 6, 1, 1, 1), (7, 7, 1, 1, 1),
                        (8, 8, 1, 1, 1), (9, 9, 1, 1, 1), (10, 10, 1, 1, 1), (11, 11, 1, 1, 1), (12, 12, 1, 1, 1), (13, 13, 1, 1, 1), (14, 14, 1, 1, 1),
                        (15, 15, 1, 1, 1), (16, 16, 1, 1, 1), (17, 17, 1, 1, 1), (18, 18, 1, 1, 1), (19, 19, 1, 1, 1), (20, 20, 1, 1, 1), (21, 21, 1, 1, 1), (22, 22, 1, 1, 1), (23, 23, 1, 1, 1), (24, 24, 1, 1, 1), (25, 25, 1, 1, 1), (26, 26, 1, 1, 1), (27, 27, 1, 1, 1), (28, 28, 1, 1, 1), (29, 29, 1, 2, 1), (30, 30, 1, 2, 1), (31, 31, 1, 2, 1), (32, 32, 1, 2, 1), (33, 33, 1, 2, 1), (34, 34, 1, 2, 1), (35, 35, 1, 2, 1), (36, 36, 1, 2, 1), (37, 37, 1, 2, 1), (38, 38, 1, 2, 1), (39, 39, 1, 2, 1), (40, 40, 1, 2, 1), (41, 41, 1, 2, 1), (42, 42, 1, 2, 1), (43, 43, 1, 2, 1), (44, 44, 1, 2, 1), (45, 45, 1, 2, 1), (46, 46, 1, 2, 1), (47, 47, 1, 2, 1), (48, 48, 1, 2, 1), (49, 49, 1, 2, 1), (50, 50, 1, 2, 1), (51, 51, 1, 2, 1), (52, 52, 1, 2, 1), (53, 53, 1, 2, 1), (54, 54, 1, 2, 1), (55, 55, 1, 2, 1), (56, 56, 1, 2, 1), (57, 57, 1, 3, 1), (58, 58, 1, 3, 1), (59, 59, 1, 3, 1), (60, 60, 1, 3, 1), (61, 61, 1, 3, 1), (62, 62, 1, 3, 1), (63, 63, 1, 3, 1), (64, 64, 1, 3, 1), (65, 65, 1, 3, 1), (66, 66, 1, 3, 1), (67, 67, 1, 3, 1), (68, 68, 1, 3, 1), (69, 69, 1, 3, 1), (70, 70, 1, 3, 1), (71, 71, 1, 3, 1), (72, 72, 1, 3, 1), (73, 73, 1, 3, 1), (74, 74, 1, 3, 1), (75, 75, 1, 3, 1), (76, 76, 1, 3, 1), (77, 77, 1, 3, 1), (78, 78, 1, 3, 1), (79, 79, 1, 3, 1), (80, 80, 1, 3, 1), (81, 81, 1, 3, 1), (82, 82, 1, 3, 1), (83, 83, 1, 3, 1), (84, 84, 1, 3, 1), (85, 85, 1, 4, 1), (86, 86, 1, 4, 1), (87, 87, 1, 4, 1), (88, 88, 1, 4, 1), (89, 89, 1, 4, 1), (90, 90, 1, 4, 1), (91, 91, 1, 4, 1), (92, 92, 1, 4, 1), (93, 93, 1, 4, 1), (94, 94, 1, 4, 1), (95, 95, 1, 4, 1), (96, 96, 1, 4, 1), (97, 97, 1, 4, 1), (98, 98, 1, 4, 1), (99, 99, 1, 4, 1), (100, 100, 1, 4, 1), (101, 101, 1, 4, 1), (102, 102, 1, 4, 1), (103, 103, 1, 4, 1), (104, 104, 1, 4, 1), (105, 105, 1, 4, 1), (106, 106, 1, 4, 1), (107, 107, 1, 4, 1), (108, 108, 1, 4, 1), (109, 109, 1, 4, 1), (110, 110, 1, 4, 1), (111, 111, 1, 4, 1), (112, 112, 1, 4, 1), (113, 113, 1, 5, 1), (114, 114, 1, 5, 1), (115, 115, 1, 5, 1), (116, 116, 1, 5, 1), (117, 117, 1, 5, 1), (118, 118, 1, 5, 1), (119, 119, 1, 5, 1), (120, 120, 1, 5, 1), (121, 121, 1, 5, 1), (122, 122, 1, 5, 1), (123, 123, 1, 5, 1), (124, 124, 1, 5, 1), (125, 125, 1, 5, 1), (126, 126, 1, 5, 1), (127, 127, 1, 5, 1), (128, 128, 1, 5, 1), (129, 129, 1, 5, 1), (130, 130, 1, 5, 1), (131, 131, 1, 5, 1), (132, 132, 1, 5, 1), (133, 133, 1, 5, 1), (134, 134, 1, 5, 1), (135, 135, 1, 5, 1), (136, 136, 1, 5, 1), (137, 137, 1, 5, 1), (138, 138, 1, 5, 1), (139, 139, 1, 5, 1), (140, 140, 1, 5, 1), (141, 141, 1, 6, 1), (142, 142, 1, 6, 1), (143, 143, 1, 6, 1), (144, 144, 1, 6, 1), (145, 145, 1, 6, 1), (146, 146, 1, 6, 1), (147, 147, 1, 6, 1), (148, 148, 1, 6, 1), (149, 149, 1, 6, 1), (150, 150, 1, 6, 1), (151, 151, 1, 6, 1), (152, 152, 1, 6, 1), (153, 153, 1, 6, 1), (154, 154, 1, 6, 1), (155, 155, 1, 6, 1), (156, 156, 1, 6, 1), (157, 157, 1, 6, 1), (158, 158, 1, 6, 1), (159, 159, 1, 6, 1), (160, 160, 1, 6, 1), (161, 161, 1, 6, 1), (162, 162, 1, 6, 1), (163, 163, 1, 6, 1), (164, 164, 1, 6, 1), (165, 165, 1, 6, 1), (166, 166, 1, 6, 1), (167, 167, 1, 6, 1), (168, 168, 1, 6, 1), (169, 169, 1, 7, 1), (170, 170, 1, 7, 1), (171, 171, 1, 7, 1), (172, 172, 1, 7, 1), (173, 173, 1, 7, 1), (174, 174, 1, 7, 1), (175, 175, 1, 7, 1), (176, 176, 1, 7, 1), (177, 177, 1, 7, 1), (178, 178, 1, 7, 1), (179, 179, 1, 7, 1), (180, 180, 1, 7, 1), (181, 181, 1, 7, 1), (182, 182, 1, 7, 1), (183, 183, 1, 7, 1), (184, 184, 1, 7, 1), (185, 185, 1, 7, 1), (186, 186, 1, 7, 1), (187, 187, 1, 7, 1), (188, 188, 1, 7, 1), (189, 189, 1, 7, 1), (190, 190, 1, 7, 1), (191, 191, 1, 7, 1), (192, 192, 1, 7, 1), (193, 193, 1, 7, 1), (194, 194, 1, 7, 1), (195, 195, 1, 7, 1), (196, 196, 1, 7, 1), (197, 197, 1, 8, 1), (198, 198, 1, 8, 1), (199, 199, 1, 8, 1), (200, 200, 1, 8, 1), (201, 201, 1, 8, 1), (202, 202, 1, 8, 1), (203, 203, 1, 8, 1), (204, 204, 1, 8, 1), (205, 205, 1, 8, 1), (206, 206, 1, 8, 1), (207, 207, 1, 8, 1), (208, 208, 1, 8, 1), (209, 209, 1, 8, 1), (210, 210, 1, 8, 1), (211, 211, 1, 8, 1), (212, 212, 1, 8, 1), (213, 213, 1, 8, 1), (214, 214, 1, 8, 1), (215, 215, 1, 8, 1), (216, 216, 1, 8, 1), (217, 217, 1, 8, 1), (218, 218, 1, 8, 1), (219, 219, 1, 8, 1), (220, 220, 1, 8, 1), (221, 221, 1, 8, 1), (222, 222, 1, 8, 1), (223, 223, 1, 8, 1), (224, 224, 1, 8, 1), (225, 225, 1, 9, 1), (226, 226, 1, 9, 1), (227, 227, 1, 9, 1), (228, 228, 1, 9, 1), (229, 229, 1, 9, 1), (230, 230, 1, 9, 1), (231, 231, 1, 9, 1), (232, 232, 1, 9, 1), (233, 233, 1, 9, 1), (234, 234, 1, 9, 1), (235, 235, 1, 9, 1), (236, 236, 1, 9, 1), (237, 237, 1, 9, 1), (238, 238, 1, 9, 1), (239, 239, 1, 9, 1), (240, 240, 1, 9, 1), (241, 241, 1, 9, 1), (242, 242, 1, 9, 1), (243, 243, 1, 9, 1), (244, 244, 1, 9, 1), (245, 245, 1, 9, 1), (246, 246, 1, 9, 1), (247, 247, 1, 9, 1), (248, 248, 1, 9, 1), (249, 249, 1, 9, 1), (250, 250, 1, 9, 1), (251, 251, 1, 9, 1), (252, 252, 1, 9, 1), (253, 253, 1, 10, 1), (254, 254, 1, 10, 1), (255, 255, 1, 10, 1), (256, 256, 1, 10, 1), (257, 257, 1, 10, 1), (258, 258, 1, 10, 1), (259, 259, 1, 10, 1), (260, 260, 1, 10, 1), (261, 261, 1, 10, 1), (262, 262, 1, 10, 1), (263, 263, 1, 10, 1), (264, 264, 1, 10, 1), (265, 265, 1, 10, 1), (266, 266, 1, 10, 1), (267, 267, 1, 10, 1), (268, 268, 1, 10, 1), (269, 269, 1, 10, 1), (270, 270, 1, 10, 1), (271, 271, 1, 10, 1), (272, 272, 1, 10, 1), (273, 273, 1, 10, 1), (274, 274, 1, 10, 1), (275, 275, 1, 10, 1), (276, 276, 1, 10, 1), (277, 277, 1, 10, 1), (278, 278, 1, 10, 1), (279, 279, 1, 10, 1), (280, 280, 1, 10, 1), (281, 281, 1, 11, 1), (282, 282, 1, 11, 1), (283, 283, 1, 11, 1), (284, 284, 1, 11, 1), (285, 285, 1, 11, 1), (286, 286, 1, 11, 1), (287, 287, 1, 11, 1), (288, 288, 1, 11, 1), (289, 289, 1, 11, 1), (290, 290, 1, 11, 1), (291, 291, 1, 11, 1), (292, 292, 1, 11, 1), (293, 293, 1, 11, 1), (294, 294, 1, 11, 1), (295, 295, 1, 11, 1), (296, 296, 1, 11, 1), (297, 297, 1, 11, 1), (298, 298, 1, 11, 1), (299, 299, 1, 11, 1), (300, 300, 1, 11, 1), (301, 301, 1, 11, 1), (302, 302, 1, 11, 1), (303, 303, 1, 11, 1), (304, 304, 1, 11, 1), (305, 305, 1, 11, 1), (306, 306, 1, 11, 1), (307, 307, 1, 11, 1), (308, 308, 1, 11, 1), (309, 309, 1, 12, 1), (310, 310, 1, 12, 1), (311, 311, 1, 12, 1), (312, 312, 1, 12, 1), (313, 313, 1, 12, 1), (314, 314, 1, 12, 1), (315, 315, 1, 12, 1), (316, 316, 1, 12, 1), (317, 317, 1, 12, 1), (318, 318, 1, 12, 1), (319, 319, 1, 12, 1), (320, 320, 1, 12, 1), (321, 321, 1, 12, 1), (322, 322, 1, 12, 1), (323, 323, 1, 12, 1), (324, 324, 1, 12, 1), (325, 325, 1, 12, 1), (326, 326, 1, 12, 1), (327, 327, 1, 12, 1), (328, 328, 1, 12, 1), (329, 329, 1, 12, 1), (330, 330, 1, 12, 1), (331, 331, 1, 12, 1), (332, 332, 1, 12, 1), (333, 333, 1, 12, 1), (334, 334, 1, 12, 1), (335, 335, 1, 12, 1), (336, 336, 1, 12, 1), (337, 337, 1, 13, 1), (338, 338, 1, 13, 1), (339, 339, 1, 13, 1), (340, 340, 1, 13, 1), (341, 341, 1, 13, 1), (342, 342, 1, 13, 1), (343, 343, 1, 13, 1), (344, 344, 1, 13, 1), (345, 345, 1, 13, 1), (346, 346, 1, 13, 1), (347, 347, 1, 13, 1), (348, 348, 1, 13, 1), (349, 349, 1, 13, 1), (350, 350, 1, 13, 1), (351, 351, 1, 13, 1), (352, 352, 1, 13, 1), (353, 353, 1, 13, 1), (354, 354, 1, 13, 1), (355, 355, 1, 13, 1), (356, 356, 1, 13, 1), (357, 357, 1, 13, 1), (358, 358, 1, 13, 1), (359, 359, 1, 13, 1), (360, 360, 1, 13, 1), (361, 361, 1, 13, 1), (362, 362, 1, 13, 1), (363, 363, 1, 13, 1), (364, 364, 1, 13, 1), (365, 365, 1, 14, 1), (366, 366, 1, 14, 1), (367, 367, 1, 14, 1), (368, 368, 1, 14, 1), (369, 369, 1, 14, 1), (370, 370, 1, 14, 1), (371, 371, 1, 14, 1), (372, 372, 1, 14, 1), (373, 373, 1, 14, 1), (374, 374, 1, 14, 1), (375, 375, 1, 14, 1), (376, 376, 1, 14, 1), (377, 377, 1, 14, 1), (378, 378, 1, 14, 1), (379, 379, 1, 14, 1), (380, 380, 1, 14, 1), (381, 381, 1, 14, 1), (382, 382, 1, 14, 1), (383, 383, 1, 14, 1), (384, 384, 1, 14, 1), (385, 385, 1, 14, 1), (386, 386, 1, 14, 1), (387, 387, 1, 14, 1), (388, 388, 1, 14, 1), (389, 389, 1, 14, 1), (390, 390, 1, 14, 1), (391, 391, 1, 14, 1), (392, 392, 1, 14, 1), (393, 393, 1, 15, 1), (394, 394, 1, 15, 1), (395, 395, 1, 15, 1), (396, 396, 1, 15, 1), (397, 397, 1, 15, 1), (398, 398, 1, 15, 1), (399, 399, 1, 15, 1), (400, 400, 1, 15, 1), (401, 401, 1, 15, 1), (402, 402, 1, 15, 1), (403, 403, 1, 15, 1), (404, 404, 1, 15, 1), (405, 405, 1, 15, 1), (406, 406, 1, 15, 1), (407, 407, 1, 15, 1), (408, 408, 1, 15, 1), (409, 409, 1, 15, 1), (410, 410, 1, 15, 1), (411, 411, 1, 15, 1), (412, 412, 1, 15, 1), (413, 413, 1, 15, 1), (414, 414, 1, 15, 1), (415, 415, 1, 15, 1), (416, 416, 1, 15, 1), (417, 417, 1, 15, 1), (418, 418, 1, 15, 1), (419, 419, 1, 15, 1), (420, 420, 1, 15, 1), (421, 421, 1, 16, 1), (422, 422, 1, 16, 1), (423, 423, 1, 16, 1), (424, 424, 1, 16, 1), (425, 425, 1, 16, 1), (426, 426, 1, 16, 1), (427, 427, 1, 16, 1), (428, 428, 1, 16, 1), (429, 429, 1, 16, 1), (430, 430, 1, 16, 1), (431, 431, 1, 16, 1), (432, 432, 1, 16, 1), (433, 433, 1, 16, 1), (434, 434, 1, 16, 1), (435, 435, 1, 16, 1), (436, 436, 1, 16, 1), (437, 437, 1, 16, 1), (438, 438, 1, 16, 1), (439, 439, 1, 16, 1), (440, 440, 1, 16, 1), (441, 441, 1, 16, 1), (442, 442, 1, 16, 1), (443, 443, 1, 16, 1), (444, 444, 1, 16, 1), (445, 445, 1, 16, 1), (446, 446, 1, 16, 1), (447, 447, 1, 16, 1), (448, 448, 1, 16, 1), (449, 449, 1, 17, 1), (450, 450, 1, 17, 1), (451, 451, 1, 17, 1), (452, 452, 1, 17, 1), (453, 453, 1, 17, 1), (454, 454, 1, 17, 1), (455, 455, 1, 17, 1), (456, 456, 1, 17, 1), (457, 457, 1, 17, 1), (458, 458, 1, 17, 1), (459, 459, 1, 17, 1), (460, 460, 1, 17, 1), (461, 461, 1, 17, 1), (462, 462, 1, 17, 1), (463, 463, 1, 17, 1), (464, 464, 1, 17, 1), (465, 465, 1, 17, 1), (466, 466, 1, 17, 1), (471, 471, 1, 17, 1), (472, 472, 1, 17, 1), (473, 473, 1, 17, 1), (474, 474, 1, 17, 1), (475, 475, 1, 17, 1), (476, 476, 1, 17, 1), (477, 477, 1, 18, 1), (478, 478, 1, 18, 1), (479, 479, 1, 18, 1), (480, 480, 1, 18, 1), (481, 481, 1, 18, 1), (482, 482, 1, 18, 1), (483, 483, 1, 18, 1), (484, 484, 1, 18, 1), (485, 485, 1, 18, 1), (486, 486, 1, 18, 1), (487, 487, 1, 18, 1), (488, 488, 1, 18, 1), (489, 489, 1, 18, 1), (490, 490, 1, 18, 1), (491, 491, 1, 18, 1), (492, 492, 1, 18, 1), (493, 493, 1, 18, 1), (494, 494, 1, 18, 1), (499, 499, 1, 18, 1), (500, 500, 1, 18, 1), (501, 501, 1, 18, 1), (502, 502, 1, 18, 1), (503, 503, 1, 18, 1), (504, 504, 1, 18, 1)]
        
    seter_hovedscene_nedregalleri = [
        (505, 1, 1, 1, 2), (506, 2, 1, 1, 2), (507, 3, 1, 1, 2), (508, 4, 1, 1, 2), (509, 5, 1, 1, 2), (510, 6, 1, 1, 2), (511, 7, 1, 1, 2), (512, 8, 1, 1, 2), (513, 9, 1, 1, 2), (514, 10, 1, 1, 2)]

    seter_hovedscene_øvregalleri = [
    (515, 1, 1, 1, 3), (516, 2, 1, 1, 3), (517, 3, 1, 1, 3), (518, 4, 1, 1, 3), (519, 5, 1, 1, 3), (520, 6, 1, 1, 3), (521, 7, 1, 1, 3), (522, 8, 1, 1, 3), (523, 9, 1, 1, 3), (524, 10, 1, 1, 3)]

    seter_gamlesceneparkett = [
    (1, 1, 2, 1, 1), (2, 2, 2, 1, 1), (3, 3, 2, 1, 1), (4, 4, 2, 1, 1), (5, 5, 2, 1, 1), (6, 6, 2, 1, 1), (7, 7, 2, 1, 1), 
    (8, 8, 2, 1, 1), (9, 9, 2, 1, 1), (10, 10, 2, 1, 1), (11, 11, 2, 1, 1), (12, 12, 2, 1, 1), (13, 13, 2, 1, 1), 
    (14, 14, 2, 1, 1), (15, 15, 2, 1, 1), (16, 16, 2, 1, 1), (17, 17, 2, 1, 1), (18, 18, 2, 1, 1), (19, 1, 2, 2, 1), 
    (20, 2, 2, 2, 1), (21, 3, 2, 2, 1), (22, 4, 2, 2, 1), (23, 5, 2, 2, 1), (24, 6, 2, 2, 1), (25, 7, 2, 2, 1), 
    (26, 8, 2, 2, 1), (27, 9, 2, 2, 1), (28, 10, 2, 2, 1), (29, 11, 2, 2, 1), (30, 12, 2, 2, 1), (31, 13, 2, 2, 1), 
    (32, 14, 2, 2, 1), (33, 15, 2, 2, 1), (34, 16, 2, 2, 1), (35, 1, 2, 3, 1), (36, 2, 2, 3, 1), (37, 3, 2, 3, 1), 
    (38, 4, 2, 3, 1), (39, 5, 2, 3, 1), (40, 6, 2, 3, 1), (41, 7, 2, 3, 1), (42, 8, 2, 3, 1), (43, 9, 2, 3, 1), 
    (44, 10, 2, 3, 1), (45, 11, 2, 3, 1), (46, 12, 2, 3, 1), (47, 13, 2, 3, 1), (48, 14, 2, 3, 1), (49, 15, 2, 3, 1), 
    (50, 16, 2, 3, 1), (51, 17, 2, 3, 1), (52, 1, 2, 4, 1), (53, 2, 2, 4, 1), (54, 3, 2, 4, 1), (55, 4, 2, 4, 1), 
    (56, 5, 2, 4, 1), (57, 6, 2, 4, 1), (58, 7, 2, 4, 1), (59, 8, 2, 4, 1), (60, 9, 2, 4, 1), (61, 10, 2, 4, 1), 
    (62, 11, 2, 4, 1), (63, 12, 2, 4, 1), (64, 13, 2, 4, 1), (65, 14, 2, 4, 1), (66, 15, 2, 4, 1), (67, 16, 2, 4, 1), 
    (68, 17, 2, 4, 1), (69, 18, 2, 4, 1), (70, 1, 2, 5, 1), (71, 2, 2, 5, 1), (72, 3, 2, 5, 1), (73, 4, 2, 5, 1), 
    (74, 5, 2, 5, 1), (75, 6, 2, 5, 1), (76, 7, 2, 5, 1), (77, 8, 2, 5, 1), (78, 9, 2, 5, 1), (79, 10, 2, 5, 1), 
    (80, 11, 2, 5, 1), (81, 12, 2, 5, 1), (82, 13, 2, 5, 1), (83, 14, 2, 5, 1), (84, 15, 2, 5, 1), (85, 16, 2, 5, 1), 
    (86, 17, 2, 5, 1), (87, 18, 2, 5, 1), (88, 1, 2, 6, 1), (89, 2, 2, 6, 1), (90, 3, 2, 6, 1), (91, 4, 2, 6, 1), 
    (92, 5, 2, 6, 1), (93, 6, 2, 6, 1), (94, 7, 2, 6, 1), (95, 8, 2, 6, 1), (96, 9, 2, 6, 1), (97, 10, 2, 6, 1), 
    (98, 11, 2, 6, 1), (99, 12, 2, 6, 1), (100, 13, 2, 6, 1), (101, 14, 2, 6, 1), (102, 15, 2, 6, 1), (103, 16, 2, 6, 1), 
    (104, 1, 2, 6, 1), (105, 2, 2, 7, 1), (106, 3, 2, 7, 1), (107, 4, 2, 7, 1), (108, 5, 2, 7, 1), (109, 6, 2, 7, 1), 
    (110, 7, 2, 7, 1), (111, 8, 2, 7, 1), (112, 9, 2, 7, 1), (113, 10, 2, 7, 1), (114, 11, 2, 7, 1), (115, 12, 2, 7, 1), 
    (116, 13, 2, 7, 1), (117, 14, 2, 7, 1), (118, 15, 2, 7, 1), (119, 16, 2, 7, 1), (120, 17, 2, 7, 1), (121, 18, 2, 7, 1), 
    (122, 1, 2, 8, 1), (123, 2, 2, 8, 1), (124, 3, 2, 8, 1), (125, 4, 2, 8, 1), (126, 5, 2, 8, 1), (127, 6, 2, 8, 1), 
    (128, 7, 2, 8, 1), (129, 8, 2, 8, 1), (130, 9, 2, 8, 1), (131, 10, 2, 8, 1), (132, 11, 2, 8, 1), (133, 12, 2, 8, 1), 
    (134, 13, 2, 8, 1), (135, 14, 2, 8, 1), (136, 15, 2, 8, 1), (137, 16, 2, 8, 1), (138, 17, 2, 8, 1), (139, 1, 2, 8, 1), 
    (140, 2, 2, 9, 1), (141, 3, 2, 9, 1), (142, 4, 2, 9, 1), (143, 5, 2, 9, 1), (144, 6, 2, 9, 1), (145, 7, 2, 9, 1), 
    (146, 8, 2, 9, 1), (147, 9, 2, 9, 1), (148, 10, 2, 9, 1), (149, 11, 2, 9, 1), (150, 12, 2, 9, 1), (151, 13, 2, 9, 1), 
    (152, 14, 2, 9, 1), (153, 15, 2, 9, 1), (154, 16, 2, 9, 1), (155, 17, 2, 9, 1), (156, 1, 2, 9, 1), (157, 2, 2, 10, 1), 
    (158, 3, 2, 10, 1), (159, 4, 2, 10, 1), (160, 5, 2, 10, 1), (161, 6, 2, 10, 1), (162, 7, 2, 10, 1), (163, 8, 2, 10, 1), 
    (164, 9, 2, 10, 1), (165, 10, 2, 10, 1), (166, 11, 2, 10, 1), (167, 12, 2, 10, 1), (168, 13, 2, 10, 1), (169, 14, 2, 10, 1), 
    (170, 15, 2, 10, 1)
    ]

    seter_gamlescenebalkong = [
    (171, 1, 2, 1, 2), (172, 2, 2, 1, 2), (173, 3, 2, 1, 2), (174, 4, 2, 1, 2), (175, 5, 2, 1, 2),
    (176, 6, 2, 1, 2), (177, 7, 2, 1, 2), (178, 8, 2, 1, 2), (179, 9, 2, 1, 2), (180, 10, 2, 1, 2),
    (181, 11, 2, 1, 2), (182, 12, 2, 1, 2), (183, 13, 2, 1, 2), (184, 14, 2, 1, 2), (185, 15, 2, 1, 2),
    (186, 16, 2, 1, 2), (187, 17, 2, 1, 2), (188, 18, 2, 1, 2), (189, 19, 2, 1, 2), (190, 20, 2, 1, 2),
    (191, 21, 2, 1, 2), (192, 22, 2, 1, 2), (193, 23, 2, 1, 2), (194, 24, 2, 1, 2), (195, 25, 2, 1, 2),
    (196, 26, 2, 1, 2), (197, 27, 2, 1, 2), (198, 28, 2, 1, 2), (199, 1, 2, 2, 2), (200, 2, 2, 2, 2),
    (201, 3, 2, 2, 2), (202, 4, 2, 2, 2), (203, 5, 2, 2, 2), (204, 6, 2, 2, 2), (205, 7, 2, 2, 2),
    (206, 8, 2, 2, 2), (207, 9, 2, 2, 2), (208, 10, 2, 2, 2), (209, 11, 2, 2, 2), (210, 12, 2, 2, 2),
    (211, 13, 2, 2, 2), (212, 14, 2, 2, 2), (213, 15, 2, 2, 2), (214, 16, 2, 2, 2), (215, 17, 2, 2, 2),
    (216, 18, 2, 2, 2), (217, 19, 2, 2, 2), (218, 20, 2, 2, 2), (219, 21, 2, 2, 2), (220, 22, 2, 2, 2),
    (221, 23, 2, 2, 2), (222, 24, 2, 2, 2), (223, 25, 2, 2, 2), (224, 26, 2, 2, 2), (225, 27, 2, 2, 2),
    (226, 1, 2, 3, 2), (227, 2, 2, 3, 2), (228, 3, 2, 3, 2), (229, 4, 2, 3, 2), (230, 5, 2, 3, 2),
    (231, 6, 2, 3, 2), (232, 7, 2, 3, 2), (233, 8, 2, 3, 2), (234, 9, 2, 3, 2), (235, 10, 2, 3, 2),
    (236, 11, 2, 3, 2), (237, 12, 2, 3, 2), (238, 13, 2, 3, 2), (239, 14, 2, 3, 2), (240, 15, 2, 3, 2),
    (241, 16, 2, 3, 2), (242, 17, 2, 3, 2), (243, 18, 2, 3, 2), (244, 19, 2, 3, 2), (245, 20, 2, 3, 2),
    (246, 21, 2, 3, 2), (247, 22, 2, 3, 2), (248, 1, 2, 4, 2), (249, 2, 2, 4, 2), (250, 3, 2, 4, 2),
    (251, 4, 2, 4, 2), (252, 5, 2, 4, 2), (253, 6, 2, 4, 2), (254, 7, 2, 4, 2), (255, 8, 2, 4, 2),
    (256, 9, 2, 4, 2), (257, 10, 2, 4, 2), (258, 11, 2, 4, 2), (259, 12, 2, 4, 2), (260, 13, 2, 4, 2),
    (261, 14, 2, 4, 2), (262, 15, 2, 4, 2), (263, 16, 2, 4, 2), (264, 17, 2, 4, 2)
    ]

    seter_gamlescenegalleri = [
        (265, 1, 2, 1, 3), (266, 2, 2, 1, 3), (267, 3, 2, 1, 3), (268, 4, 2, 1, 3),
    (269, 5, 2, 1, 3), (270, 6, 2, 1, 3), (271, 7, 2, 1, 3), (272, 8, 2, 1, 3), (273, 9, 2, 1, 3), (274, 10, 2, 1, 3), 
    (275, 11, 2, 1, 3), (276, 12, 2, 1, 3), (277, 13, 2, 1, 3), (278, 14, 2, 1, 3), (279, 15, 2, 1, 3), 
    (280, 16, 2, 1, 3), (281, 17, 2, 1, 3), (282, 18, 2, 1, 3), (283, 19, 2, 1, 3), (284, 20, 2, 1, 3), 
    (285, 21, 2, 1, 3), (286, 22, 2, 1, 3), (287, 23, 2, 1, 3), (288, 24, 2, 1, 3), (289, 25, 2, 1, 3), 
    (290, 26, 2, 1, 3), (291, 27, 2, 1, 3), (292, 28, 2, 1, 3), (293, 29, 2, 1, 3), (294, 30, 2, 1, 3), 
    (295, 31, 2, 1, 3), (296, 32, 2, 1, 3), (297, 33, 2, 1, 3), (298, 2, 2, 2, 3), (299, 3, 2, 2, 3), 
    (300, 4, 2, 2, 3), (301, 5, 2, 2, 3), (302, 6, 2, 2, 3), (303, 7, 2, 2, 3), (304, 8, 2, 2, 3), 
    (305, 9, 2, 2, 3), (306, 10, 2, 2, 3), (307, 11, 2, 2, 3), (308, 12, 2, 2, 3), (309, 13, 2, 2, 3), 
    (310, 14, 2, 2, 3), (311, 15, 2, 2, 3), (312, 16, 2, 2, 3), (313, 17, 2, 2, 3), (314, 18, 2, 2, 3), 
    (315, 19, 2, 2, 3), (316, 3, 2, 3, 3), (317, 4, 2, 3, 3), (318, 5, 2, 3, 3), (319, 6, 2, 3, 3), 
    (320, 7, 2, 3, 3), (321, 8, 2, 3, 3), (322, 9, 2, 3, 3), (323, 10, 2, 3, 3), (324, 11, 2, 3, 3), 
    (325, 12, 2, 3, 3), (326, 13, 2, 3, 3), (327, 14, 2, 3, 3), (328, 15, 2, 3, 3), (329, 16, 2, 3, 3), 
    (330, 17, 2, 3, 3), (331, 18, 2, 3, 3), (332, 19, 2, 3, 3)
    ]
    
    prisklasser = [
    ("Ordinær", "Kongsemnene", 450),
    ("Honnør", "Kongsemnene", 380),
    ("Student", "Kongsemnene", 280),
    ("Gruppe 10", "Kongsemnene", 420),  # Gjelder minimum 10 billetter
    ("Gruppe honnør 10", "Kongsemnene", 360),
    ("Ordinær", "Størst av alt er kjærligheten", 350),
    ("Honnør", "Størst av alt er kjærligheten", 300),
    ("Student", "Størst av alt er kjærligheten", 220),
    ("Barn", "Størst av alt er kjærligheten", 220),
    ("Gruppe 10", "Størst av alt er kjærligheten", 320),
    ("Gruppe honnør 10", "Størst av alt er kjærligheten", 270)
]
    
    forestillinger = [
        ('Kongsemnene', '2024-02-01', '19:00'),
       ('Kongsemnene', '2024-02-02', '19:00'),
       ('Kongsemnene', '2024-02-03', '19:00'),
       ('Kongsemnene', '2024-02-05', '19:00'),
       ('Kongsemnene', '2024-02-06', '19:00'),
       ('Størst av alt er kjærligheten', '2024-02-03', '18:30'),
       ('Størst av alt er kjærligheten', '2024-02-06', '18:30'),
       ('Størst av alt er kjærligheten', '2024-02-07', '18:30'),
       ('Størst av alt er kjærligheten', '2024-02-12', '18:30'),
       ('Størst av alt er kjærligheten', '2024-02-13', '18:30'),
       ('Størst av alt er kjærligheten', '2024-02-14', '18:30'),
    ]

    teatre = [
        ("vinter/vår 2024"),
        ("sommer/høst 2024"),
    ]

    direktører = [
        (1,15),
    ]
    
    ansatte = [
        (16,1),
        (17,2),
        (18,3),
        (19,4),
        (20,5),
        (21,6),
        (22,7),
        (23,8),
        (24,9),
        (25,10),        
        (26,11),    
        (27,12),    
        (28,13),    
        (29,14),    
        (30,15),    
        (31,16),    
        (32,17),    
        (33,18),    
    ]

    biletter_hovedscenen = [
    ("Kongsemnene", "Ordinær", 11, 1),
    ("Kongsemnene", "Ordinær", 12, 1),
    ("Kongsemnene", "Ordinær", 13, 1),
    ("Kongsemnene", "Ordinær", 14, 1),
    ("Kongsemnene", "Ordinær", 15, 1),
    ("Kongsemnene", "Ordinær", 16, 1),
    ("Kongsemnene", "Ordinær", 17, 1),
    ("Kongsemnene", "Ordinær", 18, 1),
    ("Kongsemnene", "Ordinær", 19, 1),
    ("Kongsemnene", "Ordinær", 20, 1),
    ("Kongsemnene", "Ordinær", 21, 1),
    ("Kongsemnene", "Ordinær", 22, 1),
    ("Kongsemnene", "Ordinær", 23, 1),
    ("Kongsemnene", "Ordinær", 24, 1),
    ("Kongsemnene", "Ordinær", 25, 1),
    ("Kongsemnene", "Ordinær", 26, 1),
    ("Kongsemnene", "Ordinær", 27, 1),
    ("Kongsemnene", "Ordinær", 28, 1),
    ("Kongsemnene", "Ordinær", 29, 1),
    ("Kongsemnene", "Ordinær", 30, 1),
    ("Kongsemnene", "Ordinær", 31, 1),
    ("Kongsemnene", "Ordinær", 32, 1),
    ("Kongsemnene", "Ordinær", 33, 1),
    ("Kongsemnene", "Ordinær", 34, 1),
    ("Kongsemnene", "Ordinær", 35, 1),
    ("Kongsemnene", "Ordinær", 36, 1),
    ("Kongsemnene", "Ordinær", 37, 1),
    ("Kongsemnene", "Ordinær", 38, 1),
    ("Kongsemnene", "Ordinær", 39, 1),
    ("Kongsemnene", "Ordinær", 40, 1),
    ("Kongsemnene", "Ordinær", 41, 1),
    ("Kongsemnene", "Ordinær", 42, 1),
    ("Kongsemnene", "Ordinær", 43, 1),
    ("Kongsemnene", "Ordinær", 44, 1),
    ("Kongsemnene", "Ordinær", 45, 1),
    ("Kongsemnene", "Ordinær", 46, 1),
    ("Kongsemnene", "Ordinær", 47, 1),
    ("Kongsemnene", "Ordinær", 66, 1),
    ("Kongsemnene", "Ordinær", 66, 1),
    ("Kongsemnene", "Ordinær", 67, 1),
    ("Kongsemnene", "Ordinær", 68, 1),
    ("Kongsemnene", "Ordinær", 69, 1),
    ("Kongsemnene", "Ordinær", 70, 1),
    ("Kongsemnene", "Ordinær", 71, 1),
    ("Kongsemnene", "Ordinær", 72, 1),
    ("Kongsemnene", "Ordinær", 73, 1),
    ("Kongsemnene", "Ordinær", 74, 1),
    ("Kongsemnene", "Ordinær", 75, 1),
    ("Kongsemnene", "Ordinær", 94, 1),
    ("Kongsemnene", "Ordinær", 95, 1),
    ("Kongsemnene", "Ordinær", 96, 1),
    ("Kongsemnene", "Ordinær", 97, 1),
    ("Kongsemnene", "Ordinær", 98, 1),
    ("Kongsemnene", "Ordinær", 99, 1),
    ("Kongsemnene", "Ordinær", 100, 1),
    ("Kongsemnene", "Ordinær", 101, 1),
    ("Kongsemnene", "Ordinær", 127, 1),
    ("Kongsemnene", "Ordinær", 128, 1),
    ("Kongsemnene", "Ordinær", 154, 1),
    ("Kongsemnene", "Ordinær", 155, 1),
    ("Kongsemnene", "Ordinær", 182, 1),
    ("Kongsemnene", "Ordinær", 183, 1),
    ("Kongsemnene", "Ordinær", 337, 1),
    ("Kongsemnene", "Ordinær", 338, 1),
    ("Kongsemnene", "Ordinær", 339, 1),
    ("Kongsemnene", "Ordinær", 347, 1),
    ("Kongsemnene", "Ordinær", 375, 1),
    ("Kongsemnene", "Ordinær", 398, 1),
    ("Kongsemnene", "Ordinær", 399, 1),
    ("Kongsemnene", "Ordinær", 400, 1),
    ("Kongsemnene", "Ordinær", 403, 1),
    ("Kongsemnene", "Ordinær", 431, 1)
]

   
    biletter_gamlescenen = [

        ("Størst av alt er kjærligheten", "Ordinær", 1, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 2, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 8, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 9, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 19, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 20, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 21, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 27, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 38, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 39, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 43, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 55, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 56, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 59, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 60, 1),

        ("Størst av alt er kjærligheten", "Ordinær", 77, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 78, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 95, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 112, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 113, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 130, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 147, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 164, 1),

        ("Størst av alt er kjærligheten", "Ordinær", 226, 1),
        ("Størst av alt er kjærligheten", "Ordinær", 227, 1)
    ]

    seed_ansattstatus(dbpath, status)

    for sal in saler:
        seed_sal(dbpath, sal)

    for person in personer:
        seed_person(dbpath, [person])

    for act in acts_data:
        seed_akt(dbpath, act)
    
    for actor in actors_data:
        seed_skuespiller(dbpath, [actor])

    for role in roles:    
        seed_rolle(dbpath, [role])

    for oppgave in oppgavetyper:
        seed_oppgavetype(dbpath, [oppgave])

    for teaterstykke in teaterstykker:
        seed_teaterstykke(dbpath, teaterstykke)

    for stykke in teaterstykker:
        for oppgtype in oppgavetyper:
            seed_arbeidsoppgave(dbpath, (oppgtype, stykke[0]))

    for kunde in kunder:
        seed_kunde(dbpath, kunde)

    for prisklasse in prisklasser:
        seed_prisklasse(dbpath, prisklasse)
    
    for forestilling in forestillinger:
        seed_forestilling(dbpath, forestilling)   

    for teater in teatre:
        seed_teater(dbpath, teater)

    for direktør in direktører:
        seed_direktør(dbpath, direktør) 

    for område in områder_hovedscene:
        seed_område(dbpath, område)

    for område in områder_gamlescene:
        seed_område(dbpath, område)

    for sete in seter_hovedscene:
        seed_sete(dbpath, sete)

    for sete in seter_hovedscene_nedregalleri:
        seed_sete(dbpath, sete)

    for sete in seter_hovedscene_øvregalleri:
        seed_sete(dbpath, sete)

    for sete in seter_gamlesceneparkett:
        seed_sete(dbpath, sete)

    for sete in seter_gamlescenebalkong:
        seed_sete(dbpath, sete)

    for sete in seter_gamlescenegalleri:
        seed_sete(dbpath, sete)

    for ansatt in ansatte:
        seed_ansatt(dbpath, ansatt)

    seed_billettkjøp(dbpath, (1, 1, dt.datetime(year=2024, month=2, day=1), 1, 0, 1))

    for billett in biletter_hovedscenen:
        seed_billett(dbpath, billett)

    for billett in biletter_gamlescenen:
        seed_billett(dbpath, billett)

    #sfor arbeidsoppgave in arbeidsoppgaver:

    
seed_data("Createdb.db")