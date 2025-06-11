TRAIN_DATA = [
    (
        "Our next getaway is Oradea, Romania where we hope to check out 7 sights. Mostly bike, staying at Strada Horea 7, and keeping to 18 kilometes Expect to spend around 98 RON, and we're only considering places at least 4,3★.",
        {'entities': [(20, 35, 'LOCATION'), (63, 71, 'ATTRACTIONS_COUNT'), (80, 84, 'TRANSPORT'), (97, 111, 'ADDRESS'), (128, 140, 'MAX_DISTANCE'), (164, 170, 'MAX_PRICE'), (206, 219, 'MIN_RATING')]}
    ),
    (
        "We’re off to Pitesti, Romania, want to visit 1 things and will be using bicyle. Accommodation is Calea Bucuresti 22. Distance cap: 15 km Expect to spend around $154, and we're only considering places 78 points.",
        {'entities': [(13, 29, 'LOCATION'), (45, 53, 'ATTRACTIONS_COUNT'), (72, 78, 'TRANSPORT'), (97, 115, 'ADDRESS'), (131, 136, 'MAX_DISTANCE'), (160, 164, 'MAX_PRICE'), (200, 209, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Galati, Romania, aiming for 2 spots. We'll use walk most of the time and rest at Strada Horea 7. No more than 22 kms Expect to spend around 191 dollars, and we're only considering places at least 4,8★.",
        {'entities': [(22, 37, 'LOCATION'), (50, 57, 'ATTRACTIONS_COUNT'), (69, 73, 'TRANSPORT'), (103, 117, 'ADDRESS'), (132, 138, 'MAX_DISTANCE'), (162, 173, 'MAX_PRICE'), (209, 222, 'MIN_RATING')]}
    ),
    (
        "We’re off to Oradea, Romania, want to visit 2 spots and will be using walk. Accommodation is Strada Memorandumului 5. Distance cap: 16 kms Expect to spend around 160 USD, and we're only considering places 43/10 score.",
        {'entities': [(13, 28, 'LOCATION'), (44, 51, 'ATTRACTIONS_COUNT'), (70, 74, 'TRANSPORT'), (93, 116, 'ADDRESS'), (132, 138, 'MAX_DISTANCE'), (162, 169, 'MAX_PRICE'), (205, 216, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Bucharest, Romania, aiming for 4 things. We'll use bicyle most of the time and rest at Piata Avram Iancu 2. No more than 16 kms Expect to spend around $139, and we're only considering places 4,8 stars.",
        {'entities': [(22, 40, 'LOCATION'), (53, 61, 'ATTRACTIONS_COUNT'), (73, 79, 'TRANSPORT'), (109, 128, 'ADDRESS'), (143, 149, 'MAX_DISTANCE'), (173, 177, 'MAX_PRICE'), (213, 222, 'MIN_RATING')]}
    ),
    (
        "We’re off to Iasi, Romania, want to visit 10 landmarks and will be using bicyle. Accommodation is Calea Bucuresti 22. Distance cap: 15 km Expect to spend around 195 dollars, and we're only considering places rated 3,8/5.",
        {'entities': [(13, 26, 'LOCATION'), (42, 54, 'ATTRACTIONS_COUNT'), (73, 79, 'TRANSPORT'), (98, 116, 'ADDRESS'), (132, 137, 'MAX_DISTANCE'), (161, 172, 'MAX_PRICE'), (208, 219, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Satu Mare, Romania, aiming for 9 monuments. We'll use bike most of the time and rest at Bd Independentei 14. No more than 28 km Expect to spend around 232 USD, and we're only considering places 4,3 stars.",
        {'entities': [(22, 40, 'LOCATION'), (53, 64, 'ATTRACTIONS_COUNT'), (76, 80, 'TRANSPORT'), (110, 129, 'ADDRESS'), (144, 149, 'MAX_DISTANCE'), (173, 180, 'MAX_PRICE'), (216, 225, 'MIN_RATING')]}
    ),
    (
        "Visiting Constanta, Romania soon! Plan is to cover 2 monuments by walk. We'll lodge at Strada Horea 7, aiming not to exceed 25 km Expect to spend around 215 USD, and we're only considering places at least 3,9★.",
        {'entities': [(9, 27, 'LOCATION'), (51, 62, 'ATTRACTIONS_COUNT'), (66, 70, 'TRANSPORT'), (87, 101, 'ADDRESS'), (124, 129, 'MAX_DISTANCE'), (153, 160, 'MAX_PRICE'), (196, 209, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Satu Mare, Romania where we hope to check out 4 landmarks. Mostly walk, staying at Bd George Cosbuc 33, and keeping to 18 kilometes Expect to spend around 256 EUR, and we're only considering places 49/10 score.",
        {'entities': [(20, 38, 'LOCATION'), (66, 77, 'ATTRACTIONS_COUNT'), (86, 90, 'TRANSPORT'), (103, 122, 'ADDRESS'), (139, 151, 'MAX_DISTANCE'), (175, 182, 'MAX_PRICE'), (218, 229, 'MIN_RATING')]}
    ),
    (
        "Heading to Arad, Romania, planning for 5 things, moving around by car, and staying at Bd Independentei 14. Targeting 22 kms max Expect to spend around 259 USD, and we're only considering places 94 points.",
        {'entities': [(11, 24, 'LOCATION'), (39, 47, 'ATTRACTIONS_COUNT'), (66, 69, 'TRANSPORT'), (86, 105, 'ADDRESS'), (117, 123, 'MAX_DISTANCE'), (151, 158, 'MAX_PRICE'), (194, 203, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Bucharest, Romania. I’d like to visit 5 monuments, mainly by foot, and stay at Str Vasile Lucaciu 9. I hope to keep it under 12 kilometres Expect to spend around 143 dollars, and we're only considering places 80 points.",
        {'entities': [(23, 41, 'LOCATION'), (61, 72, 'ATTRACTIONS_COUNT'), (84, 88, 'TRANSPORT'), (102, 122, 'ADDRESS'), (148, 161, 'MAX_DISTANCE'), (185, 196, 'MAX_PRICE'), (232, 241, 'MIN_RATING')]}
    ),
    (
        "We’re off to Bacau, Romania, want to visit 4 spots and will be using bike. Accommodation is Piata Avram Iancu 2. Distance cap: 20 km Expect to spend around 257 dollars, and we're only considering places rated 3,8/5.",
        {'entities': [(13, 27, 'LOCATION'), (43, 50, 'ATTRACTIONS_COUNT'), (69, 73, 'TRANSPORT'), (92, 111, 'ADDRESS'), (127, 132, 'MAX_DISTANCE'), (156, 167, 'MAX_PRICE'), (203, 214, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Timisoara, Romania—hoping to visit 10 monuments via bike. Our spot: Strada Mihai Eminescu 8. Distance? Around 16 kms Expect to spend around 68 EUR, and we're only considering places 4,9 stars.",
        {'entities': [(12, 30, 'LOCATION'), (47, 59, 'ATTRACTIONS_COUNT'), (64, 68, 'TRANSPORT'), (80, 103, 'ADDRESS'), (122, 128, 'MAX_DISTANCE'), (152, 158, 'MAX_PRICE'), (194, 203, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Brasov, Romania where we hope to check out 3 landmarks. Mostly car, staying at Bd Independentei 14, and keeping to 24 kilometes Expect to spend around $275, and we're only considering places rated 5,0/5.",
        {'entities': [(20, 35, 'LOCATION'), (63, 74, 'ATTRACTIONS_COUNT'), (83, 86, 'TRANSPORT'), (99, 118, 'ADDRESS'), (135, 147, 'MAX_DISTANCE'), (171, 175, 'MAX_PRICE'), (211, 222, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Brasov, Romania—hoping to visit 8 sights via car. Our spot: Piata Avram Iancu 2. Distance? Around 30 km Expect to spend around 68 EUR, and we're only considering places at least 4,7★.",
        {'entities': [(12, 27, 'LOCATION'), (44, 52, 'ATTRACTIONS_COUNT'), (57, 60, 'TRANSPORT'), (72, 91, 'ADDRESS'), (110, 115, 'MAX_DISTANCE'), (139, 145, 'MAX_PRICE'), (181, 194, 'MIN_RATING')]}
    ),
    (
        "Visiting Bacau, Romania soon! Plan is to cover 6 attr by bicyle. We'll lodge at Strada Mihai Eminescu 8, aiming not to exceed 16 kms Expect to spend around $166, and we're only considering places 40/10 score.",
        {'entities': [(9, 23, 'LOCATION'), (47, 53, 'ATTRACTIONS_COUNT'), (57, 63, 'TRANSPORT'), (80, 103, 'ADDRESS'), (126, 132, 'MAX_DISTANCE'), (156, 160, 'MAX_PRICE'), (196, 207, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Arad, Romania. I’d like to visit 10 spots, mainly by foot, and stay at Strada Libertatii 15. I hope to keep it under 16 kms Expect to spend around 254 RON, and we're only considering places rated 4,2/5.",
        {'entities': [(23, 36, 'LOCATION'), (56, 64, 'ATTRACTIONS_COUNT'), (76, 80, 'TRANSPORT'), (94, 114, 'ADDRESS'), (140, 146, 'MAX_DISTANCE'), (170, 177, 'MAX_PRICE'), (213, 224, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Ploiesti, Romania—hoping to visit 7 sights via car. Our spot: Piata Avram Iancu 2. Distance? Around 35 km Expect to spend around 144 EUR, and we're only considering places 4,0 stars.",
        {'entities': [(12, 29, 'LOCATION'), (46, 54, 'ATTRACTIONS_COUNT'), (59, 62, 'TRANSPORT'), (74, 93, 'ADDRESS'), (112, 117, 'MAX_DISTANCE'), (141, 148, 'MAX_PRICE'), (184, 193, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Iasi, Romania—hoping to visit 3 spots via car. Our spot: Strada Memorandumului 5. Distance? Around 16 kms Expect to spend around 249 dollars, and we're only considering places 74 points.",
        {'entities': [(12, 25, 'LOCATION'), (42, 49, 'ATTRACTIONS_COUNT'), (54, 57, 'TRANSPORT'), (69, 92, 'ADDRESS'), (111, 117, 'MAX_DISTANCE'), (141, 152, 'MAX_PRICE'), (188, 197, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Baia Mare, Romania. I’d like to visit 10 attractons, mainly by walk, and stay at Strada Memorandumului 5. I hope to keep it under 20 km Expect to spend around 178 dollars, and we're only considering places 84 points.",
        {'entities': [(23, 41, 'LOCATION'), (61, 74, 'ATTRACTIONS_COUNT'), (86, 90, 'TRANSPORT'), (104, 127, 'ADDRESS'), (153, 158, 'MAX_DISTANCE'), (182, 193, 'MAX_PRICE'), (229, 238, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Sibiu, Romania where we hope to check out 3 atr. Mostly car, staying at Strada Libertatii 15, and keeping to 30 km Expect to spend around 198 dollars, and we're only considering places 84 points.",
        {'entities': [(20, 34, 'LOCATION'), (62, 67, 'ATTRACTIONS_COUNT'), (76, 79, 'TRANSPORT'), (92, 112, 'ADDRESS'), (129, 134, 'MAX_DISTANCE'), (158, 169, 'MAX_PRICE'), (205, 214, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Brasov, Romania—hoping to visit 4 places via bike. Our spot: Strada Memorandumului 5. Distance? Around 12 kilometres Expect to spend around 152 EUR, and we're only considering places 45/10 score.",
        {'entities': [(12, 27, 'LOCATION'), (44, 52, 'ATTRACTIONS_COUNT'), (57, 61, 'TRANSPORT'), (73, 96, 'ADDRESS'), (115, 128, 'MAX_DISTANCE'), (152, 159, 'MAX_PRICE'), (195, 206, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Constanta, Romania—hoping to visit 9 places via bike. Our spot: Bd George Cosbuc 33. Distance? Around 12 kilometres Expect to spend around 291 EUR, and we're only considering places 40/10 score.",
        {'entities': [(12, 30, 'LOCATION'), (47, 55, 'ATTRACTIONS_COUNT'), (60, 64, 'TRANSPORT'), (76, 95, 'ADDRESS'), (114, 127, 'MAX_DISTANCE'), (151, 158, 'MAX_PRICE'), (194, 205, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Bacau, Romania. I’d like to visit 6 places, mainly by bus, and stay at Strada Libertatii 15. I hope to keep it under 18 kilometes Expect to spend around 87 dollars, and we're only considering places at least 4,9★.",
        {'entities': [(23, 37, 'LOCATION'), (57, 65, 'ATTRACTIONS_COUNT'), (77, 80, 'TRANSPORT'), (94, 114, 'ADDRESS'), (140, 152, 'MAX_DISTANCE'), (176, 186, 'MAX_PRICE'), (222, 235, 'MIN_RATING')]}
    ),
    (
        "Heading to Constanta, Romania, planning for 7 atr, moving around by bicyle, and staying at Strada Mihai Eminescu 8. Targeting 25 km max Expect to spend around 219 USD, and we're only considering places at least 4,3★.",
        {'entities': [(11, 29, 'LOCATION'), (44, 49, 'ATTRACTIONS_COUNT'), (68, 74, 'TRANSPORT'), (91, 114, 'ADDRESS'), (126, 131, 'MAX_DISTANCE'), (159, 166, 'MAX_PRICE'), (202, 215, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Ploiesti, Romania where we hope to check out 10 attractions. Mostly foot, staying at Piata Avram Iancu 2, and keeping to 16 kms Expect to spend around $86, and we're only considering places at least 4,9★.",
        {'entities': [(20, 37, 'LOCATION'), (65, 79, 'ATTRACTIONS_COUNT'), (88, 92, 'TRANSPORT'), (105, 124, 'ADDRESS'), (141, 147, 'MAX_DISTANCE'), (171, 174, 'MAX_PRICE'), (210, 223, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bacau, Romania where we hope to check out 3 spots. Mostly bus, staying at Strada Memorandumului 5, and keeping to 10 km Expect to spend around 242 dollars, and we're only considering places 4,7 stars.",
        {'entities': [(20, 34, 'LOCATION'), (62, 69, 'ATTRACTIONS_COUNT'), (78, 81, 'TRANSPORT'), (94, 117, 'ADDRESS'), (134, 139, 'MAX_DISTANCE'), (163, 174, 'MAX_PRICE'), (210, 219, 'MIN_RATING')]}
    ),
    (
        "Visiting Cluj Napoca, Romania soon! Plan is to cover 5 attractons by train. We'll lodge at Piata Avram Iancu 2, aiming not to exceed 16 kms Expect to spend around 178 RON, and we're only considering places 48/10 score.",
        {'entities': [(9, 29, 'LOCATION'), (53, 65, 'ATTRACTIONS_COUNT'), (69, 74, 'TRANSPORT'), (91, 110, 'ADDRESS'), (133, 139, 'MAX_DISTANCE'), (163, 170, 'MAX_PRICE'), (206, 217, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Pitesti, Romania where we hope to check out 3 monuments. Mostly foot, staying at Bd Mamaia 15, and keeping to 16 kms Expect to spend around 78 EUR, and we're only considering places 4,7 stars.",
        {'entities': [(20, 36, 'LOCATION'), (64, 75, 'ATTRACTIONS_COUNT'), (84, 88, 'TRANSPORT'), (101, 113, 'ADDRESS'), (130, 136, 'MAX_DISTANCE'), (160, 166, 'MAX_PRICE'), (202, 211, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Timisoara, Romania—hoping to visit 2 places via bike. Our spot: Bd Mamaia 15. Distance? Around 25 km Expect to spend around 205 EUR, and we're only considering places rated 4,3/5.",
        {'entities': [(12, 30, 'LOCATION'), (47, 55, 'ATTRACTIONS_COUNT'), (60, 64, 'TRANSPORT'), (76, 88, 'ADDRESS'), (107, 112, 'MAX_DISTANCE'), (136, 143, 'MAX_PRICE'), (179, 190, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Cluj Napoca, Romania where we hope to check out 8 things. Mostly bus, staying at Bd Independentei 14, and keeping to 12 kilometres Expect to spend around 74 EUR, and we're only considering places 4,3 stars.",
        {'entities': [(20, 40, 'LOCATION'), (68, 76, 'ATTRACTIONS_COUNT'), (85, 88, 'TRANSPORT'), (101, 120, 'ADDRESS'), (137, 150, 'MAX_DISTANCE'), (174, 180, 'MAX_PRICE'), (216, 225, 'MIN_RATING')]}
    ),
    (
        "Heading to Bucharest, Romania, planning for 4 landmarks, moving around by foot, and staying at Str Vasile Lucaciu 9. Targeting 35 km max Expect to spend around 110 EUR, and we're only considering places 4,6 stars.",
        {'entities': [(11, 29, 'LOCATION'), (44, 55, 'ATTRACTIONS_COUNT'), (74, 78, 'TRANSPORT'), (95, 115, 'ADDRESS'), (127, 132, 'MAX_DISTANCE'), (160, 167, 'MAX_PRICE'), (203, 212, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Bacau, Romania, aiming for 7 things. We'll use foot most of the time and rest at Calea Bucuresti 22. No more than 10 km Expect to spend around $293, and we're only considering places rated 3,7/5.",
        {'entities': [(22, 36, 'LOCATION'), (49, 57, 'ATTRACTIONS_COUNT'), (69, 73, 'TRANSPORT'), (103, 121, 'ADDRESS'), (136, 141, 'MAX_DISTANCE'), (165, 169, 'MAX_PRICE'), (205, 216, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Targu Mures, Romania where we hope to check out 4 spots. Mostly bus, staying at Bd Mamaia 15, and keeping to 12 kilometres Expect to spend around 178 EUR, and we're only considering places rated 4,3/5.",
        {'entities': [(20, 40, 'LOCATION'), (68, 75, 'ATTRACTIONS_COUNT'), (84, 87, 'TRANSPORT'), (100, 112, 'ADDRESS'), (129, 142, 'MAX_DISTANCE'), (166, 173, 'MAX_PRICE'), (209, 220, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Pitesti, Romania—hoping to visit 7 monuments via bicyle. Our spot: Strada Horea 7. Distance? Around 12 kilometres Expect to spend around 125 RON, and we're only considering places 47/10 score.",
        {'entities': [(12, 28, 'LOCATION'), (45, 56, 'ATTRACTIONS_COUNT'), (61, 67, 'TRANSPORT'), (79, 93, 'ADDRESS'), (112, 125, 'MAX_DISTANCE'), (149, 156, 'MAX_PRICE'), (192, 203, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Timisoara, Romania—hoping to visit 6 attr via train. Our spot: Str Vasile Lucaciu 9. Distance? Around 12 kilometres Expect to spend around $108, and we're only considering places 4,5 stars.",
        {'entities': [(12, 30, 'LOCATION'), (47, 53, 'ATTRACTIONS_COUNT'), (58, 63, 'TRANSPORT'), (75, 95, 'ADDRESS'), (114, 127, 'MAX_DISTANCE'), (151, 155, 'MAX_PRICE'), (191, 200, 'MIN_RATING')]}
    ),
    (
        "Heading to Bacau, Romania, planning for 9 atr, moving around by bus, and staying at Strada Memorandumului 5. Targeting 18 kilometes max Expect to spend around 102 RON, and we're only considering places rated 4,4/5.",
        {'entities': [(11, 25, 'LOCATION'), (40, 45, 'ATTRACTIONS_COUNT'), (64, 67, 'TRANSPORT'), (84, 107, 'ADDRESS'), (119, 131, 'MAX_DISTANCE'), (159, 166, 'MAX_PRICE'), (202, 213, 'MIN_RATING')]}
    ),
    (
        "Visiting Targu Mures, Romania soon! Plan is to cover 5 things by train. We'll lodge at Strada Libertatii 15, aiming not to exceed 10 km Expect to spend around $132, and we're only considering places 3,9 stars.",
        {'entities': [(9, 29, 'LOCATION'), (53, 61, 'ATTRACTIONS_COUNT'), (65, 70, 'TRANSPORT'), (87, 107, 'ADDRESS'), (130, 135, 'MAX_DISTANCE'), (159, 163, 'MAX_PRICE'), (199, 208, 'MIN_RATING')]}
    ),
    (
        "We’re off to Bucharest, Romania, want to visit 2 places and will be using foot. Accommodation is Str Vasile Lucaciu 9. Distance cap: 16 kms Expect to spend around $108, and we're only considering places 70 points.",
        {'entities': [(13, 31, 'LOCATION'), (47, 55, 'ATTRACTIONS_COUNT'), (74, 78, 'TRANSPORT'), (97, 117, 'ADDRESS'), (133, 139, 'MAX_DISTANCE'), (163, 167, 'MAX_PRICE'), (203, 212, 'MIN_RATING')]}
    ),
    (
        "Heading to Bucharest, Romania, planning for 5 spots, moving around by bus, and staying at Bd Independentei 14. Targeting 24 kilometes max Expect to spend around 274 dollars, and we're only considering places 4,9 stars.",
        {'entities': [(11, 29, 'LOCATION'), (44, 51, 'ATTRACTIONS_COUNT'), (70, 73, 'TRANSPORT'), (90, 109, 'ADDRESS'), (121, 133, 'MAX_DISTANCE'), (161, 172, 'MAX_PRICE'), (208, 217, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Constanta, Romania—hoping to visit 9 atts via train. Our spot: Strada Mihai Eminescu 8. Distance? Around 25 km Expect to spend around $179, and we're only considering places 37/10 score.",
        {'entities': [(12, 30, 'LOCATION'), (47, 53, 'ATTRACTIONS_COUNT'), (58, 63, 'TRANSPORT'), (75, 98, 'ADDRESS'), (117, 122, 'MAX_DISTANCE'), (146, 150, 'MAX_PRICE'), (186, 197, 'MIN_RATING')]}
    ),
    (
        "Visiting Ploiesti, Romania soon! Plan is to cover 5 monuments by foot. We'll lodge at Piata Avram Iancu 2, aiming not to exceed 24 kilometes Expect to spend around 283 EUR, and we're only considering places rated 4,9/5.",
        {'entities': [(9, 26, 'LOCATION'), (50, 61, 'ATTRACTIONS_COUNT'), (65, 69, 'TRANSPORT'), (86, 105, 'ADDRESS'), (128, 140, 'MAX_DISTANCE'), (164, 171, 'MAX_PRICE'), (207, 218, 'MIN_RATING')]}
    ),
    (
        "Heading to Targu Mures, Romania, planning for 4 attr, moving around by walk, and staying at Strada Memorandumului 5. Targeting 15 km max Expect to spend around 261 EUR, and we're only considering places rated 3,9/5.",
        {'entities': [(11, 31, 'LOCATION'), (46, 52, 'ATTRACTIONS_COUNT'), (71, 75, 'TRANSPORT'), (92, 115, 'ADDRESS'), (127, 132, 'MAX_DISTANCE'), (160, 167, 'MAX_PRICE'), (203, 214, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Ploiesti, Romania—hoping to visit 1 attractons via foot. Our spot: Calea Bucuresti 22. Distance? Around 25 km Expect to spend around 166 RON, and we're only considering places rated 4,0/5.",
        {'entities': [(12, 29, 'LOCATION'), (46, 58, 'ATTRACTIONS_COUNT'), (63, 67, 'TRANSPORT'), (79, 97, 'ADDRESS'), (116, 121, 'MAX_DISTANCE'), (145, 152, 'MAX_PRICE'), (188, 199, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Ploiesti, Romania, aiming for 7 attractons. We'll use car most of the time and rest at Strada Mihai Eminescu 8. No more than 20 km Expect to spend around 224 RON, and we're only considering places at least 3,5★.",
        {'entities': [(22, 39, 'LOCATION'), (52, 64, 'ATTRACTIONS_COUNT'), (76, 79, 'TRANSPORT'), (109, 132, 'ADDRESS'), (147, 152, 'MAX_DISTANCE'), (176, 183, 'MAX_PRICE'), (219, 232, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bucharest, Romania where we hope to check out 3 things. Mostly train, staying at Bd Mamaia 15, and keeping to 15 km Expect to spend around 190 USD, and we're only considering places 3,7 stars.",
        {'entities': [(20, 38, 'LOCATION'), (66, 74, 'ATTRACTIONS_COUNT'), (83, 88, 'TRANSPORT'), (101, 113, 'ADDRESS'), (130, 135, 'MAX_DISTANCE'), (159, 166, 'MAX_PRICE'), (202, 211, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Pitesti, Romania—hoping to visit 9 things via car. Our spot: Strada Mihai Eminescu 8. Distance? Around 15 km Expect to spend around $119, and we're only considering places 4,9 stars.",
        {'entities': [(12, 28, 'LOCATION'), (45, 53, 'ATTRACTIONS_COUNT'), (58, 61, 'TRANSPORT'), (73, 96, 'ADDRESS'), (115, 120, 'MAX_DISTANCE'), (144, 148, 'MAX_PRICE'), (184, 193, 'MIN_RATING')]}
    ),
    (
        "Visiting Baia Mare, Romania soon! Plan is to cover 6 places by train. We'll lodge at Strada Libertatii 15, aiming not to exceed 15 km Expect to spend around 149 RON, and we're only considering places 4,5 stars.",
        {'entities': [(9, 27, 'LOCATION'), (51, 59, 'ATTRACTIONS_COUNT'), (63, 68, 'TRANSPORT'), (85, 105, 'ADDRESS'), (128, 133, 'MAX_DISTANCE'), (157, 164, 'MAX_PRICE'), (200, 209, 'MIN_RATING')]}
    ),
    (
        "Visiting Cluj Napoca, Romania soon! Plan is to cover 9 things by bus. We'll lodge at Strada Libertatii 15, aiming not to exceed 28 km Expect to spend around $225, and we're only considering places at least 3,6★.",
        {'entities': [(9, 29, 'LOCATION'), (53, 61, 'ATTRACTIONS_COUNT'), (65, 68, 'TRANSPORT'), (85, 105, 'ADDRESS'), (128, 133, 'MAX_DISTANCE'), (157, 161, 'MAX_PRICE'), (197, 210, 'MIN_RATING')]}
    ),
    (
        "We’re off to Bacau, Romania, want to visit 4 landmarks and will be using bicyle. Accommodation is Strada Memorandumului 5. Distance cap: 20 km Expect to spend around 169 dollars, and we're only considering places 4,6 stars.",
        {'entities': [(13, 27, 'LOCATION'), (43, 54, 'ATTRACTIONS_COUNT'), (73, 79, 'TRANSPORT'), (98, 121, 'ADDRESS'), (137, 142, 'MAX_DISTANCE'), (166, 177, 'MAX_PRICE'), (213, 222, 'MIN_RATING')]}
    ),
    (
        "Visiting Arad, Romania soon! Plan is to cover 8 things by bike. We'll lodge at Calea Bucuresti 22, aiming not to exceed 30 km Expect to spend around 199 RON, and we're only considering places 3,9 stars.",
        {'entities': [(9, 22, 'LOCATION'), (46, 54, 'ATTRACTIONS_COUNT'), (58, 62, 'TRANSPORT'), (79, 97, 'ADDRESS'), (120, 125, 'MAX_DISTANCE'), (149, 156, 'MAX_PRICE'), (192, 201, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bacau, Romania where we hope to check out 5 atr. Mostly foot, staying at Str Vasile Lucaciu 9, and keeping to 12 kilometres Expect to spend around 103 dollars, and we're only considering places rated 4,6/5.",
        {'entities': [(20, 34, 'LOCATION'), (62, 67, 'ATTRACTIONS_COUNT'), (76, 80, 'TRANSPORT'), (93, 113, 'ADDRESS'), (130, 143, 'MAX_DISTANCE'), (167, 178, 'MAX_PRICE'), (214, 225, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Galati, Romania where we hope to check out 2 attractions. Mostly bike, staying at Bd Mamaia 15, and keeping to 22 kms Expect to spend around 258 RON, and we're only considering places rated 3,5/5.",
        {'entities': [(20, 35, 'LOCATION'), (63, 76, 'ATTRACTIONS_COUNT'), (85, 89, 'TRANSPORT'), (102, 114, 'ADDRESS'), (131, 137, 'MAX_DISTANCE'), (161, 168, 'MAX_PRICE'), (204, 215, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Bucharest, Romania—hoping to visit 2 spots via bike. Our spot: Strada Libertatii 15. Distance? Around 35 km Expect to spend around $227, and we're only considering places at least 3,6★.",
        {'entities': [(12, 30, 'LOCATION'), (47, 54, 'ATTRACTIONS_COUNT'), (59, 63, 'TRANSPORT'), (75, 95, 'ADDRESS'), (114, 119, 'MAX_DISTANCE'), (143, 147, 'MAX_PRICE'), (183, 196, 'MIN_RATING')]}
    ),
    (
        "Heading to Baia Mare, Romania, planning for 3 monuments, moving around by bicyle, and staying at Strada Mihai Eminescu 8. Targeting 10 km max Expect to spend around 289 USD, and we're only considering places 82 points.",
        {'entities': [(11, 29, 'LOCATION'), (44, 55, 'ATTRACTIONS_COUNT'), (74, 80, 'TRANSPORT'), (97, 120, 'ADDRESS'), (132, 137, 'MAX_DISTANCE'), (165, 172, 'MAX_PRICE'), (208, 217, 'MIN_RATING')]}
    ),
    (
        "We’re off to Arad, Romania, want to visit 10 attractions and will be using bike. Accommodation is Strada Horea 7. Distance cap: 28 km Expect to spend around 291 RON, and we're only considering places 37/10 score.",
        {'entities': [(13, 26, 'LOCATION'), (42, 56, 'ATTRACTIONS_COUNT'), (75, 79, 'TRANSPORT'), (98, 112, 'ADDRESS'), (128, 133, 'MAX_DISTANCE'), (157, 164, 'MAX_PRICE'), (200, 211, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Baia Mare, Romania, aiming for 10 attractions. We'll use train most of the time and rest at Bd Independentei 14. No more than 28 km Expect to spend around 67 USD, and we're only considering places at least 4,2★.",
        {'entities': [(22, 40, 'LOCATION'), (53, 67, 'ATTRACTIONS_COUNT'), (79, 84, 'TRANSPORT'), (114, 133, 'ADDRESS'), (148, 153, 'MAX_DISTANCE'), (177, 183, 'MAX_PRICE'), (219, 232, 'MIN_RATING')]}
    ),
    (
        "We’re off to Ploiesti, Romania, want to visit 4 atts and will be using bicyle. Accommodation is Strada Mihai Eminescu 8. Distance cap: 10 km Expect to spend around $159, and we're only considering places 47/10 score.",
        {'entities': [(13, 30, 'LOCATION'), (46, 52, 'ATTRACTIONS_COUNT'), (71, 77, 'TRANSPORT'), (96, 119, 'ADDRESS'), (135, 140, 'MAX_DISTANCE'), (164, 168, 'MAX_PRICE'), (204, 215, 'MIN_RATING')]}
    ),
    (
        "Visiting Brasov, Romania soon! Plan is to cover 5 spots by bicyle. We'll lodge at Strada Libertatii 15, aiming not to exceed 20 km Expect to spend around 140 RON, and we're only considering places at least 4,8★.",
        {'entities': [(9, 24, 'LOCATION'), (48, 55, 'ATTRACTIONS_COUNT'), (59, 65, 'TRANSPORT'), (82, 102, 'ADDRESS'), (125, 130, 'MAX_DISTANCE'), (154, 161, 'MAX_PRICE'), (197, 210, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Constanta, Romania, aiming for 1 atts. We'll use bike most of the time and rest at Strada Mihai Eminescu 8. No more than 24 kilometes Expect to spend around 194 USD, and we're only considering places 72 points.",
        {'entities': [(22, 40, 'LOCATION'), (53, 59, 'ATTRACTIONS_COUNT'), (71, 75, 'TRANSPORT'), (105, 128, 'ADDRESS'), (143, 155, 'MAX_DISTANCE'), (179, 186, 'MAX_PRICE'), (222, 231, 'MIN_RATING')]}
    ),
    (
        "Visiting Pitesti, Romania soon! Plan is to cover 2 attr by walk. We'll lodge at Bd Independentei 14, aiming not to exceed 15 km Expect to spend around 268 RON, and we're only considering places at least 4,3★.",
        {'entities': [(9, 25, 'LOCATION'), (49, 55, 'ATTRACTIONS_COUNT'), (59, 63, 'TRANSPORT'), (80, 99, 'ADDRESS'), (122, 127, 'MAX_DISTANCE'), (151, 158, 'MAX_PRICE'), (194, 207, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Bucharest, Romania. I’d like to visit 5 places, mainly by train, and stay at Strada Libertatii 15. I hope to keep it under 28 km Expect to spend around 239 EUR, and we're only considering places 4,7 stars.",
        {'entities': [(23, 41, 'LOCATION'), (61, 69, 'ATTRACTIONS_COUNT'), (81, 86, 'TRANSPORT'), (100, 120, 'ADDRESS'), (146, 151, 'MAX_DISTANCE'), (175, 182, 'MAX_PRICE'), (218, 227, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Arad, Romania where we hope to check out 9 things. Mostly bicyle, staying at Strada Horea 7, and keeping to 10 km Expect to spend around 93 EUR, and we're only considering places rated 4,9/5.",
        {'entities': [(20, 33, 'LOCATION'), (61, 69, 'ATTRACTIONS_COUNT'), (78, 84, 'TRANSPORT'), (97, 111, 'ADDRESS'), (128, 133, 'MAX_DISTANCE'), (157, 163, 'MAX_PRICE'), (199, 210, 'MIN_RATING')]}
    ),
    (
        "Heading to Satu Mare, Romania, planning for 2 atts, moving around by walk, and staying at Str Vasile Lucaciu 9. Targeting 15 km max Expect to spend around $184, and we're only considering places 84 points.",
        {'entities': [(11, 29, 'LOCATION'), (44, 50, 'ATTRACTIONS_COUNT'), (69, 73, 'TRANSPORT'), (90, 110, 'ADDRESS'), (122, 127, 'MAX_DISTANCE'), (155, 159, 'MAX_PRICE'), (195, 204, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Bucharest, Romania—hoping to visit 1 landmarks via bike. Our spot: Strada Horea 7. Distance? Around 18 kilometes Expect to spend around 160 RON, and we're only considering places at least 4,8★.",
        {'entities': [(12, 30, 'LOCATION'), (47, 58, 'ATTRACTIONS_COUNT'), (63, 67, 'TRANSPORT'), (79, 93, 'ADDRESS'), (112, 124, 'MAX_DISTANCE'), (148, 155, 'MAX_PRICE'), (191, 204, 'MIN_RATING')]}
    ),
    (
        "Visiting Bacau, Romania soon! Plan is to cover 6 landmarks by foot. We'll lodge at Strada Libertatii 15, aiming not to exceed 16 kms Expect to spend around 293 USD, and we're only considering places 70 points.",
        {'entities': [(9, 23, 'LOCATION'), (47, 58, 'ATTRACTIONS_COUNT'), (62, 66, 'TRANSPORT'), (83, 103, 'ADDRESS'), (126, 132, 'MAX_DISTANCE'), (156, 163, 'MAX_PRICE'), (199, 208, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Sibiu, Romania—hoping to visit 6 attractons via foot. Our spot: Strada Libertatii 15. Distance? Around 15 km Expect to spend around $73, and we're only considering places 47/10 score.",
        {'entities': [(12, 26, 'LOCATION'), (43, 55, 'ATTRACTIONS_COUNT'), (60, 64, 'TRANSPORT'), (76, 96, 'ADDRESS'), (115, 120, 'MAX_DISTANCE'), (144, 147, 'MAX_PRICE'), (183, 194, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Constanta, Romania where we hope to check out 3 atts. Mostly bicyle, staying at Str Vasile Lucaciu 9, and keeping to 24 kilometes Expect to spend around $293, and we're only considering places 78 points.",
        {'entities': [(20, 38, 'LOCATION'), (66, 72, 'ATTRACTIONS_COUNT'), (81, 87, 'TRANSPORT'), (100, 120, 'ADDRESS'), (137, 149, 'MAX_DISTANCE'), (173, 177, 'MAX_PRICE'), (213, 222, 'MIN_RATING')]}
    ),
    (
        "Heading to Timisoara, Romania, planning for 5 atts, moving around by train, and staying at Piata Avram Iancu 2. Targeting 15 km max Expect to spend around 121 USD, and we're only considering places rated 4,3/5.",
        {'entities': [(11, 29, 'LOCATION'), (44, 50, 'ATTRACTIONS_COUNT'), (69, 74, 'TRANSPORT'), (91, 110, 'ADDRESS'), (122, 127, 'MAX_DISTANCE'), (155, 162, 'MAX_PRICE'), (198, 209, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Targu Mures, Romania—hoping to visit 9 places via bus. Our spot: Strada Horea 7. Distance? Around 25 km Expect to spend around 159 RON, and we're only considering places 4,8 stars.",
        {'entities': [(12, 32, 'LOCATION'), (49, 57, 'ATTRACTIONS_COUNT'), (62, 65, 'TRANSPORT'), (77, 91, 'ADDRESS'), (110, 115, 'MAX_DISTANCE'), (139, 146, 'MAX_PRICE'), (182, 191, 'MIN_RATING')]}
    ),
    (
        "We’re off to Ploiesti, Romania, want to visit 6 monuments and will be using bike. Accommodation is Calea Bucuresti 22. Distance cap: 15 km Expect to spend around 282 RON, and we're only considering places at least 4,7★.",
        {'entities': [(13, 30, 'LOCATION'), (46, 57, 'ATTRACTIONS_COUNT'), (76, 80, 'TRANSPORT'), (99, 117, 'ADDRESS'), (133, 138, 'MAX_DISTANCE'), (162, 169, 'MAX_PRICE'), (205, 218, 'MIN_RATING')]}
    ),
    (
        "Visiting Targu Mures, Romania soon! Plan is to cover 5 landmarks by bicyle. We'll lodge at Strada Mihai Eminescu 8, aiming not to exceed 28 km Expect to spend around 97 EUR, and we're only considering places 38/10 score.",
        {'entities': [(9, 29, 'LOCATION'), (53, 64, 'ATTRACTIONS_COUNT'), (68, 74, 'TRANSPORT'), (91, 114, 'ADDRESS'), (137, 142, 'MAX_DISTANCE'), (166, 172, 'MAX_PRICE'), (208, 219, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Ploiesti, Romania. I’d like to visit 1 atts, mainly by bike, and stay at Bd George Cosbuc 33. I hope to keep it under 16 kms Expect to spend around 298 EUR, and we're only considering places 90 points.",
        {'entities': [(23, 40, 'LOCATION'), (60, 66, 'ATTRACTIONS_COUNT'), (78, 82, 'TRANSPORT'), (96, 115, 'ADDRESS'), (141, 147, 'MAX_DISTANCE'), (171, 178, 'MAX_PRICE'), (214, 223, 'MIN_RATING')]}
    ),
    (
        "We’re off to Ploiesti, Romania, want to visit 10 landmarks and will be using train. Accommodation is Bd Independentei 14. Distance cap: 28 km Expect to spend around 67 EUR, and we're only considering places at least 4,3★.",
        {'entities': [(13, 30, 'LOCATION'), (46, 58, 'ATTRACTIONS_COUNT'), (77, 82, 'TRANSPORT'), (101, 120, 'ADDRESS'), (136, 141, 'MAX_DISTANCE'), (165, 171, 'MAX_PRICE'), (207, 220, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Oradea, Romania where we hope to check out 8 atr. Mostly bike, staying at Piata Avram Iancu 2, and keeping to 12 kilometres Expect to spend around $96, and we're only considering places rated 4,1/5.",
        {'entities': [(20, 35, 'LOCATION'), (63, 68, 'ATTRACTIONS_COUNT'), (77, 81, 'TRANSPORT'), (94, 113, 'ADDRESS'), (130, 143, 'MAX_DISTANCE'), (167, 170, 'MAX_PRICE'), (206, 217, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Bacau, Romania. I’d like to visit 7 spots, mainly by train, and stay at Strada Horea 7. I hope to keep it under 28 km Expect to spend around 67 dollars, and we're only considering places at least 4,6★.",
        {'entities': [(23, 37, 'LOCATION'), (57, 64, 'ATTRACTIONS_COUNT'), (76, 81, 'TRANSPORT'), (95, 109, 'ADDRESS'), (135, 140, 'MAX_DISTANCE'), (164, 174, 'MAX_PRICE'), (210, 223, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Brasov, Romania, aiming for 6 attr. We'll use bicyle most of the time and rest at Strada Mihai Eminescu 8. No more than 22 kms Expect to spend around $190, and we're only considering places 47/10 score.",
        {'entities': [(22, 37, 'LOCATION'), (50, 56, 'ATTRACTIONS_COUNT'), (68, 74, 'TRANSPORT'), (104, 127, 'ADDRESS'), (142, 148, 'MAX_DISTANCE'), (172, 176, 'MAX_PRICE'), (212, 223, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Iasi, Romania, aiming for 7 attractons. We'll use bus most of the time and rest at Bd Mamaia 15. No more than 18 kilometes Expect to spend around 279 EUR, and we're only considering places 4,9 stars.",
        {'entities': [(22, 35, 'LOCATION'), (48, 60, 'ATTRACTIONS_COUNT'), (72, 75, 'TRANSPORT'), (105, 117, 'ADDRESS'), (132, 144, 'MAX_DISTANCE'), (168, 175, 'MAX_PRICE'), (211, 220, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Iasi, Romania. I’d like to visit 1 atr, mainly by bicyle, and stay at Strada Horea 7. I hope to keep it under 16 kms Expect to spend around 125 USD, and we're only considering places rated 4,7/5.",
        {'entities': [(23, 36, 'LOCATION'), (56, 61, 'ATTRACTIONS_COUNT'), (73, 79, 'TRANSPORT'), (93, 107, 'ADDRESS'), (133, 139, 'MAX_DISTANCE'), (163, 170, 'MAX_PRICE'), (206, 217, 'MIN_RATING')]}
    ),
    (
        "Heading to Galati, Romania, planning for 4 atr, moving around by foot, and staying at Str Vasile Lucaciu 9. Targeting 16 kms max Expect to spend around $74, and we're only considering places 98 points.",
        {'entities': [(11, 26, 'LOCATION'), (41, 46, 'ATTRACTIONS_COUNT'), (65, 69, 'TRANSPORT'), (86, 106, 'ADDRESS'), (118, 124, 'MAX_DISTANCE'), (152, 155, 'MAX_PRICE'), (191, 200, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Satu Mare, Romania. I’d like to visit 6 attr, mainly by bus, and stay at Bd George Cosbuc 33. I hope to keep it under 12 kilometres Expect to spend around 107 EUR, and we're only considering places 49/10 score.",
        {'entities': [(23, 41, 'LOCATION'), (61, 67, 'ATTRACTIONS_COUNT'), (79, 82, 'TRANSPORT'), (96, 115, 'ADDRESS'), (141, 154, 'MAX_DISTANCE'), (178, 185, 'MAX_PRICE'), (221, 232, 'MIN_RATING')]}
    ),
    (
        "Heading to Ploiesti, Romania, planning for 5 attractons, moving around by train, and staying at Strada Horea 7. Targeting 16 kms max Expect to spend around 120 dollars, and we're only considering places 4,7 stars.",
        {'entities': [(11, 28, 'LOCATION'), (43, 55, 'ATTRACTIONS_COUNT'), (74, 79, 'TRANSPORT'), (96, 110, 'ADDRESS'), (122, 128, 'MAX_DISTANCE'), (156, 167, 'MAX_PRICE'), (203, 212, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Bucharest, Romania, aiming for 8 landmarks. We'll use train most of the time and rest at Strada Memorandumului 5. No more than 25 km Expect to spend around 228 RON, and we're only considering places 42/10 score.",
        {'entities': [(22, 40, 'LOCATION'), (53, 64, 'ATTRACTIONS_COUNT'), (76, 81, 'TRANSPORT'), (111, 134, 'ADDRESS'), (149, 154, 'MAX_DISTANCE'), (178, 185, 'MAX_PRICE'), (221, 232, 'MIN_RATING')]}
    ),
    (
        "We’re off to Targu Mures, Romania, want to visit 7 things and will be using bus. Accommodation is Strada Mihai Eminescu 8. Distance cap: 18 kilometes Expect to spend around 96 EUR, and we're only considering places 96 points.",
        {'entities': [(13, 33, 'LOCATION'), (49, 57, 'ATTRACTIONS_COUNT'), (76, 79, 'TRANSPORT'), (98, 121, 'ADDRESS'), (137, 149, 'MAX_DISTANCE'), (173, 179, 'MAX_PRICE'), (215, 224, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Baia Mare, Romania where we hope to check out 4 attractions. Mostly bicyle, staying at Piata Avram Iancu 2, and keeping to 20 km Expect to spend around 172 EUR, and we're only considering places 96 points.",
        {'entities': [(20, 38, 'LOCATION'), (66, 79, 'ATTRACTIONS_COUNT'), (88, 94, 'TRANSPORT'), (107, 126, 'ADDRESS'), (143, 148, 'MAX_DISTANCE'), (172, 179, 'MAX_PRICE'), (215, 224, 'MIN_RATING')]}
    ),
    (
        "Heading to Baia Mare, Romania, planning for 5 atts, moving around by train, and staying at Bd Mamaia 15. Targeting 18 kilometes max Expect to spend around $138, and we're only considering places 90 points.",
        {'entities': [(11, 29, 'LOCATION'), (44, 50, 'ATTRACTIONS_COUNT'), (69, 74, 'TRANSPORT'), (91, 103, 'ADDRESS'), (115, 127, 'MAX_DISTANCE'), (155, 159, 'MAX_PRICE'), (195, 204, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Cluj Napoca, Romania. I’d like to visit 7 attractons, mainly by foot, and stay at Piata Avram Iancu 2. I hope to keep it under 30 km Expect to spend around 146 RON, and we're only considering places rated 4,8/5.",
        {'entities': [(23, 43, 'LOCATION'), (63, 75, 'ATTRACTIONS_COUNT'), (87, 91, 'TRANSPORT'), (105, 124, 'ADDRESS'), (150, 155, 'MAX_DISTANCE'), (179, 186, 'MAX_PRICE'), (222, 233, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Arad, Romania, aiming for 3 atr. We'll use train most of the time and rest at Strada Memorandumului 5. No more than 30 km Expect to spend around 223 dollars, and we're only considering places at least 4,3★.",
        {'entities': [(22, 35, 'LOCATION'), (48, 53, 'ATTRACTIONS_COUNT'), (65, 70, 'TRANSPORT'), (100, 123, 'ADDRESS'), (138, 143, 'MAX_DISTANCE'), (167, 178, 'MAX_PRICE'), (214, 227, 'MIN_RATING')]}
    ),
    (
        "Visiting Bucharest, Romania soon! Plan is to cover 4 spots by bike. We'll lodge at Piata Avram Iancu 2, aiming not to exceed 28 km Expect to spend around 190 USD, and we're only considering places rated 4,2/5.",
        {'entities': [(9, 27, 'LOCATION'), (51, 58, 'ATTRACTIONS_COUNT'), (62, 66, 'TRANSPORT'), (83, 102, 'ADDRESS'), (125, 130, 'MAX_DISTANCE'), (154, 161, 'MAX_PRICE'), (197, 208, 'MIN_RATING')]}
    ),
    (
        "Visiting Timisoara, Romania soon! Plan is to cover 8 attr by train. We'll lodge at Strada Memorandumului 5, aiming not to exceed 20 km Expect to spend around 145 RON, and we're only considering places at least 4,5★.",
        {'entities': [(9, 27, 'LOCATION'), (51, 57, 'ATTRACTIONS_COUNT'), (61, 66, 'TRANSPORT'), (83, 106, 'ADDRESS'), (129, 134, 'MAX_DISTANCE'), (158, 165, 'MAX_PRICE'), (201, 214, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Sibiu, Romania, aiming for 4 attractions. We'll use bus most of the time and rest at Bd Independentei 14. No more than 30 km Expect to spend around 61 dollars, and we're only considering places 74 points.",
        {'entities': [(22, 36, 'LOCATION'), (49, 62, 'ATTRACTIONS_COUNT'), (74, 77, 'TRANSPORT'), (107, 126, 'ADDRESS'), (141, 146, 'MAX_DISTANCE'), (170, 180, 'MAX_PRICE'), (216, 225, 'MIN_RATING')]}
    ),
    (
        "We’re off to Sibiu, Romania, want to visit 9 attractons and will be using bicyle. Accommodation is Bd Mamaia 15. Distance cap: 20 km Expect to spend around 160 EUR, and we're only considering places 49/10 score.",
        {'entities': [(13, 27, 'LOCATION'), (43, 55, 'ATTRACTIONS_COUNT'), (74, 80, 'TRANSPORT'), (99, 111, 'ADDRESS'), (127, 132, 'MAX_DISTANCE'), (156, 163, 'MAX_PRICE'), (199, 210, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Arad, Romania—hoping to visit 9 things via walk. Our spot: Strada Horea 7. Distance? Around 28 km Expect to spend around 200 dollars, and we're only considering places at least 4,6★.",
        {'entities': [(12, 25, 'LOCATION'), (42, 50, 'ATTRACTIONS_COUNT'), (55, 59, 'TRANSPORT'), (71, 85, 'ADDRESS'), (104, 109, 'MAX_DISTANCE'), (133, 144, 'MAX_PRICE'), (180, 193, 'MIN_RATING')]}
    ),
    (
        "Heading to Constanta, Romania, planning for 9 sights, moving around by car, and staying at Bd Independentei 14. Targeting 15 km max Expect to spend around $203, and we're only considering places rated 4,9/5.",
        {'entities': [(11, 29, 'LOCATION'), (44, 52, 'ATTRACTIONS_COUNT'), (71, 74, 'TRANSPORT'), (91, 110, 'ADDRESS'), (122, 127, 'MAX_DISTANCE'), (155, 159, 'MAX_PRICE'), (195, 206, 'MIN_RATING')]}
    ),
    (
        "Heading to Galati, Romania, planning for 7 monuments, moving around by bicyle, and staying at Strada Libertatii 15. Targeting 12 kilometres max Expect to spend around 159 dollars, and we're only considering places 44/10 score.",
        {'entities': [(11, 26, 'LOCATION'), (41, 52, 'ATTRACTIONS_COUNT'), (71, 77, 'TRANSPORT'), (94, 114, 'ADDRESS'), (126, 139, 'MAX_DISTANCE'), (167, 178, 'MAX_PRICE'), (214, 225, 'MIN_RATING')]}
    ),
    (
        "Heading to Bacau, Romania, planning for 8 attractions, moving around by foot, and staying at Strada Mihai Eminescu 8. Targeting 28 km max Expect to spend around 225 RON, and we're only considering places 4,1 stars.",
        {'entities': [(11, 25, 'LOCATION'), (40, 53, 'ATTRACTIONS_COUNT'), (72, 76, 'TRANSPORT'), (93, 116, 'ADDRESS'), (128, 133, 'MAX_DISTANCE'), (161, 168, 'MAX_PRICE'), (204, 213, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Constanta, Romania—hoping to visit 1 attractions via car. Our spot: Piata Avram Iancu 2. Distance? Around 12 kilometres Expect to spend around 230 dollars, and we're only considering places 82 points.",
        {'entities': [(12, 30, 'LOCATION'), (47, 60, 'ATTRACTIONS_COUNT'), (65, 68, 'TRANSPORT'), (80, 99, 'ADDRESS'), (118, 131, 'MAX_DISTANCE'), (155, 166, 'MAX_PRICE'), (202, 211, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Ploiesti, Romania where we hope to check out 5 atts. Mostly bicyle, staying at Bd Independentei 14, and keeping to 35 km Expect to spend around $139, and we're only considering places 3,6 stars.",
        {'entities': [(20, 37, 'LOCATION'), (65, 71, 'ATTRACTIONS_COUNT'), (80, 86, 'TRANSPORT'), (99, 118, 'ADDRESS'), (135, 140, 'MAX_DISTANCE'), (164, 168, 'MAX_PRICE'), (204, 213, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Constanta, Romania, aiming for 1 attractions. We'll use car most of the time and rest at Bd George Cosbuc 33. No more than 10 km Expect to spend around 80 RON, and we're only considering places 41/10 score.",
        {'entities': [(22, 40, 'LOCATION'), (53, 66, 'ATTRACTIONS_COUNT'), (78, 81, 'TRANSPORT'), (111, 130, 'ADDRESS'), (145, 150, 'MAX_DISTANCE'), (174, 180, 'MAX_PRICE'), (216, 227, 'MIN_RATING')]}
    ),
    (
        "Heading to Galati, Romania, planning for 4 monuments, moving around by foot, and staying at Bd Mamaia 15. Targeting 18 kilometes max Expect to spend around $276, and we're only considering places 36/10 score.",
        {'entities': [(11, 26, 'LOCATION'), (41, 52, 'ATTRACTIONS_COUNT'), (71, 75, 'TRANSPORT'), (92, 104, 'ADDRESS'), (116, 128, 'MAX_DISTANCE'), (156, 160, 'MAX_PRICE'), (196, 207, 'MIN_RATING')]}
    ),
    (
        "We’re off to Constanta, Romania, want to visit 5 attr and will be using foot. Accommodation is Str Vasile Lucaciu 9. Distance cap: 30 km Expect to spend around 292 EUR, and we're only considering places 100 points.",
        {'entities': [(13, 31, 'LOCATION'), (47, 53, 'ATTRACTIONS_COUNT'), (72, 76, 'TRANSPORT'), (95, 115, 'ADDRESS'), (131, 136, 'MAX_DISTANCE'), (160, 167, 'MAX_PRICE'), (203, 213, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Cluj Napoca, Romania. I’d like to visit 7 attr, mainly by foot, and stay at Calea Bucuresti 22. I hope to keep it under 30 km Expect to spend around 181 dollars, and we're only considering places 36/10 score.",
        {'entities': [(23, 43, 'LOCATION'), (63, 69, 'ATTRACTIONS_COUNT'), (81, 85, 'TRANSPORT'), (99, 117, 'ADDRESS'), (143, 148, 'MAX_DISTANCE'), (172, 183, 'MAX_PRICE'), (219, 230, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Timisoara, Romania where we hope to check out 7 atr. Mostly foot, staying at Calea Bucuresti 22, and keeping to 22 kms Expect to spend around 62 EUR, and we're only considering places 4,0 stars.",
        {'entities': [(20, 38, 'LOCATION'), (66, 71, 'ATTRACTIONS_COUNT'), (80, 84, 'TRANSPORT'), (97, 115, 'ADDRESS'), (132, 138, 'MAX_DISTANCE'), (162, 168, 'MAX_PRICE'), (204, 213, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Iasi, Romania, aiming for 1 atr. We'll use bicyle most of the time and rest at Strada Libertatii 15. No more than 35 km Expect to spend around 174 RON, and we're only considering places 37/10 score.",
        {'entities': [(22, 35, 'LOCATION'), (48, 53, 'ATTRACTIONS_COUNT'), (65, 71, 'TRANSPORT'), (101, 121, 'ADDRESS'), (136, 141, 'MAX_DISTANCE'), (165, 172, 'MAX_PRICE'), (208, 219, 'MIN_RATING')]}
    ),
    (
        "Heading to Cluj Napoca, Romania, planning for 10 attractons, moving around by bike, and staying at Piata Avram Iancu 2. Targeting 16 kms max Expect to spend around 282 dollars, and we're only considering places 4,4 stars.",
        {'entities': [(11, 31, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (78, 82, 'TRANSPORT'), (99, 118, 'ADDRESS'), (130, 136, 'MAX_DISTANCE'), (164, 175, 'MAX_PRICE'), (211, 220, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Bucharest, Romania, aiming for 4 sights. We'll use foot most of the time and rest at Bd Independentei 14. No more than 28 km Expect to spend around 269 EUR, and we're only considering places at least 4,5★.",
        {'entities': [(22, 40, 'LOCATION'), (53, 61, 'ATTRACTIONS_COUNT'), (73, 77, 'TRANSPORT'), (107, 126, 'ADDRESS'), (141, 146, 'MAX_DISTANCE'), (170, 177, 'MAX_PRICE'), (213, 226, 'MIN_RATING')]}
    ),
    (
        "We’re off to Sibiu, Romania, want to visit 4 sights and will be using car. Accommodation is Piata Avram Iancu 2. Distance cap: 28 km Expect to spend around 272 EUR, and we're only considering places at least 4,2★.",
        {'entities': [(13, 27, 'LOCATION'), (43, 51, 'ATTRACTIONS_COUNT'), (70, 73, 'TRANSPORT'), (92, 111, 'ADDRESS'), (127, 132, 'MAX_DISTANCE'), (156, 163, 'MAX_PRICE'), (199, 212, 'MIN_RATING')]}
    ),
    (
        "Heading to Baia Mare, Romania, planning for 1 landmarks, moving around by bike, and staying at Bd George Cosbuc 33. Targeting 24 kilometes max Expect to spend around 70 dollars, and we're only considering places 4,4 stars.",
        {'entities': [(11, 29, 'LOCATION'), (44, 55, 'ATTRACTIONS_COUNT'), (74, 78, 'TRANSPORT'), (95, 114, 'ADDRESS'), (126, 138, 'MAX_DISTANCE'), (166, 176, 'MAX_PRICE'), (212, 221, 'MIN_RATING')]}
    ),
    (
        "Heading to Ploiesti, Romania, planning for 9 attractons, moving around by car, and staying at Bd Mamaia 15. Targeting 22 kms max Expect to spend around 178 EUR, and we're only considering places at least 4,5★.",
        {'entities': [(11, 28, 'LOCATION'), (43, 55, 'ATTRACTIONS_COUNT'), (74, 77, 'TRANSPORT'), (94, 106, 'ADDRESS'), (118, 124, 'MAX_DISTANCE'), (152, 159, 'MAX_PRICE'), (195, 208, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Constanta, Romania, aiming for 9 atts. We'll use bicyle most of the time and rest at Piata Avram Iancu 2. No more than 18 kilometes Expect to spend around 272 RON, and we're only considering places 45/10 score.",
        {'entities': [(22, 40, 'LOCATION'), (53, 59, 'ATTRACTIONS_COUNT'), (71, 77, 'TRANSPORT'), (107, 126, 'ADDRESS'), (141, 153, 'MAX_DISTANCE'), (177, 184, 'MAX_PRICE'), (220, 231, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Iasi, Romania—hoping to visit 10 landmarks via foot. Our spot: Strada Horea 7. Distance? Around 20 km Expect to spend around 82 USD, and we're only considering places 35/10 score.",
        {'entities': [(12, 25, 'LOCATION'), (42, 54, 'ATTRACTIONS_COUNT'), (59, 63, 'TRANSPORT'), (75, 89, 'ADDRESS'), (108, 113, 'MAX_DISTANCE'), (137, 143, 'MAX_PRICE'), (179, 190, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Cluj Napoca, Romania where we hope to check out 7 spots. Mostly train, staying at Bd Mamaia 15, and keeping to 25 km Expect to spend around 186 EUR, and we're only considering places 38/10 score.",
        {'entities': [(20, 40, 'LOCATION'), (68, 75, 'ATTRACTIONS_COUNT'), (84, 89, 'TRANSPORT'), (102, 114, 'ADDRESS'), (131, 136, 'MAX_DISTANCE'), (160, 167, 'MAX_PRICE'), (203, 214, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Arad, Romania, aiming for 8 spots. We'll use bike most of the time and rest at Piata Avram Iancu 2. No more than 18 kilometes Expect to spend around 190 RON, and we're only considering places at least 4,7★.",
        {'entities': [(22, 35, 'LOCATION'), (48, 55, 'ATTRACTIONS_COUNT'), (67, 71, 'TRANSPORT'), (101, 120, 'ADDRESS'), (135, 147, 'MAX_DISTANCE'), (171, 178, 'MAX_PRICE'), (214, 227, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Baia Mare, Romania where we hope to check out 3 attr. Mostly bus, staying at Bd Independentei 14, and keeping to 30 km Expect to spend around 186 dollars, and we're only considering places 100 points.",
        {'entities': [(20, 38, 'LOCATION'), (66, 72, 'ATTRACTIONS_COUNT'), (81, 84, 'TRANSPORT'), (97, 116, 'ADDRESS'), (133, 138, 'MAX_DISTANCE'), (162, 173, 'MAX_PRICE'), (209, 219, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Galati, Romania where we hope to check out 7 atr. Mostly foot, staying at Bd Mamaia 15, and keeping to 18 kilometes Expect to spend around 167 dollars, and we're only considering places at least 4,2★.",
        {'entities': [(20, 35, 'LOCATION'), (63, 68, 'ATTRACTIONS_COUNT'), (77, 81, 'TRANSPORT'), (94, 106, 'ADDRESS'), (123, 135, 'MAX_DISTANCE'), (159, 170, 'MAX_PRICE'), (206, 219, 'MIN_RATING')]}
    ),
    (
        "Visiting Sibiu, Romania soon! Plan is to cover 8 spots by train. We'll lodge at Str Vasile Lucaciu 9, aiming not to exceed 24 kilometes Expect to spend around $83, and we're only considering places 3,9 stars.",
        {'entities': [(9, 23, 'LOCATION'), (47, 54, 'ATTRACTIONS_COUNT'), (58, 63, 'TRANSPORT'), (80, 100, 'ADDRESS'), (123, 135, 'MAX_DISTANCE'), (159, 162, 'MAX_PRICE'), (198, 207, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Galati, Romania—hoping to visit 10 monuments via bus. Our spot: Strada Mihai Eminescu 8. Distance? Around 30 km Expect to spend around 130 RON, and we're only considering places 4,7 stars.",
        {'entities': [(12, 27, 'LOCATION'), (44, 56, 'ATTRACTIONS_COUNT'), (61, 64, 'TRANSPORT'), (76, 99, 'ADDRESS'), (118, 123, 'MAX_DISTANCE'), (147, 154, 'MAX_PRICE'), (190, 199, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Iasi, Romania—hoping to visit 3 attractions via foot. Our spot: Bd Mamaia 15. Distance? Around 15 km Expect to spend around 182 RON, and we're only considering places 4,9 stars.",
        {'entities': [(12, 25, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (60, 64, 'TRANSPORT'), (76, 88, 'ADDRESS'), (107, 112, 'MAX_DISTANCE'), (136, 143, 'MAX_PRICE'), (179, 188, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Pitesti, Romania where we hope to check out 1 places. Mostly foot, staying at Calea Bucuresti 22, and keeping to 15 km Expect to spend around 64 USD, and we're only considering places 88 points.",
        {'entities': [(20, 36, 'LOCATION'), (64, 72, 'ATTRACTIONS_COUNT'), (81, 85, 'TRANSPORT'), (98, 116, 'ADDRESS'), (133, 138, 'MAX_DISTANCE'), (162, 168, 'MAX_PRICE'), (204, 213, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Bucharest, Romania. I’d like to visit 5 places, mainly by car, and stay at Strada Horea 7. I hope to keep it under 24 kilometes Expect to spend around 181 EUR, and we're only considering places 46/10 score.",
        {'entities': [(23, 41, 'LOCATION'), (61, 69, 'ATTRACTIONS_COUNT'), (81, 84, 'TRANSPORT'), (98, 112, 'ADDRESS'), (138, 150, 'MAX_DISTANCE'), (174, 181, 'MAX_PRICE'), (217, 228, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Bucharest, Romania. I’d like to visit 5 attractons, mainly by bicyle, and stay at Strada Libertatii 15. I hope to keep it under 30 km Expect to spend around 129 dollars, and we're only considering places at least 4,6★.",
        {'entities': [(23, 41, 'LOCATION'), (61, 73, 'ATTRACTIONS_COUNT'), (85, 91, 'TRANSPORT'), (105, 125, 'ADDRESS'), (151, 156, 'MAX_DISTANCE'), (180, 191, 'MAX_PRICE'), (227, 240, 'MIN_RATING')]}
    ),
    (
        "Heading to Targu Mures, Romania, planning for 3 atts, moving around by car, and staying at Calea Bucuresti 22. Targeting 35 km max Expect to spend around $260, and we're only considering places at least 4,3★.",
        {'entities': [(11, 31, 'LOCATION'), (46, 52, 'ATTRACTIONS_COUNT'), (71, 74, 'TRANSPORT'), (91, 109, 'ADDRESS'), (121, 126, 'MAX_DISTANCE'), (154, 158, 'MAX_PRICE'), (194, 207, 'MIN_RATING')]}
    ),
    (
        "Visiting Timisoara, Romania soon! Plan is to cover 2 monuments by train. We'll lodge at Str Vasile Lucaciu 9, aiming not to exceed 24 kilometes Expect to spend around 134 USD, and we're only considering places at least 4,7★.",
        {'entities': [(9, 27, 'LOCATION'), (51, 62, 'ATTRACTIONS_COUNT'), (66, 71, 'TRANSPORT'), (88, 108, 'ADDRESS'), (131, 143, 'MAX_DISTANCE'), (167, 174, 'MAX_PRICE'), (210, 223, 'MIN_RATING')]}
    ),
    (
        "Heading to Targu Mures, Romania, planning for 10 atr, moving around by foot, and staying at Bd Independentei 14. Targeting 16 kms max Expect to spend around 185 dollars, and we're only considering places 72 points.",
        {'entities': [(11, 31, 'LOCATION'), (46, 52, 'ATTRACTIONS_COUNT'), (71, 75, 'TRANSPORT'), (92, 111, 'ADDRESS'), (123, 129, 'MAX_DISTANCE'), (157, 168, 'MAX_PRICE'), (204, 213, 'MIN_RATING')]}
    ),
    (
        "Heading to Bucharest, Romania, planning for 8 monuments, moving around by car, and staying at Strada Memorandumului 5. Targeting 10 km max Expect to spend around 63 EUR, and we're only considering places 72 points.",
        {'entities': [(11, 29, 'LOCATION'), (44, 55, 'ATTRACTIONS_COUNT'), (74, 77, 'TRANSPORT'), (94, 117, 'ADDRESS'), (129, 134, 'MAX_DISTANCE'), (162, 168, 'MAX_PRICE'), (204, 213, 'MIN_RATING')]}
    ),
    (
        "We’re off to Pitesti, Romania, want to visit 6 places and will be using walk. Accommodation is Bd Mamaia 15. Distance cap: 10 km Expect to spend around 105 RON, and we're only considering places 76 points.",
        {'entities': [(13, 29, 'LOCATION'), (45, 53, 'ATTRACTIONS_COUNT'), (72, 76, 'TRANSPORT'), (95, 107, 'ADDRESS'), (123, 128, 'MAX_DISTANCE'), (152, 159, 'MAX_PRICE'), (195, 204, 'MIN_RATING')]}
    ),
    (
        "Visiting Bacau, Romania soon! Plan is to cover 3 attractions by car. We'll lodge at Calea Bucuresti 22, aiming not to exceed 35 km Expect to spend around 158 EUR, and we're only considering places 78 points.",
        {'entities': [(9, 23, 'LOCATION'), (47, 60, 'ATTRACTIONS_COUNT'), (64, 67, 'TRANSPORT'), (84, 102, 'ADDRESS'), (125, 130, 'MAX_DISTANCE'), (154, 161, 'MAX_PRICE'), (197, 206, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Iasi, Romania—hoping to visit 9 sights via bike. Our spot: Calea Bucuresti 22. Distance? Around 12 kilometres Expect to spend around 147 dollars, and we're only considering places 98 points.",
        {'entities': [(12, 25, 'LOCATION'), (42, 50, 'ATTRACTIONS_COUNT'), (55, 59, 'TRANSPORT'), (71, 89, 'ADDRESS'), (108, 121, 'MAX_DISTANCE'), (145, 156, 'MAX_PRICE'), (192, 201, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Pitesti, Romania, aiming for 2 attractions. We'll use bus most of the time and rest at Piata Avram Iancu 2. No more than 30 km Expect to spend around 185 dollars, and we're only considering places 4,0 stars.",
        {'entities': [(22, 38, 'LOCATION'), (51, 64, 'ATTRACTIONS_COUNT'), (76, 79, 'TRANSPORT'), (109, 128, 'ADDRESS'), (143, 148, 'MAX_DISTANCE'), (172, 183, 'MAX_PRICE'), (219, 228, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Constanta, Romania—hoping to visit 2 attractons via walk. Our spot: Calea Bucuresti 22. Distance? Around 22 kms Expect to spend around 298 dollars, and we're only considering places 49/10 score.",
        {'entities': [(12, 30, 'LOCATION'), (47, 59, 'ATTRACTIONS_COUNT'), (64, 68, 'TRANSPORT'), (80, 98, 'ADDRESS'), (117, 123, 'MAX_DISTANCE'), (147, 158, 'MAX_PRICE'), (194, 205, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Ploiesti, Romania where we hope to check out 1 attractons. Mostly bus, staying at Strada Mihai Eminescu 8, and keeping to 35 km Expect to spend around 233 RON, and we're only considering places 3,7 stars.",
        {'entities': [(20, 37, 'LOCATION'), (65, 77, 'ATTRACTIONS_COUNT'), (86, 89, 'TRANSPORT'), (102, 125, 'ADDRESS'), (142, 147, 'MAX_DISTANCE'), (171, 178, 'MAX_PRICE'), (214, 223, 'MIN_RATING')]}
    ),
    (
        "We’re off to Oradea, Romania, want to visit 10 atts and will be using train. Accommodation is Strada Libertatii 15. Distance cap: 10 km Expect to spend around $283, and we're only considering places rated 4,1/5.",
        {'entities': [(13, 28, 'LOCATION'), (44, 51, 'ATTRACTIONS_COUNT'), (70, 75, 'TRANSPORT'), (94, 114, 'ADDRESS'), (130, 135, 'MAX_DISTANCE'), (159, 163, 'MAX_PRICE'), (199, 210, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Brasov, Romania, aiming for 7 atr. We'll use foot most of the time and rest at Str Vasile Lucaciu 9. No more than 10 km Expect to spend around $191, and we're only considering places 86 points.",
        {'entities': [(22, 37, 'LOCATION'), (50, 55, 'ATTRACTIONS_COUNT'), (67, 71, 'TRANSPORT'), (101, 121, 'ADDRESS'), (136, 141, 'MAX_DISTANCE'), (165, 169, 'MAX_PRICE'), (205, 214, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Brasov, Romania, aiming for 4 landmarks. We'll use bus most of the time and rest at Strada Libertatii 15. No more than 28 km Expect to spend around 131 RON, and we're only considering places 4,7 stars.",
        {'entities': [(22, 37, 'LOCATION'), (50, 61, 'ATTRACTIONS_COUNT'), (73, 76, 'TRANSPORT'), (106, 126, 'ADDRESS'), (141, 146, 'MAX_DISTANCE'), (170, 177, 'MAX_PRICE'), (213, 222, 'MIN_RATING')]}
    ),
    (
        "Heading to Targu Mures, Romania, planning for 10 places, moving around by train, and staying at Calea Bucuresti 22. Targeting 12 kilometres max Expect to spend around 143 USD, and we're only considering places 4,2 stars.",
        {'entities': [(11, 31, 'LOCATION'), (46, 55, 'ATTRACTIONS_COUNT'), (74, 79, 'TRANSPORT'), (96, 114, 'ADDRESS'), (126, 139, 'MAX_DISTANCE'), (167, 174, 'MAX_PRICE'), (210, 219, 'MIN_RATING')]}
    ),
    (
        "Visiting Oradea, Romania soon! Plan is to cover 10 spots by bicyle. We'll lodge at Strada Horea 7, aiming not to exceed 20 km Expect to spend around $291, and we're only considering places at least 4,3★.",
        {'entities': [(9, 24, 'LOCATION'), (48, 56, 'ATTRACTIONS_COUNT'), (60, 66, 'TRANSPORT'), (83, 97, 'ADDRESS'), (120, 125, 'MAX_DISTANCE'), (149, 153, 'MAX_PRICE'), (189, 202, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Bacau, Romania—hoping to visit 9 things via bike. Our spot: Bd Mamaia 15. Distance? Around 25 km Expect to spend around 230 EUR, and we're only considering places 49/10 score.",
        {'entities': [(12, 26, 'LOCATION'), (43, 51, 'ATTRACTIONS_COUNT'), (56, 60, 'TRANSPORT'), (72, 84, 'ADDRESS'), (103, 108, 'MAX_DISTANCE'), (132, 139, 'MAX_PRICE'), (175, 186, 'MIN_RATING')]}
    ),
    (
        "We’re off to Oradea, Romania, want to visit 2 attr and will be using foot. Accommodation is Bd Independentei 14. Distance cap: 12 kilometres Expect to spend around $92, and we're only considering places 43/10 score.",
        {'entities': [(13, 28, 'LOCATION'), (44, 50, 'ATTRACTIONS_COUNT'), (69, 73, 'TRANSPORT'), (92, 111, 'ADDRESS'), (127, 140, 'MAX_DISTANCE'), (164, 167, 'MAX_PRICE'), (203, 214, 'MIN_RATING')]}
    ),
    (
        "We’re off to Galati, Romania, want to visit 3 monuments and will be using bicyle. Accommodation is Strada Libertatii 15. Distance cap: 30 km Expect to spend around $221, and we're only considering places at least 4,3★.",
        {'entities': [(13, 28, 'LOCATION'), (44, 55, 'ATTRACTIONS_COUNT'), (74, 80, 'TRANSPORT'), (99, 119, 'ADDRESS'), (135, 140, 'MAX_DISTANCE'), (164, 168, 'MAX_PRICE'), (204, 217, 'MIN_RATING')]}
    ),
    (
        "We’re off to Bucharest, Romania, want to visit 8 atts and will be using walk. Accommodation is Bd Mamaia 15. Distance cap: 22 kms Expect to spend around 105 USD, and we're only considering places 45/10 score.",
        {'entities': [(13, 31, 'LOCATION'), (47, 53, 'ATTRACTIONS_COUNT'), (72, 76, 'TRANSPORT'), (95, 107, 'ADDRESS'), (123, 129, 'MAX_DISTANCE'), (153, 160, 'MAX_PRICE'), (196, 207, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Bacau, Romania—hoping to visit 7 atr via foot. Our spot: Strada Mihai Eminescu 8. Distance? Around 12 kilometres Expect to spend around $71, and we're only considering places rated 3,8/5.",
        {'entities': [(12, 26, 'LOCATION'), (43, 48, 'ATTRACTIONS_COUNT'), (53, 57, 'TRANSPORT'), (69, 92, 'ADDRESS'), (111, 124, 'MAX_DISTANCE'), (148, 151, 'MAX_PRICE'), (187, 198, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Targu Mures, Romania—hoping to visit 10 sights via walk. Our spot: Bd Independentei 14. Distance? Around 20 km Expect to spend around 143 USD, and we're only considering places 47/10 score.",
        {'entities': [(12, 32, 'LOCATION'), (49, 58, 'ATTRACTIONS_COUNT'), (63, 67, 'TRANSPORT'), (79, 98, 'ADDRESS'), (117, 122, 'MAX_DISTANCE'), (146, 153, 'MAX_PRICE'), (189, 200, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Oradea, Romania. I’d like to visit 10 attractons, mainly by bike, and stay at Calea Bucuresti 22. I hope to keep it under 15 km Expect to spend around $197, and we're only considering places 86 points.",
        {'entities': [(23, 38, 'LOCATION'), (58, 71, 'ATTRACTIONS_COUNT'), (83, 87, 'TRANSPORT'), (101, 119, 'ADDRESS'), (145, 150, 'MAX_DISTANCE'), (174, 178, 'MAX_PRICE'), (214, 223, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Galati, Romania where we hope to check out 4 attr. Mostly bike, staying at Bd George Cosbuc 33, and keeping to 30 km Expect to spend around 152 RON, and we're only considering places 41/10 score.",
        {'entities': [(20, 35, 'LOCATION'), (63, 69, 'ATTRACTIONS_COUNT'), (78, 82, 'TRANSPORT'), (95, 114, 'ADDRESS'), (131, 136, 'MAX_DISTANCE'), (160, 167, 'MAX_PRICE'), (203, 214, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Baia Mare, Romania, aiming for 3 spots. We'll use car most of the time and rest at Bd George Cosbuc 33. No more than 30 km Expect to spend around 190 dollars, and we're only considering places rated 3,5/5.",
        {'entities': [(22, 40, 'LOCATION'), (53, 60, 'ATTRACTIONS_COUNT'), (72, 75, 'TRANSPORT'), (105, 124, 'ADDRESS'), (139, 144, 'MAX_DISTANCE'), (168, 179, 'MAX_PRICE'), (215, 226, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Targu Mures, Romania—hoping to visit 5 attractons via car. Our spot: Bd George Cosbuc 33. Distance? Around 18 kilometes Expect to spend around 152 dollars, and we're only considering places 86 points.",
        {'entities': [(12, 32, 'LOCATION'), (49, 61, 'ATTRACTIONS_COUNT'), (66, 69, 'TRANSPORT'), (81, 100, 'ADDRESS'), (119, 131, 'MAX_DISTANCE'), (155, 166, 'MAX_PRICE'), (202, 211, 'MIN_RATING')]}
    ),
    (
        "We’re off to Bucharest, Romania, want to visit 5 monuments and will be using car. Accommodation is Strada Mihai Eminescu 8. Distance cap: 35 km Expect to spend around 74 USD, and we're only considering places at least 4,4★.",
        {'entities': [(13, 31, 'LOCATION'), (47, 58, 'ATTRACTIONS_COUNT'), (77, 80, 'TRANSPORT'), (99, 122, 'ADDRESS'), (138, 143, 'MAX_DISTANCE'), (167, 173, 'MAX_PRICE'), (209, 222, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Sibiu, Romania. I’d like to visit 5 landmarks, mainly by bus, and stay at Str Vasile Lucaciu 9. I hope to keep it under 24 kilometes Expect to spend around 64 EUR, and we're only considering places 40/10 score.",
        {'entities': [(23, 37, 'LOCATION'), (57, 68, 'ATTRACTIONS_COUNT'), (80, 83, 'TRANSPORT'), (97, 117, 'ADDRESS'), (143, 155, 'MAX_DISTANCE'), (179, 185, 'MAX_PRICE'), (221, 232, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Baia Mare, Romania—hoping to visit 2 attr via train. Our spot: Bd Independentei 14. Distance? Around 25 km Expect to spend around 241 EUR, and we're only considering places 4,1 stars.",
        {'entities': [(12, 30, 'LOCATION'), (47, 53, 'ATTRACTIONS_COUNT'), (58, 63, 'TRANSPORT'), (75, 94, 'ADDRESS'), (113, 118, 'MAX_DISTANCE'), (142, 149, 'MAX_PRICE'), (185, 194, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Constanta, Romania, aiming for 7 attr. We'll use bicyle most of the time and rest at Strada Memorandumului 5. No more than 10 km Expect to spend around 158 RON, and we're only considering places at least 4,2★.",
        {'entities': [(22, 40, 'LOCATION'), (53, 59, 'ATTRACTIONS_COUNT'), (71, 77, 'TRANSPORT'), (107, 130, 'ADDRESS'), (145, 150, 'MAX_DISTANCE'), (174, 181, 'MAX_PRICE'), (217, 230, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Arad, Romania—hoping to visit 9 atts via car. Our spot: Strada Horea 7. Distance? Around 12 kilometres Expect to spend around 98 EUR, and we're only considering places 4,5 stars.",
        {'entities': [(12, 25, 'LOCATION'), (42, 48, 'ATTRACTIONS_COUNT'), (53, 56, 'TRANSPORT'), (68, 82, 'ADDRESS'), (101, 114, 'MAX_DISTANCE'), (138, 144, 'MAX_PRICE'), (180, 189, 'MIN_RATING')]}
    ),
    (
        "We’re off to Galati, Romania, want to visit 1 attr and will be using foot. Accommodation is Calea Bucuresti 22. Distance cap: 30 km Expect to spend around $176, and we're only considering places 74 points.",
        {'entities': [(13, 28, 'LOCATION'), (44, 50, 'ATTRACTIONS_COUNT'), (69, 73, 'TRANSPORT'), (92, 110, 'ADDRESS'), (126, 131, 'MAX_DISTANCE'), (155, 159, 'MAX_PRICE'), (195, 204, 'MIN_RATING')]}
    ),
    (
        "Heading to Constanta, Romania, planning for 9 spots, moving around by bike, and staying at Strada Memorandumului 5. Targeting 10 km max Expect to spend around 236 EUR, and we're only considering places rated 4,4/5.",
        {'entities': [(11, 29, 'LOCATION'), (44, 51, 'ATTRACTIONS_COUNT'), (70, 74, 'TRANSPORT'), (91, 114, 'ADDRESS'), (126, 131, 'MAX_DISTANCE'), (159, 166, 'MAX_PRICE'), (202, 213, 'MIN_RATING')]}
    ),
    (
        "Heading to Pitesti, Romania, planning for 4 places, moving around by bus, and staying at Bd Mamaia 15. Targeting 15 km max Expect to spend around 290 RON, and we're only considering places 88 points.",
        {'entities': [(11, 27, 'LOCATION'), (42, 50, 'ATTRACTIONS_COUNT'), (69, 72, 'TRANSPORT'), (89, 101, 'ADDRESS'), (113, 118, 'MAX_DISTANCE'), (146, 153, 'MAX_PRICE'), (189, 198, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Galati, Romania—hoping to visit 6 spots via bike. Our spot: Strada Horea 7. Distance? Around 20 km Expect to spend around $117, and we're only considering places at least 4,4★.",
        {'entities': [(12, 27, 'LOCATION'), (44, 51, 'ATTRACTIONS_COUNT'), (56, 60, 'TRANSPORT'), (72, 86, 'ADDRESS'), (105, 110, 'MAX_DISTANCE'), (134, 138, 'MAX_PRICE'), (174, 187, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Constanta, Romania—hoping to visit 1 spots via bus. Our spot: Strada Horea 7. Distance? Around 30 km Expect to spend around 89 USD, and we're only considering places 44/10 score.",
        {'entities': [(12, 30, 'LOCATION'), (47, 54, 'ATTRACTIONS_COUNT'), (59, 62, 'TRANSPORT'), (74, 88, 'ADDRESS'), (107, 112, 'MAX_DISTANCE'), (136, 142, 'MAX_PRICE'), (178, 189, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Cluj Napoca, Romania. I’d like to visit 4 spots, mainly by foot, and stay at Str Vasile Lucaciu 9. I hope to keep it under 30 km Expect to spend around 134 RON, and we're only considering places 4,1 stars.",
        {'entities': [(23, 43, 'LOCATION'), (63, 70, 'ATTRACTIONS_COUNT'), (82, 86, 'TRANSPORT'), (100, 120, 'ADDRESS'), (146, 151, 'MAX_DISTANCE'), (175, 182, 'MAX_PRICE'), (218, 227, 'MIN_RATING')]}
    ),
    (
        "Heading to Satu Mare, Romania, planning for 1 attr, moving around by bus, and staying at Strada Mihai Eminescu 8. Targeting 24 kilometes max Expect to spend around 230 dollars, and we're only considering places at least 3,6★.",
        {'entities': [(11, 29, 'LOCATION'), (44, 50, 'ATTRACTIONS_COUNT'), (69, 72, 'TRANSPORT'), (89, 112, 'ADDRESS'), (124, 136, 'MAX_DISTANCE'), (164, 175, 'MAX_PRICE'), (211, 224, 'MIN_RATING')]}
    ),
    (
        "Heading to Galati, Romania, planning for 2 attr, moving around by walk, and staying at Strada Horea 7. Targeting 28 km max Expect to spend around 94 USD, and we're only considering places 50/10 score.",
        {'entities': [(11, 26, 'LOCATION'), (41, 47, 'ATTRACTIONS_COUNT'), (66, 70, 'TRANSPORT'), (87, 101, 'ADDRESS'), (113, 118, 'MAX_DISTANCE'), (146, 152, 'MAX_PRICE'), (188, 199, 'MIN_RATING')]}
    ),
    (
        "We’re off to Ploiesti, Romania, want to visit 8 monuments and will be using train. Accommodation is Bd Independentei 14. Distance cap: 28 km Expect to spend around 101 dollars, and we're only considering places 40/10 score.",
        {'entities': [(13, 30, 'LOCATION'), (46, 57, 'ATTRACTIONS_COUNT'), (76, 81, 'TRANSPORT'), (100, 119, 'ADDRESS'), (135, 140, 'MAX_DISTANCE'), (164, 175, 'MAX_PRICE'), (211, 222, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Sibiu, Romania where we hope to check out 2 spots. Mostly bike, staying at Strada Horea 7, and keeping to 18 kilometes Expect to spend around 261 EUR, and we're only considering places rated 3,7/5.",
        {'entities': [(20, 34, 'LOCATION'), (62, 69, 'ATTRACTIONS_COUNT'), (78, 82, 'TRANSPORT'), (95, 109, 'ADDRESS'), (126, 138, 'MAX_DISTANCE'), (162, 169, 'MAX_PRICE'), (205, 216, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Targu Mures, Romania where we hope to check out 10 attractions. Mostly foot, staying at Bd George Cosbuc 33, and keeping to 35 km Expect to spend around $205, and we're only considering places 39/10 score.",
        {'entities': [(20, 40, 'LOCATION'), (68, 82, 'ATTRACTIONS_COUNT'), (91, 95, 'TRANSPORT'), (108, 127, 'ADDRESS'), (144, 149, 'MAX_DISTANCE'), (173, 177, 'MAX_PRICE'), (213, 224, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Oradea, Romania where we hope to check out 5 places. Mostly train, staying at Calea Bucuresti 22, and keeping to 24 kilometes Expect to spend around 251 dollars, and we're only considering places 36/10 score.",
        {'entities': [(20, 35, 'LOCATION'), (63, 71, 'ATTRACTIONS_COUNT'), (80, 85, 'TRANSPORT'), (98, 116, 'ADDRESS'), (133, 145, 'MAX_DISTANCE'), (169, 180, 'MAX_PRICE'), (216, 227, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Baia Mare, Romania, aiming for 6 landmarks. We'll use train most of the time and rest at Strada Mihai Eminescu 8. No more than 30 km Expect to spend around 78 dollars, and we're only considering places 38/10 score.",
        {'entities': [(22, 40, 'LOCATION'), (53, 64, 'ATTRACTIONS_COUNT'), (76, 81, 'TRANSPORT'), (111, 134, 'ADDRESS'), (149, 154, 'MAX_DISTANCE'), (178, 188, 'MAX_PRICE'), (224, 235, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Iasi, Romania. I’d like to visit 2 atr, mainly by foot, and stay at Bd George Cosbuc 33. I hope to keep it under 20 km Expect to spend around 251 RON, and we're only considering places 48/10 score.",
        {'entities': [(23, 36, 'LOCATION'), (56, 61, 'ATTRACTIONS_COUNT'), (73, 77, 'TRANSPORT'), (91, 110, 'ADDRESS'), (136, 141, 'MAX_DISTANCE'), (165, 172, 'MAX_PRICE'), (208, 219, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Bucharest, Romania. I’d like to visit 5 attractions, mainly by train, and stay at Strada Horea 7. I hope to keep it under 12 kilometres Expect to spend around $73, and we're only considering places 4,8 stars.",
        {'entities': [(23, 41, 'LOCATION'), (61, 74, 'ATTRACTIONS_COUNT'), (86, 91, 'TRANSPORT'), (105, 119, 'ADDRESS'), (145, 158, 'MAX_DISTANCE'), (182, 185, 'MAX_PRICE'), (221, 230, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Oradea, Romania—hoping to visit 6 atr via train. Our spot: Bd Mamaia 15. Distance? Around 28 km Expect to spend around 180 dollars, and we're only considering places 42/10 score.",
        {'entities': [(12, 27, 'LOCATION'), (44, 49, 'ATTRACTIONS_COUNT'), (54, 59, 'TRANSPORT'), (71, 83, 'ADDRESS'), (102, 107, 'MAX_DISTANCE'), (131, 142, 'MAX_PRICE'), (178, 189, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bucharest, Romania where we hope to check out 1 atts. Mostly foot, staying at Piata Avram Iancu 2, and keeping to 30 km Expect to spend around 75 dollars, and we're only considering places at least 4,8★.",
        {'entities': [(20, 38, 'LOCATION'), (66, 72, 'ATTRACTIONS_COUNT'), (81, 85, 'TRANSPORT'), (98, 117, 'ADDRESS'), (134, 139, 'MAX_DISTANCE'), (163, 173, 'MAX_PRICE'), (209, 222, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Galati, Romania, aiming for 5 landmarks. We'll use walk most of the time and rest at Strada Horea 7. No more than 15 km Expect to spend around 264 RON, and we're only considering places 43/10 score.",
        {'entities': [(22, 37, 'LOCATION'), (50, 61, 'ATTRACTIONS_COUNT'), (73, 77, 'TRANSPORT'), (107, 121, 'ADDRESS'), (136, 141, 'MAX_DISTANCE'), (165, 172, 'MAX_PRICE'), (208, 219, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Satu Mare, Romania—hoping to visit 7 atts via bicyle. Our spot: Piata Avram Iancu 2. Distance? Around 20 km Expect to spend around 242 RON, and we're only considering places 84 points.",
        {'entities': [(12, 30, 'LOCATION'), (47, 53, 'ATTRACTIONS_COUNT'), (58, 64, 'TRANSPORT'), (76, 95, 'ADDRESS'), (114, 119, 'MAX_DISTANCE'), (143, 150, 'MAX_PRICE'), (186, 195, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Cluj Napoca, Romania. I’d like to visit 1 places, mainly by walk, and stay at Strada Horea 7. I hope to keep it under 16 kms Expect to spend around 202 EUR, and we're only considering places at least 3,9★.",
        {'entities': [(23, 43, 'LOCATION'), (63, 71, 'ATTRACTIONS_COUNT'), (83, 87, 'TRANSPORT'), (101, 115, 'ADDRESS'), (141, 147, 'MAX_DISTANCE'), (171, 178, 'MAX_PRICE'), (214, 227, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Galati, Romania—hoping to visit 7 attr via bike. Our spot: Bd Independentei 14. Distance? Around 22 kms Expect to spend around 91 EUR, and we're only considering places 4,6 stars.",
        {'entities': [(12, 27, 'LOCATION'), (44, 50, 'ATTRACTIONS_COUNT'), (55, 59, 'TRANSPORT'), (71, 90, 'ADDRESS'), (109, 115, 'MAX_DISTANCE'), (139, 145, 'MAX_PRICE'), (181, 190, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Cluj Napoca, Romania—hoping to visit 9 attractions via bus. Our spot: Piata Avram Iancu 2. Distance? Around 22 kms Expect to spend around 107 RON, and we're only considering places rated 4,4/5.",
        {'entities': [(12, 32, 'LOCATION'), (49, 62, 'ATTRACTIONS_COUNT'), (67, 70, 'TRANSPORT'), (82, 101, 'ADDRESS'), (120, 126, 'MAX_DISTANCE'), (150, 157, 'MAX_PRICE'), (193, 204, 'MIN_RATING')]}
    ),
    (
        "We’re off to Galati, Romania, want to visit 9 attractons and will be using bus. Accommodation is Piata Avram Iancu 2. Distance cap: 25 km Expect to spend around 271 USD, and we're only considering places 43/10 score.",
        {'entities': [(13, 28, 'LOCATION'), (44, 56, 'ATTRACTIONS_COUNT'), (75, 78, 'TRANSPORT'), (97, 116, 'ADDRESS'), (132, 137, 'MAX_DISTANCE'), (161, 168, 'MAX_PRICE'), (204, 215, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Cluj Napoca, Romania—hoping to visit 2 monuments via train. Our spot: Strada Mihai Eminescu 8. Distance? Around 12 kilometres Expect to spend around 264 USD, and we're only considering places at least 4,9★.",
        {'entities': [(12, 32, 'LOCATION'), (49, 60, 'ATTRACTIONS_COUNT'), (65, 70, 'TRANSPORT'), (82, 105, 'ADDRESS'), (124, 137, 'MAX_DISTANCE'), (161, 168, 'MAX_PRICE'), (204, 217, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Iasi, Romania. I’d like to visit 10 landmarks, mainly by train, and stay at Bd George Cosbuc 33. I hope to keep it under 20 km Expect to spend around 182 dollars, and we're only considering places 39/10 score.",
        {'entities': [(23, 36, 'LOCATION'), (56, 68, 'ATTRACTIONS_COUNT'), (80, 85, 'TRANSPORT'), (99, 118, 'ADDRESS'), (144, 149, 'MAX_DISTANCE'), (173, 184, 'MAX_PRICE'), (220, 231, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Brasov, Romania where we hope to check out 9 sights. Mostly car, staying at Calea Bucuresti 22, and keeping to 28 km Expect to spend around 272 EUR, and we're only considering places at least 4,4★.",
        {'entities': [(20, 35, 'LOCATION'), (63, 71, 'ATTRACTIONS_COUNT'), (80, 83, 'TRANSPORT'), (96, 114, 'ADDRESS'), (131, 136, 'MAX_DISTANCE'), (160, 167, 'MAX_PRICE'), (203, 216, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Oradea, Romania where we hope to check out 3 things. Mostly walk, staying at Strada Libertatii 15, and keeping to 18 kilometes Expect to spend around 207 RON, and we're only considering places 86 points.",
        {'entities': [(20, 35, 'LOCATION'), (63, 71, 'ATTRACTIONS_COUNT'), (80, 84, 'TRANSPORT'), (97, 117, 'ADDRESS'), (134, 146, 'MAX_DISTANCE'), (170, 177, 'MAX_PRICE'), (213, 222, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Baia Mare, Romania—hoping to visit 3 landmarks via bicyle. Our spot: Bd George Cosbuc 33. Distance? Around 35 km Expect to spend around 188 USD, and we're only considering places 76 points.",
        {'entities': [(12, 30, 'LOCATION'), (47, 58, 'ATTRACTIONS_COUNT'), (63, 69, 'TRANSPORT'), (81, 100, 'ADDRESS'), (119, 124, 'MAX_DISTANCE'), (148, 155, 'MAX_PRICE'), (191, 200, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Satu Mare, Romania—hoping to visit 10 atts via bus. Our spot: Strada Mihai Eminescu 8. Distance? Around 10 km Expect to spend around 191 RON, and we're only considering places rated 3,6/5.",
        {'entities': [(12, 30, 'LOCATION'), (47, 54, 'ATTRACTIONS_COUNT'), (59, 62, 'TRANSPORT'), (74, 97, 'ADDRESS'), (116, 121, 'MAX_DISTANCE'), (145, 152, 'MAX_PRICE'), (188, 199, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Sibiu, Romania where we hope to check out 4 places. Mostly car, staying at Strada Memorandumului 5, and keeping to 30 km Expect to spend around 290 USD, and we're only considering places 4,6 stars.",
        {'entities': [(20, 34, 'LOCATION'), (62, 70, 'ATTRACTIONS_COUNT'), (79, 82, 'TRANSPORT'), (95, 118, 'ADDRESS'), (135, 140, 'MAX_DISTANCE'), (164, 171, 'MAX_PRICE'), (207, 216, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Constanta, Romania where we hope to check out 1 attractions. Mostly walk, staying at Bd Independentei 14, and keeping to 25 km Expect to spend around 64 RON, and we're only considering places 4,6 stars.",
        {'entities': [(20, 38, 'LOCATION'), (66, 79, 'ATTRACTIONS_COUNT'), (88, 92, 'TRANSPORT'), (105, 124, 'ADDRESS'), (141, 146, 'MAX_DISTANCE'), (170, 176, 'MAX_PRICE'), (212, 221, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Iasi, Romania—hoping to visit 6 spots via train. Our spot: Piata Avram Iancu 2. Distance? Around 20 km Expect to spend around 226 EUR, and we're only considering places 74 points.",
        {'entities': [(12, 25, 'LOCATION'), (42, 49, 'ATTRACTIONS_COUNT'), (54, 59, 'TRANSPORT'), (71, 90, 'ADDRESS'), (109, 114, 'MAX_DISTANCE'), (138, 145, 'MAX_PRICE'), (181, 190, 'MIN_RATING')]}
    ),
    (
        "Visiting Constanta, Romania soon! Plan is to cover 3 atr by train. We'll lodge at Calea Bucuresti 22, aiming not to exceed 12 kilometres Expect to spend around 192 dollars, and we're only considering places 4,1 stars.",
        {'entities': [(9, 27, 'LOCATION'), (51, 56, 'ATTRACTIONS_COUNT'), (60, 65, 'TRANSPORT'), (82, 100, 'ADDRESS'), (123, 136, 'MAX_DISTANCE'), (160, 171, 'MAX_PRICE'), (207, 216, 'MIN_RATING')]}
    ),
    (
        "Visiting Satu Mare, Romania soon! Plan is to cover 8 landmarks by bus. We'll lodge at Strada Horea 7, aiming not to exceed 12 kilometres Expect to spend around 189 USD, and we're only considering places 48/10 score.",
        {'entities': [(9, 27, 'LOCATION'), (51, 62, 'ATTRACTIONS_COUNT'), (66, 69, 'TRANSPORT'), (86, 100, 'ADDRESS'), (123, 136, 'MAX_DISTANCE'), (160, 167, 'MAX_PRICE'), (203, 214, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Cluj Napoca, Romania where we hope to check out 2 places. Mostly bicyle, staying at Strada Libertatii 15, and keeping to 10 km Expect to spend around 158 EUR, and we're only considering places at least 4,0★.",
        {'entities': [(20, 40, 'LOCATION'), (68, 76, 'ATTRACTIONS_COUNT'), (85, 91, 'TRANSPORT'), (104, 124, 'ADDRESS'), (141, 146, 'MAX_DISTANCE'), (170, 177, 'MAX_PRICE'), (213, 226, 'MIN_RATING')]}
    ),
    (
        "We’re off to Cluj Napoca, Romania, want to visit 9 attr and will be using walk. Accommodation is Strada Memorandumului 5. Distance cap: 30 km Expect to spend around 108 dollars, and we're only considering places 4,3 stars.",
        {'entities': [(13, 33, 'LOCATION'), (49, 55, 'ATTRACTIONS_COUNT'), (74, 78, 'TRANSPORT'), (97, 120, 'ADDRESS'), (136, 141, 'MAX_DISTANCE'), (165, 176, 'MAX_PRICE'), (212, 221, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Sibiu, Romania. I’d like to visit 6 atr, mainly by walk, and stay at Bd Independentei 14. I hope to keep it under 15 km Expect to spend around 180 USD, and we're only considering places 78 points.",
        {'entities': [(23, 37, 'LOCATION'), (57, 62, 'ATTRACTIONS_COUNT'), (74, 78, 'TRANSPORT'), (92, 111, 'ADDRESS'), (137, 142, 'MAX_DISTANCE'), (166, 173, 'MAX_PRICE'), (209, 218, 'MIN_RATING')]}
    ),
    (
        "We’re off to Oradea, Romania, want to visit 7 attr and will be using train. Accommodation is Strada Memorandumului 5. Distance cap: 15 km Expect to spend around $204, and we're only considering places rated 3,8/5.",
        {'entities': [(13, 28, 'LOCATION'), (44, 50, 'ATTRACTIONS_COUNT'), (69, 74, 'TRANSPORT'), (93, 116, 'ADDRESS'), (132, 137, 'MAX_DISTANCE'), (161, 165, 'MAX_PRICE'), (201, 212, 'MIN_RATING')]}
    ),
    (
        "We’re off to Arad, Romania, want to visit 4 atr and will be using bus. Accommodation is Strada Memorandumului 5. Distance cap: 28 km Expect to spend around 168 USD, and we're only considering places rated 4,7/5.",
        {'entities': [(13, 26, 'LOCATION'), (42, 47, 'ATTRACTIONS_COUNT'), (66, 69, 'TRANSPORT'), (88, 111, 'ADDRESS'), (127, 132, 'MAX_DISTANCE'), (156, 163, 'MAX_PRICE'), (199, 210, 'MIN_RATING')]}
    ),
    (
        "Heading to Timisoara, Romania, planning for 7 sights, moving around by walk, and staying at Piata Avram Iancu 2. Targeting 12 kilometres max Expect to spend around 95 EUR, and we're only considering places 47/10 score.",
        {'entities': [(11, 29, 'LOCATION'), (44, 52, 'ATTRACTIONS_COUNT'), (71, 75, 'TRANSPORT'), (92, 111, 'ADDRESS'), (123, 136, 'MAX_DISTANCE'), (164, 170, 'MAX_PRICE'), (206, 217, 'MIN_RATING')]}
    ),
    (
        "We’re off to Targu Mures, Romania, want to visit 5 sights and will be using bus. Accommodation is Calea Bucuresti 22. Distance cap: 25 km Expect to spend around 117 dollars, and we're only considering places at least 3,8★.",
        {'entities': [(13, 33, 'LOCATION'), (49, 57, 'ATTRACTIONS_COUNT'), (76, 79, 'TRANSPORT'), (98, 116, 'ADDRESS'), (132, 137, 'MAX_DISTANCE'), (161, 172, 'MAX_PRICE'), (208, 221, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Timisoara, Romania, aiming for 9 landmarks. We'll use bicyle most of the time and rest at Strada Libertatii 15. No more than 10 km Expect to spend around 288 EUR, and we're only considering places at least 4,8★.",
        {'entities': [(22, 40, 'LOCATION'), (53, 64, 'ATTRACTIONS_COUNT'), (76, 82, 'TRANSPORT'), (112, 132, 'ADDRESS'), (147, 152, 'MAX_DISTANCE'), (176, 183, 'MAX_PRICE'), (219, 232, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Oradea, Romania where we hope to check out 8 monuments. Mostly walk, staying at Bd Independentei 14, and keeping to 15 km Expect to spend around 62 EUR, and we're only considering places 50/10 score.",
        {'entities': [(20, 35, 'LOCATION'), (63, 74, 'ATTRACTIONS_COUNT'), (83, 87, 'TRANSPORT'), (100, 119, 'ADDRESS'), (136, 141, 'MAX_DISTANCE'), (165, 171, 'MAX_PRICE'), (207, 218, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Constanta, Romania, aiming for 4 spots. We'll use bike most of the time and rest at Bd George Cosbuc 33. No more than 35 km Expect to spend around 177 dollars, and we're only considering places at least 4,9★.",
        {'entities': [(22, 40, 'LOCATION'), (53, 60, 'ATTRACTIONS_COUNT'), (72, 76, 'TRANSPORT'), (106, 125, 'ADDRESS'), (140, 145, 'MAX_DISTANCE'), (169, 180, 'MAX_PRICE'), (216, 229, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Targu Mures, Romania where we hope to check out 10 atts. Mostly bus, staying at Calea Bucuresti 22, and keeping to 28 km Expect to spend around 218 dollars, and we're only considering places 4,3 stars.",
        {'entities': [(20, 40, 'LOCATION'), (68, 75, 'ATTRACTIONS_COUNT'), (84, 87, 'TRANSPORT'), (100, 118, 'ADDRESS'), (135, 140, 'MAX_DISTANCE'), (164, 175, 'MAX_PRICE'), (211, 220, 'MIN_RATING')]}
    ),
    (
        "We’re off to Targu Mures, Romania, want to visit 7 landmarks and will be using car. Accommodation is Strada Memorandumului 5. Distance cap: 15 km Expect to spend around 117 EUR, and we're only considering places 4,2 stars.",
        {'entities': [(13, 33, 'LOCATION'), (49, 60, 'ATTRACTIONS_COUNT'), (79, 82, 'TRANSPORT'), (101, 124, 'ADDRESS'), (140, 145, 'MAX_DISTANCE'), (169, 176, 'MAX_PRICE'), (212, 221, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bucharest, Romania where we hope to check out 4 spots. Mostly train, staying at Bd Independentei 14, and keeping to 24 kilometes Expect to spend around 207 EUR, and we're only considering places rated 3,8/5.",
        {'entities': [(20, 38, 'LOCATION'), (66, 73, 'ATTRACTIONS_COUNT'), (82, 87, 'TRANSPORT'), (100, 119, 'ADDRESS'), (136, 148, 'MAX_DISTANCE'), (172, 179, 'MAX_PRICE'), (215, 226, 'MIN_RATING')]}
    ),
    (
        "We’re off to Bacau, Romania, want to visit 9 places and will be using foot. Accommodation is Strada Libertatii 15. Distance cap: 12 kilometres Expect to spend around 225 dollars, and we're only considering places 74 points.",
        {'entities': [(13, 27, 'LOCATION'), (43, 51, 'ATTRACTIONS_COUNT'), (70, 74, 'TRANSPORT'), (93, 113, 'ADDRESS'), (129, 142, 'MAX_DISTANCE'), (166, 177, 'MAX_PRICE'), (213, 222, 'MIN_RATING')]}
    ),
    (
        "I’m planning a trip to Targu Mures, Romania. I’d like to visit 2 attractions, mainly by foot, and stay at Calea Bucuresti 22. I hope to keep it under 12 kilometres Expect to spend around 121 USD, and we're only considering places at least 4,8★.",
        {'entities': [(23, 43, 'LOCATION'), (63, 76, 'ATTRACTIONS_COUNT'), (88, 92, 'TRANSPORT'), (106, 124, 'ADDRESS'), (150, 163, 'MAX_DISTANCE'), (187, 194, 'MAX_PRICE'), (230, 243, 'MIN_RATING')]}
    ),
]