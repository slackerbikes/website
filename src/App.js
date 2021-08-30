import logo from './logo.svg';
import './App.css';
import About from './components/about.js'
import Tile from './components/tile'
import Nav from './components/nav'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom/cjs/react-router-dom.min';
import Menu from './menu'
import Certificates from './components/certificates';
import Booking from './components/booking';
import Gallery from './components/gallery';
import Group from './components/group';
import Pricing from './components/pricing';
import Reviews from './components/reviews';

function App() {
  return (
    <Router>
      <div className="App">
        <Nav />
        <div className="content">
          <Switch>
            <Route exact path="/website">
              <Menu />
            </Route>

            <Route path="/about">
              <About />
            </Route>

            <Route path="/booking">
              <Booking />
            </Route>

            <Route path="/certificates">
              <Certificates />
            </Route>

            <Route path="/gallery">
              <Gallery />
            </Route>

            <Route path="/group">
              <Group />
            </Route>

            <Route path="/pricing">
              <Pricing />
            </Route>

            <Route path="/reviews">
              <Reviews />
            </Route>
            
          </Switch>
        </div>
      </div>
      
    </Router>
  )
};

export default App;
