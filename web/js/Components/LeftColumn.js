import React from "react";
import ReactDOM from "react-dom";

const LeftColumn = React.createClass({
	render() {
		const columnStyle = {
			width		: "300px",
			height		: "100%",
			float		: "left",
			backgroundColor	: "#F2F6F7",
		}
		return (
			<div style={columnStyle}>
			</div>
		);
	}
});

export default LeftColumn;
