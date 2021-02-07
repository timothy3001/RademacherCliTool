from homepilot.homepilot_login import login_homepilot
from homepilot.homepilot_devices import get_devices, update_capability, boost_thermostat as b_thermostat
from homepilot.helpers import clean_base_url
from homepilot.models.device import Device
import json
import click

logged_in = False

def ensure_login(url, password):
    global logged_in
    if not logged_in:        
        logged_in = login_homepilot(url, password)
        if not logged_in:
            raise Exception('Something went wrong logging in!')


@click.group()
def main():
    pass


@main.command()
@click.option("--url", "-h", required=True, help="URL to homepilot")
@click.option("--password", "-p", help="Password to use to access homepilot")
def devices(url, password):
    url = clean_base_url(url)
    ensure_login(url, password)

    devices = get_devices(url)

    for device in devices:
        click.echo(f'ID: {device.device_id} Name: {device.name} Group: {device.device_group}')

@main.command()
@click.option("--url", "-h", required=True, help="URL to homepilot")
@click.option("--password", "-p", help="Password to use to access homepilot")
@click.option("--device-id", required=True)
@click.option("--off", is_flag=True)
def boostthermostat(url, password, device_id, off):
    url = clean_base_url(url)
    ensure_login(url, password)
    
    b_thermostat(url, device_id, not off)

@main.command()
@click.option("--url", "-h", required=True, help="URL to homepilot")
@click.option("--password", "-p", help="Password to use to access homepilot")
@click.option("--device-id", required=True)
@click.option("--capability", required=True, 
    help="Enter a JSON containing name and value. E.g. --capability='{\"name\":\"BOOST_ACTIVE_CFG\", \"value\": true'")
def updatecapability(url, password, device_id, capability):
    url = clean_base_url(url)
    ensure_login(url, password)

    json_capability = json.loads(capability)

    if not json_capability \
        or 'name' not in json_capability \
        or 'value' not in json_capability:
        raise Exception('Please make sure to supply a json with "name" and "value" field!')

    update_capability(url, device_id, json_capability['name'], json_capability['value'])


if __name__ == '__main__':
    main()
