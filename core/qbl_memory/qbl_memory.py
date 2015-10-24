#!/usr/bin/env python
# -*- coding: utf-8 -*-


class QblMemory:

    def __init__(self):
        self.qbl_objects = {}

    def add_new_data(self, qbl_memory_data):
        for key, value in qbl_memory_data.iteritems():
            self.qbl_objects[key] = value

    def remove_object(self, key):
        if key in self.qbl_objects:
            del self.qbl_objects[key]
            return True
        else:
            return False

    def remove_all(self):
        self.qbl_objects = {}
