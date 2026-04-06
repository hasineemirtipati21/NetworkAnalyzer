import axios from "axios";

export const getData = async () => {
  return await axios.get("http://127.0.0.1:8000/data");
};