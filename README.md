# This project was made for my personal homemade server. Its purpose is to make some sort of messenging app into the console.

## Requirements:
- Python3

## How to use:
1. In the code replace the ip of my server with yours and whatever port you used. (in the client side replace your ip and port, and serverside just replace the port)
2. go to your server (i use ubuntu server) and open the port you want to use:
   ```
   sudo ufw allow 17172/tcp
   ```
   in my case i use 17172 
3. make sure to port forward 17172 from your router
4. run the client with python 3 on the server
   ```
   python3 server.py
   ```
5. any user now just needs to go on thier computer and run
   ```
   python3 client.py
   ```
have fun!
