const Departure = (props) => {

    const destination = props.destination || '???';
    const departureTime = props.departureTime || '??:??';

    return (
        <div className="departure">
            <h1 id="destination">{destination}</h1>
            <p id="departureTime">{departureTime}</p>
        </div>
    )
}

export default Departure;