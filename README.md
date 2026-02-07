# Image Caption Generator

A Flask-based web application that generates descriptive captions for uploaded images using the BLIP (Bootstrapping Language-Image Pre-training) model from Salesforce.

## Overview

This project implements an image captioning system that leverages state-of-the-art transformer-based models to automatically generate natural language descriptions of images. The application features a modern glassmorphism UI design and provides a simple, intuitive interface for users to upload images and receive AI-generated captions.

## Features

- **Automatic Image Captioning**: Generate descriptive captions for any uploaded image
- **Modern UI**: Glassmorphism design with smooth animations and transitions
- **Real-time Processing**: Instant caption generation upon image upload
- **File Management**: Secure file handling with UUID-based naming to prevent overwrites
- **CORS Support**: Configured for cross-origin requests from specified origins
- **Error Handling**: Robust error handling for invalid files and processing errors

## Technology Stack

### Backend
- **Flask**: Web framework for Python
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **Transformers**: Hugging Face library for pre-trained models
- **PIL (Pillow)**: Image processing library
- **PyTorch**: Deep learning framework (required by Transformers)

### Frontend
- **HTML5**: Markup structure
- **CSS3**: Styling with glassmorphism effects
- **Vanilla JavaScript**: Client-side interactivity and AJAX requests

### Machine Learning Model
- **BLIP (Salesforce/blip-image-captioning-base)**: Pre-trained vision-language model
  - Paper: "BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation"
  - Authors: Li et al., 2022
  - Model Hub: https://huggingface.co/Salesforce/blip-image-captioning-base

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd image-caption-generator
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install flask flask-cors transformers pillow torch huggingface-hub
   ```

4. **Configure Hugging Face authentication**
   
   Replace the placeholder token in `generate_caption.py` with your own Hugging Face access token:
   ```python
   login("your_huggingface_token_here")
   ```
   
   You can obtain a token from https://huggingface.co/settings/tokens

5. **Cache the model (optional but recommended)**
   ```bash
   python cache_model.py
   ```
   This downloads and caches the BLIP model locally, improving startup time for subsequent runs.

6. **Create required directories**
   ```bash
   mkdir -p static/uploads
   mkdir -p templates
   ```

## Quick Start

1. **Start the Flask development server**
   ```bash
   python app.py
   ```

2. **Access the application**
   
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. **Generate a caption**
   - Click "Upload Image" to select an image file
   - Click "Generate" to process the image
   - View the generated caption displayed below the buttons


## API Endpoints

### POST /generate_caption

Generates a caption for an uploaded image.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: Form data with 'file' field containing the image

**Response:**
```json
{
  "caption": "a dog sitting on a bench"
}
```

**Error Responses:**
```json
{
  "error": "No file part"
}
```
```json
{
  "error": "No selected file"
}
```

## Model Information

### BLIP (Bootstrapping Language-Image Pre-training)

The application uses the BLIP model developed by Salesforce Research. BLIP is a vision-language pre-training framework that achieves state-of-the-art performance on various vision-language tasks.

**Key Features:**
- Unified understanding and generation capabilities
- Pre-trained on large-scale image-text pairs
- Efficient fine-tuning on downstream tasks
- Robust performance on image captioning tasks

**Reference Paper:**
```
@inproceedings{li2022blip,
  title={BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation},
  author={Li, Junnan and Li, Dongxu and Xiong, Caiming and Hoi, Steven},
  booktitle={International Conference on Machine Learning},
  year={2022}
}
```

**Model Card:** https://huggingface.co/Salesforce/blip-image-captioning-base

## Configuration

### CORS Settings

The application is configured to accept requests from `http://127.0.0.1:5500`. To modify this:

```python
CORS(app, resources={r"/generate_caption": {"origins": "your_origin_here"}})
```

### Upload Directory

Images are stored in `static/uploads/`. To change this location:

```python
app.config['UPLOAD_FOLDER'] = 'your_upload_directory'
```

## Security Considerations

1. **API Token**: Never commit your Hugging Face API token to version control. Use environment variables instead:
   ```python
   import os
   from huggingface_hub import login
   login(os.getenv('HUGGINGFACE_TOKEN'))
   ```

2. **File Upload**: Implement file type validation and size limits for production deployments

3. **CORS**: Restrict CORS origins to trusted domains only

4. **File Storage**: Implement cleanup routines to remove old uploaded files

## Troubleshooting

### Common Issues

**Model Download Fails:**
- Ensure you have a valid Hugging Face token
- Check your internet connection
- Verify disk space for model storage (approximately 1GB)

**Import Errors:**
- Verify all dependencies are installed: `pip list`
- Ensure virtual environment is activated
- Try reinstalling requirements: `pip install --upgrade -r requirements.txt`

**File Upload Fails:**
- Check that `static/uploads/` directory exists and has write permissions
- Verify the file is a valid image format (JPEG, PNG, WebP, etc.)

## Performance Optimization

- **Model Caching**: Run `cache_model.py` to pre-download the model
- **GPU Acceleration**: Install PyTorch with CUDA support for faster inference
- **Batch Processing**: Modify the application to support multiple image uploads

## Future Enhancements

- Support for multiple caption generation models
- Batch image processing
- Caption history and favorites
- Export captions to various formats
- Integration with cloud storage services
- Mobile-responsive design improvements

## License

This project uses the BLIP model which is released under the BSD-3-Clause License by Salesforce.
