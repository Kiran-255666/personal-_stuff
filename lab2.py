import pexpect

def ssh_and_execute_commands(host, username, password, commands):
    try:
        # Start the SSH session
        ssh_command = f"ssh {username}@{host}"
        ssh_session = pexpect.spawn(ssh_command, timeout=60)

        # Expect password prompt and send password
        ssh_session.expect("password:")
        ssh_session.sendline(password)

        # Execute each command
        for command in commands:
            ssh_session.expect(r"\$")  # Expect the shell prompt
            ssh_session.sendline(command)

        # Exit the session
        ssh_session.expect(r"\$")
        ssh_session.sendline("exit")
        ssh_session.close()

    except pexpect.EOF:
        print("Connection closed unexpectedly.")
    except pexpect.TIMEOUT:
        print("Connection timed out.")

if __name__ == "__main__":
    # Remote server details
    remote_host = "192.168.1.145"
    remote_user = "rps"
    remote_password = "rps@123"

    # Commands to execute remotely
    commands_to_run = [
        "sudo apt update",  # Update package list
        "sudo apt install -y wget",  # Install wget as an example package
        "wget https://raw.githubusercontent.com/Kiran-255666/personal-_stuff/refs/heads/main/sample.txt",  # Download a file
        "mv sample.txt ~/downloads/",  # Move the downloaded file to a directory
    ]

    # Automate SSH and commands
    ssh_and_execute_commands(remote_host, remote_user, remote_password, commands_to_run)
