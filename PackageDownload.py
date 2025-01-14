import pexpect

def ssh_automation():
    ssh_host = "192.168.1.166"
    username = "rps"
    password = "rps@123"
    package_name = "wget"
    file_url = "https://raw.githubusercontent.com/Kiran-255666/personal-_stuff/refs/heads/main/sample.txt"
    download_dir = "~/Downloads"

    try:
        child = pexpect.spawn(f"ssh {username}@{ssh_host}", timeout=60, encoding="utf-8", logfile=open("debug.log", "wb"))

        child.expect("password: ")
        child.sendline(password)
        child.expect(r"\$ ")

        print("[Installing package]")
        child.sendline(f'echo "{password}" | sudo -S apt-get install -y {package_name}')
        child.expect(r"\$ ")

        print("[Preparing download directory]")
        child.sendline(f"mkdir -p {download_dir}")
        child.expect(r"\$ ")

        print("[Downloading file]")
        child.sendline(f"wget -P {download_dir} {file_url}")
        child.expect(r"\$ ")

        print("[Listing files]")
        child.sendline(f"ls {download_dir}")
        child.expect(r"\$ ")
        print(child.before)  # Output the file list

        child.sendline("exit")
        child.close()
        print("Remote operations completed successfully!")

    except pexpect.exceptions.EOF:
        print("Unexpected EOF encountered.")
    except pexpect.exceptions.TIMEOUT:
        print("Operation timed out. Check debug.log for details.")

ssh_automation()
