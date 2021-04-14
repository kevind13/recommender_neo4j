import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
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
					<div
						className={`row__nameProduct ${isUser && "row__name"}`}
						key={isUser ? item.id : item.product}
					>
						<p>{isUser ? item.id : item.product}</p>
						{isUser && (
							<Link to={`/user/${item.id}`} className="row__link">
								Go
							</Link>
						)}
					</div>
				))}
			</div>
		</div>
	);
}

export default Row;
