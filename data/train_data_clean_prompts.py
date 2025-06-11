TRAIN_DATA = [
    (
        "Thinking of exploring Bacau, Romania, aiming for 10 attractions. We'll use bus most of the time and rest at Strada Tudor Vladimirescu 22. No more than 14 kilometers Expect to spend around 246 RON, and we're only considering places 98 points.",
        {'entities': [(22, 36, 'LOCATION'), (49, 63, 'ATTRACTIONS_COUNT'), (75, 78, 'TRANSPORT'), (151, 164, 'MAX_DISTANCE'), (108, 136, 'ADDRESS'), (188, 195, 'MAX_PRICE'), (231, 240, 'MIN_RATING')]}
    ),
    (
        "We're booking Craiova, Romania, targeting 4 attractions by walking. Lodging at Strada Mihai Eminescu 8 and trying not to exceed 25 kilometers Expect to spend around 206 USD, and we're only considering places 4,4 stars.",
        {'entities': [(14, 30, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (59, 66, 'TRANSPORT'), (128, 141, 'MAX_DISTANCE'), (79, 102, 'ADDRESS'), (165, 172, 'MAX_PRICE'), (208, 217, 'MIN_RATING')]}
    ),
    (
        "We’re off to Sibiu, Romania, want to visit 10 attractions and will be using bicycle. Accommodation is Str. Vasile Lucaciu 9. Distance cap: 24 kilometers Expect to spend around 272 EUR, and we're only considering places rated 4,6/5.",
        {'entities': [(13, 27, 'LOCATION'), (43, 57, 'ATTRACTIONS_COUNT'), (76, 83, 'TRANSPORT'), (139, 152, 'MAX_DISTANCE'), (102, 123, 'ADDRESS'), (176, 183, 'MAX_PRICE'), (219, 230, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Galati, Romania, aiming for 7 attractions. We'll use bicycle most of the time and rest at Strada Universitatii 5. No more than 17 kilometers Expect to spend around 246 USD, and we're only considering places 38/10 score.",
        {'entities': [(22, 37, 'LOCATION'), (50, 63, 'ATTRACTIONS_COUNT'), (75, 82, 'TRANSPORT'), (149, 162, 'MAX_DISTANCE'), (112, 134, 'ADDRESS'), (186, 193, 'MAX_PRICE'), (229, 240, 'MIN_RATING')]}
    ),
    (
        "I'm planning a trip to Iasi, Romania. I'd like to visit 10 attractions, mainly by bike, and stay at Strada Mihai Eminescu 8. I hope to keep it under 25 kilometers Expect to spend around 91 RON, and we're only considering places 39/10 score.",
        {'entities': [(23, 36, 'LOCATION'), (56, 70, 'ATTRACTIONS_COUNT'), (82, 86, 'TRANSPORT'), (149, 162, 'MAX_DISTANCE'), (100, 123, 'ADDRESS'), (186, 192, 'MAX_PRICE'), (228, 239, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Pitesti, Romania—hoping to visit 3 attractions via bicycle. Our spot: Str. Vasile Lucaciu 9. Distance? Around 17 kilometers Expect to spend around 78 RON, and we're only considering places at least 3,9★.",
        {'entities': [(12, 28, 'LOCATION'), (45, 58, 'ATTRACTIONS_COUNT'), (63, 70, 'TRANSPORT'), (122, 135, 'MAX_DISTANCE'), (82, 103, 'ADDRESS'), (159, 165, 'MAX_PRICE'), (201, 214, 'MIN_RATING')]}
    ),
    (
        "Bacau, Romania is on my radar! Planning 8 attractions and bike most of the way. Staying at Strada Universitatii 5 and want to stay under 22 kilometers Expect to spend around 139 EUR, and we're only considering places 96 points.",
        {'entities': [(0, 14, 'LOCATION'), (40, 53, 'ATTRACTIONS_COUNT'), (58, 62, 'TRANSPORT'), (137, 150, 'MAX_DISTANCE'), (91, 113, 'ADDRESS'), (174, 181, 'MAX_PRICE'), (217, 226, 'MIN_RATING')]}
    ),
    (
        "Heading to Craiova, Romania, planning for 9 attractions, moving around by bicycle, and staying at Strada Memorandumului 5. Targeting 18 kilometers max Expect to spend around 246 USD, and we're only considering places at least 3,9★.",
        {'entities': [(11, 27, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (74, 81, 'TRANSPORT'), (133, 146, 'MAX_DISTANCE'), (98, 121, 'ADDRESS'), (174, 181, 'MAX_PRICE'), (217, 230, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Pitesti, Romania where we hope to check out 3 attractions. Mostly bike, staying at Sos. Nicolina 50, and keeping to 10 kilometers Expect to spend around $247, and we're only considering places rated 3,9/5.",
        {'entities': [(20, 36, 'LOCATION'), (64, 77, 'ATTRACTIONS_COUNT'), (86, 90, 'TRANSPORT'), (136, 149, 'MAX_DISTANCE'), (103, 119, 'ADDRESS'), (173, 177, 'MAX_PRICE'), (213, 224, 'MIN_RATING')]}
    ),
    (
        "We’re off to Galati, Romania, want to visit 5 attractions and will be using bicycle. Accommodation is Strada Mihai Eminescu 8. Distance cap: 13 kilometers Expect to spend around 178 USD, and we're only considering places 3,6 stars.",
        {'entities': [(13, 28, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (76, 83, 'TRANSPORT'), (141, 154, 'MAX_DISTANCE'), (102, 125, 'ADDRESS'), (178, 185, 'MAX_PRICE'), (221, 230, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Oradea, Romania, aiming for 4 attractions. We'll use train most of the time and rest at Strada Libertatii 15. No more than 15 kilometers Expect to spend around 95 dollars, and we're only considering places 84 points.",
        {'entities': [(22, 37, 'LOCATION'), (50, 63, 'ATTRACTIONS_COUNT'), (75, 80, 'TRANSPORT'), (145, 158, 'MAX_DISTANCE'), (110, 130, 'ADDRESS'), (182, 192, 'MAX_PRICE'), (228, 237, 'MIN_RATING')]}
    ),
    (
        "I'm planning a trip to Satu Mare, Romania. I'd like to visit 3 attractions, mainly by car, and stay at Calea Victoriei 12. I hope to keep it under 18 kilometers Expect to spend around $62, and we're only considering places 96 points.",
        {'entities': [(23, 41, 'LOCATION'), (61, 74, 'ATTRACTIONS_COUNT'), (86, 89, 'TRANSPORT'), (147, 160, 'MAX_DISTANCE'), (103, 121, 'ADDRESS'), (184, 187, 'MAX_PRICE'), (223, 232, 'MIN_RATING')]}
    ),
    (
        "Visiting Bacau, Romania soon! Plan is to cover 2 attractions by walking. We'll lodge at Strada Libertatii 15, aiming not to exceed 25 kilometers Expect to spend around 222 dollars, and we're only considering places 82 points.",
        {'entities': [(9, 23, 'LOCATION'), (47, 60, 'ATTRACTIONS_COUNT'), (64, 71, 'TRANSPORT'), (131, 144, 'MAX_DISTANCE'), (88, 108, 'ADDRESS'), (168, 179, 'MAX_PRICE'), (215, 224, 'MIN_RATING')]}
    ),
    (
        "We’re off to Arad, Romania, want to visit 7 attractions and will be using walking. Accommodation is Bd. George Cosbuc 33. Distance cap: 19 kilometers Expect to spend around 265 RON, and we're only considering places at least 4,0★.",
        {'entities': [(13, 26, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (74, 81, 'TRANSPORT'), (136, 149, 'MAX_DISTANCE'), (100, 120, 'ADDRESS'), (173, 180, 'MAX_PRICE'), (216, 229, 'MIN_RATING')]}
    ),
    (
        "We’re off to Ploiesti, Romania, want to visit 6 attractions and will be using bike. Accommodation is Str. Vasile Lucaciu 9. Distance cap: 29 kilometers Expect to spend around 192 USD, and we're only considering places rated 3,7/5.",
        {'entities': [(13, 30, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (78, 82, 'TRANSPORT'), (138, 151, 'MAX_DISTANCE'), (101, 122, 'ADDRESS'), (175, 182, 'MAX_PRICE'), (218, 229, 'MIN_RATING')]}
    ),
    (
        "Next on the list: Galati, Romania. About 3 attractions, traveling by walking, with a base at Strada Memorandumului 5. Hoping to stay within 29 kilometers Expect to spend around 276 RON, and we're only considering places at least 5,0★.",
        {'entities': [(18, 33, 'LOCATION'), (41, 54, 'ATTRACTIONS_COUNT'), (69, 76, 'TRANSPORT'), (140, 153, 'MAX_DISTANCE'), (93, 116, 'ADDRESS'), (177, 184, 'MAX_PRICE'), (220, 233, 'MIN_RATING')]}
    ),
    (
        "Heading to Sibiu, Romania, planning for 8 attractions, moving around by walking, and staying at Strada Tudor Vladimirescu 22. Targeting 20 kilometers max Expect to spend around 188 EUR, and we're only considering places rated 4,9/5.",
        {'entities': [(11, 25, 'LOCATION'), (40, 53, 'ATTRACTIONS_COUNT'), (72, 79, 'TRANSPORT'), (136, 149, 'MAX_DISTANCE'), (96, 124, 'ADDRESS'), (177, 184, 'MAX_PRICE'), (220, 231, 'MIN_RATING')]}
    ),
    (
        "Heading to Timisoara, Romania, planning for 10 attractions, moving around by walking, and staying at Bd. Independentei 14. Targeting 23 kilometers max Expect to spend around 242 dollars, and we're only considering places rated 4,9/5.",
        {'entities': [(11, 29, 'LOCATION'), (44, 58, 'ATTRACTIONS_COUNT'), (77, 84, 'TRANSPORT'), (133, 146, 'MAX_DISTANCE'), (101, 121, 'ADDRESS'), (174, 185, 'MAX_PRICE'), (221, 232, 'MIN_RATING')]}
    ),
    (
        "Visiting Galati, Romania soon! Plan is to cover 7 attractions by bus. We'll lodge at Strada Republicii 20, aiming not to exceed 14 kilometers Expect to spend around 132 EUR, and we're only considering places 82 points.",
        {'entities': [(9, 24, 'LOCATION'), (48, 61, 'ATTRACTIONS_COUNT'), (65, 68, 'TRANSPORT'), (128, 141, 'MAX_DISTANCE'), (85, 105, 'ADDRESS'), (165, 172, 'MAX_PRICE'), (208, 217, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Satu Mare, Romania, aiming for 9 attractions. We'll use bicycle most of the time and rest at Strada Tudor Vladimirescu 22. No more than 19 kilometers Expect to spend around 287 dollars, and we're only considering places 74 points.",
        {'entities': [(22, 40, 'LOCATION'), (53, 66, 'ATTRACTIONS_COUNT'), (78, 85, 'TRANSPORT'), (158, 171, 'MAX_DISTANCE'), (115, 143, 'ADDRESS'), (195, 206, 'MAX_PRICE'), (242, 251, 'MIN_RATING')]}
    ),
    (
        "We're booking Arad, Romania, targeting 2 attractions by bus. Lodging at Strada Mihai Eminescu 8 and trying not to exceed 23 kilometers Expect to spend around 224 EUR, and we're only considering places 3,9 stars.",
        {'entities': [(14, 27, 'LOCATION'), (39, 52, 'ATTRACTIONS_COUNT'), (56, 59, 'TRANSPORT'), (121, 134, 'MAX_DISTANCE'), (72, 95, 'ADDRESS'), (158, 165, 'MAX_PRICE'), (201, 210, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Iasi, Romania, aiming for 10 attractions. We'll use train most of the time and rest at Sos. Nicolina 50. No more than 20 kilometers Expect to spend around 281 EUR, and we're only considering places 82 points.",
        {'entities': [(22, 35, 'LOCATION'), (48, 62, 'ATTRACTIONS_COUNT'), (74, 79, 'TRANSPORT'), (140, 153, 'MAX_DISTANCE'), (109, 125, 'ADDRESS'), (177, 184, 'MAX_PRICE'), (220, 229, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Galati, Romania where we hope to check out 2 attractions. Mostly bus, staying at Piata Avram Iancu 2, and keeping to 23 kilometers Expect to spend around 225 USD, and we're only considering places at least 4,3★.",
        {'entities': [(20, 35, 'LOCATION'), (63, 76, 'ATTRACTIONS_COUNT'), (85, 88, 'TRANSPORT'), (137, 150, 'MAX_DISTANCE'), (101, 120, 'ADDRESS'), (174, 181, 'MAX_PRICE'), (217, 230, 'MIN_RATING')]}
    ),
    (
        "We're booking Cluj-Napoca, Romania, targeting 8 attractions by car. Lodging at Calea Bucuresti 22 and trying not to exceed 27 kilometers Expect to spend around 230 USD, and we're only considering places 78 points.",
        {'entities': [(14, 34, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (63, 66, 'TRANSPORT'), (123, 136, 'MAX_DISTANCE'), (79, 97, 'ADDRESS'), (160, 167, 'MAX_PRICE'), (203, 212, 'MIN_RATING')]}
    ),
    (
        "Ploiesti, Romania is on my radar! Planning 3 attractions and bicycle most of the way. Staying at Strada Republicii 20 and want to stay under 29 kilometers Expect to spend around 278 RON, and we're only considering places 74 points.",
        {'entities': [(0, 17, 'LOCATION'), (43, 56, 'ATTRACTIONS_COUNT'), (61, 68, 'TRANSPORT'), (141, 154, 'MAX_DISTANCE'), (97, 117, 'ADDRESS'), (178, 185, 'MAX_PRICE'), (221, 230, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Satu Mare, Romania—hoping to visit 10 attractions via walking. Our spot: Piata Avram Iancu 2. Distance? Around 19 kilometers Expect to spend around 183 EUR, and we're only considering places 4,6 stars.",
        {'entities': [(12, 30, 'LOCATION'), (47, 61, 'ATTRACTIONS_COUNT'), (66, 73, 'TRANSPORT'), (123, 136, 'MAX_DISTANCE'), (85, 104, 'ADDRESS'), (160, 167, 'MAX_PRICE'), (203, 212, 'MIN_RATING')]}
    ),
    (
        "I'm planning a trip to Satu Mare, Romania. I'd like to visit 3 attractions, mainly by bicycle, and stay at Strada Universitatii 5. I hope to keep it under 27 kilometers Expect to spend around $66, and we're only considering places 86 points.",
        {'entities': [(23, 41, 'LOCATION'), (61, 74, 'ATTRACTIONS_COUNT'), (86, 93, 'TRANSPORT'), (155, 168, 'MAX_DISTANCE'), (107, 129, 'ADDRESS'), (192, 195, 'MAX_PRICE'), (231, 240, 'MIN_RATING')]}
    ),
    (
        "We're booking Oradea, Romania, targeting 4 attractions by train. Lodging at Strada Tudor Vladimirescu 22 and trying not to exceed 20 kilometers Expect to spend around 160 dollars, and we're only considering places 76 points.",
        {'entities': [(14, 29, 'LOCATION'), (41, 54, 'ATTRACTIONS_COUNT'), (58, 63, 'TRANSPORT'), (130, 143, 'MAX_DISTANCE'), (76, 104, 'ADDRESS'), (167, 178, 'MAX_PRICE'), (214, 223, 'MIN_RATING')]}
    ),
    (
        "Craiova, Romania is on my radar! Planning 3 attractions and bus most of the way. Staying at Calea Victoriei 12 and want to stay under 25 kilometers Expect to spend around 65 RON, and we're only considering places 4,8 stars.",
        {'entities': [(0, 16, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (60, 63, 'TRANSPORT'), (134, 147, 'MAX_DISTANCE'), (92, 110, 'ADDRESS'), (171, 177, 'MAX_PRICE'), (213, 222, 'MIN_RATING')]}
    ),
    (
        "Next on the list: Satu Mare, Romania. About 9 attractions, traveling by bike, with a base at Bd. George Cosbuc 33. Hoping to stay within 12 kilometers Expect to spend around 288 EUR, and we're only considering places 40/10 score.",
        {'entities': [(18, 36, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (72, 76, 'TRANSPORT'), (137, 150, 'MAX_DISTANCE'), (93, 113, 'ADDRESS'), (174, 181, 'MAX_PRICE'), (217, 228, 'MIN_RATING')]}
    ),
    (
        "We're booking Arad, Romania, targeting 7 attractions by bike. Lodging at Strada Horea 7 and trying not to exceed 13 kilometers Expect to spend around 257 dollars, and we're only considering places rated 4,2/5.",
        {'entities': [(14, 27, 'LOCATION'), (39, 52, 'ATTRACTIONS_COUNT'), (56, 60, 'TRANSPORT'), (113, 126, 'MAX_DISTANCE'), (73, 87, 'ADDRESS'), (150, 161, 'MAX_PRICE'), (197, 208, 'MIN_RATING')]}
    ),
    (
        "Visiting Targu Mures, Romania soon! Plan is to cover 5 attractions by car. We'll lodge at Strada Mihai Eminescu 8, aiming not to exceed 12 kilometers Expect to spend around 132 dollars, and we're only considering places rated 4,6/5.",
        {'entities': [(9, 29, 'LOCATION'), (53, 66, 'ATTRACTIONS_COUNT'), (70, 73, 'TRANSPORT'), (136, 149, 'MAX_DISTANCE'), (90, 113, 'ADDRESS'), (173, 184, 'MAX_PRICE'), (220, 231, 'MIN_RATING')]}
    ),
    (
        "Focsani, Romania is on my radar! Planning 2 attractions and train most of the way. Staying at Calea Victoriei 12 and want to stay under 10 kilometers Expect to spend around 79 RON, and we're only considering places 94 points.",
        {'entities': [(0, 16, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (60, 65, 'TRANSPORT'), (136, 149, 'MAX_DISTANCE'), (94, 112, 'ADDRESS'), (173, 179, 'MAX_PRICE'), (215, 224, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Timisoara, Romania, aiming for 10 attractions. We'll use bike most of the time and rest at Strada Libertatii 15. No more than 18 kilometers Expect to spend around 84 EUR, and we're only considering places at least 4,6★.",
        {'entities': [(22, 40, 'LOCATION'), (53, 67, 'ATTRACTIONS_COUNT'), (79, 83, 'TRANSPORT'), (148, 161, 'MAX_DISTANCE'), (113, 133, 'ADDRESS'), (185, 191, 'MAX_PRICE'), (227, 240, 'MIN_RATING')]}
    ),
    (
        "Visiting Arad, Romania soon! Plan is to cover 8 attractions by bicycle. We'll lodge at Sos. Nicolina 50, aiming not to exceed 26 kilometers Expect to spend around 282 dollars, and we're only considering places 90 points.",
        {'entities': [(9, 22, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (63, 70, 'TRANSPORT'), (126, 139, 'MAX_DISTANCE'), (87, 103, 'ADDRESS'), (163, 174, 'MAX_PRICE'), (210, 219, 'MIN_RATING')]}
    ),
    (
        "We're booking Satu Mare, Romania, targeting 3 attractions by bus. Lodging at Strada Horea 7 and trying not to exceed 28 kilometers Expect to spend around $195, and we're only considering places 90 points.",
        {'entities': [(14, 32, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (61, 64, 'TRANSPORT'), (117, 130, 'MAX_DISTANCE'), (77, 91, 'ADDRESS'), (154, 158, 'MAX_PRICE'), (194, 203, 'MIN_RATING')]}
    ),
    (
        "We're booking Baia Mare, Romania, targeting 2 attractions by bus. Lodging at Strada Libertatii 15 and trying not to exceed 21 kilometers Expect to spend around 187 RON, and we're only considering places 4,0 stars.",
        {'entities': [(14, 32, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (61, 64, 'TRANSPORT'), (123, 136, 'MAX_DISTANCE'), (77, 97, 'ADDRESS'), (160, 167, 'MAX_PRICE'), (203, 212, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Satu Mare, Romania—hoping to visit 2 attractions via train. Our spot: Calea Bucuresti 22. Distance? Around 11 kilometers Expect to spend around 201 USD, and we're only considering places 96 points.",
        {'entities': [(12, 30, 'LOCATION'), (47, 60, 'ATTRACTIONS_COUNT'), (65, 70, 'TRANSPORT'), (119, 132, 'MAX_DISTANCE'), (82, 100, 'ADDRESS'), (156, 163, 'MAX_PRICE'), (199, 208, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Cluj-Napoca, Romania, aiming for 10 attractions. We'll use bike most of the time and rest at Strada Libertatii 15. No more than 11 kilometers Expect to spend around 203 EUR, and we're only considering places rated 3,9/5.",
        {'entities': [(22, 42, 'LOCATION'), (55, 69, 'ATTRACTIONS_COUNT'), (81, 85, 'TRANSPORT'), (150, 163, 'MAX_DISTANCE'), (115, 135, 'ADDRESS'), (187, 194, 'MAX_PRICE'), (230, 241, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Iasi, Romania—hoping to visit 10 attractions via bike. Our spot: Bd. Independentei 14. Distance? Around 13 kilometers Expect to spend around 159 EUR, and we're only considering places at least 3,5★.",
        {'entities': [(12, 25, 'LOCATION'), (42, 56, 'ATTRACTIONS_COUNT'), (61, 65, 'TRANSPORT'), (116, 129, 'MAX_DISTANCE'), (77, 97, 'ADDRESS'), (153, 160, 'MAX_PRICE'), (196, 209, 'MIN_RATING')]}
    ),
    (
        "Next on the list: Timisoara, Romania. About 4 attractions, traveling by bike, with a base at Strada Universitatii 5. Hoping to stay within 15 kilometers Expect to spend around 296 dollars, and we're only considering places 90 points.",
        {'entities': [(18, 36, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (72, 76, 'TRANSPORT'), (139, 152, 'MAX_DISTANCE'), (93, 115, 'ADDRESS'), (176, 187, 'MAX_PRICE'), (223, 232, 'MIN_RATING')]}
    ),
    (
        "We're booking Ploiesti, Romania, targeting 3 attractions by train. Lodging at Strada Memorandumului 5 and trying not to exceed 21 kilometers Expect to spend around 211 dollars, and we're only considering places 70 points.",
        {'entities': [(14, 31, 'LOCATION'), (43, 56, 'ATTRACTIONS_COUNT'), (60, 65, 'TRANSPORT'), (127, 140, 'MAX_DISTANCE'), (78, 101, 'ADDRESS'), (164, 175, 'MAX_PRICE'), (211, 220, 'MIN_RATING')]}
    ),
    (
        "Next on the list: Galati, Romania. About 7 attractions, traveling by bike, with a base at Strada Horea 7. Hoping to stay within 21 kilometers Expect to spend around 135 USD, and we're only considering places rated 4,9/5.",
        {'entities': [(18, 33, 'LOCATION'), (41, 54, 'ATTRACTIONS_COUNT'), (69, 73, 'TRANSPORT'), (128, 141, 'MAX_DISTANCE'), (90, 104, 'ADDRESS'), (165, 172, 'MAX_PRICE'), (208, 219, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Focsani, Romania—hoping to visit 5 attractions via walking. Our spot: Strada Libertatii 15. Distance? Around 25 kilometers Expect to spend around 91 RON, and we're only considering places 90 points.",
        {'entities': [(12, 28, 'LOCATION'), (45, 58, 'ATTRACTIONS_COUNT'), (63, 70, 'TRANSPORT'), (121, 134, 'MAX_DISTANCE'), (82, 102, 'ADDRESS'), (158, 164, 'MAX_PRICE'), (200, 209, 'MIN_RATING')]}
    ),
    (
        "Oradea, Romania is on my radar! Planning 6 attractions and bike most of the way. Staying at Strada Republicii 20 and want to stay under 24 kilometers Expect to spend around 109 RON, and we're only considering places rated 3,5/5.",
        {'entities': [(0, 15, 'LOCATION'), (41, 54, 'ATTRACTIONS_COUNT'), (59, 63, 'TRANSPORT'), (136, 149, 'MAX_DISTANCE'), (92, 112, 'ADDRESS'), (173, 180, 'MAX_PRICE'), (216, 227, 'MIN_RATING')]}
    ),
    (
        "Next on the list: Pitesti, Romania. About 5 attractions, traveling by walking, with a base at Bd. Mamaia 15. Hoping to stay within 11 kilometers Expect to spend around 219 EUR, and we're only considering places 80 points.",
        {'entities': [(18, 34, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (70, 77, 'TRANSPORT'), (131, 144, 'MAX_DISTANCE'), (94, 107, 'ADDRESS'), (168, 175, 'MAX_PRICE'), (211, 220, 'MIN_RATING')]}
    ),
    (
        "Iasi, Romania is on my radar! Planning 7 attractions and train most of the way. Staying at Strada Universitatii 5 and want to stay under 24 kilometers Expect to spend around 69 RON, and we're only considering places rated 4,2/5.",
        {'entities': [(0, 13, 'LOCATION'), (39, 52, 'ATTRACTIONS_COUNT'), (57, 62, 'TRANSPORT'), (137, 150, 'MAX_DISTANCE'), (91, 113, 'ADDRESS'), (174, 180, 'MAX_PRICE'), (216, 227, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bucharest, Romania where we hope to check out 6 attractions. Mostly walking, staying at Calea Victoriei 12, and keeping to 21 kilometers Expect to spend around $154, and we're only considering places at least 4,7★.",
        {'entities': [(20, 38, 'LOCATION'), (66, 79, 'ATTRACTIONS_COUNT'), (88, 95, 'TRANSPORT'), (143, 156, 'MAX_DISTANCE'), (108, 126, 'ADDRESS'), (180, 184, 'MAX_PRICE'), (220, 233, 'MIN_RATING')]}
    ),
    (
        "Visiting Oradea, Romania soon! Plan is to cover 2 attractions by car. We'll lodge at Bd. Mamaia 15, aiming not to exceed 22 kilometers Expect to spend around 292 EUR, and we're only considering places 100 points.",
        {'entities': [(9, 24, 'LOCATION'), (48, 61, 'ATTRACTIONS_COUNT'), (65, 68, 'TRANSPORT'), (121, 134, 'MAX_DISTANCE'), (85, 98, 'ADDRESS'), (158, 165, 'MAX_PRICE'), (201, 211, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Craiova, Romania, aiming for 6 attractions. We'll use bike most of the time and rest at Strada Libertatii 15. No more than 23 kilometers Expect to spend around 239 RON, and we're only considering places 72 points.",
        {'entities': [(22, 38, 'LOCATION'), (51, 64, 'ATTRACTIONS_COUNT'), (76, 80, 'TRANSPORT'), (145, 158, 'MAX_DISTANCE'), (110, 130, 'ADDRESS'), (182, 189, 'MAX_PRICE'), (225, 234, 'MIN_RATING')]}
    ),
    (
        "Visiting Brasov, Romania soon! Plan is to cover 6 attractions by car. We'll lodge at Calea Bucuresti 22, aiming not to exceed 30 kilometers Expect to spend around $150, and we're only considering places at least 4,4★.",
        {'entities': [(9, 24, 'LOCATION'), (48, 61, 'ATTRACTIONS_COUNT'), (65, 68, 'TRANSPORT'), (126, 139, 'MAX_DISTANCE'), (85, 103, 'ADDRESS'), (163, 167, 'MAX_PRICE'), (203, 216, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Galati, Romania—hoping to visit 4 attractions via bike. Our spot: Bd. George Cosbuc 33. Distance? Around 24 kilometers Expect to spend around $204, and we're only considering places rated 4,4/5.",
        {'entities': [(12, 27, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (62, 66, 'TRANSPORT'), (117, 130, 'MAX_DISTANCE'), (78, 98, 'ADDRESS'), (154, 158, 'MAX_PRICE'), (194, 205, 'MIN_RATING')]}
    ),
    (
        "We're booking Satu Mare, Romania, targeting 2 attractions by train. Lodging at Strada Universitatii 5 and trying not to exceed 22 kilometers Expect to spend around 289 RON, and we're only considering places at least 4,0★.",
        {'entities': [(14, 32, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (61, 66, 'TRANSPORT'), (127, 140, 'MAX_DISTANCE'), (79, 101, 'ADDRESS'), (164, 171, 'MAX_PRICE'), (207, 220, 'MIN_RATING')]}
    ),
    (
        "We're booking Constanta, Romania, targeting 3 attractions by train. Lodging at Strada Tudor Vladimirescu 22 and trying not to exceed 30 kilometers Expect to spend around 191 EUR, and we're only considering places 3,6 stars.",
        {'entities': [(14, 32, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (61, 66, 'TRANSPORT'), (133, 146, 'MAX_DISTANCE'), (79, 107, 'ADDRESS'), (170, 177, 'MAX_PRICE'), (213, 222, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Oradea, Romania where we hope to check out 2 attractions. Mostly car, staying at Bd. George Cosbuc 33, and keeping to 26 kilometers Expect to spend around 118 EUR, and we're only considering places 86 points.",
        {'entities': [(20, 35, 'LOCATION'), (63, 76, 'ATTRACTIONS_COUNT'), (85, 88, 'TRANSPORT'), (138, 151, 'MAX_DISTANCE'), (101, 121, 'ADDRESS'), (175, 182, 'MAX_PRICE'), (218, 227, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Iasi, Romania—hoping to visit 7 attractions via walking. Our spot: Bd. George Cosbuc 33. Distance? Around 28 kilometers Expect to spend around 139 EUR, and we're only considering places 98 points.",
        {'entities': [(12, 25, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (60, 67, 'TRANSPORT'), (118, 131, 'MAX_DISTANCE'), (79, 99, 'ADDRESS'), (155, 162, 'MAX_PRICE'), (198, 207, 'MIN_RATING')]}
    ),
    (
        "Next on the list: Suceava, Romania. About 4 attractions, traveling by walking, with a base at Strada Universitatii 5. Hoping to stay within 30 kilometers Expect to spend around $141, and we're only considering places rated 4,3/5.",
        {'entities': [(18, 34, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (70, 77, 'TRANSPORT'), (140, 153, 'MAX_DISTANCE'), (94, 116, 'ADDRESS'), (177, 181, 'MAX_PRICE'), (217, 228, 'MIN_RATING')]}
    ),
    (
        "Iasi, Romania is on my radar! Planning 5 attractions and car most of the way. Staying at Bd. Independentei 14 and want to stay under 27 kilometers Expect to spend around $249, and we're only considering places 88 points.",
        {'entities': [(0, 13, 'LOCATION'), (39, 52, 'ATTRACTIONS_COUNT'), (57, 60, 'TRANSPORT'), (133, 146, 'MAX_DISTANCE'), (89, 109, 'ADDRESS'), (170, 174, 'MAX_PRICE'), (210, 219, 'MIN_RATING')]}
    ),
    (
        "Heading to Cluj-Napoca, Romania, planning for 2 attractions, moving around by bicycle, and staying at Calea Bucuresti 22. Targeting 10 kilometers max Expect to spend around $86, and we're only considering places 4,2 stars.",
        {'entities': [(11, 31, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (78, 85, 'TRANSPORT'), (132, 145, 'MAX_DISTANCE'), (102, 120, 'ADDRESS'), (173, 176, 'MAX_PRICE'), (212, 221, 'MIN_RATING')]}
    ),
    (
        "Visiting Focsani, Romania soon! Plan is to cover 2 attractions by bus. We'll lodge at Bd. George Cosbuc 33, aiming not to exceed 27 kilometers Expect to spend around 198 USD, and we're only considering places 72 points.",
        {'entities': [(9, 25, 'LOCATION'), (49, 62, 'ATTRACTIONS_COUNT'), (66, 69, 'TRANSPORT'), (129, 142, 'MAX_DISTANCE'), (86, 106, 'ADDRESS'), (166, 173, 'MAX_PRICE'), (209, 218, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bacau, Romania where we hope to check out 3 attractions. Mostly bus, staying at Strada Tudor Vladimirescu 22, and keeping to 14 kilometers Expect to spend around 264 USD, and we're only considering places at least 3,5★.",
        {'entities': [(20, 34, 'LOCATION'), (62, 75, 'ATTRACTIONS_COUNT'), (84, 87, 'TRANSPORT'), (145, 158, 'MAX_DISTANCE'), (100, 128, 'ADDRESS'), (182, 189, 'MAX_PRICE'), (225, 238, 'MIN_RATING')]}
    ),
    (
        "I'm planning a trip to Sibiu, Romania. I'd like to visit 5 attractions, mainly by train, and stay at Bd. Independentei 14. I hope to keep it under 24 kilometers Expect to spend around 141 RON, and we're only considering places 43/10 score.",
        {'entities': [(23, 37, 'LOCATION'), (57, 70, 'ATTRACTIONS_COUNT'), (82, 87, 'TRANSPORT'), (147, 160, 'MAX_DISTANCE'), (101, 121, 'ADDRESS'), (184, 191, 'MAX_PRICE'), (227, 238, 'MIN_RATING')]}
    ),
    (
        "Visiting Arad, Romania soon! Plan is to cover 5 attractions by walking. We'll lodge at Strada Universitatii 5, aiming not to exceed 15 kilometers Expect to spend around 280 EUR, and we're only considering places at least 4,9★.",
        {'entities': [(9, 22, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (63, 70, 'TRANSPORT'), (132, 145, 'MAX_DISTANCE'), (87, 109, 'ADDRESS'), (169, 176, 'MAX_PRICE'), (212, 225, 'MIN_RATING')]}
    ),
    (
        "We're booking Brasov, Romania, targeting 6 attractions by walking. Lodging at Str. Vasile Lucaciu 9 and trying not to exceed 18 kilometers Expect to spend around $191, and we're only considering places 4,6 stars.",
        {'entities': [(14, 29, 'LOCATION'), (41, 54, 'ATTRACTIONS_COUNT'), (58, 65, 'TRANSPORT'), (125, 138, 'MAX_DISTANCE'), (78, 99, 'ADDRESS'), (162, 166, 'MAX_PRICE'), (202, 211, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Targu Mures, Romania where we hope to check out 3 attractions. Mostly bike, staying at Str. Vasile Lucaciu 9, and keeping to 20 kilometers Expect to spend around 231 dollars, and we're only considering places 86 points.",
        {'entities': [(20, 40, 'LOCATION'), (68, 81, 'ATTRACTIONS_COUNT'), (90, 94, 'TRANSPORT'), (145, 158, 'MAX_DISTANCE'), (107, 128, 'ADDRESS'), (182, 193, 'MAX_PRICE'), (229, 238, 'MIN_RATING')]}
    ),
    (
        "Visiting Constanta, Romania soon! Plan is to cover 9 attractions by walking. We'll lodge at Bd. Independentei 14, aiming not to exceed 16 kilometers Expect to spend around 60 RON, and we're only considering places 98 points.",
        {'entities': [(9, 27, 'LOCATION'), (51, 64, 'ATTRACTIONS_COUNT'), (68, 75, 'TRANSPORT'), (135, 148, 'MAX_DISTANCE'), (92, 112, 'ADDRESS'), (172, 178, 'MAX_PRICE'), (214, 223, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Ploiesti, Romania where we hope to check out 9 attractions. Mostly bike, staying at Calea Bucuresti 22, and keeping to 10 kilometers Expect to spend around 222 RON, and we're only considering places rated 3,6/5.",
        {'entities': [(20, 37, 'LOCATION'), (65, 78, 'ATTRACTIONS_COUNT'), (87, 91, 'TRANSPORT'), (139, 152, 'MAX_DISTANCE'), (104, 122, 'ADDRESS'), (176, 183, 'MAX_PRICE'), (219, 230, 'MIN_RATING')]}
    ),
    (
        "We’re off to Bacau, Romania, want to visit 4 attractions and will be using bus. Accommodation is Calea Bucuresti 22. Distance cap: 27 kilometers Expect to spend around 148 RON, and we're only considering places rated 4,7/5.",
        {'entities': [(13, 27, 'LOCATION'), (43, 56, 'ATTRACTIONS_COUNT'), (75, 78, 'TRANSPORT'), (131, 144, 'MAX_DISTANCE'), (97, 115, 'ADDRESS'), (168, 175, 'MAX_PRICE'), (211, 222, 'MIN_RATING')]}
    ),
    (
        "Cluj-Napoca, Romania is on my radar! Planning 6 attractions and train most of the way. Staying at Sos. Nicolina 50 and want to stay under 14 kilometers Expect to spend around $261, and we're only considering places 42/10 score.",
        {'entities': [(0, 20, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (64, 69, 'TRANSPORT'), (138, 151, 'MAX_DISTANCE'), (98, 114, 'ADDRESS'), (175, 179, 'MAX_PRICE'), (215, 226, 'MIN_RATING')]}
    ),
    (
        "Next on the list: Craiova, Romania. About 3 attractions, traveling by walking, with a base at Calea Bucuresti 22. Hoping to stay within 30 kilometers Expect to spend around $90, and we're only considering places 80 points.",
        {'entities': [(18, 34, 'LOCATION'), (42, 55, 'ATTRACTIONS_COUNT'), (70, 77, 'TRANSPORT'), (136, 149, 'MAX_DISTANCE'), (94, 112, 'ADDRESS'), (173, 176, 'MAX_PRICE'), (212, 221, 'MIN_RATING')]}
    ),
    (
        "Visiting Iasi, Romania soon! Plan is to cover 4 attractions by car. We'll lodge at Bd. Independentei 14, aiming not to exceed 21 kilometers Expect to spend around 79 RON, and we're only considering places 46/10 score.",
        {'entities': [(9, 22, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (63, 66, 'TRANSPORT'), (126, 139, 'MAX_DISTANCE'), (83, 103, 'ADDRESS'), (163, 169, 'MAX_PRICE'), (205, 216, 'MIN_RATING')]}
    ),
    (
        "We're booking Timisoara, Romania, targeting 4 attractions by bus. Lodging at Strada Horea 7 and trying not to exceed 10 kilometers Expect to spend around 141 RON, and we're only considering places 47/10 score.",
        {'entities': [(14, 32, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (61, 64, 'TRANSPORT'), (117, 130, 'MAX_DISTANCE'), (77, 91, 'ADDRESS'), (154, 161, 'MAX_PRICE'), (197, 208, 'MIN_RATING')]}
    ),
    (
        "We're booking Iasi, Romania, targeting 9 attractions by walking. Lodging at Bd. Independentei 14 and trying not to exceed 16 kilometers Expect to spend around 89 EUR, and we're only considering places 4,5 stars.",
        {'entities': [(14, 27, 'LOCATION'), (39, 52, 'ATTRACTIONS_COUNT'), (56, 63, 'TRANSPORT'), (122, 135, 'MAX_DISTANCE'), (76, 96, 'ADDRESS'), (159, 165, 'MAX_PRICE'), (201, 210, 'MIN_RATING')]}
    ),
    (
        "Visiting Arad, Romania soon! Plan is to cover 5 attractions by car. We'll lodge at Calea Victoriei 12, aiming not to exceed 16 kilometers Expect to spend around 244 RON, and we're only considering places 48/10 score.",
        {'entities': [(9, 22, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (63, 66, 'TRANSPORT'), (124, 137, 'MAX_DISTANCE'), (83, 101, 'ADDRESS'), (161, 168, 'MAX_PRICE'), (204, 215, 'MIN_RATING')]}
    ),
    (
        "Next on the list: Oradea, Romania. About 6 attractions, traveling by bike, with a base at Calea Bucuresti 22. Hoping to stay within 19 kilometers Expect to spend around 146 RON, and we're only considering places at least 3,8★.",
        {'entities': [(18, 33, 'LOCATION'), (41, 54, 'ATTRACTIONS_COUNT'), (69, 73, 'TRANSPORT'), (132, 145, 'MAX_DISTANCE'), (90, 108, 'ADDRESS'), (169, 176, 'MAX_PRICE'), (212, 225, 'MIN_RATING')]}
    ),
    (
        "We're booking Targu Mures, Romania, targeting 5 attractions by car. Lodging at Piata Victoriei 10 and trying not to exceed 30 kilometers Expect to spend around 242 EUR, and we're only considering places rated 3,7/5.",
        {'entities': [(14, 34, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (63, 66, 'TRANSPORT'), (123, 136, 'MAX_DISTANCE'), (79, 97, 'ADDRESS'), (160, 167, 'MAX_PRICE'), (203, 214, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Timisoara, Romania, aiming for 6 attractions. We'll use train most of the time and rest at Piata Victoriei 10. No more than 18 kilometers Expect to spend around 292 RON, and we're only considering places rated 4,5/5.",
        {'entities': [(22, 40, 'LOCATION'), (53, 66, 'ATTRACTIONS_COUNT'), (78, 83, 'TRANSPORT'), (146, 159, 'MAX_DISTANCE'), (113, 131, 'ADDRESS'), (183, 190, 'MAX_PRICE'), (226, 237, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Ploiesti, Romania, aiming for 7 attractions. We'll use car most of the time and rest at Strada Tudor Vladimirescu 22. No more than 25 kilometers Expect to spend around 128 EUR, and we're only considering places 96 points.",
        {'entities': [(22, 39, 'LOCATION'), (52, 65, 'ATTRACTIONS_COUNT'), (77, 80, 'TRANSPORT'), (153, 166, 'MAX_DISTANCE'), (110, 138, 'ADDRESS'), (190, 197, 'MAX_PRICE'), (233, 242, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Iasi, Romania, aiming for 7 attractions. We'll use car most of the time and rest at Calea Victoriei 12. No more than 21 kilometers Expect to spend around 243 EUR, and we're only considering places 88 points.",
        {'entities': [(22, 35, 'LOCATION'), (48, 61, 'ATTRACTIONS_COUNT'), (73, 76, 'TRANSPORT'), (139, 152, 'MAX_DISTANCE'), (106, 124, 'ADDRESS'), (176, 183, 'MAX_PRICE'), (219, 228, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Oradea, Romania, aiming for 5 attractions. We'll use walking most of the time and rest at Piata Victoriei 10. No more than 27 kilometers Expect to spend around 163 dollars, and we're only considering places 42/10 score.",
        {'entities': [(22, 37, 'LOCATION'), (50, 63, 'ATTRACTIONS_COUNT'), (75, 82, 'TRANSPORT'), (145, 158, 'MAX_DISTANCE'), (112, 130, 'ADDRESS'), (182, 193, 'MAX_PRICE'), (229, 240, 'MIN_RATING')]}
    ),
    (
        "Baia Mare, Romania is on my radar! Planning 7 attractions and bus most of the way. Staying at Piata Victoriei 10 and want to stay under 14 kilometers Expect to spend around 77 RON, and we're only considering places rated 4,8/5.",
        {'entities': [(0, 18, 'LOCATION'), (44, 57, 'ATTRACTIONS_COUNT'), (62, 65, 'TRANSPORT'), (136, 149, 'MAX_DISTANCE'), (94, 112, 'ADDRESS'), (173, 179, 'MAX_PRICE'), (215, 226, 'MIN_RATING')]}
    ),
    (
        "Heading to Buzau, Romania, planning for 3 attractions, moving around by car, and staying at Bd. Mamaia 15. Targeting 21 kilometers max Expect to spend around 163 USD, and we're only considering places 40/10 score.",
        {'entities': [(11, 25, 'LOCATION'), (40, 53, 'ATTRACTIONS_COUNT'), (72, 75, 'TRANSPORT'), (117, 130, 'MAX_DISTANCE'), (92, 105, 'ADDRESS'), (158, 165, 'MAX_PRICE'), (201, 212, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Suceava, Romania, aiming for 9 attractions. We'll use walking most of the time and rest at Bd. Independentei 14. No more than 22 kilometers Expect to spend around 177 EUR, and we're only considering places 3,9 stars.",
        {'entities': [(22, 38, 'LOCATION'), (51, 64, 'ATTRACTIONS_COUNT'), (76, 83, 'TRANSPORT'), (148, 161, 'MAX_DISTANCE'), (113, 133, 'ADDRESS'), (185, 192, 'MAX_PRICE'), (228, 237, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Targu Mures, Romania where we hope to check out 3 attractions. Mostly train, staying at Bd. Mamaia 15, and keeping to 16 kilometers Expect to spend around 204 RON, and we're only considering places 74 points.",
        {'entities': [(20, 40, 'LOCATION'), (68, 81, 'ATTRACTIONS_COUNT'), (90, 95, 'TRANSPORT'), (138, 151, 'MAX_DISTANCE'), (108, 121, 'ADDRESS'), (175, 182, 'MAX_PRICE'), (218, 227, 'MIN_RATING')]}
    ),
    (
        "Sibiu, Romania is on my radar! Planning 9 attractions and train most of the way. Staying at Calea Victoriei 12 and want to stay under 30 kilometers Expect to spend around 251 RON, and we're only considering places 4,2 stars.",
        {'entities': [(0, 14, 'LOCATION'), (40, 53, 'ATTRACTIONS_COUNT'), (58, 63, 'TRANSPORT'), (134, 147, 'MAX_DISTANCE'), (92, 110, 'ADDRESS'), (171, 178, 'MAX_PRICE'), (214, 223, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bacau, Romania where we hope to check out 9 attractions. Mostly car, staying at Bd. Mamaia 15, and keeping to 26 kilometers Expect to spend around 92 USD, and we're only considering places rated 4,4/5.",
        {'entities': [(20, 34, 'LOCATION'), (62, 75, 'ATTRACTIONS_COUNT'), (84, 87, 'TRANSPORT'), (130, 143, 'MAX_DISTANCE'), (100, 113, 'ADDRESS'), (167, 173, 'MAX_PRICE'), (209, 220, 'MIN_RATING')]}
    ),
    (
        "Visiting Brasov, Romania soon! Plan is to cover 5 attractions by bicycle. We'll lodge at Piata Avram Iancu 2, aiming not to exceed 12 kilometers Expect to spend around 74 dollars, and we're only considering places 82 points.",
        {'entities': [(9, 24, 'LOCATION'), (48, 61, 'ATTRACTIONS_COUNT'), (65, 72, 'TRANSPORT'), (131, 144, 'MAX_DISTANCE'), (89, 108, 'ADDRESS'), (168, 178, 'MAX_PRICE'), (214, 223, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Constanta, Romania, aiming for 2 attractions. We'll use train most of the time and rest at Strada Horea 7. No more than 15 kilometers Expect to spend around 290 dollars, and we're only considering places 4,9 stars.",
        {'entities': [(22, 40, 'LOCATION'), (53, 66, 'ATTRACTIONS_COUNT'), (78, 83, 'TRANSPORT'), (142, 155, 'MAX_DISTANCE'), (113, 127, 'ADDRESS'), (179, 190, 'MAX_PRICE'), (226, 235, 'MIN_RATING')]}
    ),
    (
        "Oradea, Romania is on my radar! Planning 4 attractions and train most of the way. Staying at Bd. George Cosbuc 33 and want to stay under 11 kilometers Expect to spend around 194 RON, and we're only considering places 3,8 stars.",
        {'entities': [(0, 15, 'LOCATION'), (41, 54, 'ATTRACTIONS_COUNT'), (59, 64, 'TRANSPORT'), (137, 150, 'MAX_DISTANCE'), (93, 113, 'ADDRESS'), (174, 181, 'MAX_PRICE'), (217, 226, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Timisoara, Romania where we hope to check out 10 attractions. Mostly walking, staying at Strada Memorandumului 5, and keeping to 23 kilometers Expect to spend around 237 dollars, and we're only considering places 43/10 score.",
        {'entities': [(20, 38, 'LOCATION'), (66, 80, 'ATTRACTIONS_COUNT'), (89, 96, 'TRANSPORT'), (149, 162, 'MAX_DISTANCE'), (109, 132, 'ADDRESS'), (186, 197, 'MAX_PRICE'), (233, 244, 'MIN_RATING')]}
    ),
    (
        "We're booking Satu Mare, Romania, targeting 10 attractions by car. Lodging at Piata Avram Iancu 2 and trying not to exceed 13 kilometers Expect to spend around 107 USD, and we're only considering places 88 points.",
        {'entities': [(14, 32, 'LOCATION'), (44, 58, 'ATTRACTIONS_COUNT'), (62, 65, 'TRANSPORT'), (123, 136, 'MAX_DISTANCE'), (78, 97, 'ADDRESS'), (160, 167, 'MAX_PRICE'), (203, 212, 'MIN_RATING')]}
    ),
    (
        "Heading to Ploiesti, Romania, planning for 4 attractions, moving around by car, and staying at Strada Mihai Eminescu 8. Targeting 15 kilometers max Expect to spend around 86 RON, and we're only considering places rated 3,8/5.",
        {'entities': [(11, 28, 'LOCATION'), (43, 56, 'ATTRACTIONS_COUNT'), (75, 78, 'TRANSPORT'), (130, 143, 'MAX_DISTANCE'), (95, 118, 'ADDRESS'), (171, 177, 'MAX_PRICE'), (213, 224, 'MIN_RATING')]}
    ),
    (
        "Visiting Arad, Romania soon! Plan is to cover 7 attractions by bicycle. We'll lodge at Str. Vasile Lucaciu 9, aiming not to exceed 21 kilometers Expect to spend around 190 RON, and we're only considering places rated 4,2/5.",
        {'entities': [(9, 22, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (63, 70, 'TRANSPORT'), (131, 144, 'MAX_DISTANCE'), (87, 108, 'ADDRESS'), (168, 175, 'MAX_PRICE'), (211, 222, 'MIN_RATING')]}
    ),
    (
        "Thinking of exploring Bacau, Romania, aiming for 9 attractions. We'll use bike most of the time and rest at Strada Memorandumului 5. No more than 19 kilometers Expect to spend around 258 dollars, and we're only considering places 5,0 stars.",
        {'entities': [(22, 36, 'LOCATION'), (49, 62, 'ATTRACTIONS_COUNT'), (74, 78, 'TRANSPORT'), (146, 159, 'MAX_DISTANCE'), (108, 131, 'ADDRESS'), (183, 194, 'MAX_PRICE'), (230, 239, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bucharest, Romania where we hope to check out 5 attractions. Mostly car, staying at Bd. Mamaia 15, and keeping to 18 kilometers Expect to spend around 127 EUR, and we're only considering places 82 points.",
        {'entities': [(20, 38, 'LOCATION'), (66, 79, 'ATTRACTIONS_COUNT'), (88, 91, 'TRANSPORT'), (134, 147, 'MAX_DISTANCE'), (104, 117, 'ADDRESS'), (171, 178, 'MAX_PRICE'), (214, 223, 'MIN_RATING')]}
    ),
    (
        "Dreaming of Ploiesti, Romania—hoping to visit 9 attractions via walking. Our spot: Calea Bucuresti 22. Distance? Around 27 kilometers Expect to spend around 147 dollars, and we're only considering places rated 4,7/5.",
        {'entities': [(12, 29, 'LOCATION'), (46, 59, 'ATTRACTIONS_COUNT'), (64, 71, 'TRANSPORT'), (120, 133, 'MAX_DISTANCE'), (83, 101, 'ADDRESS'), (157, 168, 'MAX_PRICE'), (204, 215, 'MIN_RATING')]}
    ),
    (
        "I'm planning a trip to Ploiesti, Romania. I'd like to visit 4 attractions, mainly by bicycle, and stay at Strada Memorandumului 5. I hope to keep it under 22 kilometers Expect to spend around 263 RON, and we're only considering places at least 4,4★.",
        {'entities': [(23, 40, 'LOCATION'), (60, 73, 'ATTRACTIONS_COUNT'), (85, 92, 'TRANSPORT'), (155, 168, 'MAX_DISTANCE'), (106, 129, 'ADDRESS'), (192, 199, 'MAX_PRICE'), (235, 248, 'MIN_RATING')]}
    ),
    (
        "I'm planning a trip to Cluj-Napoca, Romania. I'd like to visit 5 attractions, mainly by bike, and stay at Str. Vasile Lucaciu 9. I hope to keep it under 20 kilometers Expect to spend around 136 RON, and we're only considering places 45/10 score.",
        {'entities': [(23, 43, 'LOCATION'), (63, 76, 'ATTRACTIONS_COUNT'), (88, 92, 'TRANSPORT'), (153, 166, 'MAX_DISTANCE'), (106, 127, 'ADDRESS'), (190, 197, 'MAX_PRICE'), (233, 244, 'MIN_RATING')]}
    ),
    (
        "We’re off to Pitesti, Romania, want to visit 2 attractions and will be using car. Accommodation is Sos. Nicolina 50. Distance cap: 21 kilometers Expect to spend around 172 dollars, and we're only considering places 72 points.",
        {'entities': [(13, 29, 'LOCATION'), (45, 58, 'ATTRACTIONS_COUNT'), (77, 80, 'TRANSPORT'), (131, 144, 'MAX_DISTANCE'), (99, 115, 'ADDRESS'), (168, 179, 'MAX_PRICE'), (215, 224, 'MIN_RATING')]}
    ),
    (
        "Our next getaway is Bucharest, Romania where we hope to check out 6 attractions. Mostly bike, staying at Str. Vasile Lucaciu 9, and keeping to 19 kilometers Expect to spend around 292 EUR, and we're only considering places 3,7 stars.",
        {'entities': [(20, 38, 'LOCATION'), (66, 79, 'ATTRACTIONS_COUNT'), (88, 92, 'TRANSPORT'), (143, 156, 'MAX_DISTANCE'), (105, 126, 'ADDRESS'), (180, 187, 'MAX_PRICE'), (223, 232, 'MIN_RATING')]}
    ),
]