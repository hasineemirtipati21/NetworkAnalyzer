import StatsCard from "../components/StatsCard";
import ProtocolPie from "../components/ProtocolPie";
import TrafficChart from "../components/TrafficChart";
import TopIPsBar from "../components/TopIPsBar";

function Dashboard({ data }: any) {
  return (
    <div style={{ padding: "20px" }}>
      <h1>📡 Network Traffic Dashboard</h1>

      <div style={{ display: "flex", gap: "20px" }}>
        <StatsCard title="Total Packets" value={data.total_packets} />
        <StatsCard title="Packet Rate" value={data.metrics.packet_rate.toFixed(2)} />
      </div>

      <TrafficChart data={data.traffic_data} />
      <ProtocolPie data={data.protocol_distribution} />
      <TopIPsBar data={data.top_ips} />

      <h2>🚨 Suspicious Traffic</h2>
      {data.suspicious.length === 0 ? (
        <p>No suspicious activity</p>
      ) : (
        data.suspicious.map((s: any, i: number) => (
          <p key={i} style={{ color: "red" }}>
            {s.ip} ({s.count} packets)
          </p>
        ))
      )}
    </div>
  );
}

export default Dashboard;