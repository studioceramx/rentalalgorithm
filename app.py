import streamlit as st

def calculate_daily_rate(C, d, alpha, beta):
    """Calculate daily rental rate using the formula:
       Daily Rate(d) = (alpha * C) / (d ** beta)
    """
    if d <= 0:
        return 0
    return (alpha * C) / (d ** beta)

def main():
    st.title("Ceramx Rental Calculator")

    st.write("""
    This app computes the **daily rental rate** and **total rental cost** for an art piece or equipment based on:
    
    **Formula**:  
    Daily Rate(d) = (α × C) / (d^β)

    Where:
    - C: Purchase (retail) cost of the artwork  
    - d: Number of days the piece is rented  
    - α: Scaling constant (fraction of C)  
    - β: Discount exponent (controls how quickly the daily rate decreases)
    """)

    # --- User Inputs ---
    C = st.number_input("Purchase Cost (C)", value=1000.0, min_value=0.0, step=100.0)
    d = st.number_input("Number of Days (d)", value=10, min_value=1, step=1)
    alpha = st.slider("Scaling Constant (α)", min_value=0.0, max_value=1.0, value=0.35, step=0.01)
    beta = st.slider("Discount Exponent (β)", min_value=0.0, max_value=2.0, value=0.50, step=0.01)

    # --- Calculations ---
    daily_rate = calculate_daily_rate(C, d, alpha, beta)
    total_cost = daily_rate * d

    # --- Display Results ---
    st.subheader("Results")
    st.write(f"**Daily Rental Rate:** AED{daily_rate:,.2f}")
    st.write(f"**Total Rental Cost:** AED{total_cost:,.2f}")

if __name__ == "__main__":
    main()
