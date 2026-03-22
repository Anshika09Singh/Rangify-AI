from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def llm_style_advice(gender, skin, palette):

    try:

        prompt = f"""
        You are a professional fashion stylist.

        User Details:
        Gender: {gender}
        Skin tone: {skin}

        Recommended colors: {palette}

        Suggest:
        1 outfit idea
        1 styling tip
        1 fashion trend insight
        """

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("Gemini error:", e)

        return None