from flask import Flask, request
import json
import algorithm_implement
import make_json_serializable
app = Flask(__name__)

class algorithm_result:
    elevators = []
    people = []

    def to_json(self):
        dict_name_value = {}

        for name, value in vars(self).items():
            dict_name_value[name] = value
        return dict_name_value

@app.route('/', methods=['GET'])
def hello():
    return 'Hello! This is a elevator dispatch Server, powered by Flask, Please use POST :D'


@app.route('/', methods=['post'])
def algorithm():
    data=request.get_data()

    js = json.loads(data)
    t = js['Time']

    people = []
    for p in js['People']:
        person = algorithm_implement.person()
        person.come_time = p['come_time']
        person.from_floor = p['from_floor']
        person.to_floor = p['to_floor']
        person.current_floor = p['current_floor']
        person.in_which_elevator = p['in_which_elevator']
        person.is_out = p['is_out']

        people.append(person)
    result = algorithm_implement.core_algorithm(t, people)
    r = algorithm_result()
    r.elevators = result[0]
    r.people = result[1]
    r_json = json.dumps(r, indent=4)
    print(r_json)
    return r_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
