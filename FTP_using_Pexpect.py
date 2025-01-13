import pexpect 

 

def ftp_automation(): 

    ftp_host = "192.168.1.166"  # Replace with your FTP server 

    username = "ftpuser"   # Replace with your username 

    password = "YankeeD00dle!"   # Replace with your password 

    remote_file = "/hoome/ftpuser/ftp/files/ftpfile.txt"  # Replace with a file name on the FTP server 

    local_file = "/home/rps/Downloads/ftpdownloadedfile.txt"  # Name for the downloaded file 

 

    try: 

        # Start the FTP session 

        child = pexpect.spawn(f"ftp {ftp_host}") 

 

        # Login: Handle username 

        child.expect("Name .*: ") 

        child.sendline(username) 

 

        # Login: Handle password 

        child.expect("Password:") 

        child.sendline(password) 

 

        # FTP prompt: Execute commands 

        child.expect("ftp> ") 

         

        # List files 

        child.sendline("ls") 

        child.expect("ftp> ") 

        print(child.before.decode())  # Print the directory contents 

 

        # Download a file 

        child.sendline(f"get {remote_file} {local_file}") 

        child.expect("ftp> ") 

 

        # Close the session 

        child.sendline("bye") 

        child.close() 

        print(f"File '{remote_file}' downloaded as '{local_file}' successfully!") 

 

    except pexpect.exceptions.EOF: 

        print("Unexpected EOF occurred.") 

    except pexpect.exceptions.TIMEOUT: 

        print("The operation timed out.") 

 

ftp_automation() 
