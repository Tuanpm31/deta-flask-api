from flask import Flask, request
from deta import Deta
from flask.json import jsonify
from flask_restful.inputs import boolean

# put your project keys here
deta = Deta("")
db = deta.Base("todos")

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
  return "Hello World"

@app.route("/todos", methods=["POST"])
def create_todos():
  title = request.json.get("title")
  description = request.json.get("description")
  completed = request.json.get("completed")

  todo = db.put({
    "title": title,
    "description": description,
    "completed": completed
  })
  return jsonify(todo), 201

@app.route("/todos", methods=["GET"])
def get_todos():
  completed = boolean(request.args.get("completed"))
  todos = db.fetch({"completed": completed})
  return jsonify(todos.items), 200

@app.route("/todos", methods=["PUT"])
def update_todos():
  todo = db.put(request.json)
  return todo

@app.route("/todos/<key>", methods=["DELETE"])
def delete_todos(key):
  db.delete(key)
  return jsonify({"success": True})


if __name__ == "__main__":
  app.run(debug=True)