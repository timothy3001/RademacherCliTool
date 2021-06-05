from typing import List

class Device:
    def __init__(self, json):
        capabilities_json = json['capabilities']
        self.capabilities: List[Capability] = []

        for capability_json in capabilities_json:
            self.capabilities.append(Capability(capability_json))


class Capability:
    def __init__(self, json):
        self.name = json['name']
        self.value = json['value'] if 'value' in json else None
        self.min_value = json['min_value'] if 'min_value' in json else None
        self.max_value = json['max_value'] if 'max_value' in json else None
        self.step_size = json['step_size'] if 'step_size' in json else None
        self.read_only = json['read_only'] if 'read_only' in json else None
        self.timestamp = json['timestamp'] if 'timestamp' in json else None
