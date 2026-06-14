import { useState } from "react";
import api from "../api";
import ReactMarkdown from "react-markdown";
import "./DoctorChat.css";


export default function DoctorChat() {


const [message,setMessage] = useState("");

const [loading,setLoading] = useState(false);



const [chats,setChats] = useState([

{
sender:"ai",
text:
`
## 👋 Welcome to Medinova AI Doctor

I am your healthcare assistant.

You can ask me about:

• Symptoms  
• Health questions  
• Medical reports  
• General health advice  

How can I help you today?
`
}

]);





const sendMessage = async()=>{


if(!message.trim()) return;



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



setChats(prev=>[

...prev,

{

sender:"ai",

text:
response.data.response || 
response.data.message

}

]);



}

catch(error){


console.log(error);



setChats(prev=>[

...prev,

{

sender:"ai",

text:
`
⚠️ Sorry, I cannot connect to Medinova AI right now.

Please try again.
`

}

]);


}



setLoading(false);



};





return(


<div className="doctor-page">


<div className="doctor-card">



{/* HEADER */}

<div className="doctor-header">


<div className="doctor-avatar">

🤖

</div>


<div>

<h2>
Medinova AI Doctor
</h2>

<p>
Your personal healthcare assistant
</p>

</div>


</div>





{/* CHAT AREA */}


<div className="chat-box">


{

chats.map((chat,index)=>(


<div

key={index}

className={

chat.sender==="user"

?

"user-message"

:

"ai-message"

}


>


<div className="message-icon">


{

chat.sender==="user"

?

"👤"

:

"🤖"

}


</div>




<div className="message-text">


<ReactMarkdown>

{chat.text}

</ReactMarkdown>


</div>



</div>



))


}




{

loading &&

<div className="typing">

🤖 Medinova AI is thinking...

</div>


}



</div>





{/* INPUT */}


<div className="input-section">


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

Send ➤

</button>



</div>




</div>


</div>


)



}