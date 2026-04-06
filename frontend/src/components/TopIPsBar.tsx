import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

function TopIPsBar({ data }: any) {
  const chartData = Object.entries(data).map(([ip, count]) => ({
    ip,
    count
  }));

  return (
    <div>
      <h2>🌐 Top IP Traffic</h2>
      <BarChart width={500} height={250} data={chartData}>
        <XAxis dataKey="ip" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" />
      </BarChart>
    </div>
  );
}

export default TopIPsBar;