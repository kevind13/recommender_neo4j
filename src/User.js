import React from "react";
import "./User.css";
import Row from "./components/Row";
import request from "./request";
import Banner from "./components/Banner";

function User(props) {
	const id = props.match.params.id;
	return (
		<div className="User">
			<Banner />
			<Row
				title="Purchased products"
				fetchUrl={`${request.fetchProducts}${id}`}
			/>
			<Row
				title="Recommended products"
				fetchUrl={`${request.fetchRecommendations}${id}`}
			/>
		</div>
	);
}

export default User;
