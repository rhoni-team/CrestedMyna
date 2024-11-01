// mapping/js/ajax_calls/ajax_mapping.js

export function getAllPoints() {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/get-records/',
            type: "GET",
            dataType: "json",
            success: (data) => {
                console.log("records in ajax", data.records);
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
                console.log("records in ajax", data.countries);
                resolve(data.countries);  // Resolve the Promise with the data
            },
            error: (error) => {
                console.log(error);
                reject(error);  // Reject the Promise with the error
            }
        });
    });
}
