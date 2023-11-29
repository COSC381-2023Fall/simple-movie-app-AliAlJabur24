import './App.css';
import React, { useState } from 'react';


function App() {
  const [inputText, setInputText] = useState('');
  const [apiReponse, setApiReponse] = useState('');
  

  const HandleInput = (e) => {
    setInputText(e.target.value);
  };
  

  const handleSubmit = async () => {
    try{
      const response = await fetch(`http://127.0.0.1:8000/movies/${inputText}`);
      const data = await response.json();
      setApiReponse(data.name);
    }
    catch (error){
      console.log('Error Fetching Info:', error);
    }
  };

  return (
    <div className="App">
      <div className="centered">
        <input type="text" placeholder="Enter Movie ID"  value={inputText} onChange={HandleInput} />
        <button onClick={handleSubmit}> Find Movie </button>
        {apiReponse && <div>{JSON.stringify(apiReponse)}</div>}
      </div>
    </div>
  );
}

export default App;
