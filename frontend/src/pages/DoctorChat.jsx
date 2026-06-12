import {useState} from "react";
import api from "../api";
import "./DoctorChat.css";


export default function DoctorChat(){


const [message,setMessage]=useState("");

const [loading,setLoading]=useState(false);



const [chats,setChats]=useState([

{
sender:"ai",
text:"Hello 👋 I am Netravaan AI Doctor. How can I help you today?"
}

]);




const sendMessage = async()=>{


if(!message) return;



const userMessage={

sender:"user",

text:message

};



setChats(prev=>[

...prev,

userMessage

]);



setMessage("");

setLoading(true);



try{


const response = await api.post(

"/chat",

{

message:userMessage.text

}

);



setTimeout(()=>{


setChats(prev=>[

...prev,

{

sender:"ai",

text:response.data.response

}

]


);


setLoading(false);



},1000);



}


catch(error){


setChats(prev=>[

...prev,

{

sender:"ai",

text:"Sorry, unable to connect with AI doctor"

}

]);


setLoading(false);


}



};





return(


<div className="doctor-container">


<div className="doctor-header">


<div className="avatar">

🩺

</div>


<div>

<h2>
Netravaan AI Doctor
</h2>

<p>
Healthcare Assistant
</p>

</div>


</div>





<div className="chat-box">


{

chats.map((chat,index)=>(


<div

key={index}

className={

chat.sender==="user"

?

"user-msg"

:

"ai-msg"

}


>


{

chat.sender==="ai" &&

<span>
🤖
</span>

}


{chat.text}


</div>


))


}



{

loading &&

<div className="typing">

AI Doctor typing...

</div>


}




</div>





<div className="input-area">


<input


value={message}


onChange={(e)=>
setMessage(e.target.value)
}


placeholder="Ask your health question..."



onKeyDown={(e)=>{

if(e.key==="Enter")

sendMessage()

}}



/>



<button onClick={sendMessage}>

Send

</button>



</div>





</div>



)


}