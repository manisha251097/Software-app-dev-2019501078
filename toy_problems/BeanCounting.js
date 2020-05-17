function beanCounting(word) {
    let count = 0;
    if (typeof word == "string") {
        for (let index = 0; index < word.length; index++) {
            if (word[index] == "B") {
                count++;
            }
        }
        return count;
    } else {
        return "Input must be a string"
    }
}
let input = ["BILLBILLBILLBILLbill", [], "b", "BabaBAbAAb"]
for (let index = 0; index < input.length; index++) {
    const element = input[index];
    let res = beanCounting(element)
    if (typeof res === "number") {
        console.log("The word" + " " + element + " " + "contains character B " + res + " times")
    } else {
        console.log(res)
    }
}

function beanCountingWithChar(word, char) {
    let count = 0;
    if (typeof word == "string") {
        for (let index = 0; index < word.length; index++) {
            if (word[index] == char) {
                count++;
            }
        }
        return count;
    } else {
        return "Input Must be a string"
    }
}
console.log()
char = ["L", "B", "b", "a",]
for (let index = 0; index < input.length; index++) {
    const element = input[index];
    const ch = char[index]
    let res = beanCountingWithChar(element, ch)
    if (typeof res === "number") {
        console.log("The word" + " " + element + " " + "contains character " + ch + " " + res + " times")
    } else {
        console.log(res)
    }
}