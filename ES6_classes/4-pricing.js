import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this.amount;
  }

  set amount(amountInstance) {
    this._amount = amountInstance;
  }

  get currency() {
    return this._currency;
  }

  set currency(currencyInstance) {
    if (currencyInstance instanceof Currency) this._currency = currencyInstance;
  }

  displayFullPrice() {
    return `${this.amount} ${this._currency.displayFullCurrency}`;
  }

  static convertPrice(amount, conversionRate) {
    const convert = amount * conversionRate;

    return convert;
  }
}
