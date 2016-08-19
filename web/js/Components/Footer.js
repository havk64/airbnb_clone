/* ===-----------------------------------------------------===
 *	Footer Zone for our web application
 *	Footer is an instance of a React Component
 *
 *	by Alexandro de Oliveira, for Holberton School
 * ===-----------------------------------------------------===	
 */
import React 	from 'react';
import ReactDOM from 'react-dom';

const Footer = React.createClass({
	render() {
		const footerStyle = {
			position	: "fixed",
			width		: "100%",
			height		: "40px",
			bottom		: "0px",
			backgroundColor	: "#fff",
			borderTop	: "2px solid #F2F6F7",
			textAlign	: "center"
		}
		return (
			<footer style={footerStyle}>
				&copy; Alexandro de Oliveira for Holberton School
			</footer>
		);
	}
});

export default Footer;

