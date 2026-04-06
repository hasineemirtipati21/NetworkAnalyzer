import pandas as pd
from metrics import calculate_metrics

def analyze_traffic():
    data = pd.read_csv("traffic_data.csv")
    data.columns = data.columns.str.strip()

    total_packets = len(data)

    # Convert Time
    data["Time"] = pd.to_numeric(data["Time"], errors="coerce")
    data["Time_sec"] = data["Time"].astype(int)

    # 📈 Traffic over time
    traffic = (
        data.groupby("Time_sec")
        .size()
        .reset_index(name="count")
        .tail(20)
    )

    traffic_data = [
        {"time": int(row["Time_sec"]), "packets": int(row["count"])}
        for _, row in traffic.iterrows()
    ]

    # 🥧 Protocol distribution
    protocol_dist = data["Protocol"].value_counts().to_dict()

    # 🌐 Top IPs
    top_ips = data["Source"].value_counts().head(5).to_dict()

    # 🚨 Suspicious
    suspicious = [
        {"ip": ip, "count": count}
        for ip, count in data["Source"].value_counts().items()
        if count > 300
    ]

    metrics = calculate_metrics(data)

    return {
        "total_packets": total_packets,
        "traffic_data": traffic_data,   # 👈 NEW
        "protocol_distribution": protocol_dist,
        "top_ips": top_ips,
        "suspicious": suspicious,
        "metrics": metrics
    }