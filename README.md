# ArpGen

ARP Flooding Genrater for network stress test


# arp = ArpGen("<INTERFACE_NAME>")
# arp.pkt_gen(get_mac_addr(),"ff:ff:ff:ff:ff:ff","<SOURCE IP ADDRESS>","<DESTINATION IP ADDRESS>")

Example:
arp = ArpGen("ens192")
arp.pkt_gen(get_mac_addr(),"ff:ff:ff:ff:ff:ff","10.149.0.1","10.149.100.25")
