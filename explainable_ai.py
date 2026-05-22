def explain_risk(prediction):

    if prediction > 90:
        return "Emergency alert generated due to rising flood severity."

    elif prediction > 75:
        return "Moderate disaster escalation detected."

    else:
        return "Emergency conditions remain stable."