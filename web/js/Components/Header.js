import React from "react";
import ReactDOM from "react-dom";

class Header extends React.Component {
  render() {
    const container = {
      width		: "100%",
      height		: "60px",
      backgroundColor	: "#fff",
      display		: "flex",
      flexDirection	: "row",
      alignItems	: "center",
      justifyContent	: "space-between"
    };
    const rightDiv = {
      width		: "200px",
      height		: "100%",
      color		: "#eee"
    }
    const img 	= {
      height 		: "100px"
    }
    return (<div style={container}>
	    <img style={img} src="./static/Airbnb.png" alt="Airbnb Logo" />
	    <div style={rightDiv}></div>
	    </div>);
  }
}

export default Header;
