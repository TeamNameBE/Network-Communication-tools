# Networking Programming Tools

This repository contains basic tools that can be used to communicate with a server for programming challenges

## IRCBot

This is a sample IRC bot that can be used for programming challenges

It handles connection, ping and writes what it sends and what it receives

Sample usage :

```python
from network-communication-tools.irc import IRC

server = "freenode.org"  # Provide a valid server IP/Hostname
port = 6667
channel = "#sample_channel"
botnick = "TeamNameBot"
botnickpass = "michel"
botpass = "<%= @michelpassword %>"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)
irc.send(channel, "up")

while True:
    text = irc.get_response()

    if "PRIVMSG" in text and botnick in text and "hello" in text:
        irc.send(channel, "Hello !")
```

## TCPWrapper

This is a simple socket communication wrapper to use for challenges using netcat

Example : A simple time Attack

```python
from network-communication-tools.tcpWrapper import TCPWrapper

hostname = sys.argv[1]
port = int(sys.argv[2])
key_size = 12  # Set to -1 for unknown size

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"

sock = TCPWrapper(hostname, port)
sock.open()
print(sock.receive())

key = ""
for x in range(key_size):
    timings = []
    for index, letter in enumerate(alphabet):
        startTime = time.time()
        sock.send(key + letter + "\n")
        sock.receive()
        timeElapsed = time.time() - startTime
        timings.append(timeElapsed)

    key += alphabet[timings.index(max(timings))]
    print(key)

```
