import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

export const Navbar = () => (
	<nav className="navbar">
		<Link className="navbar__name" to="/">
			Home
		</Link>
	</nav>
);
