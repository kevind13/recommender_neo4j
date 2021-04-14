import React from "react";
import "./Users.css";
import Row from "./components/Row";
import request from "./request";
import Banner from "./components/Banner";

function Users() {
	return (
		<div className="App">
			{/* Nav */}
			<Banner />
			<Row title="Users" fetchUrl={request.fetchUsers} isUser />
		</div>
	);
}

export default Users;
