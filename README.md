# ArpGen

ネットワーク負荷検証のためにARP Floodingを起こすツール

arp.pyの下記2行を環境に合わせて変更して実行


arp = ArpGen("ens192")

arp.pkt_gen(get_mac_addr(),"ff:ff:ff:ff:ff:ff","10.149.0.1","10.149.100.25")

