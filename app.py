from flask import Flask, jsonify, request

app = Flask(__name__)

stores = {
    'myStore': {
        'name': 'My store',
        'items': {
            'item1': {
                'name': 'my item',
                'price': 15.99
            },
            'item2': {
                'name': 'your item',
                'price': 1.99
            }
        }
    },
    'otherStore': {
        'name': 'The other store',
        'items': {
            'item1': {
                'name': 'other item',
                'price': 9.99
            }
        }
    }
}


@app.route('/')
def home():
    return "Hello my man!! Welcome to the store!\n"


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    if request_data['id'] not in stores.keys():
        new_store = {
            'name': request_data['name'],
            'items': {}
        }
        stores[request_data['id']] = new_store
        return jsonify(new_store)
    else:
        return jsonify("Store already exist; Object not created.")


@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify(stores)


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for key in stores.keys():
        if key == name:
            return jsonify(stores[key])


@app.route('/store/<string:name>/<string:item>', methods=["GET"])
def get_items_in_store(name, item):
    for key in stores.keys():
        if key == name:
            for second_key in stores[key]['items'].keys():
                if item == second_key:
                    return jsonify(stores[key]['items'][second_key])


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass


app.run(port=5000)
