import pexpect

def ssh_login_with_key(hostname, username, private_key_path, command):
    try:
        # Spawn SSH command
        ssh_command = f"ssh -i {private_key_path} {username}@{hostname}"
        child = pexpect.spawn(ssh_command)

        # Handle expected prompts
        child.expect(["Are you sure you want to continue connecting (yes/no)?", pexpect.EOF, pexpect.TIMEOUT], timeout=10)
        if "Are you sure" in child.before.decode():
            child.sendline("yes")
            child.expect("password:", timeout=5)

        # If the SSH connection is successful, execute the command
        child.sendline(command)
        child.expect(pexpect.EOF)

        # Retrieve command output
        output = child.before.decode()
        print(f"Command Output: {output}")
        child.close()
    except pexpect.exceptions.ExceptionPexpect as e:
        print(f"An error occurred: {e}")

# Replace with your details
ssh_login_with_key(
    hostname="192.168.1.1666",
    username="rps",
    private_key_path="~/.ssh/id_rsa",
    command="ls -l"
)
