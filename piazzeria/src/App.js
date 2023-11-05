import PizzaSidebar from "./PizzaSidebar.js";
import Post from "./Post.js";
import "./App.css";
import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]);
  const [isRAQOpen, setIsRAQOpen] = useState(false);

  useEffect(() => {
    fetch("http://localhost:8080/members")
      .then((response) => response.json())
      .then((data) => {
        // message = 'Loading'
        // once data is retrieved
        // message = data.message
        setData(data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="App">
      {data.members ? (
        data.members.map((person, index) => <div key={index}>{person}</div>)
      ) : (
        <></>
      )}
      <PizzaSidebar isRAQOpen={isRAQOpen} setIsRAQOpen={setIsRAQOpen} />
      <Post isRAQOpen={isRAQOpen} setIsRAQOpen={setIsRAQOpen} />
    </div>
  );
}

export default App;
