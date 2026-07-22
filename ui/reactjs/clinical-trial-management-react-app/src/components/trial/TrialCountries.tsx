import React from "react";

import "../../styles/TrialCountries.css"

interface TrialCountriesProps {
    countries: string[];
    onCountriesChange: (countries: string[]) => void;
}

const availableCountries = [
    "India",
    "United States",
    "Germany",
    "United Kingdom",
    "Canada",
    "Australia",
    "France",
    "Japan",
    "Singapore",
    "Brazil",
    "South Korea",
    "China"
];

const TrialCountries: React.FC<TrialCountriesProps> = ({
    countries,
    onCountriesChange,
}) => {

    const handleChange = (
        event: React.ChangeEvent<HTMLSelectElement>
    ) => {

        const values = Array.from(
            event.target.selectedOptions,
            option => option.value
        );

        onCountriesChange(values);
    };

    return (

        <div className="card">

            <div className="card-header">

                <h2>Participating Countries</h2>

            </div>

            <div className="card-body">

                <label>

                    Select Countries

                </label>

                <select

                    multiple

                    size={8}

                    value={countries}

                    onChange={handleChange}

                    className="country-select"

                >

                    {

                        availableCountries.map(country => (

                            <option

                                key={country}

                                value={country}

                            >

                                {country}

                            </option>

                        ))

                    }

                </select>

                <div className="selected-list">

                    <h4>Selected Countries</h4>

                    {

                        countries.length === 0

                        ?

                        <p>No countries selected.</p>

                        :

                        countries.map(country => (

                            <span
                                key={country}
                                className="country-chip"
                            >
                                {country}
                            </span>

                        ))

                    }

                </div>

            </div>

        </div>

    );

};

export default TrialCountries;