

def make_drop_down(pattern_attributes):
    settings = []
    for pt, attrs in pattern_attributes.items():
        if len(attrs) == 0: continue

        st = dict(Name=pt, inputs=[])

        for k, v in attrs.items():
            inp = {}
            if isinstance(v, int):
                inp['type'] = 'slider'
                inp['max'] = 100
                inp['min'] = 0

            elif isinstance(v, str):
                inp['type'] = "string"

            elif isinstance(v, bool):
                inp['type'] = 'switch'

            inp['initial_value'] = v
            inp['label'] = k

            st['inputs'].append(inp)

        settings.append(st)
    return settings


random = True  # set values as per you want below if random
slider_values = {
    'delay': {
        'min': 0,
        'max': 100,
        'current': 23
    },
    'red': {
        'min': 0,
        'max': 255,
        'current': 23
    },
    'green': {
        'min': 0,
        'max': 255,
        'current': 23
    },
    'blue': {
        'min': 0,
        'max': 255,
        'current': 40

    },
    'alpha': {
        'min': 0,
        'max': 255,
        'current': 23
    },
}
