# Extracting Tables

## Lesson Objective

- Learn how to extract tables from documents and infer their structures.

## Table Extraction

- **Text Analysis**
  - Most RAG use cases focus on text content within documents.
- **Structured Data**
  - Some industries (i.e. finance, insurance) deal heavily with structured data embedded in unstructured documents.
- **Inherent Structures**
  - Some documents (HTML, Word Docs) contain table structure information.
- **Inference Required**
  - For other documents (PDFs, images), you need to use visual cues to first identify the table within the document and then process it to extract information from the table.
- **Techniques**
  - Table Transformers
  - Vision Transformers
  - OCR Pre-processing
- **HTML Output**
  - After extracting content from the table, convert output to HTML format to preserve the structure when we pass the table to LLM.

## Table Transformers

- Table transformer is a model that identifies bounding boxes for table cells and converts the output to HTML.
- Publication: TableFormer: Table Structure Understanding with Transformers (2022)
  - [arxiv](https://arxiv.org/abs/2203.01017)
  - Authors from IBM Research
  - A transformer based model that predicts table structure and bounding boxes for the table content simultaneously in an end-to-end approach.
- Two steps:
  - First identify tables using the document layout model
  - Then run the table through the table transformer
- ![TableFormer](../images/5_0.png)
- **Advantages**
  - Can trace cells back to the original bounding boxes
- **Disadvantages**
  - Multiple expensive model calls that includes
    - Multiple document layout detection calls
    - Multiple OCR calls

## Vision Transformers

- Use the vision transformer models from [previous lesson](./Lesson_4.md#vision-transformers)
  - In previous lesson output was JSON whereas here we will have HTML
- **Advantage**
  - Allows for prompting
  - More flexible
  - Single model call
- **Disadvantage**
  - Generative and prone to hallucination
  - No bounding boxes

## OCR Postprocessing

- Identify the tables using Document Layout Detection model
- Instead of sending the table to Table Transformer, table is OCRed and then build the table structure based on patterns in OCR output
  - Uses rule-based methods.

- **Advantages**
  - Fast, accurate for well behaved tables
- **Disadvantages**
  - Requires statistical or rules based parsing
  - Less flexible than other approaches
  - On complex tables the result may not be good
  - No link back to bounding boxes in image

## Notebook

- [Jupter Notebook](../code/Lesson_5_Student.ipynb)
- After extracting table from the document and converting the table content to HTML, it can be helpful to summarize these tables so that you can search on these tables when you perform similarity search within a RAG architecture.
- This is achieved here using LangChain.
- Issue faced in local run
  - `TypeError: Client.__init__() got an unexpected keyword argument 'proxies'`
  - Solution:
    - Downgrade `httpx` to `0.27.2` as suggested in [OpenAI forum](https://community.openai.com/t/error-with-openai-1-56-0-client-init-got-an-unexpected-keyword-argument-proxies/1040332)
      - This happens since httpx removed the deprecated keyword `proxies`.
    - Jupyter notebook needs to be restarted to reflect updated version of `httpx`
    - Alternative solution suggested in the above forum: Upgrade openai library.
    - [`httpx`](https://pypi.org/project/httpx/) builds on the well-established usability of `requests`.
