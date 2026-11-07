# Week 5 Lab: Reusable Shipping Quote

- **Test Run:** I ran an order with a subtotal of 120. The program successfully applied the 10% discount and waived the shipping fee, resulting in 108.0 final total.
- **Change after testing:** I updated the `get_discount_rate` threshold to properly include `subtotal >= 100.0` instead of just `> 100.0` to ensure the exact boundary value triggers the discount.
