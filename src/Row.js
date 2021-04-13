import React, { useState, useEffect } from "react";

function Row({ title, fetchUrl }) {
	const [values, setValues] = useState([]);

	useEffect(() => {
		async function fetchData() {
			const res = await fetch(`http://localhost:5000/users`);
			console.log(res);
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
