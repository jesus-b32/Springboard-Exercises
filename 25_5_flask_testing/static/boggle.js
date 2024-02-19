// form = document.querySelector('#boggleForm');
class BoggleGame{
    constructor(board, seconds = 60) { //timer is in seconds
        this.board = document.querySelector('#' + board)
        this.seconds = seconds;
        this.score = 0;
        this.wordsUsed = new Set
        // this.wordInput = document.querySelector('#guess_input')
        this.timer = setInterval(this.tick.bind(this), 1000); // run tick function every second
        this.boggleForm = document.querySelector('#boggleForm');


        //this changes from object to the element the event handler was added to. 
        //The .bind method returns a new bar function with the this value bound to whatever you passed it. In this case, it is bound to the original this from the constructor.
        this.boggleForm.addEventListener('submit', this.handleSubmit.bind(this));
    }
    showMessage(message, cls) {
        const msg = document.querySelector('#message')
        msg.innerText = message

    }

    async handleSubmit(e) {
        e.preventDefault();
        const word =  document.querySelector('#guess_input').value;
        if(this.wordsUsed.has(word)) {
            this.showMessage(`Already found ${word}`);
            return;
        }

        // console.log('Value from guess input: ', word);
        const response = await axios.get(`/check_word`, {params: {word: word}}); 

        // console.log(response.data.result);

        if(response.data.result === 'not-on-board') {
            this.showMessage(`${word} is not a valid word on this boggle board`);

        } else if (response.data.result === 'not-word'){
            this.showMessage(`${word} is not a valid word`);
        } else {
            this.showMessage(`${word} is a valid word on this boggle board`);
            this.score += word.length;
            this.wordsUsed.add(word);
            document.querySelector('#score').innerText = this.score;
        }
        document.querySelector('#guess_input').value = '';
    }

    showTimer() {
        document.querySelector('#timer').innerText = `${this.seconds}s`;
    }

    gameOver() {
        this.board.classList.toggle('hide');
        this.boggleForm.classList.toggle('hide');
    }

    async tick() {
        this.seconds -= 1;
        this.showTimer()

        if(this.seconds === 0) {
            clearInterval(this.timer);
            // console.log('Times Up!')
            this.gameOver()
        }
    }
}


let game = new BoggleGame("boggle_board");
