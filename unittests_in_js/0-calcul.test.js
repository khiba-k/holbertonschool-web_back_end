const calculateNumber = require("./0-calcul");
const assert = require("assert");

describe("calculateNumber", function () {
  it("Should return 4", function () {
    let a = 1,
      b = 3;
    let result = 4;

    assert.equal(calculateNumber(a, b), result);
  });

  it("Should return 5", function () {
    let a = 1,
      b = 3.7;
    let result = 5;

    assert.equal(calculateNumber(a, b), result);
  });

  it("Should return 5", function () {
    let a = 1.2,
      b = 3.7;
    let result = 5;

    assert.equal(calculateNumber(a, b), result);
  });

  it("Should return 6", function () {
    let a = 1.5,
      b = 3.7;
    let result = 6;

    assert.equal(calculateNumber(a, b), result);
  });

  it("Should return 3", function () {
    let a = -1.5,
      b = 3.7;
    let result = 3;

    assert.equal(calculateNumber(a, b), result);
  });

  it("Should return 6", function () {
    let a = 1.57,
      b = 3.7;
    let result = 6;

    assert.equal(calculateNumber(a, b), result);
  });
});
