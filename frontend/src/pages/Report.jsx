import {useState} from "react";
import api from "../api";
import "./Report.css";


export default function Report(){


const [file,setFile]=useState(null);

const [result,setResult]=useState("");



async function upload(){


let form=new FormData();

form.append(
"file",
file
);



let res=await api.post(
"/upload-report",
form
);


setResult(
res.data.analysis
);



}




return(

<div className="report">


<h1>
📄 Medical Report Analyzer
</h1>



<input

type="file"

onChange={(e)=>setFile(e.target.files[0])}

/>



<button onClick={upload}>
Analyze Report
</button>



<p>

{result}

</p>



</div>


)

}