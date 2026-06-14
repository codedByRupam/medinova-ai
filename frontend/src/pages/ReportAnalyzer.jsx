import {useState} from "react";
import api from "../api";
import "./ReportAnalyzer.css";



export default function ReportAnalyzer(){


const [file,setFile]=useState(null);

const [data,setData]=useState(null);

const [loading,setLoading]=useState(false);



const uploadReport=async()=>{


if(!file)return;


let form=new FormData();

form.append(
"file",
file
);



setLoading(true);



try{


const res=await api.post(

"/report",

form

);



setData(res.data.analysis);



}

catch(e){

alert(
"Report upload failed"
);

}



setLoading(false);


}





return(


<div className="report-page">


<h1>
🩺 Medical Report Analyzer
</h1>


<p>
Upload your medical report and get an easy explanation
</p>



<div className="upload-box">


<input

type="file"

accept=".pdf"

onChange={
e=>setFile(e.target.files[0])
}

/>


<button onClick={uploadReport}>

Analyze Report

</button>


</div>





{
loading &&

<h3>
Analyzing report...
</h3>

}






{
data &&


<div className="report-card">



<section className="summary">

<h2>
📝 Summary
</h2>

<p>

{data.summary}

</p>

</section>





<details>


<summary>

🔍 Key Findings

</summary>



<ul>

{

data.findings.map(

(item,i)=>

<li key={i}>

{item}

</li>


)

}

</ul>



</details>







<details>


<summary>

⚠️ Possible Concerns

</summary>



<ul>

{

data.concerns.map(

(item,i)=>

<li key={i}>

{item}

</li>


)

}

</ul>



</details>






<details>


<summary>

✅ Health Advice

</summary>



<ul>

{

data.advice.map(

(item,i)=>

<li key={i}>

{item}

</li>


)

}

</ul>



</details>




<div className="warning">


⚕️ AI generated information only.
Always consult a healthcare professional.

</div>



</div>


}





</div>


)


}