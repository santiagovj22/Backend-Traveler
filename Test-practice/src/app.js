// var cont = 1;
// var cont2 = 0;
// var bandera = 0;

// var x = prompt("Enter a number: ")

// while(cont <= x){
//     while(cont < cont){
//         if(cont % cont2 == 0 && cont2 != 1 && cont2 != cont){
//             bandera = 1;
//         }
//         cont2++;
//     }

//     if(bandera == 0){
//         console.log(cont2);
//     }
//     else{
//         bandera=0;
//     }
//     cont++;
//     cont2 = 0;
// }

function add(a,b, c){
    return c ? a + b + c : a + b
}

function minus(a,b){
    var x = true
    return x ? a - b : 0
}

// suma de los primeros n numeros primos al cuadrado
function isPrimo(n) {
    if (n <= 0) {
      return false
    }
    for (var i = 2; i < n; i++) {
      if (n % i === 0) {
        return false
      }
    }
    return n !== 1
}

function listPrimo(n){
    const lista = []
    let index = 2
    if (typeof(n) == typeof('')){
        return lista
    }
    if (n == Math.floor(n)) {
        return lista
    }
    while(lista.length < n){
        if(isPrimo(index)){
            lista.push(index)
        }
        index++
    }
    return lista
}


module.exports = { add , minus, isPrimo , listPrimo}