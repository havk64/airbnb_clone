/* ===----------------------------------------------------------===
 *	Content Zone for our web application
 *	Implements 'Content' as an instance of a React Component
 *
 *	by Alexandro de Oliveira, for Holberton School
 * ===----------------------------------------------------------===	
 */
import React 	from 'react';
import ReactDOM from 'react-dom';

const Content = React.createClass({
	render() {
		const contentStyle = {
			height	: "100%",
			float	: "left"
		}
		return (
			<div style={contentStyle}>
			</div>
		);
	}
});

export default Content;
