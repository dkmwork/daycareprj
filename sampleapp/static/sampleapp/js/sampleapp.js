jQuery(document).ready(function(){
    jQuery('.select2').select2({
        width:'400px'
    })
    jQuery('.datepicker').datepicker();
// check dupliate 'class name' in class form 

function validate_contact(arg){
    var phone_no=arg
    var phone = jQuery.trim(phone_no)
    intRegex = /^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/
    if ((intRegex.test(phone)==false)){
        alert('Please enter a valid contact number')
    }
}
function validate_email(arg){
    var email=arg
    var re = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ((re.test(email)==false)){
        alert("Please enter a valid email address")
    }
}
jQuery('#id_contact_no').blur(function(){
    
    var contact= jQuery(this).val()
    validate_contact(contact)
})

jQuery('#id_student_email').blur(function(){

    var email = jQuery(this).val()
    validate_email(email)

})

jQuery('#id_teachers_email').blur(function(){
    
    var email = jQuery(this).val()
    validate_email(email)
})

// jQuery('#id_student_dob').change(async function(){

//     dob=jQuery(this).val()
//     console.log(dob.getFullYear())
//     const response = await fetch(`check_class/${dob}`,{
//         method: 'get'
//     })
//     const body = await response.json()
//     console.log(body)
    
// })

jQuery('#id_student_dob').change(function(){
    
    
    dob = jQuery(this).val()
    jQuery.ajax({
        type:'GET',
        url:'check_class',
        data:{
            student_dob:dob
        },
        success:function(response){
            
            //console.log(response.class_name)
            jQuery('#id_student_class option').each(function(){
                if (jQuery(this).text()==response.class_name){
                    jQuery(this).prop('selected','selected')
                }
                
            })
            var options = jQuery('#id_student_class option');
            for (var i=0; i<options.length;i++) {
                if (options[i].text !=response.class_name){
                    
                    options[i].disabled = true;
                }
                
              }
           
            
        }
    })
})

jQuery('#id_class_name').change(async function(){
    current_class = jQuery(this).val()
    const response = await fetch(`check_duplicate1/${current_class}`, {
            method: 'get'
            // headers: {
            //     'Content-Type': 'application/json',
            //     'Authorization': "Bearer "+ mytoken
            // }
        })
        const body =await response.json()
        if (body!=0){
            alert(current_class + " already exists !!!")
        }
        console.log(body)
})
// jQuery('#id_class_name').change(function(){
//     current_class = jQuery(this).val()
//     jQuery.ajax({
//         type:'GET',
//         url:'check_duplicate',
//         data:{
//             classname:current_class,
//         },
//         success:function(response){
//             console.log(response)
//             if (response!=0){
//                 alert (current_class + " already exists !!!")
//                 jQuery('#id_class_name').val('')
//             }
//         }
//     })
// })

jQuery('#id_classname').change(function(){
    current_class = jQuery(this).val()
    jQuery.ajax({
        type:"GET",
        url:"select_student",
        data:{
            classname:current_class,
        },
        success:function(response){
            console.log(response)
        }
    })
})


})