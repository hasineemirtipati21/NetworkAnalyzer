import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function TrafficChart({ data }: any) {
  return (
    <div>
      <h2>📈 Traffic Over Time</h2>
      <LineChart width={500} height={250} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="packets" />
      </LineChart>
    </div>
  );
}

export default TrafficChart;