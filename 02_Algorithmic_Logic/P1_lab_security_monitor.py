"""
TITLE: Autonomous Lab Security & Environment Monitor (ALSEM)
DESCRIPTION: Integrated project covering Sections 1 & 2. 
             Implements bitwise security, nested climate logic, 
             and loop-based data processing.
AUTHOR: Junior Ramapuputla
"""

def verify_security_access(access_hex):
    """
    Task 1: Bitwise & Conditionals
    Check Bit 0 (Power) and Bit 7 (Admin).
    Return a string: "Admin", "User", or "Denied".
    """
    # Convert hex string to int
    access_int = int(access_hex, 16)
    
    # Define Masks: 0x01 (Power), 0x80 (Admin)
    PWR_MASK = 0x01 #Bit 0: System power (0000 0001)
    ADM_MASK = 0x80 #Bit 7: Admin Privilege (1000 0000)
    
    # Logic: If no power -> Denied. If power + admin -> Admin. Else -> User.
    is_powered = bool(access_int & PWR_MASK)
    is_admin = bool(access_int & ADM_MASK)
    
    if not is_powered:
        return "Denied"
    
    if not is_admin:
        return "User"
    else:
        return "Admin"

def climate_decision_engine(temp, humidity, is_active):
    """
    Task 2: Nested If/Else logic.
    Categorize system state based on environmental thresholds.
    """
    # Logic: 
    # If not active -> "OFFLINE"
    # If active -> Check Temp > 30 (then check humidity), Else check Temp < 18...

    if is_active:
        if temp > 30:
            if humidity > 70:
                return "CRITICAL: MOLD RISK"
            else: return "WARNING: OVERHEAT"
        elif temp < 18:
            return "WARNING: UNDER-TEMP"
        else:
            return "NOMINAL"
    else:
        return "OFFLINE"
    

def process_sensor_burst(readings):
    """
    Task 3: Loops (For/While) and Loop Control (Break/Pass).
    Calculate average voltage from a list. 
    Ignore 0.0 (pass), Stop if > 5.0 (break).
    """
    # Use a loop to sum valid readings and count them.
    # Return (average, status_message)
    pass

def get_error_description(code):
    """
    Task 4: Switch/Case implementation via Dictionary.
    Map codes 0-3 to descriptions using Unicode symbols.
    """
    # 0: "SYSTEM_OK", 1: "TEMP_SIGMA_HIGH \u03C3", 2: "VOLT_DROP \u0394", 3: "RES_LOAD \u03A9"
    # Use .get(code, "UNKNOWN_ERR")
    pass

def main():
    print("--- 🛡 ALSEM SYSTEM INITIALIZING 🛡 ---\n")

    # 1. TEST SECURITY
    access_status = verify_security_access("0x81") # Power ON + Admin ON
    print(f"Access Level: {access_status}")

    # 2. TEST CLIMATE
    # Test case: 32°C and 85% Humidity (Critical Mold Risk)
    climate_msg = climate_decision_engine(32.0, 85.0, True)
    print(f"Climate Report: {climate_msg}")

    # 3. TEST DATA PROCESSING
    # Should process 1.2, 3.4, skip 0.0, and stop at 9.9
    raw_data = [1.2, 0.0, 3.4, 9.9, 2.1] 
    avg_v, data_msg = process_sensor_burst(raw_data)
    print(f"Voltage Analysis: Avg={avg_v}V | Status: {data_msg}")

    # 4. TEST ERROR DESCRIPTION
    print(f"Code 2 Translation: {get_error_description(2)}")

if __name__ == "__main__":
    main()