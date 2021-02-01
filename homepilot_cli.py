from homepilot.homepilot_login import login_homepilot
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
    ensure_login(url, password)


if __name__ == '__main__':
    main()
