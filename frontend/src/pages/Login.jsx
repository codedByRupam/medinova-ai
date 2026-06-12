import {useState} from "react";
import {useNavigate} from "react-router-dom";
import api from "../api";


export default function Login(){


const navigate=useNavigate();


const [email,setEmail]=useState("");

const [password,setPassword]=useState("");



async function login(){


try{


const res = await api.post(
"/login",
{
email,
password
}
);



localStorage.setItem(
"token",
res.data.token
);



navigate("/");



}
catch(err){


alert("Login failed");


}



}



return(


<div className="auth">


<h1>
Medinova AI
</h1>



<input

placeholder="Email"

onChange={(e)=>setEmail(e.target.value)}

/>



<input

placeholder="Password"

type="password"

onChange={(e)=>setPassword(e.target.value)}

/>



<button onClick={login}>

Login

</button>



</div>



)


}