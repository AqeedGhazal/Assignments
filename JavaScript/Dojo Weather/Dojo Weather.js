
function showtemp(){
    let x = "loading Weather report"
    alert(x);
}
function hide(){
    var elementname = document.querySelector("#msg")
    elementname.remove() ;
}

function c2f(temp){
    return Math.round((9/5*temp)+32);
}
function f2c(temp){
    return Math.round(5/9*(temp-32));
}

function convert(element){
    
    for(var i=1 ; i<9 ; i++){
        var tempspan = document.querySelector("#temp" + i);
        var tempVal = parseInt(tempspan.innerText);
        if (element.value=="C"){
            tempspan.innerText=f2c(tempVal);
        }
        else{
            tempspan.innerText=c2f(tempVal);
        }
    }
}
