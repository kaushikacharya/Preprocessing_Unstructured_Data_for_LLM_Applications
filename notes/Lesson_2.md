# Normalizing the Content

## Lesson Objective

- Learn how to extract and normalize content from a diverse range of document types to enable LLM refer information from PDFs, PowerPoints, Word docs, HTML and more.

## Normalizing Diverse Documents

### What's the need for normalization?

- **Format Diversity**
  - Documents come in a variety of formats (PDF, Word, EPUB, Markdown etc.)
- **Common Format**
  - First step in preprocessing: Convert raw documents into a common format that identifies common document elements like titles and narrative text.

### Benefits of normalization

- **Normalization Benefit**
  - Normalized format allows any document to be processed in the same way, regardless of the source format.
    - Filtering out unwanted elements, like headers and footer.
      - Example: If we have to do that separately for PDF and HTML, you would have to write separate logic for each document.
  - Allows **downstream operations** like chunking in the same way on all different document types.

- **Reduced Processing Cost**
  - Typically the most expensive part of processing documents is extracting the initial content.
  - Downstream tasks like chunking are inexpensive operations on normalized outputs.
  - Experimenting with different chunking strategies becomes computationally inexpensive on normalizing all of the content to the same format.

## Data Serialization

- Typical next step after normalizing the content.
- **Serialization Benefits**
  - Serialization allows the results of document preprocessing to be used again later.
- **Advantages of JSON**
  - Structure is common and well understood
  - Is a standard HTTP response
    - This will come into play when you're processing documents like PDFs and images that require model-based workloads that you'll run over an API.
  - Usable in multiple programming languages
    - Example: Pre-process documents in Python and then serialize in JSON which can be then used in a different language say JavaScript
  - Convertible to JSONL for streamning use cases

## HTML Page

- **LLM Relevance**
  - Integrate fresh internet data into LLMs to maintain their currentness and relevance.
- **HTML Understanding**
  - Essential for structuring web content, using elements `<h1>` for titles and `<p>` for narrative text.
- **Data Extraction and Categorization**
  - Analyzing HTML elements to extract and organize web content into structured formats for relevant information distillation.
  - Unstructured information example
    ![Text categorization](../images/2_0.png)
    - Long text: Likely to be narrative text
    - Short capitalized text: Likely to be title

## MS PowerPoint

- **Professional Use**
  - Widely used in consulting to present ideas, strategies, and results. Crucial for enhancing LLM's knowledge base.
- **Extraction Process**
  - Involves parsing elements like bulleted paragraphs, slide notes, shapes and tables in PowerPoint slides.
  - Extraction process for PPTX files are very similar to HTML files.
    - Bunch of XML that we can pre-process using rules-based logic.
- **Tool Utilization**
  - Python libraries, such as `pptx` navigate and extract textual or visual information from slides.

## PDF with Complex Layout and Tables

- In above cases, we learned about extraction using rule based logic.
- HTML and PPTs: Semi-structured
- PDFs and Images: We look for visual cues

- **PDF Characteristics**
  - Maintains consistent formatting across devices
  - Complex structures with diverse layouts, including text, images and tables in non-sequential order
- **Extraction Tools and Libraries**
  - Facilitate text and element extraction
  - Preserve context and layout, distinguishing between main text, headers, footers, and side notes.
- **Advanced Capabilities**
  - Use OCR and Transformer-based technology

## Notebook

- [Jupyter Notebook](../code/Lesson_2_Student.ipynb)
- Unstructured APIs are used to process PDFs and images because of computational expense.
- Additional resources:
  - [Unstructured core functionality](https://docs.unstructured.io/open-source/core-functionality/overview)
  - [SignUp page](https://github.com/Unstructured-IO/unstructured#try-the-unstructured-serverless-api) for Serverless API
    - [Guide](https://docs.unstructured.io/api-reference/api-services/saas-api-development-guide)
- Installation required/Issues faced to run the notebook locally (in WSL) on VS code:
  - NLTK libraries required
    - [Punkt Sentence Tokenizer](https://www.nltk.org/api/nltk.tokenize.punkt.html)
    - [Part-of-Speech tagger: veraged Perceptron Tagger](https://www.nltk.org/_modules/nltk/tag/perceptron.html)
      - [Article by spaCy author](https://explosion.ai/blog/part-of-speech-pos-tagger-in-python)
  - `panel` requires installation of [jupyter_bokeh](https://github.com/holoviz/panel/issues/3240)
  - Issues faced:
    - Issue #1:
      - API URL
        - `unstructured-client` version mentioned in [requirements.txt](../code/requirements.txt) appends `/general/v0/general` to the API url. For details [click here](https://github.com/Unstructured-IO/unstructured/issues/3837).

    - Issue #2:
      - Failed to render JSON on [Jupyter notebook in VS code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) using either
        - [IPython.display](https://github.com/jupyter/notebook/issues/5446)
        - [panel](https://panel.holoviz.org/reference/panes/JSON.html)
      - Solution
        - [Jupyter Extension for VS code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) provides basic notebook support.
        - Command `jupyter --version` shows that `notebook` package wasn't installed in Jupyter extension for VS code.
        - To install run the command as mentioned in [jupyter docs](https://docs.jupyter.org/en/latest/install/notebook-classic.html)
          - `pip3 install jupyter`
        - Now `jupyter --version` shows `notebook` package installed and rendering works for
          - `panel` from HoloViz
        - But `JSON` is still displaying `IPython.core.display.JSON object`

    - Issue #3:
      - Failed to render PDF
        - [Display using `IFrame`](https://stackoverflow.com/questions/19470099/view-pdf-image-in-an-ipython-notebook) works on running notebook on browser but fails to render on VS code.
        - Similar issue with [panel PDF](https://panel.holoviz.org/reference/panes/PDF.html)
