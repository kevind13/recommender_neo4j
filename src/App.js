import React, { Fragment } from "react";
import { HashRouter, Route, Switch } from "react-router-dom";
import Users from "./Users";
import User from "./User";
import Error from "./Error";
import { Navbar } from "./Navbar";

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
			</Fragment>
		</HashRouter>
	);
}

export default App;
