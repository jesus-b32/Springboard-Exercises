/** Connect Four
 *
 * Player 1 and 2 alternate turns. On each turn, a piece is dropped down a
 * column until a player gets four-in-a-row (horiz, vert, or diag) or until
 * board fills (tie)
 */

class Game {
  constructor (player1, player2) {//width, height, board, currentPlayer
      this.width = 7;
      this.height = 6;
      this.board = [];
      this.currentPlayer = player1;
      this.makeBoard();
      this.makeHtmlBoard();
      this.gameOver = false;
      this.player1 = player1;
      this.player2 = player2;
  }

  makeBoard() {
      for (let y = 0; y < this.height; y++) {
          this.board.push(Array.from({ length: this.width }));
        }
  }

  makeHtmlBoard() {
      const board = document.getElementById('board');
      board.innerHTML = '';

      // make column tops (clickable area for adding a piece to that column)
      const top = document.createElement('tr');
      top.setAttribute('id', 'column-top');

      this.handleGameClick = this.handleClick.bind(this); //need to bind event listener callback to game object

      top.addEventListener('click', this.handleGameClick);
    
      for (let x = 0; x < this.width; x++) {
        const headCell = document.createElement('td');
        headCell.setAttribute('id', x);
        top.append(headCell);
      }
    
      board.append(top);
    
      // make main part of board
      for (let y = 0; y < this.height; y++) {
        const row = document.createElement('tr');
    
        for (let x = 0; x < this.width; x++) {
          const cell = document.createElement('td');
          cell.setAttribute('id', `${y}-${x}`);
          row.append(cell);
        }
    
        board.append(row);
      }
  }

  findSpotForCol(x) {
      for (let y = this.height - 1; y >= 0; y--) {
        if (!this.board[y][x]) {
          return y;
        }
      }
      return null;
  }

  placeInTable(y, x) {
      const piece = document.createElement('div');
      piece.classList.add('piece');
      piece.style.backgroundColor = this.currentPlayer.color;
      piece.style.top = -50 * (y + 2);
    
      const spot = document.getElementById(`${y}-${x}`);
      spot.append(piece);
  }

  endGame(msg) {
      alert(msg);
      const top = document.querySelector('#column-top');
      top.removeEventListener('click', this.handleGameClick);
  }

  handleClick(evt) {
      // get x from ID of clicked cell
      const x = +evt.target.id;
    
      // get next spot in column (if none, ignore click)
      const y = this.findSpotForCol(x);
      if (y === null) {
        return;
      }
    
      // place piece in board and add to HTML table
      this.board[y][x] = this.currentPlayer; //currPlayer board
      this.placeInTable(y, x);//placeInTable
      
      // check for win
      if (this.checkForWin()) { //checkForWin
        this.gameOver = true;
        return this.endGame(`${this.currentPlayer.color} player won!`);//endGame currPlayer
      }
      
      // check for tie
      if (this.board.every(row => row.every(cell => cell))) { //board
        return this.endGame('Tie!');//endGame
      }
        
      // switch players
      this.currentPlayer = this.currentPlayer === this.player1 ? this.player2 : this.player1; // currPlayer = currPlayer === 1 ? 2 : 1;
  }    

  checkForWin() {
      const _win = (cells) => {
        // Check four cells to see if they're all color of current player
        //  - cells: list of four (y, x) cells
        //  - returns true if all are legal coordinates & all match currPlayer
    
        return cells.every(
          ([y, x]) =>
            y >= 0 &&
            y < this.height &&
            x >= 0 &&
            x < this.width &&
            this.board[y][x] === this.currentPlayer//currPlayer board
        );
      }
    
      for (let y = 0; y < this.height; y++) {
        for (let x = 0; x < this.width; x++) {
          // get "check list" of 4 cells (starting here) for each of the different
          // ways to win
          const horiz = [[y, x], [y, x + 1], [y, x + 2], [y, x + 3]];
          const vert = [[y, x], [y + 1, x], [y + 2, x], [y + 3, x]];
          const diagDR = [[y, x], [y + 1, x + 1], [y + 2, x + 2], [y + 3, x + 3]];
          const diagDL = [[y, x], [y + 1, x - 1], [y + 2, x - 2], [y + 3, x - 3]];
    
          // find winner (only checking each win-possibility as needed)
          if (_win(horiz) || _win(vert) || _win(diagDR) || _win(diagDL)) {
            return true;
          }
        }
      }
  }
}

class Player {
  constructor(color) {
    this.color = color;
  }
}

document.querySelector('#start').addEventListener('click', () => {
  let player1 = new Player(document.querySelector('#player1_color').value);
  let player2 = new Player(document.querySelector('#player2_color').value);
  new Game(player1, player2);
});