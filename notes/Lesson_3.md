# Metadata Extraction and Chunking

## Lesson Objective

- Learn how to enrich extracted content with metadata, which helps downstream RAG results by supporting hybrid search, allowing you to chunk content more meaningfully for semantic search.

## What is Metadata?

- Metadata is the additional information extracted during pre-processing the document.
- Metadata can be at both of these levels
  - Document level metadata
    - Information about the document itself, such as filename, source URL, or filetype.
  - Structural metadata (Element level)
    - Extracted from the structure of the document, such as
      - Category of element type, hierarchical relationships between the different element types.
- Search enhancement
  - In RAG systems, metadata provides filtering options for hybrid search.
- Metadata example
  ![Metadata example](../images/3_0.png)

## Semantic Search for LLMs

### Semantic Search with Vector Databases

- **Goal**
  - Given an input text, find semantically similar content from a corpus of documents for use in prompt templates.
- **Embedding**
  - Convert text to vectors that can be compared through a similarity function, such as cosine similarity.
- **Vector Database**
  - A database optimized for performing similarity search.
- **Prompt Templating**
  - Insert relevant content into a template to generate a prompt for the LLM. Often content semantically similar to an input query.

### Other Concepts

- **Load**
  - Inserts the vectors into the database, along with the source documents or a pointer to the source documents.
- **Query Embed**
  - Embed the input for the similarity search
- **Compare and Retrieve**
  - Compare the query embedding to documents in the Vector DB
  - Retrieve the *k* most similar documents

## Hybrid Search

### Semantic Similarity Search Challenges

- **Too Many Matches**
- **Most Recent Information**
  - Users may want to bias results based on some other information, such as the most recent information, not just the most semantically similar.
- **Loss of important information**
  - Loss of important information within the document that's relevant to the search, such as section information.

### Solution

- **Hybrid Strategy**
  - Hybrdi search is a search strategy that combines semantic search with other information retrieval techniques, such as filtering and keyword search.
- **Filtering Options**
  - Metadata from documents provides filtering options for hybrid search.
  - Metadata is also useful for other operations such as chunking.

## Chunking

- **Chunking Necessity**
  - Chunking is taking a long piece of text and breaking it down into smaller pieces so that you can pass those smaller pieces into the vector database. And then include those snippents into prompt templates to pass to an LLM.
- **Why is Chunking required?**
  - Limited context of LLM
  - LLMs cost more due to larger context window
    - Chunking saves money on inference cost
- **Even Size Chunks**
  - The easiest way is to split the document into roughly even size chunks.
- **Chubking by Atomic Elements**
  - By identifying atomic elements, you can chunk by combining elements rather than splitting raw text:
    - Results in more coherent chunks
    - Example: Combining content under the same section header into the same chunk

## Chunking from Elements

### Constructing Chunks from Document Elements

- **Partitioning**
  - First, break the document down into atomic elements.
- **Combine Elements into Chunks**
  - Add document element one by one until character or token threshold is reached.
- **Apply Break Conditions**
  - Goal: Group content together that logically belongs together.
  - Apply a condition for starting a new chunk, such as when we reach a new title element (indicating a new section), when element metadata changes (indicating a new page or section), or when content similarity exceeds a threshold.

### Advantages

- **Coherent Chunks**
  - Keeps content from the same document element together, resulting in more coherent chunks.
- **Structured Chunks**
  - Allows the chunking method to take advantage of the document structure. This is unlike tranditional chunking techniques that split on token or character count.
- **Rapid Experimentation**
  - Building chunks from document elements allows for rapid experimentation (paritioning is expensive, chunking is fast).

## Notebook

- [Jupyter Notebook](../code/Lesson_3_Student.ipynb)
- **Goal**
  - To be able to identify the chapter for each section in the document and then conduct a hybrid search where we'll ask a question about a particular chapter within the document.
- **ChromaDB**
  - In-memory database used in this lesson to conduct similarity search.
