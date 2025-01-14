import pexpect 

 

def ssh_automation(): 

    # Define server and operation details 

    ssh_host = "192.168.1.166"  # Replace with your remote server 

    username = "rps"       # Replace with your username 

    password = "rps@123"       # Replace with your password 

    package_name = "wget"            # Package to install 

    file_url = "https://raw.githubusercontent.com/Kiran-255666/personal-_stuff/refs/heads/main/sample.txt"  # File to download 

    download_dir = "~/Downloads"     # Target directory on remote server 

 

    try: 

        # Start an SSH session 

        child = pexpect.spawn(f"ssh {username}@{ssh_host}") 

 

        # Wait for the password prompt 

        child.expect("password: ") 

        child.sendline(password) 

 

        # Wait for the shell prompt 

        child.expect(r"\$ ") 

 

        # Step 1: Install the specified package 

        print("[Installing package]") 

        child.sendline(f"sudo apt-get install -y {package_name}") 

        child.expect("password for .*: ") 

        child.sendline(password) 

        child.expect(r"\$ ") 

 

        # Step 2: Create the target directory if it doesn't exist 

        print("[Preparing download directory]") 

        child.sendline(f"mkdir -p {download_dir}") 

        child.expect(r"\$ ") 

 

        # Step 3: Download the file 

        print("[Downloading file]") 

        child.sendline(f"wget -P {download_dir} {file_url}") 

        child.expect(r"\$ ") 

 

        # Step 4: List the files in the download directory 

        print("[Listing files]") 

        child.sendline(f"ls {download_dir}") 

        child.expect(r"\$ ") 

        print(child.before.decode())  # Output the file list 

 

        # Step 5: Close the session 

        child.sendline("exit") 

        child.close() 

        print("Remote operations completed successfully!") 

 

    except pexpect.exceptions.EOF: 

        print("Unexpected EOF encountered.") 

    except pexpect.exceptions.TIMEOUT: 

        print("Operation timed out.") 

 

# Execute the function 

ssh_automation() 
