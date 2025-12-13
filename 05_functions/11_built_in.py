def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""

    chai = "ginger"
    return flavor

print(chai_flavor.__doc__)   #Anything written in two underscore called dunder. 
print(chai_flavor.__name__)


help(len)   #'help' keyword used to explains language-level behavior.

def generate_bill(chai=0, samosa=0): 
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting www.python.com"



# 🔹 Why dunder exists?

# Python uses them to implement language behavior

# You usually don’t create new ones

# You use or override them

# Examples:

# __init__ → constructor

# __str__ → string representation

# __len__ → used by len()

# __doc__ → documentation