const {add, minus, isPrimo, listPrimo} = require('../src/app');

test('adds 1 + 2 to equal 3', () => {
    expect(add(1,2)).toBe(3);
});
test('adds 3 + 3 + 4 to equal 10', () => {
    expect(add(3,3,4)).toBe(10);
});

test('minus 3 - 3 to equal 0', () => {
    expect(minus(3,3)).toBe(0)
});

test('El numero deberia ser primo', () => {
    expect(isPrimo(7)).toBe(true)
})
test('El numero no deberia ser primo', () => {
    expect(isPrimo(8)).toBe(false)
})
test('El numero negativo no deberia ser primo', () => {
    expect(isPrimo(-7)).toBe(false)
})
test('El numero 0 no deberia ser primo', () => {
    expect(isPrimo(0)).toBe(false)
})
test('El numero 1 no deberia ser primo', () => {
    expect(isPrimo(1)).toBe(false)
})
//---------------------------------------------------
test('Lista de 3 primeros numeros primos', () => {
    expect(listPrimo(3)).toEqual([2,3,5])
})
test('Cuando se espera un cero deberia imprimir array vacio', () => {
    expect(listPrimo(0)).toEqual([])
})
test('Cuando se ingresa un negativo, se espera un array vacio', () => {
    expect(listPrimo(-3)).toEqual([])
})
test('El numero 1 deberia retornar 1 primo', () => {
    expect(listPrimo(1)).toEqual([2])
})
test('Cuando se ingresa 5 se devuelven los primeros 5 numeros primos', () => {
    expect(listPrimo(5)).toEqual([2,3,5,7,11])
})
test('Cuando se ingresa un string se espera un array vacio', () => {
    expect(listPrimo('2')).toEqual([])
})
test('Cuando se ingresa un decimal se espera un array vacio', () => {
    expect(listPrimo(2.4)).toEqual([])
})