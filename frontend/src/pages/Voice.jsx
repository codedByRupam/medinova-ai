import axios from "axios";


export default function Voice(){


function talk(){


axios.get(

"http://localhost:8000/voice"

)

.then(res=>{


alert(res.data.answer);


})


}



return(

<div className="hero">


<h1>

🎤 AI Voice Doctor

</h1>


<div className="card">


<button onClick={talk}>

Start Voice Assistant

</button>


</div>


</div>

)


}