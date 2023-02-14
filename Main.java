public class Main {
  String cor = "branca";
  float comprimento = 2.3f;
  float largura = 0.75f;
  String material = "MDF";
  boolean aberta = false;
  String estado = "fechada";
  
  void abrir(){
  	aberta = true;
  }
  
  void fechar(){
  	aberta = false;
  }
  
  String mostrarEstado(String estado){
  	if (aberta = true){
    	estado = "aberta";
        }else{
        	estado = "fechada";
             }
    return estado;
  }

}
