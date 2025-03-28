const sinon = require("sinon");
const expect = require("chai").expect;
const sendPaymentRequestToApi = require("./3-payment.js");
const Utils = require("./utils");

describe("sendPaymentRequestToApi", function () {
  it("calculateNumber Method should be called once", function () {
    const utils = new Utils();

    // Spy on utils method
    const spy = sinon.spy(utils, "calculateNumber");

    const calculateNum = utils.calculateNumber("SUM", 100, 20);
    const sendPaymentReq = sendPaymentRequestToApi(100, 20);

    // Test that the function returns same amount as method
    expect(sendPaymentReq).to.equal(calculateNum);

    // Spy that method is called once in function
    sinon.assert.calledOnce(spy);

    // Spy that method is called with correct args
    sinon.assert.calledWith(spy, "SUM", 100, 20);

    spy.restore();
  });

  it("Stub calculateNumber Method", function () {
    // Create stub
    const stub = sinon.stub(Utils.prototype, "calculateNumber");
    stub.withArgs("SUM", 100, 20).returns(10);

    // Create spy for console.log
    const consoleSpy = sinon.spy(console, "log");

    // Test sendPaymentRequestToApi returns same val as stub
    sendPaymentReq = sendPaymentRequestToApi(100, 20);
    expect(sendPaymentReq).to.equal(10);

    // Test that stub method is called with correct args
    sinon.assert.calledWith(stub, "SUM", 100, 20);

    // Spy that the console log returns correct msg
    sinon.assert.calledWith(consoleSpy, `The total is: 10`);

    consoleSpy.restore();
  });
});
