"""
 packets will enter the filter in the following JSON format:
 
 {
    "packets": [
        {
            "source": "10.0.0.1",
            "destination": "172.169.20.15",
            "suspicious": 1
        },
        {
            "source": "10.0.0.2",
            "destination": "172.169.20.10",
            "suspicious": 0
        }
    ]
}
"""
import json
import pprint

def generate_test_packets()
    return json.load(open("packets.json"))['packets']

packets = generate_test_packets()

pprint.pprint(packets)

ok_packets = []

for packet in packets
    if not packet['suspicious']:
        ok_packets.append(packet)

for packet in ok_packets:
    print(json.dumps(packet, indent=4))

    if packet['suspicious']:
        raise Exception("suspicious packet got thru!")

print("packet filter works!")

# with open('packets.json') as f:
#     data = json.load(f)
#     packets = data['packets']
#     # print(packets)

# for packet in packets:
#     # print(packet)
#     if packet['suspicious'] == 1:
#         packets.remove(packet)
#         # print(packets)

# for packet in packets:
#     print(json.dumps(packet, indent=4))

#     if packet['suspicious'] == 1:
#         raise Exception("Suspicious packet got through!")


# print("Packet filter works!")


    
