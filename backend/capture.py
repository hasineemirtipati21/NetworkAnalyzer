from scapy.all import sniff
import pandas as pd
import time

file = "traffic_data.csv"

def process_packet(packet):
    try:
        if packet.haslayer("IP"):
            data = {
                "Time": time.time(),
                "Source": packet["IP"].src,
                "Destination": packet["IP"].dst,
                "Protocol": packet["IP"].proto,
                "Length": len(packet)
            }

            df = pd.DataFrame([data])

            # Append to CSV
            df.to_csv(file, mode='a', header=False, index=False)

    except:
        pass


def start_capture():
    print("Starting packet capture...")
    
    # Create CSV with header if not exists
    try:
        pd.read_csv(file)
    except:
        pd.DataFrame(columns=["Time","Source","Destination","Protocol","Length"]).to_csv(file, index=False)

    sniff(
    prn=process_packet,
    store=False,
    iface="\\Device\\NPF_{9C488612-D4CD-485C-9362-1603DCF1CDE6}"
)
if __name__ == "__main__":
  start_capture() 