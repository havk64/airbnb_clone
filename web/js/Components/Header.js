/* ===--------------------------------------------------------------===
 *	Header Zone for our web application
 *	Implements 'Header' and 'Logo' instances of React Component
 *
 *	by Alexandro de Oliveira, for Holberton School
 * ===---------------------------------------------------------------===	
 */
import React 	from "react";
import ReactDOM	from "react-dom";

const Logo = React.createClass({
	render() {
		const img = {
			height: "100px"
		}
		const src = "./static/Airbnb.png"
		const alt = "Airbnb Logo"
		return (
			<img style={img} src={src} alt={alt} />
		);
	}
});

const Header = React.createClass({
	render() {
		const header = {
			width		: "100%",
      			height		: "60px",
      			backgroundColor	: "#fff",
      			display		: "flex",
      			flexDirection	: "row",
      			alignItems	: "center",
      			justifyContent	: "space-between",
			borderBottom	: "2px solid #F2F6F7"
		}
		const rightDiv = {
      			width		: "200px",
      			height		: "100%",
      			backgroundColor	: "#F2F6F7"
		}
		
		return (
			<header style={header}>
	    		<Logo />
	    		<div style={rightDiv}></div>
	    		</header>
		);
	}
});

export default Header;
