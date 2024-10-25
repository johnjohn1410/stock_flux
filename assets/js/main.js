function loadContent(page) {
    fetch('./assets/js/pageConfigs.json')  // Caminho para o JSON com as configurações
        .then(response => response.json())
        .then(configs => {
            const config = configs[page];
            if (config) {
                fetch(page)
                    .then(response => response.text())
                    .then(data => {
                        document.querySelector('.main-content').innerHTML = data;
                        runPageSpecificScript(config);
                    })
                    .catch(error => console.error('Erro ao carregar a página:', error));
            } else {
                console.error('Configuração não encontrada para a página:', page);
            }
        })
        .catch(error => console.error('Erro ao carregar as configurações:', error));
}

async function search(page) {
    try {
        const response = await fetch('./assets/js/pageConfigs.json');  // Caminho para o JSON com as configurações
        const configs = await response.json();
        
        const config = configs[page];
        if (config) {
            const pageResponse = await fetch(page);
            const data = await pageResponse.text();
            
            const filtros = config.filters.map(filtro => {
                return `${filtro.paramName}=${document.getElementById(filtro.id).value}`;
            }).join('&');
            
            const tableBody = document.getElementById(`${config.tableName}-tbody`);
            await populateGrid(config.tableName, filtros, tableBody);  // Alterado a ordem dos parâmetros
        } else {
            console.error('Configuração não encontrada para a página:', page);
        }
    } catch (error) {
        console.error('Erro ao carregar as configurações ou a página:', error);
    }
}

function runPageSpecificScript(config) {
    const { tableName } = config;
    const tbody = document.getElementById(`${tableName}-tbody`);

    if (tbody) {
        populateGrid(tableName, tbody);
    }
}

async function populateGrid(table, tbody) {
    let url = `http://127.0.0.1:5000/api/${table}`;

    try {
        const response = await fetch(url);
        const itens = await response.json();
        tbody.innerHTML = ''; // Limpa o tbody

        itens.forEach(item => {
            const row = document.createElement('tr');

            Object.values(item).forEach(value => {
                const cell = document.createElement('td');
                cell.textContent = value;
                row.appendChild(cell);
            });

            tbody.appendChild(row);
        });
    } catch (error) {
        console.error('Erro ao buscar os dados:', error);
    }
}

window.onload = function() {
    var ctx1 = document.getElementById('chart1').getContext('2d');
    var chart1 = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
            datasets: [{
                label: 'Amoxicilina',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    var ctx2 = document.getElementById('chart2').getContext('2d');
    var chart2 = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
            datasets: [{
                label: 'Ibuprofeno',
                data: [3, 2, 2, 6, 7, 8],
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    };