# Chatty
Chatty is a basic client(s)/server terminal app utilizing socket communication written with Python. Goal of this project is to learn basic socket communication, threading and explore the python socket library. Both server and client come with some basic functions that are executed when a specific message is entered into the terminal.

<img src='https://github.com/ianmat55/socket-chatbot/blob/main/images/chatty.png'>

## Commands 
<img src='https://github.com/ianmat55/socket-chatbot/blob/main/images/server_cmds.png'>
Server Functions:
- kick(): kicks a specific user from chat
- ls(): lists active connections
- bc(): send msg directly to one client

https://github.com/ianmat55/socket-chatbot/blob/main/images/client_cmds.png
Both Client and Server:
- read(): specify a path to text file and server will read file into chat
- cls(): clears terminal
- exit(): close connection
- help(): print help table

## How to Run
1. Fork or download github repo
2. pip install 'rich'. Program coded with python v3.8.10
3. cd to project directory and type 'python3 server_start.py' start server
4. enter 'local' to connect for localhost
5. Type 'python3 start_server.py' start server. To start client, enter 'python3 start_client.py'. Can run multiple times for multiple clients
6. enter 'local' to connect to server


