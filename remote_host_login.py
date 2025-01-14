import paramiko

def ssh_connect_and_interact(remote_host, username, password):
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        
        # Automatically add the server's host key if it's not already known
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print(f"Connecting to {remote_host}...")
        
        # Connect to the remote host
        ssh_client.connect(hostname=remote_host, username=username, password=password)
        print("Connection established.")
        
        # Start an interactive shell session
        print("Starting interactive shell session...")
        channel = ssh_client.invoke_shell()
        
        # Keep the session interactive
        while True:
            # Read from the shell
            if channel.recv_ready():
                output = channel.recv(1024).decode()
                print(output, end="")  # Print the shell output
                
            # Allow the user to send commands
            user_input = input("Enter command (or 'exit' to quit): ")
            if user_input.lower() == "exit":
                break
            channel.send(user_input + "\n")
        
        # Close the shell session
        channel.close()
        print("Shell session closed.")
    
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username or password.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the SSH client
        ssh_client.close()
        print("Connection closed.")

if __name__ == "__main__":
    # Replace with your SSH server details
    remote_host = "192.168.1.166"
    username = "rps"
    password = "rps@123"
    
    ssh_connect_and_interact(remote_host, username, password)
