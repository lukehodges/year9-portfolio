var count=0
var timer=0
function move(obj){
    count += 1
    var x = Math.trunc(Math.random()*600)
    var y = Math.trunc(Math.random()*600)
    console.log(x,y)
    document.getElementById("mole").style.margin=x,y
    document.getElementById("count").innerHTML='moles hits: '+count;
}