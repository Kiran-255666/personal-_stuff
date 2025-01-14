import pexpect
import sys


import sys
import pexpect

def ssh_connect(host, username, password):
    """
    Establish an SSH connection to a remote machine.
    :param host: The hostname or IP address of the remote machine.
    :param username: The SSH username.
    :param password: The SSH password.
    :return: A pexpect session connected to the remote machine.
    """
    try:
        print(f"Connecting to {host} as {username}...")
        ssh_command = f"ssh {username}@{host}"
        session = pexpect.spawn(ssh_command, timeout=30)

        # Use sys.stdout with string handling for compatibility
        session.logfile = sys.stdout.buffer if hasattr(sys.stdout, 'buffer') else sys.stdout

        # Handle SSH password prompt
        index = session.expect(["password:", pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            session.sendline(password)
            session.expect(f"{username}@")
            print(f"Successfully connected to {host}.")
        elif index == 1:
            print("Unexpected EOF while trying to connect via SSH.")
            session.close()
            return None
        elif index == 2:
            print("SSH connection timed out.")
            session.close()
            return None

        return session
    except Exception as e:
        print(f"An error occurred while connecting to {host}: {e}")
        return None



def remote_install_package(session, package_name):
    """
    Install a package on a remote machine via SSH.
    :param session: The active SSH session.
    :param package_name: The name of the package to install.
    """
    try:
        print(f"Installing {package_name} on the remote machine...")
        session.sendline(f"sudo apt-get install {package_name} -y")
        index = session.expect(["password for", pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            password = input("Enter the sudo password for the remote machine: ")
            session.sendline(password)
            session.expect(pexpect.EOF)
            print(f"{package_name} installed successfully on the remote machine.")
        elif index == 1:
            print(f"Unexpected EOF during {package_name} installation.")
        elif index == 2:
            print(f"Operation timed out while installing {package_name}.")
    except Exception as e:
        print(f"An error occurred while installing {package_name}: {e}")


def remote_download_file(session, tool_name, url, destination):
    """
    Download a file on a remote machine via SSH using a specified tool.
    :param session: The active SSH session.
    :param tool_name: The tool to use for downloading (e.g., wget, curl).
    :param url: The URL of the file to download.
    :param destination: The destination path on the remote machine.
    """
    try:
        print(f"Downloading file from {url} to {destination} using {tool_name} on the remote machine...")
        command = f"{tool_name} -O {destination} {url}" if tool_name == "wget" else f"{tool_name} -o {destination} {url}"
        session.sendline(command)
        session.expect(pexpect.EOF)
        print("File downloaded successfully on the remote machine.")
    except Exception as e:
        print(f"An error occurred during the file download on the remote machine: {e}")


if __name__ == "__main__":
    # Remote machine credentials
    remote_host = "192.168.1.166"  # Replace with your remote machine's IP or hostname
    username = "rps"  # Replace with your SSH username
    password = "rps@123"  # Replace with your SSH password

    # Example tool and file download details
    tool = "wget"  # Tool to use (e.g., wget or curl)
    file_url = "https://raw.githubusercontent.com/Kiran-255666/personal-_stuff/refs/heads/main/sample.txt"
    destination_path = "~/sample-file.txt"

    # Establish SSH connection
    ssh_session = ssh_connect(remote_host, username, password)
    if ssh_session:
        # Install the tool if necessary
        remote_install_package(ssh_session, tool)

        # Download the file
        remote_download_file(ssh_session, tool, file_url, destination_path)

        # Close the SSH session
        ssh_session.close()
