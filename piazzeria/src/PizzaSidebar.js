import React from 'react';
import './PizzaSidebar.css'; // Import your CSS file

const PizzaSidebar = ({ folders = ['a1', 'a2', 'a3'] }) => {
  return (
    <div className="pizza-sidebar">
      <ul>
        {folders.map(f => 
        <li className="no-bullets">
          <button className="pizza">{f}</button>
        </li>)}
      </ul>
    </div>
  );
};

export default PizzaSidebar;