import React from 'react';
import ReactDOM from 'react-dom';

const Footer = React.createClass({
	render() {
		const footerStyle = {
			position	: "fixed",
			width		: "100%",
			height		: "40px",
			bottom		: "0px",
			backgroundColor	: "#fff",
			borderTop	: "1px solid gray",
			textAlign	: "center"
		}
		return (
			<footer style={footerStyle}>
				&copy; Alexandro de Oliveira for Holberton School
			</footer>
		       )
	}
});

export default Footer;

