import React, { useState } from "react";
import axios from "axios";
import "./QueryInterface.css";
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
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [getlog, setData] = useState([]);
  const [selectedOption, setSelectedOption] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [datetime, setDateTime] = useState(false);
  const handleOptionChange = (e) => {
    if (e.target.value === "timestamp") setDateTime(true);
    else {
      setDateTime(false);
    }
    setSelectedOption(e.target.value);
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };
  const handleStartDateChange = (e) => {
    setStartDate(e.target.value);
  };

  const handleEndDateChange = (e) => {
    setEndDate(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (selectedOption === "") {
      alert("Select any option !");
      return;
    }
    if (searchTerm === "") {
      alert("Enter Search Term !");
      return;
    }
    console.log(startDate + " : " + endDate);
    try {
      var response = "";
      if (selectedOption === "timestamp") {
        response = await axios({
          method: "get",
          url: `http://localhost:3000/query-interface?filter=${selectedOption}&start=${startDate}&end=${endDate}`,
        });
      } else {
        response = await axios({
          method: "get",
          url: `http://localhost:3000/query-interface?search=${searchTerm}&filter=${selectedOption}`,
        });
      }
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
          {datetime === true ? (
            <div>
              <label className="from">From :</label>
              <input
                type="text"
                value={startDate}
                onChange={handleStartDateChange}
              />
              <br />
              <label className="to">To &nbsp;&nbsp;:</label>
              <input
                type="text"
                value={endDate}
                onChange={handleEndDateChange}
              />
            </div>
          ) : (
            <p></p>
          )}
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
