import React from 'react';
import ReactDOM from 'react-dom';
import Header from './Components/Header.js';
import LeftColumn from './Components/LeftColumn.js';
import Content from './Components/Content.js';
import Footer from './Components/Footer.js';

const divStyle = { height: "100%", border: "1px solid yellow" };

ReactDOM.render(
		<div style={divStyle}>
			<Header />
			<main>
				<LeftColumn />
				<Content />
			</main>
			<Footer />
		</div>,
		document.getElementById('container')
	       );
