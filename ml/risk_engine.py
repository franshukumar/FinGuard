def calculate_risk(probability):

    if probability < 0.30:
        return {
            "risk_score": round(probability, 4),
            "risk_level": "LOW",
            "decision": "APPROVE"
        }

    elif probability < 0.70:
        return {
            "risk_score": round(probability, 4),
            "risk_level": "MEDIUM",
            "decision": "REVIEW"
        }

    else:
        return {
            "risk_score": round(probability, 4),
            "risk_level": "HIGH",
            "decision": "BLOCK"
        }