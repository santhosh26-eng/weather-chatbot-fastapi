from litellm import completion

def ask_ai(weather):

    prompt = f"""
    Temperature: {weather['temperature']}°C
    Condition: {weather['condition']}

    Tell the user whether to carry:
    - Umbrella
    - Jacket
    - Water bottle
    """

    response = completion(
        model="gpt-4.1-mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content