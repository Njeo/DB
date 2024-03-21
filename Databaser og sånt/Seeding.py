import sqlite3

def seed_ansattstatus(dbpath, status):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        for stat in status:
            cur.execute("INSERT INTO ansattStatus (status) VALUES (?)", (stat,))
        # The connection is automatically committed and closed at the end of the with block.

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

    cur.execute("INSERT INTO sete (seteNr, salId, radNr, omraadeId) VALUES (?,?,?,?)",
                (data[0], data[1], data[2], data[3]))
    
    conn.commit()
    conn.close()

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

    cur.execute("INSERT INTO billettkjøp (kjøpsreferanse, kundeId, billettantall, totalpris) VALUES (?,?,?,?)",
                (data[0], data[1], data[2], data[3]))

    conn.commit()
    conn.close()

def seed_billett(dbpath, data):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

    cur.execute("INSERT INTO billett (tittel, prisklasseNavn, seteId, kjøpsreferanse) VALUES (?,?,?,?)",
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
                data[0],data[1])
    conn.commit()
    conn.close()


def seed_data(dbpath):
    saler = [
        ("Hovedscenen", 516, 18), 
        ("Gamle scene", 338, 33)
    ]

    områder_hovedscene = [
        (1, 1, "hovedområde"), (2, 1, "øvre galleri"), (3, 1, "nedre galleri")
    ]

    områder_gamlescene = [
        "parkett", "balkong", "galleri"
    ]

    

    status = ["deltid", "fulltid"]

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

    
    seter_hovedscene = [(1, 1, 1, 1), (2, 1, 1, 1), (3, 1, 1, 1), (4, 1, 1, 1), (5, 1, 1, 1), (6, 1, 1, 1), (7, 1, 1, 1), (8, 1, 1, 1), (9, 1, 1, 1), (10, 1, 1, 1), (11, 1, 1, 1), (12, 1, 1, 1), (13, 1, 1, 1), (14, 1, 1, 1), (15, 1, 1, 1), (16, 1, 1, 1), (17, 1, 2, 1), (18, 1, 2, 1), (19, 1, 2, 1), (20, 1, 2, 1), (21, 1, 2, 1), (22, 1, 2, 1), (23, 1, 2, 1), (24, 1, 2, 1), (25, 1, 2, 1), (26, 1, 2, 1), (27, 1, 2, 1), (28, 1, 2, 1), (29, 1, 2, 1), (30, 1, 2, 1), (31, 1, 2, 1), (32, 1, 2, 1), (33, 1, 3, 1), (34, 1, 3, 1), (35, 1, 3, 1), (36, 1, 3, 1), (37, 1, 3, 1), (38, 1, 3, 1), (39, 1, 3, 1), (40, 1, 3, 1), (41, 1, 3, 1), (42, 1, 3, 1), (43, 1, 3, 1), (44, 1, 3, 1), (45, 1, 3, 1), (46, 1, 3, 1), (47, 1, 3, 1), (48, 1, 3, 1), (49, 1, 4, 1), (50, 1, 4, 1), (51, 1, 4, 1), (52, 1, 4, 1), (53, 1, 4, 1), (54, 1, 4, 1), (55, 1, 4, 1), (56, 1, 4, 1), (57, 1, 4, 1), (58, 1, 4, 1), (59, 1, 4, 1), (60, 1, 4, 1), (61, 1, 4, 1), (62, 1, 4, 1), (63, 1, 4, 1), (64, 1, 4, 1), (65, 1, 5, 1), (66, 1, 5, 1), (67, 1, 5, 1), (68, 1, 5, 1), (69, 1, 5, 1), (70, 1, 5, 1), (71, 1, 5, 1), (72, 1, 5, 1), (73, 1, 5, 1), (74, 1, 5, 1), (75, 1, 5, 1), (76, 1, 5, 1), (77, 1, 5, 1), (78, 1, 5, 1), (79, 1, 5, 1), (80, 1, 5, 1), (81, 1, 6, 1), (82, 1, 6, 1), (83, 1, 6, 1), (84, 1, 6, 1), (85, 1, 6, 1), (86, 1, 6, 1), (87, 1, 6, 1), (88, 1, 6, 1), (89, 1, 6, 1), (90, 1, 6, 1), (91, 1, 6, 1), (92, 1, 6, 1), (93, 1, 6, 1), (94, 1, 6, 1), (95, 1, 6, 1), (96, 1, 6, 1), (97, 1, 7, 1), (98, 1, 7, 1), (99, 1, 7, 1), (100, 1, 7, 1), (101, 1, 7, 1), (102, 1, 7, 1), (103, 1, 7, 1), (104, 1, 7, 1), (105, 1, 7, 1), (106, 1, 7, 1), (107, 1, 7, 1), (108, 1, 7, 1), (109, 1, 7, 1), (110, 1, 7, 1), (111, 1, 7, 1), (112, 1, 7, 1), (113, 1, 8, 1), (114, 1, 8, 1), (115, 1, 8, 1), (116, 1, 8, 1), (117, 1, 8, 1), (118, 1, 8, 1), (119, 1, 8, 1), (120, 1, 8, 1), (121, 1, 8, 1), (122, 1, 8, 1), (123, 1, 8, 1), (124, 1, 8, 1), (125, 1, 8, 1), (126, 1, 8, 1), (127, 1, 8, 1), (128, 1, 8, 1), (129, 1, 9, 1), (130, 1, 9, 1), (131, 1, 9, 1), (132, 1, 9, 1), (133, 1, 9, 1), (134, 1, 9, 1), (135, 1, 9, 1), (136, 1, 9, 1), (137, 1, 9, 1), (138, 1, 9, 1), (139, 1, 9, 1), (140, 1, 9, 1), (141, 1, 9, 1), (142, 1, 9, 1), (143, 1, 9, 1), (144, 1, 9, 1), (145, 1, 10, 1), (146, 1, 10, 1), (147, 1, 10, 1), (148, 1, 10, 1), (149, 1, 10, 1), (150, 1, 10, 1), (151, 1, 10, 1), (152, 1, 10, 1), (153, 1, 10, 1), (154, 1, 10, 1), (155, 1, 10, 1), (156, 1, 10, 1), (157, 1, 10, 1), (158, 1, 10, 1), (159, 1, 10, 1), (160, 1, 10, 1), (161, 1, 11, 1), (162, 1, 11, 1), (163, 1, 11, 1), (164, 1, 11, 1), (165, 1, 11, 1), (166, 1, 11, 1), (167, 1, 11, 1), (168, 1, 11, 1), (169, 1, 11, 1), (170, 1, 11, 1), (171, 1, 11, 1), (172, 1, 11, 1), (173, 1, 11, 1), (174, 1, 11, 1), (175, 1, 11, 1), (176, 1, 11, 1), (177, 1, 12, 1), (178, 1, 12, 1), (179, 1, 12, 1), (180, 1, 12, 1), (181, 1, 12, 1), (182, 1, 12, 1), (183, 1, 12, 1), (184, 1, 12, 1), (185, 1, 12, 1), (186, 1, 12, 1), (187, 1, 12, 1), (188, 1, 12, 1), (189, 1, 12, 1), (190, 1, 12, 1), (191, 1, 12, 1), (192, 1, 12, 1), (193, 1, 13, 1), (194, 1, 13, 1), (195, 1, 13, 1), (196, 1, 13, 1), (197, 1, 13, 1), (198, 1, 13, 1), (199, 1, 13, 1), (200, 1, 13, 1), (201, 1, 13, 1), (202, 1, 13, 1), (203, 1, 13, 1), (204, 1, 13, 1), (205, 1, 13, 1), (206, 1, 13, 1), (207, 1, 13, 1), (208, 1, 13, 1), (209, 1, 14, 1), (210, 1, 14, 1), (211, 1, 14, 1), (212, 1, 14, 1), (213, 1, 14, 1), (214, 1, 14, 1), (215, 1, 14, 1), (216, 1, 14, 1), (217, 1, 14, 1), (218, 1, 14, 1), (219, 1, 14, 1), (220, 1, 14, 1), (221, 1, 14, 1), (222, 1, 14, 1), (223, 1, 14, 1), (224, 1, 14, 1), (225, 1, 15, 1), (226, 1, 15, 1), (227, 1, 15, 1), (228, 1, 15, 1), (229, 1, 15, 1), (230, 1, 15, 1), (231, 1, 15, 1), (232, 1, 15, 1), (233, 1, 15, 1), (234, 1, 15, 1), (235, 1, 15, 1), (236, 1, 15, 1), (237, 1, 15, 1), (238, 1, 15, 1), (239, 1, 15, 1), (240, 1, 15, 1), (241, 1, 16, 1), (242, 1, 16, 1), (243, 1, 16, 1), (244, 1, 16, 1), (245, 1, 16, 1), (246, 1, 16, 1), (247, 1, 16, 1), (248, 1, 16, 1), (249, 1, 16, 1), (250, 1, 16, 1), (251, 1, 16, 1), (252, 1, 16, 1), (253, 1, 16, 1), (254, 1, 16, 1), (255, 1, 16, 1), (256, 1, 16, 1), (257, 1, 17, 1), (258, 1, 17, 1), (259, 1, 17, 1), (260, 1, 17, 1), (261, 1, 17, 1), (262, 1, 17, 1), (263, 1, 17, 1), (264, 1, 17, 1), (265, 1, 17, 1), (266, 1, 17, 1), (267, 1, 17, 1), (268, 1, 17, 1), (269, 1, 17, 1), (270, 1, 17, 1), (271, 1, 17, 1), (272, 1, 17, 1), (273, 1, 18, 1), (274, 1, 18, 1), (275, 1, 18, 1), (276, 1, 18, 1), (277, 1, 18, 1), (278, 1, 18, 1), (279, 1, 18, 1), (280, 1, 18, 1), (281, 1, 18, 1), (282, 1, 18, 1), (283, 1, 18, 1), (284, 1, 18, 1), (285, 1, 18, 1), (286, 1, 18, 1), (287, 1, 18, 1), (288, 1, 18, 1), (289, 1, 19, 1), (290, 1, 19, 1), (291, 1, 19, 1), (292, 1, 19, 1), (293, 1, 19, 1), (294, 1, 19, 1), (295, 1, 19, 1), (296, 1, 19, 1), (297, 1, 19, 1), (298, 1, 19, 1), (299, 1, 19, 1), (300, 1, 19, 1), (301, 1, 19, 1), (302, 1, 19, 1), (303, 1, 19, 1), (304, 1, 19, 1), (305, 1, 20, 1), (306, 1, 20, 1), (307, 1, 20, 1), (308, 1, 20, 1), (309, 1, 20, 1), (310, 1, 20, 1), (311, 1, 20, 1), (312, 1, 20, 1), (313, 1, 20, 1), (314, 1, 20, 1), (315, 1, 20, 1), (316, 1, 20, 1), (317, 1, 20, 1), (318, 1, 20, 1), (319, 1, 20, 1), (320, 1, 20, 1), (321, 1, 21, 1), (322, 1, 21, 1), (323, 1, 21, 1), (324, 1, 21, 1), (325, 1, 21, 1), (326, 1, 21, 1), (327, 1, 21, 1), (328, 1, 21, 1), (329, 1, 21, 1), (330, 1, 21, 1), (331, 1, 21, 1), (332, 1, 21, 1), (333, 1, 21, 1), (334, 1, 21, 1), (335, 1, 21, 1), (336, 1, 21, 1), (337, 1, 22, 1), (338, 1, 22, 1), (339, 1, 22, 1), (340, 1, 22, 1), (341, 1, 22, 1), (342, 1, 22, 1), (343, 1, 22, 1), (344, 1, 22, 1), (345, 1, 22, 1), (346, 1, 22, 1), (347, 1, 22, 1), (348, 1, 22, 1), (349, 1, 22, 1), (350, 1, 22, 1), (351, 1, 22, 1), (352, 1, 22, 1), (353, 1, 23, 1), (354, 1, 23, 1), (355, 1, 23, 1), (356, 1, 23, 1), (357, 1, 23, 1), (358, 1, 23, 1), (359, 1, 23, 1), (360, 1, 23, 1), (361, 1, 23, 1), (362, 1, 23, 1), (363, 1, 23, 1), (364, 1, 23, 1), (365, 1, 23, 1), (366, 1, 23, 1), (367, 1, 23, 1), (368, 1, 23, 1), (369, 1, 24, 1), (370, 1, 24, 1), (371, 1, 24, 1), (372, 1, 24, 1), (373, 1, 24, 1), (374, 1, 24, 1), (375, 1, 24, 1), (376, 1, 24, 1), (377, 1, 24, 1), (378, 1, 24, 1), (379, 1, 24, 1), (380, 1, 24, 1), (381, 1, 24, 1), (382, 1, 24, 1), (383, 1, 24, 1), (384, 1, 24, 1), (385, 1, 25, 1), (386, 1, 25, 1), (387, 1, 25, 1), (388, 1, 25, 1), (389, 1, 25, 1), (390, 1, 25, 1), (391, 1, 25, 1), (392, 1, 25, 1), (393, 1, 25, 1), (394, 1, 25, 1), (395, 1, 25, 1), (396, 1, 25, 1), (397, 1, 25, 1), (398, 1, 25, 1), (399, 1, 25, 1), (400, 1, 25, 1), (401, 1, 26, 1), (402, 1, 26, 1), (403, 1, 26, 1), (404, 1, 26, 1), (405, 1, 26, 1), (406, 1, 26, 1), (407, 1, 26, 1), (408, 1, 26, 1), (409, 1, 26, 1), (410, 1, 26, 1), (411, 1, 26, 1), (412, 1, 26, 1), (413, 1, 26, 1), (414, 1, 26, 1), (415, 1, 26, 1), (416, 1, 26, 1), (417, 1, 27, 1), (418, 1, 27, 1), (419, 1, 27, 1), (420, 1, 27, 1), (421, 1, 27, 1), (422, 1, 27, 1), (423, 1, 27, 1), (424, 1, 27, 1), (425, 1, 27, 1), (426, 1, 27, 1), (427, 1, 27, 1), (428, 1, 27, 1), (429, 1, 27, 1), (430, 1, 27, 1), (431, 1, 27, 1), (432, 1, 27, 1), (433, 1, 28, 1), (434, 1, 28, 1), (435, 1, 28, 1), (436, 1, 28, 1), (437, 1, 28, 1), (438, 1, 28, 1), (439, 1, 28, 1), (440, 1, 28, 1), (441, 1, 28, 1), (442, 1, 28, 1), (443, 1, 28, 1), (444, 1, 28, 1), (445, 1, 28, 1), (446, 1, 28, 1), (447, 1, 28, 1), (448, 1, 28, 1), (449, 1, 17, 1), (450, 1, 17, 1), (451, 1, 17, 1), (452, 1, 17, 1), (453, 1, 17, 1), (454, 1, 17, 1), (455, 1, 17, 1), (456, 1, 17, 1), (457, 1, 17, 1), (458, 1, 17, 1), (459, 1, 17, 1), (460, 1, 17, 1), (461, 1, 17, 1), (462, 1, 17, 1), (463, 1, 17, 1), (464, 1, 17, 1), (465, 1, 17, 1), (466, 1, 17, 1), (471, 1, 17, 1), (472, 1, 17, 1), (473, 1, 17, 1), (474, 1, 17, 1), (475, 1, 17, 1), (476, 1, 17, 1), (477, 1, 18, 1), (478, 1, 18, 1), (479, 1, 18, 1), (480, 1, 18, 1), (481, 1, 18, 1), (482, 1, 18, 1), (483, 1, 18, 1), (484, 1, 18, 1), (485, 1, 18, 1), (486, 1, 18, 1), (487, 1, 18, 1), (488, 1, 18, 1), (489, 1, 18, 1), (490, 1, 18, 1), (491, 1, 18, 1), (492, 1, 18, 1), (493, 1, 18, 1), (494, 1, 18, 1), (499, 1, 18, 1), (500, 1, 18, 1), (501, 1, 18, 1), (502, 1, 18, 1), (503, 1, 18, 1), (504, 1, 18, 1), (505, 1, 1, 2), (506, 1, 1, 2), (507, 1, 1, 2), (508, 1, 1, 2), (509, 1, 1, 2), (510, 1, 1, 2), (511, 1, 1, 2), (512, 1, 1, 2), (513, 1, 1, 2), (514, 1, 1, 2), (515, 1, 1, 3), (516, 1, 1, 3), (517, 1, 1, 3), (518, 1, 1, 3), (519, 1, 1, 3), (520, 1, 1, 3), (521, 1, 1, 3), (522, 1, 1, 3), (523, 1, 1, 3), (524, 1, 1, 3)]

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
        (16,9)
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
        seed_kunde(dbpath,kunde)

    for prisklasse in prisklasser:
        seed_prisklasse(dbpath,prisklasse)
    
    for forestilling in forestillinger:
        seed_forestilling(dbpath,forestilling)   

    for teater in teatre:
        seed_teater(dbpath,teater)

    for direktør in direktører:
        seed_direktør(dbpath,direktør) 

    for område in områder_hovedscene:
        seed_område(dbpath, område)

    for sete in seter_hovedscene:
        seed_sete(dbpath, sete)

    for ansatt in ansatte:
        seed_ansatt(dbpath,[ansatt])

    #sfor arbeidsoppgave in arbeidsoppgaver:

    
seed_data("Createdb.db")