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


# Quiz 5 Questions

# What are the limitations of the Bag-of-Words representation?

# Bag-of-Words takes up a lot of space because each word has a vector space. Since the bag of words has every value
# that is not in the string set to 0, and the rest of the values set to the frequency that they occur. However,
# frequency may be the most representative way to capture the meaning of words. Words that appear the most frequently
# such as articles might not convey as much meaning as rarer words such as proper nouns. Additionally Bag of Words
# does not preserve the order of strings, which could change the meaning of the sentence.

# Describe the Chain Rule and Markov Assumption and how they are used to estimate the probability of a word sequence.

# The chain rule is used to find out the probability that words in a string word occur together by multiplying the
# probability of the first word by the probability the second word occurs given the first word multiplied by the
# probability of the third word given the first word squared and continues this pattern to the nth word. However,
# this will create a very low probability if there are many words in a string because most words do not occur in the
# exact same lengthy order all the time. Therefore the Markov Assumption is employed, which assumes that the
# probability that the previous word is related to the word is roughly the same as the probability of all the words
# in a string being related.

# Explain how the Word2Vec approach uses feed-forward neural networks to generate word embeddings. What are the
# advantages of the Word2Vec representation over the Bag-of-Words representation?

# Word2Vec uses Continuous Bag of Words and Skip-Gram distributional architectures. The Continuous Bag of Words
# predicts what a word will be given the surrounding contextual words. This generates a score. The Skip-Gram
# architecture is given a word and attempts to predict the contextual words. This gives the model training data to
# use to become more accurate in generation. Some advantages of Word2Vec are that it does not look at all the data in
# a string at the same time but focuses on the relationships between a word and its contextual words. Therefore it is
# not reliant on frequency.

# Explain what patterns are learned in the multi-head attentions of a Transformer. What are the advantages of the
# Transformer embeddings over the Word2Vec embeddings?

# The multi-head attention module learns the relationship between words by performing matrix multiplication on n by d
# matrices where n is the vector of words and d is the number of dimensions. The multiplication and transformations
# use weights that the model determines itself during training. This calculates the attention score which is the
# weight between the ngrams. Each head of the transformer can learn different patterns such as local relationships
# between the following and preceding words to a word as well as global relationships between words far apart in the
# document or contextual patterns. It can also learn semantic meanings between words or the syntax. While Word2Vec
# gets the context of a few words surrounding the word, multi-head attention is much more accurate because it can
# process the relationship between each word and all the other words. This enables it to understand much more
# context, especially of a longer document, whereas Word2Vec would not be able to form those connections. Word2Vec is
# good at capturing local patterns but is not as good at capturing the rest of the patterns or a multiplicity of
# complex relationships.
