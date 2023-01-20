let optionBtn = document.getElementsByClassName('optionBtn')

for(i in optionBtn){
    optionBtn[i].addEventListener('click', function(e){
        let  option =(e.currentTarget.id).toString().split("_")
        let question = (option[0])
        let choice = option[1]
        let user = option[2]

        axios.post('http://127.0.0.1:8000/api/votes/', {
            VQuestion:`${question}`,
            Result: choice,
            User: user
          })
          .then(function (response) {
            if(response.data['already']){
              window.alert('you can vote only one time')
            }
            else{
              document.location.reload(true)
            }
          })
          .catch(function (error) {
            console.log(error);
          });
        
    })
}


