import os
import subprocess

def run(backup_file):
    subprocess.run([
        'python',
        'e_istc/manage.py',
        'loaddata',
        backup_file
    ])

if __name__ == '__main__':
    # This script is intended to be run from a management command
    pass
