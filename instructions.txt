# Documentation

I decided to use the python programming language to create my websocket in. 
In order to write this I looked up some example programs and modeled my programs from that.
Unfortunately I cannot find the URL of those programs I looked at. But I would include them if I did.

### Problems

I didn't have many problems writting the wesocket. I only ran into trivial issues such as the toUpper() function
in python 2.7 being used slightly differently than it is in python 3 and a couple of other trivial issues.


### Requirements

In order to run my scripts you must have:

- at least one server/computer with linux installed
- Python 2.7 installed

### Set up

The scripts are currently set up to work on a single computer but it is capable of running on two.
In order to change the ip addresses you should ONLY change the client script ip. You may also want 
to change the TCP_PORT in case it is already taken. Anything in the 5000-5999 range is acceptable.

Changing the client ip/port to use more than one computer:

Original section of code:

   '''python

   TCP_IP = '127.0.0.1'
   TCP_PORT = 5829   

   '''

New section you have changed:

   '''python

   TCP_IP = 'x.x.x.x'
   TCP_PORT = xxxx

   '''


### Running the program

To run my scripts open a terminal window and run socket-server.py with the command:

   python socket-server.py

After you have done this, open a second terminal and start the client script with the command:

   python client-connect.py

Once you have done this the program should now be running properly.

### Using The Program

To use my program you will first observe the instructions on the screen:

   Enter some text:
   reply:


Follow the instructions and enter some text to send to the server:

   Enter some text: Hello
   reply:  HELLO

The program can also handle things such as punctuation, quotations, and numbers:

   Enter some text: what's up??
   reply:  WHAT'S UP??
   Enter some text: 123 test 123
   reply:  123 TEST 123

In order to exit the program simply type "exit" and press enter:

   Enter some text: exit
   reply:  EXIT
   Exiting client program!

## THANKS!

Thank you for using my program. I hope you enjoyed it.

