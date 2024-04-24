import './App.css';
import About from './Pages/About';
import Contact from './Pages/Contact';
import Landing from './Pages/Landing';
import Shop from './Pages/Shop';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Routes>
         <Route path='/' element={<Landing/>} />
         <Route path='/About' element={<About/>} />
         <Route path='/Shop' element={<Shop/>} />
         <Route path='/Contact' element={<Contact />} />
       </Routes>
    </div>
  );
}

export default App;
