import { BrowserRouter, Link, Route } from 'react-router-dom/cjs/react-router-dom.min';
import Tile from './components/tile'
// import About from './components/about.js'

function Menu() {
    return (
        <div className="menu">
            <div class="tile-container">
                <Link to="/booking">
                    <Tile title="Booking" id="booking"/>     
                </Link> 

                <Link to="/pricing">
                    <Tile title="Pricing" id="pricing"/>
                </Link> 

                <Link to="/about">
                    <Tile title="About" id="about"/>
                </Link> 

                <Link to="/gallery">
                    <Tile title="Gallery" id="gallery"/>
                </Link> 

                <Link to="/reviews">
                    <Tile title="Reviews" id="reviews"/>
                </Link> 

                <Link to="/certificates">
                    <Tile title="Certificates" id="certificates"/>
                </Link> 

                <Link to="/group">
                    <Tile title="Group Rides" id="grouprides"/>
                </Link> 
            </div>
        </div>
    );
}

export default Menu;