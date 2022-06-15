if (document.cookie) {
  var canvas = document.createElement("canvas");
  var div = document.createElement("div");

  div.appendChild(canvas);
  div.style.padding = "0px 200px 0px 200px";
  canvas.id = "BMIChart";

  document.body.appendChild(div);

  const ctx = document.getElementById("BMIChart").getContext("2d");

  axios
    .post("http://127.0.0.1:5000/bmi/data")
    .then((response) => {
      console.log(response.data);
      const bmi = response.data;
      getOneDataFromDay(bmi);
      createChart(bmi);
    })
    .catch((e) => {
      console.log(e);
    });

  function removeTime(date = new Date()) {
    return new Date(date.getFullYear(), date.getMonth(), date.getDate());
  }

  function getOneDataFromDay(response) {
    var data = {};
    response
      .slice()
      .reverse()
      .forEach((el) => {
        var date = Date.parse(el.date);
        var dateWithoutTime = removeTime(new Date(date));
        if (!(dateWithoutTime in data)) {
          data = {
            ...data,
            [dateWithoutTime]: {
              height: el.height,
              weight: el.weight,
            },
          };
        }
        if (Object.keys(data).length >= 7) {
          return data;
        }
      });
    return data;
  }

  function minDate(dates) {
    return new Date(
      Math.min(
        ...dates.map((element) => {
          return new Date(element);
        })
      )
    );
  }

  const week = {
    0: "Niedziela",
    1: "Poniedziałek",
    2: "Wtorek",
    3: "Środa",
    4: "Czwartek",
    5: "Piątek",
    6: "Sobota",
  };

  function createChartData(data) {
    var chartData = [];

    var numberOfKeys = Object.keys(data).length;

    for (let i = 0; i < numberOfKeys; i++) {
      var key = minDate(Object.keys(data));
      var obj = data[key];
      delete data[key];
      chartData.push({
        x: week[key.getDay()],
        y: obj.weight / (((obj.height / 100) * obj.height) / 100),
      });
    }

    return chartData;
  }

  const createChart = (bmi) => {
    const myChart = new Chart(ctx, {
      type: "line",
      data: {
        datasets: [
          {
            label: "BMI",
            data: createChartData(getOneDataFromDay(bmi)),
            fill: false,
            borderColor: "rgb(75, 192, 192)",
            tension: 0.1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  };
}
