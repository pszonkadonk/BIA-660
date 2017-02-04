def Tests_for_ATM_simulator():

   # A user will not be able to make a negative withdrawal
   assert not valid_withdrawal_request(current_balance = 5000, requested_withdrawal = -500, grace = 0)

   # This particular user will not be able to withdraw any funds if they have a grace value of negative 1 (or more)
   assert not valid_withdrawal_request(current_balance = 100, requested_withdrawal = 25, grace = -1)

   # No user regardless or their balance, will be able to withdraw more then 50,000 from an ATM
   assert not valid_withdrawal_request(current_balance = 1000000, requested_withdrawal= 50001, grace = 1)
   assert valid_withdrawal_request(current_balance = 1000000, requested_withdrawal= 50000, grace = 1)

   # Every user must have a valid pin number on file in the system
   assert not authenticated_pin(user_pin = None, entered_pin = 5678, username = "Michael Pszonka")

   #All users must have a pin number that is exactly four digits.
   assert not authenticated_pin(user_pin = 123, entered_pin = 123)
   assert not authenticated_pin(user_pin = 12345, entered_pin = 12345)
   assert authenticated_pin(user_pin = 1234, entered_pin = 1234)

   print("Tests Passed!")


# Michael Pszonka
# BIA 660
# Homework 2B