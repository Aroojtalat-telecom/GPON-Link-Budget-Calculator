# GPON Optical Link Budget Calculator ⚡

A Python-based Command Line Interface (CLI) tool designed to calculate the optical link budget for GPON (Gigabit Passive Optical Network) / FTTH infrastructure. 

##  Overview
In telecommunications, before deploying a fiber network, engineers must ensure that the optical signal leaving the OLT (Optical Line Terminal) reaches the customer's ONT (Optical Network Terminal) with sufficient power. This tool automates that calculation.

##  Features & Calculations
This script calculates the total optical loss and system margin by taking the following parameters into account:
* **Fiber Attenuation:** Standardized at 0.25 dB/km for downstream transmission.
* **Passive Splitter Loss:** Accurate approximations for 1:N split ratios (from 1:2 up to 1:128).
* **Connector & Splice Losses:** Customizable inputs for physical network joints.
* **ONT Receiver Sensitivity:** Evaluates the final received power against a standard -27 dBm threshold to determine Link Pass/Fail status.

##  How to Run
Simply run the script in any Python environment:
```bash
python gpon_calculator.py
##  Example Output

```text
--- GPON Optical Link Budget Calculator ---
Enter OLT Transmit Power (dBm) [e.g., 2.5]: 2.5
Enter Fiber Distance (km) [e.g., 5]: 10
Enter number of Connectors [e.g., 4]: 4
Enter number of Splices [e.g., 2]: 2
Enter Splitter Ratio (2, 4, 8, 16, 32, 64, 128) [e.g., 64]: 64

--- Link Budget Results ---
Total Loss: 25.70 dB
Received Power at ONT: -23.20 dBm
System Margin: 3.80 dB
Status: PASS (Link is highly reliable)
