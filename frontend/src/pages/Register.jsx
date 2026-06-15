import {useState} from "react";

import {useNavigate} from "react-router-dom";

import api from "../api";   // adjust path if your api.js location is different


export default function Register(){


const nav = useNavigate();


const [data,setData] = useState({});



function register(){


api.post(

"/register",

data

)

.then(()=>{


alert("Registered");

nav("/login");


})


.catch((err)=>{

console.log(err);

alert("Registration failed");

});


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