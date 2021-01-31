class Snake{

    head: HTMLElement;
    bodies: HTMLCollection;
    element: HTMLElement;

    constructor(){
        this.head = document.querySelector('#snake > div') as HTMLElement;
        this.bodies = document.getElementById('snake')!.getElementsByTagName('div');

    }

    get X(){
        return this.head.offsetLeft;
    }

    get Y(){
        return this.head.offsetTop;
    }

    // set X(){
    //     this.head.style.left = 100 + 'px';
    // }
    //
    // set Y(){
    //     this.head.style.top = 100 + 'px';
    // }

    addBody(){
        this.element.insertAdjacentHTML("beforeend","<div></div>");
    }

}

export default Snake;