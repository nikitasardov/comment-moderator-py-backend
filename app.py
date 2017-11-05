#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import Response
import json
import get_functions

app = Flask(__name__)

#app_data
app_data  = {
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
            'title': 'Article 1',
            'text': 'Article 1. Unfortunately, many effective as they could be. In fact, Fast Company reports that 74% of younger workers leave reviews unsure about what their managers actually think of their performance.',
            'comments': [1, 3, 7]
        },
        {
            'id': 2,
            'author': 2,
            'title': 'Article 2',
            'text': 'Article 2. Gulper eel collared carpetshark electric ray bream yellowtail bigeye squaretail zebra oto skipjack tuna bull shark. Guitarfish gulf menhaden golden trout amur pike sauger Bombay duck, angelfish, sandburrower; buffalofish channel catfish panga pikeperch knifejaw Antarctic icefish? Cutthroat trout telescopefish roosterfish pejerrey eulachon alooh sea bream. North American darter Kafue pike velvet catfish soldierfish northern anchovy trench threadfin bream New World rivuline rockling antenna codlet." Trevally barbeled houndshark grunion tubeblenny sleeper shark madtom walking catfish merluccid hake.',
            'comments': [2, 4]
        },
        {
            'id': 3,
            'author': 1,
            'title': 'Article 3',
            'text': 'Article 3. Slimy mackerel char; three-toothed puffer pilchard; splitfin hawkfish butterfly ray Australasian salmon. Mouthbrooder morid cod redmouth whalefish boxfish trout-perch; channel catfish, lemon sole, sailback scorpionfish saury ghost carp whale shark.',
            'comments': [5, 6]
        }
    ]
}

def to_json(data):
    return json.dumps(data, sort_keys=True, indent=2) + "\n"


def resp(code, data):
    return Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )

#GET /api/articles
@app.route('/api/articles/')
def get_all_articles():
    articles_array = []
    for article in app_data['articles']:
        a = get_functions.get_article_by_id(article['id'], app_data)
        articles_array.append(a)
    return resp(200, articles_array)

#GET /api/articles/<id>
@app.route('/api/articles/<int:article_id>')
def get_article_id(article_id):
    a = get_functions.get_article_by_id(article_id, app_data)
    return resp(200, a)

#PUT /api/comments/1
@app.route('/api/comments/<int:comment_id>', methods=['PUT'])
def put_comment(comment_id):
    return 'PUT /api/comments/%d' % comment_id
    #{"success": true}

#PUT /api/user/1
@app.route('/api/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    new_users = []
    for user in app_data['users']:
        if user['id'] == user_id:
            new_users.append({'id': user_id, 'name': request.form['name']})
        else:
            new_users.append(user)
    app_data.update({'users': new_users})

    return resp(200, {'success': True})

@app.errorhandler(404)
def page_not_found(error):
    #return 'incorrect api address', 400
    bad_request = {'message':'incorrect api address'}
    return resp(400, bad_request)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4567)
