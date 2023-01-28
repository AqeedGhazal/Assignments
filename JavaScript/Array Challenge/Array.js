//var arr = [3.14,"food" , "pie" , true , "food"];
//var arr1 = [4,1,5,6,2];

//function alwayshungry(){

    //for (var i=0 ; i<arr1.length ; i++){
        //if(arr[i]=="food")
        //console.log("yummy");    
//}
//}
//alwayshungry(arr);


//function highpass(arr,cutoff){
//var filteredArr = [] ; 
    //for(var i =0 ; i<arr.length ; i++){
        //if(arr[i]>cutoff){
       // filteredArr.push(arr[i]);
        //}
    //}
        //return filteredArr;
//}
 //var result = highpass([6,8,3,10,-2,5,9],5);
//console.log(result);

//function betterThanAverage(arr){
    //var sum =0 ;
    //for(var i = 0 ; i<arr.length ; i++){
        //sum+=arr[i];
   // }
   // var avg = sum/arr.length;
   // var count = 0 ; 
   // for (var i =0 ; i<arr.length ; i++){
      //  if(arr[i]>avg){
          //  count++;
     //   }
   // }
  //  return count;
//}
//var result = betterThanAverage([6,8,3,10,-2,5,9]);
//console.log(result); 

//function reverse(arr){
    //var first = 0 ;
   // var last = arr.length-1;
   // while(first<last){
        //var x = arr[first];
        //arr[first]=arr[last];
        //arr[last]=x;
       // first++;
       // last--; 
  //  }
   // return arr ; 
//}
//var result = reverse(["a","b","c","d","e"])
//console.log(result);

function fibonacciArray(n){
    var arr=[0,1];
    while(arr.length<n){
        var prev = arr[arr.length-1];
        var prev2 = arr[arr.length-2];
        arr.push(prev+prev2);
    }
    return arr;
}
 var result = fibonacciArray(10);
 console.log(result); 


