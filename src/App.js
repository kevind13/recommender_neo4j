import React from "react";
import "./App.css";
import Row from "./Row";
import request from "./request";
function App() {
	return (
		<div className="App">
			<h1>Best recommender 🚀 </h1>
			<Row title="Users" fetchUrl={request.fetchUsers} />
		</div>
	);
}

export default App;
