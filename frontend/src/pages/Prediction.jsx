import {useState} from "react";
import api from "../api";
import "./Prediction.css";


export default function Prediction(){


const [data,setData]=useState({

Fever:0,
Cough:0,
Fatigue:0,
Difficulty_Breathing:0,
Age:20,
Gender:0,
Blood_Pressure:120,
Cholesterol_Level:200,
Outcome_Variable:0

});


const [result,setResult]=useState("");



function change(e){

setData({

...data,

[e.target.name]:e.target.value

})


}



async function predict(){


let res=await api.post(
"/predict",
data
);


setResult(
res.data.predicted_disease
);



}





return(

<div className="prediction">


<h1>
🧬 Disease Prediction
</h1>



{
Object.keys(data).map((x)=>(


<input

key={x}

name={x}

placeholder={x}

onChange={change}

/>



))


}



<button onClick={predict}>
Predict
</button>



<h2>
{result}
</h2>


</div>


)


}