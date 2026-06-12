import {useState} from "react";
import api from "../api";
import "./Doctor.css";


export default function Doctor(){


const [msg,setMsg]=useState("");

const [chat,setChat]=useState([]);



async function send(){


let res=await api.post("/chat",
{
message:msg
});


setChat([
...chat,
{
user:msg,
bot:res.data.response
}
]);


setMsg("");

}




return(


<div className="doctor">


<h1>
🤖 AI Doctor
</h1>


<div className="chatbox">


{
chat.map((c,i)=>(

<div key={i}>


<p className="user">
You:
{c.user}
</p>


<p className="bot">
AI Doctor:
{c.bot}
</p>



</div>


))

}



</div>




<input

value={msg}

onChange={(e)=>setMsg(e.target.value)}

placeholder="Ask your health question"

/>


<button onClick={send}>
Send
</button>



</div>


)


}