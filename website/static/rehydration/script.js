/*Glass*/
var plus = document.getElementById("plus");
var minus = document.getElementById("minus");
var glass = document.getElementById("glass");
var water = document.getElementById("water");
var litersNum = 1;

plus.onclick = addWater;

function addWater(e) {
  litersNum = litersNum + 0.5;
  if (litersNum > 4) {
    litersNum = 4;
  }
  water.style.transform = "scale(" + litersNum + ")";
  if (litersNum > 1) {
    water.style.borderRadius = "50%";
    water.style.bottom = "-80px";
  }
  axios.post("http://127.0.0.1:5000/hydration");
}

minus.onclick = removeWater;

function removeWater(e) {
  litersNum = litersNum - 0.5;
  if (litersNum <= 0.5) {
    water.style.borderRadius = "0px";
    water.style.bottom = "-150px";
    litersNum = 0.5;
  }
  if (litersNum <= 1) {
    water.style.borderRadius = "0px";
    water.style.bottom = "-150px";
  }

  water.style.transform = "scale(" + litersNum + ")";
}
/*Glass*/

/*Week Month*/
var week = document.getElementById("week");
var month = document.getElementById("month");

var chartImg = document.getElementById("chart-img");

week.onclick = getGraph;
month.onclick = getGraph;

function getGraph(e) {
  week.classList.remove("chart-button_active");
  month.classList.remove("chart-button_active");

  e.target.classList.add("chart-button_active");
  if (e.target.id == "week") {
    chartImg.src = "../../static/assets/images/week.png";
    console.log(chartImg);
  } else {
    chartImg.src = "../../static/assets/images/month.png";
  }
}

/*Week Month*/
