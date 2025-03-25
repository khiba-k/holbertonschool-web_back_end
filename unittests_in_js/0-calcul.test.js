const calculateNumber = require("./0-calcul");
const assert = require("assert");

describe("calculateNumber", function () {
  it("Should round 2 to the nearest integer and add to 5", function () {
    assert.equal(calculateNumber(2, 5), 7);
  });

  it("Should add 2 to 0 when 2 is already an integer", function () {
    assert.equal(calculateNumber(2, 0), 2);
  });

  it("Should round 2.7 to 3 and add to 5", function () {
    assert.equal(calculateNumber(2.7, 5), 8);
  });

  it("Should round 2.5 to 3 and add to 5.7", function () {
    assert.equal(calculateNumber(2.5, 5.7), 9);
  });

  it("Should round 3 to the nearest integer and add to -5", function () {
    assert.equal(calculateNumber(3, -5), -2);
  });

  it("Should round -3 to the nearest integer and add to 5", function () {
    assert.equal(calculateNumber(-3, 5), 2);
  });

  it("Should round -3.7 to -4 and add to 5", function () {
    assert.equal(calculateNumber(-3.7, 5), 1);
  });

  it("Should round 3.7 to 4 and add to -5", function () {
    assert.equal(calculateNumber(3.7, -5), -1);
  });

  it("Should round -3.2 to -3 and add to 5", function () {
    assert.equal(calculateNumber(-3.2, 5), 2);
  });

  it("Should round 3.2 to 3 and add to -5", function () {
    assert.equal(calculateNumber(3.2, -5), -2);
  });
});
