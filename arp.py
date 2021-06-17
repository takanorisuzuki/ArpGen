# coding: utf-8
import socket
import struct
import sys
import time
import uuid
import re

class ArpGen:
    def __init__(self, interface):
        self.soc = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        self.soc.bind((interface, 0))
    def __del__(self):
        self.soc.close()
    def pkt_gen(self,s_mac,d_mac,s_ip,d_ip):
        s_mac = self.mac_to_string(s_mac)
        d_mac = self.mac_to_string(d_mac)
        s_ip = socket.inet_aton(s_ip)
        d_ip = socket.inet_aton(d_ip)
        ether = self.make_ether(s_mac,d_mac)
        arp = self.make_arp(s_mac, d_mac, s_ip, d_ip)
        packet = ether+arp
        while True:
            self.soc.send(packet)
            time.sleep(1)
    def mac_to_string(self, mac_arg):
        mac = ["00" for _ in range(6)]
        mac_list = mac_arg.split(":")
        for i in range(len(mac_list)):
            mac[i] = mac_list[i]
        mac_bin = ""
        for m in mac:
            mac_bin += struct.pack("!B", int(m,16))
        return mac_bin
    def make_ether(self, s_mac, d_mac):
        return struct.pack("!6s6sH", d_mac, s_mac, 0x0806)
    def make_arp(self, s_mac, d_mac, s_ip, d_ip):
        return struct.pack("!HHBBH6s4s6s4s", 0x1, 0x0800, 6, 4, 1, s_mac, s_ip, d_mac, d_ip)
    def get_mac_addr(self):
        node = uuid.getnode()
        mac = uuid.UUID(int=node)
        addr = mac.hex[-12:]
        mac_addr = ":".join(re.split('(..)',addr)[1::2])
        return mac_addr

# arp = ArpGen("ens192")
# arp.pkt_gen(get_mac_addr(),"ff:ff:ff:ff:ff:ff","10.149.0.1","10.149.100.25")
