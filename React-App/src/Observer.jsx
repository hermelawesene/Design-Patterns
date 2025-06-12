import { useState, useEffect } from 'react';

function Observer() {
   const [count, setCount] = useState(0); // Observable state

  // Observer component that reacts to count changes
  useEffect(() => {
    console.log(`Count changed to: ${count}`);
  }, [count]); // Dependency array specifies what to observe

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}

export default Observer