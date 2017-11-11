import json

def read_data(path = 'data.json'):
    try:
        with open(path, 'r') as f:
            data = json.loads(f.read())
        print('data loaded from FILE')
        return data
    except Exception:
        data = {
            'users': [
                {'id': 1, 'name': 'Arnold Sh'},
                {'id': 2, 'name': 'Harsimrat Kaur Badal'},
                {'id': 3, 'name': 'Dharmendra Pradhan'},
                {'id': 4, 'name': 'Sushma Swaraj'},
                {'id': 5, 'name': 'Grigory R'},
                #{'id': 6, 'name': 'Sushri Uma Bharati'},
                #{'id': 7, 'name': 'Presley E'},
                #{'id': 8, 'name': 'Maneka Sanjay Gandhi'},
                #{'id': 9, 'name': 'Gendalf G'},
                #{'id': 10, 'name': 'Mukhtar Abbas Naqvi'}
            ],
            'comments': [
                {
                    'id': 1,
                    'text': 'Unfortunately, many of today`s performance reviews aren`t anywhere as effective as they could be. In fact, Fast Company reports that 74% of younger workers leave reviews unsure about what their managers actually think of their performance.',
                    'commenter': 1
                },
                {
                    'id': 2,
                    'text': 'Catalufa eelpout. Gulper eel collared carpetshark electric ray bream yellowtail bigeye squaretail zebra oto skipjack tuna bull shark. Guitarfish gulf menhaden golden trout amur pike sauger Bombay duck, angelfish, sandburrower; buffalofish channel catfish panga pikeperch knifejaw Antarctic icefish? Cutthroat trout telescopefish roosterfish pejerrey eulachon alooh sea bream. North American darter Kafue pike velvet catfish soldierfish northern anchovy trench threadfin bream New World rivuline rockling antenna codlet." Trevally barbeled houndshark grunion tubeblenny sleeper shark madtom walking catfish merluccid hake.',
                    'commenter': 2
                },
                {
                    'id': 3,
                    'text': 'Slimy mackerel char; three-toothed puffer pilchard; splitfin hawkfish butterfly ray Australasian salmon. Mouthbrooder morid cod redmouth whalefish boxfish trout-perch; channel catfish, lemon sole, sailback scorpionfish saury ghost carp whale shark.',
                    'commenter': 5
                },
                {
                    'id': 4,
                    'text': 'Snake mudhead bat ray canary rockfish Billfish lighthousefish; sweeper angelfish trout cod huchen eel ribbonbearer. Yellowtail, spotted danio sockeye salmon morid cod, "hog sucker, sturgeon." Ragfish Black sea bass swordtail ridgehead; orbicular velvetfish creek chub emperor bream garibaldi hussar scorpionfish. Crocodile icefish loach minnow popeye catafula dory eagle ray rough scad herring glassfish, butterfly ray. Duckbill eel; grass carp. Barbel razorfish pirate perch sand stargazer priapumfish largemouth bass mummichog California halibut squawfish hake smalleye squaretail velvet catfish.',
                    'commenter': 3
                },
                {
                    'id': 5,
                    'text': 'Dolly Varden trout loach minnow marlin lemon shark scaly dragonfish spadefish stoneroller minnow. Longnose sucker, archerfish flying gurnard. Black swallower electric knifefish orangespine unicorn fish slimy mackerel redmouth whalefish topminnow velvetfish, tripod fish dusky grouper yellowtail clownfish orangespine unicorn fish. Tadpole cod sablefish common tunny: footballfish desert pupfish glass catfish butterfly ray pirate perch. Bramble shark beaked salmon, summer flounder pearlfish opaleye flashlight fish galjoen fish haddock California flyingfish smelt huchen, leopard danio',
                    'commenter': 4
                },
                {
                    'id': 6,
                    'text': 'Mozambique tilapia yellowtail kingfish knifejaw boga threadfin bream sea lamprey hussar snook yellowfin grouper, scup, black dragonfish. Bocaccio swamp-eel suckermouth armored catfish common tunny lungfish New Zealand sand diver. Ground shark clownfish stingfish barbelless catfish? Wrymouth threadfin California smoothtongue New World rivuline wels catfish torrent fish wallago. Silverside tarpon; Pacific trout fingerfish opah sunfish African lungfish, "Japanese eel," scup seamoth South American darter? North American freshwater catfish. Sand knifefish northern sea robin, porbeagle shark squeaker, jackfish luminous hake arowana threespine stickleback sand dab? Herring smelt barred danio oldwife, lightfish armorhead, "lancetfish, pencilsmelt." Opaleye hamlet menhaden medaka cavefish grunt sculpin beaked sandfish leopard danio deep sea anglerfish? Beardfish surf sardine wrasse spearfish requiem shark minnow nibbler, cusk-eel bristlenose catfish gulper; pollyfish pineconef',
                    'commenter': 3
                },
                {
                    'id': 7,
                    'text': 'North American freshwater catfish, river stingray, firefish opaleye alooh spookfish Blenny velvet-belly shark, arapaima." Shiner sandroller, guppy telescopefish deep sea bonefish, "loach forehead brooder river loach swamp-eel handfish triplespine, scat sole eelblenny sawfish kuhli loach koi, olive flounder, Old World rivuline." Gizzard shad. Amago grayling tench ronquil Rattail lampfish sawtooth eel loweye catfish neon tetra.',
                    'commenter': 4
                }
            ],
            'articles': [
                {
                    'id': 1,
                    'author': 5,
                    'title': 'Cucumbers recalled in salmonella outbreak',
                    'text': 'Article 1. Unfortunately, many effective as they could be. In fact, Fast Company reports that 74% of younger workers leave reviews unsure about what their managers actually think of their performance.',
                    'comments': [1, 3, 7]
                },
                {
                    'id': 2,
                    'author': 2,
                    'title': 'Hungary migrant stand-off continues',
                    'text': 'Article 2. Gulper eel collared carpetshark electric ray bream yellowtail bigeye squaretail zebra oto skipjack tuna bull shark. Guitarfish gulf menhaden golden trout amur pike sauger Bombay duck, angelfish, sandburrower; buffalofish channel catfish panga pikeperch knifejaw Antarctic icefish? Cutthroat trout telescopefish roosterfish pejerrey eulachon alooh sea bream. North American darter Kafue pike velvet catfish soldierfish northern anchovy trench threadfin bream New World rivuline rockling antenna codlet." Trevally barbeled houndshark grunion tubeblenny sleeper shark madtom walking catfish merluccid hake.',
                    'comments': [2, 4]
                },
                {
                    'id': 3,
                    'author': 1,
                    'title': 'Kapoor sculpture vandalized again',
                    'text': 'Article 3. Slimy mackerel char; three-toothed puffer pilchard; splitfin hawkfish butterfly ray Australasian salmon. Mouthbrooder morid cod redmouth whalefish boxfish trout-perch; channel catfish, lemon sole, sailback scorpionfish saury ghost carp whale shark.',
                    'comments': [5, 6]
                }
            ]
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        print('DEFAULT data loaded')
        return data
    finally:
        f.close()

def get_author_info(author_id, app_data):
    for user in app_data['users']:
        if user['id'] == author_id:
            author = {
                'id': user['id'],
                'name': user['name']
            }
    if 'author' in locals():
        return {
            'id': author['id'],
            'name': author['name']
        }
    else:
        return {
            'id': '',
            'name': ''
        }

def get_comments(comments_id_array, app_data):
    comments_info_array = []
    for comment_id in comments_id_array:
        for comment in app_data['comments']:
            if comment['id'] == comment_id:
                prepared_comment = {
                    'id': comment['id'],
                    'text': comment['text'],
                    'commenter': get_author_info(comment['commenter'], app_data)
                }
                comments_info_array.append(prepared_comment)
    return comments_info_array

def get_comments_by_author(author_id):
    comments_info_array = []
    return comments_info_array

def get_article_by_id(article_id, app_data):
    for article in app_data['articles']:
        if article['id'] == article_id:
            article_info = {
                'id': article['id'],
                'author': get_author_info(article['author'], app_data),
                'title': article['title'],
                'text': article['text'],
                'comments': get_comments(article['comments'], app_data)
            }

    if 'article_info' in locals():
        return {
            'id': article_info['id'],
            'author': article_info['author'],
            'title': article_info['title'],
            'text': article_info['text'],
            'comments': article_info['comments']
        }
    else:
        return {
            'id': '',
            'author': '',
            'title': '',
            'text': '',
            'comments': []
        }

