function StatsCard({ title, value }: any) {
  return (
    <div style={{
      background: "#111",
      color: "#fff",
      padding: "15px",
      borderRadius: "10px",
      width: "200px"
    }}>
      <h4>{title}</h4>
      <h2>{value}</h2>
    </div>
  );
}

export default StatsCard;