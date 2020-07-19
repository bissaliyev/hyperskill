import sys
import math

# args = sys.argv

params = {}
for k, v in ((k.lstrip("-"), v) for k, v in (a.split('=') for a in sys.argv[1:])):
    params[k] = v
# print(params)

if params['type'] == 'diff':
    if not all(p in params for p in ["principal", "interest", "periods"]):
        print("Incorrect parameters")
    else:
        credit_principal = int(params['principal'])
        credit_interest = float(params['interest'])
        periods = int(params['periods'])

        credit_interest = credit_interest / (12 * 100)

        diff_payment = []
        for m in range(0, periods):
            diff_payment.append(math.ceil(credit_principal / periods + credit_interest *
                               (credit_principal - (credit_principal * (m + 1 - 1)) / periods)))

        overpayment = sum(diff_payment) - credit_principal

        for i, d in enumerate(diff_payment):
            print("Month " + str(i + 1) + ": paid out " + str(d))

        print("\nOverpayment = " + str(overpayment))

elif params['type'] == 'annuity':
    option = ""
    if all(p in params for p in ["principal", "payment", "interest"]):
        option = "n"
    elif all(p in params for p in ["principal", "periods", "interest"]):
        option = "a"
    elif all(p in params for p in ["payment", "periods", "interest"]):
        option = "p"
    else:
        print("Incorrect parameters")

    if option == "n":
        # enter data
        credit_principal = int(params['principal'])
        monthly_payments = int(params['payment'])
        credit_interest = float(params['interest'])

        # calculate formula
        credit_interest = credit_interest / (12 * 100)
        x = monthly_payments / (monthly_payments - credit_interest * credit_principal)
        periods = math.log(x, 1 + credit_interest)

        periods = math.ceil(periods)
        years = int(periods // 12)
        months = math.ceil(periods % 12)
        overpayment = periods * monthly_payments - credit_principal

        # output results
        # print("It takes " + str(periods) + " month to repay the credit")

        message = ""
        if years > 1 and months > 1:
            message = f'{years} years and {months} months'
        elif years >= 1:
            message = f'{years} ' + 'years' if years > 1 else 'year'
        elif months >= 1:
            message = f'{months} ' + 'months' if years > 1 else 'month'

        print("You need " + message + " to repay this credit!")
        print("\nOverpayment = " + str(overpayment))

    elif option == "a":
        # enter data
        credit_principal = int(params['principal'])
        periods = int(params['periods'])
        credit_interest = float(params['interest'])

        # calculate
        credit_interest = credit_interest / (12 * 100)
        monthly_payments = credit_principal * (credit_interest * (1 + credit_interest) ** periods) \
                           / ((1 + credit_interest) ** periods - 1)
        monthly_payments = math.ceil(monthly_payments)
        overpayment = monthly_payments * periods - credit_principal

        # output results
        print("Your annuity payment = " + str(monthly_payments) + "!")
        print("\nOverpayment = " + str(overpayment))

    elif option == "p":
        # enter data
        monthly_payments = float(params['payment'])
        periods = int(params['periods'])
        credit_interest = float(params['interest'])

        # calculate
        credit_interest = credit_interest / (12 * 100)
        credit_principal = monthly_payments / ((credit_interest * (1 + credit_interest) ** periods) / ((1 + credit_interest) ** periods - 1))
        credit_principal = round(credit_principal)
        overpayment = monthly_payments * periods - credit_principal

        # output results
        print("Your credit principal = " + str(credit_principal) + "!")
        print("\nOverpayment = " + str(overpayment))
else:
    print("Incorrect parameters")