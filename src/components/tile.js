import React from 'react';

class Tile extends React.Component {
    render() {
        return (
            <div class="tile" id={this.props.id}>
                <h1>{this.props.title}</h1>
            </div>
        );
    }
}

export default Tile;