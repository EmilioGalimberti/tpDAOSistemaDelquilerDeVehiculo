// /sistema/static/js/charts.js

// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {

    // --- LÓGICA DE GRÁFICOS (CANVAS API) ---

    /**
     * Dibuja un gráfico de barras simple.
     */
    function drawBarChart() {
        const canvas = document.getElementById('barChart');
        // ¡Importante! Verificamos si el canvas existe en esta página
        if (!canvas || !canvas.getContext) {
            return; // No hacer nada si no encontramos el canvas
        }

        const ctx = canvas.getContext('2d');
        const data = [
            { label: 'Corolla', value: 52 },
            { label: 'Ranger', value: 35 },
            { label: 'Versa', value: 41 },
            { label: 'Onix', value: 28 },
        ];

        const canvasHeight = canvas.height;
        const canvasWidth = canvas.width;
        const barWidth = 40;
        const barMargin = 50;
        const chartHeight = canvasHeight - 40; // Espacio para etiquetas
        const maxValue = Math.max(...data.map(item => item.value));

        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Color de relleno
        ctx.fillStyle = '#3498db';
        ctx.font = '14px Arial';

        data.forEach((item, index) => {
            const barHeight = (item.value / maxValue) * chartHeight;
            const x = (index * (barWidth + barMargin)) + 60; // Posición X
            const y = canvasHeight - barHeight - 20; // Posición Y

            // Dibuja la barra
            ctx.fillRect(x, y, barWidth, barHeight);

            // Dibuja la etiqueta
            ctx.fillStyle = '#333';
            ctx.textAlign = 'center';
            ctx.fillText(item.label, x + barWidth / 2, canvasHeight - 5);
        });

        // Dibuja eje Y (simple)
        ctx.beginPath();
        ctx.moveTo(30, 10);
        ctx.lineTo(30, canvasHeight - 20);
        ctx.lineTo(canvasWidth - 10, canvasHeight - 20);
        ctx.strokeStyle = '#bdc3c7';
        ctx.stroke();
    }

    /**
     * Dibuja un gráfico de líneas simple.
     */
    function drawLineChart() {
        const canvas = document.getElementById('lineChart');
        // ¡Importante! Verificamos si el canvas existe en esta página
        if (!canvas || !canvas.getContext) {
            return; // No hacer nada si no encontramos el canvas
        }

        const ctx = canvas.getContext('2d');
        const data = [1200, 1900, 1500, 2100, 1800, 2400]; // Datos de facturación
        const labels = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'];

        const canvasHeight = canvas.height;
        const canvasWidth = canvas.width;
        const chartHeight = canvasHeight - 40;
        const chartWidth = canvasWidth - 40;
        const maxValue = Math.max(...data);
        const stepX = chartWidth / (data.length - 1);

        ctx.clearRect(0, 0, canvasWidth, canvasHeight);

        // Dibuja Ejes
        ctx.beginPath();
        ctx.moveTo(30, 10);
        ctx.lineTo(30, canvasHeight - 20);
        ctx.lineTo(canvasWidth - 10, canvasHeight - 20);
        ctx.strokeStyle = '#bdc3c7';
        ctx.stroke();

        // Dibuja la línea
        ctx.beginPath();
        ctx.moveTo(30, canvasHeight - 20 - (data[0] / maxValue) * chartHeight);
        ctx.strokeStyle = '#e74c3c';
        ctx.lineWidth = 3;

        data.forEach((value, index) => {
            if (index === 0) return;
            const x = (index * stepX) + 30;
            const y = canvasHeight - 20 - (value / maxValue) * chartHeight;
            ctx.lineTo(x, y);
        });
        ctx.stroke();

        // Dibuja puntos y etiquetas
        ctx.fillStyle = '#e74c3c';
        ctx.font = '12px Arial';
        data.forEach((value, index) => {
            const x = (index * stepX) + 30;
            const y = canvasHeight - 20 - (value / maxValue) * chartHeight;

            // Punto
            ctx.beginPath();
            ctx.arc(x, y, 5, 0, Math.PI * 2);
            ctx.fill();

            // Etiqueta X
            ctx.fillStyle = '#333';
            ctx.textAlign = 'center';
            ctx.fillText(labels[index], x, canvasHeight - 5);
        });
    }

    // Iniciar los gráficos
    drawBarChart();
    drawLineChart();

});