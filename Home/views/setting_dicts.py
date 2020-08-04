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
            st['inputs']="NA"
            # remove keys from dict
            attrs = {}



        for k, v in attrs.items():

            # set the initial value and labels
            inp = dict(
                initial_value=v['value'],
                label=v['name']
            )

            # check the type
            tp=eval(v['type'])

            if tp== bool:
                inp['type'] = 'switch'

            elif tp== int or tp== float:
                inp['type'] = 'slider'
                inp['max'] = 100
                inp['min'] = 0

            elif tp== str:
                inp['type'] = "string"

            elif tp ==list:
                inp['type'] = "list"
                inp['options'] = v['options']

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
            max=100,
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
