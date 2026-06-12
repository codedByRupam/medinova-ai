import {useState} from "react";

import axios from "axios";

import {useNavigate} from "react-router-dom";



export default function Register(){


const nav=useNavigate();


const [data,setData]=useState({});


function register(){


axios.post(

"http://localhost:8000/register",

data

)

.then(()=>{


alert("Registered");

nav("/login");


})


}




return(

<div className="auth">


<h1>
Create Account
</h1>


<input
placeholder="Name"
onChange={
e=>setData({...data,name:e.target.value})
}
/>



<input
placeholder="Email"
onChange={
e=>setData({...data,email:e.target.value})
}
/>



<input

type="password"

placeholder="Password"

onChange={
e=>setData({...data,password:e.target.value})
}

/>


<button onClick={register}>

Register

</button>



</div>


)

}