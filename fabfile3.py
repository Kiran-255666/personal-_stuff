from fabric import task, Connection

REMOTE_HOST = "192.168.1.166"
USERNAME = "rps"
PASSWORD = "rps@123"

@task
def query_local_and_remote_info(c):
    """Query system information and directory contents for both local and remote hosts."""
    try:
        print("\n--- Local System Information ---\n")
        
        # List of local commands
        local_commands = [
            ("Hostname", "hostname"),
            ("Network Configuration", "ifconfig" if c.local("uname", hide=True).stdout.strip() == "Linux" else "ipconfig"),
            ("System Uptime", "uptime"),
            ("Current Users", "who"),
            ("Memory Usage", "free -h"),
            ("Disk Usage", "df -h")
        ]

        # Execute local commands
        for desc, command in local_commands:
            print(f"> {desc}:")
            result = c.local(command, hide=True)
            print(result.stdout.strip(), "\n")

    except Exception as e:
        print(f"Error obtaining local system information: {e}")

    try:
        print("\n--- Remote System Information ---\n")
        
        # Establish connection to the remote host
        conn = c.Connection if hasattr(c, 'connection') else Connection(
            host=REMOTE_HOST,
            user=USERNAME,
            connect_kwargs={"password": PASSWORD},
        )
        conn.open()  # Explicitly open the connection

        # List of remote commands
        remote_commands = [
            ("Hostname", "hostname"),
            ("Network Configuration", "ifconfig" if conn.run("uname", hide=True).stdout.strip() == "Linux" else "ipconfig"),
            ("System Uptime", "uptime"),
            ("Current Users", "who"),
            ("Memory Usage", "free -h"),
            ("Disk Usage", "df -h")
        ]

        # Execute remote commands
        for desc, command in remote_commands:
            print(f"> {desc}:")
            result = conn.run(command, hide=True)
            print(result.stdout.strip(), "\n")

        # Close the connection
        conn.close()

    except Exception as e:
        print(f"Error obtaining remote system information: {e}")
