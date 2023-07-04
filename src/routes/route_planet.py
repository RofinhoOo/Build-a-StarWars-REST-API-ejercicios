

@app.route('/planets/<int:planets_id>', methods=['GET'])
def handle_planets_id(planets_id):

    response_body = {
        "msg": f"Hello, this is your GET /planets/<int:planets_id> response {planets_id}"

    }
    
    return jsonify(response_body), 200