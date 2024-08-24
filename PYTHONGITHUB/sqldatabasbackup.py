import subprocess

def backup_database(db_name, backup_file):
    command = f"mysqldump -u your_username -p your_password {db_name} > {backup_file}"
    subprocess.run(command, shell=True)
    print(f"Database backup created at {backup_file}")

backup_database('your_database', 'backup.sql')
