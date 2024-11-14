# Please implement a program that synchronizes two folders: source and replica.
# The program should maintain a full, identical copy of source folder at replica folder.

# Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;
# Synchronization should be performed periodically;
# File creation/copying/removal operations should be logged to a file and to the console output;
# Folder paths, synchronization interval and log file path should be provided using the command line arguments;
# It is undesirable to use third-party libraries that implement folder synchronization;
# It is allowed (and recommended) to use external libraries implementing other well-known algorithms.
# For example, there is no point in implementing yet another function that calculates MD5 if you need it for the task – it is perfectly acceptable to use a third-party (or built-in) library;
# The solution should be presented in the form of a link to the public GitHub repository.

# Extra: implement different instances by using different threads to make it possible for the synchronization of multiple folders (source to replica pairs)

from foldersync import FolderSync
from helpers import input_sync_details

def main():
    sync_objects = []

    while True:
        sync_details = input_sync_details()
        if sync_details[0] is None:  # User chose to exit
            break
        
        source_directory, destination_directory, interval, log_file = sync_details

        print(f"Starting synchronization from {source_directory} to {destination_directory} every {interval} seconds.")

        # Create a FolderSync object and start synchronization
        folder_sync = FolderSync(source_directory, destination_directory, interval, log_file)
        sync_thread = folder_sync.start_sync()
        sync_objects.append(folder_sync)

    print("\nStopping all synchronizations...")

    # Signal all threads to stop
    for sync in sync_objects:
        sync.stop_sync()

    # Optionally, wait for all threads to finish
    for sync in sync_objects:
        sync_thread.join()

    print("All synchronizations stopped.")

if __name__ == "__main__":
    main()