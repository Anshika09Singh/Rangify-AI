from tools.pinterest_tool import pinterest_search
from tools.llm_style_tool import llm_style_advice


def agent(prompt, skin, gender):

    # Rule-based color palette
    if skin == "warm":
        palette = ["olive", "mustard", "terracotta"]

    elif skin == "cool":
        palette = ["lavender", "plum", "sapphire"]

    else:
        palette = ["beige", "navy", "gray"]

    # Search outfit inspiration based on gender
    inspiration = pinterest_search(palette, gender)

    # Fallback if search fails
    if not inspiration:

        inspiration = []

        for color in palette:
            inspiration.append({
                "image": None,
                "source": f"https://www.pinterest.com/search/pins/?q={color}%20{gender}%20outfit"
            })

    # LLM stylist advice
    try:
        ai_advice = llm_style_advice(gender, skin, palette)
    except Exception:
        ai_advice = "AI stylist advice is currently unavailable."

    return {
        "palette": palette,
        "links": inspiration,
        "ai_advice": ai_advice
    }