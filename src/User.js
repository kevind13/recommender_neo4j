import React from "react";
import "./User.css";
import Row from "./Row";
import request from "./request";

function User() {
	return (
		<div className="App">
			<h1>User information 🔬 </h1>
			<Row title="Purchased products" fetchUrl={request.fetchProducts} />
			<Row
				title="Recommended products"
				fetchUrl={request.fetchRecommendations}
			/>
		</div>
	);
}

export default User;
