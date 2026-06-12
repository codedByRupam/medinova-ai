import {Link} from "react-router-dom";

import {
FaHeartbeat,
FaFileMedical,
FaMicrophone
} from "react-icons/fa";

import "./Dashboard.css";


export default function Dashboard(){


return (

<div>


<Navbar/>


<section className="hero">


<h1>
Welcome to Netravaan AI 🩺
</h1>


<p>
Your Personal AI Healthcare Assistant
</p>



<div className="cards">



<Link to="/prediction" className="card">


<FaHeartbeat size={45}/>

<h2>
Disease Prediction
</h2>


<p>
AI powered health analysis
</p>


</Link>





<Link to="/report" className="card">


<FaFileMedical size={45}/>


<h2>
Medical Reports
</h2>


<p>
Upload and analyze reports
</p>


</Link>





<Link to="/voice" className="card">


<FaMicrophone size={45}/>


<h2>
Voice Assistant
</h2>


<p>
Talk with AI doctor
</p>


</Link>



</div>


</section>


</div>


)


}