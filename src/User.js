import React from "react";
import "./User.css";
import Row from "./components/Row";
import request from "./request";
import Banner from "./components/Banner";

function User() {
	return (
		<div className="User">
			<Banner />
			<Row title="Purchased products" fetchUrl={request.fetchProducts} />
			<Row
				title="Recommended products"
				fetchUrl={request.fetchRecommendations}
			/>
		</div>
	);
}

export default User;
