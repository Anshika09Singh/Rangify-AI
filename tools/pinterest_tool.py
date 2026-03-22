from ddgs import DDGS

def pinterest_search(colors, gender):

    results = []

    with DDGS() as ddgs:

        for color in colors:

            query = f"{color} {gender} outfit fashion"

            try:
                images = ddgs.images(
                    query,
                    max_results=5,
                    safesearch="off"
                )

                for img in images:

                    image_url = img.get("image")
                    page_url = img.get("url")

                    if image_url:
                        results.append({
                            "image": image_url,
                            "source": page_url
                        })

            except Exception:
                continue

    return results