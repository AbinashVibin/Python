def percentage(*args):
   total = sum(args)
   avg = total / len(args)
   return avg
# Example usage:
avg = percentage(56, 61, 73)
print('average =', avg)