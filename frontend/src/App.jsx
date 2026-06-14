import {BrowserRouter, Routes, Route} from "react-router-dom";

import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Doctor from "./pages/Doctor";
import Prediction from "./pages/Prediction";
import Report from "./pages/Report";
import Voice from "./pages/Voice";
import Register from "./pages/Register";


function App(){


return(

<BrowserRouter>


<Navbar/>

<Routes>

<Route path="/" element={<Home/>}/>

<Route 
path="/register"
element={<Register/>}
/>



<Route 
path="/doctor" 
element={<Doctor/>}
/>


<Route 
path="/prediction" 
element={<Prediction/>}
/>


<Route 
path="/report" 
element={<Report/>}
/>


<Route 
path="/voice" 
element={<Voice/>}
/>


</Routes>


</BrowserRouter>


)

}


export default App;