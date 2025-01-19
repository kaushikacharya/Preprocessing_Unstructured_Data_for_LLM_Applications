# Build Your Own RAG Bot

## Lesson Objective

- Build your own RAG bot on douments that includes PDF, PPT and markdown.

## Build Your Own RAG bot

![RAG pipeline](../images/6_0.png)

## Notebook

- Files include:
  - PDF that includes complex tables
  - Powerpoint deck that contains information about the DoNUT model
  - Markdown file: README from DoNUT github repository
- Retrieval and Question Answering with Sources
  - [Deprecated since version 0.2.13](https://api.python.langchain.com/en/latest/chains/langchain.chains.qa_with_sources.loading.load_qa_with_sources_chain.html)
  - For version 0.2, check out the article: [RAG application to return sources](https://python.langchain.com/v0.2/docs/how_to/qa_sources/)
- Issues faced:
  - Metadata for few chunk documents have values which are not supported for a vector store.
  - **Solution**:
    - Use `filter_complex_metadata` to filter out these metadatas.
    - Sources:
      - [Deeplearning.ai course forum](https://community.deeplearning.ai/t/try-filtering-complex-metadata-from-the-document-using-langchain-community-vectorstores-utils-filter-complex-metadata/628474/3)
      - [LangChain discussion thread](https://github.com/langchain-ai/langchain/issues/8556)
- How are "sources" returned along with response?
  - [`combine_prompt`](https://github.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/chains/qa_with_sources/map_reduce_prompt.py) used in [`_load_map_reduce_chain`](https://api.python.langchain.com/en/latest/_modules/langchain/chains/qa_with_sources/loading.html) function uses prompt template mentioning `create a final answer with references ("SOURCES")`.
