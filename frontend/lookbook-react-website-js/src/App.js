import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

import Navbar from './components/Navbar';

import Home from './components/pages/HomePage';
import Services from './components/pages/ServicesPage';
import AboutUs from './components/pages/AboutUsPage';
import SignUp from './components/pages/SignUpPage';
import SignIn from './components/pages/SignInPage';

import Footer from './components/Footer';
import UserHome from './components/pages/UserHomePage';

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
          <Route exact path='/login' element={<SignIn/>} />
          <Route exact path='user-home' element={<UserHome/>} />
        </Routes>
        <Footer />
      </Router>
    </>
  );
}

export default App;