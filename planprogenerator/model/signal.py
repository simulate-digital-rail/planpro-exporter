import random
import uuid
import string


class Signal(object):

    def __init__(self, edge, distance_edge, effective_direction, function, kind):
        self.signal_uuid = str(uuid.uuid4())
        self.trip = None
        self.edge = edge
        self.distance_edge = distance_edge
        self.effective_direction = effective_direction.lower()

        if function in Signal.get_supported_functions():
            self.function = function
        else:
            self.function = Signal.get_supported_functions()[0]

        if kind in Signal.get_supported_kinds():
            self.kind = kind
        else:
            self.kind = Signal.get_supported_kinds()[0]

        self.classification_number = "60"
        self.element_name = Signal.get_random_element_name()
        self.control_member_uuid = str(uuid.uuid4())

    def get_node_before(self):
        if self.effective_direction == "in":
            return self.edge.node_a
        return self.edge.node_b

    def get_node_after(self):
        if self.effective_direction == "in":
            return self.edge.node_b
        return self.edge.node_a

    def get_side_distance(self):
        if self.effective_direction == "in":
            return 3.950
        return -3.950

    def get_uuids(self):
        return [self.signal_uuid, self.control_member_uuid]

    used_element_names = set()

    @staticmethod
    def get_random_element_name():
        element_name = Signal.get_random_char() + Signal.get_random_char()
        while element_name in Signal.used_element_names:
            element_name = Signal.get_random_char() + Signal.get_random_char()
        Signal.used_element_names.add(element_name)
        return element_name

    @staticmethod
    def get_random_char():
        return random.choice(string.ascii_letters.upper())

    @staticmethod
    def get_supported_functions():
        return ["Einfahr_Signal", "Ausfahr_Signal", "Blocksignal", "andere"]

    @staticmethod
    def get_supported_kinds():
        return ["Hauptsignal", "Mehrabschnittssignal", "Vorsignal", "Sperrsignal", "Hauptsperrsignal", "andere"]
