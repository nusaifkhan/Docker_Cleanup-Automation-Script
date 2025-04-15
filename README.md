# Docker Cleanup Python Automation Script 🧼🐳

## Overview

This Python script automates the cleanup of your Docker environment by performing the following steps:

- **Stop all running containers**
- **Remove all containers** (both running and stopped)
- **Remove all Docker images**
- **Remove all unused volumes**
- **Clean up unused Docker networks**

It’s a quick and easy way for DevOps engineers and enthusiasts to reclaim disk space and maintain a tidy Docker setup.

## Requirements

- **Docker**: Installed, running, and accessible via your terminal.
- **Python 3**: Installed on your system.
- No additional Python packages are required as the script uses Python’s built-in `subprocess` module.

## Usage Instructions

1. **Save the Script**  
   Copy the code into a file, for example, `docker_cleanup.py`.

2. **Run the Script**  
    Open your terminal, navigate to the folder containing the script, and execute:
   ```bash
   python3 docker_cleanup.py
   ```
   If you run into permission issues, you might need to run it with sudo.

## Code Explanation

**Below is the complete code with inline comments explaining each step:**

```python
import subprocess

# Function to perform Docker cleanup

def docker_cleanup():
try: # Step 1: Stop all running Docker containers # "docker ps -q" lists all running container IDs # "docker stop $(docker ps -q)" stops all containers using their IDs
subprocess.run("docker stop $(docker ps -q)", shell=True, check=True)

        # Step 2: Remove all containers (both running and stopped)
        # "docker ps -a -q" lists all container IDs (including stopped containers)
        # "docker rm $(docker ps -a -q)" removes all containers by their IDs
        subprocess.run("docker rm $(docker ps -a -q)", shell=True, check=True)

        # Step 3: Remove all Docker images
        # "docker images -q" lists all image IDs
        # "docker rmi -f $(docker images -q)" forcefully removes all images
        subprocess.run("docker rmi -f $(docker images -q)", shell=True, check=True)

        # Step 4: Remove all unused Docker volumes
        # "docker volume ls -q" lists all volume names/IDs
        # "docker volume rm $(docker volume ls -q)" removes all volumes
        subprocess.run("docker volume rm $(docker volume ls -q)", shell=True, check=True)

        # Step 5: Clean up unused Docker networks
        # "docker network prune -f" removes all unused networks
        subprocess.run("docker network prune -f", shell=True, check=True)

        # Print success message
        print("Docker cleanup completed successfully! 🧼🐳")

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the cleanup process
        print(f"An error occurred during cleanup: {e}")

# Main entry point for the script

if **name** == "**main**": # Call the cleanup function
docker_cleanup()
```

## Contributing

**Contributions to improve the script are welcome! Feel free to fork the repository, submit pull requests, or open issues if you have suggestions or encounter any problems.**

## License

**This project is licensed under the MIT License. See the LICENSE file for more details.**
