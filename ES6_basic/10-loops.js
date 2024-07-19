export default function appendToEachArrayValue(array, appendString) {
    let arr = [];

    for (let value of array) {
        newarr.push(appendString + value);
    }

    return arr;
}