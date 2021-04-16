var count=0
var timer=0
function change() {
	var x = Math.floor(Math.random() * 256); // range is 0-255
	var y = Math.floor(Math.random() * 256);
	var z = Math.floor(Math.random() * 256);
	var thergb = "rgb(" + x + "," + y + "," + z + ")"; 
	console.log(thergb,document.body.style.background);
	document.body.style.background=thergb;
}
function move(obj){
    count += 1
    var x = Math.trunc(Math.random()*600)
    var y = Math.trunc(Math.random()*600)
    console.log(x,y)
    document.getElementById("mole").style.margin=x,y;
    document.getElementById("count").innerHTML='moles hits: '+count;
    change();
}