import subprocess

# Function to perform Docker cleanup
def docker_cleanup():
    try:
        # Step 1: Stop all running Docker containers
        # "docker ps -q" lists all running container IDs
        # "docker stop $(docker ps -q)" stops all containers using their IDs
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
if __name__ == "__main__":
    # Call the cleanup function
    docker_cleanup()
# This script performs a comprehensive cleanup of Docker containers, images, volumes, and networks.
# It stops all running containers, removes all containers and images,
# and cleans up unused volumes and networks.
# It uses subprocess to run Docker commands in the shell.
# The script is designed to be run as a standalone program.
# It handles errors gracefully and prints a success message upon completion.
# The script is intended for users who want to free up space and resources
# by cleaning up their Docker environment.
# Note: Use this script with caution, as it will remove all Docker containers, images, and volumes.
# Make sure to back up any important data before running it.
# This script is intended for users who are familiar with Docker and its command-line interface.
# It is recommended to run this script in a controlled environment
# where you can safely perform cleanup operations.
# The script is written in Python and uses the subprocess module        
