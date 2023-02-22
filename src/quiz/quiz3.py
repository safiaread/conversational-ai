import re
from typing import Dict, Any, List

from emora_stdm import DialogueFlow, Macro, Ngrams


def movies() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hi there, let\'s talk about movies. What\'s the name of your favorite actor?`': {
            '#ACTOR': {
                '#IF($TITLE) $NAME `is a prestigious actor! Speaking of great things, '
                'what\'s the latest movie you saw?`': {
                    '[#ONT(korean)]': {
                        '`Do you need subtitles to read Korean?`': {
                            'error': {
                                '`Unfortunately I can only read English. What do you look for in dramatic '
                                'movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful '
                                        'personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(musical)]': {
                        '`Do you think musicals are better than regular movies?`': {
                            'error': {
                                '`I like both. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(oldmovies)]': {
                        '`Do you prefer black and white movies to those in color?`': {
                            'error': {
                                '`I think black and white has charm. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(historical)]': {
                        '`Are you a history buff?`': {
                            'error': {
                                '`I failed history in high school. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(sports)]': {
                        '`What\'s your favorite sport?`': {
                            'error': {
                                '`I like tennis the most. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(cameron)]': {
                        '`What do you think about James Cameron`': {
                            'error': {
                                '`I literally don\'t have an opinion of him. How important are special effects in sci-fi movies?`': {
                                    'error': {
                                        '`I think cgi can feel a little fake sometimes, they don\'t have practical effect\'s charms.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(starwars)]': {
                        '`Are you a C3PO or RD-D2 stan?`': {
                            'error': {
                                '`RD-D2 has always had my heart. How important are special effects in sci-fi movies?`': {
                                    'error': {
                                        '`I think cgi can feel a little fake sometimes, they don\'t have practical effect\'s charms.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(christmas)]': {
                        '`Do you like Christmas?`': {
                            'error': {
                                '`My favorite thing about Christmas is mistletoe. Are you a romantic?`': {
                                    'error': {
                                        '`They say there\'s someone for everyone.`': {
                                            'error': {
                                                '`Yeah. Thanks for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(shakespeare)]': {
                        '`What\'s your favorite Shakespeare play?`': {
                            'error': {
                                '`Shakespeare writes iconic couples. Are you a romantic?`': {
                                    'error': {
                                        '`They say there\'s someone for everyone.`': {
                                            'error': {
                                                '`Yeah. Thanks for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(disney)]': {
                        '`Which disney princess are you most like?`': {
                            'error': {
                                '`I think I\'m a Mulan. Do you generally like animated films?`': {
                                    'error': {
                                        '`I think animation is a super creative medium.`': {
                                            'error': {
                                                '`Yeah, totally. Thanks for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(dreamworks)]': {
                        '`Where do you think Puss in Boots got his boots from?`': {
                            'error': {
                                '`I don\'t know. Maybe some things are best left a mystery! Do you generally like '
                                'animated films?`': {
                                    'error': {
                                        '`I think animation is a super creative medium.`': {
                                            'error': {
                                                '`Yeah, totally. Thanks for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(tolkien)]': {
                        '`Frodo or Bilbo?`': {
                            'error': {
                                '`I wish I could be a hobbit. Do generally like fantasy movies?`': {
                                    'error': {
                                        '`Fantasy worlds are a nice escape from the real world.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(marvel)]': {
                        '`Which Avenger\'s superpower would you want most?`': {
                            'error': {
                                '`I would want to be able to fly. Do you think action movies are more exciting because of the fight sequences?`': {
                                    'error': {
                                        '`I think that fight choreography is an impressive profession.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(oscar)]': {
                        '`Did you know that movie won an oscar?`': {
                            'error': {
                                '`Awards don\'t always mean movies are good, but its a nice indicator. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(shyamalan)]': {
                        '`Are you a fan of a Shyamalan twist?`': {
                            'error': {
                                '`Sixth Sense really got me!. Is horror your favorite genre?`': {
                                    'error': {
                                        '`I\'m a scaredy-cat.`': {
                                            'error': {
                                                '`That\'s cool. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(doll)]': {
                        '`Are you scared of haunted dolls?`': {
                            'error': {
                                '`They terrify me. Is horror your favorite genre?`': {
                                    'error': {
                                        '`I\'m a scaredy-cat.`': {
                                            'error': {
                                                '`That\'s cool. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(hitchcock)]': {
                        '`do you like the style of hitchcock movies?`': {
                            'error': {
                                '`They terrify me. Is mystery your favorite genre?`': {
                                    'error': {
                                        '`I like to try to figure out who the murderer is`': {
                                            'error': {
                                                '`That\'s cool. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'error': {
                        '`Sorry I haven\'t heard of that movie.`': 'end'
                    }
                },
                '$NAME `is a great actor, I agree. Speaking of great things, what\'s the latest movie '
                'you saw?`': {
                    '[#ONT(korean)]': {
                        '`Do you need subtitles to read Korean?`': {
                            'error': {
                                '`Unfortunately I can only read English. What do you look for in dramatic '
                                'movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful '
                                        'personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(musical)]': {
                        '`Do you think musicals are better than regular movies?`': {
                            'error': {
                                '`I like both. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(oldmovies)]': {
                        '`Do you prefer black and white movies to those in color?`': {
                            'error': {
                                '`I think black and white has charm. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(historical)]': {
                        '`Are you a history buff?`': {
                            'error': {
                                '`I failed history in high school. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(sports)]': {
                        '`What\'s your favorite sport?`': {
                            'error': {
                                '`I like tennis the most. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(cameron)]': {
                        '`What do you think about James Cameron`': {
                            'error': {
                                '`I literally don\'t have an opinion of him. How important are special effects in sci-fi movies?`': {
                                    'error': {
                                        '`I think cgi can feel a little fake sometimes, they don\'t have practical effect\'s charms.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(starwars)]': {
                        '`Are you a C3PO or RD-D2 stan?`': {
                            'error': {
                                '`RD-D2 has always had my heart. How important are special effects in sci-fi movies?`': {
                                    'error': {
                                        '`I think cgi can feel a little fake sometimes, they don\'t have practical effect\'s charms.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(christmas)]': {
                        '`Do you like Christmas?`': {
                            'error': {
                                '`My favorite thing about Christmas is mistletoe. Are you a romantic?`': {
                                    'error': {
                                        '`They say there\'s someone for everyone.`': {
                                            'error': {
                                                '`Yeah. Thanks for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(shakespeare)]': {
                        '`What\'s your favorite Shakespeare play?`': {
                            'error': {
                                '`Shakespeare writes iconic couples. Are you a romantic?`': {
                                    'error': {
                                        '`They say there\'s someone for everyone.`': {
                                            'error': {
                                                '`Yeah. Thanks for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(disney)]': {
                        '`Which disney princess are you most like?`': {
                            'error': {
                                '`I think I\'m a Mulan. Do you generally like animated films?`': {
                                    'error': {
                                        '`I think animation is a super creative medium.`': {
                                            'error': {
                                                '`Yeah, totally. Thanks for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(dreamworks)]': {
                        '`Where do you think Puss in Boots got his boots from?`': {
                            'error': {
                                '`I don\'t know. Maybe some things are best left a mystery! Do you generally like '
                                'animated films?`': {
                                    'error': {
                                        '`I think animation is a super creative medium.`': {
                                            'error': {
                                                '`Yeah, totally. Thanks for chatting with me!`': 'end'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(tolkien)]': {
                        '`Frodo or Bilbo?`': {
                            'error': {
                                '`I wish I could be a hobbit. Do generally like fantasy movies?`': {
                                    'error': {
                                        '`Fantasy worlds are a nice escape from the real world.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(marvel)]': {
                        '`Which Avenger\'s superpower would you want most?`': {
                            'error': {
                                '`I would want to be able to fly. Do you think action movies are more exciting because of the fight sequences?`': {
                                    'error': {
                                        '`I think that fight choreography is an impressive profession.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(oscar)]': {
                        '`Did you know that movie won an oscar?`': {
                            'error': {
                                '`Awards don\'t always mean movies are good, but its a nice indicator. What do you look for in dramatic movies?`': {
                                    'error': {
                                        '`I think the cinematography in dramatic movies can be super suspenseful personally.`': {
                                            'error': {
                                                '`That\'s a good point. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(shyamalan)]': {
                        '`Are you a fan of a Shyamalan twist?`': {
                            'error': {
                                '`Sixth Sense really got me!. Is horror your favorite genre?`': {
                                    'error': {
                                        '`I\'m a scaredy-cat.`': {
                                            'error': {
                                                '`That\'s cool. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(doll)]': {
                        '`Are you scared of haunted dolls?`': {
                            'error': {
                                '`They terrify me. Is horror your favorite genre?`': {
                                    'error': {
                                        '`I\'m a scaredy-cat.`': {
                                            'error': {
                                                '`That\'s cool. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '[#ONT(hitchcock)]': {
                        '`do you like the style of hitchcock movies?`': {
                            'error': {
                                '`They terrify me. Is mystery your favorite genre?`': {
                                    'error': {
                                        '`I like to try to figure out who the murderer is`': {
                                            'error': {
                                                '`That\'s cool. Thank\'s for chatting with me!`': 'end'

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'error': {
                        '`Sorry I haven\'t heard of that movie.`': 'end'
                    }
                }
            },
            'error': {
                '`Sorry I don\'t know that movie': 'end'
            }
        }
    }

    macros = {
        'ACTOR': MacroActorName()
    }

    df = DialogueFlow('start', end_state='end')
    df.knowledge_base().load_json_file(
        '/Users/safiaread/Pycharmprojects/conversational-ai/resources/ontology_quiz3.json')
    df.load_transitions(transitions)
    df.add_macros(macros)
    return df


class MacroActorName(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        r = re.compile(r'([Ss]ir|[Dd]ame)?(?:\s+)?([A-z]+(?:\s+)?[A-z]+)')
        m = r.search(ngrams.text())
        if m is None: return False

        title, name = None, None

        if m.group(1):
            title = True
            name = m.group(2)
        else:
            name = m.group(2)

        vars['TITLE'] = title
        vars['NAME'] = name

        return True


if __name__ == '__main__':
    movies().run()
