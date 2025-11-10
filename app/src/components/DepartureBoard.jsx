import { React, useState } from 'react';
import config from '../../config.json';

const DepartureBoard = () => {
    const [departures, setDepartures] = useState([]);
    const stationCode = "GLC";

    const fetchDepartures = async () => {
        try {
            const response = await fetch(
                `https://api1.raildata.org.uk/1010-live-departure-board-dep1_2/LDBWS/api/20220120/GetDepartureBoard/${stationCode}`, {
                    method: 'GET',
                    headers: {
                        'x-apikey': `${config.API_KEY}`,
                }
        });
            const data = await response.json();
            let services = [];
            console.log('Fetched departures data:', data);
            for (const service of data.trainServices) {
                console.log(`Service to ${service.destination[0].locationName} at ${service.std} is ${service.status}`);
                services.push({destination: service.destination[0].locationName, time: service.std});
            }
            console.log('Processed services:', services);
            setDepartures(services);
            console.log(departures)
        } catch (error) {
            console.error('Error fetching departures:', error);
        }
    };

    return (
        <div>
            <h1>Departure Board</h1>
            <button onClick={fetchDepartures}>Load Departures</button>
            <ul>
                {departures.map((departure, index) => (
                    <li key={index}>
                        {departure.time} - {departure.destination}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default DepartureBoard;