class Second {
  public static void main(String[] args) {
    Main porta = new Main();
    System.out.println("No consultório farmacêutico tem uma porta " + porta.cor + ", " + porta.comprimento + " x " + porta.largura + ", feita de " + porta.material + ".");
    
    System.out.println("No momento, a porta se encontra " + porta.estado + ".");
    System.out.println("Vamos mudar isso?");
    porta.abrir();
    porta.mostrarEstado(porta.estado);
    System.out.println("Agora a porta está " + porta.estado + ".");
    System.out.println("Vamos mudar isso?");
    porta.fechar();
    porta.mostrarEstado(porta.estado);
    System.out.print("Agora a porta está " + porta.estado + ".");
  }
}
