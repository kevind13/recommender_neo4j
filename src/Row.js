import React, { useState, useEffect } from "react";
import axios from "./axios";
function Row({ title, fetchUrl }) {
	const [values, setValues] = useState([]);

	useEffect(() => {
		async function fetchData() {
			const res = await axios.get(fetchUrl);
			console.log(res.data);
			return res;
		}
		fetchData();
	}, []);
	return (
		<div>
			<h2>Row</h2>
		</div>
	);
}

export default Row;
