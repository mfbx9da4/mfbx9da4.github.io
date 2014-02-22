##Features
- all essential styles are set inside javascript to make game more reusable
- you can also use this on a touch screen
- reusable: easy to change colors, size and appearance by modifying variables at the top
- xkcd font :-)



##Todo
- Have an animation loop: animate moving of peices
- Refactor to shorten methods into sub methods
- Score animations
- Animate sidebar to appear
- don't actually need row and col!
- implement computer:
- clean up logs and window.
- after anim working refactor moves to directions
- piece on first row isnt able to move?

###Done
- need to fix how determining whether queen did jump
- is_queen move many squares if not jumping
- Large refactor of globals to peices object
- Queen color
- fix queen can jump queen
- fix when queen jumps, if she can't play change
- implement game over
- handling computer when it has a second jump



##Rules

- Checkers is played by two players. Each player begins the game with 12 colored discs. (Typically, one set of pieces is black and the other red.)
- The board consists of 64 squares, alternating between 32 dark and 32 light squares. It is positioned so that each player has a light square on the right side corner closest to him or her.
- Each player places his or her pieces on the 12 dark squares closest to him or her.
- Black moves first. Players then alternate moves.
- Moves are allowed only on the dark squares, so pieces always move diagonally. Single pieces are always limited to forward moves (toward the opponent).
- A piece making a non-capturing move (not involving a jump) may move only one square.
- A piece making a capturing move (a jump) leaps over one of the opponent's pieces, landing in a straight diagonal line on the other side. Only one piece may be captured in a single jump; however, multiple jumps are allowed on a single turn.
- When a piece is captured, it is removed from the board.
- If a player is able to make a capture, there is no option -- the jump must be made. If more than one capture is available, the player is free to choose whichever he or she prefers.
- When a piece reaches the furthest row from the player who controls that piece, it is crowned and becomes a king. One of the pieces which had been captured is placed on top of the king so that it is twice as high as a single piece.
- Kings are limited to moving diagonally, but may move both forward and backward. (Remember that single pieces, i.e. non-kings, are always limited to forward moves.)
- Kings may combine jumps in several directions -- forward and backward -- on the same turn. Single pieces may shift direction diagonally during a multiple capture turn, but must always jump forward (toward the opponent).
- A player wins the game when the opponent cannot make a move. In most cases, this is because all of the opponent's pieces have been captured, but it could also be because all of his pieces are blocked in.
