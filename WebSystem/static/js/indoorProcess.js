// 使用 fetch 從後端 API 獲取數據
fetch('/indoorAPI/data')
    .then(response => response.json())
    .then(data => {
        document.getElementById("indoor_current_temp").textContent = data.realTimeData[0];
        document.getElementById("indoor_current_moist").textContent = data.realTimeData[1];
        document.getElementById("indoor_suggestion").textContent = getControl(data.control);
        createChart(data.history)
    })
    .catch(error => console.error('Error fetching data:', error));

function getControl(control) {
    let ret = 0
    switch (control[0]) {
        case 0: ret = "無"; break;
        case 1: ret = "開啟窗戶"; break;
        case 2: ret = "開啟冷氣"; break;
        case 3: ret = "開啟暖氣"; break;
    }
    ret += " | ";
    switch (control[1]) {
        case 0: ret += "無"; break;
        case 1: ret += "開啟除濕機"; break;
        case 2: ret += "開啟加濕器"; break;
    }
    return ret
}

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

    new Chart(
        document.getElementById('indoor_temp_chart').getContext('2d'), {
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
        document.getElementById('indoor_moist_chart').getContext('2d'), {
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
}