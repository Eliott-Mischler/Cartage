document.getElementById("buttonPrenom").addEventListener("click", prenomEdit);

function prenomEdit(){
  document.getElementById("prenom").style.display = "none";
  document.getElementById("buttonPrenom").style.display = "none";
  document.getElementById("formPrenom").style.display = "block";
}
document.getElementById("buttonNom").addEventListener("click", nomEdit);

function nomEdit(){
  document.getElementById("nom").style.display = "none";
  document.getElementById("buttonNom").style.display = "none";
  document.getElementById("formNom").style.display = "block";
}
document.getElementById("buttonAdress").addEventListener("click", adressEdit);

function adressEdit(){
  document.getElementById("adress").style.display = "none";
  document.getElementById("buttonAdress").style.display = "none";
  document.getElementById("formAdress").style.display = "block";
}
document.getElementById("buttonMail").addEventListener("click", mailEdit);

function mailEdit(){
  document.getElementById("mail").style.display = "none";
  document.getElementById("buttonMail").style.display = "none";
  document.getElementById("formMail").style.display = "block";
}
document.getElementById("buttonPhone").addEventListener("click", phoneEdit);

function phoneEdit(){
  document.getElementById("phone").style.display = "none";
  document.getElementById("buttonPhone").style.display = "none";
  document.getElementById("formPhone").style.display = "block";
}
document.getElementById("buttonCar").addEventListener("click", carEdit);

function carEdit(){
  document.getElementById("car").style.display = "none";
  document.getElementById("buttonCar").style.display = "none";
  document.getElementById("formCar").style.display = "block";
}
document.getElementById("buttonHours").addEventListener("click", hoursEdit);

function hoursEdit(){
  document.getElementById("p_hours").style.display = "none";
  document.getElementById("buttonHours").style.display = "none";
  document.getElementById("formHours").style.display = "block";
}
document.getElementById("buttonPassword").addEventListener("click", passwordEdit);

function passwordEdit(){
  document.getElementById("formPassword").style.display = "block";
  document.getElementById("buttonPassword").style.display = "none";
}