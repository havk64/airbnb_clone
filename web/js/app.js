import React from 'react';
import ReactDOM from 'react-dom';
import Header from './Components/Header.js';
import LeftColumn from './Components/LeftColumn.js';

ReactDOM.render(
		<div>
		<Header />
		<LeftColumn />
		</div>,
		document.getElementById('container')
	       );
