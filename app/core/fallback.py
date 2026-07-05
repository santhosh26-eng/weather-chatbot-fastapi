def fallback(weather):

    temp = weather["temperature"]
    condition = weather["condition"].lower()

    advice = []

    # Umbrella suggestion
    if "rain" in condition or "drizzle" in condition or "thunderstorm" in condition:
        advice.append("☔ Carry an umbrella.")
    else:
        advice.append("☀ No umbrella needed.")

    # Jacket suggestion
    if temp < 20:
        advice.append("🧥 Wear a jacket.")
    else:
        advice.append("👕 Light clothing is fine.")

    # Water bottle suggestion
    if temp > 30:
        advice.append("💧 Carry a water bottle and stay hydrated.")

    return " ".join(advice)