$(document).ready(function () {
    $("#showHide").on("click", function(e){
      e.preventDefault()
      $("#icon").toggleClass("fa-eye")
    
      if($("#id_password, #id_password2, #id_current_password").attr("type") === "password"){
        $("#id_password, #id_password2, #id_current_password").attr("type", "text")
      }
      else{
        $("#id_password, #id_password2, #id_current_password").attr("type", "password")
      }
    });

});

let profileDropdownList = document.querySelector(".profile-dropdown-list");
let btn = document.querySelector(".profile-dropdown-btn");

let classList = profileDropdownList.classList;

const toggle = () => classList.toggle("active");

window.addEventListener("click", function (e) {
  if (!btn.contains(e.target)) classList.remove("active");
});


