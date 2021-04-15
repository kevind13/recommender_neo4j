import React, { Fragment } from "react";
import { HashRouter, Route, Switch } from "react-router-dom";
import Users from "./Users";
import User from "./User";
import Error from "./components/Error";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

function App() {
	return (
		<HashRouter basename="/">
			<Fragment>
				<Navbar />
				<Switch>
					<Route exact path="/" component={Users} />
					<Route exact path="/user/:id" component={User} />
					<Route component={Error} />
				</Switch>
				<Footer />
			</Fragment>
		</HashRouter>
	);
}

export default App;
