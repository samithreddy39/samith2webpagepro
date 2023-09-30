
document.addEventListener("DOMContentLoaded", function () {
    function searchrollnumber() {

        const rollNumber = document.getElementById("rollNumber").value;
    
        // Send a GET request to your Flask server
        fetch(`/search?rollNumber=${rollNumber}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Check if the response contains the "result" key
                if ('result' in data) {
                    const result = data.result;
                    document.getElementById("result").innerHTML = `Result: ${result}`;
                } else {
                    document.getElementById("result").innerHTML = 'Error: Invalid response format';
                }
            })
            .catch(error => {
                document.getElementById("result").innerHTML = `Error: ${error.message}`;
            });
    }

});