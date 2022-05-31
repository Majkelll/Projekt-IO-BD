function BMI() {
    var h=document.getElementById('h').value;
    var w=document.getElementById('w').value;
    var bmi=w/(h/100*h/100);
    var bmio=(bmi.toFixed(2));

    document.getElementById("result").innerHTML="Your BMI is " + bmio;
}
function CALORIES(){
  var h=document.getElementById('h').value;
  var w=document.getElementById('w').value;
  var w=document.getElementById('a').value;

  if (document.getElementById("male").checked) {
        S =  Math.round((9.99*w)+(6.25*h)-(4.92*a)+5)
    } else if (document.getElementById("female").checked) {
        S =  Math.round((9.99*w)+(6.25*h)-(4.92*a)-161)
    }
    var Calor =(S.toFixed());
    document.getElementById("result_2").innerHTML=Calor;
}