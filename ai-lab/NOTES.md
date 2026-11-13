## 1. Simple LLM Call
simple llm call to gemini made via google's genai module

## 2. Memory: Maintaining history
we send the whole conversation ourselves to the follow up request

## 3. Embeddings
have a embedding model which converts the text into vectors(numbers) 

## 4. Semantic Search
Embed every text into vectors and store them in vector db. Search them via scores

## 5. Chroma DB
Create collection, append documents with ids, embeddings(vectors), metadata as a record. Query the texts matching the input text by vectors

## 6. RAG
1. Retrive the related context from vectorDB 
2. Augment the retrived context to the input prompt
3. Generate the response from llm by sending the prompt

## 7. LangChain
langchain is a wrapper that is used to streamline the complex workflows
- Having a prompt template for reusing the common template for dynamic inputs
- making a chain like flow input -> prompt_template -> llm
- structured output from llm, getting a structured python object instead of plain text

## 8. LangGraph 
steps (nodes) + shared state (memory) + rules for what runs next (edges and conditional edges)