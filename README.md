# ArpGen

ARP Flooding Genrater for network stress test


How to execute in Python:
- arp = ArpGen("<INTERFACE_NAME>")
- arp.pkt_gen(get_mac_addr(),"ff:ff:ff:ff:ff:ff","<SOURCE_IP_ADDRESS>","<DESTINATION_IP_ADDRESS>")


Example:
arp = ArpGen("ens192")
arp.pkt_gen(get_mac_addr(),"ff:ff:ff:ff:ff:ff","10.149.0.1","10.149.100.25")
