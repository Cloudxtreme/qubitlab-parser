#!/usr/bin/env python
# -*- coding: utf-8 -*-


class QblMemory:

    def __init__(self):
        self.qbl_objects = {
            'gates': {},
            'circuits': {},
            'states': {}
        }

        self.qbl_tmb_objects = {
            'gates': {},
            'circuits': {},
            'states': {}
        }

    def add_new_object(self, object_name, object_type, object_data):
        pass

    def commit_new_objects(self):
        pass

    def revert_new_objects(self):
        pass

    def remove_object(self, object_name):
        pass

    def remove_all(self):
        pass
