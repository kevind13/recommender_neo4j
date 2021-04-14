import React from "react";
import "./App.css";
import Row from "./Row";
import request from "./request";
import Banner from "./Banner";

function App() {
	return (
		<div className="App">
			{/* Nav */}
			<Banner />
			<Row title="Users" fetchUrl={request.fetchUsers} isUser />
		</div>
	);
}

export default App;
