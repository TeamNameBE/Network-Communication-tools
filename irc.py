import socket
import sys
import time


class IRC:
    irc = socket.socket()

    def __init__(self):
        # Define the socket
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        # Transfer data
        final_msg = "PRIVMSG " + channel + " " + msg + "\n"
        print("~~>", final_msg)
        self.irc.send(bytes(final_msg, "UTF-8"))

    def connect(self, server, port, channel, botnick, botpass, botnickpass):
        # Connect to the server
        print("Connecting to: " + server)
        self.irc.connect((server, port))

        # Perform user authentication
        self.irc.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " :python\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
        self.irc.send(bytes("NICKSERV IDENTIFY " + botnickpass + " " + botpass + "\n", "UTF-8"))
        time.sleep(5)

        # join the channel
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))
        time.sleep(2)
        while "End of /NAMES" not in self.get_response():
            pass

    def get_response(self):
        time.sleep(1)
        # Get the response
        try:
            resp = self.irc.recv(2040)
            resp = resp.decode("UTF-8")
        except Exception as e:
            print(f"Error decoding : {str(resp)} - ({e})")
            resp = str(resp)

        if resp != "":
            print("<~~", resp)

        if resp.find("PING") != -1:
            self.irc.send(bytes('PONG ' + resp.split()[1] + '\r\n', "UTF-8"))

        return resp
