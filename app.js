import React, { useState, useEffect, useRef } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const messageListRef = useRef(null);

  // Auto-scroll to the latest message
  useEffect(() => {
    if (messageListRef.current) {
      messageListRef.current.scrollTop = messageListRef.current.scrollHeight;
    }
  }, [messages]);
  
  // Greeting message on component mount
  useEffect(() => {
    setMessages([{ sender: 'bot', text: 'Hello! What kind of furniture are you looking for today?' }]);
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');

    // Fetch recommendation from backend
    try {
      const response = await fetch('http://127.0.0.1:8000/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: input }),
      });
      const data = await response.json();
      
      const botMessage = {
        sender: 'bot',
        product: data.recommendation
      };
      setMessages(prev => [...prev, botMessage]);

    } catch (error) {
      const errorMessage = { sender: 'bot', text: 'Sorry, I am having trouble connecting to the server.' };
      setMessages(prev => [...prev, errorMessage]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Furniture Recommender</h2>
      </div>
      <div className="message-list" ref={messageListRef}>
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}-message`}>
            <div className="message-bubble">
              {msg.text}
              {msg.product && (
                <div className="product-card">
                  <img src={msg.product.images} alt={msg.product.title} />
                  <h3>{msg.product.title}</h3>
                  <p><strong>Price:</strong> {msg.product.price}</p>
                  <p><strong>Material:</strong> {msg.product.material}</p>
                  <p><em>{msg.product.generated_description}</em></p>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
      <form className="chat-input-form" onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="e.g., a modern table for my living room"
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;