function move(obj){
    var x = Math.trunc(Math.random()*1000)
    var y = Math.trunc(Math.random()*1000)
    console.log(x,y)
    document.getElementById("mole").style.margin=x,y
}