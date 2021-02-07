class DeviceV4:
    def _determine_device_group(self, device_group_id: int) -> str:
        if device_group_id == DeviceGroupsEnum.SWITCHES:
            return "SWITCHES"
        elif device_group_id == DeviceGroupsEnum.BLINDS:
            return "BLINDS"
        elif device_group_id == DeviceGroupsEnum.DIMMERS:
            return "DIMMERS"
        elif device_group_id == DeviceGroupsEnum.THERMOS:
            return "THERMOS"
        elif device_group_id == DeviceGroupsEnum.DOORS:
            return "DOORS"
        elif device_group_id == DeviceGroupsEnum.HUE_WHITE:
            return "HUE_WHITE"
        elif device_group_id == DeviceGroupsEnum.HUE_WHITE_AMBIENCE:
            return "HUE_WHITE_AMBIENCE"
        elif device_group_id == DeviceGroupsEnum.SENSORS:
            return "SENSORS"
        elif device_group_id == DeviceGroupsEnum.CAMERAS:
            return "CAMERAS"
        elif device_group_id == DeviceGroupsEnum.REMOTE_CONTROLS:
            return "REMOTE_CONTROLS"
        return ""

    def __init__(self, json):
        self.device_id: int = json['did']        
        self.name: str = json['name']
        self.device_group_id = json['deviceGroup']
        self.device_group = self._determine_device_group(self.device_group_id)


class DeviceGroupsEnum:
    # Actuators 
    SWITCHES = 1
    BLINDS = 2
    DIMMERS = 4
    THERMOS = 5
    DOORS = 8
    HUE_WHITE = 81
    HUE_WHITE_AMBIENCE = 82
    HUE_COLOR_AMBIENCE = 83
    
    # Others
    SENSORS = 3
    CAMERAS = 9
    REMOTE_CONTROLS = 10