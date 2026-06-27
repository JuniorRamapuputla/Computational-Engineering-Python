"""
TITLE: Lab Inventory & Power Analysis System
DESCRIPTION: A computational tool for managing hardware inventory. Implements 
             dictionary-based data mapping, arithmetic power modeling, 
             and sequence slicing for automated reporting.
AUTHOR: [Junior Ramapuputla]
DATE: 2026/06/27
"""

def create_device_record(name, device_id, voltage, is_active):
    """
    Task 1.1: Ingests raw hardware data into a structured dictionary.
    Ensures data integrity through explicit typecasting.
    """
    device_record = {
        'name': str(name),
        'device_id': int(device_id),
        'base_voltage': float(voltage),
        'is_active': bool(is_active),
        'serial_code': f"SN-{device_id}"  # Robust string formatting
    }
    return device_record


def calculate_power_needs(record):
    """
    Task 1.2: Calculates weekly power consumption using a linear model.
    Validates results against industry-standard PSU ratings.
    """
    PSU_RATINGS = [1.0, 3.5, 5.0, 7.5, 12.0]
    
    # Linear Power Model: (V * 1.5) + 0.75
    raw_power = (record.get('base_voltage') * 1.5) + 0.75
    
    # Ensure precision for comparison
    weekly_power = round(raw_power, 2)
    is_standard = weekly_power in PSU_RATINGS

    return weekly_power, is_standard


def generate_procurement_report(record, power_value):
    """
    Task 1.3 & 1.4: Extracts essential data via slicing and generates 
    a professional multi-line status report.
    """
    # Create an attribute sequence for processing
    attributes = [
        record.get('serial_code'),
        record.get('name'),
        power_value,
        record.get('is_active')
    ]

    # Slice: Extracting Serial, Name, and Power (Indices 0, 1, 2)
    report_data = attributes[:3] 

    # Multi-line formatted output
    report_string = (
        f"DEVICE SERIAL:  {report_data[0]}\n"
        f"HARDWARE:       {report_data[1]}\n"
        f"REQUIRED POWER: {report_data[2]} W"
    )

    return report_string


def main():
    """Entry point for the inventory analysis system."""
    # Test Case: High-performance Microcontroller
    print("--- Starting Lab Inventory Analysis ---\n")

    # 1. Data Ingestion
    device = create_device_record("ESP32-Dev", "5050", 3.3, True)

    # 2. Computational Logic
    power, is_standard = calculate_power_needs(device)

    # 3. Output Generation
    report = generate_procurement_report(device, power)

    # Console display logic
    status_label = "Standard Rating" if is_standard else "Custom Requirement"
    print(f"Device Identity: {device['name']} | Status: {status_label}")
    print("\nPROCUREMENT NOTIFICATION:")
    print("-" * 25)
    print(report)
    print("-" * 25)


if __name__ == "__main__":
    main()