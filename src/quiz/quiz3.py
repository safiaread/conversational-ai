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
                    '[#ONT(musical)]': {
                        '`Do you think Ryan Reynolds discovered jazz?`': {
                            'error': {
                                '`I\'m just joking! What do you look for in dramatic movies?`': {
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
                    '[#ONT(action)]': {
                        '`Do you know a lot about African history?`': {
                            'error': {
                                '`I want to take a course so I can learn more. What do you look for in dramatic '
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
                    '[#ONT(musical)]': {
                        '`Do you think Ryan Reynolds discovered jazz?`': {
                            'error': {
                                '`I\'m just joking! What do you look for in dramatic movies?`': {
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
                    '[#ONT(action)]': {
                        '`Do you know a lot about African history?`': {
                            'error': {
                                '`I want to take a course so I can learn more. What do you look for in dramatic '
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
                    'error': {
                        '`Sorry I haven\'t heard of that movie.`': 'end'
                    }
                }
            },
            'error': {
                '`Sorry I don\'t know who that is.`': 'end'
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
