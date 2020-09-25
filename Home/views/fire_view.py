import logging
import os
import pathlib

from Home.views.setting_dicts import parse_settings, parse_additional_settings
from firebase.connector import FireBaseConnector

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s\n'
formatter = logging.Formatter(format)

logging.basicConfig(format=format)
fire_view_logger = logging.getLogger("fire_view_logger")

cur_dir = str(pathlib.Path(__file__).parent.absolute())
fileHandler = logging.FileHandler(f"{cur_dir}/log.log")
fileHandler.setFormatter(formatter)
fire_view_logger.addHandler(fileHandler)
fire_view_logger.setLevel(logging.DEBUG)


class Singleton(type):
    _instances = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]


class FireView(metaclass=Singleton):

    def __init__(self):
        self.fbc = None

    def tracker(self):
        self.update_settings()
        print("updated")
        # todo: add call to renderer

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

        fire_view_logger.debug("Settign dict updated")

    def init_firebase(self, options):
        """
        Init the firebase class, update the render settings and start the firebase
        :param options: dict, dict containing options from the arg parser
        :return:
        """

        if options['debug']:
            fire_view_logger.setLevel(logging.DEBUG)

        fire_view_logger.debug(f"init_firebase called with options:\n{options}")

        self.fbc = FireBaseConnector(credential_path=options['credential_path'], database_url=options['databaseURL'],
                                     debug=options['debug'], tracker=self.tracker)

        # update env settings for render
        self.update_settings()
        # start firebase
        self.fbc.start()
        fire_view_logger.debug("FireBaseConnector Started")

    def process_request(self, request):
        values = request.GET.dict()
        self.fbc.update_db(values)
        self.update_settings()


FV = FireView()
