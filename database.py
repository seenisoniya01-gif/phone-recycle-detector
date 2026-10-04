# Mock TRAI MNRL Database
# In the real world, this data resides with TRAI, but it is not publicly accessible

RECYCLED_NUMBERS = {
    "9876543210": {
        "recycled_date": "2024-03-15",
        "old_user": "I***jeet S***h",
        "reason": "Loan default - SIM surrendered",
        "risk_level": "HIGH",
        "alerts": [
            "Bank loan recovery calls",
            "OTP from old Google account",
            "WhatsApp verification attempts"
        ]
    },
    "8765432109": {
        "recycled_date": "2024-08-22",
        "old_user": "R***ni K***ar",
        "reason": "90 days inactive - auto recycle",
        "risk_level": "MEDIUM",
        "alerts": [
            "Food delivery app OTPs",
            "Old bank SMS alerts"
        ]
    },
    "7654321098": {
        "recycled_date": "2025-01-10",
        "old_user": "A***sh V***an",
        "reason": "SIM swap fraud investigation",
        "risk_level": "CRITICAL",
        "alerts": [
            "UPI OTPs",
            "Aadhaar verification calls",
            "Loan recovery - multiple banks"
        ]
    }
}

def check_number(phone: str) -> dict:
    """Check if the phone number has been recycled"""
    # Clean input
    phone = phone.strip().replace("+91", "").replace(" ", "").replace("-", "")
    
    if len(phone) != 10 or not phone.isdigit():
        return {"status": "invalid", "message": "Please enter a valid 10-digit number"}
    
    if phone in RECYCLED_NUMBERS:
        data = RECYCLED_NUMBERS[phone]
        return {
            "status": "recycled",
            "phone": phone,
            "recycled_date": data["recycled_date"],
            "old_user": data["old_user"],
            "reason": data["reason"],
            "risk_level": data["risk_level"],
            "alerts": data["alerts"],
            "advice": [
                "This number is still linked to the old user's accounts",
                "Update this number in your Bank/UPI apps",
                "Ignore any unknown OTPs you receive",
                "If you receive loan recovery calls, say 'wrong number'"
            ]
        }
    else:
        return {
            "status": "clean",
            "phone": phone,
            "message": "This number has not been recycled. It is safe.",
            "risk_level": "LOW"
        }

def report_number(phone: str, issue: str) -> dict:
    """User report - receiving old user calls"""
    return {
        "status": "reported",
        "phone": phone,
        "issue": issue,
        "message": "Report received. We will forward this to TRAI.",
        "report_id": f"RPT-{hash(phone) % 100000:05d}"
    }