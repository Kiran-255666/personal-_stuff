import pexpect

def ssh_test():
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

        # Wait for shell prompt
        child.expect(r"\$", timeout=30)

        # Close the session
        child.sendline("exit")
        child.close()

    except pexpect.exceptions.EOF as e:
        print(f"EOF Error: {e}")
    except pexpect.exceptions.TIMEOUT as e:
        print(f"Timeout Error: {e}")
    except Exception as e:
        print(f"Other Error: {e}")

if __name__ == "__main__":
    ssh_test()
