import os
import subprocess
from datetime import datetime

def run():
    backup_dir = 'backups'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(backup_dir, f'backup_{timestamp}.json')

    subprocess.run([
        'python',
        'e_istc/manage.py',
        'dumpdata',
        '--exclude=contenttypes',
        '--exclude=auth.Permission',
        '--indent=2',
        f'--output={backup_file}'
    ])

if __name__ == '__main__':
    run()
