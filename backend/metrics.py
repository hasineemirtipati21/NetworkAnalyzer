import pandas as pd
import time

def calculate_metrics(data):

    if data.empty:
        return None

    data.columns = data.columns.str.strip()

    # Convert columns safely
    data["Time"] = pd.to_numeric(data["Time"], errors="coerce")
    data["Length"] = pd.to_numeric(data.get("Length", 0), errors="coerce").fillna(0)

    total_packets = len(data)
    total_bytes = data["Length"].sum()

    # -------------------------------
    # ⚡ REAL-TIME PACKET RATE (LAST 5 SECONDS)
    # -------------------------------
    current_time = time.time()

    recent = data[data["Time"] > (current_time - 5)]

    duration = 5  # fixed window

    packet_rate = len(recent) / duration

    # -------------------------------
    # 📡 BANDWIDTH (REAL-TIME)
    # -------------------------------
    recent_bytes = recent["Length"].sum()
    bandwidth = recent_bytes / duration

    # -------------------------------
    # 📦 THROUGHPUT
    # -------------------------------
    throughput = bandwidth

    # -------------------------------
    # 📉 PACKET LOSS (simple estimate)
    # -------------------------------
    packets_sent = total_packets + 10
    packet_loss = (packets_sent - total_packets) / packets_sent

    # -------------------------------
    # 🚨 ANOMALY SCORE
    # -------------------------------
    anomaly_score = abs(packet_rate - 50) / 50

    return {
        "total_packets": total_packets,
        "packet_rate": round(packet_rate, 2),
        "bandwidth": round(bandwidth, 2),
        "throughput": round(throughput, 2),
        "packet_loss": round(packet_loss, 4),
        "anomaly_score": round(anomaly_score, 2)
    }