import {Link,useNavigate} from "react-router-dom";
import "./Navbar.css";


export default function Navbar(){


const navigate = useNavigate();



function logout(){


localStorage.removeItem("token");


navigate("/");


window.location.reload();


}



return(


<nav>


<h2>

🌿 Medinova AI

</h2>



<div>


<Link to="/">
Home
</Link>



<Link to="/doctor">
🤖 AI Doctor
</Link>



<Link to="/prediction">
🧬 Prediction
</Link>



<Link to="/report">
📄 Reports
</Link>



<Link to="/voice">
🎙 Voice
</Link>



<button onClick={logout}>

Logout

</button>



</div>


</nav>



)


}