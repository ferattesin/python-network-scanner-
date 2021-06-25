import scapy.all as scapy
import optparse


def get_user_input():

	parse_object = optparse.OptionParser()

	parse_object.add_option("-i","--ipddr",dest="dest_ipaddr",help="destination ip address")

	return parse_object.parse_args()


def get_request(ip_address):

	arp_request = scapy.ARP(pdst=ip_address)

	broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

	combined_packet = broadcast_packet/arp_request

	
	return combined_packet
	


def result_show(packet):

	(answer_list,unanwser_list) = scapy.srp(packet,timeout=1)
	

	answer_list.summary()



(user_input,arguments) = get_user_input()

if not user_input.dest_ipaddr:
	print("you need help (--help)")

else:
	result_show(get_request(user_input.dest_ipaddr))




