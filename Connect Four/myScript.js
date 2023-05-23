var player1 = prompt("Player One: Enter Your Name, you will be Blue");
var player1Color = 'rgb(86, 151, 255)';

var player2 = prompt("Player Two: Enter Your Name, YOu will be Red");
var player2Color = 'rgb(237, 45, 73)';

var game_on = true;
var table = $('table tr');


function reportWin(rowNum, colNum){
    console.log("You won")
}


function changeColor(rowIndex, colIndex, changeColor){
    return  table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}