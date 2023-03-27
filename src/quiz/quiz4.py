import random
import re
import time
import pickle
import pandas as pd
from typing import Dict, Any, List

from emora_stdm import DialogueFlow, Macro, Ngrams


class MacroTime(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[str]):
        current_time = time.strftime("%H")
        greet = str()
        if int(current_time) <= 12:
            if int(current_time) <= 5:
                greet = "Gosh it's early in the morning"
            else:
                greet = "Good Morning"
        if int(current_time) <= 17:
            if int(current_time) > 12:
                greet = "Good Afternoon"
        if int(current_time) <= 21:
            if int(current_time) > 17:
                greet = "Good Evening"
        else:
            greet = "Good Night"

        return greet


def recommender() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '#GATE `Hi, what\'s your name?`': 'name',
        '#GATE `Hi, what should I call you?`': 'name',
        '#GATE `Hi, how should I refer to you?`': 'name',
        '#GATE `Hi, what would you like to be called?`': 'name',
        '#GATE `Hi, what are you usually called?`': 'name',
        '#GATE `Hi, what do you go by?`': 'name',
        '#GATE `Hi, who are you?`': 'name',
        '#GATE `Hi, what\'s the best thing to call you?`': 'name',
        '#GATE `Hi, your name please?`': 'name',
        '`Hey, give me your name! (Please)`': {
            'state': 'name',
            'score': 0.1
        }
    }

    transitions_name = {
        'state': 'name',
        '#TIME `by the way!`': {
            '#NAME #VISITS': {
                '#IF($NEW) `Nice to meet you` $NAME `! What would you like a '
                'recommendation for?`': {
                    'state': 'ask',
                    '[{#LEM(movie), film}]': 'movie',
                    '[{#LEM(music), #LEM(song)}]': 'music',
                    '[{no, not}]': {
                        '`Oh, okay. I hope you have a good day!`': 'end'
                    },
                    'error': {
                        '`Sorry I don\'t know enough about that topic to give recommendations.`': 'end'
                    }
                },
                '`Fancy seeing you again` $NAME`. Did you like` $REC`?`': {
                    'score': 0.1,
                    '[{yes, yeah, sure, uh huh, best, good, great, amazing}]': {
                        '`I\'m glad that you liked it! What else would you like a recommendation for?`': 'ask'
                    },
                    '[{no, suck, sucked, bad, worst}]': {
                        '`I\'m sorry about that! Could you give me another shot? What would you like a recommendation '
                        'for?`': 'ask'
                    },
                    '[{fine, alright, okay, mid, ambivalent, maybe}]': {
                        '`I bet I can do better! Would you like a movie or song rec?`': 'ask'
                    },
                    'error': {
                        '`Alright. Would you like another movie or song recommendation?`'
                    }
                }
            },
            'error': {
                '`Sorry I\'m such an airhead! Can you chat again later?`': 'end'
            }
        }
    }

    transitions_movie = {
        'state': 'movie',
        '`You should watch` #MOVIES': {
            '[{about, info, information, description}]': {
                'Let me google that real quick. $REC `is described by IMDB as:` $REC_INFO': {
                    'error': {
                        '`I hope you end up watching` $REC`!`': 'end'
                    }
                }
            },
            '[{genre, type}]': {
                '$REC `is a ` $REC_GENRE `movie.`': {
                    'error': {
                        '`I hope you end up watching` $REC`!`': 'end'
                    }
                }
            },
            '[{again, another, seen, saw, already, watched}]':  {
                '`Song or Movie?`': {
                    '[{#LEM(movie), film}]': 'movie',
                    '[{#LEM(music), #LEM(song)}]': 'music'
                }
            },
            '[{okay, ok, will do, sure, thanks}]': {
                '`I hope you have fun! Bye!': 'end'
            },
            'error': {
                'Alright then, see you later!': 'end'
            }
        }
    }
    transitions_music = {
        'state': 'music',
        '`You should listen to ` #MUSIC': {
            '[{about, by, artist, info, information}]': {
                '$REC `is an amazing song by` $REC_INFO': {
                    'error': {
                        '`Take a listen, I\'m sure you\'ll enjoy it!`': 'end'
                    }
                }
            },
            '[{cool, okay, ok, thanks, great, amazing, thanks, thx}]': {
                '`I\'m glad I could help!`': 'end'
            },
            '[{again, another, heard, listened, already, played}]': {
                '`Would you like another song or movie recommendation?`': {
                    '[{#LEM(movie), film}]': 'movie',
                    '[{#LEM(music), #LEM(song)}]': 'music'
                }
            },
            'error': {
                '`Alright then, see you soon!`': 'end'
            }
        }
    }

    macros = {
        'NAME': MacroGetName(),
        'TIME': MacroTime(),
        'VISITS': MacroVisits(),
        'MOVIES': MacroMovies(),
        "MUSIC": MacroMusic()
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    df.load_transitions(transitions_name)
    df.load_transitions(transitions_movie)
    df.load_transitions(transitions_music)
    df.add_macros(macros)
    return df


class MacroGetName(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        r = re.compile(
            r'(?:[a|b][m|e][\s][c][a][l][l][e][d])(?:\s)([a-z]+)|(?:[b][y])(?:\s)([a-z]+)|(?:[a][s])(?:\s)([a-z]+)|(?:[m][e])(?:\s)([a-z]+)|(?:[i][s])(?:\s)([a-z]+)|(?:[a][m])(?:\s)([a-z]+)|^([a-z]+)$|^([a-z]+)(?:\s)(?:[a-z]+)$')
        m = r.search(ngrams.text())
        if m is None: return False
        if m.group(8):
            name = m.group(8)
        if m.group(7):
            name = m.group(7)
        if m.group(6):
            name = m.group(6)
        if m.group(5):
            name = m.group(5)
        if m.group(4):
            name = m.group(4)
        if m.group(3):
            name = m.group(3)
        if m.group(2):
            name = m.group(2)
        if m.group(1):
            name = m.group(1)
        vars['NAME'] = name
        return True


class MacroVisits(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        vn = 'VISITS'
        if vn not in vars:
            vars[vn] = 1
            vars['NEW'] = True
        else:
            count = vars[vn] + 1
            vars[vn] = count
            vars['NEW'] = False


class MacroMovies(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        movies = pd.read_csv('/Users/safiaread/Pycharmprojects/conversational-ai/resources/IMDB.csv')
        movie = movies.iloc[random.randint(0, 1000)]
        movierec = movie["Title"][4:]
        vars['REC'] = movierec
        vars['REC_INFO'] = movie["Description"]
        vars['REC_GENRE'] = movie["Genre"]
        return movierec


class MacroMusic(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        songs = pd.read_csv('/Users/safiaread/Pycharmprojects/conversational-ai/resources/song1000.csv')
        song = songs.iloc[random.randint(0, 1000)]
        songrec = song["song"]
        vars['REC'] = songrec
        vars['REC_INFO'] = song["artist"]
        return songrec


def save(df: DialogueFlow, varfile: str):
    df.run()
    d = {k: v for k, v in df.vars().items() if not k.startswith('_')}
    pickle.dump(d, open(varfile, 'wb'))


def load(df: DialogueFlow, varfile: str):
    d = pickle.load(open(varfile, 'rb'))
    df.vars().update(d)
    df.run()
    save(df, varfile)


if __name__ == '__main__':
    save(recommender(), '/Users/safiaread/Pycharmprojects/conversational-ai/resources/recommender.pkl')
    load(recommender(), '/Users/safiaread/Pycharmprojects/conversational-ai/resources/recommender.pkl')
