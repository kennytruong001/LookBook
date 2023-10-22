import React, {useState} from 'react'
import { useSearchParams } from 'react-router-dom'
import { SearchBar } from "../SearchBar";
import { SearchResultsList } from "../SearchResultsList";


export default function UserHome(data) {
  const [results, setResults] = useState([]);
  //const { username, password, schedule } = data.match.params;

  return (
    <>
      <h1 className='user-home' href="/user-home">
        <SearchBar setResults={setResults} />
        {results && results.length > 0 && <SearchResultsList results={results} />}
      </h1> 

      <table>
        <thead>
          <tr>
            <th>Sunday</th>
            <th>Mondday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
            <th>Saturday</th>
          </tr>
        </thead>
      </table>
    </>
  )
}