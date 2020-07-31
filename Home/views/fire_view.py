import os

from Home.views.setting_dicts import parse_settings, parse_additional_settings
from firebase.connector import FireBaseConnector


class Singleton(type):
    _instances = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]


class FireView(metaclass=Singleton):

    def __init__(self):
        self.fbc = None

    def update_settings(self):
        """
        Update the settings for the rendering based on the local copy of the database in the fbc class
        :return:
        """
        # get the local db
        pattern_attributes = self.fbc.local_db['pattern_attributes']

        # parse them
        settings = parse_settings(self.fbc.local_db)
        additional_settings = parse_additional_settings(pattern_attributes)

        # update env functions
        os.environ['ADDITIONAL_SETTINGS'] = str(additional_settings)
        os.environ['SETTINGS'] = str(settings)

    def init_firebase(self, options):
        """
        Init the firebase class, update the render settings and start the firebase
        :param options: dict, dict containing options from the arg parser
        :return:
        """
        self.fbc = FireBaseConnector(credential_path=options['credential_path'], database_url=options['databaseURL'],
                                     debug=options['debug'])
        # update env settings for render
        self.update_settings()
        # start firebase
        self.fbc.start()

    def process_request(self, request):
        values = request.GET.dict()
        print(f"Values recived : {values}")
        self.fbc.check_diff(values)
        self.update_settings()


FV = FireView()
