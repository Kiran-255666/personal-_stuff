import pexpect

def ssh_automation():
    ssh_host = "192.168.1.166"
    username = "rps"
    password = "rps@123"
    package_name = "wget"
    file_url = "https://raw.githubusercontent.com/Kiran-255666/personal-_stuff/refs/heads/main/sample.txt"
    download_dir = "~/mydownloads"

    try:
        # Set up the SSH connection with an increased timeout
        child = pexpect.spawn(f"ssh {username}@{ssh_host}", timeout=500, encoding='utf-8')

        # Open a debug log file
        child.logfile = open("debug.log", "w", encoding="utf-8")

        # Handle SSH password prompt
        child.expect("password: ")
        child.sendline(password)

        # Handle shell prompt
        child.expect(r".*[$#] ")

        print("[Installing package]")
        child.sendline(f"sudo apt-get install -y {package_name}")
        child.expect("password for .*: ", timeout=500)  # Wait for the sudo password prompt
        child.sendline(password)  # Provide the sudo password
        child.expect(r".*[$#] ", timeout=500)  # Wait for the installation to complete

        print("[Preparing download directory]")
        child.sendline(f"mkdir -p {download_dir}")
        child.expect(r".*[$#] ", timeout=500)

        print("[Downloading file]")
        child.sendline(f"wget -P {download_dir} {file_url}")
        child.expect(r".*[$#] ", timeout=500)

        print("[Listing files]")
        child.sendline(f"ls {download_dir}")
        child.expect(r".*[$#] ", timeout=500)
        print(child.before)  # Print the file list

        child.sendline("exit")
        child.close()
        print("Remote operations completed successfully!")

    except pexpect.exceptions.EOF:
        print("Unexpected EOF encountered.")
    except pexpect.exceptions.TIMEOUT:
        print("Operation timed out. Check debug.log for details.")

ssh_automation()
