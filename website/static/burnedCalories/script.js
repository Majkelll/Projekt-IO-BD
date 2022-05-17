var ageSlider = document.getElementById("age");
var ageOutput = document.getElementById("age-output");
ageOutput.innerHTML = ageSlider.value;

ageSlider.oninput = function () {
  ageOutput.innerHTML = this.value;
};

var heightSlider = document.getElementById("height");
var heightOutput = document.getElementById("height-output");
heightOutput.innerHTML = heightSlider.value;

heightSlider.oninput = function () {
  heightOutput.innerHTML = this.value;
};

var weightSlider = document.getElementById("weight");
var weightOutput = document.getElementById("weight-output");
weightOutput.innerHTML = weightSlider.value;

weightSlider.oninput = function () {
  weightOutput.innerHTML = this.value;
};
