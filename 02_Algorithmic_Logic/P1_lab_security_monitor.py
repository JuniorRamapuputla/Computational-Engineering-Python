"""
TITLE: Autonomous Lab Security & Environment Monitor (ALSEM)
DESCRIPTION: Integrated firmware simulation for a smart laboratory controller. 
             Handles bitwise hardware security handshakes, nested environmental 
             logic, and robust sensor data processing.
AUTHOR: Junior Ramapuputla
"""

def verify_security_access(access_hex):
    """
    Validates a hexadecimal status register to determine user permissions.
    Checks power status before evaluating privilege levels.
    """
    # Parse incoming hexadecimal register
    access_int = int(access_hex, 16)
    
    # Define Bitwise Masks
    PWR_MASK = 0x01  # Bit 0: Hardware Power Status
    ADM_MASK = 0x80  # Bit 7: Administrative Privilege
    
    # Extract flag states
    is_powered = bool(access_int & PWR_MASK)
    is_admin = bool(access_int & ADM_MASK)
    
    # Access control logic
    if not is_powered:
        return "Denied: Hardware Offline"
    
    if is_admin:
        return "Admin"
    else:
        return "Standard User"


def evaluate_environmental_state(temp, humidity, is_active):
    """
    Determines system safety based on temperature and humidity thresholds.
    Implements nested logic to identify specific environmental risks.
    """
    if not is_active:
        return "OFFLINE"

    if temp > 30.0:
        # Evaluate mold risk based on high humidity at high temperatures
        if humidity > 70.0:
            return "CRITICAL: MOLD RISK"
        else:
            return "WARNING: OVERHEAT"
            
    elif temp < 18.0:
        return "WARNING: UNDER-TEMP"
    
    else:
        return "NOMINAL"
    

def process_telemetry_burst(readings):
    """
    Iterates through a telemetry data packet to calculate average voltage.
    Handles data noise, clock-cycle skips, and critical sensor failures.
    """
    running_total = 0.0
    valid_samples = 0
    system_status = "SUCCESS"
    
    # Iterate through telemetry values
    for val in readings:
        # Ignore 0.0 values (skipped cycles)
        if val == 0.0:
            pass 
        
        # Identify short-circuits or sensor failure
        elif val > 5.0:
            system_status = "SENSOR_FAILURE_DETECTED"
            break 
        
        # Filter low-level signal noise
        elif val < 1.0:
            continue 
        
        # Process valid data
        else:
            running_total += val
            valid_samples += 1
    
    # Ensure precision and prevent division by zero
    if valid_samples > 0:
        average = round(running_total / valid_samples, 2)
    else: 
        average = 0.0
    
    return average, system_status


def translate_status_code(code):
    """
    Maps hardware integer codes to technical descriptions using 
    engineering notation and Unicode symbols.
    """
    status_map = {
        0 : "SYSTEM_OK",
        1 : "TEMP_SIGMA_HIGH \u03C3",
        2 : "VOLT_DROP \u0394",
        3 : "RES_LOAD \u03A9"
    }
    
    return status_map.get(code, "UNKNOWN_ERROR_CODE")


def main():
    """
    Executes integration testing for the ALSEM firmware module.
    """
    print("--- 🛡 ALSEM SYSTEM INITIALIZING 🛡 ---\n")

    # 1. Security Validation
    # 0x81 corresponds to Power ON and Admin ON
    access_level = verify_security_access("0x81") 
    print(f"Access Level:     {access_level}")

    # 2. Environmental Analysis
    # Simulated case: 32°C and 85% Humidity
    environment_report = evaluate_environmental_state(32.0, 85.0, True)
    print(f"Climate Report:   {environment_report}")

    # 3. Telemetry Processing
    # Data contains: valid(1.2), skip(0.0), valid(3.4), failure(9.9)
    telemetry_data = [1.2, 0.0, 3.4, 9.9, 2.1] 
    v_avg, status_msg = process_telemetry_burst(telemetry_data)
    print(f"Telemetry Mean:   {v_avg}V | Status: {status_msg}")

    # 4. Diagnostics Translation
    print(f"ID Mapping (2):   {translate_status_code(2)}")

    print("\n--- 🛡 SYSTEM STABLE ---")


if __name__ == "__main__":
    main()