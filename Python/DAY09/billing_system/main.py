# Import our custom Invoice entity layout definition
from billing_mod import Invoice


def main():
    print("=== Core Automated Point-of-Sale Register ===")
    
    # 1. Initialize a large enterprise transaction account (Qualifies for 10% Tier)
    invoice_one = Invoice(customer_name="Acme Logistics Corp", tax_rate=0.075)
    invoice_one.add_item("Enterprise Software Licensing", unit_price=450.00, quantity=1)
    invoice_one.add_item("Cloud Server Allocation Units", unit_price=75.50, quantity=2)
    
    # 2. Initialize a standard personal retail account
    invoice_two = Invoice(customer_name="Dr. Evelyn Harper")
    invoice_two.add_item("Ergonomic Mesh Task Chair", unit_price=185.00, quantity=1)
    invoice_two.add_item("High-Speed USB-C Data Cable", unit_price=14.99, quantity=3)
    
    # 3. Process records through standard output channels
    for inv in [invoice_one, invoice_two]:
        statement = inv.compile_statement()
        
        print(f"\n==========================================")
        print(f" STATEMENT: {statement['Invoice ID']}")
        print(f" Client:    {statement['Customer']}")
        print(f" Date:      {statement['Date']}")
        print(f"------------------------------------------")
        print(f" Item Breakdown:")
        for item in inv.items:
            print(f"   * {item.name:<30} x{item.quantity} (${item.unit_price:,.2f} ea)")
        print(f"------------------------------------------")
        print(f" Gross Subtotal:         {statement['Subtotal']:,.2f}")
        print(f" Promotional Discount:  -{statement['Discount Applied']:,.2f}")
        print(f" Regional Sales Tax:    +{statement['Tax Amount']:,.2f}")
        print(f" FINAL SETTLEMENT DUE:   {statement['Total Due']:,.2f}")
        
    print(f"==========================================\n")

if __name__ == "__main__":
    main()