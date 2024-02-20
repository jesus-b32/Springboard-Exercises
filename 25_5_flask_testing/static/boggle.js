// form = document.querySelector('#boggleForm');
class BoggleGame{
    constructor(board, seconds) { //timer is in seconds
        this.board = document.querySelector('#' + board)
        this.seconds = seconds;
        this.score = 0;
        this.wordsUsed = new Set
        this.timer = setInterval(this.tick.bind(this), 1000); // run tick function every second
        this.boggleForm = document.querySelector('#boggleForm');


        //this changes from object to the element the event handler was added to. 
        //The .bind method returns a new bar function with the this value bound to whatever you passed it. In this case, it is bound to the original this from the constructor.
        this.boggleForm.addEventListener('submit', this.handleSubmit.bind(this));
    }

    // Function used to display message in message section of HTML
    showMessage(message, cls) {
        const msg = document.querySelector('#message')
        msg.innerText = message

    }

    // Get word entered by user and sends it to server to check if word is valid. 
    // Server responds with the following JSON response in data: {“result”: “ok”} , {“result”: “not-on-board”}, or {“result”: “not-a-word”}
    async handleSubmit(e) {
        e.preventDefault();
        const word =  document.querySelector('#guess_input').value;

        // check if word entered already been used
        if(this.wordsUsed.has(word)) {
            this.showMessage(`Already found ${word}`);
            return;
        }

        // send a get request to get a resonse to whether word is valid or not
        const response = await axios.get(`/check_word`, {params: {word: word}}); 

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

    async gameOver() {
        this.board.classList.toggle('hide');
        this.boggleForm.classList.toggle('hide');
        
        //send score to server to determine if a new record has been set or not
        const response = await axios.post(`/game_over`, {score: this.score});
    
        if(response.data.new_record) { 
            this.showMessage(`You Set a New Record: ${this.score}`);
        } else {
            this.showMessage(`Final Score: ${this.score}`);
        }


    }

    // timer function
    async tick() {
        this.seconds -= 1;
        this.showTimer()

        if(this.seconds === 0) {
            clearInterval(this.timer);
            this.gameOver()
        }
    }
}


let game = new BoggleGame("boggle_board", 60);
