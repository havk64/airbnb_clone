/* ===-----------------------------------------------------===
 *	Application entry point
 *	Rendering React Components
 *
 *	by Alexandro de Oliveira, for Holberton School
 * ===-----------------------------------------------------===	
 */
import React 		from 'react';
import ReactDOM		from 'react-dom';
import Header		from './Components/Header.js';
import LeftColumn	from './Components/LeftColumn.js';
import Content		from './Components/Content.js';
import Footer		from './Components/Footer.js';

const divStyle 	= { height: "100%" };
const mainStyle	= { height: "100%", marginBottom: "40px" };

ReactDOM.render(
		<div style={divStyle}>
			<Header />
			<main style={mainStyle}>
				<LeftColumn />
				<Content />
			</main>
			<Footer />
		</div>,
		document.getElementById('container')
	);
