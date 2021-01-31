class   ScorePanel{
    score = 0;
    level = 1;

    maxlevel:number;
    upScore:number;



    scoreEle: HTMLElement;
    levelEle: HTMLElement;

    constructor(maxlevel:number = 10 ,upScore:number=10){
        this.scoreEle = document.getElementById('score');
        this.scoreEle = document.getElementById('level');
        this.maxlevel = maxlevel;
        this.upScore = upScore;


    }

    addScore(){
        this.scoreEle.innerHTML = ++this.score + '';
        if(this.score % this.upScore == 0){
            this.levelUp();
        }
            
        

       
    }

    levelUp(){
        if(this.level <10){
            this.scoreEle.innerHTML = ++this.level + '';
        }
    }
}

export default ScorePanel;
