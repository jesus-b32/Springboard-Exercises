/**
 * Write a function called guessingGame which returns a function that allows you to guess a random whole number between 0 and 99. Every time you create a new game, it should select a new random number, and keep it secret from the player.
 *
 * Once the game has started, you can guess the number. The game should tell you whether your guess is too high, too low, or correct.
 *
 * After a correct guess, the game ends.
 */
function guessingGame() {
  let secret = Math.floor(Math.random() * 100);
  let count = 0;
  let gameOver = false;
  return function guess(num) {
    if (gameOver) return 'The game is over, you already won!';
    if (num > secret) {
      count++;
      return `${num} is too high!`;
    } else if (num < secret) {
      count++;
      return `${num} is too low!`;
    } else {
      count++;
      gameOver = true;
      return `You win! You found ${secret} in ${count} guesses.`;
    }
  };
}

module.exports = { guessingGame };
