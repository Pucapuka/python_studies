package com.mycompany.animacao;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.Random;
import javax.swing.*;

public class Animacao extends JFrame
                      implements Runnable{
    Thread t;
    boolean exe = false;
    boolean rightMove = false; //move para a direita?
    boolean leftMove = false; //move para a esquerda?
    int a,s,v,z = 0; //a e s vai trabalhar o personagem, v e z, a vida
    int score = 0;
    int life = 3;
    int i = 250;//personagem
    int i2 = 800; //granada
    int i3 = 600; //granada
    int i4 = 400; //granada
    int j = 300;//personagem
    int j2 = 0; //granada
    int j3 = 0; //granada
    int j4 = 0; //granada
    int k = 0;
    int m = 0; //mover o cenário
    int l = 1; //para trabalhar os cenários
    int q = 24;
    Image[] imagem = new Image[13];
    ImageIcon[] icon = new ImageIcon[13];
    Image[] granada = new Image[1];
    ImageIcon[] granade = new ImageIcon[1];
    Image[] explosao = new Image[24];
    ImageIcon[] explosion = new ImageIcon[24];
    Image[] cenario = new Image[1];
    ImageIcon[] cen = new ImageIcon[1];
    Image[] vida = new Image[1];
    ImageIcon[] vid = new ImageIcon[1];
    Image[] morto = new Image[1];
    ImageIcon[] dead = new ImageIcon[1];
    int tempoDecorrido = 0;
    Timer faseTimer; //calcula o tempo da fase
    boolean faseCompleta = false; //a fase está completa?
    
    public void showNotify(){ //método para iniciar a animação
        t.start();
        exe = true;
    }
    
    public void hideNotify(){ //método para parar a animação
        exe = false;
        t = null;
    }

    

    public Animacao(){
        t = new Thread(this);
        setSize(800,500);
        setVisible(true);
        showNotify();
        
        for(int p = 7; p<=12; p++){
            icon[p] = new ImageIcon("C:\\Users\\lilin\\OneDrive\\Documentos\\"
                    + "NetBeansProjects\\animacao\\src\\sprite_"+p+".png");
            imagem[p] = icon[p].getImage();
        }
        
        dead[0] = new ImageIcon("C:\\Users\\lilin\\OneDrive\\Documentos\\"
                + "NetBeansProjects\\animacao\\src\\sprite_26.png");
        morto[0] = dead[0].getImage();
        
        granade[0] = new ImageIcon("C:\\Users\\lilin\\OneDrive\\Documentos\\"
                + "NetBeansProjects\\animacao\\src\\granada.png");
        granada[0] = granade[0].getImage();
        

        
        for(k=0; k<=2; k++){
            explosion[k] = new ImageIcon("C:\\Users\\lilin\\OneDrive\\Documentos\\"
                    + "NetBeansProjects\\animacao\\src\\explosao_"+k+".png");
            explosao[k] = explosion[k].getImage();
        }
       
        cen[0] = new ImageIcon("C:\\Users\\lilin\\OneDrive\\Documentos\\"
                + "NetBeansProjects\\animacao\\src\\cenario"+l+".png");
        cenario[0] = cen[0].getImage();
  
//colocando a imagem para as vidas que o personagem tem

        vid[0] = new ImageIcon("C:\\Users\\lilin\\OneDrive\\Documentos\\"
                + "NetBeansProjects\\animacao\\src\\vida.png");
        vida[0] = vid[0].getImage();

// Criando um Timer que atualiza o tempo decorrido a cada segundo
        faseTimer = new Timer(1000, new ActionListener() {
        @Override
       public void actionPerformed(ActionEvent e) {
                if (!faseCompleta) {
                    tempoDecorrido++;
                    if (tempoDecorrido >= 60) {
                        faseCompleta = true; // Marca a fase como completa
                    }
                }
            }
    });
         faseTimer.start(); // Inicia o Timer

//criando um Listener para as teclas utilizadas no jogo
 addKeyListener(new KeyAdapter() {  
    public void keyPressed(KeyEvent kp) {
           int keyP = kp.getKeyCode();
           
           if (keyP == KeyEvent.VK_LEFT) {
               leftMove = true;
           }else if (keyP == KeyEvent.VK_RIGHT) {
               rightMove = true;
           }
               
       }
       
       public void keyReleased (KeyEvent kr) {
           int keyR = kr.getKeyCode();
           
           if (keyR == KeyEvent.VK_LEFT) {
               leftMove = false;
           } else if (keyR == KeyEvent.VK_RIGHT) {
               rightMove = false;
           }
       }
});

}   
    
//Evento de colisão de objetos (personagem e granadas)
    public boolean collide(float x1,float y1, float w1, float h1, float x2,
        float y2, float w2, float h2){
        
        if(x1 + w1 > x2 && x1 < x2 + w2 && y1 + h1 > y2 && y1 < y2 + h2){
            return true;        }
        return false;
    }
            
        public void paint(Graphics g){
        g.setColor(Color.BLACK);
        g.drawLine(0, j, getWidth(), j);
        g.setColor(Color.WHITE);
        g.fillRect(10,10,getWidth(),getHeight()); //esse método preenche de branco de modo que "apague"  o desenho anterior, dando a ilusão de movimento.
        //g.setColor(new Color(k,l,m)); //para colorir o desenho em RGB, é preciso instanciar um objeto a partir da classe Color
        //g.setColor(Color.RED); //aí a cor fica só vermelha
        
// cenário
        g.drawImage(cenario[0], m, 0, this);
        //calculando a posição do cenário
        int x2 = m + cenario[0].getWidth(this);
        //fazendo uma cópia dele
        g.drawImage(cenario[0], x2, 0, this);
        g.drawImage(cenario[0], cenario[0].getWidth(this) - m, 0, this);
        
//número de vidas do personagem
        z = 50;
        for(v = 0; v < life; v++){
            g.drawImage(vida[0], z ,450-vida[0].getHeight(this), this);
            z += 50;
        }
        
//Score
    g.drawString("SCORE: "+score, 650, 450);
        
//Personagem
       //essa aqui e uma string para verificar a posição do personagem, só ativo ela quando quero verificar 
       // g.drawString("X = " + String.valueOf(i) + ", Y = " + String.valueOf(j), i - 50, j - 5 );

        g.drawImage(imagem[a], i, j, this);//personagem
        if(life<0){
            g.clearRect(i,j,imagem[a].getWidth(this), imagem[a].getHeight(this));
            g.drawImage(cenario[0], m, 0, this);
            g.drawImage(morto[s], i, j+50, this);
        }

//granadas
        //granadas fase 1
        g.drawImage(granada[0], i2-=10, j2+=10,this);
        //granadas fase 2 (adiciona uma)
        if (l == 2) {
            g.drawImage(granada[0], i3-=10, j3+=10,this);
        //granadas fase 3 (adiciona duas)
        } else if (l == 3) {
             g.drawImage(granada[0], i3-=10, j3+=10,this);
             g.drawImage(granada[0], i4-=10, j4+=10,this);
        }

//gerando animação da explosão , caso haja colisão de objetos
    //com a granada 1
        if (collide(i, j, imagem[a].getWidth(this), imagem[a].getHeight(this), i2, j2,
            granada[0].getWidth(this), granada[0].getHeight(this))) {
        g.clearRect(i2, j2, granada[0].getWidth(this), granada[0].getHeight(this));
        
        for (int frame = 0; frame < 24; frame++) {
            g.drawImage(explosao[frame], i2, j2, null);
            try {
                Thread.sleep(100); // tempo de espera, pode ser ajustado
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            repaint();
        }
        j2 = 0; //a granada volta pro topo da tela
        life --; //perde uma vida após a colisão
        score -= 300; //perde trezentos pontos por ser atingido
        if(score<0)   //evitando score negativo
            score=0;
}
        
    //com a granada 2
     if (collide(i, j, imagem[a].getWidth(this), imagem[a].getHeight(this), i3, j3,
            granada[0].getWidth(this), granada[0].getHeight(this))) {
        g.clearRect(i3, j3, granada[0].getWidth(this), granada[0].getHeight(this));
        
        for (int frame = 0; frame < 24; frame++) {
            g.drawImage(explosao[frame], i3, j3, null);
            try {
                Thread.sleep(100); // Adjust the sleep duration as needed
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            repaint();
        }
        j3 = 0;
        life --;
        score -= 300; //perde trezentos pontos por ser atingido
        if(score<0)
            score=0;
}
     
    //com a granada 3
    
    if (collide(i, j, imagem[a].getWidth(null), imagem[a].getHeight(null), i4, j4,
            granada[0].getWidth(null), granada[0].getHeight(null))) {
        g.clearRect(i4, j4, granada[0].getWidth(null), granada[0].getHeight(null));
        
        for (int frame = 0; frame < 24; frame++) {
            g.drawImage(explosao[frame], i4, j4, null);
            try {
                Thread.sleep(100); // Adjust the sleep duration as needed
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            repaint();
        }
        j4 = 0;
        life --;
        score -= 300; //perde trezentos pontos por ser atingido
        if(score<0)
            score=0;
}

        //g.drawString("X = " +String.valueOf(i)+ "Y = "+String.valueOf(j), a, a);
        //g.setColor(Color.BLACK);
        //g.drawLine(0, 371, getWidth(), 371);
        
//        if(j2==125 || j3 == 125 || j4 == 125){
//            q = 0;
//            for(q=0; q<24; q++){
//                q++;
//         }
//        }
    }
        
    public void picMove(){
        while(exe){
            //se a vida for menor que zero, GAME OVER
            if(life<0){  
                mostrarFimDeJogo();
            }
            //movendo cenário para trás
            m = (m - 1);
            //frame do personagem
            a++;
            //condicionais das granadas que passam
            if(j2==350){
                j2 = 0;
                score += 200; //ganha 200 pontos por não pegar a bomba
            }
             if (j3 == 350) {
                j3 = 0;
                score += 200; // ganha 200 pontos por não pegar a bomba
            }
            
             if (j4 == 350) {
                j4 = 0;
                score += 200; // ganha 200 pontos por não pegar a bomba
            }
            if(i2 < i){
                j2=0;
                i2 = new Random().nextInt(300,800);
                score += 200; //ganha 200 pontos por não pegar a bomba
            }
            
            if (i3 < i){
                j3=0;
                i3 = new Random().nextInt(300, 800);
                score += 200; // ganha 200 pontos por não pegar a bomba;
            }
            
            if(i4 < i){
                j4=0;
                i4 = new Random().nextInt(300,800);
                score += 200; //ganha 200 pontos por não pegar a bomba
            } 
            
            //trabalhando os movimentos
            
            if(leftMove){
                i -= 10;
            }else if(rightMove){
                i += 10;
            }
            
            try{
                Thread.sleep(300);
            }catch(Exception e){}
            repaint();
            if(a>=12)
                a=7;
            
            if (faseCompleta) {
                mostrarFimDaFase();
                if(l<3)
                    l++;
                else{
                    mostrarFimDeJogo();
                }
                faseCompleta = false;
                tempoDecorrido = 0;
                cen[0] = new ImageIcon("C:\\Users\\lilin\\OneDrive\\Documentos\\"
                + "NetBeansProjects\\animacao\\src\\cenario"+l+".png");
                cenario[0] = cen[0].getImage();
            }
            
        }
    }
    
    
     private void mostrarFimDaFase() {
        // Exibe a mensagem de "Fase Completa"
        JOptionPane.showMessageDialog(this, "Fase Completa", "Fim da Fase", JOptionPane.INFORMATION_MESSAGE);
     }
     
     private void mostrarFimDeJogo(){
         JOptionPane.showMessageDialog(this, "GAME OVER\nSCORE: "+score, "Fim de Jogo",JOptionPane.INFORMATION_MESSAGE);
         System.exit(0);
     }


    public static void main(String[] args) {
        Animacao a = new Animacao();
        a.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
    }
    
 @Override
    public void run(){
 
        while(exe){
           picMove();
           hideNotify();
        
    }
  }

    private int getHeight(Image[] granada) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}