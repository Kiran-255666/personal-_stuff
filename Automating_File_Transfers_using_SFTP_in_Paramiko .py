import paramiko

def sftp_file_transfer(hostname, port, username, password, local_file_path, remote_file_path, mode="upload"):
    try:
        # Initialize SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote host
        print(f"Connecting to {hostname}...")
        ssh_client.connect(hostname, port=port, username=username, password=password)
        print(f"Connected to {hostname}!")
        
        # Open SFTP session
        sftp = ssh_client.open_sftp()
        
        if mode == "upload":
            # Upload the file
            print(f"Uploading {local_file_path} to {remote_file_path}...")
            sftp.put(local_file_path, remote_file_path)
            print("File uploaded successfully.")
        elif mode == "download":
            # Download the file
            print(f"Downloading {remote_file_path} to {local_file_path}...")
            sftp.get(remote_file_path, local_file_path)
            print("File downloaded successfully.")
        else:
            print("Invalid mode! Use 'upload' or 'download'.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the SFTP session and SSH connection
        if 'sftp' in locals():
            sftp.close()
            print("SFTP session closed.")
        ssh_client.close()
        print("SSH connection closed.")

if __name__ == "__main__":
    # Replace these with your remote host details
    hostname = "192.168.1.166"  # Remote host's IP or domain
    port = 22                             # Default SSH port
    username = "rps"            # Your username
    password = "rps@123"            # Your password
    
    # File paths
    local_file_path = "/home/rps/Downloads/samplefile.txt"  # Local file path
    remote_file_path = "/home/rps/Desktop/sftptransferredfile.txt"  # Remote file path

    # Choose operation mode: "upload" or "download"
    mode = "upload"  # Change to "download" to fetch files from the remote server

    # Automate file transfer
    sftp_file_transfer(hostname, port, username, password, local_file_path, remote_file_path, mode)
