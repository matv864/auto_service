import First from "./firstpage";
import Second from "./2page";

import { useEffect, useState } from 'react';

// export const PopupCard = () => {
//   const [showCard, setShowCard] = useState(false);

//   useEffect(() => {
//     const timer = setTimeout(() => {
//       setShowCard(true);
//     }, 60000); // 60 секунд

//     return () => clearTimeout(timer);
//   }, []);

//   return (
//     showCard && (
//       <div className="fixed bottom-4 right-4 bg-orange-500 text-white p-4 rounded-lg shadow-lg">
//         <div className="text-black">
//           <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
//         </div>
//       </div>
//     )
//   );
// };


function Body() {
    return (
      <main class="flex-grow">
        <First/>
        <Second/>
      </main>

    );
  }
  
export default Body;


  