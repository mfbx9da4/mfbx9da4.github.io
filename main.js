// Checkers in pure-js; Author: David Adler; Date: 12/02/2013

// Inital positions of checkers and squares
var INIT_CHECKERS = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0]];
var INIT_SQUARES = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1]];

// -----Checkers and sqaures config-----
// 1 red, 2 black
var CHECKER_COLORS = {1: 'firebrick', 2: '#313131'};
var CHECKER_BORDER = {width: 5, color: '#000'};
// 0 white, 1 black, 2 active
var SQUARE_COLORS = {0: '#ccc', 1: '#fff', 2: 'steelblue'};
// the int representing the checker of the other color
var ANTI_CHECKER = {1: 2, 2: 1};
// 1 can move bottom right or bottom left. (second value in array need to check if checer can jump)
// 2 can move top right or top left relative to self.
var CHECKER_MOVES = {1: [{row: 1, col: 1}, {row: 1, col: -1}], 
                     2: [{row: -1, col: 1}, {row: -1, col: -1}]};

// -----Dimensions config------
var SQUARE_SIZE = 50;
var BOARD_DIM = INIT_SQUARES.length;
var BOARD_WIDTH = SQUARE_SIZE * BOARD_DIM;
var BOARD_HEIGHT = SQUARE_SIZE * BOARD_DIM;

function deep_copy(array) {
    var out = Array(array.length);
    for (var i = 0; i < array.length; i++) {
        out[i] = array[i].slice();
    }
    return out;
}

function Board (canvas) {
    var board = this;
    board.can = canvas;
    board.ctx = canvas.getContext('2d');

    document.body.addEventListener("mouseup", board.onUp().mouse, false);
    board.can.addEventListener("touchend", board.onUp().touch, false);

    board.active = [];
    board.checkers = deep_copy(INIT_CHECKERS);
    board.squares = deep_copy(INIT_SQUARES);

}

Board.prototype.find_legal_moves = function(pos) {
    var board = this;
    var checker = board.checkers[pos.row][pos.col];
    // anti means a checker of opposite color
    var anti = ANTI_CHECKER[checker];

    var moves = CHECKER_MOVES[checker];

    if (moves !== undefined) {

        for (var i = 0; i < moves.length; i++) {
            var delta = moves[i];

            // new trail position
            var mv = {};
            mv.row = pos.row + delta.row;
            mv.col = pos.col + delta.col;

            if (board.checkers[mv.row][mv.col] === 0) {
                // adjacent empty
                board.active.push({row: mv.row, col: mv.col});

            } else if (board.checkers[mv.row][mv.col] == anti &&
                       board.checkers[mv.row*2][mv.col*2] === 0) {
                // can jump adjacent
                board.active.push({row: mv.row*2, col: mv.col*2});
            }

            if (board.active.length) {
                // also animate square beneath checker if it has legal moves
                board.active.push({row: pos.row, col: pos.col});
            }

        }
    }
};

Board.prototype.onUp = function(e) {
    var board = this;
    return {
        mouse: function(e) {
            var coords = {};
            coords.x = e.pageX - board.can.offsetLeft;
            coords.y = e.pageY - board.can.offsetTop;
            var pos = board.translateCoords(coords);
            board.selectChecker(pos);
        },
        touch: function(e) {
            e.preventDefault();
            var coords = {};
            coords.x = e.targetTouches[0].pageX - board.can.offsetLeft;
            coords.y = e.targetTouches[0].pageY - board.can.offsetTop;
            var pos = board.translateCoords(coords);
            board.selectChecker(pos);
        }
    };
};

Board.prototype.translateCoords = function(coords) {
    var board = this;
    var pos = {};
    pos.col = parseInt(coords.x / SQUARE_SIZE);
    pos.row = parseInt(coords.y / SQUARE_SIZE);
    return pos;
};

Board.prototype.selectChecker = function(pos) {
    var board = this;
    board.reset_animated();
    board.show_legal(pos);
};

Board.prototype.reset_animated = function() {
    var board = this;
    for (var i = 0; i < board.active.length; i++) {
        var pos = board.active[i];
        board.squares[pos.row][pos.col] = INIT_SQUARES[pos.row][pos.col];
    }
    board.active = [];
    board.draw();
};

Board.prototype.show_legal = function(pos) {
    var board = this;
    board.find_legal_moves(pos);
    for (var i = 0; i < board.active.length; i++) {
        pos = board.active[i];
        board.squares[pos.row][pos.col] = 2;
    }
    board.draw();
};

Board.prototype.draw = function() {
    var board = this;
    board.draw_board();
    board.draw_checkers();
};

Board.prototype.draw_board = function() {
    var board = this;
    for (var row = 0; row < BOARD_DIM; row++) {
        for (var col = 0; col < BOARD_DIM; col++) {
            var square = board.squares[row][col];

            var x = col * SQUARE_SIZE;
            var y = row * SQUARE_SIZE;

            board.ctx.fillStyle = SQUARE_COLORS[square];

            board.ctx.fillRect(x, y, SQUARE_SIZE, SQUARE_SIZE);
        }
    }
};

Board.prototype.draw_checkers = function() {
    var board = this;
    var radius = (SQUARE_SIZE / 2) - CHECKER_BORDER.width;

    for (var row = 0; row < BOARD_DIM; row++) {
        for (var col = 0; col < BOARD_DIM; col++) {
            var checker = board.checkers[row][col];
            if (checker !== 0) {
                // If there is a checker in the square

                // get center of square
                var x = col * SQUARE_SIZE;
                var y = row * SQUARE_SIZE;
                var center_x = x + (SQUARE_SIZE / 2);
                var center_y = y + (SQUARE_SIZE / 2);

                board.ctx.beginPath();
                board.ctx.arc(center_x, center_y, radius, 0, 2 * Math.PI, false);
                board.ctx.fillStyle = CHECKER_COLORS[checker];
                board.ctx.fill();
                board.ctx.lineWidth = CHECKER_BORDER.width;
                board.ctx.strokeStyle = CHECKER_BORDER.color;
                board.ctx.stroke();
            }
        }
    }
};

function initCanvas() {
    var container = document.getElementById('game-container');
    var canvas = document.createElement('canvas');
    canvas.width = BOARD_WIDTH;
    canvas.height = BOARD_HEIGHT;
    container.appendChild(canvas);
    return canvas;
}


function main() {
    // Create canvas
    var canvas = initCanvas();

    var board = new Board(canvas);
    board.draw();

}

main();