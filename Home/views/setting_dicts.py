def parse_additional_settings(pattern_attributes):
    """
    Create a dropdown menu from the attribute list in the firebase
    :param pattern_attributes: dictiornay as returned by the FireBaseConnector.init_attributes
    :return: str, structure to build the menu
    """
    settings = []
    for pt, attrs in pattern_attributes.items():

        st = dict(Name=pt, inputs=[])

        # empty value not shown
        if attrs == "NA":
            inp = dict(
                type="empty",
            )
            st['inputs'].append(inp)
            # remove keys from dict
            attrs = {}

        # check if there is a hidden property which is indicative of a multichoice
        if any(["__" in elem for elem in list(attrs.keys())]):
            # get both key and hidden one
            hidden_k = [elem for elem in list(attrs.keys()) if "_" in elem][0]
            k = hidden_k.strip("__")
            # add inputs
            inp = dict(
                type="list",
                initial_value=attrs[k],
                label=k,
                options=attrs[hidden_k]
            )
            st['inputs'].append(inp)
            # remove keys from dict
            attrs.pop(k)
            attrs.pop(hidden_k)

        for k, v in attrs.items():
            inp = {}

            if isinstance(v, bool):
                inp['type'] = 'switch'

            elif isinstance(v, int):
                inp['type'] = 'slider'
                inp['max'] = 100
                inp['min'] = 0

            elif isinstance(v, str):
                inp['type'] = "string"

            inp['initial_value'] = v
            inp['label'] = k

            st['inputs'].append(inp)

        settings.append(st)
    return settings


def parse_settings(local_db):
    """
    Define the standard setting dictionary
    :param fbc: FireBaseConnector
    :return: dict
    """
    # get required values
    rate = local_db['rate']
    random_colors = local_db['RGBA']['random']
    cur_pattern = local_db['cur_pattern']
    rgba = local_db['RGBA']

    # build settings
    settings = dict(
        cur_pattern=cur_pattern,
        rate=dict(
            min=0,
            max=250,
            current=rate,
        ),
        random_colors=random_colors,
        red=dict(
            min=0,
            max=255,
            current=rgba['r'],
        ),
        green=dict(
            min=0,
            max=255,
            current=rgba['g'],
        ),
        blue=dict(
            min=0,
            max=255,
            current=rgba['b'],
        ),
        alpha=dict(
            min=0,
            max=255,
            current=rgba['a'],
        ),
    )
    return settings
