# Preprocessing PDFs and Images

## Lesson Objective

- Learn about document image analysis techniques, such as document layout detection and vision transformers.
- Learn how to use these techiques to process PDFs and images.

## Document Image Analysis

- **Preprocessing with Rules-based Parsers**
  - Many docunemt types, such as HTML, Word Docs and Markdown include formatting information.
  - These documents can be preprocessed with rules-based parsers.
- **Visual Information**
  - For documents such as PDFs and images, the formatting information is visual.
- Document Image Analysis (DIA) allows us to extract formatting information and text from the raw image of a document.

## DIA Methods

- **Document Layout Detection (DLD)**
  - Uses an object detection model to draw and label bounding boxes around layout elements on a document image.
- **Vision Transformer (ViT)**
  - Models take a document image as input and produce a text representation of a structured output (like JSON) as output.
  - Note: ViTs can optionally take a text prompt just like an LLM transformer can.

## Document Layout Detection

- **Vision Detection**
  - Identify and classify bounding box using a computer vision model, such as YOLOX or Detectron2.
  - Refers YOLOX paper on [arxiv](https://arxiv.org/abs/2107.08430)
  - ![Document Layout Detection](../images/4_0.png)
- **Text Extraction**
  - Depending on the document type, there may be two methods for doing this:
    - Optical Character Recognition (OCR) required to extract text.
    - **Direct Extraction**
      - For some documents like PDFs, text is available within the document itself.
      - Use the bounding box information to trace the bounding box to the original document and extract the text content that falls withing the bounding box.

## Vision Transformers

- In contrast to Document Layout Detection, Vision Transformers extract content from PDFs and images in a single step.
- **Visual Translation**
  - Input image is passed to the encoder and the decoder produces text output.
- **DONUT Architecture**
  - DONUT: Document Understanding Transformer
  - One common architecture for vision transformers
- **Direct Conversion**
  - OCR is not required
  - Input image is directly converted to text
- **Structured Training**
  - Can train the model to output a valid JSON string with the structured document output.
- Paper: OCR-free Document Understanding Transformer
  - [arxiv](https://arxiv.org/abs/2111.15664)
- Output: Text and category
  - ![Vision Transformers](../images/4_1.png)

## Advantages & Disadvantages

### Document Layout Models

- **Advantages**
  - Model is trained on a fixed set of element types, and so it can become very good at recognizing those.
  - Provides bounding box information, which allows you to trace the results back to the original document, and in some cases allows you to extract text without running OCR.
- **Disadvantages**
  - May require two model calls
    - Object detection
    - OCR
  - Less flexible
    - Work from a fixed set of element types

### Vision Transformers (Pros and Cons)

- **Advantages**
  - More flexible for non-standard document types, like forms.
    - They are able to extract information like key value pairs relatively easily.
  - More adaptable to new ontologies
    - New element types can be added through prompting
- **Disadvantages**
  - Model is generative, so it is potentially prone to hallucination or repetition, just like in natural language use cases
  - Computationally expensive
    - Much more expensive than document layout detection models

## Notebook

- [Jupyter Notebook](../code/Lesson_4_Student.ipynb)
- We'll preprocess the same document first in an HTML representation and then in a PDF representation.
- We'll see how we can extract a similar set of document types, whether we're processing the document using a rule-based technique, or extracting information based on visual cues.
- Strategy: `fast`
  - Extracts text directly from the document and can be used from simple PDFs like the news article in this notebook.
- Paritioning strategies [documentation in unstructured io](https://docs.unstructured.io/api-reference/api-services/partitioning)
