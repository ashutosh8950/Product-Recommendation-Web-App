import random
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.llms import OpenAI # Placeholder for any LLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# This is a mock setup for LangChain. In a real app, you'd have an API key.
# from dotenv import load_dotenv
# load_dotenv()
# llm = OpenAI(temperature=0.7)

app = FastAPI()

# Allow CORS for the React frontend to communicate with the backend
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Mock Data representing the dataset [cite: 10] ---
# This simulates data retrieved from a vector database query.
mock_db = [
    {
        "uniq_id": "a1", "title": "Ergonomic Oak Office Chair", "price": "$250",
        "description": "A stylish and comfortable chair made from sustainable oak.",
        "categories": ["Furniture", "Office"], "material": "Wood",
        "images": "https://i.imgur.com/example-chair.jpeg" # Placeholder image URL
    },
    {
        "uniq_id": "b2", "title": "Minimalist Steel Coffee Table", "price": "$180",
        "description": "A sleek and modern coffee table with a durable steel frame.",
        "categories": ["Furniture", "Living Room"], "material": "Metal",
        "images": "https://i.imgur.com/example-table.jpeg" # Placeholder image URL
    },
    {
        "uniq_id": "c3", "title": "Cozy Wool Area Rug", "price": "$300",
        "description": "A soft, hand-woven wool rug to add warmth to any room.",
        "categories": ["Home Decor", "Rugs"], "material": "Wool",
        "images": "https://i.imgur.com/example-rug.jpeg" # Placeholder image URL
    }
]

class UserPrompt(BaseModel):
    query: str

def mock_genai_description(product_title: str, user_query: str) -> str:
    """Simulates a call to a GenAI model using LangChain to generate a description[cite: 31]."""
    # In a real app, this would use the configured llm and chain.
    # prompt = PromptTemplate(template="Generate a creative, short description for a {product} based on the user's request for '{query}'.", input_variables=["product", "query"])
    # chain = LLMChain(llm=llm, prompt=prompt)
    # response = chain.run(product=product_title, query=user_query)
    # return response
    return f"Discover the '{product_title}', the perfect match for your search for '{user_query}'. It blends timeless design with modern functionality, creating a unique piece for your home."

@app.post("/recommend")
async def get_recommendations(prompt: UserPrompt):
    """
    This endpoint simulates a vector search and then generates a creative description.
    """
    # 1. Simulate a vector database search to find relevant products[cite: 32].
    retrieved_product = random.choice(mock_db)

    # 2. Use a simulated GenAI model to generate a creative description[cite: 31].
    generated_description = mock_genai_description(retrieved_product["title"], prompt.query)
    retrieved_product["generated_description"] = generated_description

    return {"recommendation": retrieved_product}

@app.get("/analytics")
async def get_analytics_data():
    """Provides mock data for the analytics page[cite: 8, 36]."""
    return {
        "total_products": len(mock_db),
        "avg_price": 243.33,
        "category_distribution": {"Furniture": 2, "Home Decor": 1}
    }