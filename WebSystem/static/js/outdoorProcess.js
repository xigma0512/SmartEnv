// 使用 fetch 從後端 API 獲取數據
fetch('/outdoorAPI/data')
    .then(response => response.json())
    .then(data => {
        document.getElementById("outdoor_current_temp").textContent = data.realTimeData[0];
        document.getElementById("outdoor_current_moist").textContent = data.realTimeData[1];
        document.getElementById("outdoor_current_pm25").textContent = data.realTimeData[2];
        createChart(data.history)
    })
    .catch(error => console.error('Error fetching data:', error));


function createChart(history) {

    const tempDatasets = {
        label: '溫度',
        data: history.temp,
        borderColor: 'rgb(0, 134, 11)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderWidth: 2
    }

    const moistDatasets = {
        label: '濕度',
        data: history.moist,
        borderColor: 'rgb(38, 96, 255)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderWidth: 2
    }

    const pmDataset = {
        label: 'PM2.5',
        data: history['pm2.5'],
        borderColor: 'rgb(38, 96, 255)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderWidth: 2
    }


    new Chart(
        document.getElementById('outdoor_temp_chart').getContext('2d'), {
        type: 'line',
        data: {
            labels: history.labels,
            datasets: [tempDatasets]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                }
            },
            scales: {
                x: { title: { display: true, text: '時間(小時)' } },
                y: { title: { display: true, text: '溫度(°C)' } }
            }
        }
    });

    new Chart(
        document.getElementById('outdoor_moist_chart').getContext('2d'), {
        type: 'line',
        data: {
            labels: history.labels,
            datasets: [moistDatasets]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                }
            },
            scales: {
                x: { title: { display: true, text: '時間(小時)' } },
                y: { title: { display: true, text: '濕度(%)' } }
            }
        }
    });

    new Chart(
        document.getElementById('outdoor_pm2.5_chart').getContext('2d'), {
        type: 'line',
        data: {
            labels: history.labels,
            datasets: [pmDataset]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                }
            },
            scales: {
                x: { title: { display: true, text: '時間(小時)' } },
                y: { title: { display: true, text: '濃度(μg/m3)' } }
            }
        }
    });
}