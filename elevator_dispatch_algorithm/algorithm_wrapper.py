import file_util
import algorithm_implement
import json
import make_json_serializable  # 用于自定义对象的JSON


class algorithm_result:
    elevators = []
    people = []

    def to_json(self):
        dict_name_value = {}

        for name, value in vars(self).items():
            dict_name_value[name] = value
        return dict_name_value


if __name__ == "__main__":
    js = file_util.read_all_text('in.json')
    js = json.loads(js)
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
