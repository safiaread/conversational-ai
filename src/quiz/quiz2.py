from emora_stdm import DialogueFlow
def hair_salon() -> DialogueFlow:
    transitions = {
        'state': 'start',
        '`Hello, how can I help you?`': {
            '[{haircut, hair cut, cut, trim, buzz, trimmed, buzzed, bangs, fade, faded, buzz cut, buzzcut}]': {
                '`Sure. What date and time are you looking for?`': {
                    '{[{monday, tuesday, mon, tues}, 2, pm],[{monday,mon} {10,11}, am],[{monday,mon} 1, pm]}': {
                        '`You\'re appointment is set. See you!`': 'end'
                    },
                    'error': {
                        '`Sorry, that slot is not available for a haircut.`': {
                            'error': {
                                '`Goodbye`': 'end'
                            }
                        }
                    }
                }
            },
            '[{haircoloring, hair coloring, dye, hair dyed, dyed, bleach, bleached, bleaching, balayage, highlights}]': {
                '`Sure. What date and time are you looking for?`': {
                    '{[{wednesday, thursday, wed, weds, thur, thurs}, {10,11}, am],[wed, weds, wednesday, 1, pm]}': {
                        '`You\'re appointment is set. See you!`': 'end'
                    },
                    'error': {
                        '`Sorry, that slot is not available for a haircut.`': {
                            'error': {
                                '`Goodbye`': 'end'
                            }
                        }
                    }
                }
            },
            '[{perm, permed}]': {
                '`Sure. What date and time are you looking for?`': {
                    '{[{friday, saturday, fri, sat}, 2, pm], [{friday, saturday, fri, sat}, 10, am], [{friday, fri}, 11,am], [{friday, fri}, 1, pm]}': {
                        '`You\'re appointment is set. See you!`': 'end'
                    },
                    'error': {
                        '`Sorry, that slot is not available for a perm. The times we have available are Friday at '
                        '10 AM, 11 AM, 1 PM, and 2 PM or Saturday at 10 AM and 2 PM.`': {
                            '{[{friday, saturday, fri, sat}, 2, pm], [{friday, saturday, fri, sat}, 10, am], [{friday, fri}, 11,am], [{friday, fri}, 1, pm]}': {  # FIX
                                '`You\'re appointment is set. See you!`': 'end'
                            },
                            'error': {
                                '`Ok, have a good day.`': 'end'
                            }
                        }
                    }
                }
            },
            'error': {
                '`Sorry, we do not provide that service.`': {
                    'error': {
                        '`Goodbye.`': 'end'
                    }
                }
            }
        }
    }

    df = DialogueFlow('start', end_state='end')
    df.load_transitions(transitions)
    return df


if __name__ == '__main__':
    hair_salon().run()


