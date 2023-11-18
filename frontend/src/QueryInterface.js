import React, { useState } from "react";
import axios from "axios";
import "./queryinterface.css";
import LogTable from "./LogTable";

const options = [
  "level",
  "message",
  "resourceId",
  "timestamp",
  "traceId",
  "spanId",
  "commit",
  "parentResourceId",
];
const QueryInterface = () => {
  const [getlog, setData] = useState([]);
  const [selectedOption, setSelectedOption] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const handleOptionChange = (e) => {
    setSelectedOption(e.target.value);
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios({
        method: "get",
        url: `http://localhost:3000/query-interface?search=${searchTerm}&filter=${selectedOption}`,
      });
      console.log(response.data.logs);
      console.log("WOrking");
      setData(response.data.logs);
      getlog.map((logz, index) => {
        console.log(logz[0]);
      });
      console.log(getlog);
      // console.log(response.data.logs[0][3]);
    } catch (error) {
      console.error("API Error:", error);
    }
  };

  return (
    <div className="container">
      <div className="searchcontiner">
        <form onSubmit={handleSubmit}>
          <select value={selectedOption} onChange={handleOptionChange}>
            <option value="">Select an option</option>
            {options.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
          <input
            type="text"
            placeholder="Search..."
            value={searchTerm}
            onChange={handleSearchChange}
          />
          <button type="submit">Submit</button>
        </form>
      </div>

      <div className="error-table">
        <LogTable errorData={getlog} />
      </div>
    </div>
  );
};

export default QueryInterface;
