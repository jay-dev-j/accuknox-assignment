# Assignment 2 - Q3: Vector Database

A vector database is a database which stores and searches for data in the form of vectors.

A vector is a numeric representation of data including text images or documents.

## Process

First, the data is converted into vectors using an embedding model. These type of vectors are stored in a vector database.
When the user gives a query, the query is converted into a vector form. This database performs the search for similar vectors and delivers relevant data.

## Example

Let us consider that I am creating a chatbot that would answer
questions using the company documents.

Firstly, I convert the company documents into vectors and keep all in a vector database. When the user gives a question, it is converted into a vector. Using this, the vector database retrieves similar data and shares the data with the
LLM. Now the LLM uses that data to generate the best response.

## Vector Database i would choose

In this scenario, I would prefer using ChromaDB.
I have chosen ChromaDB because of its very easy implementation through Python and it is suitable for projects like this where learning can take place. It is capable of storing embeddings and performing similarity searches to find most relevant information.