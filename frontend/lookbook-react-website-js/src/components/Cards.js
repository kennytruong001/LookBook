import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

function Cards() {
  return (
    <div className='cards'>
      <h1>Check out these services around your area!</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src='images/img-1.jpg'
              text="Search for local barbershops for men's haircuts"
              label='Haircuts'
              path='/services'
            />
            <CardItem
              src='images/img-2.png'
              text='Book a manicure appointment'
              label='Manicures/Pedicures'
              path='/services'
            />
          </ul>
          <ul className='cards__items'>
            <CardItem
              src='/images/img-3.jpg'
              text='Find a tattoo artist'
              label='Tattoo'
              path='/services'
            />
            <CardItem
              src='/images/img-4.jpg'
              text='Look for a masseuse for a relaxing massage'
              label='Massage'
              path='/products'
            />
            <CardItem
              src='/images/img-5.jpg'
              text='Meet with local wedding planners'
              label='Wedding'
              path='/sign-up'
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;