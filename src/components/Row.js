import React, { useState, useEffect } from "react";
import axios from "../axios";
import "./Row.css";

function Row({ title, fetchUrl, isUser }) {
	const [values, setValues] = useState([]);

	useEffect(() => {
		async function fetchData() {
			const res = await axios.get(fetchUrl);
			setValues(res.data);
			return res;
		}
		fetchData();
	}, [fetchUrl]);

	return (
		<div className="row">
			<h2>{title}</h2>

			<div className="row__names">
				{values.map((item) => (
					<p
						className="row__name"
						key={isUser ? item.id : item.product}
					>
						{isUser ? item.id : item.product}
					</p>
				))}
			</div>
		</div>
	);
}

export default Row;
