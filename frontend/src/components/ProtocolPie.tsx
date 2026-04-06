import { PieChart, Pie, Cell, Tooltip } from "recharts";

function ProtocolPie({ data }: any) {
  const chartData = Object.entries(data).map(([key, value]) => ({
    name: key,
    value
  }));

  return (
    <div>
      <h2>📊 Protocol Distribution</h2>
      <PieChart width={300} height={300}>
        <Pie data={chartData} dataKey="value" outerRadius={100}>
          {chartData.map((_, i) => (
            <Cell key={i} />
          ))}
        </Pie>
        <Tooltip />
      </PieChart>
    </div>
  );
}

export default ProtocolPie;