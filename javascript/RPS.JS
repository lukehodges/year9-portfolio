const prompt = require('prompt-sync')();
console.log('ROCK PAPER SCISSORS')
const name = prompt('rock paper or SCISSORS (r,p,s)> ').toLowerCase();
items = Array('r','p','s');
var item = items[Math.floor(Math.random() * items.length)];
console.log('computer chose '+item)
console.log('you chose '+name)
if (item==name){console.log('draw go again');}

// setting values for pc
let comp
if (item=='r'){comp = 0}
else if (item=='p'){comp = 1}
else if (item=='s'){comp = 2}

// setting values for player
let play
if (name=='r'){play = 0}
else if (name=='p'){play = 1}
else if (name=='s'){play = 2}


if (!(comp) && play == 1){console.log('you crush the rock and WIN');}// rock vs paper
else if (!(play) && comp == 1){console.log('pc crushes the rock and you LOSE');}// vice versa
else if (comp< play){console.log('you snip the paper in half and WIN')}// paper vs scissors
else if (comp> play){console.log('pc snips the paper in half and you LOSE')}// vice cersa
else if(!(play)&& comp == 3){console.log('you smash the scissors with your rock and WIN')}// scissors vs rock
else if(!(comp)&& play == 3){console.log('pc smashes the scissors with its rock and you LOSE')}// vice versa
