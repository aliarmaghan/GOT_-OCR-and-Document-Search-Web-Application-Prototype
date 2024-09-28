from transformers import AutoModel, AutoTokenizer
import numpy as np
from PIL import Image



def load_got_model():
    """
    Function to load the GOT-OCR 2.0 model and tokenizer.
    Returns:
        tokenizer: Tokenizer for the GOT model.
        model: Pretrained GOT-OCR model.
    """
    tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)
    model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', 
                                      trust_remote_code=True, 
                                      low_cpu_mem_usage=True, 
                                      device_map='cuda', 
                                      use_safetensors=True, 
                                      pad_token_id=tokenizer.eos_token_id).eval().cuda()
    return tokenizer, model




def extract_text_with_got(image_path):
    """
    Function to process an image and extract text using the GOT model.
    
    Args:
        image_path (str or file-like object): Path to the image or file uploaded.
        
    Returns:
        str: Extracted text from the image.
    """
     # Load the GOT-OCR model and tokenizer
    tokenizer, model = load_got_model()



    # Use the model's chat function to perform OCR on the tensor
    res = model.chat(tokenizer, image_path, ocr_type='ocr')  # OCR the image tensor
    
    return res