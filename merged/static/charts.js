document.addEventListener("DOMContentLoaded", function () {
    fetch("/data")
        .then(response => response.json())
        .then(data => updateCharts(data));

    function updateCharts(data) {
        // *Donut Chart (Passed vs Failed)*
        new Chart(document.getElementById("donutChart").getContext("2d"), {
            type: "doughnut",
            data: {
                labels: ["Passed", "Failed"],
                datasets: [{
                    data: [data.passed, data.failed],
                    backgroundColor: ["#4CAF50", "#F44336"]
                }]
            },
            options: {
                cutout: "80%",  // Makes the ring thinner
                plugins: {
                    legend: { position: "bottom" }
                }
            }
        });

        // *Gauge Chart (Test Completion Progress)*
        new Chart(document.getElementById("gaugeChart").getContext("2d"), {
            type: "doughnut",
            data: {
                labels: ["Completed", "Remaining"],
                datasets: [{
                    data: [data.progress, 100 - data.progress], // Example: Progress % 
                    backgroundColor: ["#2196F3", "#E0E0E0"]
                }]
            },
            options: {
                cutout: "85%",  // Makes the gauge thinner
                rotation: -90,  // Starts from bottom
                circumference: 180,  // Makes it a half-doughnut (gauge)
                plugins: {
                    legend: { display: false }
                }
            }
        });

        // *Area Chart (Tests Executed Over Time)*
        new Chart(document.getElementById("areaChart").getContext("2d"), {
            type: "line",
            data: {
                labels: data.dates,
                datasets: [{
                    label: "Tests Executed",
                    data: data.tests_executed,
                    backgroundColor: "rgba(76, 175, 80, 0.3)", // Light green fill
                    borderColor: "#4CAF50",
                    fill: true
                }]
            },
            options: {
                responsive: true,
                tension: 0.4, // Smooth curves
                plugins: {
                    legend: { position: "top" }
                }
            }
        });
    }
});