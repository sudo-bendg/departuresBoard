const Departure = (props) => {

    const destination = props.destination || '???';
    const departureTime = props.departureTime || '??:??';

    return (
        <div className="departure">
            <h1 id="destination">{destination}</h1>
            <h1 id="departureTime">{departureTime}</h1>
        </div>
    )
}

export default Departure;