import paramiko
import os

reg_key = input("Please enter registration key: ")


hostname = "127.0.0.1"
port = 22
username = "username"
password = "pass"
remote_dir = '/dir1/dir2/'

local_dir = 'C:\\Users\\user_name\\Desktop\\sftp_logs_downloader\\downloaded_logs\\'

if os.path.exists(local_dir):
    pass
else:
    os.mkdir(local_dir)

log_dir = local_dir + reg_key + '\\'


def download_files_from_sftp(hostname, port, username, password, remote_dir, local_dir):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the SFTP server
        ssh.connect(hostname, port=port, username=username, password=password)
        
        # Create an SFTP client
        sftp = ssh.open_sftp()
        
        # Change to the remote directory
        sftp.chdir(remote_dir)
        
        # List files in the remote directory
        files = sftp.listdir()

        # Download zip files
        for file in files:
            if reg_key in file:
                if os.path.exists(log_dir):
                    remote_file = remote_dir + '/' + file
                    local_file = log_dir + file.replace(':', '_')
                    sftp.get(remote_file, local_file)
                    print(f'Downloaded: {file}')
                else:
                    os.mkdir(log_dir)
                    remote_file = remote_dir + '/' + file
                    local_file = log_dir + file.replace(':', '_')
                    sftp.get(remote_file, local_file)
                    print(f'Downloaded: {file}')
                    
        # Close the SFTP connection
        sftp.close()
        
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials.")
    except paramiko.ssh_exception.SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
    except paramiko.ssh_exception.NoValidConnectionsError as connectionError:
        print("Unable to connect to the server: %s" % connectionError)
    finally:
        # Close the SSH connection
        ssh.close()
    '''except paramiko.ssh_exception.SFTPError as sftpException:
        print("SFTP operation failed: %s" % sftpException)'''
    


# Call the function to download files
download_files_from_sftp(hostname, port, username, password, remote_dir, local_dir)
