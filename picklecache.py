#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PickleCache Module, Reads and Writes to files, and autosyncs."""

import os
import pickle


class PickleCache(object):
    """Docstring
    Attributes = None
    """

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """PickleCache Constructor Docstring
        Args:
            __file_path  = Placeholder for file_path
            __data (dict) = Placeholder for data.
            __file_object (None) = Placeholder for data in major changes.
            autosync (bool) (Default = False) = Autosync

        Returns:
            None
        Examples:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.__data = {}
        self.__file_object = None
        self.autosync = autosync
        self.load()

    def __len__(self):
        """Length of pseudo-attritute data dictionary.
        Args:
            __data (dict) = pseudo-attribute dictionary data

        Returns:
            self.__data (int) = Length object.
        """
        return len(self.__data)

    def __setitem__(self, key, value):
        """Sets key and value in dictionary.
        Args:
            key = key in dict.
            value = value in dict.

        Returns:
            None
            raise LookupError

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """
        try:
            self.__data[key] = value
            if self.autosync is True:
                self.flush()
        except LookupError:
            raise LookupError

    def __getitem__(self, key):
        """Returns Value if key in dictionary.
        Args:
            key = key in dict.

        Returns:
            value = value in dict if True.
            raise KeyError if False.

        Examples:
             >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        try:
            if self.__data[key]:
                return self.__data[key]

        except LookupError:
            raise KeyError

    def __delitem__(self, key):
        """Deletes key  and value in dictionary.
        Args:
            key = key in dictionary.

        Returns:
            None

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """
        if key in self.__data:
            del self.__data[key]

            if self.autosync is True:
                self.flush()

    def load(self):
        """Loads Data and reads and writes data in file.
        Args:
            current_file = Placeholder for __file_path.

        Returns:
            None

        Examples:
            >>> import pickle
            >>> fh = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'bar'
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
        """Save stored data to file.
        Args:
            flushfile = Placeholder for filepath and open to write.

        Returns:
            None

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """
        with open(self.__file_path, 'w') as flushfile:
            self.__file_object = flushfile
            pickle.dump(self.__data, self.__file_object)
        flushfile.close()
