import { useEffect, useState } from "react";
import { getData } from "./services/api";
import Dashboard from "./pages/Dashboard";

function App() {
  const [data, setData] = useState<any>(null);

  const fetchData = async () => {
    const res = await getData();
    setData(res.data);
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 2000);
    return () => clearInterval(interval);
  }, []);

  if (!data) return <h2>Loading...</h2>;

  return <Dashboard data={data} />;
}

export default App;