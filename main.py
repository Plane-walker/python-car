import os
from scape.command import run_with_command


if __name__ == '__main__':
    os.environ.setdefault('SCAPE_SETTINGS', 'conf.settings')
    run_with_command()
