const calculateNumber = require("./0-calcul");
const assert = require("assert");
const { describe, it } = require("mocha");

describe("calculateNumber", function () {
  it("Should round args then add them", function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
