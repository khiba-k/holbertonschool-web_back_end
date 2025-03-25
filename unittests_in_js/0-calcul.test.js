const calculateNumber = require("./0-calcul");
const assert = require("assert");

describe("calculateNumber Test", function () {
  it("Should return sum rounded", function () {
    let a = 1.5,
      b = 3.7;
    let result = Math.floor(a) + Math.floor(b);

    assert.equal(calculateNumber(a, b), result);
  });
});
