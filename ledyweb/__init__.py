import logging
import pathlib

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s\n'
formatter = logging.Formatter(format)

logging.basicConfig(format=format)
wsgi_logger = logging.getLogger("wsgi_logger")

cur_dir = str(pathlib.Path(__file__).parent.absolute())
fileHandler = logging.FileHandler(f"{cur_dir}/log.log")
fileHandler.setFormatter(formatter)
wsgi_logger.addHandler(fileHandler)
wsgi_logger.setLevel(logging.DEBUG)
