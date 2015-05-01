#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 Synthesizing"""

import os
import pickle


class PickleCache(object):
    """Docstring
    Attributes = None
    """

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor Docstring
        Args:
        Returns:
        Examples:
        """
        self.__file_path = file_path
        self.__data = {}
        self.__file_object = None
        self.autosync = autosync
        self.load()

    def __len__(self):
        """Method Docstring
        Args:
        Returns:
        Examples:
        """
        return len(self.__data)

    def __setitem__(self, key, value):
        """Method Docstring
        Args:
        Returns:
        Examples:
        """
        try:
            self.__data[key] = value
            if self.autosync is True:
                self.flush()
        except LookupError:
            raise LookupError

    def __getitem__(self, key):
        """Method Docstring
        Args:
        Returns:
        Examples:
        """
        try:
            if self.__data[key]:
                return self.__data[key]

        except LookupError:
            raise KeyError

    def __delitem__(self, key):
        """Method Docstring
        Args:
        Returns:
        Examples:
        """
        if key in self.__data:
            del self.__data[key]

            if self.autosync is True:
                self.flush()

    def load(self):
        """Method Docstring
        Args:
        Returns:
        Examples:
        """
        current_file = self.__file_path

        if os.path.exists(current_file) and os.path.getsize(current_file) > 0:
            with open(current_file, 'rb') as openfile:
                self.__data = pickle.load(openfile)
                openfile.close()
        else:
            os.path.exists(current_file)
            with open(current_file, 'w') as writefile:
                pickle.dump(self.__data, writefile)
                writefile.close()

    def flush(self):
        """Method Docstring
        Args:
        Returns:
        Examples:
        """
        with open(self.__file_path, 'w') as flushfile:
            self.__file_object = flushfile
            pickle.dump(self.__data, self.__file_object)
        flushfile.close()
