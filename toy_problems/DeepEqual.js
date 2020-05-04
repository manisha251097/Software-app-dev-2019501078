function deepEqual(obj1, obj2, ) {

    if (obj1 === obj2) {

        return true

    } else if ((typeof obj1 == "object" && obj1 != null) && (typeof obj2 == "object" && obj2 != null)) {

        const obj1Keys = Object.keys(obj1)
        const obj2Keys = Object.keys(obj2)

        if (obj1Keys.length != obj2Keys.length) {
            return false;
        }

        for (let index = 0; index < obj1Keys.length; index++) {

            const o1Key = obj1Keys[index]
            const o2Key = obj2Keys[index]

            if (o1Key === o2Key) {

                if (!deepEqual(obj1[o1Key], obj2[o2Key])) {
                    return false
                }

            } else {
                return false
            }
        }
        return true
    } else {
        return false
    }
}


console.log(deepEqual("abcd", "abcd"))
console.log(deepEqual("BI", "BIL"))

console.log(deepEqual({ A: "A" }, { A: "A" }))
console.log(deepEqual({ A: "A" }, { B: "A" }))

console.log(deepEqual(["A"], ["A"]))
console.log(deepEqual(["A"], ["B"]))

console.log(deepEqual({ A: { B: "C" } }, { A: { B: "C" } }))
console.log(deepEqual({ A: { B: "C" } }, { A: { C: "C" } }))

console.log(deepEqual({ A: "A" }, { A: "A", C: "D" }))
console.log(deepEqual(null, null))