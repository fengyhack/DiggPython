from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

class TaskListAPI(Resource):
    def get(self):
        return jsonify({'tasks': tasks})

    def post(self):
        return "POST"

api.add_resource(TaskListAPI, '/tasks', endpoint = 'tasks')

class TaskAPI(Resource):
    def get(self, id):
        task = list(filter(lambda t: t['id'] == id, tasks))
        if len(task) == 0:
            abort(404)
        return jsonify({'task': task[0]})

    def put(self, id):
        return "PUT"

    def delete(self, id):
        return "DELETE"

api.add_resource(TaskAPI, '/tasks/<int:id>', endpoint = 'task')

@app.route('/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify( { 'task': task[0] } )
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)