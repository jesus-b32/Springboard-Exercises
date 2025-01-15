/**
 * Write a function called createAccount which creates a bank account given a PIN number and an initial deposit amount. The return value should be an object with four methods on it:
 * - checkBalance: Given the correct PIN, return the current balance. (If the PIN is invalid, return “Invalid PIN.”)
 * - deposit: Given the correct PIN and a deposit amount, increment the account balance by the amount. (If the PIN is invalid, return “Invalid PIN.”)
 * - withdraw: Given the correct PIN and a withdrawal amount, decrement the account balance by the amount. You also shouldn’t be able to withdraw more than you have. (If the PIN is invalid, return “Invalid PIN.”)
 * - changePin: Given the old PIN and a new PIN, change the PIN number to the new PIN. (If the old PIN is invalid, return “Invalid PIN.”
 *
 * @param {string} pin
 * @param {number} amount
 */
function createAccount(myPin, balance = 0) {
  return {
    checkBalance(pin) {
      if (pin === myPin) {
        return `$${balance}`;
      }
      return 'Invalid PIN.';
    },
    deposit(pin, amount) {
      if (pin === myPin) {
        balance += amount;
        return `Successfully deposited $${amount}. Current balance: $${balance}.`;
      }
      return 'Invalid PIN.';
    },
    withdraw(pin, amount) {
      if (pin === myPin) {
        if (amount > balance) {
          return 'Withdrawal amount exceeds account balance. Transaction cancelled.';
        } else if (amount <= balance) {
          balance -= amount;
          return `Successfully withdrew $${amount}. Current balance: $${balance}.`;
        }
      } else {
        return 'Invalid PIN.';
      }
    },
    changePin(oldPin, newPin) {
      if (oldPin === myPin) {
        myPin = newPin;
        return 'PIN successfully changed!';
      }
      return 'Invalid PIN.';
    },
  };
}

module.exports = { createAccount };
