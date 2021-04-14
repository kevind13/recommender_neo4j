import React from "react";
import "./Banner.css";

function Banner() {
	return (
		<header
			className="banner"
			style={{
				backgroundSize: "cover",
				backgroundImage: `url(https://git.io/JO3Ye)`,
				backgroundPosition: "center center",
			}}
		>
			<div className="banner__contents">
				<h1 className="banner__title">Best recommender 🚀 </h1>
				<h1 className="banner__description">
					Not very good looking, but powerful! 😅
				</h1>
			</div>
		</header>
	);
}

export default Banner;
