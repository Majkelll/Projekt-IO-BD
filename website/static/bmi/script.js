var canvas = document.createElement("canvas");
var div = document.createElement("div");

div.appendChild(canvas);
div.style.padding = "0px 200px 0px 200px"
canvas.id = "BMIChart";

document.body.appendChild(div);

const ctx = document.getElementById('BMIChart').getContext('2d');

axios.post('http://127.0.0.1:5000/bmi/data')
  .then((response) => {
    console.log(response.data);
    const bmi = response.data;
    createChart(bmi);
  })
  .catch((e) => {
    console.log(e);
  });

const createData = (bmi) => bmi.map((data) => {
  return {
    'x': data.date,
    'y': data.height
  }
});

const createChart = (bmi) => {
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      datasets: [{
        label: 'BMI',
        data: createData(bmi),
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
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
}