import pexpect

def ssh_automation():
    ssh_host = "192.168.1.166"
    username = "rps"
    password = "rps@123"
    package_name = "wget"
    file_url = "https://raw.githubusercontent.com/Kiran-255666/personal-_stuff/refs/heads/main/sample.txt"
    download_dir = "~/mydownloads"

    try:
        # Use encoding to handle Unicode strings
        child = pexpect.spawn(f"ssh {username}@{ssh_host}", timeout=120, encoding='utf-8')

        # Open the debug log in text mode
        child.logfile = open("debug.txt", "w", encoding='utf-8')

        # Handle the password prompt
        child.expect("password: ", timeout=60)
        child.sendline(password)

        # Handle the login banner
        child.expect("Last login", timeout=60)
        child.expect(r".*[$#] ", timeout=60)  # Match the shell prompt

        print("[Installing package]")
        child.sendline(f'sudo apt-get install -y {package_name}')
        child.expect(r".*[$#] ", timeout=60)

        print("[Preparing download directory]")
        child.sendline(f"mkdir -p {download_dir}")
        child.expect(r".*[$#] ", timeout=60)

        print("[Downloading file]")
        child.sendline(f"wget -P {download_dir} {file_url}")
        child.expect(r".*[$#] ", timeout=60)

        print("[Listing files]")
        child.sendline(f"ls {download_dir}")
        child.expect(r".*[$#] ", timeout=60)
        print(child.before)  # Output the file list

        child.sendline("exit")
        child.close()
        print("Remote operations completed successfully!")

    except pexpect.exceptions.EOF:
        print("Unexpected EOF encountered.")
    except pexpect.exceptions.TIMEOUT:
        print("Operation timed out. Check debug.txt for details.")

ssh_automation()
