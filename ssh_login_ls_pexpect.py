import pexpect

def ssh_login_and_execute():
    try:
        # Update hostname, username, and private key path
        hostname = "192.168.1.166"
        username = "rps"
        private_key_path = "/home/rps/.ssh/id_rsa"

        # SSH command
        ssh_command = f"ssh -i {private_key_path} {username}@{hostname}"
        print(f"Running command: {ssh_command}")

        # Start SSH session
        child = pexpect.spawn(ssh_command)

        # Debug: Log all interactions
        child.logfile = open("debug_log.txt", "wb")

        # Handle "Are you sure you want to continue connecting" prompt
        index = child.expect([
            "Are you sure you want to continue connecting (yes/no)?",
            r"\$",  # Shell prompt
            pexpect.EOF,
            pexpect.TIMEOUT,
        ], timeout=30)

        if index == 0:  # New host key confirmation
            child.sendline("yes")
            child.expect(r"\$")

        elif index == 2:  # EOF
            raise Exception("Connection closed unexpectedly (EOF).")

        elif index == 3:  # Timeout
            raise Exception("Connection timed out.")

        # Commands to execute
        commands = ["hostname", "ifconfig", "ls -l"]

        for command in commands:
            print(f"Executing command: {command}")
            child.sendline(command)
            child.expect(r"\$")  # Wait for shell prompt to reappear

            # Retrieve and print output
            output = child.before.decode()
            print(f"Output of `{command}`:\n{output}")

        # Close the session
        child.sendline("exit")
        child.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ssh_login_and_execute()
