// mapping/js/ajax_calls/ajax_mapping.js

export function getAllPoints() {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/get-records/',
            type: "GET",
            dataType: "json",
            success: (data) => {
                resolve(data.records);  // Resolve the Promise with the data
            },
            error: (error) => {
                console.log(error);
                reject(error);  // Reject the Promise with the error
            }
        });
    });
}

export function getCountriesPolygonsWithACRecords() {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/get-countries-polygons/',
            type: "GET",
            dataType: "json",
            success: (data) => {
                resolve(data.countries);  // Resolve the Promise with the data
            },
            error: (error) => {
                console.log(error);
                reject(error);  // Reject the Promise with the error
            }
        });
    });
}

export async function getCountryDetails(countryCode) {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: `/get-country-details/`,
            type: "GET",
            dataType: "json",
            data: { country_code: countryCode },
            success: (data) => {
                resolve(data.country_details);  // Resolve the Promise with the data
            },
            error: (error) => {
                console.log(error);
                reject(error);  // Reject the Promise with the error
            }
        });
    });
}
