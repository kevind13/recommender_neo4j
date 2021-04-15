import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
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

	const history = useHistory();

	return (
		<div className="row">
			<h2 className="row__title">{title}</h2>

			<div className="row__names">
				{values.map((item) => (
					<div
						className={isUser ? "row__name" : "row__nameProduct"}
						key={isUser ? item.id : item.product}
					>
						{isUser && (
							<img
								className="row__img"
								onClick={() => history.push(`/user/${item.id}`)}
								src={`https://ui-avatars.com/api/?name=${
									isUser ? item.id : item.product
								}&background=random&rounded=true&length=3&size=128`}
								alt={isUser ? item.id : item.product}
							/>
						)}
						<p className="row__string">
							{isUser ? item.id : item.product}
						</p>
					</div>
				))}
			</div>
		</div>
	);
}

export default Row;
