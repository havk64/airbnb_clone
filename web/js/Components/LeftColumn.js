import React from "react";
import ReactDOM from "react-dom";

class LeftColumn extends React.Component {
	render() {
		const columnStyle = {
			width		: "300px",
			height		: "100%",
			float		: "left",
			backgroundColor	: "#aaa",
		}
		return  <div style={columnStyle}>
			</div>;
	}
}

export default LeftColumn;