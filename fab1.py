from fabric import task

REMOTE_HOST = "192.168.1.194"
USERNAME = "admin"
PASSWORD = "yankeeD00dle"

@task
def get_remote_directory_contents(c):
    """Retrieve and display the contents of a remote directory dynamically."""
    # Accept remote directory as user input
    remote_directory = input("Enter the remote directory path: ")

    print(f"Querying the contents of the remote directory: {remote_directory}\n")
    try:
        # Establish connection to the remote machine
        conn = c.connection if hasattr(c, 'connection') else Connection(
            host=REMOTE_HOST,
            user=USERNAME,
            connect_kwargs={"password": PASSWORD},
        )
        conn.open()  # Explicitly open the connection

        # Command to list directory contents (Windows-specific)
        command = f'dir "{remote_directory}"'
        result = conn.run(command, hide=True)

        # Display the output
        print(f"Contents of {remote_directory}:\n")
        print(result.stdout.strip())

        conn.close()  # Close the connection

    except Exception as e:
        print(f"Error obtaining remote directory contents: {e}")
