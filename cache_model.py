from transformers import BlipProcessor, BlipForConditionalGeneration

# Load processor and model to cache them locally
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

print("Model and processor are cached locally.")
