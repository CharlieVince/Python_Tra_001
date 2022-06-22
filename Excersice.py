#!/usr/bin/env python3
# -*- coding: utg-8 -*-

__author__ = "Carlos Vicente"
__credits__ = ["Carlos Vicente"]
__Lisence__ = "BSD"
__maintainer__ = "Carlos Vicente"
__email__ = "carlos.quevedo.1994@gmail.com"
__status__ = "Development"
__version__ = "0.0.1"

# Default python packages
import logging
import os
import time

# pip installed python packages
from pynput.keyboard import Key, Controller


# imports from other files
from .my_file import OtherClass


class WorkLogin:
    """Class that performs functions for logging"""

    def __init__(self, conf_path=os.path.join(os.path.expanduser("~"),".work_login.conf")):
        """Saves config file location"""
        self.conf_path = conf_path
        self.keyboard = Controller()

    def login(self):
        """Logs user in through terminal"""

        # Configures config file if not done so already
        if not os.path.exists(self.conf_path):
            self.configure()
        # Opens a terminal
        os.system("gnome-terminal")
        time.sleep(1)
        with open(self.conf_path, "r") as f:
            for cmd in f:
                self._run_cmd(cmd)
    
    def configure(self):
        """Configures file that will contain commands to run"""

        logging.info("Configuring work login")
        cmds = [input("Next command, or hit enter:\n")]
        # Ugh needs 3.6 compatibility, but with 3.8 could use walrus here

        while cmds[-1] != "":
            cmds.append(input("Next command, or hit enter:\n"))