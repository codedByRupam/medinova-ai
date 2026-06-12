import {useEffect,useState} from "react";
import api from "../utils/api";


export default function Profile(){


const [user,setUser]=useState(null);



useEffect(()=>{


api.get("/profile")

.then(res=>{

setUser(res.data)

})


},[])




return(

<div>


<h1>
Patient Profile
</h1>


{

user &&

<div>


<h2>
{user.name}
</h2>


<p>
{user.email}
</p>


</div>

}



</div>

)

}