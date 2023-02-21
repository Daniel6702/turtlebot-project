import os
import paramiko
from scp import SCPClient
import sys

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def runCommand(cmd,ssh):
    stdin_, stdout_, stderr_ = ssh.exec_command(cmd)
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()
    return lines

def getFiles():
    current_path = os.path.abspath(os.getcwd())
    os.chdir(current_path+"/files_to_transfer")
    list = os.listdir()
    return list

def transferFiles(ssh):
    scp = SCPClient(ssh.get_transport(),progress=progress)
    list_of_files = getFiles()
    for file in list_of_files:
        print("Transferring: " + file)
        scp.put(file)

def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

def receiveFile(ssh,file_name):
    scp = SCPClient(ssh.get_transport())
    scp.get(file_name)

ssh = createSSHClient("192.168.2.10", "22", "ubuntu", "turtlebot")

#receiveFile(ssh,'readFromLightSensor.py')
transferFiles(ssh)

res = runCommand('ls',ssh)
print(res)