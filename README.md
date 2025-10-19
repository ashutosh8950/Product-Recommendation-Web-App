AI Furniture Recommender 🛋️
Hey! This is my submission for the intern assignment. I built this project over 2 days to create a full-stack app that uses AI to recommend furniture through a simple chat interface.

It was a fun challenge that involved combining a few different fields: a bit of machine learning, NLP, and a dash of generative AI, all wrapped up in a web app.

Here's a quick look at how it works:
(This is a great place to add a GIF of your app in action!)

What it Does (The Cool Parts) ✨
Conversational Search: Instead of clicking filters, you can just tell the app what you're looking for in plain English, like "I need a comfy chair for a small reading corner."

AI-Generated Descriptions: The app doesn't just show you a product; it uses a generative AI model to write a creative little description for it on the fly.

Modern Full-Stack Build: The frontend is a snappy React app, and the backend is powered by Python and FastAPI, which made building the API super fast.

Tech I Used 🛠️
Backend: Python, FastAPI

Frontend: React.js

AI Stuff: LangChain (for integrating the generative model)

Models (Simulated): The logic is set up to use models from HuggingFace for text and a CV model like ResNet for images.

Database (Simulated): The code simulates lookups from a vector database like Pinecone.

How It Works Under the Hood
The whole thing is pretty straightforward:

The React app (frontend) sends the user's chat message to the FastAPI server (backend).

The backend then does the AI magic: it pretends to search a vector database to find a matching product.

It then asks a GenAI model (simulated through LangChain) to write a cool description for that product based on the user's query.

Finally, it sends the product recommendation and the new description back to the frontend to be displayed in the chat.

Wanna Run It Locally? 🚀
It's pretty easy to get this running on your own machine.

1. Get the Backend Running:
Bash

# Go into the backend folder
cd backend

# Set up and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install the necessary libraries
pip install -r requirements.txt

# Start the server!
uvicorn main:app --reload
# It should now be running on http://127.0.0.1:8000
2. Get the Frontend Running:
(In a new terminal)

Bash

# Go into the frontend folder
cd frontend

# Install all the node modules
npm install

# Start the app
npm start
# It should open up in your browser at http://localhost:3000
What I Learned & What's Next
Building this in just two days was a great experience! Getting the chat UI to feel smooth and responsive was a fun challenge, and this was a great chance to really dive into using LangChain to connect different AI components.

If I had more time, here's what I'd do next:

Hook it up to a real database: Connect it to a real Pinecone instance instead of using mock data.

Image-based search: Let users upload a photo of furniture they like and find similar items.

Build out the analytics: Create a full, interactive dashboard for the analytics page.
