# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from PIL import Image
import io
import base64
import traceback

app = Flask(__name__)
CORS(app)

print("Loading Computer Vision Model... (This may take a minute)")
segmenter = pipeline("image-segmentation", model="nvidia/segformer-b0-finetuned-ade-512-512")
print("Model loaded successfully!")

@app.route('/segment', methods=['POST'])
def segment_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    
    try:
        # Read the image
        image = Image.open(file.stream).convert("RGB")
        
        # Run the AI segmentation
        results = segmenter(image)
        
        # Find the mask specifically for the 'wall' class
        wall_mask = None
        for result in results:
            # Improved matching to catch "wall" or "brick wall"
            if 'wall' in result['label'].lower():
                wall_mask = result['mask']
                break
                
        if not wall_mask:
             return jsonify({"error": "No walls detected in this image by the AI."}), 400
             
        # --- THE MAGIC FIX ---
        # Convert the AI's solid black & white mask into a transparent PNG
        # 1. Convert mask to strictly Grayscale (L)
        mask_l = wall_mask.convert("L")
        
        # 2. Create a blank, fully transparent image of the same size
        transparent_mask = Image.new("RGBA", mask_l.size, (255, 255, 255, 0))
        
        # 3. Paste the grayscale mask into the Alpha (transparency) channel of our blank image
        transparent_mask.putalpha(mask_l)
        # ---------------------
        
        # Convert to base64 to send to the browser
        buffered = io.BytesIO()
        transparent_mask.save(buffered, format="PNG")
        mask_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        return jsonify({"mask_url": f"data:image/png;base64,{mask_base64}"})

    except Exception as e:
        print("Backend Error:")
        traceback.print_exc()
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)