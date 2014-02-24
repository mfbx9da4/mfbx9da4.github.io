// Checkers in pure-js; Author: David Adler; Date: 12/02/2013

/*
*                                                         *
*   Inital positions of checkers and squares              *  
*                                                         *
*/
var INIT_CHECKERS = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0]];
// for testing purposes, a more varied grid
// var INIT_CHECKERS = [
//         [0, 1, 0, 1, 0, 1, 0, 1],
//         [1, 0, 1, 0, 1, 0, 1, 0],
//         [0, 1, 0, 1, 0, 1, 0, 1],
//         [0, 0, 0, 0, 3, 0, 0, 0],
//         [0, 0, 0, 0, 0, 4, 0, 0],
//         [2, 0, 2, 0, 2, 0, 0, 0],
//         [0, 2, 0, 2, 0, 2, 0, 2],
//         [2, 0, 2, 0, 2, 0, 2, 0]];
var INIT_SQUARES = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1]];


/*
*                                  *
*   Dimensions config              *  
*                                  *
*/
var SQUARE_SIZE = 50;
var BOARD_DIM = INIT_SQUARES.length;
var BOARD_WIDTH = SQUARE_SIZE * BOARD_DIM;
var BOARD_HEIGHT = SQUARE_SIZE * BOARD_DIM;
var INFO_WIDTH = SQUARE_SIZE * 2;


/*
*                                           *
*   Checkers and sqaures config             *  
*                                           *
*/
Utils = {};
Utils.deep_copy = function(array) {
    var out = Array(array.length);
    for (var i = 0; i < array.length; i++) {
        out[i] = array[i].slice();
    }
    return out;
}

// 0 black, 1 white, 2 active
var SQUARE_COLORS = {0: '#ccc', 1: '#fff', 2: 'steelblue'};

var teams = {
    1: {name: 'RED', 
        score: 0,
        color: 'firebrick'
    }, 
    2: {name: 'BLACK', 
        score: 0,
        color: '#313131'
    }
};

// "type ids" of queens
var queens = [3, 4];

// checker pieces config
var pieces = {
    1: {name: 'red pawn',
        is_queen: false,
        color: 'firebrick',
        moves: [{row: 1, col: 1}, {row: 1, col: -1}],
        border: {width: 5, color: '#000'},
        type: 1,
        anti: 2,
        team: 1
    },
    2: {name: 'black pawn',
        is_queen: false,
        color: '#313131',
        moves: [{row: -1, col: 1}, {row: -1, col: -1}],
        border: {width: 5, color: '#000'},
        type: 2,
        anti: 1,
        team: 2
    },
    3: {name: 'red queen',
        is_queen: true,
        color: 'firebrick',
        moves: [{row: 1, col: 1}, {row: 1, col: -1}, 
                {row: -1, col: 1}, {row: -1, col: -1}],
        trigger_row: BOARD_DIM - 1,
        border: {width: 5, color: 'gold'},
        type: 3,
        anti: 2,
        team: 1
    },
    4: {name: 'black queen',
        is_queen: true,
        color: '#313131',
        moves: [{row: 1, col: 1}, {row: 1, col: -1}, 
                {row: -1, col: 1}, {row: -1, col: -1}],
        trigger_row: 0,        
        border: {width: 5, color: 'gold'},
        type: 4,
        anti: 1,
        team: 2
    }
};

/*
*                   *
*   Utils           *  
*                   *
*/
Utils = {};
Utils.deep_copy = function(array) {
    var out = Array(array.length);
    for (var i = 0; i < array.length; i++) {
        out[i] = array[i].slice();
    }
    return out;
}

/*
*                   *
*   A checker piece *  
*                   *
*/
function Piece(config, pos) {
    var piece = this;
    piece.type = config.type;
    piece.name = config.name;
    piece.is_queen = config.is_queen;
    piece.color = config.color;
    piece.moves = config.moves;
    piece.trigger_row = config.trigger_row;
    piece.border = config.border;
    piece.anti =  config.anti;
    piece.team =  config.team;
    piece.radius = SQUARE_SIZE / 2;


    // variables for animation
    piece.is_animating = false;
    piece.animation_duration = 200;
    piece.start_time = null;
    piece.current_dir = {};
    piece.src = {};
    piece.des = {};
    piece.pos = pos;
    piece.loc = piece.translatePosToCoords(pos);
}

Piece.prototype.translatePosToCoords = function(pos) {
    var board = this;
    var coords = {};
    coords.x = pos.col * SQUARE_SIZE;
    coords.y = pos.row * SQUARE_SIZE;
    return coords;
};

Piece.prototype.move = function(src, des) {
    var piece = this;

    piece.start_animation(src, des);

    board.checker_objects[piece.des.row][piece.des.col] = piece;
    board.checker_objects[piece.src.row][piece.src.col] = undefined;

};

Piece.prototype.start_animation = function(src, des) {
    var piece = this;
    piece.start_time = new Date().getTime();
    piece.is_animating = true;

    piece.setSrcAndDes(src, des);

    piece.current_dir = piece.get_direction(piece.des, piece.src);
    var distance = piece.get_total_distance();
    piece.speed = distance / piece.animation_duration;
};

Piece.prototype.setSrcAndDes = function(src, des) {
    var piece = this;

    piece.src = src;
    var coords =  piece.translatePosToCoords(src);
    piece.src.x = coords.x;
    piece.src.y = coords.y;
    
    piece.des = des;
    coords = piece.translatePosToCoords(des);
    piece.des.x = coords.x;
    piece.des.y = coords.y;
};

Piece.prototype.get_direction = function(src, des) {
    var direction = {};
    direction.x = (src.x - des.x) > 0 ? 1 : (src.x - des.x) < 0 ? -1 : 0;
    direction.y = (src.y - des.y) > 0 ? 1 : (src.y - des.y) < 0 ? -1 : 0;
    return direction;
};

Piece.prototype.get_total_distance = function() {
    var piece = this;
    var delta = {};
    delta.x = piece.des.x - piece.src.x;
    delta.y = piece.des.y - piece.src.y;
    return Math.sqrt((delta.x * delta.x) + (delta.y * delta.y));
};

Piece.prototype.update_loc = function(board) {
    var piece = this;

    var now = new Date().getTime();
    var elapsed = now - piece.start_time;
    if(piece.is_animating) {
        piece.loc.x = piece.src.x + (piece.current_dir.x * piece.speed * elapsed);
        piece.loc.y = piece.src.y + (piece.current_dir.y * piece.speed * elapsed);
    }

    piece.check_if_finished_animation(board);
};

Piece.prototype.check_if_finished_animation = function(board) {
    var piece = this;
    if (piece.current_dir.x === 1) {
        if (piece.loc.x > piece.des.x) {
            piece.finished_animation(board);
        }
    } else if (piece.current_dir.x === -1) {
        if (piece.loc.x < piece.des.x) {
            piece.finished_animation(board);
        }
    }
};

Piece.prototype.finished_animation = function(board) {
    var piece = this;
    piece.current_dir = null;
    piece.start_time = null;
    piece.is_animating = false;

    piece.loc.x = piece.des.x;        
    piece.loc.y = piece.des.y;        

    piece.src = {};
    piece.des = {};

    if (!board.computer_team) {
        board.screen_locked = false;
    }
};

Piece.prototype.draw = function(board) {
    var piece = this;

    if (piece.is_animating) {
        piece.update_loc(board);
    }

    var center_x = piece.loc.x + (SQUARE_SIZE / 2);
    var center_y = piece.loc.y + (SQUARE_SIZE / 2);
    var radius = piece.radius - piece.border.width;

    board.ctx.beginPath();
    board.ctx.arc(center_x, center_y, radius, 0, 2 * Math.PI, false);
    board.ctx.fillStyle = piece.color;
    board.ctx.fill();
    board.ctx.lineWidth = piece.border.width;
    board.ctx.strokeStyle = piece.border.color;
    board.ctx.stroke();
};

/*
*                   *
*   The board       *  
*                   *
*/
function Board (canvas, is_playing_computer) {
    var board = this;
    board.can = canvas;
    board.ctx = canvas.getContext('2d');
    board.computer_team = is_playing_computer ? 1 : 0;

    board.can.addEventListener("mouseup", board.onUp().mouse, false);
    board.can.addEventListener("touchstart", board.onUp().touch, false);

    board.available_positions = [];
    board.checker_objects = board.init_checkers();
    board.squares = Utils.deep_copy(INIT_SQUARES);
    board.selected_pos = null;
    board.who_to_play = 1;
    board.winner = null;
    board.switch_player();
    board.screen_locked = false;

}

Board.prototype.init_checkers = function() {
    var board = this;
    var checker_objects = Array(INIT_CHECKERS.length);
    for (var i = 0; i < INIT_CHECKERS.length; i ++) {
        checker_objects[i] = Array(INIT_CHECKERS[i].length);
        for (var j = 0; j < INIT_CHECKERS[i].length; j ++) {
            var type = INIT_CHECKERS[i][j];
            if (type !== 0) {
                var pos = {row: i, col:j};
                checker_objects[i][j] = new Piece(pieces[type], pos);
            }
        }
    }
    return checker_objects;
};

Board.prototype.find_legal_moves = function(pos) {
    var board = this;
    if (pos.row >= 0 && pos.row < BOARD_DIM) {
        var checker_piece = board.checker_objects[pos.row][pos.col];
        if (checker_piece !== undefined && checker_piece.team === board.who_to_play) {
            // if user selected a checker and it is this color to play 
            var anti = checker_piece.anti;
            var moves = checker_piece.moves;
            for (var i = 0; i < moves.length; i++) {
                var delta = moves[i];
                // adjacent position
                var adj = {row: pos.row + delta.row, 
                           col: pos.col + delta.col};
                // jump pos
                var jump = {row: pos.row + (delta.row * 2),
                            col: pos.col + (delta.col * 2)};
                
                if (board.position_in_board(adj) && board.position_is_empty(adj)) {
                    // adjacent empty
                    board.available_positions.push(adj);
                    if (checker_piece.is_queen) {
                        // get sequential empty cells
                        var empty_cells = board.find_empty_cells_in_direction(adj, delta);
                        if (empty_cells.length) {
                            board.available_positions = board.available_positions.concat(empty_cells);

                        }
                        board.find_long_distance_jump(delta, jump, anti);
                    }
                } else if (board.can_jump_adjacent(adj, jump, anti)) {
                    board.available_positions.push(jump);
                }

            }
            if (board.available_positions.length) {
                // also animate square beneath checker if it has legal moves
                board.available_positions.push(pos);
                board.selected_pos = pos;
                board.selected_pos.team = checker_piece.team;
                return board.available_positions;
            }
        }
    }
    return [];
};

Board.prototype.find_long_distance_jump = function(delta, jump, anti) {
    var board = this;
    // find long distance jump
    var last_empty = board.available_positions.slice(-1)[0];
    var last_adj = {row: last_empty.row + (delta.row),
                    col: last_empty.col + (delta.col)};
    jump = {row: last_empty.row + (delta.row * 2),
                col: last_empty.col + (delta.col * 2)};
    if (board.can_jump_adjacent(last_adj, jump, anti)) {
        board.available_positions.push(jump);
    }
};

Board.prototype.find_empty_cells_in_direction = function(start, delta) {
    // delta is direction
    var board = this;
    var empty_cells = [];
    var des = {row: start.row + delta.row,
               col: start.col + delta.col};

    while (board.position_in_board(des) && 
           board.position_is_empty(des)) {

            empty_cells.push({row: des.row, col: des.col});
        
            des.row = des.row + delta.row;
            des.col = des.col + delta.col;
    }

    return empty_cells;
};

Board.prototype.position_in_board = function(pos) {
    var cond = (pos.row < BOARD_DIM && pos.col < BOARD_DIM && pos.row >= 0 && pos.col >= 0);
    return cond;
};

Board.prototype.position_is_empty = function(pos) {
    var board = this;
    var cond = (board.checker_objects[pos.row][pos.col] === undefined);
    return cond;
};

Board.prototype.can_jump_adjacent = function(adj, jump, anti) {
    var board = this;
    if (board.position_in_board(adj) && board.position_in_board(jump)) {
        if (board.position_is_empty(jump)) {
            var adjacent_checker = board.checker_objects[adj.row][adj.col];
            return (adjacent_checker !== undefined &&
                    adjacent_checker.team === anti &&
                    board.checker_objects[jump.row][jump.col] === undefined);
            
        }
        
    }
};

Board.prototype.find_jump_moves = function(pos) {
    var board = this;
    var checker_piece = board.checker_objects[pos.row][pos.col];
    var anti = checker_piece.anti;
    var moves = checker_piece.moves;

    if (moves !== undefined && checker_piece.team === board.who_to_play) {
        // if it is this color to play
        for (var i = 0; i < moves.length; i++) {
            var delta = moves[i];

            // new trial position
            var adj = {row: pos.row + delta.row, 
                       col: pos.col + delta.col};

            // jump pos
            var jump = {row: pos.row + (delta.row * 2),
                        col: pos.col + (delta.col * 2)};
            if (board.can_jump_adjacent(adj, jump, anti)) {
                board.available_positions.push({row: jump.row, col: jump.col});
            }


        }
        if (board.available_positions.length) {
            board.selected_pos = pos;
            board.selected_pos.team = checker_piece.team;
            return board.available_positions;
        }
    }
    return [];
};

Board.prototype.find_a_checker_to_jump = function() {
    var board = this;
    for (var i = 0; i < BOARD_DIM; i++) {
        for (var j = 0; j < BOARD_DIM; j++) {
            var checker = board.checker_objects[i][j];
            if (checker !== undefined) {
                var pos = {row: i, col: j};
                board.selected_pos = pos;
                board.selected_pos = board.computer_team;
                if (checker.team === board.computer_team) {
                    var moves = board.find_jump_moves(pos);
                    if (moves.length) {
                        return moves[0];
                    }
                }
            }
        }
    }
};

Board.prototype.find_a_checker_to_move = function() {
    var board = this;
    for (var i = 0; i < BOARD_DIM; i++) {
        for (var j = 0; j < BOARD_DIM; j++) {
            var checker = board.checker_objects[i][j];
            if (checker !== undefined) {
                var pos = {row: i, col: j};
                board.selected_pos = pos;
                board.selected_pos = board.computer_team;
                if (checker.team === board.computer_team) {
                    var moves = board.find_legal_moves(pos);
                    if (moves.length) {
                        return moves[0];
                    }
                }
            }
        }
    }
};

Board.prototype.computer_play = function() {
    var board = this;
    board.screen_locked = true;
    board.reset_animated();
    var movement = board.find_a_checker_to_jump();
    if (!movement) {
        movement = board.find_a_checker_to_move();
    }
    board.move(movement);
    board.screen_locked = false;
};

Board.prototype.onUp = function(e) {
    var board = this;
    return {
        mouse: function(e) {
            if (!board.screen_locked) {
                var coords = {};
                coords.x = e.pageX - board.can.offsetLeft;
                coords.y = e.pageY - board.can.offsetTop;
                var pos = board.translateCoordsToPos(coords);
                board.selectSquare(pos);
            }
        },
        touch: function(e) {
            e.preventDefault();
            if (!board.screen_locked) {
                var coords = {};
                coords.x = e.targetTouches[0].pageX - board.can.offsetLeft;
                coords.y = e.targetTouches[0].pageY - board.can.offsetTop;
                var pos = board.translateCoordsToPos(coords);
                board.selectSquare(pos);
            }
        }
    };
};

Board.prototype.translateCoordsToPos = function(coords) {
    var board = this;
    var pos = {};
    pos.col = parseInt(coords.x / SQUARE_SIZE);
    pos.row = parseInt(coords.y / SQUARE_SIZE);
    return pos;
};

Board.prototype.selectSquare = function(pos) {
    var board = this;
    if (board.selected_pos) {
        // if there already is a checker selected
        if (pos.row === board.selected_pos.row && 
            pos.col === board.selected_pos.col) {
            // if reselect the selected_pos, deselect it
            board.selected_pos = null;
            board.reset_animated();
        } else {
            for (var i = 0; i < board.available_positions.length; i++) {
                var animated = board.available_positions[i];
                if (pos.row === animated.row && pos.col === animated.col) {
                    // if selected a valid new dest
                    if (board.must_jump) {
                        board.must_jump = false;
                    }
                    return board.move(pos);
                }
            }
            if (!board.must_jump) {
                // user chose to move a different checker
                board.selectChecker(pos);
            }
        }
    } else {
        // no checker selected
        board.selectChecker(pos);
    }
};

Board.prototype.selectChecker = function(pos) {
    var board = this;
    board.reset_animated();
    board.find_legal_moves(pos);
    board.show_legal(pos);
};

Board.prototype.move = function(pos) {
    var board = this;
    var switch_player;
    var reset_animated;
    // Source and destination positions
    var src = board.selected_pos;
    var des = pos;

    // make the move
    board.animate_move(src, des);

    if (board.jumped_piece(src, des, pieces[src.team].anti)) {
        // if jumping rm intermediate checker
        board.updateScore(board.selected_pos.team);
        board.remove_intermediate_piece(src, des);
        board.reset_animated();
        var legal_moves = board.find_jump_moves(des);
        if (legal_moves.length) {
            // if can do second jump
            board.selected_pos = des;
            board.must_jump = true;
        } else {
            // can not do second jump
            switch_player = true;
            reset_animated = true;
        }
    } else {
        // did not jump
        switch_player = true;
        reset_animated = true;
    }

    if (!src.is_queen) {
        // check if has become a queen
        for (var i = 0; i < queens.length; i++) {
            var queen = pieces[queens[i]];
            if (des.row === queen.trigger_row && src.team === queen.team) {
                // make queen
                var new_queen = new Piece(queen, des);
                board.checker_objects[des.row][des.col] = new_queen;
                switch_player = true;
                reset_animated = true;
            }
        }
    }
    if (board.must_jump && board.computer_team !== board.selected_pos.team) {return board.show_legal();}
    if (board.must_jump && board.computer_team) {return board.computer_play();}
    if (switch_player) {board.switch_player();}
    if (reset_animated){board.reset_animated();}
};

Board.prototype.game_over = function() {
    var board = this;
    board.ctx.fillStyle = "rgba(87, 101, 86, 0.75)";
    board.ctx.fillRect(0, 0, board.can.width, board.can.height);
    board.ctx.fillStyle = "white";
    board.ctx.font = "16px humor";
    board.ctx.fillText("Game over. The winner was " + board.winner.name, 100, 100);
};

Board.prototype.jumped_piece = function(src, des, anti) {
    var board = this;
    var delta = board.get_distance(src, des);
    var inter = board.get_intermediate_position(src, des);
    if (Math.abs(delta.row) > 1) {
        var inter_piece = board.checker_objects[inter.row][inter.col];
        if (inter_piece !== undefined &&
            inter_piece.team === anti) {
            return true;
        }
    }
};

Board.prototype.get_distance = function(src, des) {
    var dist = {};
    dist.row = des.row - src.row;
    dist.col = des.col - src.col;
    return dist;
};

Board.prototype.get_delta = function(src, des) {
    var delta = {};
    delta.row = (des.row - src.row) / Math.abs(des.row - src.row);
    delta.col = (des.col - src.col) / Math.abs(des.col - src.col);
    return delta;
};

Board.prototype.get_intermediate_position = function(src, des) {
    var board = this;
    var inter = {};
    var delta = board.get_delta(src, des);
    inter.row = des.row - (delta.row);
    inter.col = des.col - (delta.col);
    return inter;
};

Board.prototype.remove_intermediate_piece = function(src, des) {
    var board = this;
    var inter = board.get_intermediate_position(src, des);
    board.checker_objects[inter.row][inter.col] = undefined;
};

Board.prototype.updateScore = function(team) {
    var board = this;
    teams[team].score ++;
    document.querySelector('#score' + team).innerText = teams[team].score;
    for (var i in teams) {
        if (teams[i].score == 12) {
            board.winner = teams[i];
            return board.game_over();
        }
    }
};

Board.prototype.switch_player = function() {
    var board = this;
    board.who_to_play = pieces[board.who_to_play].anti;
    var name = teams[board.who_to_play].name;
    document.querySelector('#whos-turn-to-play b').innerHTML = name;
    var color = pieces[board.who_to_play].color;
    document.getElementById('whos-turn-to-play').style.backgroundColor = color;
    if (board.who_to_play === board.computer_team) {
        board.computer_play();
    }
};

Board.prototype.reset_animated = function() {
    var board = this;
    for (var i = 0; i < board.available_positions.length; i++) {
        var pos = board.available_positions[i];
        board.squares[pos.row][pos.col] = INIT_SQUARES[pos.row][pos.col];
    }
    board.available_positions = [];
    board.draw();
};

Board.prototype.show_legal = function(pos) {
    var board = this;
    for (var i = 0; i < board.available_positions.length; i++) {
        pos = board.available_positions[i];
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
    var radius = (SQUARE_SIZE / 2) - pieces[1].border.width;

    for (var row = 0; row < BOARD_DIM; row++) {
        for (var col = 0; col < BOARD_DIM; col++) {
            var checker = board.checker_objects[row][col];
            if (checker) {
                checker.draw(board);
            }
        }
    }
};

Board.prototype.animate_move = function(src, des) {
    var board = this;
    if (board.position_in_board(src)) {
        board.checker_objects[src.row][src.col].move(src, des);
    
    }
};

function initCanvas() {
    // container
    var container = document.getElementById('checkers-game-container');
    container.style.width = (BOARD_WIDTH + INFO_WIDTH + 4) + 'px';
    container.style.height = BOARD_HEIGHT + 'px';
    container.style.margin = '30px auto';
    container.style.boxShadow = '0px 0px 30px 2px #888';
    container.style.border = '1px solid #888';
    container.style.backgroundColor = 'rgb(153, 153, 153)';

    // canvas
    var canvas = document.createElement('canvas');
    canvas.width = BOARD_WIDTH;
    canvas.height = BOARD_HEIGHT;
    canvas.style.float = 'left';
    container.appendChild(canvas);

    return canvas;
}

function initInfoDiv() {
    var container = document.getElementById('checkers-game-container');

    // info div
    var info_div = document.createElement('div');
    info_div.id = 'checkers-game-info-div';
    info_div.style.fontFamily = 'humor, Arial';
    info_div.style.fontSize = '17px';
    info_div.style.backgroundColor = '#999';
    info_div.style.borderLeft = 'black solid 4px';
    info_div.style.width = SQUARE_SIZE * 2 + 'px';
    info_div.style.height = BOARD_HEIGHT + 'px';
    info_div.style.float = 'left';
    info_div.style.color = 'white';

    // whos turn to play
    var whos_turn_to_play = document.createElement('div');
    whos_turn_to_play.id = 'whos-turn-to-play';
    whos_turn_to_play.innerHTML = "<p><b></b> to play</p>";
    whos_turn_to_play.style.margin = '8px 8px';
    whos_turn_to_play.style.padding = '8px 8px';
    whos_turn_to_play.style.borderRadius = '8px';
    whos_turn_to_play.style.opacity = '1';
    whos_turn_to_play.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';

    // score
    var score = document.createElement('div');

    var score1 = document.createElement('div');
    score1.style.backgroundColor = pieces[1].color;
    score1.style.padding = '8px 8px';
    score1.style.margin = '70px 10px';
    score1.style.borderRadius = "4px";
    score1.style.float = 'left';
    score1.id = "score1";
    score1.innerText = '0';
    score.appendChild(score1);

    var score2 = document.createElement('div');
    score2.style.backgroundColor = pieces[2].color;
    score2.style.padding = '8px 8px';
    score2.style.margin = '70px 10px';
    score2.style.borderRadius = "4px";
    score2.style.float = 'left';
    score2.id = "score2";
    score2.innerText = '0';
    score.appendChild(score2);

    info_div.appendChild(whos_turn_to_play);
    info_div.appendChild(score);

    container.appendChild(info_div);
    return info_div;
}

function initGameDialog(canvas) {
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = teams[1].color;
    ctx.fillRect(0, 0, canvas.width, canvas.height / 2);
    ctx.fillStyle = "white";
    ctx.font = "16px humor";
    ctx.fillText("Click here to play computer", 100, 100);

    ctx.fillStyle = teams[2].color;
    ctx.fillRect(0, canvas.height /2, canvas.width, canvas.height /2);
    ctx.fillStyle = "white";
    ctx.font = "16px humor";
    ctx.fillText("Click here to play a friend", 100, 100 + canvas.height/2);

    canvas.addEventListener('mouseup', function handler(e) {
        var coords = {};
        coords.x = e.pageX - canvas.offsetLeft;
        coords.y = e.pageY - canvas.offsetTop;
        if (coords.y < canvas.height/2) {
            canvas.removeEventListener('mouseup', handler, true);
            startGame(canvas, true);
        } else {
            canvas.removeEventListener('mouseup', handler, true);
            startGame(canvas, false);
        }
    }, true);
}


function startGame(canvas, is_playing_computer) {
    var info_div = initInfoDiv();
    window.board = new Board(canvas, is_playing_computer);
    var start_time = new Date().getTime();

    (function animloop(){
        requestAnimFrame(animloop);
        board.draw();
    })();
}

function main() {
    // Create canvas
    var canvas = initCanvas();
    initGameDialog(canvas);
}

// shim layer with setTimeout fallback
window.requestAnimFrame = (function(){
  return  window.requestAnimationFrame       ||
          window.webkitRequestAnimationFrame ||
          window.mozRequestAnimationFrame    ||
          function( callback ){
            window.setTimeout(callback, 1000 / 60);
          };
})();


main();