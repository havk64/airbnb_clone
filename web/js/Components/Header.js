import React from "react";
import ReactDOM from "react-dom";

class Logo extends React.Component {
	render() {
		const img = {
			height: "100px"
		}
		const src = "./static/Airbnb.png"
		const alt = "Airbnb Logo"
		return <img style={img} src={src} alt={alt} />
	}
}

class Header extends React.Component {
	render() {
		const header = {
			width		: "100%",
      			height		: "60px",
      			backgroundColor	: "#fff",
      			display		: "flex",
      			flexDirection	: "row",
      			alignItems	: "center",
      			justifyContent	: "space-between"
		}
		const rightDiv = {
      			width		: "200px",
      			height		: "100%",
      			backgroundColor	: "#F2F6F7"
		}
		
		return <header style={header}>
	    		<Logo />
	    		<div style={rightDiv}></div>
	    		</header>;
	}
}

export default Header;
