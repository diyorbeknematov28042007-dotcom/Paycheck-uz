from PIL import Image

def analyze_image(image_path: str):
    try:
        img = Image.open(image_path)
        width, height = img.size

        return {
            "status": "ok",
            "width": width,
            "height": height,
            "risk_score": 12
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }