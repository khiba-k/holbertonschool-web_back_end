const sinon = require("sinon");
const expect = require("chai").expect;
const sendPaymentRequestToApi = require("./3-payment.js");
const Utils = require("./utils");

describe("sendPaymentRequestToApi", function () {
  it("calculateNumber Method should be called once", function () {
    const utils = new Utils();
    const spy = sinon.spy(utils, "calculateNumber");

    const calculateNum = utils.calculateNumber("SUM", 100, 20);
    const sendPaymentReq = sendPaymentRequestToApi(100, 20);

    expect(sendPaymentReq).to.equal(calculateNum);
    sinon.assert.calledOnce(spy);
    sinon.assert.calledWith(spy, "SUM", 100, 20);

    spy.restore();
  });
});
