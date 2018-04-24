#!/usr/bin/env python3

from shutil import *
from logging import info as linfo
import logging
from pathlib import Path

class Settings:
    def initialize(self):
        self.GLOBAL_GITIGNORE_FILE_NAME = ".gitignore"
        self.GLOBAL_GITIGNORE_DESTINATION_PATH = str(Path.home()) + "/"
        self.VIMRC_FILE_NAME = ".vimrc"
        self.VIMRC_DESTINATION_PATH = str(Path.home()) + "/"
        self.VIMRC_LOCAL_FILE_NAME = ".vimrc_local"
        self.VIMRC_LOCAL_DESTINATION_PATH = str(Path.home()) + "/"
        self.LEMONSQUANCH_INCLUDE_FILE_NAME = ".lemonsquanch.include"
        self.LEMONSQUANCH_INCLUDE_DESTINATION_PATH = str(Path.home()) + "/"

def copyIfNotExists(fn, destination):
    if not Path(destination + fn).is_file():
        copy(fn, destination + fn)


def copyConfigurationFiles(s):
    linfo("\tCopying configuration files.")
    copyIfNotExists(s.GLOBAL_GITIGNORE_FILE_NAME, s.GLOBAL_GITIGNORE_DESTINATION_PATH)
    copyIfNotExists(s.VIMRC_FILE_NAME, s.VIMRC_DESTINATION_PATH)
    copyIfNotExists(s.VIMRC_LOCAL_FILE_NAME, s.VIMRC_LOCAL_DESTINATION_PATH)
    copyIfNotExists(s.LEMONSQUANCH_INCLUDE_FILE_NAME, s.LEMONSQUANCH_INCLUDE_DESTINATION_PATH)
    linfo("\tConfig copy finished!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    linfo("Starting configuration script.")

    s = Settings()
    s.initialize()
    copyConfigurationFiles(s)

    linfo("Finished configuration script, exiting!")
