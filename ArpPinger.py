import argparse
import scapy.all as scapy

class ARP_Ping():

	def __init__(self):
		print("ARP Ping initialized..")
		
	def get_user_input(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-i','--ipaddress',type=str,help="Enter ip range to send ARP ping.")
		args = parser.parse_args()

		if args.ipaddress != None:
			return args
		else:
			print("Enter ip range")
			
	def arp_req(self,ip):
		
		arp_request_packet = scapy.ARP(pdst=ip)
		broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
		combined_packet = broadcast_packet/arp_request_packet
		
		(answered_list, unanswered) = scapy.srp(combined_packet, timeout=1)
		answered_list.summary()
		
if __name__ == "__main__":
	arp_ping = ARP_Ping()
	ip_range = arp_ping.get_user_input()
	arp_ping.arp_req (ip_range.ipaddress)
