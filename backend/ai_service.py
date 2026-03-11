import requests

API_KEY = "AIzaSyDH9o2hVQ7TKksNQI2zBSR5ABNrX66YJrM"

def generate_summary(df):

    total_revenue = df["Revenue"].sum()
    top_region = df.groupby("Region")["Revenue"].sum().idxmax()
    top_product = df.groupby("Product_Category")["Revenue"].sum().idxmax()

    prompt = f"""
    Generate a short executive sales summary.

    Total Revenue: {total_revenue}
    Top Region: {top_region}
    Top Product Category: {top_product}
    """

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)

    data = response.json()

    # Debug print
    print("Gemini response:", data)

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return f"""
Sales Summary

Total Revenue: {total_revenue}
Top Region: {top_region}
Top Product Category: {top_product}
"""