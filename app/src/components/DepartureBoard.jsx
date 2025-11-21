import { React, useState } from 'react';
import config from '../../config.json';
import Departure from './Departure';

const DepartureBoard = () => {
    const [departures, setDepartures] = useState([]);
    const stationCode = "KWN";

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
            let count = 0
            for (const service of data.trainServices) {
                if (count >= 5) break;
                console.log(`Service to ${service.destination[0].locationName} at ${service.std} is ${service.status}`);
                services.push({destination: service.destination[0].locationName, time: service.std});
                count++;
            }
            console.log('Processed services:', services);
            setDepartures(services);
            console.log(departures)
        } catch (error) {
            console.error('Error fetching departures:', error);
        }
    };

    fetchDepartures();

    return (
        <div className='departuresBoard'>
            <ul style={{ listStyleType: 'none' }}>
                {departures.map((departure, index) => (
                    <div key={index}>
                        <Departure destination={departure.destination} departureTime={departure.time} />
                    </div>
                ))}
            </ul>
        </div>
    );
}

export default DepartureBoard;