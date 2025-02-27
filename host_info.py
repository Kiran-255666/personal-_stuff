import paramiko

# Remote server details
hostname = "104.210.115.181"  # Replace with the hostname or IP of the remote server
port = 22  # Default SSH port
username = "kiran"  # Replace with your SSH username
password = "yankeeD00dle"  # Replace with your SSH password

def ssh_execute_command(hostname, port, username, password, command):
    """
    Connects to a remote server via SSH, executes a command, and returns the output.

    :param hostname: The hostname or IP address of the remote server.
    :param port: The SSH port (default is 22).
    :param username: The username for SSH authentication.
    :param password: The password for SSH authentication.
    :param command: The command to execute on the remote server.
    :return: The command output as a string.
    """
    try:
        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()

        # Automatically add the server's host key (use cautiously)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        ssh_client.connect(hostname, port=port, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Read the command's output and error
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Print the output or error
        if output:
            print("Directories:")
            print(output)
        if error:
            print("Error:")
            print(error)

        # Close the SSH connection
        ssh_client.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# Command to list directories on the remote server
command_to_run = "ls"

# Call the function
ssh_execute_command(hostname, port, username, password, command_to_run)
