# Weaviate Tutorial: Getting Started with Semantic Search and Beyond 🤖

Weaviate is an open-source, GraphQL and RESTful API-based vector search engine that allows you to build semantic search and AI-powered applications easily. It integrates seamlessly with machine learning models to generate and manage vector embeddings, enabling fast and powerful similarity searches. This guide will walk you through the process of setting up Weaviate, from installation to creating your first index and running semantic searches, all in a friendly and approachable manner.

## Table of Contents
1. What is Weaviate?
2. Why Use Weaviate?
3. Installing Weaviate
4. Setting Up Your First Schema
5. Adding Data to Weaviate
6. Running Semantic Queries
7. Using Modules for Extra Power
8. Best Practices and Advanced Features

---

## 1. What is Weaviate? 🌐

Weaviate is a **vector search engine** that supports **semantic search** through a flexible, schema-based approach. It allows you to store data objects as vectors and enables similarity searches over those vectors. Imagine you have text documents, images, or other types of data that can be converted into embeddings; Weaviate allows you to search those embeddings by **meaning**, not just exact keyword matches.

**Core Features**:
- **Schema-Based**: Define custom classes, properties, and relations to structure your data.
- **Integrated ML Models**: Use built-in or custom machine learning models to generate embeddings automatically.
- **Flexible Search API**: Supports **GraphQL** and **REST APIs** for searching data.

## 2. Why Use Weaviate? 🧐

- **Semantic Search Made Simple**: Weaviate is perfect if you want to go beyond simple keyword searches and enable semantic similarity search.
- **Schema Flexibility**: Unlike traditional databases, you can define rich data types and relationships between entities.
- **Extensible with Modules**: Integrate with pre-trained models (e.g., **OpenAI**, **Hugging Face**) to automatically generate embeddings.
- **Scalable**: Easily scale to handle millions of objects and queries.

## 3. Installing Weaviate 🛠

Weaviate can be installed locally using Docker, which is the simplest way to get started.

### Step 1: Install Docker
If you haven't already, install Docker by following the instructions [here](https://docs.docker.com/get-docker/).

### Step 2: Run Weaviate with Docker
Weaviate provides an official Docker image that you can use to get up and running in minutes.

```bash
docker run -d \
  -p 8080:8080 \
  -e QUERY_DEFAULTS_LIMIT=25 \
  -e AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=true \
  -e PERSISTENCE_DATA_PATH="./data" \
  semitechnologies/weaviate:latest
```

This command runs Weaviate on **port 8080** and enables anonymous access for testing purposes. In a production environment, be sure to set up secure access controls.

## 4. Setting Up Your First Schema 🔢

Weaviate uses schemas to define how your data is organized. A schema is like a blueprint for your data—it defines what classes (like “Article” or “Product”) exist, and what properties each class has.

### Step 1: Define a Schema Class
To create a schema class, we’ll use Weaviate's GraphQL API to define a new class named **Article**.

- **Class Name**: `Article`
- **Properties**: `title` (text), `content` (text), `author` (text), `publication_date` (date)

```graphql
mutation {
  addClass(schema: {
    class: "Article",
    properties: [
      {
        name: "title"
        dataType: ["text"]
      },
      {
        name: "content"
        dataType: ["text"]
      },
      {
        name: "author"
        dataType: ["text"]
      },
      {
        name: "publication_date"
        dataType: ["date"]
      }
    ]
  })
}
```

This GraphQL mutation adds a new class called `Article` to your schema, making it ready to hold article objects.

## 5. Adding Data to Weaviate 📂

Once your schema is set up, you can add data (or “objects”) to Weaviate. This can be done via the REST API or GraphQL.

### Adding an Article Object
Let's add an article with a title, content, author, and publication date.

```graphql
mutation {
  AddArticle(
    content: {
      title: "The Future of AI",
      content: "Artificial Intelligence is rapidly evolving...",
      author: "Jane Doe",
      publication_date: "2023-11-01T00:00:00Z"
    }
  ) {
    title
    author
  }
}
```

Once added, this data can be searched using Weaviate's semantic capabilities.

## 6. Running Semantic Queries 🔎

The real magic of Weaviate lies in its ability to find objects based on their meaning. Instead of traditional keyword matching, you can query the index for semantically similar content.

### Example Query for Similar Articles
Let’s say you want to find articles similar to a specific query:

```graphql
{
  Get {
    Article(nearText: {
      concepts: ["advancements in AI"]
    }) {
      title
      author
      publication_date
    }
  }
}
```

In this example, Weaviate will look for articles that match the concept “advancements in AI,” even if those exact words don’t appear in the data.

## 7. Using Modules for Extra Power 🎉

Weaviate is super extensible, thanks to **modules**. These modules let you plug in pre-trained machine learning models to enrich your data. Here are some popular modules:

- **Transformers**: Use a transformer model like BERT to generate vector embeddings on-the-fly.
- **Q&A Module**: Enable question-answering capabilities by pulling answers directly from your documents.
- **OpenAI Integration**: Connect Weaviate with OpenAI’s models to enrich your dataset with contextual embeddings.

### Adding the Transformers Module
When running Weaviate with Docker, you can add a transformer module to automatically generate vector embeddings.

```bash
docker run -d \
  -p 8080:8080 \
  -e QUERY_DEFAULTS_LIMIT=25 \
  -e AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=true \
  -e PERSISTENCE_DATA_PATH="./data" \
  -e TRANSFORMERS_INFERENCE_API="sentence-transformers/all-MiniLM-L6-v2" \
  semitechnologies/weaviate:latest
```

This setup uses a pre-trained transformer model to automatically create embeddings for your text properties.

## 8. Best Practices and Advanced Features 💡

### Schema Design
- **Choose Data Types Wisely**: Weaviate supports different data types (`text`, `number`, `boolean`, etc.). Choosing the right type improves search efficiency.
- **Use Relationships**: If you have related data, like an article belonging to a category, consider using **references** to create relationships between classes.

### Index Configuration
- **Vectorizer Selection**: Choose a vectorizer that makes sense for your data. For text, transformers like **BERT** or **GPT** can generate context-aware embeddings.
- **Data Sharding**: For larger datasets, consider **sharding** to split data across multiple nodes and improve performance.

### Optimize Queries
- **Use Filters**: Add filters to queries to narrow down the search scope and improve performance.
- **Limit Results**: Use the `limit` parameter to reduce the number of results, which can speed up response time.

### Monitor with Weaviate Console
Weaviate offers a **console UI** for easy monitoring of your schema, indexes, and active queries. This is super helpful when debugging or optimizing the system.

## Final Thoughts 🤓
Weaviate offers a powerful, flexible way to perform semantic searches over your data without the complexities of building and maintaining vector indexes manually. Whether you're developing a recommendation system, an intelligent search engine, or a Q&A bot, Weaviate's capabilities can greatly simplify the process.

This tutorial covers the essentials to get you started, but there's a lot more to explore! Modules, advanced relationships, data validation, and scaling strategies can help you take your application to the next level. Dive in, experiment, and build amazing things with Weaviate!

If you need further assistance or more detailed guidance, the [official Weaviate documentation](https://weaviate.io/docs) is an excellent resource to dive deeper.