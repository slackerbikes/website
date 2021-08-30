import React from 'react';
import { BrowserRouter, Link, Route } from 'react-router-dom/cjs/react-router-dom.min';

class Nav extends React.Component {
    render() {
        return (
            <Link to="/">
            <div class="nav">
                <h1>Slacker Bikes</h1>
            </div>
            </Link>
        );
    }
}

export default Nav;