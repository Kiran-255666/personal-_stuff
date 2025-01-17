import pexpect
import sys

def connect_and_execute(remote_host, username, password, commands):
    try:
        ssh_session = pexpect.spawn(f"ssh {username}@{remote_host}", timeout=120)
        ssh_session.logfile = sys.stdout.buffer  # Log output for debugging
        
        ssh_session.expect(["Are you sure you want to continue connecting", "password:"])
        if ssh_session.after == "Are you sure you want to continue connecting":
            ssh_session.sendline("yes")
            ssh_session.expect("password:")
        ssh_session.sendline(password)

        for command in commands:
            ssh_session.expect(r"\$")
            ssh_session.sendline(command)
            ssh_session.expect(r"\$")
        
        ssh_session.sendline("exit")
        ssh_session.close()
    except pexpect.exceptions.TIMEOUT:
        print("Operation timed out.")
    except pexpect.exceptions.ExceptionPexpect as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remote_host = "192.168.1.166"  # Replace with your remote machine's IP or hostname
    username = "rps"
    password = "rps@123"
    commands = [
        "sudo apt install -y wget",
        "wget https://raw.githubusercontent.com/Kiran-255666/Pyspark_18-01-24/refs/heads/main/titanic.csv",
        "ls -la",
    ]
    connect_and_execute(remote_host, username, password, commands)
