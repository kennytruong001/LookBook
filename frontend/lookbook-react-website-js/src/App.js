import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

import Navbar from './components/Navbar';

import Home from './components/pages/Home';
import Services from './components/pages/Services';
import AboutUs from './components/pages/AboutUs';
import SignUp from './components/pages/SignUp';

import Footer from './components/Footer';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route exact path='/' element={<Home/>} />
          <Route exact path='/services' element={<Services/>} />
          <Route exact path='/about-us' element={<AboutUs/>} />
          <Route exact path='/sign-up' element={<SignUp/>} />
        </Routes>
        <Footer />
      </Router>
    </>
  );
}

export default App;