// Restart Game Button


var restart = document.querySelector("#b");



// Grab All Squares
var squares = document.querySelectorAll('td');



// Clear All Squares

function clearBoard(){
    for (var index = 0; index < squares.length; index++) {
        squares[index].textContent = '';
        
        
    }
}


restart.addEventListener('click', clearBoard);

// Check The Square Marker

function changeMarker(){
    if(this.textContent ===''){
        this.textContent = 'X';
    }else if (this.textContent === 'X'){
        this.textContent = 'O';

    }else {
        this.textContent = '';
    }
}

for (var index = 0; index < squares.length; index++) {
    squares[index].addEventListener('click', changeMarker)
    
}

// Add Event Listeners To All The Squares
