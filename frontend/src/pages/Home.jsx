import {Link} from "react-router-dom";
import "./Home.css";


export default function Home(){


return(

<div className="home">


<section className="hero">


<div>


<h1>
Healthcare Powered By
<br/>
Artificial Intelligence
</h1>


<p>
Netravaan AI is your smart healthcare assistant.
Predict diseases, analyze reports and consult AI doctor.
</p>



<div>


<Link to="/doctor">

<button>
Talk To AI Doctor
</button>

</Link>



<Link to="/prediction">

<button className="outline">
Get Started
</button>

</Link>


</div>



</div>




<Link 
to="/doctor"
className="assistant-link"
>


<div className="ai-card">


<div className="robot">
🤖 🩺
</div>


<h2>
Medinova AI
</h2>


<p>
24/7 Healthcare Assistant
</p>


<span>
Click to Chat
</span>


</div>


</Link>



</section>




<section className="features">


<h2>
Everything you need
</h2>



<div className="cards">



<div>

🧬

<h3>
Disease Prediction
</h3>

<p>
AI based health analysis
</p>

</div>




<div>

📄

<h3>
Report Analyzer
</h3>

<p>
Upload medical reports
</p>

</div>




<div>

🤖

<h3>
AI Doctor
</h3>

<p>
Ask health questions
</p>

</div>



</div>



</section>




</div>

)

}