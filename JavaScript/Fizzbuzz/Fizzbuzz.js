var x = "fizz";
var y = "buzz" ; 
var z = "fizzbuzz" ; 
for( var i=1;i<=100;i++){
    if (i % 5 ==0 && i % 3==0){
        console.log(z);
    }
    else if(i %3 ==0){
        console.log(x);
    }
    else if(i%5==0){
        console.log(y);
    }    
    else {
        console.log(i);
    }
}