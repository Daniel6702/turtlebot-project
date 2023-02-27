import os
import paramiko
from scp import SCPClient
import sys
#______________________________________________________________________________________________
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

def runCommand(cmd,ssh,input=None):
    stdin_, stdout_, stderr_ = ssh.exec_command(cmd)

    if input is not None:
        stdin_.write(input+'\n')
                    
    output = stdout_.readlines()

    return output

def transferFiles(ssh):
    scp = SCPClient(ssh.get_transport(),progress=progress) #create scp client for transfer

    current_path = os.path.abspath(os.getcwd()) #Get path of current file
    os.chdir(current_path+"/files_to_transfer") #select path with files
    list_of_files = os.listdir() #get list of files at path

    for file in list_of_files:
        print("Transferring: " + file)
        scp.put(file) #transfer list of files using the scp client

def receiveFile(ssh,file_name):
    scp = SCPClient(ssh.get_transport())
    scp.get(file_name)
#________________________________________________________________________________________________

def main():
    ssh = createSSHClient("192.168.2.10", "22", "ubuntu", "turtlebot")

    #receiveFile(ssh,'readFromLightSensor.py')
    transferFiles(ssh)

    print(runCommand('ls',ssh))
    #print(runCommand('readFromLightSensor.py',ssh,'turtlebot'))

if __name__ == "__main__":
    main()