import os
import sys
import time


class Bot:
    def __init__(self):
        self.start_time = time.time()
        self.config = {}
        self.config_mtime = 0
        self.conns = {}

        # folder used to store database and logs
        self.persist_dir = os.path.abspath('persist')

    def ensure_files(self):
        if not os.path.exists(self.persist_dir):
            os.mkdir(self.persist_dir)

        if not os.path.exists('config'):
            print('ERROR: no config file found!')
            print("Please rename 'config.default' to 'config' to set up your bot!")
            sys.exit(1)
