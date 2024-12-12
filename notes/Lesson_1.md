# Overview of LLM Data Preprocessing

## Lesson Objective

- Learn all the foundations of LLM data pre-processing, and why and how it is important and challenging problem in building LLM applications that uses different data from different sources diverse range of file formats and structures.

## Data Preprocessing and LLMs

- **Retrieval Augmented Generation (RAG)**
  - A technique for grounding LLM responsed on validated external information.
- **Contextual Integration**
  - RAG apps load context into a database, then retrieve content to insert into a prompt.
- **Industry Application**
  - For industry use cases, relevant content comes from diverse document types, such as PDFs, Word docs, email and webpages.

![RAG](../images/1_0.png)

## Preprocessing Outputs

- **Document Content**
  - Text content from the documents that is passed as context to the prompt in RAG applications.
- **Document Elements**
  - Basic building blocks of a document
    - Title
    - Narrative Text
    - List Item
    - Table
    - Image
  - Useful for various RAG tasks, such as filtering and chunking
- **Element Metadata**
  - Additional information about an element
  - Useful for filtering in **hybrid search** and for identifying the source of a response
    - Filename
    - Filetype
    - Page Number
    - Section

## Why is Data Preprocessing Hard?

- **Content Cues**
  - Different document types have different cues for element types (visual, markdown)
  - Examples
    - HTML: Tags may indicate whether a piece of text is a title or list.
    - PDFs: Visual cues
  - Challenge: Being able to pre-process all of these different document types in a common manner requires to understand how different document types indicate what a different element is in that document type.

- **Standardization Need**
  - Challenge:
    - Documents come in different format.
    - There's a need to standardize these so that your application can process them in the same way.

- **Extraction Variability**
  - Different document formats may require different extraction approaches (e.g. forms vs journal articles)

- **Metadata Insight**
  - In many cases, extracting metadata requires an understanding of document structure.
  - Metadata can be useful for various operations in RAG applications, such as filtering (taught later in the course).
