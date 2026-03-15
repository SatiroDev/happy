function abrirImagem(src){
    document.getElementById("modal").style.display = "flex"
    document.getElementById("img-grande").src = src
}

function fecharImagem(){
    document.getElementById("modal").style.display = "none"
}