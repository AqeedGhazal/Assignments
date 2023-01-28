
function changename(){
    var h1 = document.querySelector("#name");
    h1.innerText = "Aseel Issa";
}
function remove(id){
    let user = document.querySelector(id)
    user.remove();
    
}
function decrease(){
var count = document.querySelector('#num') ; 
    let num = parseInt(count.innerText)   
    num--;
    count.innerText = num;
}
function increase(){
    let count1=document.querySelector('#num1')
    let num = parseInt(count1.innerText)
    num++;
    count1.innerText=num ;
}
function accept(id){
    remove(id)
    decrease()
    increase()
}
function reject(id){
    remove(id)
    decrease()
}
