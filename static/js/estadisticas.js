// Importa las bibliotecas necesarias para los gráficos
import Chart from 'chart.js/auto';

// Datos para los gráficos
const barChartData = {
    labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    datasets: [{
        label: 'Noticias agregadas',
        data: [10, 25, 15, 30, 20],
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

const pieChartData = {
    labels: ['Rojo', 'Verde', 'Azul'],
    datasets: [{
        data: [20, 30, 50],
        backgroundColor: ['red', 'green', 'blue']
    }]
};

// Crear gráfico de barras
const barChart = new Chart(document.getElementById('barChart'), {
    type: 'bar',
    data: barChartData,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Crear gráfico circular (pastel)
const pieChart = new Chart(document.getElementById('pieChart'), {
    type: 'pie',
    data: pieChartData
});
