import random
from enum import Enum
from typing import Dict, Any, List

import openai
from emora_stdm import DialogueFlow, Macro, Ngrams

from src import utils
from src.utils import MacroGPTJSON, MacroNLG

PATH_USER_INFO = 'resources/userinfo.json'

class V(Enum):
    call_names = 0,
    apt_type = 1
    apt_hours = 2
def hair_salon() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hello, what\'s your name?`': {
            '#SET_CALL_NAMES': {
                'state': 'app',
                '`What kind of appointment are you looking to book ` #GET_CALL_NAME`? What day and time would you '
                'like?`': {
                    '#SET_APT_TYPE_HOURS': {
                        '#VALID': 'end'

                    }
                }
            }
        }
    }
    macros = {
        'VALID': MacroValid(),
        'GET_CALL_NAME': MacroNLG(get_call_name),
        'GET_APT_TYPE_HOURS': MacroNLG(get_apt_type_hours),
        'SET_CALL_NAMES': MacroGPTJSON(
            'How does the speaker want to be called?',
            {V.call_names.name: ["Mike", "Michael"]}),
        'SET_APT_TYPE_HOURS': MacroGPTJSON(
            'What type of appointment does the speaker want to book, please sort into "Hair Cut", "Hair Coloring", "Perm", or "Other".Also what day of the week and what time does the speaker want to book for their appointment?',
            {V.apt_type.name: "Hair Cut", V.apt_hours.name: [{"day": "Monday", "time": "14:00"}]},
            {V.apt_type.name: "N/A", V.apt_hours.name: []},
            set_apt_type_hours
        ),
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    df.add_macros(macros)
    return df

class MacroValid(Macro):
   def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        valid = "Great, your appointment is booked!"
        invalid = "Sorry that time isn't available."
        if vars[V.apt_type.name] == "Hair Cut":
            if vars[V.apt_hours.name] == {'Tuesday': ['14:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Monday': ['14:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Monday': ['10:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Monday': ['13:00']}:
                return valid
            else:
                return invalid
        if vars[V.apt_type.name] == "Hair Coloring":
            if vars[V.apt_hours.name] == {'Wednesday': ['13:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Wednesday': ['11:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Wednesday': ['10:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Thursday': ['11:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Thursday': ['10:00']}:
                return valid
            else:
                return invalid
        if vars[V.apt_type.name] == "Perm":
            if vars[V.apt_hours.name] == {'Friday': ['10:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Friday': ['11:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Friday': ['13:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Friday': ['14:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Saturday': ['10:00']}:
                return valid
            if vars[V.apt_hours.name] == {'Saturday': ['14:00']}:
                return valid
            else:
                return invalid
        else:
            return "Sorry we don't perform that service."


def get_call_name(vars: Dict[str, Any]):
    ls = vars[V.call_names.name]
    return ls[random.randrange(len(ls))]


def get_apt_type_hours(vars: Dict[str, Any]):
    return '\n- Type: {}\n- Hours: {}'.format(vars[V.apt_type.name], vars[V.apt_hours.name])


def set_apt_type_hours(vars: Dict[str, Any], user: Dict[str, Any]):
    vars[V.apt_type.name] = user[V.apt_type.name]
    vars[V.apt_hours.name] = {d['day']: [d['time']] for d in user[V.apt_hours.name]}

# macro to check if appointment is valid

if __name__ == '__main__':
    openai.api_key_path = utils.OPENAI_API_KEY_PATH
    hair_salon().run()