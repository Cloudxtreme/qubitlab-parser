#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CircuitBuilder:

    def __init__(self):
        self.qbl_memory = None

    def set_qbl_memory(self, qbl_memory):
        self.qbl_memory = qbl_memory

    def get_circuit(self, circuit_name):
        circuit_qbl_data = self.get_circuit_qbl_data(circuit_name)
        circuit_structure = self.replace_variables_to_structures(circuit_qbl_data)
        circuit_object = self.get_circuit_object(circuit_structure)
        return circuit_object

    def get_circuit_qbl_data(self, circuit_name):
        return {}

    def replace_variables_to_structures(self, circuit_qbl_data):
        return {}

    def get_circuit_object(self, circuit_structure):
        return {}
