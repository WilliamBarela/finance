from math import exp

def ammortization(principle, principle_original, rate, compound_period, months, payment, days_between_payments, amount_paid):
    if months == 0:
        interest_paid = amount_paid - principle_original
        print "\n\n"
        print "amount paid: " + str(amount_paid)
        print "original principle: " + str(principle_original)
        print "interest paid: " + str(interest_paid)
        print "percent principle paid: " + str(100 * principle_original / amount_paid)
        print "percent interest paid: " + str(100 * interest_paid / amount_paid)
        print "amount remaining: " + str(principle)
    else:
        months -= 1
        amount_paid += payment
        principle = principle*exp((rate/(100 * compound_period)) * days_between_payments) - payment
        print principle
        return ammortization(principle, principle_original, rate, compound_period, months, payment, days_between_payments, amount_paid)

# ammortization(40000, 40000, 3.8, 365, 48, 800, 31, 0)
