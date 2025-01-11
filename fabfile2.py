from fabric import task, Connection

REMOTE_HOST = "192.168.1.145"
USERNAME = "rps"
PASSWORD = "rps@123"


@task
def local_info(c):
    """Task to query information from the local machine."""
    print("\n--- Local Machine Information ---")
    while True:
        print("Options for Local Machine:")
        print("1. List directory contents")
        print("2. Get system information")
        print("3. Run a custom command")
        print("0. Exit local tasks")
        choice = input("Enter your choice: ")

        if choice == "1":
            directory = input("Enter the local directory path: ")
            try:
                result = c.local(f"ls -la {directory}", hide=True)
                print(f"\nContents of {directory}:\n")
                print(result.stdout.strip())
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                result = c.local("uname -a", hide=True)
                print("\nSystem Information:\n")
                print(result.stdout.strip())
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            command = input("Enter the custom command to execute locally: ")
            try:
                result = c.local(command, hide=True)
                print("\nCommand Output:\n")
                print(result.stdout.strip())
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


@task
def remote_info(c):
    """Task to query information from the remote machine."""
    print("\n--- Remote Machine Information ---")
    try:
        conn = Connection(
            host=REMOTE_HOST,
            user=USERNAME,
            connect_kwargs={"password": PASSWORD},
        )
        conn.open()  # Explicitly open the connection

        while True:
            print("\nOptions for Remote Machine:")
            print("1. List directory contents")
            print("2. Get system information")
            print("3. Run a custom command")
            print("0. Exit remote tasks")
            choice = input("Enter your choice: ")

            if choice == "1":
                remote_directory = input("Enter the remote directory path: ")
                try:
                    result = conn.run(f'ls -la "{remote_directory}"', hide=True)
                    print(f"\nContents of {remote_directory}:\n")
                    print(result.stdout.strip())
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    result = conn.run("uname -a", hide=True)
                    print("\nSystem Information:\n")
                    print(result.stdout.strip())
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                command = input("Enter the custom command to execute remotely: ")
                try:
                    result = conn.run(command, hide=True)
                    print("\nCommand Output:\n")
                    print(result.stdout.strip())
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

        conn.close()  # Close the connection

    except Exception as e:
        print(f"Error connecting to remote machine: {e}")
