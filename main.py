import numpy as np
import matplotlib.pyplot as plt
# https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx
# https://www.revenue.ie/en/jobs-and-pensions/documents/worksheet-to-calculate-your-tax-payable.pdf
TAX_CREDITS = 4_000
STANDARD_CUT_OFF_PAYE = 44_000.00


def get_income_tax(gross):

    income_tax = np.full(gross.shape, 0, dtype=np.float64)
    above_cut_off = gross > STANDARD_CUT_OFF_PAYE
    #apply 20% to all income below the cut off

    income_tax[~above_cut_off] = gross[~above_cut_off] * .2
    income_tax[above_cut_off] = STANDARD_CUT_OFF_PAYE * .2

    #apply 40% to any income above the cutoff
    income_tax[above_cut_off] += (gross[above_cut_off]-STANDARD_CUT_OFF_PAYE) * .4

    return income_tax.round(2)

def plot_basic(gross, net):
    
    fig, ax = plt.subplots()
    ax.plot(gross, net, 'g-')
    ax.set_ylim(top= ax.get_xlim()[1]) #increase out the y axis
    plt.show()

def main():
    gross_income = np.arange(18_000, 100_000+1)

    total_tax = get_income_tax(gross_income)
    tax_after_credits = total_tax - TAX_CREDITS
    tax_after_credits[tax_after_credits < 0] = 0

    net_income = gross_income - tax_after_credits

    plot_basic(gross_income, net_income)

if __name__ == '__main__':    
    main()