from flask import Flask, jsonify, request

app = Flask(__name__)

users_data = []

@app.route('/users')
def users():
    return jsonify({"users": users_data})

@app.route('/users', methods=['POST'])
def add_users():
    data = request.get_json()
    users_data.append({
        "name": data['name'],
        "birth": data['birth']
    })

    return jsonify({"msg": "usuario cadastrado com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)
