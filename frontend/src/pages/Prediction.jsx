import { useState } from "react";
import api from "../api";
import "./Prediction.css";


export default function Prediction(){


const [data,setData] = useState({

    Fever:"No",

    Cough:"No",

    Fatigue:"No",

    Difficulty_Breathing:"No",

    Age:20,

    Gender:"Male",

    Blood_Pressure:"Normal",

    Cholesterol_Level:"Normal"

});


const [result,setResult] = useState("");

const [loading,setLoading] = useState(false);




function change(e){


setData({

    ...data,

    [e.target.name]:e.target.value

});


}






async function predict(){


try{


setLoading(true);


const res = await api.post(

    "/predict",

    data

);



console.log(res.data);



setResult(res.data.prediction);



}

catch(error){


console.log(error);


setResult(
    "AI service unavailable"
);


}

finally{


setLoading(false);


}


}








return(


<div className="prediction">


<h1>
🧬 Disease Prediction
</h1>



<div className="form-card">



<label>
Fever
</label>

<select

name="Fever"

value={data.Fever}

onChange={change}

>

<option value="Yes">
Yes
</option>

<option value="No">
No
</option>

</select>






<label>
Cough
</label>

<select

name="Cough"

value={data.Cough}

onChange={change}

>

<option value="Yes">
Yes
</option>

<option value="No">
No
</option>

</select>






<label>
Fatigue
</label>


<select

name="Fatigue"

value={data.Fatigue}

onChange={change}

>

<option value="Yes">
Yes
</option>

<option value="No">
No
</option>

</select>







<label>
Difficulty Breathing
</label>


<select

name="Difficulty_Breathing"

value={data.Difficulty_Breathing}

onChange={change}

>

<option value="Yes">
Yes
</option>

<option value="No">
No
</option>

</select>








<label>
Age
</label>


<input

type="number"

name="Age"

value={data.Age}

onChange={change}

/>








<label>
Gender
</label>


<select

name="Gender"

value={data.Gender}

onChange={change}

>

<option value="Male">
Male
</option>

<option value="Female">
Female
</option>


</select>









<label>
Blood Pressure
</label>


<select

name="Blood_Pressure"

value={data.Blood_Pressure}

onChange={change}

>


<option value="Normal">
Normal
</option>


<option value="High">
High
</option>


<option value="Low">
Low
</option>


</select>









<label>
Cholesterol Level
</label>


<select

name="Cholesterol_Level"

value={data.Cholesterol_Level}

onChange={change}

>


<option value="Normal">
Normal
</option>


<option value="High">
High
</option>


<option value="Low">
Low
</option>


</select>








<button

onClick={predict}

disabled={loading}

>


{

loading

?

"Analyzing..."

:

"Predict Disease"

}


</button>





</div>








{

result &&

<div className="result-card">


<h2>
Prediction Result
</h2>


<p>
🩺 {result}
</p>


</div>


}



</div>


)


}