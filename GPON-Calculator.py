
def calculate_gpon_link_budget():
    print("--- GPON Optical Link Budget Calculator ---")
    
    # Fiber attenuation is typically 0.25 dB/km for downstream (1490nm)
    fiber_attenuation_per_km = 0.25 
    connector_loss = 0.5 # dB per connector
    splice_loss = 0.1 # dB per splice
  
    splitter_losses = {
        2: 3.5,
        4: 7.2,
        8: 10.5,
        16: 14.0,
        32: 17.5,
        64: 21.0,
        128: 24.5
    }

    try:
      
        tx_power = float(input("Enter OLT Transmit Power (dBm) [e.g., 2.5]: "))
        distance_km = float(input("Enter Fiber Distance (km) [e.g., 5]: "))
        connectors = int(input("Enter number of Connectors [e.g., 4]: "))
        splices = int(input("Enter number of Splices [e.g., 2]: "))
        split_ratio = int(input("Enter Splitter Ratio (2, 4, 8, 16, 32, 64, 128) [e.g., 64]: "))

        if split_ratio not in splitter_losses:
            print("Invalid split ratio. Please enter a valid GPON split ratio.")
            return

        total_fiber_loss = distance_km * fiber_attenuation_per_km
        total_connector_loss = connectors * connector_loss
        total_splice_loss = splices * splice_loss
        splitter_loss = splitter_losses[split_ratio]

        total_loss = total_fiber_loss + total_connector_loss + total_splice_loss + splitter_loss
        rx_power = tx_power - total_loss

        # Standard ONT Receiver Sensitivity is usually around -27 dBm
        receiver_sensitivity = -27.0
        margin = rx_power - receiver_sensitivity

        print("\n--- Link Budget Results ---")
        print(f"Total Loss: {total_loss:.2f} dB")
        print(f"Received Power at ONT: {rx_power:.2f} dBm")
        print(f"System Margin: {margin:.2f} dB")

        if rx_power >= receiver_sensitivity and margin >= 3.0:
            print("Status: PASS (Link is highly reliable)")
        elif rx_power >= receiver_sensitivity:
            print("Status: MARGINAL PASS (Link works but very little safety margin)")
        else:
            print("Status: FAIL (Received power is too low for ONT to sync)")

    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_gpon_link_budget()
