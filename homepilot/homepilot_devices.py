from homepilot.models.device import Device
from homepilot.helpers import SessionHelper, raise_http_exception
from homepilot.models.deviceV4 import DeviceV4
import click
import json
from typing import List

SUBADDRESS_DEVICES_V4 = '/v4/devices'
SUBADDRESS_DEVICES = '/devices/'

def get_devices(url) -> List[DeviceV4]:
    actuators = get_devices_devtype(url, 'Actuator', 'devices')
    sensors = get_devices_devtype(url, 'Sensor', 'meters')
    transmitters = get_devices_devtype(url, 'Transmitter', 'transmitters')
    cameras = get_devices_devtype(url, 'Camera', 'cameras')

    devices = []
    devices.extend(actuators)
    devices.extend(sensors)
    devices.extend(transmitters)
    devices.extend(cameras)

    return devices

def get_devices_devtype(url: str, devtype: str, json_sub_obj_name: str):
    result_list = []
    s = SessionHelper.current()
    path = url + SUBADDRESS_DEVICES_V4 + "?devtype=" + devtype

    res = s.get(path)

    if res.ok:
        devices_json = res.json()

        for device_json in devices_json[json_sub_obj_name]:
            result_list.append(DeviceV4(json=device_json))

    else:
        raise_http_exception('get_devices', res)
    
    return result_list
        
def boost_thermostat(url: str, device_id: int, on: bool):
    update_capability(url, device_id, 'BOOST_ACTIVE_CFG', on)

def update_capability(url: str, device_id: int, cap_name: str, cap_value: any):
    s = SessionHelper.current()
    path = url + SUBADDRESS_DEVICES + device_id

    json_data = {
        'name': cap_name,
        'value': cap_value
    }

    res = s.put(path, json=json_data)

    if not res.ok:
        raise_http_exception('update_capability', res)

def get_device(url: str, device_id: int):
    s = SessionHelper.current()
    path = url + SUBADDRESS_DEVICES + device_id

    res = s.get(path)

    if not res.ok:
        raise_http_exception('get_capabilities', res)
    
    device_raw = res.json()
    device = Device(device_raw['payload']['device'])

    return device

