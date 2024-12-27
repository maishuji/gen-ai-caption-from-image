# Give Meaningful Names to Your Photos with IMG Captioning AI

## Content
In the project, we will use *AutoProcessor* and *BlipForConditionalGeneration* from the *transformers* library to generate captions for images. 

### What are *Blip2Processor* and *BlipForConditionalGeneration*?
*Blip2Processor* is a class that processes images for the *BlipForConditionalGeneration* model. *BlipForConditionalGeneration* is a model that generates captions for images.


### How to Use the Model?

1. **Install the Required Libraries**
```bash
pip install transformers torch
```

2. **Import the Required Libraries**
```python
from transformers import BlipForConditionalGeneration, Blip2Processor
```

3. **Load the Model and Processor**
```python
processor = Blip2Processor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
```

4. **Generate Captions for Images**
```python
image = "path/to/image.jpg"
inputs = processor(image, return_tensors="pt")
caption_ids = model.generate(**inputs)
caption = processor.decode(caption_ids[0], skip_special_tokens=True)
print(caption)
```


### Usage

#### Jupyter Notebook
This project provide a jupyter notebook that demonstrates how to generate captions for images using the *BlipForConditionalGeneration* model.

#### Python Script
You can also use the python script 'image_cap.py' to generate captions for images.
```bash
python image_cap.py --image path/to/image.jpg
```

#### Demo app with gradio interface
You can also use the demo app with gradio interface to generate captions for images.
```bash
python hello.py
```

### Conclusion

In this project, we learned how to generate captions for images using the *BlipForConditionalGeneration* model. We hope you found this project helpful. Thank you for reading!