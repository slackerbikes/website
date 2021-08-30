import React from "react";
import {Helmet} from "react-helmet";

function Booking(props) {
   return (
        <div class="desc">
            <h1>Booking</h1>
            <h3>Please book your slot through our payment service. Please drop off your bike on the day of your booking, or before. If you're late please get in touch. <br /><br />We turnover bikes every week, and will notify you when it's ready.</h3>
            <img src="https://www.appointletcdn.com/loader/buttons/008DBD.png" data-appointlet-organization="slacker-bikes" class="booking-button" />
            <Helmet>
                <script src="https://www.appointletcdn.com/loader/loader.min.js" async="" defer=""></script>
            </Helmet>
            <h3>We have the following limits on services: </h3>
            <ul>
                <li>Full Service: 5 per Week</li>
                <li>Basic Service: 5 per Week</li>
                <li>Other Service (Gear, Chain, Brakes): 20 per Week</li>
            </ul>
            <h3>We take deposits to cover no shows</h3>
        </div>
    );   
}

export default Booking;